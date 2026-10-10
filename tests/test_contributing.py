"""Check the contribution documentation required by issue #5."""

from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]


class ContributingTests(unittest.TestCase):
    def test_guide_is_short_and_explains_the_process(self):
        guide = (ROOT / "CONTRIBUTING.md").read_text(encoding="utf-8")
        self.assertLess(len(guide.splitlines()), 40)
        for requirement in (
            "open an issue labelled `dcl`",
            "Goal:",
            "Acceptance criteria:",
            "draft pull requests for review",
        ):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement, guide)

    def test_readme_links_to_guide(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertRegex(readme, re.compile(r"\[[^\]]+\]\(CONTRIBUTING\.md\)"))


if __name__ == "__main__":
    unittest.main()
