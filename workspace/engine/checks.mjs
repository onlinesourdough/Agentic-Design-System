import { existsSync, lstatSync, readFileSync, readdirSync } from "node:fs";
import { basename, dirname, extname, join, relative, resolve } from "node:path";
import { spawnSync } from "node:child_process";

const root = resolve(
  process.argv.includes("--root")
    ? process.argv[process.argv.indexOf("--root") + 1]
    : process.cwd(),
);
const failures = [];
const designmd = join(
  root,
  "node_modules",
  "@google",
  "design.md",
  "dist",
  "index.js",
);
const visibleRoots = new Set(["workspace", "examples", "docs"]);
const allowedRootFiles = new Set([
  "AGENTS.md",
  "README.md",
  "LICENSE",
  "package.json",
  "package-lock.json",
]);
const legacyRootDirs = new Set(["engine", "scripts", "tests", "references"]);
const textExtensions = new Set([
  ".html",
  ".json",
  ".md",
  ".mjs",
  ".op",
  ".py",
  ".svg",
  ".yml",
  ".yaml",
]);
const requiredPaths = [
  "AGENTS.md",
  "README.md",
  ".agents/skills/agentic-design-system/SKILL.md",
  ".agents/skills/design-solution/SKILL.md",
  ".agents/skills/review-design/SKILL.md",
  ".agents/skills/audit-design-system/SKILL.md",
  "workspace/README.md",
  "workspace/BRIEF.md",
  "workspace/DESIGN.md",
  "workspace/index.html",
  "workspace/state",
  "workspace/runs",
  "workspace/history/runs.jsonl",
  "workspace/learning",
  "workspace/engine/checks.mjs",
  "workspace/engine/create-handoff.mjs",
  "workspace/engine/handoff_tracer.mjs",
  "workspace/engine/audit_design_system.py",
  "workspace/engine/audit_tracer.py",
  "workspace/engine/serve.mjs",
  "workspace/engine/tracer.py",
  "workspace/openpencil/route-console.op",
  "workspace/openpencil/exports/route-console.png",
  "examples/index.html",
  "examples/README.md",
  "docs/contract.md",
  "docs/ARCHITECTURE.md",
  "docs/SOURCE_AUDIT.md",
  "docs/THIRD_PARTY.md",
  "docs/validation.md",
  "docs/evidence-map.md",
  "docs/preservation.md",
];

function fail(message) {
  failures.push(message);
}

function rel(path) {
  return relative(root, path) || ".";
}

function read(path) {
  try {
    return readFileSync(path, "utf8");
  } catch (error) {
    fail(`cannot read ${rel(path)}: ${error.message}`);
    return "";
  }
}

function walk(directory, { includeReferences = false } = {}) {
  if (!existsSync(directory)) return [];
  const files = [];
  for (const entry of readdirSync(directory, { withFileTypes: true })) {
    if (entry.name === ".git" || entry.name === "node_modules") continue;
    if (!includeReferences && entry.name === "references") continue;
    const path = join(directory, entry.name);
    if (entry.isDirectory()) files.push(...walk(path, { includeReferences }));
    else if (entry.isFile()) files.push(path);
  }
  return files;
}

function checkShell() {
  if (!existsSync(root)) {
    fail(`root does not exist: ${root}`);
    return;
  }
  for (const entry of readdirSync(root, { withFileTypes: true })) {
    if (entry.name.startsWith(".")) continue;
    if (entry.name === "node_modules") continue;
    if (entry.isDirectory() && visibleRoots.has(entry.name)) continue;
    if (entry.isFile() && allowedRootFiles.has(entry.name)) continue;
    if (entry.isDirectory() && legacyRootDirs.has(entry.name)) {
      fail(`legacy visible root is present: ${entry.name}/`);
    } else {
      fail(`visible root is outside the ADS shell: ${entry.name}`);
    }
  }
  for (const path of requiredPaths) {
    if (!existsSync(join(root, path)))
      fail(`required path is missing: ${path}`);
  }
  for (const name of visibleRoots) {
    const path = join(root, name);
    if (!existsSync(path) || !lstatSync(path).isDirectory())
      fail(`functional root is not a directory: ${name}/`);
  }
}

function lintDesign(path) {
  if (!existsSync(designmd)) {
    fail("run npm install before Design.md lint");
    return;
  }
  const result = spawnSync(
    process.execPath,
    [designmd, "lint", "--format", "json", path],
    { cwd: root, encoding: "utf8" },
  );
  if (result.status !== 0) fail(`${rel(path)} failed Design.md lint`);
}

