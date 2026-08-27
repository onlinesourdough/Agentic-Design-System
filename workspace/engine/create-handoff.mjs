import {
  copyFileSync,
  cpSync,
  existsSync,
  mkdirSync,
  readFileSync,
  realpathSync,
  rmSync,
  statSync,
  writeFileSync,
} from "node:fs";
import { createHash } from "node:crypto";
import {
  basename,
  dirname,
  extname,
  isAbsolute,
  join,
  relative,
  resolve,
} from "node:path";
import { spawnSync } from "node:child_process";

const root = process.cwd();
const { positional, options } = parseArguments(process.argv.slice(2));
if (positional.length > 2)
  fail("Handoff accepts at most a source and output positional argument.");
const receivingOwner = options.receivingOwner?.trim();
if (!receivingOwner)
  fail(
    "Pass a non-empty --receiving-owner for the receiving project or repository.",
  );
const source = resolve(root, positional[0] ?? "workspace");
const output = resolve(root, positional[1] ?? join(source, "handoff"));
const designmd = join(
  root,
  "node_modules",
  "@google",
  "design.md",
  "dist",
  "index.js",
);

if (!existsSync(source)) fail(`${relative(root, source)} is missing.`);
assertSafeOutput(output, source);
for (const file of ["BRIEF.md", "DESIGN.md", "index.html"]) {
  if (!existsSync(join(source, file)))
    fail(`${relative(root, source)}/${file} is missing.`);
}
if (!existsSync(designmd)) fail("Run npm install before creating a handoff.");

const openPencil = inspectOpenPencilRoute(source, options);

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

if (openPencil.status === "included") {
  for (const artifact of [openPencil.source, ...openPencil.exports]) {
    const target = join(output, artifact.handoffPath);
    mkdirSync(dirname(target), { recursive: true });
    copyFileSync(artifact.absolutePath, target);
    if (sha256(target) !== artifact.sha256)
      fail(`Copied OpenPencil artifact changed: ${artifact.handoffPath}`);
  }
}

writeFileSync(
  join(output, "HANDOFF.md"),
  handoffMarkdown({
    openPencil,
    receivingOwner,
    source: relative(root, source),
  }),
);

if (openPencil.status === "fallback")
  process.stderr.write(`OpenPencil fallback: ${openPencil.reason}\n`);

process.stdout.write(
  `${JSON.stringify(
    {
      success: true,
      source: relative(root, source),
      output: relative(root, output),
      design: basename(join(source, "DESIGN.md")),
      receivingOwner,
      openpencil: {
        requested: openPencil.requested,
        status: openPencil.status,
        reason: openPencil.reason ?? null,
        source:
          openPencil.status === "included"
            ? {
                path: openPencil.source.handoffPath,
                sha256: openPencil.source.sha256,
              }
            : null,
        exports:
          openPencil.status === "included"
            ? openPencil.exports.map((artifact) => ({
                path: artifact.handoffPath,
                sha256: artifact.sha256,
              }))
            : [],
      },
    },
    null,
    2,
  )}\n`,
);

function parseArguments(args) {
  const positional = [];
  const options = { openPencilExports: [] };
  const values = new Map([
    ["--receiving-owner", "receivingOwner"],
    ["--openpencil-tool", "openPencilTool"],
    ["--openpencil-source", "openPencilSource"],
    ["--openpencil-export", "openPencilExports"],
    ["--openpencil-version", "openPencilVersion"],
    ["--openpencil-release-revision", "openPencilReleaseRevision"],
    ["--openpencil-revision", "openPencilRevision"],
    ["--openpencil-provenance", "openPencilProvenance"],
    ["--openpencil-review", "openPencilReview"],
    ["--openpencil-limitations", "openPencilLimitations"],
  ]);
  for (let index = 0; index < args.length; index += 1) {
    const argument = args[index];
    if (argument === "--openpencil") {
      options.openPencilRequested = true;
      continue;
    }
    if (values.has(argument)) {
      const value = args[index + 1];
      if (!value || value.startsWith("--"))
        fail(`${argument} requires a value.`);
      const key = values.get(argument);
      if (key === "openPencilExports") options[key].push(value);
      else options[key] = value;
      index += 1;
      continue;
    }
    if (argument.startsWith("--")) fail(`Unknown handoff option: ${argument}`);
    positional.push(argument);
  }
  return { positional, options };
}

