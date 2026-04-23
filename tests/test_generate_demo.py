import pathlib
import unittest

from generate_demo import (
    BODY_AVAILABLE_HEIGHT,
    build_demo_plan,
    build_no_zoom_validation_plan,
    parse_case_markdown,
)


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
        self.assertTrue(plan["layout_metrics"])
        self.assertFalse(any(metric["overflow"] for metric in plan["layout_metrics"]))

    def test_no_zoom_validation_fixture_splits_tall_block_before_render(self) -> None:
        plan = build_no_zoom_validation_plan()
        metrics = plan["layout_metrics"]

        self.assertGreaterEqual(len(plan["slides"]), 2)
        self.assertEqual(metrics[0]["split_count"], len(plan["slides"]))
        self.assertTrue(metrics[0]["split_required"])
        self.assertTrue(all(not metric["overflow"] for metric in metrics))
        self.assertTrue(all(metric["safe_area_available_height"] == BODY_AVAILABLE_HEIGHT for metric in metrics))
        self.assertTrue(all("当前在看：完整承接路径" in slide["title"] for slide in plan["slides"]))
        self.assertTrue(all(slide["badge"] == "正确做法" for slide in plan["slides"]))
        self.assertTrue(all("拆两拍" in slide["footer"] for slide in plan["slides"]))


if __name__ == "__main__":
    unittest.main()
