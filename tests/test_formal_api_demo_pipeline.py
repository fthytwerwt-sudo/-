import json
import io
import pathlib
import tempfile
import unittest
import urllib.error
from unittest import mock

import httpx
import openai

from formal_api_demo_core import (
    FORMAL_CASE_PATH,
    FORMAL_EXAMPLE_CONFIG_PATH,
    STATUS_BLOCKED,
    STATUS_FAILED,
    STATUS_PLANNED,
    STATUS_SUCCESS,
    _build_preview_slides,
    parse_formal_case_markdown,
    run_aliyun_tts_style_probe_round2,
    run_aliyun_tts_style_probe_variants,
    run_assembly_pipeline,
    run_generation_pipeline,
)


ROOT = pathlib.Path(__file__).resolve().parents[1]


class FormalApiDemoPipelineTests(unittest.TestCase):
    @staticmethod
    def _fake_concatenate_audio_files(_input_paths, output_path) -> None:
        pathlib.Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        pathlib.Path(output_path).write_bytes(b"fake-merged-mp3")

    def _write_local_config(
        self,
        path: pathlib.Path,
        *,
        provider_name: str = "volcengine",
        route_family: str = "ark_openai_compatible",
        api_key: str = "",
        app_id: str = "",
        model: str = "",
        endpoint_id: str = "",
        resource_id: str = "",
        voice: str = "zh_female_test",
        style: str = "knowledge",
        instruction: str = "",
        speech_rate: float = 1.0,
        pitch_rate: float = 1.0,
        volume: int = 50,
        image_model: str = "",
        video_model: str = "",
        portrait_detect_enabled: bool = False,
        portrait_detect_model: str = "liveportrait-detect",
        portrait_video_generation_enabled: bool = False,
        portrait_video_model: str = "liveportrait",
        template_id: str = "",
        space_name: str = "",
        polling_interval_seconds: int = 5,
        polling_timeout_seconds: int = 600,
    ) -> None:
        path.write_text(
            "\n".join(
                [
                    "[provider]",
                    f'name = "{provider_name}"',
                    'region = "cn-beijing"',
                    "",
                    "[auth]",
                    f'api_key = "{api_key}"',
                    f'app_id = "{app_id}"',
                    "",
                    "[tts]",
                    f'api_route_family = "{route_family}"',
                    f'model = "{model}"',
                    f'endpoint_id = "{endpoint_id}"',
                    f'resource_id = "{resource_id}"',
                    f'voice = "{voice}"',
                    f'style = "{style}"',
                    f'instruction = "{instruction}"',
                    f"speech_rate = {speech_rate}",
                    f"pitch_rate = {pitch_rate}",
                    f"volume = {volume}",
                    'response_format = "mp3"',
                    'baseline_profile = "aliyun_old_A"',
                    "",
                    "[image_generation]",
                    f'model = "{image_model}"',
                    "",
                    "[video_generation]",
                    f'model = "{video_model}"',
                    "",
                    "[portrait_detect]",
                    f"enabled = {'true' if portrait_detect_enabled else 'false'}",
                    f'model = "{portrait_detect_model}"',
                    "",
                    "[portrait_video_generation]",
                    f"enabled = {'true' if portrait_video_generation_enabled else 'false'}",
                    f'model = "{portrait_video_model}"',
                    "",
                    "[assembly]",
                    'mode = "cloud"',
                    f'template_id = "{template_id}"',
                    'subtitle_mode = "burn_in"',
                    'resolution = "1080x1920"',
                    "fps = 25",
                    "",
                    "[storage]",
                    f'space_name = "{space_name}"',
                    "",
                    "[polling]",
                    f"interval_seconds = {polling_interval_seconds}",
                    f"timeout_seconds = {polling_timeout_seconds}",
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

    def test_formal_case_seg02_copy_is_result_driven(self) -> None:
        spec = parse_formal_case_markdown(FORMAL_CASE_PATH)

        self.assertEqual(
            spec["segments"][1]["voiceover_text"],
            "目标、输入、输出一拉齐，这条链就接上了。",
        )
        self.assertEqual(
            spec["segments"][1]["caption_text"],
            "目标、输入、输出一拉齐，这条链就接上了。",
        )

    def test_preview_slides_expand_seg02_into_before_and_after_states(self) -> None:
        spec = parse_formal_case_markdown(FORMAL_CASE_PATH)
        manifest = {
            "segments": [
                {
                    "segment_id": segment["segment_id"],
                    "caption_text": segment["caption_text"],
                    "visual_intent": segment["visual_intent"],
                    "timeline": {
                        "planned_duration_seconds": segment["planned_duration_seconds"],
                    },
                }
                for segment in spec["segments"]
            ],
            "generation": {
                "visual_generation": {
                    "segment_assets": [
                        {
                            "segment_id": "seg01",
                            "image_asset_path": "/tmp/seg01.png",
                            "video_asset_path": None,
                        },
                        {
                            "segment_id": "seg02",
                            "image_asset_path": "/tmp/seg02_before.png",
                            "video_asset_path": "/tmp/seg02_after.mp4",
                        },
                        {
                            "segment_id": "seg03",
                            "image_asset_path": "/tmp/seg03.png",
                            "video_asset_path": None,
                        },
                    ]
                }
            },
        }

        slides = _build_preview_slides(manifest)

        self.assertEqual(len(slides), 4)
        self.assertEqual(
            [slide["role"] for slide in slides],
            ["hook", "hook", "process", "outcome"],
        )
        self.assertEqual(slides[1]["headline"], "目标、输入、口径、素材还散着。")
        self.assertEqual(slides[1]["chips"], ["便签堆满", "没人能接"])
        self.assertEqual(slides[1]["background_image_path"], "/tmp/seg02_before.png")
        self.assertEqual(slides[2]["headline"], "目标、输入、输出一拉齐，这条链就接上了。")
        self.assertEqual(slides[2]["chips"], ["目标", "输入", "输出"])
        self.assertEqual(slides[2]["background_video_path"], "/tmp/seg02_after.mp4")
        self.assertAlmostEqual(slides[1]["duration"] + slides[2]["duration"], 6.0)

    def test_formal_case_voiceover_copy_stays_within_current_timeline_budget(self) -> None:
        spec = parse_formal_case_markdown(FORMAL_CASE_PATH)
        budget_by_segment = {
            "seg01": 22,
            "seg02": 29,
            "seg03": 23,
        }

        for segment in spec["segments"]:
            segment_id = segment["segment_id"]
            self.assertLessEqual(
                len(segment["voiceover_text"]),
                budget_by_segment[segment_id],
                f"{segment_id} 配音文案超出当前 15 秒时间线预算",
            )
            self.assertLessEqual(
                len(segment["caption_text"]),
                budget_by_segment[segment_id],
                f"{segment_id} 字幕文案超出当前 15 秒时间线预算",
            )

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

    def test_assemble_non_dry_run_keeps_local_delivery_when_generation_is_still_blocked(self) -> None:
        with tempfile.TemporaryDirectory(prefix="formal_assemble_preview_") as temp_dir:
            output_dir = pathlib.Path(temp_dir) / "dist"
            local_config_path = pathlib.Path(temp_dir) / "formal_api_demo.local.toml"
            self._write_local_config(
                local_config_path,
                provider_name="volcengine",
                route_family="aliyun_bailian_cosyvoice",
                api_key="dashscope_test_key",
                model="cosyvoice-v3-flash",
                voice="longanyang",
                image_model="wan2.6-image",
                video_model="wan2.6-t2v",
            )

            def fake_probe(*_args, **kwargs):
                stem = kwargs.get("output_stem", "voice_probe")
                audio_path = output_dir / "tts" / f"{stem}.mp3"
                audio_path.parent.mkdir(parents=True, exist_ok=True)
                audio_path.write_bytes(b"fake-mp3")
                return {
                    "status": STATUS_SUCCESS,
                    "blocked_reason": "",
                    "failure_reason": "",
                    "error_code": "",
                    "error_message": "",
                    "audio_path": str(audio_path),
                    "request_id": f"req_{stem}",
                    "model_identifier": "cosyvoice-v3-flash",
                    "probe_text": "测试配音",
                    "voice": "longanyang",
                    "used_model_id": "cosyvoice-v3-flash",
                }

            with mock.patch("formal_api_demo_core.execute_tts_probe", side_effect=fake_probe), mock.patch(
                "formal_api_demo_core.concatenate_audio_files",
                side_effect=self._fake_concatenate_audio_files,
            ):
                run_generation_pipeline(
                    input_path=FORMAL_CASE_PATH,
                    example_config_path=FORMAL_EXAMPLE_CONFIG_PATH,
                    local_config_path=local_config_path,
                    output_dir=output_dir,
                    dry_run=False,
                )

            def fake_run_subprocess(args):
                if args and args[0] == "swift":
                    manifest_path = pathlib.Path(args[-1])
                    payload = json.loads(manifest_path.read_text(encoding="utf-8"))
                    pathlib.Path(payload["outputPath"]).write_bytes(b"fake-preview-mp4")
                    return
                raise AssertionError(f"unexpected subprocess args: {args}")

            with mock.patch("formal_api_demo_core.run_subprocess", side_effect=fake_run_subprocess):
                result = run_assembly_pipeline(
                    manifest_path=output_dir / "manifest.json",
                    example_config_path=FORMAL_EXAMPLE_CONFIG_PATH,
                    local_config_path=local_config_path,
                    output_dir=output_dir,
                    dry_run=False,
                )

            preview_manifest = json.loads(
                (output_dir / "assembly" / "preview_manifest.json").read_text(encoding="utf-8")
            )
            first_slide = preview_manifest["slides"][0]
            second_slide = preview_manifest["slides"][1]
            final_slide = preview_manifest["slides"][3]

            self.assertEqual(result["overall_status"], STATUS_BLOCKED)
            self.assertEqual(result["generation_status"], STATUS_BLOCKED)
            self.assertEqual(result["assembly_status"], STATUS_SUCCESS)
            self.assertEqual(result["local_assembly_status"], STATUS_SUCCESS)
            self.assertEqual(result["cloud_assembly_status"], STATUS_BLOCKED)
            self.assertEqual(result["assembly_preview_status"], STATUS_SUCCESS)
            self.assertIn("visual_assets_not_ready", result["current_missing_prerequisites"])
            self.assertTrue((output_dir / "final.mp4").exists())
            self.assertEqual(result["artifact_paths"]["final_video"], str(output_dir / "final.mp4"))
            self.assertTrue((output_dir / "assembly" / "formal_api_demo_preview.mp4").exists())
            self.assertEqual(first_slide["role"], "hook")
            self.assertEqual(first_slide["headline"], "AI 项目卡住，不是没思路，是流程还没拉齐。")
            self.assertEqual(second_slide["role"], "hook")
            self.assertEqual(second_slide["headline"], "目标、输入、口径、素材还散着。")
            self.assertEqual(preview_manifest["slides"][2]["role"], "process")
            self.assertEqual(preview_manifest["slides"][2]["chips"], ["目标", "输入", "输出"])
            self.assertEqual(final_slide["role"], "outcome")
            self.assertIn("先稳住样片", final_slide["chips"])
            self.assertNotIn("badge", first_slide)
            self.assertNotIn("footer", first_slide)

    def test_assemble_non_dry_run_delivers_local_mp4_when_visual_assets_ready(self) -> None:
        with tempfile.TemporaryDirectory(prefix="formal_local_impl_gap_") as temp_dir:
            output_dir = pathlib.Path(temp_dir) / "dist"
            local_config_path = pathlib.Path(temp_dir) / "formal_api_demo.local.toml"
            self._write_local_config(
                local_config_path,
                provider_name="aliyun_bailian",
                route_family="aliyun_bailian_cosyvoice",
                api_key="dashscope_test_key",
                model="cosyvoice-v3-flash",
                voice="longanyang",
                image_model="wanx2.1-image",
                video_model="wanx2.1-video",
            )

            def fake_probe(*_args, **kwargs):
                stem = kwargs.get("output_stem", "voice_probe")
                audio_path = output_dir / "tts" / f"{stem}.mp3"
                audio_path.parent.mkdir(parents=True, exist_ok=True)
                audio_path.write_bytes(b"fake-mp3")
                return {
                    "status": STATUS_SUCCESS,
                    "blocked_reason": "",
                    "failure_reason": "",
                    "error_code": "",
                    "error_message": "",
                    "audio_path": str(audio_path),
                    "request_id": f"req_{stem}",
                    "model_identifier": "cosyvoice-v3-flash",
                    "probe_text": "测试配音",
                    "voice": "longanyang",
                    "used_model_id": "cosyvoice-v3-flash",
                }

            with mock.patch("formal_api_demo_core.execute_tts_probe", side_effect=fake_probe), mock.patch(
                "formal_api_demo_core.concatenate_audio_files",
                side_effect=self._fake_concatenate_audio_files,
            ):
                run_generation_pipeline(
                    input_path=FORMAL_CASE_PATH,
                    example_config_path=FORMAL_EXAMPLE_CONFIG_PATH,
                    local_config_path=local_config_path,
                    output_dir=output_dir,
                    dry_run=False,
                )

            manifest_path = output_dir / "manifest.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["generation"]["status"] = STATUS_SUCCESS
            manifest["current_status"] = STATUS_SUCCESS
            manifest["status_summary"]["generation"] = STATUS_SUCCESS
            manifest["status_summary"]["overall_status"] = STATUS_SUCCESS
            manifest["generation"]["visual_generation"]["status"] = STATUS_SUCCESS
            manifest["generation"]["visual_generation"]["blocked_reason"] = ""
            manifest["generation"]["visual_generation"]["current_missing_prerequisites"] = []
            manifest["generation"]["visual_generation"]["missing_implementations"] = []
            manifest["generation"]["visual_generation"]["cloud"]["status"] = STATUS_SUCCESS
            manifest["generation"]["visual_generation"]["cloud"]["blocked_reason"] = ""
            manifest["generation"]["visual_generation"]["cloud"]["missing_prerequisites"] = []
            manifest["generation"]["visual_generation"]["cloud"]["missing_implementations"] = []

            for index, segment in enumerate(manifest["segments"], start=1):
                visual_path = output_dir / "visual_assets" / f"segment_{index}.png"
                visual_path.parent.mkdir(parents=True, exist_ok=True)
                visual_path.write_bytes(b"fake-visual")
                segment["output_slots"]["visual_uri"] = str(visual_path)
                manifest["generation"]["visual_generation"]["segment_assets"][index - 1]["image_asset_path"] = str(
                    visual_path
                )
                manifest["generation"]["visual_generation"]["segment_assets"][index - 1]["status"] = STATUS_SUCCESS

            manifest_path.write_text(
                json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )

            def fake_run_subprocess(args):
                if args and args[0] == "swift":
                    payload = json.loads(pathlib.Path(args[-1]).read_text(encoding="utf-8"))
                    pathlib.Path(payload["outputPath"]).write_bytes(b"fake-preview-mp4")
                    return
                raise AssertionError(f"unexpected subprocess args: {args}")

            with mock.patch("formal_api_demo_core.run_subprocess", side_effect=fake_run_subprocess):
                result = run_assembly_pipeline(
                    manifest_path=manifest_path,
                    example_config_path=FORMAL_EXAMPLE_CONFIG_PATH,
                    local_config_path=local_config_path,
                    output_dir=output_dir,
                    dry_run=False,
                )

            self.assertEqual(result["overall_status"], STATUS_SUCCESS)
            self.assertEqual(result["generation_status"], STATUS_SUCCESS)
            self.assertEqual(result["assembly_status"], STATUS_SUCCESS)
            self.assertEqual(result["local_assembly_status"], STATUS_SUCCESS)
            self.assertEqual(result["assembly_preview_status"], STATUS_SUCCESS)
            self.assertEqual(result["current_missing_implementations"], [])
            self.assertTrue((output_dir / "final.mp4").exists())
            self.assertEqual(result["artifact_paths"]["final_video"], str(output_dir / "final.mp4"))


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

    def test_generate_non_dry_run_aliyun_bailian_missing_api_key_blocks(self) -> None:
        with tempfile.TemporaryDirectory(prefix="formal_aliyun_missing_key_") as temp_dir:
            output_dir = pathlib.Path(temp_dir) / "dist"
            local_config_path = pathlib.Path(temp_dir) / "formal_api_demo.local.toml"
            self._write_local_config(
                local_config_path,
                provider_name="aliyun_bailian",
                route_family="aliyun_bailian_cosyvoice",
                api_key="",
                model="cosyvoice-v3-flash",
                voice="longxiaochun",
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

    def test_generate_non_dry_run_aliyun_bailian_missing_model_blocks(self) -> None:
        with tempfile.TemporaryDirectory(prefix="formal_aliyun_missing_model_") as temp_dir:
            output_dir = pathlib.Path(temp_dir) / "dist"
            local_config_path = pathlib.Path(temp_dir) / "formal_api_demo.local.toml"
            self._write_local_config(
                local_config_path,
                provider_name="aliyun_bailian",
                route_family="aliyun_bailian_cosyvoice",
                api_key="dashscope_test_key",
                model="",
                voice="longxiaochun",
            )

            result = run_generation_pipeline(
                input_path=FORMAL_CASE_PATH,
                example_config_path=FORMAL_EXAMPLE_CONFIG_PATH,
                local_config_path=local_config_path,
                output_dir=output_dir,
                dry_run=False,
            )

            self.assertEqual(result["overall_status"], STATUS_BLOCKED)
            self.assertIn("tts_model", result["current_missing_prerequisites"])

    def test_generate_non_dry_run_aliyun_bailian_downloads_local_visual_assets(self) -> None:
        with tempfile.TemporaryDirectory(prefix="formal_aliyun_success_") as temp_dir:
            output_dir = pathlib.Path(temp_dir) / "dist"
            local_config_path = pathlib.Path(temp_dir) / "formal_api_demo.local.toml"
            self._write_local_config(
                local_config_path,
                provider_name="aliyun_bailian",
                route_family="aliyun_bailian_cosyvoice",
                api_key="dashscope_test_key",
                model="cosyvoice-v3-flash",
                voice="longxiaochun",
                image_model="wan2.6-image",
                video_model="wan2.6-t2v",
            )

            class _JsonResponse:
                def __init__(self, payload: dict[str, object]) -> None:
                    self._payload = payload

                def __enter__(self):
                    return self

                def __exit__(self, exc_type, exc, tb):
                    return False

                def read(self) -> bytes:
                    return json.dumps(self._payload).encode("utf-8")

            class _BinaryResponse:
                def __enter__(self):
                    return self

                def __exit__(self, exc_type, exc, tb):
                    return False

                @staticmethod
                def read() -> bytes:
                    return b"fake-binary-asset"

            tts_counter = 0
            image_task_counter = 0
            video_task_counter = 0
            image_urls = {
                "img_task_1": "https://dashscope-result.example.com/image_seg01.png",
                "img_task_2": "https://dashscope-result.example.com/image_seg02.png",
                "img_task_3": "https://dashscope-result.example.com/image_seg03.png",
            }
            video_urls = {
                "vid_task_1": "https://dashscope-result.example.com/video_seg02.mp4",
            }
            download_payloads = {
                "https://dashscope-result.example.com/audio_1.mp3": b"aliyun-mp3-probe",
                "https://dashscope-result.example.com/audio_2.mp3": b"aliyun-mp3-seg01",
                "https://dashscope-result.example.com/audio_3.mp3": b"aliyun-mp3-seg02",
                "https://dashscope-result.example.com/audio_4.mp3": b"aliyun-mp3-seg03",
                image_urls["img_task_1"]: b"fake-image-seg01",
                image_urls["img_task_2"]: b"fake-image-seg02",
                image_urls["img_task_3"]: b"fake-image-seg03",
                video_urls["vid_task_1"]: b"fake-video-seg02",
            }

            def fake_urlopen(request, timeout=60):
                del timeout
                url = request.full_url
                if url.endswith("/services/audio/tts/SpeechSynthesizer"):
                    nonlocal tts_counter
                    tts_counter += 1
                    return _JsonResponse(
                        {
                            "request_id": f"aliyun_req_{tts_counter}",
                            "output": {
                                "finish_reason": "stop",
                                "audio": {
                                    "url": f"https://dashscope-result.example.com/audio_{tts_counter}.mp3",
                                    "id": f"audio_demo_{tts_counter}",
                                    "expires_at": 1772697707,
                                },
                            },
                        }
                    )
                if url.endswith("/services/aigc/image-generation/generation"):
                    nonlocal image_task_counter
                    image_task_counter += 1
                    return _JsonResponse(
                        {
                            "request_id": f"image_req_{image_task_counter}",
                            "output": {
                                "task_id": f"img_task_{image_task_counter}",
                                "task_status": "PENDING",
                            },
                        }
                    )
                if url.endswith("/services/aigc/video-generation/video-synthesis"):
                    nonlocal video_task_counter
                    video_task_counter += 1
                    return _JsonResponse(
                        {
                            "request_id": f"video_req_{video_task_counter}",
                            "output": {
                                "task_id": f"vid_task_{video_task_counter}",
                                "task_status": "PENDING",
                            },
                        }
                    )
                if "/api/v1/tasks/" in url:
                    task_id = url.rsplit("/", 1)[-1]
                    if task_id in image_urls:
                        return _JsonResponse(
                            {
                                "request_id": f"{task_id}_poll_req",
                                "output": {
                                    "task_id": task_id,
                                    "task_status": "SUCCEEDED",
                                    "finished": True,
                                    "choices": [
                                        {
                                            "finish_reason": "stop",
                                            "message": {
                                                "role": "assistant",
                                                "content": [
                                                    {
                                                        "type": "image",
                                                        "image": image_urls[task_id],
                                                    }
                                                ],
                                            },
                                        }
                                    ],
                                },
                            }
                        )
                    if task_id in video_urls:
                        return _JsonResponse(
                            {
                                "request_id": f"{task_id}_poll_req",
                                "output": {
                                    "task_id": task_id,
                                    "task_status": "SUCCEEDED",
                                    "video_url": video_urls[task_id],
                                },
                            }
                        )
                    raise AssertionError(f"unexpected task id: {task_id}")
                if url in download_payloads:
                    return _BinaryResponse()
                raise AssertionError(f"unexpected url: {url}")

            with mock.patch("formal_api_demo_core.urllib.request.urlopen", side_effect=fake_urlopen), mock.patch(
                "formal_api_demo_core.concatenate_audio_files",
                side_effect=self._fake_concatenate_audio_files,
            ):
                result = run_generation_pipeline(
                    input_path=FORMAL_CASE_PATH,
                    example_config_path=FORMAL_EXAMPLE_CONFIG_PATH,
                    local_config_path=local_config_path,
                    output_dir=output_dir,
                    dry_run=False,
                )

            manifest = json.loads((output_dir / "manifest.json").read_text(encoding="utf-8"))
            tts_probe = manifest["generation"]["tts_probe"]
            request_debug = tts_probe["request_debug"]
            audio_path = output_dir / "tts" / "voice_probe.mp3"

            self.assertEqual(result["tts_probe_status"], STATUS_SUCCESS)
            self.assertEqual(result["voiceover_status"], STATUS_SUCCESS)
            self.assertEqual(result["captions_status"], STATUS_SUCCESS)
            self.assertEqual(tts_probe["status"], STATUS_SUCCESS)
            self.assertEqual(request_debug["api_route_family"], "aliyun_bailian_cosyvoice")
            self.assertEqual(request_debug["provider"], "aliyun_bailian")
            self.assertEqual(request_debug["base_url"], "https://dashscope.aliyuncs.com/api/v1")
            self.assertEqual(
                request_debug["relative_path"],
                "/services/audio/tts/SpeechSynthesizer",
            )
            self.assertEqual(request_debug["model_identifier_source"], "model")
            self.assertTrue(audio_path.exists())
            self.assertEqual(audio_path.read_bytes(), b"fake-binary-asset")
            self.assertTrue((output_dir / "tts" / "formal_voiceover.mp3").exists())
            self.assertTrue((output_dir / "script.txt").exists())
            self.assertTrue((output_dir / "captions.srt").exists())
            self.assertTrue((output_dir / "visual_generation_plan.json").exists())
            self.assertTrue((output_dir / "preview_storyboard.json").exists())
            self.assertEqual(result["overall_status"], STATUS_SUCCESS)
            self.assertEqual(result["generation_status"], STATUS_SUCCESS)
            self.assertEqual(result["visual_generation_status"], STATUS_SUCCESS)
            self.assertEqual(result["cloud_visual_generation_status"], STATUS_SUCCESS)
            self.assertEqual(manifest["current_status"], STATUS_SUCCESS)
            self.assertEqual(
                manifest["generation"]["visual_generation"]["delivery_mode"],
                "api_generated_local_assets",
            )
            visual_assets = manifest["generation"]["visual_generation"]["segment_assets"]
            self.assertEqual(
                [asset["status"] for asset in visual_assets],
                [STATUS_SUCCESS, STATUS_SUCCESS, STATUS_SUCCESS],
            )
            self.assertTrue(pathlib.Path(visual_assets[0]["image_asset_path"]).exists())
            self.assertTrue(pathlib.Path(visual_assets[1]["image_asset_path"]).exists())
            self.assertTrue(pathlib.Path(visual_assets[1]["video_asset_path"]).exists())
            self.assertTrue(pathlib.Path(visual_assets[2]["image_asset_path"]).exists())
            self.assertEqual(
                pathlib.Path(manifest["segments"][0]["output_slots"]["visual_uri"]).read_bytes(),
                b"fake-binary-asset",
            )
            self.assertEqual(
                pathlib.Path(manifest["segments"][1]["output_slots"]["visual_uri"]).read_bytes(),
                b"fake-binary-asset",
            )
            self.assertEqual(
                pathlib.Path(manifest["segments"][2]["output_slots"]["visual_uri"]).read_bytes(),
                b"fake-binary-asset",
            )
            self.assertTrue(result["artifact_paths"]["visual_assets"])
            self.assertEqual(
                manifest["segments"][0]["task_slots"]["image_task_id"],
                "img_task_1",
            )
            self.assertEqual(
                manifest["segments"][1]["task_slots"]["video_task_id"],
                "vid_task_1",
            )
            self.assertEqual(
                manifest["segments"][1]["task_slots"]["image_task_id"],
                "img_task_2",
            )
            self.assertEqual(
                manifest["segments"][2]["task_slots"]["image_task_id"],
                "img_task_3",
            )

    def test_generate_non_dry_run_marks_blocked_when_aliyun_visual_task_poll_times_out(self) -> None:
        with tempfile.TemporaryDirectory(prefix="formal_visual_timeout_") as temp_dir:
            output_dir = pathlib.Path(temp_dir) / "dist"
            local_config_path = pathlib.Path(temp_dir) / "formal_api_demo.local.toml"
            self._write_local_config(
                local_config_path,
                provider_name="aliyun_bailian",
                route_family="aliyun_bailian_cosyvoice",
                api_key="dashscope_test_key",
                model="cosyvoice-v3-flash",
                voice="longxiaochun",
                image_model="wan2.6-image",
                video_model="wan2.6-t2v",
                polling_interval_seconds=0,
                polling_timeout_seconds=0,
            )

            tts_counter = 0

            class _JsonResponse:
                def __init__(self, payload: dict[str, object]) -> None:
                    self._payload = payload

                def __enter__(self):
                    return self

                def __exit__(self, exc_type, exc, tb):
                    return False

                def read(self) -> bytes:
                    return json.dumps(self._payload).encode("utf-8")

            class _BinaryResponse:
                def __enter__(self):
                    return self

                def __exit__(self, exc_type, exc, tb):
                    return False

                @staticmethod
                def read() -> bytes:
                    return b"aliyun-mp3"

            def fake_urlopen(request, timeout=60):
                del timeout
                url = request.full_url
                if url.endswith("/services/audio/tts/SpeechSynthesizer"):
                    nonlocal tts_counter
                    tts_counter += 1
                    return _JsonResponse(
                        {
                            "request_id": f"aliyun_req_{tts_counter}",
                            "output": {
                                "audio": {
                                    "url": f"https://dashscope-result.example.com/audio_{tts_counter}.mp3",
                                },
                            },
                        }
                    )
                if url.startswith("https://dashscope-result.example.com/audio_"):
                    return _BinaryResponse()
                if url.endswith("/services/aigc/image-generation/generation"):
                    return _JsonResponse(
                        {
                            "request_id": "image_req_1",
                            "output": {"task_id": "img_task_timeout", "task_status": "PENDING"},
                        }
                    )
                if url.endswith("/api/v1/tasks/img_task_timeout"):
                    return _JsonResponse(
                        {
                            "request_id": "image_poll_req",
                            "output": {"task_id": "img_task_timeout", "task_status": "RUNNING"},
                        }
                    )
                raise AssertionError(f"unexpected url: {url}")

            with mock.patch("formal_api_demo_core.urllib.request.urlopen", side_effect=fake_urlopen), mock.patch(
                "formal_api_demo_core.concatenate_audio_files",
                side_effect=self._fake_concatenate_audio_files,
            ), mock.patch("time.sleep", return_value=None):
                result = run_generation_pipeline(
                    input_path=FORMAL_CASE_PATH,
                    example_config_path=FORMAL_EXAMPLE_CONFIG_PATH,
                    local_config_path=local_config_path,
                    output_dir=output_dir,
                    dry_run=False,
                )

            manifest = json.loads((output_dir / "manifest.json").read_text(encoding="utf-8"))
            self.assertEqual(result["generation_status"], STATUS_BLOCKED)
            self.assertEqual(result["visual_generation_status"], STATUS_BLOCKED)
            self.assertIn("timeout", result["blocked_reason"])
            self.assertEqual(manifest["current_status"], STATUS_BLOCKED)
            self.assertEqual(
                manifest["generation"]["visual_generation"]["segment_assets"][0]["status"],
                STATUS_BLOCKED,
            )

    def test_generate_non_dry_run_marks_failed_when_aliyun_image_task_missing_result_url(self) -> None:
        with tempfile.TemporaryDirectory(prefix="formal_visual_missing_url_") as temp_dir:
            output_dir = pathlib.Path(temp_dir) / "dist"
            local_config_path = pathlib.Path(temp_dir) / "formal_api_demo.local.toml"
            self._write_local_config(
                local_config_path,
                provider_name="aliyun_bailian",
                route_family="aliyun_bailian_cosyvoice",
                api_key="dashscope_test_key",
                model="cosyvoice-v3-flash",
                voice="longxiaochun",
                image_model="wan2.6-image",
                video_model="wan2.6-t2v",
            )

            tts_counter = 0

            class _JsonResponse:
                def __init__(self, payload: dict[str, object]) -> None:
                    self._payload = payload

                def __enter__(self):
                    return self

                def __exit__(self, exc_type, exc, tb):
                    return False

                def read(self) -> bytes:
                    return json.dumps(self._payload).encode("utf-8")

            class _BinaryResponse:
                def __enter__(self):
                    return self

                def __exit__(self, exc_type, exc, tb):
                    return False

                @staticmethod
                def read() -> bytes:
                    return b"aliyun-mp3"

            def fake_urlopen(request, timeout=60):
                del timeout
                url = request.full_url
                if url.endswith("/services/audio/tts/SpeechSynthesizer"):
                    nonlocal tts_counter
                    tts_counter += 1
                    return _JsonResponse(
                        {
                            "request_id": f"aliyun_req_{tts_counter}",
                            "output": {
                                "audio": {
                                    "url": f"https://dashscope-result.example.com/audio_{tts_counter}.mp3",
                                },
                            },
                        }
                    )
                if url.startswith("https://dashscope-result.example.com/audio_"):
                    return _BinaryResponse()
                if url.endswith("/services/aigc/image-generation/generation"):
                    return _JsonResponse(
                        {
                            "request_id": "image_req_1",
                            "output": {"task_id": "img_task_missing_url", "task_status": "PENDING"},
                        }
                    )
                if url.endswith("/api/v1/tasks/img_task_missing_url"):
                    return _JsonResponse(
                        {
                            "request_id": "image_poll_req",
                            "output": {
                                "task_id": "img_task_missing_url",
                                "task_status": "SUCCEEDED",
                                "finished": True,
                                "choices": [],
                            },
                        }
                    )
                raise AssertionError(f"unexpected url: {url}")

            with mock.patch("formal_api_demo_core.urllib.request.urlopen", side_effect=fake_urlopen), mock.patch(
                "formal_api_demo_core.concatenate_audio_files",
                side_effect=self._fake_concatenate_audio_files,
            ):
                result = run_generation_pipeline(
                    input_path=FORMAL_CASE_PATH,
                    example_config_path=FORMAL_EXAMPLE_CONFIG_PATH,
                    local_config_path=local_config_path,
                    output_dir=output_dir,
                    dry_run=False,
                )

            manifest = json.loads((output_dir / "manifest.json").read_text(encoding="utf-8"))
            self.assertEqual(result["generation_status"], STATUS_FAILED)
            self.assertEqual(result["visual_generation_status"], STATUS_FAILED)
            self.assertEqual(manifest["current_status"], STATUS_FAILED)
            self.assertIn("image_result_url_missing", result["failure_reason"])

    def test_generate_non_dry_run_marks_failed_when_aliyun_video_download_fails(self) -> None:
        with tempfile.TemporaryDirectory(prefix="formal_visual_video_download_fail_") as temp_dir:
            output_dir = pathlib.Path(temp_dir) / "dist"
            local_config_path = pathlib.Path(temp_dir) / "formal_api_demo.local.toml"
            self._write_local_config(
                local_config_path,
                provider_name="aliyun_bailian",
                route_family="aliyun_bailian_cosyvoice",
                api_key="dashscope_test_key",
                model="cosyvoice-v3-flash",
                voice="longxiaochun",
                image_model="wan2.6-image",
                video_model="wan2.6-t2v",
            )

            tts_counter = 0
            image_task_counter = 0

            class _JsonResponse:
                def __init__(self, payload: dict[str, object]) -> None:
                    self._payload = payload

                def __enter__(self):
                    return self

                def __exit__(self, exc_type, exc, tb):
                    return False

                def read(self) -> bytes:
                    return json.dumps(self._payload).encode("utf-8")

            class _BinaryResponse:
                def __enter__(self):
                    return self

                def __exit__(self, exc_type, exc, tb):
                    return False

                def read(self) -> bytes:
                    return b"aliyun-mp3" if self.full_url.endswith(".mp3") else b"fake-image"

            def fake_urlopen(request, timeout=60):
                del timeout
                url = request.full_url
                if url.endswith("/services/audio/tts/SpeechSynthesizer"):
                    nonlocal tts_counter
                    tts_counter += 1
                    return _JsonResponse(
                        {
                            "request_id": f"aliyun_req_{tts_counter}",
                            "output": {
                                "audio": {
                                    "url": f"https://dashscope-result.example.com/audio_{tts_counter}.mp3",
                                },
                            },
                        }
                    )
                if url.startswith("https://dashscope-result.example.com/audio_"):
                    response = _BinaryResponse()
                    response.full_url = url
                    return response
                if url.endswith("/services/aigc/image-generation/generation"):
                    nonlocal image_task_counter
                    image_task_counter += 1
                    return _JsonResponse(
                        {
                            "request_id": f"image_req_{image_task_counter}",
                            "output": {"task_id": f"img_task_{image_task_counter}", "task_status": "PENDING"},
                        }
                    )
                if url.endswith("/services/aigc/video-generation/video-synthesis"):
                    return _JsonResponse(
                        {
                            "request_id": "video_req_1",
                            "output": {"task_id": "vid_task_download_fail", "task_status": "PENDING"},
                        }
                    )
                if url.endswith("/api/v1/tasks/img_task_1") or url.endswith("/api/v1/tasks/img_task_2"):
                    task_id = url.rsplit("/", 1)[-1]
                    return _JsonResponse(
                        {
                            "request_id": f"{task_id}_poll_req",
                            "output": {
                                "task_id": task_id,
                                "task_status": "SUCCEEDED",
                                "finished": True,
                                "choices": [
                                    {
                                        "finish_reason": "stop",
                                        "message": {
                                            "role": "assistant",
                                            "content": [
                                                {
                                                    "type": "image",
                                                    "image": f"https://dashscope-result.example.com/{task_id}.png",
                                                }
                                            ],
                                        },
                                    }
                                ],
                            },
                        }
                    )
                if url.endswith("/api/v1/tasks/vid_task_download_fail"):
                    return _JsonResponse(
                        {
                            "request_id": "vid_task_poll_req",
                            "output": {
                                "task_id": "vid_task_download_fail",
                                "task_status": "SUCCEEDED",
                                "video_url": "https://dashscope-result.example.com/vid_task_download_fail.mp4",
                            },
                        }
                    )
                if url.endswith(".png"):
                    response = _BinaryResponse()
                    response.full_url = url
                    return response
                if url.endswith(".mp4"):
                    raise urllib.error.HTTPError(
                        url,
                        403,
                        "Forbidden",
                        hdrs=None,
                        fp=io.BytesIO(b'{"code":"NoPermission","message":"download denied"}'),
                    )
                raise AssertionError(f"unexpected url: {url}")

            with mock.patch("formal_api_demo_core.urllib.request.urlopen", side_effect=fake_urlopen), mock.patch(
                "formal_api_demo_core.concatenate_audio_files",
                side_effect=self._fake_concatenate_audio_files,
            ):
                result = run_generation_pipeline(
                    input_path=FORMAL_CASE_PATH,
                    example_config_path=FORMAL_EXAMPLE_CONFIG_PATH,
                    local_config_path=local_config_path,
                    output_dir=output_dir,
                    dry_run=False,
                )

            manifest = json.loads((output_dir / "manifest.json").read_text(encoding="utf-8"))
            self.assertEqual(result["generation_status"], STATUS_FAILED)
            self.assertEqual(result["visual_generation_status"], STATUS_FAILED)
            self.assertEqual(manifest["current_status"], STATUS_FAILED)
            self.assertIn("video_download_failed", result["failure_reason"])

    def test_generate_non_dry_run_keeps_liveportrait_branch_honestly_blocked(self) -> None:
        with tempfile.TemporaryDirectory(prefix="formal_liveportrait_blocked_") as temp_dir:
            output_dir = pathlib.Path(temp_dir) / "dist"
            local_config_path = pathlib.Path(temp_dir) / "formal_api_demo.local.toml"
            self._write_local_config(
                local_config_path,
                provider_name="aliyun_bailian",
                route_family="aliyun_bailian_cosyvoice",
                api_key="dashscope_test_key",
                model="cosyvoice-v3-flash",
                voice="longxiaochun",
                image_model="wan2.6-image",
                video_model="wan2.6-t2v",
                portrait_detect_enabled=True,
                portrait_video_generation_enabled=True,
            )

            def fake_probe(*_args, **kwargs):
                output_stem = kwargs.get("output_stem", "voice_probe")
                audio_path = output_dir / "tts" / f"{output_stem}.mp3"
                audio_path.parent.mkdir(parents=True, exist_ok=True)
                audio_path.write_bytes(f"fake-{output_stem}".encode("utf-8"))
                return {
                    "status": STATUS_SUCCESS,
                    "blocked_reason": "",
                    "failure_reason": "",
                    "error_code": "",
                    "error_message": "",
                    "audio_path": str(audio_path),
                    "request_id": f"req_{output_stem}",
                    "model_identifier": "cosyvoice-v3-flash",
                    "probe_text": "测试配音",
                    "voice": "longxiaochun",
                    "used_model_id": "cosyvoice-v3-flash",
                    "request_debug": {
                        "provider": "aliyun_bailian",
                        "api_route_family": "aliyun_bailian_cosyvoice",
                    },
                }

            with mock.patch("formal_api_demo_core.execute_tts_probe", side_effect=fake_probe), mock.patch(
                "formal_api_demo_core.concatenate_audio_files",
                side_effect=self._fake_concatenate_audio_files,
            ):
                result = run_generation_pipeline(
                    input_path=FORMAL_CASE_PATH,
                    example_config_path=FORMAL_EXAMPLE_CONFIG_PATH,
                    local_config_path=local_config_path,
                    output_dir=output_dir,
                    dry_run=False,
                )

            manifest = json.loads((output_dir / "manifest.json").read_text(encoding="utf-8"))
            self.assertEqual(result["generation_status"], STATUS_BLOCKED)
            self.assertIn(
                "portrait_detect_provider_implementation",
                result["current_missing_implementations"],
            )
            self.assertEqual(
                manifest["generation"]["visual_generation"]["portrait_detect"]["status"],
                STATUS_BLOCKED,
            )
            self.assertEqual(
                manifest["generation"]["visual_generation"]["portrait_video_generation"]["status"],
                STATUS_BLOCKED,
            )

    def test_generate_non_dry_run_aliyun_bailian_marks_failed_when_remote_returns_403(self) -> None:
        with tempfile.TemporaryDirectory(prefix="formal_aliyun_failed_") as temp_dir:
            output_dir = pathlib.Path(temp_dir) / "dist"
            local_config_path = pathlib.Path(temp_dir) / "formal_api_demo.local.toml"
            self._write_local_config(
                local_config_path,
                provider_name="aliyun_bailian",
                route_family="aliyun_bailian_cosyvoice",
                api_key="dashscope_test_key",
                model="cosyvoice-v3-flash",
                voice="longxiaochun",
            )

            def fake_urlopen(request, timeout=60):
                del timeout
                raise urllib.error.HTTPError(
                    request.full_url,
                    403,
                    "Forbidden",
                    hdrs=None,
                    fp=io.BytesIO(
                        b'{"code":"InvalidApiKey","message":"test aliyun auth denied"}'
                    ),
                )

            with mock.patch("formal_api_demo_core.urllib.request.urlopen", side_effect=fake_urlopen):
                result = run_generation_pipeline(
                    input_path=FORMAL_CASE_PATH,
                    example_config_path=FORMAL_EXAMPLE_CONFIG_PATH,
                    local_config_path=local_config_path,
                    output_dir=output_dir,
                    dry_run=False,
                )

            manifest = json.loads((output_dir / "manifest.json").read_text(encoding="utf-8"))
            self.assertEqual(result["overall_status"], STATUS_FAILED)
            self.assertEqual(result["generation_status"], STATUS_FAILED)
            self.assertEqual(manifest["current_status"], STATUS_FAILED)
            self.assertEqual(
                result["failure_reason"],
                "aliyun_bailian_tts_request_failed",
            )

    def test_run_aliyun_tts_style_probe_variants_writes_three_named_audio_files(self) -> None:
        with tempfile.TemporaryDirectory(prefix="formal_aliyun_variants_") as temp_dir:
            output_dir = pathlib.Path(temp_dir) / "dist"
            local_config_path = pathlib.Path(temp_dir) / "formal_api_demo.local.toml"
            self._write_local_config(
                local_config_path,
                provider_name="aliyun_bailian",
                route_family="aliyun_bailian_cosyvoice",
                api_key="dashscope_test_key",
                model="cosyvoice-v3-flash",
                voice="longanyang",
            )

            requests: list[dict[str, object]] = []

            class _JsonResponse:
                def __init__(self, payload: dict[str, object]) -> None:
                    self._payload = payload

                def __enter__(self):
                    return self

                def __exit__(self, exc_type, exc, tb):
                    return False

                def read(self) -> bytes:
                    return json.dumps(self._payload).encode("utf-8")

            class _BinaryResponse:
                def __init__(self, content: bytes) -> None:
                    self._content = content

                def __enter__(self):
                    return self

                def __exit__(self, exc_type, exc, tb):
                    return False

                def read(self) -> bytes:
                    return self._content

            def fake_urlopen(request, timeout=60):
                del timeout
                url = request.full_url
                if url.endswith("/services/audio/tts/SpeechSynthesizer"):
                    body = json.loads(request.data.decode("utf-8"))
                    requests.append(body)
                    variant_id = len(requests)
                    return _JsonResponse(
                        {
                            "request_id": f"aliyun_req_{variant_id}",
                            "output": {
                                "finish_reason": "stop",
                                "audio": {
                                    "url": f"https://dashscope-result.example.com/audio_{variant_id}.mp3",
                                },
                            },
                        }
                    )
                if "audio_" in url:
                    variant_id = url.rsplit("_", 1)[-1].split(".", 1)[0]
                    return _BinaryResponse(f"aliyun-mp3-{variant_id}".encode("utf-8"))
                raise AssertionError(f"unexpected url: {url}")

            with mock.patch("formal_api_demo_core.urllib.request.urlopen", side_effect=fake_urlopen):
                result = run_aliyun_tts_style_probe_variants(
                    input_path=FORMAL_CASE_PATH,
                    example_config_path=FORMAL_EXAMPLE_CONFIG_PATH,
                    local_config_path=local_config_path,
                    output_dir=output_dir,
                )

            self.assertEqual(result["overall_status"], STATUS_SUCCESS)
            self.assertTrue(result["style_draft_in_request"])
            self.assertEqual(result["recommended_variant_id"], "A")
            self.assertEqual(len(result["variants"]), 3)
            self.assertEqual([item["variant_id"] for item in result["variants"]], ["A", "B", "C"])
            self.assertEqual(
                [pathlib.Path(item["audio_path"]).name for item in result["variants"]],
                ["voice_probe_A.mp3", "voice_probe_B.mp3", "voice_probe_C.mp3"],
            )
            self.assertTrue(result["variants"][0]["request_debug"]["style_draft_in_request"])
            self.assertEqual(requests[0]["input"]["instruction"], "你说话的情感是neutral。")
            self.assertEqual(requests[1]["input"]["instruction"], "你说话的情感是disgusted。")
            self.assertEqual(requests[2]["input"]["instruction"], "你说话的情感是neutral。")
            self.assertIn("rate", requests[0]["input"])
            self.assertIn("pitch", requests[0]["input"])
            self.assertIn("volume", requests[0]["input"])
            self.assertEqual(
                requests[0]["input"]["text"],
                requests[1]["input"]["text"],
            )

    def test_run_aliyun_tts_style_probe_round2_writes_four_named_audio_files_and_summary(self) -> None:
        with tempfile.TemporaryDirectory(prefix="formal_aliyun_round2_") as temp_dir:
            output_dir = pathlib.Path(temp_dir) / "dist"
            local_config_path = pathlib.Path(temp_dir) / "formal_api_demo.local.toml"
            self._write_local_config(
                local_config_path,
                provider_name="aliyun_bailian",
                route_family="aliyun_bailian_cosyvoice",
                api_key="dashscope_test_key",
                model="cosyvoice-v3-flash",
                voice="longanyang",
            )

            requests: list[dict[str, object]] = []

            class _JsonResponse:
                def __init__(self, payload: dict[str, object]) -> None:
                    self._payload = payload

                def __enter__(self):
                    return self

                def __exit__(self, exc_type, exc, tb):
                    return False

                def read(self) -> bytes:
                    return json.dumps(self._payload).encode("utf-8")

            class _BinaryResponse:
                def __init__(self, content: bytes) -> None:
                    self._content = content

                def __enter__(self):
                    return self

                def __exit__(self, exc_type, exc, tb):
                    return False

                def read(self) -> bytes:
                    return self._content

            def fake_urlopen(request, timeout=60):
                del timeout
                url = request.full_url
                if url.endswith("/services/audio/tts/SpeechSynthesizer"):
                    body = json.loads(request.data.decode("utf-8"))
                    requests.append(body)
                    variant_id = len(requests)
                    return _JsonResponse(
                        {
                            "request_id": f"aliyun_round2_req_{variant_id}",
                            "output": {
                                "finish_reason": "stop",
                                "audio": {
                                    "url": f"https://dashscope-result.example.com/round2_audio_{variant_id}.mp3",
                                },
                            },
                        }
                    )
                if "round2_audio_" in url:
                    variant_id = url.rsplit("_", 1)[-1].split(".", 1)[0]
                    return _BinaryResponse(f"aliyun-round2-mp3-{variant_id}".encode("utf-8"))
                raise AssertionError(f"unexpected url: {url}")

            with mock.patch("formal_api_demo_core.urllib.request.urlopen", side_effect=fake_urlopen):
                result = run_aliyun_tts_style_probe_round2(
                    input_path=FORMAL_CASE_PATH,
                    example_config_path=FORMAL_EXAMPLE_CONFIG_PATH,
                    local_config_path=local_config_path,
                    output_dir=output_dir,
                )

            self.assertEqual(result["overall_status"], STATUS_SUCCESS)
            self.assertTrue(result["style_draft_in_request"])
            self.assertEqual(result["recommended_variant_id"], "A2")
            self.assertIn("旧 A", result["recommendation_reason"])
            self.assertEqual(len(result["variants"]), 4)
            self.assertEqual([item["variant_id"] for item in result["variants"]], ["A1", "A2", "A3", "A4"])
            self.assertEqual(
                [pathlib.Path(item["audio_path"]).name for item in result["variants"]],
                ["voice_probe_A1.mp3", "voice_probe_A2.mp3", "voice_probe_A3.mp3", "voice_probe_A4.mp3"],
            )
            self.assertEqual(
                requests[0]["input"]["instruction"],
                "你说话的角色是军事装备分析员，你说话的情感是neutral。",
            )
            self.assertEqual(
                requests[1]["input"]["instruction"],
                "你说话的角色是军事装备拆解解说员，你说话的情感是neutral。",
            )
            self.assertEqual(
                requests[2]["input"]["instruction"],
                "你说话的角色是军事鉴定解说员，你说话的情感是disgusted。",
            )
            self.assertEqual(
                requests[3]["input"]["instruction"],
                "你说话的场景是内部评估解说，你说话的情感是neutral。",
            )
            self.assertEqual(requests[1]["input"]["rate"], 1.22)
            self.assertEqual(requests[1]["input"]["pitch"], 0.9)
            self.assertEqual(requests[1]["input"]["volume"], 45)
            self.assertEqual(requests[0]["input"]["text"], requests[3]["input"]["text"])

            summary_path = output_dir / "tts_style_probe_round2.json"
            self.assertTrue(summary_path.exists())
            summary = json.loads(summary_path.read_text(encoding="utf-8"))
            self.assertEqual(summary["recommended_variant_id"], "A2")
            self.assertEqual(summary["recommended_variant_label"], "更干、更利落")
            self.assertIn("instruction", summary["variants"][0])
            self.assertIn("speech_rate", summary["variants"][0])
            self.assertIn("pitch_rate", summary["variants"][0])
            self.assertIn("volume", summary["variants"][0])

    def test_generate_non_dry_run_edge_gateway_requires_model_not_endpoint(self) -> None:
        with tempfile.TemporaryDirectory(prefix="formal_edge_missing_model_") as temp_dir:
            output_dir = pathlib.Path(temp_dir) / "dist"
            local_config_path = pathlib.Path(temp_dir) / "formal_api_demo.local.toml"
            self._write_local_config(
                local_config_path,
                route_family="edge_gateway_openai_compatible",
                api_key="gateway_test_key",
                model="",
                endpoint_id="ep_should_be_ignored",
            )

            result = run_generation_pipeline(
                input_path=FORMAL_CASE_PATH,
                example_config_path=FORMAL_EXAMPLE_CONFIG_PATH,
                local_config_path=local_config_path,
                output_dir=output_dir,
                dry_run=False,
            )

            self.assertEqual(result["overall_status"], STATUS_BLOCKED)
            self.assertIn("tts_model", result["current_missing_prerequisites"])
            self.assertNotIn("tts_model_or_endpoint", result["current_missing_prerequisites"])

    def test_generate_non_dry_run_openspeech_missing_app_id_and_resource_id_blocks(self) -> None:
        with tempfile.TemporaryDirectory(prefix="formal_openspeech_missing_") as temp_dir:
            output_dir = pathlib.Path(temp_dir) / "dist"
            local_config_path = pathlib.Path(temp_dir) / "formal_api_demo.local.toml"
            self._write_local_config(
                local_config_path,
                route_family="doubao_openspeech_v3",
                api_key="openspeech_access_key",
                app_id="",
                resource_id="",
            )

            result = run_generation_pipeline(
                input_path=FORMAL_CASE_PATH,
                example_config_path=FORMAL_EXAMPLE_CONFIG_PATH,
                local_config_path=local_config_path,
                output_dir=output_dir,
                dry_run=False,
            )

            self.assertEqual(result["overall_status"], STATUS_BLOCKED)
            self.assertIn("app_id", result["current_missing_prerequisites"])
            self.assertIn("tts_resource_id", result["current_missing_prerequisites"])

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

    def test_generate_non_dry_run_edge_gateway_blocks_when_visual_provider_not_implemented(self) -> None:
        with tempfile.TemporaryDirectory(prefix="formal_edge_success_") as temp_dir:
            output_dir = pathlib.Path(temp_dir) / "dist"
            local_config_path = pathlib.Path(temp_dir) / "formal_api_demo.local.toml"
            self._write_local_config(
                local_config_path,
                route_family="edge_gateway_openai_compatible",
                api_key="gateway_test_key",
                model="gateway_tts_model",
                image_model="wanx2.1-image",
                video_model="wanx2.1-video",
            )

            class _SuccessResponse:
                headers = {"x-request-id": "req_edge_demo"}

                @staticmethod
                def stream_to_file(path: str) -> None:
                    pathlib.Path(path).write_bytes(b"edge-mp3")

            class _SuccessSpeechContext:
                def __enter__(self):
                    return _SuccessResponse()

                def __exit__(self, exc_type, exc, tb):
                    return False

            class _WithStreamingResponse:
                @staticmethod
                def create(**_kwargs):
                    return _SuccessSpeechContext()

            class _SpeechResource:
                with_streaming_response = _WithStreamingResponse()

            class _AudioResource:
                speech = _SpeechResource()

            class _FakeOpenAIClient:
                def __init__(self, **_kwargs):
                    self.audio = _AudioResource()

            with mock.patch("formal_api_demo_core.OpenAI", _FakeOpenAIClient), mock.patch(
                "formal_api_demo_core.concatenate_audio_files",
                side_effect=self._fake_concatenate_audio_files,
            ):
                result = run_generation_pipeline(
                    input_path=FORMAL_CASE_PATH,
                    example_config_path=FORMAL_EXAMPLE_CONFIG_PATH,
                    local_config_path=local_config_path,
                    output_dir=output_dir,
                    dry_run=False,
                )

            manifest = json.loads((output_dir / "manifest.json").read_text(encoding="utf-8"))
            request_debug = manifest["generation"]["tts_probe"]["request_debug"]
            self.assertEqual(result["overall_status"], STATUS_BLOCKED)
            self.assertEqual(result["generation_status"], STATUS_BLOCKED)
            self.assertEqual(result["tts_probe_status"], STATUS_SUCCESS)
            self.assertEqual(result["voiceover_status"], STATUS_SUCCESS)
            self.assertEqual(result["visual_generation_status"], STATUS_BLOCKED)
            self.assertEqual(result["cloud_visual_generation_status"], STATUS_BLOCKED)
            self.assertEqual(request_debug["api_route_family"], "edge_gateway_openai_compatible")
            self.assertEqual(request_debug["base_url"], "https://ai-gateway.vei.volces.com/v1")
            self.assertEqual(request_debug["model_identifier_source"], "model")
            self.assertTrue((output_dir / "tts" / "voice_probe.mp3").exists())
            self.assertTrue((output_dir / "tts" / "formal_voiceover.mp3").exists())

    def test_generate_non_dry_run_marks_failed_when_remote_returns_404(self) -> None:
        with tempfile.TemporaryDirectory(prefix="formal_tts_404_") as temp_dir:
            output_dir = pathlib.Path(temp_dir) / "dist"
            local_config_path = pathlib.Path(temp_dir) / "formal_api_demo.local.toml"
            self._write_local_config(
                local_config_path,
                api_key="ark_test_key",
                endpoint_id="ep_tts_demo",
            )

            class _FailingSpeechContext:
                def __enter__(self):
                    request = httpx.Request(
                        "POST",
                        "https://ark.cn-beijing.volces.com/api/v3/audio/speech",
                    )
                    response = httpx.Response(404, request=request, text="")
                    raise openai.NotFoundError(
                        "Error code: 404",
                        response=response,
                        body=None,
                    )

                def __exit__(self, exc_type, exc, tb):
                    return False

            class _WithStreamingResponse:
                @staticmethod
                def create(**_kwargs):
                    return _FailingSpeechContext()

            class _SpeechResource:
                with_streaming_response = _WithStreamingResponse()

            class _AudioResource:
                speech = _SpeechResource()

            class _FakeOpenAIClient:
                def __init__(self, **_kwargs):
                    self.audio = _AudioResource()

            with mock.patch("formal_api_demo_core.OpenAI", _FakeOpenAIClient):
                result = run_generation_pipeline(
                    input_path=FORMAL_CASE_PATH,
                    example_config_path=FORMAL_EXAMPLE_CONFIG_PATH,
                    local_config_path=local_config_path,
                    output_dir=output_dir,
                    dry_run=False,
                )

            self.assertEqual(result["overall_status"], STATUS_FAILED)
            self.assertEqual(result["generation_status"], STATUS_FAILED)
            self.assertEqual(result["failure_reason"], "ark_tts_route_or_identifier_not_found")

    def test_generate_non_dry_run_blocks_when_visual_generation_models_missing(self) -> None:
        with tempfile.TemporaryDirectory(prefix="formal_tts_visual_blocked_") as temp_dir:
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

            with mock.patch("formal_api_demo_core.execute_tts_probe", side_effect=fake_probe), mock.patch(
                "formal_api_demo_core.concatenate_audio_files",
                side_effect=self._fake_concatenate_audio_files,
            ):
                result = run_generation_pipeline(
                    input_path=FORMAL_CASE_PATH,
                    example_config_path=FORMAL_EXAMPLE_CONFIG_PATH,
                    local_config_path=local_config_path,
                    output_dir=output_dir,
                    dry_run=False,
                )

            self.assertEqual(result["overall_status"], STATUS_BLOCKED)
            self.assertEqual(result["generation_status"], STATUS_BLOCKED)
            self.assertEqual(result["tts_probe_status"], STATUS_SUCCESS)
            self.assertEqual(result["voiceover_status"], STATUS_SUCCESS)
            self.assertEqual(result["visual_generation_status"], STATUS_BLOCKED)
            self.assertEqual(result["cloud_visual_generation_status"], STATUS_BLOCKED)
            self.assertIn("image_generation_model", result["current_missing_prerequisites"])
            self.assertIn("video_generation_model", result["current_missing_prerequisites"])
            self.assertTrue((output_dir / "tts" / "voice_probe.mp3").exists())
            self.assertTrue((output_dir / "tts" / "formal_voiceover.mp3").exists())


if __name__ == "__main__":
    unittest.main()
