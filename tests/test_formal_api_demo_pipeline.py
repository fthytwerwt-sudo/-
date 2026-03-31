import pathlib
import tempfile
import unittest
from unittest import mock

from formal_api_demo_core import (
    FORMAL_CASE_PATH,
    FORMAL_EXAMPLE_CONFIG_PATH,
    STATUS_BLOCKED,
    STATUS_FAILED,
    STATUS_PLANNED,
    STATUS_SUCCESS,
    parse_formal_case_markdown,
    run_assembly_pipeline,
    run_generation_pipeline,
)


ROOT = pathlib.Path(__file__).resolve().parents[1]


class FormalApiDemoPipelineTests(unittest.TestCase):
    def _write_local_config(self, path: pathlib.Path, *, api_key: str = "", model: str = "", endpoint_id: str = "", voice: str = "zh_female_test", style: str = "knowledge") -> None:
        path.write_text(
            "\n".join(
                [
                    "[provider]",
                    'name = "volcengine"',
                    'region = "cn-beijing"',
                    "",
                    "[auth]",
                    f'api_key = "{api_key}"',
                    "",
                    "[tts]",
                    f'model = "{model}"',
                    f'endpoint_id = "{endpoint_id}"',
                    f'voice = "{voice}"',
                    f'style = "{style}"',
                    'response_format = "mp3"',
                ]
            )
            + "\n",
            encoding="utf-8",
        )

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
            self.assertIn("api_key", result["current_missing_prerequisites"])

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

    def test_generate_non_dry_run_with_local_config_but_missing_api_key_blocks(self) -> None:
        with tempfile.TemporaryDirectory(prefix="formal_tts_missing_key_") as temp_dir:
            output_dir = pathlib.Path(temp_dir) / "dist"
            local_config_path = pathlib.Path(temp_dir) / "formal_api_demo.local.toml"
            self._write_local_config(
                local_config_path,
                api_key="",
                endpoint_id="ep_tts_demo",
            )

            result = run_generation_pipeline(
                input_path=FORMAL_CASE_PATH,
                example_config_path=FORMAL_EXAMPLE_CONFIG_PATH,
                local_config_path=local_config_path,
                output_dir=output_dir,
                dry_run=False,
            )

            self.assertEqual(result["overall_status"], STATUS_BLOCKED)
            self.assertIn("api_key", result["current_missing_prerequisites"])

    def test_generate_non_dry_run_with_missing_model_identifier_blocks(self) -> None:
        with tempfile.TemporaryDirectory(prefix="formal_tts_missing_model_") as temp_dir:
            output_dir = pathlib.Path(temp_dir) / "dist"
            local_config_path = pathlib.Path(temp_dir) / "formal_api_demo.local.toml"
            self._write_local_config(
                local_config_path,
                api_key="ark_test_key",
                model="",
                endpoint_id="",
            )

            result = run_generation_pipeline(
                input_path=FORMAL_CASE_PATH,
                example_config_path=FORMAL_EXAMPLE_CONFIG_PATH,
                local_config_path=local_config_path,
                output_dir=output_dir,
                dry_run=False,
            )

            self.assertEqual(result["overall_status"], STATUS_BLOCKED)
            self.assertIn("tts_model_or_endpoint", result["current_missing_prerequisites"])

    def test_generate_non_dry_run_marks_failed_when_tts_probe_fails(self) -> None:
        with tempfile.TemporaryDirectory(prefix="formal_tts_failed_") as temp_dir:
            output_dir = pathlib.Path(temp_dir) / "dist"
            local_config_path = pathlib.Path(temp_dir) / "formal_api_demo.local.toml"
            self._write_local_config(
                local_config_path,
                api_key="ark_test_key",
                endpoint_id="ep_tts_demo",
            )

            with mock.patch(
                "formal_api_demo_core.execute_tts_probe",
                return_value={
                    "status": STATUS_FAILED,
                    "blocked_reason": "",
                    "failure_reason": "ark_tts_request_failed",
                    "error_code": "BadGateway",
                    "error_message": "upstream timeout",
                    "audio_path": None,
                    "request_id": None,
                    "model_identifier": "ep_tts_demo",
                    "probe_text": "测试配音",
                    "voice": "zh_female_test",
                    "used_endpoint_id": "ep_tts_demo",
                },
            ):
                result = run_generation_pipeline(
                    input_path=FORMAL_CASE_PATH,
                    example_config_path=FORMAL_EXAMPLE_CONFIG_PATH,
                    local_config_path=local_config_path,
                    output_dir=output_dir,
                    dry_run=False,
                )

            self.assertEqual(result["overall_status"], STATUS_FAILED)
            self.assertEqual(result["generation_status"], STATUS_FAILED)

    def test_generate_non_dry_run_marks_success_when_tts_probe_succeeds(self) -> None:
        with tempfile.TemporaryDirectory(prefix="formal_tts_success_") as temp_dir:
            output_dir = pathlib.Path(temp_dir) / "dist"
            local_config_path = pathlib.Path(temp_dir) / "formal_api_demo.local.toml"
            self._write_local_config(
                local_config_path,
                api_key="ark_test_key",
                endpoint_id="ep_tts_demo",
            )

            def fake_probe(*_args, **_kwargs):
                audio_path = output_dir / "tts" / "voice_probe.mp3"
                audio_path.parent.mkdir(parents=True, exist_ok=True)
                audio_path.write_bytes(b"fake-mp3")
                return {
                    "status": STATUS_SUCCESS,
                    "blocked_reason": "",
                    "failure_reason": "",
                    "error_code": "",
                    "error_message": "",
                    "audio_path": str(audio_path),
                    "request_id": "req_demo",
                    "model_identifier": "ep_tts_demo",
                    "probe_text": "测试配音",
                    "voice": "zh_female_test",
                    "used_endpoint_id": "ep_tts_demo",
                }

            with mock.patch("formal_api_demo_core.execute_tts_probe", side_effect=fake_probe):
                result = run_generation_pipeline(
                    input_path=FORMAL_CASE_PATH,
                    example_config_path=FORMAL_EXAMPLE_CONFIG_PATH,
                    local_config_path=local_config_path,
                    output_dir=output_dir,
                    dry_run=False,
                )

            self.assertEqual(result["overall_status"], STATUS_SUCCESS)
            self.assertEqual(result["generation_status"], STATUS_SUCCESS)
            self.assertTrue((output_dir / "tts" / "voice_probe.mp3").exists())


if __name__ == "__main__":
    unittest.main()
