from __future__ import annotations

import base64
import hashlib
import json
import os
import re
import shutil
import subprocess
import tempfile
import unittest
import urllib.error
import urllib.parse
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
const http = require("node:http");
const args = process.argv.slice(2);
if (args.includes("--managed")) {
  process.stderr.write("managed mode requires an external credential injector\\n");
  process.exit(64);
}
const value = (flag, fallback) => {
  const index = args.indexOf(flag);
  return index >= 0 ? args[index + 1] : fallback;
};
const host = value("--host", "127.0.0.1");
const requestedPort = Number(value("--port", "0"));
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

    def _evaluate_language_bootstrap(
        self, html: str, initial: dict[str, str]
    ) -> dict[str, object]:
        match = re.search(
            r"<script[^>]+data-ads-openpencil-language-bootstrap[^>]*>(.*?)</script>",
            html,
            re.DOTALL,
        )
        self.assertIsNotNone(match, "language bootstrap script is unavailable")
        harness = r"""
const vm = require("node:vm");
const source = Buffer.from(process.argv[1], "base64").toString("utf8");
const initial = JSON.parse(Buffer.from(process.argv[2], "base64").toString("utf8"));
const values = new Map(Object.entries(initial));
const localStorage = {
  get length() { return values.size; },
  key(index) { return [...values.keys()][index] ?? null; },
  getItem(key) { return values.has(key) ? values.get(key) : null; },
  setItem(key, value) { values.set(key, String(value)); },
};
const location = {
  replaced: null,
  replace(value) { this.replaced = value; },
};
vm.runInNewContext(source, {localStorage, location});
process.stdout.write(JSON.stringify({
  storage: Object.fromEntries(values),
  redirect: location.replaced,
}));
"""
        completed = subprocess.run(
            [
                NODE,
                "-e",
                harness,
                base64.b64encode(match.group(1).encode()).decode(),
                base64.b64encode(json.dumps(initial).encode()).decode(),
            ],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        return json.loads(completed.stdout)

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

    def test_fresh_origin_defaults_to_english_without_overwriting_user_locale(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            runtime = self._runtime(root)
            document = self._document(root)
            state = root / "state"
            started = self._run(
                "start",
                "--runtime-root",
                str(runtime),
                "--document",
                str(document),
                "--state-dir",
                str(state),
            )
            try:
                self.assertEqual(started.returncode, 0, started.stderr)
                result = json.loads(started.stdout)
                self.assertEqual(result["language_default"], "en-US")
                self.assertEqual(result["language_policy"], "seed-when-absent")
                self.assertEqual(
                    result["language_preference"],
                    "openpencil-rust-web-settings::<profile>",
                )

                with urllib.request.urlopen(result["url"], timeout=2) as response:
                    self.assertEqual(response.status, 200)
                    self.assertIn(
                        "script-src 'nonce-ads-openpencil-language'",
                        response.headers.get("Content-Security-Policy", ""),
                    )
                    bootstrap = response.read().decode()

                fresh = self._evaluate_language_bootstrap(bootstrap, {})
                seeded = json.loads(
                    fresh["storage"]["openpencil-rust-web-settings::anon"]
                )
                self.assertEqual(seeded, {"version": 1, "locale": "en-US"})
                self.assertEqual(
                    fresh["redirect"], "/?__ads_openpencil_language_ready=1"
                )

                existing = json.dumps(
                    {"version": 1, "locale": "zh-CN", "theme": "dark"}
                )
                overridden = self._evaluate_language_bootstrap(
                    bootstrap,
                    {"openpencil-rust-web-settings::anon": existing},
                )
                self.assertEqual(
                    overridden["storage"],
                    {"openpencil-rust-web-settings::anon": existing},
                )

                with urllib.request.urlopen(
                    f"{result['origin']}/?__ads_openpencil_language_ready=1",
                    timeout=2,
                ) as response:
                    self.assertEqual(response.status, 200)
                    self.assertIn(b"<canvas id=op>", response.read())
            finally:
                stopped = self._run("stop", "--state-dir", str(state))
                self.assertEqual(stopped.returncode, 0, stopped.stderr)

            self.assertFalse(state.exists())

    def test_language_bootstrap_does_not_reflect_request_query(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            runtime = self._runtime(root)
            document = self._document(root)
            state = root / "state"
            started = self._run(
                "start",
                "--runtime-root",
                str(runtime),
                "--document",
                str(document),
                "--state-dir",
                str(state),
            )
            try:
                self.assertEqual(started.returncode, 0, started.stderr)
                result = json.loads(started.stdout)
                payload = (
                    '</script><script nonce="ads-openpencil-language">'
                    "globalThis.adsBootstrapPwned=1</script>"
                )
                encoded_payload = urllib.parse.quote(payload, safe="")
                with urllib.request.urlopen(
                    f"{result['url']}?probe={encoded_payload}", timeout=2
                ) as response:
                    self.assertEqual(response.status, 200)
                    bootstrap = response.read().decode()

                self.assertNotIn("adsBootstrapPwned", bootstrap)
                self.assertNotIn(encoded_payload, bootstrap)
                self.assertEqual(bootstrap.count("<script"), 1)
                evaluated = self._evaluate_language_bootstrap(bootstrap, {})
                self.assertEqual(
                    evaluated["redirect"],
                    "/?__ads_openpencil_language_ready=1",
                )
            finally:
                stopped = self._run("stop", "--state-dir", str(state))
                self.assertEqual(stopped.returncode, 0, stopped.stderr)

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

                status = self._run("status", "--state-dir", str(state), env=env)
                self.assertEqual(status.returncode, 0, status.stderr)
                self.assertEqual(json.loads(status.stdout)["status"], "running")

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
                self.assertEqual(
                    proof["language"],
                    {
                        "default": "en-US",
                        "preference": "openpencil-rust-web-settings::<profile>",
                        "policy": "seed-when-absent",
                    },
                )
                self.assertEqual(proof["browser_opening"], "harness-owned")

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

    def test_business_freedom_reviewed_native_artifacts_are_stable(self):
        source = ROOT / "workspace/openpencil/route-console.op"
        reviewed_export = (
            ROOT / "workspace/openpencil/exports/route-console.png"
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
