import { createHash } from "node:crypto";
import {
  existsSync,
  mkdtempSync,
  readFileSync,
  readdirSync,
  rmSync,
} from "node:fs";
import { tmpdir } from "node:os";
import { join, resolve } from "node:path";
import { spawnSync } from "node:child_process";

const root = process.cwd();
const toolIndex = process.argv.indexOf("--openpencil-tool");
if (toolIndex === -1 || !process.argv[toolIndex + 1])
  fail("Pass --openpencil-tool with the verified release CLI path.");
const tool = resolve(root, process.argv[toolIndex + 1]);
const source = join(root, "workspace");
const before = fingerprint(source);
const temporary = mkdtempSync(join(tmpdir(), "ads-handoff-trace-"));

try {
  const ordinary = run([
    source,
    join(temporary, "ordinary"),
    "--receiving-owner",
    "ADS proof receiver",
  ]);
  const success = run([
    source,
    join(temporary, "openpencil"),
    "--receiving-owner",
    "ADS proof receiver",
    "--openpencil",
    "--openpencil-tool",
    tool,
    "--openpencil-source",
    "openpencil/route-console.op",
    "--openpencil-export",
    "openpencil/exports/route-console.png",
    "--openpencil-version",
    "v0.8.4",
    "--openpencil-release-revision",
    "c51d7ed41a96068a09127bbc096fee143fce0b22",
    "--openpencil-revision",
    "9c810776dab546076a5d9db791a49d9e8048dbd7",
    "--openpencil-provenance",
    "ADS-owned HTML imported and edited through the verified OpenPencil release surface; no upstream design asset copied.",
    "--openpencil-review",
    "PASS",
    "--openpencil-limitations",
    "The HTML importer approximates some CSS and the release CLI needs a separately available desktop or web server for live document operations.",
  ]);
  const fallback = run([
    source,
    join(temporary, "fallback"),
    "--receiving-owner",
    "ADS proof receiver",
    "--openpencil",
    "--openpencil-tool",
    join(temporary, "unavailable-op"),
    "--openpencil-source",
    "openpencil/route-console.op",
    "--openpencil-export",
    "openpencil/exports/route-console.png",
    "--openpencil-version",
    "v0.8.4",
    "--openpencil-release-revision",
    "c51d7ed41a96068a09127bbc096fee143fce0b22",
    "--openpencil-revision",
    "9c810776dab546076a5d9db791a49d9e8048dbd7",
    "--openpencil-provenance",
    "ADS-owned source.",
    "--openpencil-review",
    "PASS",
    "--openpencil-limitations",
    "Tool unavailable fixture.",
  ]);

  if (ordinary.openpencil.status !== "not-requested")
    fail("ordinary handoff unexpectedly selected OpenPencil");
  if (success.openpencil.status !== "included")
    fail(
      `OpenPencil success route did not include artifacts: ${JSON.stringify(success)}`,
    );
  if (fallback.openpencil.status !== "fallback")
    fail("tool-unavailable route did not report fallback");
  for (const file of [
    "DESIGN.md",
    "index.html",
    "theme.css",
    "tokens.json",
    "tailwind.theme.json",
    "HANDOFF.md",
  ])
    if (!existsSync(join(temporary, "fallback", file)))
      fail(`ordinary fallback artifact is missing: ${file}`);
  if (existsSync(join(temporary, "fallback", "openpencil")))
    fail("fallback copied OpenPencil artifacts");
  if (before !== fingerprint(source))
    fail("handoff tracing changed the selected source directory");

  process.stdout.write(
    `${JSON.stringify(
      {
        success: true,
        ordinary: ordinary.openpencil.status,
        openpencil: success.openpencil.status,
        fallback: fallback.openpencil.status,
        fallbackReason: fallback.openpencil.reason,
        sourceUnchanged: true,
        source: success.openpencil.source,
        exports: success.openpencil.exports,
      },
      null,
      2,
    )}\n`,
  );
} finally {
  rmSync(temporary, { recursive: true, force: true });
}

function run(arguments_) {
  const result = spawnSync(
    process.execPath,
    [join(root, "workspace/engine/create-handoff.mjs"), ...arguments_],
    { cwd: root, encoding: "utf8" },
  );
  if (result.status !== 0)
    fail(
      result.stderr.trim() || result.stdout.trim() || "handoff route failed",
    );
  return JSON.parse(result.stdout);
}

function fingerprint(directory) {
  const hash = createHash("sha256");
  for (const path of files(directory)) {
    hash.update(path.slice(directory.length));
    hash.update(readFileSync(path));
  }
  return hash.digest("hex");
}

function files(directory) {
  if (!existsSync(directory)) return [];
  const paths = [];
  for (const entry of readdirSync(directory, { withFileTypes: true })) {
    if (entry.name === "handoff") continue;
    const path = join(directory, entry.name);
    if (entry.isDirectory()) paths.push(...files(path));
    else if (entry.isFile()) paths.push(path);
  }
  return paths.sort();
}

function fail(message) {
  process.stderr.write(`${message}\n`);
  process.exit(1);
}
