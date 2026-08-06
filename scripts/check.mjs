import { existsSync, readFileSync, readdirSync } from "node:fs";
import { basename, join, relative } from "node:path";
import { spawnSync } from "node:child_process";

const root = process.cwd();
const examplesRoot = join(root, "examples");
const designmd = join(
  root,
  "node_modules",
  "@google",
  "design.md",
  "dist",
  "index.js",
);
const targets = [
  join(root, "workspace"),
  ...readdirSync(examplesRoot, { withFileTypes: true })
    .filter((entry) => entry.isDirectory())
    .map((entry) => join(examplesRoot, entry.name)),
];
const expectedExamples = new Set([
  "executive-powerbi-dashboard",
  "onlinesourdough-resources",
  "operations-workspace",
  "service-landing-page",
]);
const actualExamples = new Set(targets.slice(1).map((path) => basename(path)));
const failures = [];

for (const required of [
  "examples/index.html",
  ".agents/skills/design-solution/SKILL.md",
  ".agents/skills/review-design/SKILL.md",
  "docs/SOURCES.md",
  "docs/THIRD_PARTY.md",
]) {
  if (!existsSync(join(root, required)))
    failures.push(`${required} is missing.`);
}
if (existsSync(join(root, "index.html")))
  failures.push(
    "index.html belongs under examples/; remove the root entry point.",
  );
for (const legacySkill of ["skills/design-solution", "skills/review-design"]) {
  if (existsSync(join(root, legacySkill)))
    failures.push(`${legacySkill} is still in the legacy location.`);
}

if (!existsSync(designmd))
  failures.push("Run npm install before checking designs.");
if (
  [...expectedExamples].some((name) => !actualExamples.has(name)) ||
  actualExamples.size !== expectedExamples.size
) {
  failures.push(
    "examples/ must contain exactly the four documented showcases.",
  );
}

for (const target of targets) {
  for (const filename of ["BRIEF.md", "DESIGN.md", "index.html"]) {
    if (!existsSync(join(target, filename)))
      failures.push(`${relative(root, target)}/${filename} is missing.`);
  }
  if (!existsSync(join(target, "DESIGN.md")) || !existsSync(designmd)) continue;

  const lint = spawnSync(
    process.execPath,
    [designmd, "lint", "--format", "json", join(target, "DESIGN.md")],
    {
      cwd: root,
      encoding: "utf8",
    },
  );
  if (lint.status !== 0)
    failures.push(`${relative(root, target)}/DESIGN.md failed Design.md lint.`);

  const combined = ["BRIEF.md", "DESIGN.md", "index.html"]
    .map((name) => readFileSync(join(target, name), "utf8"))
    .join("\n");
  for (const pattern of [
    /lorem ipsum/i,
    /john doe/i,
    /jane smith/i,
    /acme corp/i,
    /href=["']#["']/i,
  ]) {
    if (pattern.test(combined))
      failures.push(`${relative(root, target)} contains ${pattern}.`);
  }
  const html = readFileSync(join(target, "index.html"), "utf8");
  for (const marker of ["<main", "viewport", "skip-link", ":focus-visible"]) {
    if (!html.includes(marker))
      failures.push(`${relative(root, target)}/index.html lacks ${marker}.`);
  }
}

process.stdout.write(
  `${JSON.stringify({ success: failures.length === 0, targets: targets.map((p) => relative(root, p)), failures }, null, 2)}\n`,
);
process.exitCode = failures.length === 0 ? 0 : 1;
