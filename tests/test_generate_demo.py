import pathlib
import unittest

from generate_demo import build_demo_plan, parse_case_markdown


ROOT = pathlib.Path(__file__).resolve().parents[1]
CASE_PATH = ROOT / "cases" / "demo.md"


class DemoPipelineTests(unittest.TestCase):
    def test_parse_case_markdown_reads_core_fields(self) -> None:
        case = parse_case_markdown(CASE_PATH)

        self.assertEqual(case["title"], "把模糊 AI 想法整理成可执行方案")
        self.assertEqual(case["video_params"]["页数"], "3页")
        self.assertIn("表达混乱", case["target_user"])
        self.assertIn("继续做下一版案例整理", case["cta"])

    def test_build_demo_plan_creates_three_slides_and_captions(self) -> None:
        case = parse_case_markdown(CASE_PATH)
        plan = build_demo_plan(case)

        self.assertEqual(len(plan["slides"]), 3)
        self.assertEqual(len(plan["captions"]), 3)
        self.assertIn("先把模糊想法压成目标、边界、步骤", plan["script"])
        self.assertTrue(plan["captions"][0]["text"].startswith("很多 AI 项目"))


if __name__ == "__main__":
    unittest.main()
