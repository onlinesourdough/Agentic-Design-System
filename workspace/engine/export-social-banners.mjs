import { spawn } from "node:child_process";
import {
  existsSync,
  mkdtempSync,
  readFileSync,
  rmSync,
  statSync,
} from "node:fs";
import { tmpdir } from "node:os";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const root = resolve(dirname(fileURLToPath(import.meta.url)), "../..");
const assets = join(root, "workspace", "assets");
const chrome =
  process.env.ADS_CHROME ??
  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";

const exportsToBuild = [
  {
    source: "gustav-social-banner-r1-linkedin.svg",
    output: "gustav-social-banner-r1-linkedin.png",
    width: 1584,
    height: 396,
  },
  {
    source: "gustav-social-banner-r1-x.svg",
    output: "gustav-social-banner-r1-x.png",
    width: 1500,
    height: 500,
  },
  {
    source: "gustav-social-banner-r1-linkedin-crop-proof.svg",
    output: "gustav-social-banner-r1-linkedin-crop-proof.png",
    width: 1440,
    height: 720,
  },
  {
    source: "gustav-social-banner-r1-x-crop-proof.svg",
    output: "gustav-social-banner-r1-x-crop-proof.png",
    width: 960,
    height: 600,
  },
];

if (!existsSync(chrome))
  throw new Error(`Chrome executable unavailable: ${chrome}`);

for (const item of exportsToBuild) await exportSvg(item);

process.stdout.write(
  `${exportsToBuild
    .map((item) => `${item.output} ${item.width}x${item.height} PNG`)
    .join("\n")}\n`,
);

async function exportSvg({ source, output, width, height }) {
  const sourcePath = join(assets, source);
  const outputPath = join(assets, output);
  if (!existsSync(sourcePath))
    throw new Error(`Missing SVG source: ${sourcePath}`);

  const svg = readFileSync(sourcePath, "utf8");
  const canvas = svg.match(/<svg[^>]+width="(\d+)"[^>]+height="(\d+)"/);
  if (!canvas || Number(canvas[1]) !== width || Number(canvas[2]) !== height)
    throw new Error(`${source} does not declare ${width}x${height}.`);

  rmSync(outputPath, { force: true });
  const profile = mkdtempSync(join(tmpdir(), "ads-social-banner-chrome-"));
  const args = [
    "--headless=new",
    "--disable-background-networking",
    "--disable-component-update",
    "--disable-default-apps",
    "--disable-gpu",
    "--disable-sync",
    "--hide-scrollbars",
    "--allow-file-access-from-files",
    "--metrics-recording-only",
    "--no-default-browser-check",
    "--no-first-run",
    "--run-all-compositor-stages-before-draw",
    "--force-device-scale-factor=1",
    `--window-size=${width},${height}`,
    `--user-data-dir=${profile}`,
    `--screenshot=${outputPath}`,
    pathToFileURL(sourcePath).href,
  ];

  const child = spawn(chrome, args, { stdio: "ignore" });
  try {
    await waitForPng(outputPath, width, height, child);
  } finally {
    if (child.exitCode === null) child.kill("SIGTERM");
    await Promise.race([
      new Promise((resolveExit) => child.once("exit", resolveExit)),
      delay(1200),
    ]);
    if (child.exitCode === null) child.kill("SIGKILL");
    rmSync(profile, { recursive: true, force: true });
  }
}

async function waitForPng(path, width, height, child) {
  const deadline = Date.now() + 15000;
  let previousSize = -1;
  let stableReads = 0;
  while (Date.now() < deadline) {
    if (existsSync(path)) {
      const size = statSync(path).size;
      stableReads = size > 24 && size === previousSize ? stableReads + 1 : 0;
      previousSize = size;
      if (stableReads >= 2) {
        const bytes = readFileSync(path);
        const signature = bytes.subarray(0, 8).toString("hex");
        const actualWidth = bytes.readUInt32BE(16);
        const actualHeight = bytes.readUInt32BE(20);
        if (signature !== "89504e470d0a1a0a")
          throw new Error(`${path} is not PNG.`);
        if (actualWidth !== width || actualHeight !== height)
          throw new Error(
            `${path} is ${actualWidth}x${actualHeight}; expected ${width}x${height}.`,
          );
        return;
      }
    }
    if (child.exitCode !== null && !existsSync(path))
      throw new Error(
        `Chrome exited ${child.exitCode} before writing ${path}.`,
      );
    await delay(100);
  }
  throw new Error(`Timed out waiting for ${path}.`);
}

function delay(milliseconds) {
  return new Promise((resolveDelay) => setTimeout(resolveDelay, milliseconds));
}
