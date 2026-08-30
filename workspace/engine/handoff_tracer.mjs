import { createHash } from "node:crypto";
import {
  cpSync,
  existsSync,
  mkdirSync,
  mkdtempSync,
  readFileSync,
  readdirSync,
  rmSync,
  writeFileSync,
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
  const minimalSource = join(temporary, "minimal-source");
  mkdirSync(minimalSource);
  writeFileSync(
    join(minimalSource, "BRIEF.md"),
    `# Minimal portable brief

- **Receiving outcome:** Apply the approved visual direction in the named receiving repository.
- **Source/reference rights, provenance, and licensing:** ADS-owned tracer text under the repository license; no external assets.
`,
    "utf8",
  );
  writeFileSync(
    join(minimalSource, "DESIGN.md"),
    `---
name: Minimal portable direction
version: 1.0.0
---

# Minimal portable direction

- **Known limitations:** This fixture proves the handoff contract, not a rendered implementation.
`,
    "utf8",
  );
  writeFileSync(
    join(minimalSource, "REVIEW.md"),
    "# Review evidence\n\nResult: PASS\n",
    "utf8",
  );
  const ordinary = run([
    minimalSource,
    join(temporary, "ordinary"),
    "--receiving-owner",
    "ADS proof receiver",
  ]);
  const companionSource = join(temporary, "optional-companion-source");
  cpSync(source, companionSource, { recursive: true });
  mkdirSync(join(companionSource, "assets"), { recursive: true });
  writeFileSync(
    join(companionSource, "assets/selected.txt"),
    "selected companion\n",
    "utf8",
  );
  writeFileSync(
    join(companionSource, "assets/unselected.txt"),
    "not selected\n",
    "utf8",
  );
  const selectedCompanions = run([
    companionSource,
    join(temporary, "selected-companions"),
    "--receiving-owner",
    "ADS proof receiver",
    "--preview",
    "--asset",
    "assets/selected.txt",
    "--export",
    "css",
    "--export",
    "tokens",
    "--export",
    "tailwind",
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
  const websiteOutput = join(temporary, "website-application");
  const website = run([
    join(root, "examples/service-landing-page"),
    websiteOutput,
    "--receiving-owner",
    "Plainwork implementation project",
  ]);
  const dashboardOutput = join(temporary, "dashboard-slide");
  const dashboard = run([
    join(root, "examples/executive-powerbi-dashboard"),
    dashboardOutput,
    "--receiving-owner",
    "Common Table analytics project",
  ]);

  const contentSource = join(temporary, "acs-originated-content-source");
  cpSync(join(root, "examples/onlinesourdough-resources"), contentSource, {
    recursive: true,
  });
  writeFileSync(
    join(contentSource, "BRIEF.md"),
    `# Brief — ACS-originated content visual fixture

- **Need:** Translate an accepted ACS editorial promise and selected source media into thumbnail composition and motion-language direction.
- **Audience:** The ACS editor responsible for the final content package.
- **Receiving outcome:** Apply the approved thumbnail composition and motion direction while ACS retains editorial, edit, render, package, and publication ownership.
- **States:** Static thumbnail, motion opening, reduced motion, and unavailable source media.
- **Constraints:** ADS must not invent the hook, script, caption, source-media choice, edit timing, or publication package and must not invoke ACS.
- **Source/reference rights, provenance, and licensing:** This isolated fixture references the ADS-owned Resources direction and its documented local asset provenance; it adds no external asset or duplicated ACS production truth.
- **Ownership boundary:** ADS owns visual composition, style/voice expression, and motion direction. ACS owns editorial content and all production execution.
- **Proof:** The accepted handoff is portable, hashed, and usable without ADS at runtime.
- **Receiving project or repository:** Agentic Content System fixture receiver.
- **Review and acceptance owner:** Existing ADS Review evidence approves the direction; the fixture receiver explicitly accepts the generated snapshot.
`,
    "utf8",
  );
  const contentOutput = join(temporary, "content-visual-accepted");
  const contentVisual = run([
    contentSource,
    contentOutput,
    "--receiving-owner",
    "Agentic Content System fixture receiver",
  ]);
  acceptFixture(contentOutput);
  const acceptedFingerprint = fingerprint(contentOutput);
  const immutable = runFailure([
    contentSource,
    contentOutput,
    "--receiving-owner",
    "Agentic Content System fixture receiver",
  ]);
  if (!immutable.includes("Accepted handoff snapshots are immutable"))
    fail("accepted content-visual snapshot was not protected");
  if (acceptedFingerprint !== fingerprint(contentOutput))
    fail("accepted content-visual snapshot changed after regeneration attempt");

  const revisedDesign = readFileSync(join(contentSource, "DESIGN.md"), "utf8")
    .replace(/^version: alpha$/m, "version: beta")
    .concat(
      "\n## Isolated revision fixture\n\nThis temporary tracer-only revision proves explicit re-handoff without changing the accepted snapshot.\n",
    );
  writeFileSync(join(contentSource, "DESIGN.md"), revisedDesign, "utf8");
  const revisedOutput = join(temporary, "content-visual-revision");
  const revisedContent = run([
    contentSource,
    revisedOutput,
    "--receiving-owner",
    "Agentic Content System fixture receiver",
  ]);

  const contentGap = {
    detected: true,
    missingDecision: "approved editorial promise for the visual",
    siblingSuggestion: "Agentic Content System",
    boundedRequest:
      "Return one accepted editorial promise and selected source-media reference; ADS will continue only with visual direction.",
    routing: "suggestion-only",
    invoked: false,
  };

  if (ordinary.openpencil.status !== "not-requested")
    fail("minimal handoff unexpectedly selected OpenPencil");
  if (
    ordinary.companions.preview ||
    ordinary.companions.assets.length ||
    ordinary.companions.exports.length
  )
    fail("minimal handoff unexpectedly included optional companions");
  const minimalPaths = ordinary.handoff.artifacts
    .map((item) => item.path)
    .sort()
    .join(",");
  if (minimalPaths !== "BRIEF.md,DESIGN.md,REVIEW.md")
    fail(`minimal handoff has an unexpected artifact set: ${minimalPaths}`);
  if (
    !selectedCompanions.companions.preview ||
    selectedCompanions.companions.assets.join(",") !== "assets/selected.txt" ||
    selectedCompanions.companions.exports.join(",") !==
      "theme.css,tokens.json,tailwind.theme.json"
  )
    fail("explicit companion selection was not preserved");
  if (existsSync(join(temporary, "selected-companions/assets/unselected.txt")))
    fail("unselected asset was copied");
  if (success.openpencil.status !== "included")
    fail(
      `OpenPencil success route did not include artifacts: ${JSON.stringify(success)}`,
    );
  if (fallback.openpencil.status !== "fallback")
    fail("tool-unavailable route did not report fallback");
  for (const file of ["BRIEF.md", "DESIGN.md", "REVIEW.md", "HANDOFF.md"])
    if (!existsSync(join(temporary, "fallback", file)))
      fail(`ordinary fallback artifact is missing: ${file}`);
  if (existsSync(join(temporary, "fallback", "openpencil")))
    fail("fallback copied OpenPencil artifacts");
  if (before !== fingerprint(source))
    fail("handoff tracing changed the selected source directory");
  assertPortableSnapshot(
    join(root, "examples/service-landing-page"),
    websiteOutput,
    website,
  );
  assertPortableSnapshot(
    join(root, "examples/executive-powerbi-dashboard"),
    dashboardOutput,
    dashboard,
  );
  assertPortableSnapshot(contentSource, revisedOutput, revisedContent);
  if (contentVisual.handoff.id !== revisedContent.handoff.id)
    fail("a later content-visual revision changed the stable handoff identity");
  if (contentVisual.handoff.revision === revisedContent.handoff.revision)
    fail(
      "a later content-visual revision did not create a new handoff revision",
    );
  if (acceptedFingerprint !== fingerprint(contentOutput))
    fail("the accepted snapshot changed while creating a later revision");
  if (contentGap.invoked || contentGap.routing !== "suggestion-only")
    fail("content gap created an automatic sibling route");

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
        portableContract: ordinary.handoff.contract,
        minimal: {
          artifacts: ordinary.handoff.artifacts.map((item) => item.path),
          companions: ordinary.companions,
        },
        optionalCompanions: selectedCompanions.companions,
        surfaces: {
          websiteApplication: {
            source: "examples/service-landing-page",
            handoff: website.handoff.id,
            revision: website.handoff.revision,
            designCanonical: true,
          },
          dashboardSlide: {
            source: "examples/executive-powerbi-dashboard",
            handoff: dashboard.handoff.id,
            revision: dashboard.handoff.revision,
            designCanonical: true,
          },
          contentVisual: {
            origin: "ACS-originated brief fixture",
            receiver: "Agentic Content System fixture receiver",
            handoff: contentVisual.handoff.id,
            acceptedRevision: contentVisual.handoff.revision,
            nextRevision: revisedContent.handoff.revision,
            acceptedSnapshotImmutable: true,
            nextRevisionAcceptance: revisedContent.handoff.acceptance,
            designCanonical: true,
            adsRuntimeRequiredByReceiver: false,
          },
        },
        contentGap,
      },
      null,
      2,
    )}\n`,
  );
} finally {
  rmSync(temporary, { recursive: true, force: true });
}

function assertPortableSnapshot(sourceDirectory, outputDirectory, result) {
  if (result.handoff.contract !== "ADS-HANDOFF/1")
    fail(`unexpected portable handoff contract: ${result.handoff.contract}`);
  if (result.handoff.review.status !== "PASS")
    fail("portable handoff was generated without review PASS");
  if (result.handoff.acceptance !== "PENDING")
    fail("new portable handoff did not begin pending acceptance");
  const design = result.handoff.artifacts.find(
    (artifact) => artifact.path === "DESIGN.md",
  );
  if (!design) fail("portable handoff manifest lacks canonical DESIGN.md");
  if (
    createHash("sha256")
      .update(readFileSync(join(sourceDirectory, "DESIGN.md")))
      .digest("hex") !== design.sha256
  )
    fail("portable handoff DESIGN.md hash does not match its source revision");
  if (
    readFileSync(join(sourceDirectory, "DESIGN.md"), "utf8") !==
    readFileSync(join(outputDirectory, "DESIGN.md"), "utf8")
  )
    fail("portable handoff changed canonical DESIGN.md");
  const binder = readFileSync(join(outputDirectory, "HANDOFF.md"), "utf8");
  for (const marker of [
    "Receiving outcome:",
    "## Included snapshot and integrity",
    "## Provenance and licensing",
    "## Known limitations",
    "Acceptance state: PENDING",
  ])
    if (!binder.includes(marker)) fail(`portable HANDOFF.md lacks ${marker}`);
}

function acceptFixture(outputDirectory) {
  const path = join(outputDirectory, "HANDOFF.md");
  const accepted = readFileSync(path, "utf8")
    .replace("Acceptance state: PENDING", "Acceptance state: ACCEPTED")
    .replace(
      "Accepted by: _(receiving owner must complete)_",
      "Accepted by: Agentic Content System fixture receiver",
    )
    .replace(
      "Accepted at: _(receiving owner must complete)_",
      "Accepted at: 2026-08-30T00:00:00Z",
    )
    .replace(
      "Acceptance statement: The receiving owner must explicitly replace the pending fields. Generation, copying, or use does not imply acceptance.",
      "Acceptance statement: Accepted for the isolated thumbnail and motion-direction fixture; ACS retains production ownership.",
    );
  writeFileSync(path, accepted, "utf8");
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

function runFailure(arguments_) {
  const result = spawnSync(
    process.execPath,
    [join(root, "workspace/engine/create-handoff.mjs"), ...arguments_],
    { cwd: root, encoding: "utf8" },
  );
  if (result.status === 0) fail("expected handoff route to fail");
  return `${result.stderr}\n${result.stdout}`;
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
