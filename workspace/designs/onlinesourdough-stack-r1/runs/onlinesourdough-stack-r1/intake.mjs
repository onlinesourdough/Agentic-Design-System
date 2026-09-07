import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import { createRequire } from "node:module";
const require = createRequire(import.meta.url);
const sharp = require("/Users/gustavanderson/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/sharp");
const root = path.dirname(new URL(import.meta.url).pathname);
const source =
  "/Users/gustavanderson/Documents/Codex/2026-09-05/s-dan-men-hvor-er-det/onlinesourdough-stack/masters";
const keys = [
  "org",
  "aios",
  "ads",
  "acs",
  "skills",
  "atlas",
  "resources",
  "review",
  "powerbi",
  "project",
  "system",
];
const hash = (b) => crypto.createHash("sha256").update(b).digest("hex");
const records = [];
for (const file of [...keys.map((k) => `${k}-icon.png`), "org-banner.png"]) {
  const sourcePath = path.join(source, file);
  const bytes = fs.readFileSync(sourcePath);
  const meta = await sharp(bytes).metadata();
  const banner = file === "org-banner.png";
  if (
    meta.width !== (banner ? 2172 : 1254) ||
    meta.height !== (banner ? 724 : 1254)
  )
    throw new Error(`Unexpected dimensions: ${file}`);
  const relative = `assets/masters/${file}`;
  fs.mkdirSync(path.join(root, "assets/masters"), { recursive: true });
  fs.copyFileSync(
    sourcePath,
    path.join(root, relative),
    fs.constants.COPYFILE_EXCL,
  );
  if (hash(bytes) !== hash(fs.readFileSync(path.join(root, relative))))
    throw new Error(`Copy mismatch: ${file}`);
  const record = {
    source_path: sourcePath,
    path: relative,
    sha256: hash(bytes),
    dimensions: [meta.width, meta.height],
    exports: [],
  };
  if (!banner) {
    fs.mkdirSync(path.join(root, "assets/exports"), { recursive: true });
    for (const size of [1024, 512, 128, 64]) {
      const target = `assets/exports/${file.replace(".png", `-${size}.png`)}`;
      if (fs.existsSync(path.join(root, target)))
        throw new Error(`Refusing overwrite: ${target}`);
      await sharp(bytes)
        .resize({ width: size, kernel: "lanczos3" })
        .png()
        .toFile(path.join(root, target));
      const output = fs.readFileSync(path.join(root, target));
      const measured = await sharp(output).metadata();
      if (measured.width !== size || measured.height !== size)
        throw new Error(`Export dimensions: ${target}`);
      record.exports.push({
        path: target,
        sha256: hash(output),
        dimensions: [measured.width, measured.height],
      });
    }
  }
  if (hash(fs.readFileSync(sourcePath)) !== record.sha256)
    throw new Error(`Source changed: ${file}`);
  records.push(record);
}
console.log(
  JSON.stringify(
    {
      sharp_version: sharp.versions.sharp,
      method:
        "width-only proportional Lanczos3 resampling; no crop, repaint, recolor or text replacement",
      records,
    },
    null,
    2,
  ),
);
