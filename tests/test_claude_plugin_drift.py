import filecmp
import unittest
from pathlib import Path

class TestClaudePluginDrift(unittest.TestCase):
    def test_task_support_skill_drift(self):
        repo_root = Path(__file__).resolve().parent.parent
        canonical_skill = repo_root / "skills" / "diffyn-task-support" / "SKILL.md"
        plugin_skill = repo_root / "integrations" / "claude-code" / "diffyn" / "skills" / "diffyn-task-support" / "SKILL.md"

        self.assertTrue(canonical_skill.exists(), f"Canonical skill missing: {canonical_skill}")
        self.assertTrue(plugin_skill.exists(), f"Plugin skill missing: {plugin_skill}")
        self.assertTrue(
            filecmp.cmp(canonical_skill, plugin_skill, shallow=False),
            "Drift detected: Plugin SKILL.md does not match the canonical copy."
        )

if __name__ == "__main__":
    unittest.main()