function inspectOpenPencilRoute(sourceRoot, values) {
  if (!values.openPencilRequested)
    return { requested: false, status: "not-requested" };

  const required = [
    ["--openpencil-tool", values.openPencilTool],
    ["--openpencil-source", values.openPencilSource],
    ["--openpencil-export", values.openPencilExports[0]],
    ["--openpencil-version", values.openPencilVersion],
    ["--openpencil-release-revision", values.openPencilReleaseRevision],
    ["--openpencil-revision", values.openPencilRevision],
    ["--openpencil-provenance", values.openPencilProvenance],
    ["--openpencil-review", values.openPencilReview],
    ["--openpencil-limitations", values.openPencilLimitations],
  ];
  const missing = required.filter(([, value]) => !value).map(([name]) => name);
  if (missing.length)
    return fallback(`selected route lacks ${missing.join(", ")}`);
  if (values.openPencilReview !== "PASS")
    return fallback(
      "selected route has not received an OpenPencil review PASS",
    );
  if (!/^[0-9a-f]{40}$/.test(values.openPencilReleaseRevision))
    return fallback(
      "OpenPencil release revision must be a 40-character Git SHA",
    );
  if (!/^[0-9a-f]{40}$/.test(values.openPencilRevision))
    return fallback(
      "OpenPencil upstream revision must be a 40-character Git SHA",
    );

  const tool = resolve(root, values.openPencilTool);
  const version = spawnSync(tool, ["--version"], { encoding: "utf8" });
  if (version.status !== 0)
    return fallback(
      version.error?.code === "ENOENT"
        ? `OpenPencil tool is unavailable at ${values.openPencilTool}`
        : `OpenPencil version check failed at ${values.openPencilTool}`,
    );
  let actualVersion;
  try {
    actualVersion = JSON.parse(version.stdout).version;
  } catch {
    return fallback("OpenPencil tool returned an unreadable version response");
  }
  if (
    String(actualVersion).replace(/^v/, "") !==
    values.openPencilVersion.replace(/^v/, "")
  )
    return fallback(
      `OpenPencil tool version ${actualVersion} does not match ${values.openPencilVersion}`,
    );

  let sourceArtifact;
  let exportArtifacts;
  try {
    sourceArtifact = artifact(sourceRoot, values.openPencilSource, ".op");
    exportArtifacts = values.openPencilExports.map((path) =>
      artifact(sourceRoot, path, [".png", ".svg"]),
    );
  } catch (error) {
    return fallback(error.message);
  }
  return {
    requested: true,
    status: "included",
    toolVersion: actualVersion,
    version: values.openPencilVersion,
    releaseRevision: values.openPencilReleaseRevision,
    revision: values.openPencilRevision,
    provenance: values.openPencilProvenance,
    review: values.openPencilReview,
    limitations: values.openPencilLimitations,
    source: sourceArtifact,
    exports: exportArtifacts,
  };
}

function artifact(sourceRoot, sourceRelativePath, allowedExtensions) {
  if (isAbsolute(sourceRelativePath))
    throw new Error(
      `OpenPencil path must be source-relative: ${sourceRelativePath}`,
    );
  const absolutePath = resolve(sourceRoot, sourceRelativePath);
  const scoped = relative(sourceRoot, absolutePath);
  if (!scoped || scoped.startsWith("..") || isAbsolute(scoped))
    throw new Error(
      `OpenPencil path escapes the selected source: ${sourceRelativePath}`,
    );
  if (!existsSync(absolutePath))
    throw new Error(
      `OpenPencil artifact is unavailable: ${sourceRelativePath}`,
    );
  const realSourceRoot = realpathSync(sourceRoot);
  const realArtifact = realpathSync(absolutePath);
  if (!statSync(realArtifact).isFile())
    throw new Error(
      `OpenPencil artifact is not a regular file: ${sourceRelativePath}`,
    );
  const realScoped = relative(realSourceRoot, realArtifact);
  if (!realScoped || realScoped.startsWith("..") || isAbsolute(realScoped))
    throw new Error(
      `OpenPencil artifact resolves outside the selected source: ${sourceRelativePath}`,
    );
  const allowed = Array.isArray(allowedExtensions)
    ? allowedExtensions
    : [allowedExtensions];
  if (!allowed.includes(extname(absolutePath).toLowerCase()))
    throw new Error(
      `OpenPencil artifact has an unsupported extension: ${sourceRelativePath}`,
    );
  const handoffPath = join(
    "openpencil",
    scoped.replace(/^openpencil[\\/]/, ""),
  );
  return {
    absolutePath: realArtifact,
    handoffPath,
    sha256: sha256(realArtifact),
  };
}