function checkPreview(path) {
  const html = read(path);
  for (const marker of ["<main", "viewport", "skip-link", ":focus-visible"]) {
    if (!html.includes(marker)) fail(`${rel(path)} lacks ${marker}`);
  }
  if (!html.includes("prefers-reduced-motion"))
    fail(`${rel(path)} lacks reduced-motion behavior`);
  for (const pattern of [
    /lorem ipsum/i,
    /john doe/i,
    /jane smith/i,
    /acme corp/i,
  ]) {
    if (pattern.test(html)) fail(`${rel(path)} contains ${pattern}`);
  }
}

function checkLocalLinks(path) {
  const html = read(path);
  const attributes = [...html.matchAll(/(?:href|src)=["']([^"']+)["']/gi)];
  for (const [, target] of attributes) {
    if (
      !target ||
      target.startsWith("#") ||
      target.startsWith("http:") ||
      target.startsWith("https:") ||
      target.startsWith("mailto:") ||
      target.startsWith("data:") ||
      target.includes("${")
    )
      continue;
    const clean = target.split("?")[0];
    const targetPath = resolve(dirname(path), clean);
    if (!existsSync(targetPath) && !existsSync(join(targetPath, "index.html")))
      fail(`${rel(path)} points to missing local path ${target}`);
  }
}

function checkExamples() {
  const examplesRoot = join(root, "examples");
  const index = read(join(examplesRoot, "index.html"));
  const readme = read(join(examplesRoot, "README.md"));
  const exampleDirs = readdirSync(examplesRoot, { withFileTypes: true })
    .filter((entry) => entry.isDirectory() && !entry.name.startsWith("."))
    .map((entry) => entry.name)
    .sort();
  if (exampleDirs.length < 1) fail("examples/ has no curated directories");
  for (const slug of exampleDirs) {
    const directory = join(examplesRoot, slug);
    for (const filename of [
      "BRIEF.md",
      "DESIGN.md",
      "index.html",
      "README.md",
      "proof.json",
    ]) {
      if (!existsSync(join(directory, filename)))
        fail(`examples/${slug}/${filename} is missing`);
    }
    lintDesign(join(directory, "DESIGN.md"));
    checkPreview(join(directory, "index.html"));
    checkLocalLinks(join(directory, "index.html"));
    if (!index.includes(`${slug}/index.html`))
      fail(`examples/index.html does not list ${slug}`);
    if (!readme.includes(slug) && slug !== "onlinesourdough-resources")
      fail(`examples/README.md does not mention ${slug}`);
    const proofPath = join(directory, "proof.json");
    try {
      const proof = JSON.parse(read(proofPath));
      if (proof.curated !== true || proof.review !== "PASS")
        fail(`examples/${slug}/proof.json is not a curated PASS proof`);
    } catch {
      fail(`examples/${slug}/proof.json is not valid JSON`);
    }
  }
}

function checkWorkspace() {
  lintDesign(join(root, "workspace/DESIGN.md"));
  checkPreview(join(root, "workspace/index.html"));
  checkLocalLinks(join(root, "workspace/index.html"));
  const workspace = read(join(root, "workspace/index.html"));
  for (const state of [
    "success",
    "loading",
    "error",
    "empty",
    "permission",
    "offline",
  ]) {
    if (!workspace.includes(`data-state="${state}"`))
      fail(`workspace/index.html lacks ${state} state fixture`);
  }
  const adapter = join(
    root,
    "examples/onlinesourdough-resources/assets/adapters",
  );
  for (const file of ["heroui-disclosure.css", "README.md"]) {
    if (!existsSync(join(adapter, file)))
      fail(`Resources adapter file is missing: ${file}`);
  }
  const resourcePreview = read(
    join(root, "examples/onlinesourdough-resources/index.html"),
  );
  if (!resourcePreview.includes("assets/adapters/heroui-disclosure.css"))
    fail("Resources preview does not load the reviewed local adapter");
  if (!resourcePreview.includes('data-adapter="heroui-disclosure"'))
    fail("Resources preview does not expose the adapter state");

  const sourceAudit = read(join(root, "docs/SOURCE_AUDIT.md"));
  const design = read(join(root, "workspace/DESIGN.md"));
  for (const marker of [
    "## Current design/source trace",
    "**Role:** UI/library source",
    "**Role:** inspiration/reference source",
    "**Role:** optional tool adapter",
  ]) {
    if (!sourceAudit.includes(marker))
      fail(`docs/SOURCE_AUDIT.md lacks ${marker}`);
  }
  for (const marker of [
    "source:heroui-ui-library",
    "source:desengs-inspiration",
    "source:openpencil-optional-adapter",
  ]) {
    if (!design.includes(marker))
      fail(`workspace/DESIGN.md lacks source decision ${marker}`);
  }

  const handoff = read(join(root, "workspace/engine/create-handoff.mjs"));
  for (const marker of [
    'status: "not-requested"',
    'status: "fallback"',
    'status: "included"',
    "openPencilReleaseRevision",
    "receivingOwner",
  ]) {
    if (!handoff.includes(marker))
      fail(`handoff generator lacks optional binding marker ${marker}`);
  }
  if (
    lstatSync(join(root, "workspace/openpencil/route-console.op")).size === 0 ||
    lstatSync(join(root, "workspace/openpencil/exports/route-console.png"))
      .size === 0
  )
    fail("OpenPencil source or reviewed export is empty");

  const auditSkill = read(
    join(root, ".agents/skills/audit-design-system/SKILL.md"),
  );
  for (const marker of ["read-only", "PASS", "FAIL", "BLOCKED"]) {
    if (!auditSkill.includes(marker))
      fail(`audit-design-system skill lacks ${marker}`);
  }
}

