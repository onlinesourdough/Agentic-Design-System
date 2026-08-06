import { cpSync, existsSync, mkdirSync, rmSync, writeFileSync } from "node:fs";
import { basename, join, relative, resolve } from "node:path";
import { spawnSync } from "node:child_process";

const root = process.cwd();
const source = resolve(root, process.argv[2] ?? "workspace");
const output = resolve(root, process.argv[3] ?? join(source, "handoff"));
const designmd = join(
  root,
  "node_modules",
  "@google",
  "design.md",
  "dist",
  "index.js",
);

for (const file of ["BRIEF.md", "DESIGN.md", "index.html"]) {
  if (!existsSync(join(source, file)))
    fail(`${relative(root, source)}/${file} is missing.`);
}
if (!existsSync(designmd)) fail("Run npm install before creating a handoff.");

rmSync(output, { recursive: true, force: true });
mkdirSync(output, { recursive: true });
for (const file of ["DESIGN.md", "index.html"])
  cpSync(join(source, file), join(output, file));
if (existsSync(join(source, "assets")))
  cpSync(join(source, "assets"), join(output, "assets"), { recursive: true });

for (const [format, file] of [
  ["css-tailwind", "theme.css"],
  ["dtcg", "tokens.json"],
  ["json-tailwind", "tailwind.theme.json"],
]) {
  const exported = spawnSync(
    process.execPath,
    [designmd, "export", "--format", format, join(source, "DESIGN.md")],
    { encoding: "utf8" },
  );
  if (exported.status !== 0 || !exported.stdout.trim())
    fail(exported.stderr.trim() || `Export failed for ${format}.`);
  writeFileSync(join(output, file), `${exported.stdout.trimEnd()}\n`);
}

writeFileSync(
  join(output, "HANDOFF.md"),
  `# Design handoff\n\nSource: \`${relative(root, source)}\`\n\nCopy this directory into the receiving project or repository. That destination becomes the canonical owner. Revalidate behavior, accessibility, content, and tokens against its real implementation; this preview is not a runtime dependency.\n`,
);
process.stdout.write(
  `${JSON.stringify({ success: true, source: relative(root, source), output: relative(root, output), design: basename(join(source, "DESIGN.md")) }, null, 2)}\n`,
);

function fail(message) {
  process.stderr.write(
    `${JSON.stringify({ success: false, error: message })}\n`,
  );
  process.exit(1);
}
