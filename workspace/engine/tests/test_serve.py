from __future__ import annotations

import re
import subprocess
import tempfile
import unittest
import urllib.error
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
SCRIPT = ROOT / "workspace/engine/serve.mjs"


class PreviewServerTests(unittest.TestCase):
    def _root(self, temporary: str) -> tuple[Path, Path]:
        root = Path(temporary) / "checkout"
        design = root / "workspace/designs/selected-design"
        design.mkdir(parents=True)
        for name in ("BRIEF.md", "DESIGN.md"):
            (design / name).write_text(f"# {name}\n", encoding="utf-8")
        (design / "index.html").write_text("<main>Selected preview</main>\n", encoding="utf-8")
        return root, design

    def test_preview_binds_loopback_and_rejects_escape_symlinks_and_bad_urls(self):
        with tempfile.TemporaryDirectory() as temporary:
            root, design = self._root(temporary)
            outside = Path(temporary) / "outside.txt"
            outside.write_text("must not serve", encoding="utf-8")
            (design / "outside.txt").symlink_to(outside)
            process = subprocess.Popen(
                ["node", str(SCRIPT), "--design", "selected-design", "--port", "0"],
                cwd=root,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            try:
                line = process.stdout.readline() if process.stdout else ""
                match = re.search(r"http://127\.0\.0\.1:(\d+)", line)
                self.assertIsNotNone(match, line)
                origin = f"http://127.0.0.1:{match.group(1)}"
                self.assertEqual(
                    urllib.request.urlopen(origin, timeout=2).read(), b"<main>Selected preview</main>\n"
                )
                for path in ("/outside.txt", "/..%2Foutside.txt"):
                    with self.assertRaises(urllib.error.HTTPError) as request:
                        urllib.request.urlopen(origin + path, timeout=2)
                    self.assertEqual(request.exception.code, 404)
                    request.exception.close()
                with self.assertRaises(urllib.error.HTTPError) as request:
                    urllib.request.urlopen(origin + "/%E0%A4%A", timeout=2)
                self.assertEqual(request.exception.code, 400)
                request.exception.close()
            finally:
                process.terminate()
                try:
                    process.wait(timeout=3)
                except subprocess.TimeoutExpired:
                    process.kill()
                    process.wait(timeout=3)
                if process.stdout:
                    process.stdout.close()
                if process.stderr:
                    process.stderr.close()

    def test_preview_refuses_a_symlinked_collection(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary) / "checkout"
            outside = Path(temporary) / "outside"
            (outside / "selected-design").mkdir(parents=True)
            (root / "workspace").mkdir(parents=True)
            (root / "workspace/designs").symlink_to(outside)
            result = subprocess.run(
                ["node", str(SCRIPT), "--design", "selected-design", "--port", "0"],
                cwd=root,
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("must be a regular directory", result.stderr)


if __name__ == "__main__":
    unittest.main()
