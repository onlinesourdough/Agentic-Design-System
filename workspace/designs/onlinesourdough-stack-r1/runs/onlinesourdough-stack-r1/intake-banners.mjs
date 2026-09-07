import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import { createRequire } from "node:module";
const require = createRequire(import.meta.url);
const sharp = require("/Users/gustavanderson/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/sharp");
const root = path.dirname(new URL(import.meta.url).pathname);
const source =
  "/Users/gustavanderson/Documents/Codex/2026-09-05/s-dan-men-hvor-er-det/onlinesourdough-stack/masters";
const hash = (b) => crypto.createHash("sha256").update(b).digest("hex");
const manifest = JSON.parse(
  fs.readFileSync(path.join(root, "manifest.json"), "utf8"),
);
const inputs = [];
// Validate every input and existing destination before any copy or export.
for (const item of manifest.identities) {
  const sourcePath = path.join(source, item.asset_key + "-banner.png");
  const bytes = fs.readFileSync(sourcePath);
  const m = await sharp(bytes).metadata();
  if (m.width !== 2172 || m.height !== 724)
    throw new Error("Unexpected banner dimensions: " + sourcePath);
  const relative = "assets/masters/" + item.asset_key + "-banner.png";
  const destination = path.join(root, relative);
  const target = "assets/exports/" + item.asset_key + "-banner-1536x512.png";
  if (
    fs.existsSync(destination) &&
    hash(fs.readFileSync(destination)) !== hash(bytes)
  )
    throw new Error("Existing master mismatch: " + relative);
  if (fs.existsSync(path.join(root, target)))
    throw new Error("Export already exists: " + target);
  inputs.push({
    key: item.asset_key,
    sourcePath,
    bytes,
    relative,
    destination,
    target,
  });
}
const records = [];
for (const x of inputs) {
  if (!fs.existsSync(x.destination))
    fs.copyFileSync(x.sourcePath, x.destination, fs.constants.COPYFILE_EXCL);
  if (hash(fs.readFileSync(x.destination)) !== hash(x.bytes))
    throw new Error("Copy mismatch");
  await sharp(x.bytes)
    .resize({ width: 1536, kernel: "lanczos3" })
    .png()
    .toFile(path.join(root, x.target));
  const output = fs.readFileSync(path.join(root, x.target));
  const m = await sharp(output).metadata();
  if (m.width !== 1536 || m.height !== 512)
    throw new Error("Export dimensions mismatch");
  if (hash(fs.readFileSync(x.sourcePath)) !== hash(x.bytes))
    throw new Error("Source changed");
  records.push({
    key: x.key,
    source_path: x.sourcePath,
    path: x.relative,
    sha256: hash(x.bytes),
    dimensions: [2172, 724],
    export: { path: x.target, sha256: hash(output), dimensions: [1536, 512] },
  });
}
console.log(
  JSON.stringify({
    sharp_version: sharp.versions.sharp,
    method:
      "width-only proportional Lanczos3 resampling; no crop, repaint, recolor or text replacement",
    records,
  }),
);
