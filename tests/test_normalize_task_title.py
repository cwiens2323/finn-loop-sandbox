import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from finn_loop_sandbox import normalize_task_title


class NormalizeTaskTitleTests(unittest.TestCase):
    def test_normal_title_is_unchanged(self):
        self.assertEqual(normalize_task_title("Build release notes"), "Build release notes")

    def test_repeated_whitespace_is_collapsed(self):
        self.assertEqual(
            normalize_task_title("  Build\t release\nnotes  "),
            "Build release notes",
        )

    def test_empty_and_whitespace_only_titles_are_empty(self):
        self.assertEqual(normalize_task_title(""), "")
        self.assertEqual(normalize_task_title(" \t\n "), "")


if __name__ == "__main__":
    unittest.main()
