import { createHash, randomBytes } from "node:crypto";
import { spawn, spawnSync } from "node:child_process";
import {
  chmodSync,
  closeSync,
  existsSync,
  mkdirSync,
  openSync,
  readFileSync,
  realpathSync,
  renameSync,
  rmSync,
  statSync,
  writeFileSync,
} from "node:fs";
import { createServer, request as httpRequest } from "node:http";
import { tmpdir } from "node:os";
import { basename, dirname, extname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const EXPECTED_VERSION = "0.8.4";
const EXPECTED_VSIX_SHA256 =
  "7ce6cde22f7e8584de2faca0279f6d74438675291c2547a7d99230fc0e629342";
const SCHEMA = "ADS-OPENPENCIL-WORKBENCH/1";
const SCRIPT = fileURLToPath(import.meta.url);
const ROOT = realpathSync(resolve(dirname(SCRIPT), "../.."));
const DEFAULT_STATE_ROOT = join(
  tmpdir(),
  `ads-openpencil-workbench-${hashBytes(Buffer.from(ROOT)).slice(0, 12)}`,
);

await main();

async function main() {
  const [command = "help", ...rawArguments] = process.argv.slice(2);
  const arguments_ = parseArguments(rawArguments);
  try {
    if (command === "start") await start(arguments_);
    else if (command === "status") await status(arguments_);
    else if (command === "logs") logs(arguments_);
    else if (command === "stop") await stop(arguments_);
    else if (command === "check") await check(arguments_);
    else if (command === "__serve") await serve(arguments_);
    else if (command === "help" || command === "--help" || command === "-h")
      help();
    else fail(`Unknown OpenPencil workbench command: ${command}`);
  } catch (error) {
    fail(error instanceof Error ? error.message : String(error));
  }
}

function parseArguments(args) {
  const values = new Set([
    "--document",
    "--expected-document-sha256",
    "--expected-export-sha256",
    "--expected-nodes",
    "--export",
    "--host",
    "--lines",
    "--runtime-root",
    "--state-dir",
    "--vsix",
  ]);
  const parsed = {};
  for (let index = 0; index < args.length; index += 1) {
    const argument = args[index];
    if (!values.has(argument)) fail(`Unknown OpenPencil option: ${argument}`);
    const value = args[index + 1];
    if (!value || value.startsWith("--")) fail(`${argument} requires a value.`);
    parsed[argument.slice(2).replaceAll("-", "_")] = value;
    index += 1;
  }
  return parsed;
}

function options(arguments_) {
  const stateRoot = resolve(arguments_.state_dir ?? DEFAULT_STATE_ROOT);
  const host = arguments_.host ?? "127.0.0.1";
  if (host !== "127.0.0.1")
    throw new Error(
      `OpenPencil workbench requires strict origin 127.0.0.1; received ${host}.`,
    );
  return { host, stateRoot };
}

async function start(arguments_) {
  const { host, stateRoot } = options(arguments_);
  if (Boolean(arguments_.vsix) === Boolean(arguments_.runtime_root))
    throw new Error("Pass exactly one of --vsix or --runtime-root.");
  if (!arguments_.document)
    throw new Error("start requires --document <file.op>.");
  const document = requiredFile(
    arguments_.document,
    ".op",
    "OpenPencil document",
  );
  const expectedNodes = optionalPositiveInteger(
    arguments_.expected_nodes,
    "--expected-nodes",
  );
  const documentCheck = inspectDocument(document);
  if (expectedNodes !== null && documentCheck.nodes !== expectedNodes)
    throw new Error(
      `OpenPencil document has ${documentCheck.nodes} nodes; expected ${expectedNodes}.`,
    );
  if (
    arguments_.expected_document_sha256 &&
    documentCheck.sha256 !== arguments_.expected_document_sha256
  )
    throw new Error(
      `OpenPencil document SHA-256 ${documentCheck.sha256} does not match ${arguments_.expected_document_sha256}.`,
    );

  if (existsSync(stateRoot)) {
    const current = await readLiveState(stateRoot, 1_500);
    if (current) {
      if (realpathSync(current.document) !== document)
        throw new Error(
          `OpenPencil workbench already serves a different document: ${current.document}`,
        );
      output(publicState(current));
      return;
    }
    const stale = readState(stateRoot);
    if (stale?.pid && processRunning(stale.pid))
      throw new Error(
        `OpenPencil workbench state is unresponsive while pid ${stale.pid} is alive; inspect logs before cleanup.`,
      );
    rmSync(stateRoot, { recursive: true, force: true });
  }

  mkdirSync(dirname(stateRoot), { recursive: true });
  mkdirSync(stateRoot, { mode: 0o700 });
  const logPath = join(stateRoot, "workbench.log");
  try {
    const runtime = arguments_.vsix
      ? prepareVsixRuntime(arguments_.vsix, stateRoot)
      : inspectRuntimeRoot(arguments_.runtime_root);
    const config = {
      schema: SCHEMA,
      control_token: randomBytes(24).toString("hex"),
      document,
      document_sha256: documentCheck.sha256,
      expected_nodes: expectedNodes,
      host,
      log_path: logPath,
      runtime_root: runtime.root,
      runtime_source: runtime.source,
      state_root: stateRoot,
    };
    const configPath = join(stateRoot, "config.json");
    writePrivateJson(configPath, config);
    const logFd = openSync(logPath, "a", 0o600);
    const manager = spawn(
      process.execPath,
      [SCRIPT, "__serve", "--state-dir", stateRoot],
      {
        cwd: ROOT,
        detached: true,
        stdio: ["ignore", logFd, logFd],
      },
    );
    closeSync(logFd);
    manager.unref();

    const deadline = Date.now() + 20_000;
    while (Date.now() < deadline) {
      const ready = readState(stateRoot);
      if (ready?.status === "running") {
        output(publicState(ready));
        return;
      }
      const startupError = readJson(join(stateRoot, "error.json"));
      if (startupError?.error) throw new Error(startupError.error);
      block(100);
    }
    throw new Error(
      "OpenPencil workbench did not become ready within 20 seconds.",
    );
  } catch (error) {
    rmSync(stateRoot, { recursive: true, force: true });
    throw error;
  }
}

async function serve(arguments_) {
  const { stateRoot } = options(arguments_);
  const config = readJson(join(stateRoot, "config.json"));
  if (!config || config.schema !== SCHEMA)
    throw new Error("OpenPencil workbench manager lacks a valid config.");

  let upstream;
  let proxy;
  let state;
  let stopping = false;
  const stopManager = async ({ removeState = true } = {}) => {
    if (stopping) return;
    stopping = true;
    if (proxy) await closeServer(proxy);
    if (upstream && processRunning(upstream.pid)) {
      upstream.kill("SIGTERM");
      if (!(await waitForExit(upstream, 2_000))) upstream.kill("SIGKILL");
    }
    if (removeState) rmSync(stateRoot, { recursive: true, force: true });
  };

  try {
    let upstreamPort = null;
    proxy = createServer((incoming, response) => {
      if (incoming.url === "/__ads_workbench/status") {
        jsonResponse(response, 200, publicState(state));
        return;
      }
      if (incoming.url === "/__ads_workbench/stop") {
        if (
          incoming.method !== "POST" ||
          incoming.headers["x-ads-workbench-token"] !== config.control_token
        ) {
          jsonResponse(response, 403, { error: "forbidden" });
          return;
        }
        jsonResponse(response, 202, { stopping: true });
        setTimeout(() => void stopManager().then(() => process.exit(0)), 25);
        return;
      }
      if (upstreamPort === null) {
        jsonResponse(response, 503, { error: "upstream-not-ready" });
        return;
      }
      proxyRequest(incoming, response, upstreamPort);
    });
    await listen(proxy, config.host, 0);
    const address = proxy.address();
    if (!address || typeof address === "string")
      throw new Error(
        "OpenPencil workbench could not resolve its loopback port.",
      );
    const origin = `http://127.0.0.1:${address.port}`;
    const runtime = inspectRuntimeRoot(config.runtime_root);
    upstreamPort = await allocateLoopbackPort();
    upstream = spawn(
      runtime.server,
      [
        "--serve-web",
        "--host",
        "127.0.0.1",
        "--port",
        String(upstreamPort),
        "--file",
        config.document,
        "--allow-origin",
        origin,
      ],
      {
        env: {
          ...process.env,
          OPENPENCIL_CANVASKIT_DIR: runtime.canvaskit,
          OPENPENCIL_WEB_BUNDLE_DIR: runtime.pkg,
        },
        stdio: ["pipe", "pipe", "pipe"],
      },
    );
    upstream.stderr.setEncoding("utf8");
    upstream.stderr.on("data", (chunk) => process.stderr.write(chunk));
    upstream.stdout.setEncoding("utf8");
    upstream.stdout.on("data", (chunk) => process.stdout.write(chunk));

    const health = await waitForHealth(upstreamPort, 10_000);
    if (health.server !== "openpencil-mcp" || health.mode !== "web-canvas")
      throw new Error("OpenPencil daemon health is not the v0.8.4 web canvas.");
    if (health.localIp && health.localIp !== "127.0.0.1")
      throw new Error(
        `OpenPencil daemon escaped strict origin: ${health.localIp}.`,
      );
    const canonicalCanvasKit = await fetchBuffer(
      `http://127.0.0.1:${upstreamPort}/canvaskit/canvaskit.js`,
    );
    if (canonicalCanvasKit.status !== 200)
      throw new Error("OpenPencil daemon lacks /canvaskit/canvaskit.js.");

    const documentCheck = inspectDocument(config.document);
    if (
      config.expected_nodes !== null &&
      documentCheck.nodes !== config.expected_nodes
    )
      throw new Error(
        `OpenPencil document has ${documentCheck.nodes} nodes; expected ${config.expected_nodes}.`,
      );
    state = {
      schema: SCHEMA,
      status: "running",
      version: EXPECTED_VERSION,
      host: "127.0.0.1",
      origin,
      url: `${origin}/`,
      pid: process.pid,
      upstream_pid: upstream.pid,
      document: config.document,
      document_sha256: documentCheck.sha256,
      nodes: documentCheck.nodes,
      runtime_source: config.runtime_source,
      canvasKit_alias: "/pkg/canvaskit/* -> /canvaskit/*",
      control_token: config.control_token,
      state_root: stateRoot,
      log_path: config.log_path,
      started_at: new Date().toISOString(),
    };
    writePrivateJson(join(stateRoot, "state.json"), state);

    upstream.once("exit", (code, signal) => {
      if (!stopping) {
        process.stderr.write(
          `OpenPencil upstream exited unexpectedly (${code ?? signal}).\n`,
        );
        void stopManager().then(() => process.exit(1));
      }
    });
    process.once(
      "SIGTERM",
      () => void stopManager().then(() => process.exit(0)),
    );
    process.once(
      "SIGINT",
      () => void stopManager().then(() => process.exit(0)),
    );
    await new Promise(() => {});
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    await stopManager({ removeState: false });
    writePrivateJson(join(stateRoot, "error.json"), { error: message });
    throw error;
  }
}

async function status(arguments_) {
  const { stateRoot } = options(arguments_);
  if (!existsSync(join(stateRoot, "state.json"))) {
    output({ schema: SCHEMA, status: "stopped" });
    return;
  }
  const live = await readLiveState(stateRoot, 2_000);
  if (!live)
    throw new Error("OpenPencil workbench state is stale or unreachable.");
  output(publicState(live));
}

function logs(arguments_) {
  const { stateRoot } = options(arguments_);
  const lineCount = optionalPositiveInteger(
    arguments_.lines ?? "80",
    "--lines",
  );
  const logPath = join(stateRoot, "workbench.log");
  if (!existsSync(logPath))
    throw new Error("OpenPencil workbench log is unavailable.");
  const lines = readFileSync(logPath, "utf8").split(/\r?\n/);
  process.stdout.write(
    `${lines.slice(-lineCount).join("\n").replace(/^\n+/, "")}\n`,
  );
}

async function stop(arguments_) {
  const { stateRoot } = options(arguments_);
  const current = readState(stateRoot);
  if (!current) {
    if (existsSync(stateRoot))
      rmSync(stateRoot, { recursive: true, force: true });
    output({ schema: SCHEMA, status: "stopped", stopped: false });
    return;
  }
  const response = await fetch(`${current.origin}/__ads_workbench/stop`, {
    method: "POST",
    headers: { "x-ads-workbench-token": current.control_token },
    signal: AbortSignal.timeout(2_000),
  }).catch(() => null);
  if (!response || response.status !== 202)
    throw new Error("OpenPencil workbench refused the bounded stop request.");
  const deadline = Date.now() + 7_000;
  while (Date.now() < deadline && existsSync(stateRoot)) block(100);
  if (existsSync(stateRoot))
    throw new Error(
      "OpenPencil workbench did not clean its state within 7 seconds.",
    );
  output({ schema: SCHEMA, status: "stopped", stopped: true });
}

async function check(arguments_) {
  const { stateRoot } = options(arguments_);
  const live = await readLiveState(stateRoot, 2_000);
  if (!live) throw new Error("OpenPencil workbench is not running.");
  const origin = new URL(live.url).origin;
  if (origin !== live.origin || new URL(live.url).hostname !== "127.0.0.1")
    throw new Error(
      `OpenPencil workbench returned an unsafe origin: ${live.url}`,
    );
  const expectedNodes = optionalPositiveInteger(
    arguments_.expected_nodes,
    "--expected-nodes",
  );
  const document = requiredFile(
    arguments_.document ?? live.document,
    ".op",
    "OpenPencil document",
  );
  const documentCheck = inspectDocument(document);
  if (expectedNodes !== null && documentCheck.nodes !== expectedNodes)
    throw new Error(
      `OpenPencil document has ${documentCheck.nodes} nodes; expected ${expectedNodes}.`,
    );
  if (
    arguments_.expected_document_sha256 &&
    documentCheck.sha256 !== arguments_.expected_document_sha256
  )
    throw new Error(
      "OpenPencil document SHA-256 does not match the expected review.",
    );

  const root = await fetchBuffer(live.url);
  const canonicalJs = await fetchBuffer(`${origin}/canvaskit/canvaskit.js`);
  const aliasJs = await fetchBuffer(`${origin}/pkg/canvaskit/canvaskit.js`);
  const canonicalWasm = await fetchBuffer(`${origin}/canvaskit/canvaskit.wasm`);
  const aliasWasm = await fetchBuffer(`${origin}/pkg/canvaskit/canvaskit.wasm`);
  for (const [name, response] of [
    ["root", root],
    ["canonical CanvasKit JS", canonicalJs],
    ["aliased CanvasKit JS", aliasJs],
    ["canonical CanvasKit wasm", canonicalWasm],
    ["aliased CanvasKit wasm", aliasWasm],
  ]) {
    if (response.status !== 200)
      throw new Error(`${name} returned HTTP ${response.status}.`);
  }
  if (
    hashBytes(canonicalJs.body) !== hashBytes(aliasJs.body) ||
    hashBytes(canonicalWasm.body) !== hashBytes(aliasWasm.body)
  )
    throw new Error(
      "CanvasKit compatibility routes do not return identical bytes.",
    );

  let exportCheck = null;
  if (arguments_.export) {
    const exportPath = requiredFile(
      arguments_.export,
      [".png", ".svg"],
      "reviewed export",
    );
    exportCheck = { path: exportPath, sha256: hashFile(exportPath) };
    if (
      arguments_.expected_export_sha256 &&
      exportCheck.sha256 !== arguments_.expected_export_sha256
    )
      throw new Error(
        "Reviewed export SHA-256 does not match the expected review.",
      );
  }
  output({
    schema: SCHEMA,
    status: "PASS",
    version: live.version,
    origin,
    url: live.url,
    document: { path: document, ...documentCheck },
    export: exportCheck,
    canvasKit: {
      canonical: "/canvaskit/*",
      compatibility: "/pkg/canvaskit/*",
      identical: true,
    },
    browser_opening: "harness-owned",
  });
}

function prepareVsixRuntime(vsixPath, stateRoot) {
  const vsix = requiredFile(vsixPath, ".vsix", "OpenPencil VSIX");
  const digest = hashFile(vsix);
  if (digest !== EXPECTED_VSIX_SHA256)
    throw new Error(
      `OpenPencil VSIX SHA-256 ${digest} does not match the verified v${EXPECTED_VERSION} artifact.`,
    );
  const packageRead = spawnSync(
    "unzip",
    ["-p", vsix, "extension/package.json"],
    { encoding: "utf8" },
  );
  if (packageRead.status !== 0)
    throw new Error("OpenPencil VSIX lacks extension/package.json.");
  let packageJson;
  try {
    packageJson = JSON.parse(packageRead.stdout);
  } catch {
    throw new Error("OpenPencil VSIX package metadata is unreadable.");
  }
  if (String(packageJson.version) !== EXPECTED_VERSION)
    throw new Error(
      `OpenPencil runtime version ${packageJson.version} does not match ${EXPECTED_VERSION}.`,
    );
  const runtimeParent = join(stateRoot, "runtime");
  mkdirSync(runtimeParent);
  const extracted = spawnSync(
    "unzip",
    [
      "-q",
      vsix,
      "extension/package.json",
      "extension/bin/op-host-web-server",
      "extension/bin/op-host-web-server.exe",
      "extension/web/*",
      "-d",
      runtimeParent,
    ],
    { encoding: "utf8" },
  );
  if (extracted.status !== 0 && extracted.status !== 11)
    throw new Error(
      extracted.stderr.trim() || "OpenPencil VSIX extraction failed.",
    );
  const runtime = inspectRuntimeRoot(join(runtimeParent, "extension"));
  return {
    ...runtime,
    source: `verified-vsix:${basename(vsix)}#sha256:${digest}`,
  };
}

function inspectRuntimeRoot(path) {
  if (!path) throw new Error("OpenPencil runtime root is required.");
  const root = resolve(path);
  const packagePath = join(root, "package.json");
  if (!existsSync(packagePath))
    throw new Error(`OpenPencil runtime lacks package.json: ${root}`);
  let packageJson;
  try {
    packageJson = JSON.parse(readFileSync(packagePath, "utf8"));
  } catch {
    throw new Error("OpenPencil runtime package metadata is unreadable.");
  }
  if (String(packageJson.version) !== EXPECTED_VERSION)
    throw new Error(
      `OpenPencil runtime version ${packageJson.version} does not match ${EXPECTED_VERSION}.`,
    );
  const candidates = [
    join(root, "bin", "op-host-web-server"),
    join(root, "bin", "op-host-web-server.exe"),
  ];
  const server = candidates.find((candidate) => existsSync(candidate));
  if (!server) throw new Error("OpenPencil runtime lacks op-host-web-server.");
  const pkg = join(root, "web", "pkg");
  const canvaskit = join(root, "web", "canvaskit");
  for (const path_ of [
    join(pkg, "op_host_web.js"),
    join(pkg, "op_host_web_bg.wasm"),
    join(canvaskit, "canvaskit.js"),
    join(canvaskit, "canvaskit.wasm"),
  ]) {
    if (!existsSync(path_) || !statSync(path_).isFile())
      throw new Error(
        `OpenPencil runtime lacks ${path_.slice(root.length + 1)}.`,
      );
  }
  if (process.platform !== "win32") chmodSync(server, 0o755);
  return {
    root: realpathSync(root),
    server: realpathSync(server),
    pkg: realpathSync(pkg),
    canvaskit: realpathSync(canvaskit),
    source: `runtime-root:${realpathSync(root)}`,
  };
}

function proxyRequest(incoming, response, upstreamPort) {
  const url = new URL(incoming.url ?? "/", "http://127.0.0.1");
  if (
    url.pathname === "/pkg/canvaskit" ||
    url.pathname.startsWith("/pkg/canvaskit/")
  )
    url.pathname = url.pathname.slice(4);
  const headers = { ...incoming.headers };
  headers.host = `127.0.0.1:${upstreamPort}`;
  const upstream = httpRequest(
    {
      hostname: "127.0.0.1",
      port: upstreamPort,
      method: incoming.method,
      path: `${url.pathname}${url.search}`,
      headers,
    },
    (upstreamResponse) => {
      response.writeHead(
        upstreamResponse.statusCode ?? 502,
        upstreamResponse.headers,
      );
      upstreamResponse.pipe(response);
    },
  );
  upstream.on("error", (error) => {
    if (!response.headersSent)
      jsonResponse(response, 502, {
        error: "openpencil-upstream",
        message: error.message,
      });
    else response.end();
  });
  incoming.pipe(upstream);
}

async function waitForHealth(port, timeoutMs) {
  const deadline = Date.now() + timeoutMs;
  while (Date.now() < deadline) {
    try {
      const response = await fetch(`http://127.0.0.1:${port}/api/mcp/server`, {
        signal: AbortSignal.timeout(1_000),
      });
      if (response.ok) return await response.json();
    } catch {
      // The daemon may still be loading the selected document.
    }
    await delay(100);
  }
  throw new Error("OpenPencil daemon health did not become ready.");
}

async function allocateLoopbackPort() {
  const reservation = createServer();
  await listen(reservation, "127.0.0.1", 0);
  const address = reservation.address();
  if (!address || typeof address === "string") {
    await closeServer(reservation);
    throw new Error("OpenPencil workbench could not reserve a loopback port.");
  }
  const port = address.port;
  await closeServer(reservation);
  return port;
}

async function readLiveState(stateRoot, timeoutMs) {
  const current = readState(stateRoot);
  if (!current?.origin || !current?.control_token) return null;
  let url;
  try {
    url = new URL(current.origin);
  } catch {
    return null;
  }
  if (url.protocol !== "http:" || url.hostname !== "127.0.0.1") return null;
  try {
    const response = await fetch(`${current.origin}/__ads_workbench/status`, {
      signal: AbortSignal.timeout(timeoutMs),
    });
    if (!response.ok) return null;
    const live = await response.json();
    return live.schema === SCHEMA && live.status === "running"
      ? { ...current, ...live }
      : null;
  } catch {
    return null;
  }
}

function inspectDocument(path) {
  let document;
  try {
    document = JSON.parse(readFileSync(path, "utf8"));
  } catch {
    throw new Error(`OpenPencil document is not readable JSON: ${path}`);
  }
  let nodes = 0;
  const visit = (value) => {
    if (Array.isArray(value)) {
      value.forEach(visit);
      return;
    }
    if (!value || typeof value !== "object") return;
    if (typeof value.id === "string" && typeof value.type === "string")
      nodes += 1;
    Object.values(value).forEach(visit);
  };
  visit(document);
  return { nodes, sha256: hashFile(path) };
}

async function fetchBuffer(url) {
  try {
    const response = await fetch(url, { signal: AbortSignal.timeout(10_000) });
    return {
      status: response.status,
      contentType: response.headers.get("content-type"),
      body: Buffer.from(await response.arrayBuffer()),
    };
  } catch (error) {
    throw new Error(`OpenPencil request failed for ${url}: ${error.message}`);
  }
}

function listen(server, host, port) {
  return new Promise((resolve_, reject) => {
    server.once("error", reject);
    server.listen(port, host, () => {
      server.off("error", reject);
      resolve_();
    });
  });
}

function closeServer(server) {
  return new Promise((resolve_) => {
    server.close(() => resolve_());
    server.closeAllConnections?.();
  });
}

function waitForExit(child, timeoutMs) {
  if (!processRunning(child.pid)) return Promise.resolve(true);
  return Promise.race([
    new Promise((resolve_) => child.once("exit", () => resolve_(true))),
    delay(timeoutMs).then(() => false),
  ]);
}

function requiredFile(path, extensions, label) {
  const absolute = resolve(path);
  if (!existsSync(absolute) || !statSync(absolute).isFile())
    throw new Error(`${label} is unavailable: ${absolute}`);
  const allowed = Array.isArray(extensions) ? extensions : [extensions];
  if (!allowed.includes(extname(absolute).toLowerCase()))
    throw new Error(`${label} has an unsupported extension: ${absolute}`);
  return realpathSync(absolute);
}

function optionalPositiveInteger(value, label) {
  if (value === undefined || value === null) return null;
  const number = Number(value);
  if (!Number.isInteger(number) || number < 1)
    throw new Error(`${label} must be a positive integer.`);
  return number;
}

function processRunning(pid) {
  if (!Number.isInteger(pid) || pid < 1) return false;
  try {
    process.kill(pid, 0);
    return true;
  } catch {
    return false;
  }
}

function publicState(state) {
  if (!state) return { schema: SCHEMA, status: "starting" };
  const { control_token: _controlToken, ...public_ } = state;
  return public_;
}

function readState(stateRoot) {
  return readJson(join(stateRoot, "state.json"));
}

function readJson(path) {
  if (!existsSync(path)) return null;
  try {
    return JSON.parse(readFileSync(path, "utf8"));
  } catch {
    return null;
  }
}

function writePrivateJson(path, value) {
  const temporary = `${path}.${process.pid}.tmp`;
  writeFileSync(temporary, `${JSON.stringify(value, null, 2)}\n`, {
    mode: 0o600,
  });
  renameSync(temporary, path);
}

function hashFile(path) {
  return hashBytes(readFileSync(path));
}

function hashBytes(bytes) {
  return createHash("sha256").update(bytes).digest("hex");
}

function jsonResponse(response, status, value) {
  const body = `${JSON.stringify(value)}\n`;
  response.writeHead(status, {
    "content-type": "application/json; charset=utf-8",
    "content-length": Buffer.byteLength(body),
    "cache-control": "no-store",
  });
  response.end(body);
}

function output(value) {
  process.stdout.write(`${JSON.stringify(value, null, 2)}\n`);
}

function block(milliseconds) {
  Atomics.wait(new Int32Array(new SharedArrayBuffer(4)), 0, 0, milliseconds);
}

function delay(milliseconds) {
  return new Promise((resolve_) => setTimeout(resolve_, milliseconds));
}

function help() {
  process.stdout.write(`ADS OpenPencil workbench (${SCHEMA})

Usage:
  npm run openpencil -- start --vsix <verified-v0.8.4.vsix> --document <file.op>
  npm run openpencil -- status
  npm run openpencil -- logs [--lines 80]
  npm run openpencil -- check [--expected-nodes N] [--export reviewed.png]
  npm run openpencil -- stop

The workbench binds only 127.0.0.1 and prints a JSON \"url\" for a harness-owned
built-in browser. It never invokes an OS browser. OpenPencil remains an external,
verified, replaceable v${EXPECTED_VERSION} runtime and is cleaned by stop.
`);
}

function fail(message) {
  process.stderr.write(
    `${JSON.stringify({ success: false, error: message })}\n`,
  );
  process.exit(1);
}
