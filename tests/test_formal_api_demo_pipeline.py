import pathlib
import tempfile
import unittest

from formal_api_demo_core import (
    FORMAL_CASE_PATH,
    FORMAL_EXAMPLE_CONFIG_PATH,
    STATUS_BLOCKED,
    STATUS_PLANNED,
    parse_formal_case_markdown,
    run_assembly_pipeline,
    run_generation_pipeline,
)


ROOT = pathlib.Path(__file__).resolve().parents[1]


class FormalApiDemoPipelineTests(unittest.TestCase):
    def test_parse_formal_case_markdown_reads_core_fields(self) -> None:
        spec = parse_formal_case_markdown(FORMAL_CASE_PATH)

        self.assertEqual(spec["theme"], "把散乱的 AI 工作流整理成可执行 SOP")
        self.assertEqual(spec["total_duration_seconds"], 15.0)
        self.assertEqual(spec["aspect_ratio"], "9:16")
        self.assertEqual(len(spec["segments"]), 3)
        self.assertEqual(spec["segments"][0]["segment_id"], "seg01")
        self.assertTrue(spec["segments"][1]["needs_video"])

    def test_parse_formal_case_markdown_raises_for_missing_hook(self) -> None:
        with tempfile.TemporaryDirectory(prefix="formal_case_") as temp_dir:
            temp_path = pathlib.Path(temp_dir) / "invalid.md"
            temp_path.write_text(
                "\n".join(
                    [
                        "# 主题",
                        "测试缺 hook",
                        "",
                        "## 基础参数",
                        "- 总时长：15秒",
                        "- 视频比例：9:16",
                        "",
                        "## 目标场景",
                        "AI 项目讲解",
                        "",
                        "## 目标用户",
                        "测试用户",
                        "",
                        "## 全局质量要求",
                        "- 开头 3 秒必须有 hook",
                        "",
                        "## 结尾落点",
                        "测试结尾",
                        "",
                        "## 分段结构",
                        "### 第1段",
                        "- 段落ID：seg01",
                        "- 计划时长：5秒",
                        "- 段目标：测试目标",
                        "- 配音文案：测试配音",
                        "- 字幕文案：测试字幕",
                        "- 画面意图：测试画面",
                        "- 需要图片：是",
                        "- 需要视频：否",
                        "- 允许真实桌面素材：否",
                    ]
                ),
                encoding="utf-8",
            )

            with self.assertRaisesRegex(ValueError, "缺少必填章节：Hook"):
                parse_formal_case_markdown(temp_path)

    def test_generate_dry_run_outputs_manifest_and_result_summary(self) -> None:
        with tempfile.TemporaryDirectory(prefix="formal_generate_") as temp_dir:
            output_dir = pathlib.Path(temp_dir) / "dist"
            result = run_generation_pipeline(
                input_path=FORMAL_CASE_PATH,
                example_config_path=FORMAL_EXAMPLE_CONFIG_PATH,
                local_config_path=None,
                output_dir=output_dir,
                dry_run=True,
            )

            self.assertEqual(result["overall_status"], STATUS_PLANNED)
            self.assertEqual(result["generation_status"], STATUS_PLANNED)
            self.assertTrue((output_dir / "manifest.json").exists())
            self.assertTrue((output_dir / "generation_gate.json").exists())
            self.assertTrue((output_dir / "result_summary.json").exists())
            self.assertIn("access_key_id", result["current_missing_prerequisites"])

    def test_assemble_dry_run_reads_manifest_and_outputs_result_summary(self) -> None:
        with tempfile.TemporaryDirectory(prefix="formal_assemble_") as temp_dir:
            output_dir = pathlib.Path(temp_dir) / "dist"
            run_generation_pipeline(
                input_path=FORMAL_CASE_PATH,
                example_config_path=FORMAL_EXAMPLE_CONFIG_PATH,
                local_config_path=None,
                output_dir=output_dir,
                dry_run=True,
            )

            result = run_assembly_pipeline(
                manifest_path=output_dir / "manifest.json",
                example_config_path=FORMAL_EXAMPLE_CONFIG_PATH,
                local_config_path=None,
                output_dir=output_dir,
                dry_run=True,
            )

            self.assertEqual(result["overall_status"], STATUS_PLANNED)
            self.assertEqual(result["assembly_status"], STATUS_PLANNED)
            self.assertTrue((output_dir / "assembly_gate.json").exists())
            self.assertTrue((output_dir / "assembly_plan.json").exists())
            self.assertTrue((output_dir / "result_summary.json").exists())

    def test_generate_non_dry_run_without_local_config_blocks(self) -> None:
        with tempfile.TemporaryDirectory(prefix="formal_blocked_") as temp_dir:
            output_dir = pathlib.Path(temp_dir) / "dist"
            result = run_generation_pipeline(
                input_path=FORMAL_CASE_PATH,
                example_config_path=FORMAL_EXAMPLE_CONFIG_PATH,
                local_config_path=None,
                output_dir=output_dir,
                dry_run=False,
            )

            self.assertEqual(result["overall_status"], STATUS_BLOCKED)
            self.assertEqual(result["generation_status"], STATUS_BLOCKED)
            self.assertNotEqual(result["blocked_reason"], "")


if __name__ == "__main__":
    unittest.main()
