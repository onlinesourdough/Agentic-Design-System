from __future__ import annotations

import hashlib
import http.server
import json
import os
import shutil
import subprocess
import tempfile
import threading
import unittest
import urllib.error
import urllib.request
from pathlib import Path
from typing import Optional


ROOT = Path(__file__).resolve().parents[3]
SCRIPT = ROOT / "workspace/engine/openpencil-workbench.mjs"
NODE = shutil.which("node") or "node"


class OpenPencilWorkbenchTests(unittest.TestCase):
    def _runtime(self, root: Path, version: str = "0.8.4") -> Path:
        runtime = root / "runtime"
        (runtime / "bin").mkdir(parents=True)
        (runtime / "web/pkg").mkdir(parents=True)
        (runtime / "web/canvaskit").mkdir(parents=True)
        (runtime / "package.json").write_text(
            json.dumps({"name": "fake-openpencil", "version": version}),
            encoding="utf-8",
        )
        (runtime / "web/pkg/op_host_web.js").write_text(
            "export const fake = true;\n", encoding="utf-8"
        )
        (runtime / "web/pkg/op_host_web_bg.wasm").write_bytes(b"fake-wasm")
        (runtime / "web/canvaskit/canvaskit.js").write_text(
            "globalThis.CanvasKitInit = () => {};\n", encoding="utf-8"
        )
        (runtime / "web/canvaskit/canvaskit.wasm").write_bytes(
            b"fake-canvaskit-wasm"
        )
        server = runtime / "bin/op-host-web-server"
        server.write_text(
            """#!/usr/bin/env node
const fs = require("node:fs");
const path = require("node:path");
const http = require("node:http");
const args = process.argv.slice(2);
if (args.includes("--managed")) {
  process.stderr.write("managed mode requires an external credential injector\\n");
  process.exit(64);
}
if (args[0] === "--mcp") {
  if (process.env.ADS_FAKE_MCP_HANG === "1") {
    setInterval(() => {}, 1000);
    return;
  }
  let input = "";
  process.stdin.setEncoding("utf8");
  process.stdin.on("data", (chunk) => { input += chunk; });
  process.stdin.on("end", () => {
    for (const line of input.split(/\\r?\\n/).filter(Boolean)) {
      const request = JSON.parse(line);
      if (request.id === 1) {
        process.stdout.write(JSON.stringify({
          jsonrpc: "2.0",
          id: 1,
          result: { protocolVersion: "2024-11-05", capabilities: { tools: {} }, serverInfo: { name: "openpencil-mcp", version: "0.8.4" } },
        }) + "\\n");
      }
      if (request.id === 2 && request.method === "tools/call") {
        if (process.env.ADS_FAKE_MCP_OUTPUT_LIMIT === "1") {
          process.stdout.write("x".repeat(1000001), () => process.exit(0));
          return;
        }
        if (process.env.ADS_FAKE_MCP_FAILURE === "1") {
          process.stdout.write(JSON.stringify({
            jsonrpc: "2.0",
            id: 2,
            error: { code: -32000, message: "fixture native export failure" },
          }) + "\\n");
          continue;
        }
        const outputDir = request.params.arguments.outputDir;
        fs.mkdirSync(outputDir, { recursive: false });
        const png = Buffer.alloc(24);
        Buffer.from("89504e470d0a1a0a", "hex").copy(png, 0);
        png.writeUInt32BE(64, 16);
        png.writeUInt32BE(42, 20);
        const name = "fixture-frame.png";
        fs.writeFileSync(path.join(outputDir, name), png);
        process.stdout.write(JSON.stringify({
          jsonrpc: "2.0",
          id: 2,
          result: { content: [{ type: "text", text: JSON.stringify({ directory: outputDir, format: "png", attempted: 1, written: [name], failed: [] }) }] },
        }) + "\\n");
      }
    }
    process.exit(0);
  });
  return;
}
const value = (flag, fallback) => {
  const index = args.indexOf(flag);
  return index >= 0 ? args[index + 1] : fallback;
};
const host = value("--host", "127.0.0.1");
const requestedPort = Number(value("--port", "0"));
fs.writeFileSync(path.join(__dirname, "..", "server-args.json"), JSON.stringify(args));
const token = "0123456789abcdef0123456789abcdef";
const js = Buffer.from("fake-canvaskit-js");
const wasm = Buffer.from("fake-canvaskit-wasm");
const server = http.createServer((request, response) => {
  if (request.url === "/api/mcp/server") {
    response.writeHead(200, {"content-type": "application/json"});
    response.end(JSON.stringify({
      running: true,
      port: server.address().port,
      localIp: host,
      server: "openpencil-mcp",
      mode: "web-canvas",
    }));
    return;
  }
  if (request.url === "/") {
    response.writeHead(200, {"content-type": "text/html"});
    response.end("<!doctype html><title>OpenPencil</title><canvas id=op></canvas>");
    return;
  }
  if (request.url === "/canvaskit/canvaskit.js") {
    response.writeHead(200, {"content-type": "text/javascript"});
    response.end(js);
    return;
  }
  if (request.url === "/canvaskit/canvaskit.wasm") {
    response.writeHead(200, {"content-type": "application/wasm"});
    response.end(wasm);
    return;
  }
  response.writeHead(404, {"content-type": "text/plain"});
  response.end("not found");
});
server.listen(requestedPort, host, () => {
  process.stdout.write(JSON.stringify({
    ok: true,
    port: server.address().port,
    token,
    version: "0.8.4",
  }) + "\\n");
  process.stderr.write("fake OpenPencil daemon ready\\n");
});
process.stdin.resume();
process.stdin.on("end", () => server.close(() => process.exit(0)));
process.on("SIGTERM", () => server.close(() => process.exit(0)));
""",
            encoding="utf-8",
        )
        server.chmod(server.stat().st_mode | 0o111)
        return runtime

    def _document(self, root: Path) -> Path:
        document = root / "fixture.op"
        document.write_text(
            json.dumps(
                {
                    "version": "1.0",
                    "children": [
                        {
                            "id": "node-1",
                            "type": "frame",
                            "name": "Fixture",
                            "children": [],
                        }
                    ],
                }
            ),
            encoding="utf-8",
        )
        return document

    def _run(
        self, *arguments: str, env: Optional[dict[str, str]] = None
    ) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [NODE, str(SCRIPT), *arguments],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
            env=env,
        )

    def test_wrong_version_and_non_loopback_origin_are_denied(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            document = self._document(root)
            state = root / "state"
            wrong_version = self._run(
                "start",
                "--runtime-root",
                str(self._runtime(root, "0.8.5")),
                "--document",
                str(document),
                "--state-dir",
                str(state),
            )
            self.assertNotEqual(wrong_version.returncode, 0)
            self.assertIn("does not match 0.8.4", wrong_version.stderr)
            self.assertFalse(state.exists())

            runtime = self._runtime(root / "second")
            wrong_origin = self._run(
                "start",
                "--runtime-root",
                str(runtime),
                "--document",
                str(document),
                "--state-dir",
                str(state),
                "--host",
                "0.0.0.0",
            )
            self.assertNotEqual(wrong_origin.returncode, 0)
            self.assertIn("strict origin 127.0.0.1", wrong_origin.stderr)
            self.assertFalse(state.exists())

    def test_canvaskit_alias_no_os_open_status_logs_and_cleanup(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            runtime = self._runtime(root)
            document = self._document(root)
            reviewed_export = root / "reviewed.png"
            reviewed_export.write_bytes(b"reviewed-export")
            state = root / "state"
            spy_dir = root / "spies"
            spy_dir.mkdir()
            opened = root / "browser-opened"
            for command in ("open", "xdg-open", "zen", "op"):
                spy = spy_dir / command
                spy.write_text(
                    f"#!/bin/sh\nprintf '%s\\n' '{command}' >> '{opened}'\n",
                    encoding="utf-8",
                )
                spy.chmod(spy.stat().st_mode | 0o111)
            env = {
                **os.environ,
                "PATH": f"{spy_dir}{os.pathsep}{os.environ.get('PATH', '')}",
            }

            started = self._run(
                "start",
                "--runtime-root",
                str(runtime),
                "--document",
                str(document),
                "--expected-nodes",
                "1",
                "--state-dir",
                str(state),
                env=env,
            )
            try:
                self.assertEqual(started.returncode, 0, started.stderr)
                result = json.loads(started.stdout)
                self.assertEqual(result["version"], "0.8.4")
                self.assertEqual(result["host"], "127.0.0.1")
                self.assertTrue(result["url"].startswith("http://127.0.0.1:"))
                self.assertNotIn("control_token", result)
                self.assertEqual(Path(result["document"]), document.resolve())
                self.assertNotEqual(Path(result["working_document"]), document.resolve())
                self.assertEqual(
                    Path(result["working_document"]).read_bytes(), document.read_bytes()
                )
                daemon_args = json.loads(
                    (runtime / "server-args.json").read_text(encoding="utf-8")
                )
                self.assertEqual(
                    Path(daemon_args[daemon_args.index("--file") + 1]),
                    Path(result["working_document"]),
                )

                status = self._run("status", "--state-dir", str(state), env=env)
                self.assertEqual(status.returncode, 0, status.stderr)
                self.assertEqual(json.loads(status.stdout)["status"], "running")
                original_source = document.read_bytes()

                failed_output = root / "failed-native-output"
                failed_native = self._run(
                    "native-export",
                    "--state-dir",
                    str(state),
                    "--output-dir",
                    str(failed_output),
                    env={**env, "ADS_FAKE_MCP_FAILURE": "1"},
                )
                self.assertNotEqual(failed_native.returncode, 0)
                self.assertIn("fixture native export failure", failed_native.stderr)
                self.assertFalse(failed_output.exists())

                timeout_output = root / "timeout-native-output"
                timed_out = self._run(
                    "native-export",
                    "--state-dir",
                    str(state),
                    "--output-dir",
                    str(timeout_output),
                    env={**env, "ADS_FAKE_MCP_HANG": "1"},
                )
                self.assertNotEqual(timed_out.returncode, 0)
                self.assertIn("was terminated", timed_out.stderr)
                self.assertFalse(timeout_output.exists())

                oversized_output = root / "oversized-native-output"
                oversized = self._run(
                    "native-export",
                    "--state-dir",
                    str(state),
                    "--output-dir",
                    str(oversized_output),
                    env={**env, "ADS_FAKE_MCP_OUTPUT_LIMIT": "1"},
                )
                self.assertNotEqual(oversized.returncode, 0)
                self.assertIn("output exceeded", oversized.stderr)
                self.assertFalse(oversized_output.exists())

                native_output = root / "native-output"
                native = self._run(
                    "native-export",
                    "--state-dir",
                    str(state),
                    "--output-dir",
                    str(native_output),
                    env=env,
                )
                self.assertEqual(native.returncode, 0, native.stderr)
                native_proof = json.loads(native.stdout)
                self.assertEqual(native_proof["status"], "PASS")
                self.assertEqual(
                    native_proof["export"]["method"],
                    "verified-native-mcp:export_frames",
                )
                self.assertEqual(len(native_proof["export"]["files"]), 1)
                exported = Path(native_proof["export"]["files"][0]["path"])
                self.assertTrue(exported.is_file())
                self.assertEqual(native_proof["export"]["files"][0]["width"], 64)
                self.assertEqual(native_proof["export"]["files"][0]["height"], 42)
                self.assertEqual(
                    document.read_bytes(),
                    Path(result["working_document"]).read_bytes(),
                    "native export must not change source or private working copy",
                )
                repeated = self._run(
                    "native-export",
                    "--state-dir",
                    str(state),
                    "--output-dir",
                    str(native_output),
                    env=env,
                )
                self.assertNotEqual(repeated.returncode, 0)
                self.assertIn("output already exists", repeated.stderr)

                outside = root / "outside"
                outside.mkdir()
                escaped_parent = root / "escaped-output-parent"
                os.symlink(outside, escaped_parent)
                escaped = self._run(
                    "native-export",
                    "--state-dir",
                    str(state),
                    "--output-dir",
                    str(escaped_parent / "export"),
                    env=env,
                )
                self.assertNotEqual(escaped.returncode, 0)
                self.assertIn("must not traverse a symlink", escaped.stderr)
                self.assertEqual(list(outside.iterdir()), [])

                document.write_text(
                    json.dumps({"version": "drifted", "children": []}),
                    encoding="utf-8",
                )
                drifted_output = root / "drifted-native-output"
                drifted = self._run(
                    "native-export",
                    "--state-dir",
                    str(state),
                    "--output-dir",
                    str(drifted_output),
                    env=env,
                )
                self.assertNotEqual(drifted.returncode, 0)
                self.assertIn("changed since this private session started", drifted.stderr)
                self.assertFalse(drifted_output.exists())
                document.write_bytes(original_source)

                checked = self._run(
                    "check",
                    "--state-dir",
                    str(state),
                    "--document",
                    str(document),
                    "--expected-nodes",
                    "1",
                    "--expected-document-sha256",
                    hashlib.sha256(document.read_bytes()).hexdigest(),
                    "--export",
                    str(reviewed_export),
                    "--expected-export-sha256",
                    hashlib.sha256(reviewed_export.read_bytes()).hexdigest(),
                    env=env,
                )
                self.assertEqual(checked.returncode, 0, checked.stderr)
                proof = json.loads(checked.stdout)
                self.assertEqual(proof["status"], "PASS")
                self.assertTrue(proof["canvasKit"]["identical"])
                self.assertEqual(proof["browser_opening"], "harness-owned")
                self.assertEqual(proof["locale"]["value"], "en-US")
                self.assertTrue(proof["locale"]["served"])

                with urllib.request.urlopen(result["url"], timeout=2) as response:
                    html = response.read().decode("utf-8")
                    self.assertIn("ads-openpencil-fresh-locale", html)
                    self.assertIn("openpencil-rust-web-settings::anon", html)
                    self.assertIn('locale:"en-US"', html)

                with urllib.request.urlopen(
                    f"{result['origin']}/pkg/canvaskit/canvaskit.js", timeout=2
                ) as response:
                    self.assertEqual(response.status, 200)
                    self.assertEqual(response.read(), b"fake-canvaskit-js")

                bounded_logs = self._run(
                    "logs", "--state-dir", str(state), "--lines", "20", env=env
                )
                self.assertEqual(bounded_logs.returncode, 0, bounded_logs.stderr)
                self.assertIn("fake OpenPencil daemon ready", bounded_logs.stdout)
                self.assertFalse(opened.exists(), "an OS or Zen browser was invoked")
            finally:
                stopped = self._run("stop", "--state-dir", str(state), env=env)
                self.assertEqual(stopped.returncode, 0, stopped.stderr)

            self.assertFalse(state.exists())
            with self.assertRaises((urllib.error.URLError, TimeoutError)):
                urllib.request.urlopen(result["url"], timeout=1)
            stopped_status = self._run(
                "status", "--state-dir", str(state), env=env
            )
            self.assertEqual(stopped_status.returncode, 0, stopped_status.stderr)
            self.assertEqual(json.loads(stopped_status.stdout)["status"], "stopped")

    def test_legacy_live_state_requires_restart_without_mutation(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            document = self._document(root)
            runtime = self._runtime(root)
            state = root / "legacy-state"
            state.mkdir()

            class LegacyStatus(http.server.BaseHTTPRequestHandler):
                def do_GET(self):
                    if self.path != "/__ads_workbench/status":
                        self.send_error(404)
                        return
                    body = json.dumps(
                        {
                            "schema": "ADS-OPENPENCIL-WORKBENCH/1",
                            "status": "running",
                        }
                    ).encode("utf-8")
                    self.send_response(200)
                    self.send_header("content-type", "application/json")
                    self.send_header("content-length", str(len(body)))
                    self.end_headers()
                    self.wfile.write(body)

                def log_message(self, format, *arguments):
                    return

            server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), LegacyStatus)
            worker = threading.Thread(target=server.serve_forever, daemon=True)
            worker.start()
            state_file = state / "state.json"
            original = {
                "schema": "ADS-OPENPENCIL-WORKBENCH/1",
                "status": "running",
                "origin": f"http://127.0.0.1:{server.server_port}",
                "control_token": "legacy-control-token",
                "document": str(document.resolve()),
                "document_sha256": hashlib.sha256(document.read_bytes()).hexdigest(),
            }
            before = json.dumps(original, indent=2) + "\n"
            state_file.write_text(before, encoding="utf-8")
            try:
                resumed = self._run(
                    "start",
                    "--runtime-root",
                    str(runtime),
                    "--document",
                    str(document),
                    "--state-dir",
                    str(state),
                )
                self.assertNotEqual(resumed.returncode, 0)
                self.assertIn(
                    "predates private working-document isolation", resumed.stderr
                )
                self.assertEqual(state_file.read_text(encoding="utf-8"), before)
                self.assertFalse((state / "document").exists())
                self.assertTrue(worker.is_alive())
            finally:
                server.shutdown()
                server.server_close()
                worker.join(timeout=2)

    def test_business_freedom_reviewed_native_artifacts_are_stable(self):
        source = ROOT / "workspace/designs/ads-business-freedom-content-e2e-r1/openpencil/route-console.op"
        reviewed_export = (
            ROOT / "workspace/designs/ads-business-freedom-content-e2e-r1/openpencil/exports/route-console.png"
        )
        document = json.loads(source.read_text(encoding="utf-8"))

        def nodes(value: object) -> int:
            if isinstance(value, list):
                return sum(nodes(item) for item in value)
            if not isinstance(value, dict):
                return 0
            current = int(isinstance(value.get("id"), str) and isinstance(value.get("type"), str))
            return current + sum(nodes(item) for item in value.values())

        self.assertEqual(nodes(document), 314)
        self.assertEqual(
            hashlib.sha256(source.read_bytes()).hexdigest(),
            "33ab74b5315b89f68eefe8b6a3d3da193e968afab6f851de3c9f3b2f97b9b0e0",
        )
        self.assertEqual(
            hashlib.sha256(reviewed_export.read_bytes()).hexdigest(),
            "734c32836a61c42088141d84308392a198403d6e4a80991f65d3d2f9a8b5e92d",
        )


if __name__ == "__main__":
    unittest.main()