function checkLedger() {
  const path = join(root, "workspace/history/runs.jsonl");
  if (!existsSync(path)) return;
  const required = new Set([
    "run_id",
    "started_at",
    "finished_at",
    "status",
    "input_ref",
    "output_ref",
    "proof_ref",
    "previous_run_id",
    "previous_run_relation",
    "failure",
    "recovery",
  ]);
  const seen = new Map();
  const recovered = new Set();
  const lines = read(path).split(/\r?\n/).filter(Boolean);
  lines.forEach((line, index) => {
    let record;
    try {
      record = JSON.parse(line);
    } catch {
      fail(`ledger line ${index + 1} is not valid JSON`);
      return;
    }
    for (const field of required) {
      if (!(field in record)) fail(`ledger line ${index + 1} lacks ${field}`);
    }
    const id = record.run_id;
    if (!id || seen.has(id)) fail(`ledger repeats run_id ${id}`);
    const previous = record.previous_run_id;
    if (previous !== null && !seen.has(previous))
      fail(`ledger line ${index + 1} points to a later or missing run`);
    if (previous === null && record.previous_run_relation !== null)
      fail(`ledger line ${index + 1} has a relation without a predecessor`);
    if (
      previous !== null &&
      !["predecessor", "recovery"].includes(record.previous_run_relation)
    )
      fail(`ledger line ${index + 1} has an invalid relation`);
    if (record.status === "failed" && record.failure === null)
      fail(`ledger line ${index + 1} failed without failure evidence`);
    if (record.previous_run_relation === "recovery") {
      if (!record.recovery || record.recovery.from_run_id !== previous)
        fail(`ledger line ${index + 1} lacks matching recovery evidence`);
      if (recovered.has(previous))
        fail(`ledger recovers ${previous} more than once`);
      recovered.add(previous);
    }
    if (id) seen.set(id, record);
  });
}

function checkPublicText() {
  const oldIdentity = ["Design", "template"].join("-");
  const forbidden = [
    oldIdentity,
    ["design", "-template", "-overview.svg"].join(""),
    ["scripts", "/check.mjs"].join(""),
    ["scripts", "/create-handoff.mjs"].join(""),
    ["scripts", "/serve.mjs"].join(""),
    ["workspace", "/output"].join(""),
  ];
  const secretPatterns = [
    /-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----/,
    /(?:ghp_|github_pat_|xox[baprs]-)[A-Za-z0-9_-]{12,}/,
    /\bAKIA[0-9A-Z]{16}\b/,
  ];
  const scanRoots = [
    root,
    join(root, ".agents"),
    join(root, "workspace"),
    join(root, "examples"),
    join(root, "docs"),
  ];
  const files = [...new Set(scanRoots.flatMap((path) => walk(path)))].filter(
    (path) =>
      textExtensions.has(extname(path)) || basename(path) === "package.json",
  );
  for (const path of files) {
    const text = read(path);
    for (const phrase of forbidden) {
      if (
        text.includes(phrase) &&
        !(rel(path) === "docs/preservation.md" && phrase === oldIdentity)
      )
        fail(`stale identity/path ${phrase} in ${rel(path)}`);
    }
    for (const pattern of secretPatterns) {
      if (pattern.test(text)) fail(`secret-like text in ${rel(path)}`);
    }
  }
}

checkShell();
checkWorkspace();
checkExamples();
checkLedger();
checkPublicText();

if (failures.length) {
  process.stderr.write(
    `FAIL: ADS checks\n${failures.map((item) => `- ${item}`).join("\n")}\n`,
  );
  process.exitCode = 1;
} else {
  process.stdout.write(
    `${JSON.stringify(
      {
        success: true,
        root,
        visibleRoots: ["workspace/", "examples/", "docs/"],
        examples: readdirSync(join(root, "examples"), { withFileTypes: true })
          .filter((entry) => entry.isDirectory() && !entry.name.startsWith("."))
          .map((entry) => entry.name)
          .sort(),
      },
      null,
      2,
    )}\n`,
  );
}
