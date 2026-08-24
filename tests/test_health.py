import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from finn_loop_sandbox import health


class HealthTests(unittest.TestCase):
    def test_health(self):
        self.assertEqual(health(), "ok")


if __name__ == "__main__":
    unittest.main()