function assertSafeOutput(outputPath, sourcePath) {
  const candidate = canonicalPath(outputPath);
  for (const [name, protectedPath] of [
    ["repository root", realpathSync(root)],
    ["selected source", realpathSync(sourcePath)],
  ]) {
    if (isSameOrAncestor(candidate, protectedPath))
      fail(
        `Unsafe handoff output: ${outputPath} is ${name === "repository root" ? "the repository root or an ancestor of it" : "the selected source or an ancestor of it"}.`,
      );
  }
}

function canonicalPath(path) {
  let existing = resolve(path);
  const missing = [];
  while (!existsSync(existing)) {
    const parent = dirname(existing);
    if (parent === existing) break;
    missing.unshift(basename(existing));
    existing = parent;
  }
  return resolve(realpathSync(existing), ...missing);
}

function isSameOrAncestor(parent, child) {
  const scoped = relative(parent, child);
  return !scoped || (!scoped.startsWith("..") && !isAbsolute(scoped));
}

function fallback(reason) {
  return { requested: true, status: "fallback", reason };
}

function sha256(path) {
  return createHash("sha256").update(readFileSync(path)).digest("hex");
}

function clean(value) {
  return String(value)
    .replace(/[\r\n]+/g, " ")
    .replace(/`/g, "'")
    .trim();
}

function handoffMarkdown({ openPencil, receivingOwner, source: sourcePath }) {
  const lines = [
    "# ADS design handoff",
    "",
    `Source: \`${clean(sourcePath)}\``,
    "",
    `Receiving owner: ${clean(receivingOwner)}`,
    "",
    "Copy this directory into the receiving project or repository. That destination becomes the canonical owner of its implementation. Revalidate behavior, accessibility, content, and tokens against the receiving code; this preview remains a portable design proof.",
    "",
    "The semantic `DESIGN.md`, browser preview, and token exports are the ordinary portable boundary. OpenPencil is optional and replaceable; no receiving runtime depends on it.",
    "",
    "## OpenPencil binding",
    "",
  ];
  if (openPencil.status === "not-requested") {
    lines.push(
      "Status: not selected. This is an ordinary HTML/tokens handoff and contains no `.op` source.",
    );
  } else if (openPencil.status === "fallback") {
    lines.push(
      "Status: fallback to the ordinary handoff.",
      "",
      `Reason: ${clean(openPencil.reason)}`,
      "",
      "No `.op` source or OpenPencil export was copied. The selected source directory was not changed.",
    );
  } else {
    lines.push(
      "Status: included after supervised tool and visual review.",
      "",
      `Upstream version: \`${clean(openPencil.version)}\` (release commit \`${openPencil.releaseRevision}\`)`,
      "",
      `Observed upstream main revision: \`${openPencil.revision}\``,
      "",
      `Verified CLI response: \`${clean(openPencil.toolVersion)}\``,
      "",
      `Editable source: \`${openPencil.source.handoffPath}\` — SHA-256 \`${openPencil.source.sha256}\``,
      "",
      "Reviewed export boundary:",
      "",
      ...openPencil.exports.map(
        (item) => `- \`${item.handoffPath}\` — SHA-256 \`${item.sha256}\``,
      ),
      "",
      `Provenance: ${clean(openPencil.provenance)}`,
      "",
      `Review result: ${clean(openPencil.review)}`,
      "",
      `Known limitations: ${clean(openPencil.limitations)}`,
      "",
      "Only the listed exports were reviewed. Editing the `.op` source or regenerating an export reopens visual Review. `DESIGN.md` remains the portable semantic direction; the `.op` file is an optional tool-native working source.",
    );
  }
  return `${lines.join("\n")}\n`;
}

function fail(message) {
  process.stderr.write(
    `${JSON.stringify({ success: false, error: message })}\n`,
  );
  process.exit(1);
}
