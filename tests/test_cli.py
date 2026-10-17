import contextlib
import io
import json
import os
import tempfile
import unittest
from pathlib import Path

from roi_dashboard.cli import main

OUTPUT_NAMES = ["roi-2026-09.html", "roi-2026-09.json"]


def run_build(out_dir, month="2026-09"):
    with contextlib.redirect_stdout(io.StringIO()):
        return main(["build", "--month", month, "--out-dir", str(out_dir)])


class BuildCommandTest(unittest.TestCase):
    def test_build_writes_one_html_file_and_one_json_file(self):
        with tempfile.TemporaryDirectory() as out_dir:
            self.assertEqual(run_build(out_dir), 0)
            self.assertEqual(sorted(os.listdir(out_dir)), OUTPUT_NAMES)

    def test_json_report_covers_the_requested_month(self):
        with tempfile.TemporaryDirectory() as out_dir:
            run_build(out_dir)
            report = json.loads(Path(out_dir, "roi-2026-09.json").read_text(encoding="utf-8"))
        self.assertEqual(report["month"], "2026-09")
        self.assertEqual(len(report["departments"]), 4)

    def test_repeated_builds_are_byte_identical(self):
        with tempfile.TemporaryDirectory() as first, tempfile.TemporaryDirectory() as second:
            run_build(first)
            run_build(second)
            for name in OUTPUT_NAMES:
                self.assertEqual(Path(first, name).read_bytes(), Path(second, name).read_bytes())

    def test_rejects_a_malformed_month(self):
        with tempfile.TemporaryDirectory() as out_dir:
            with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
                run_build(out_dir, month="2026-9")


if __name__ == "__main__":
    unittest.main()
