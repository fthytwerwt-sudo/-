import pathlib
import tempfile
import unittest
from unittest import mock

from formal_api_demo_core import (
    FORMAL_EXAMPLE_CONFIG_PATH,
    FORMAL_MAINLINE_CASE_PATH,
    STATUS_BLOCKED,
    STATUS_SUCCESS,
    build_visual_generation_plan,
    evaluate_generation_gate,
    load_formal_config,
    parse_formal_case_markdown,
)


class FormalMainlineRouteTests(unittest.TestCase):
    def test_parse_formal_case_reads_optional_style_prompt(self) -> None:
        case_text = """# 主题
测试卡通人物段

## 基础参数
- 总时长：12秒
- 视频比例：9:16

## 目标场景
测试

## 目标用户
测试用户

## 全局质量要求
- 测试要求

## Hook
测试 hook

## 结尾落点
测试结尾

## 分段结构
### 第1段
- 段落ID：seg01
- 计划时长：12秒
- 段目标：测试
- 配音文案：测试文案
- 字幕文案：测试文案
- 画面意图：测试画面
- 需要图片：是
- 需要视频：是
- 允许真实桌面素材：否
- 段载体：human
- 素材来源：api_generated
- 风格提示：Q版 / 3D 盲盒手办感 / 浅绿色帽子
"""
        with tempfile.TemporaryDirectory(prefix="formal_case_style_") as temp_dir:
            case_path = pathlib.Path(temp_dir) / "测试_case.md"
            case_path.write_text(case_text, encoding="utf-8")

            spec = parse_formal_case_markdown(case_path)

        self.assertEqual(spec["segments"][0]["style_prompt"], "Q版 / 3D 盲盒手办感 / 浅绿色帽子")

    def test_parse_formal_mainline_case_reads_api_human_local_footage_route(self) -> None:
        spec = parse_formal_case_markdown(FORMAL_MAINLINE_CASE_PATH)

        self.assertEqual(spec["route_profile"], "api_human_local_footage_light_ppt_cloud_editing")
        self.assertEqual(spec["video_route_strategy"], "hybrid")
        self.assertEqual([segment["carrier"] for segment in spec["segments"]], [
            "human",
            "self_footage",
            "light_ppt",
            "human",
        ])
        self.assertEqual(
            [segment["asset_source"] for segment in spec["segments"]],
            ["api_generated", "user_media", "api_generated", "api_generated"],
        )
        self.assertEqual(
            [segment["asset_key"] for segment in spec["segments"]],
            ["hook_human", "process_self_footage", "result_card", "close_human"],
        )

    def test_generation_gate_blocks_when_required_process_footage_is_missing(self) -> None:
        spec = parse_formal_case_markdown(FORMAL_MAINLINE_CASE_PATH)
        config_bundle = load_formal_config(
            example_config_path=FORMAL_EXAMPLE_CONFIG_PATH,
            local_config_path=None,
        )

        gate = evaluate_generation_gate(
            video_spec=spec,
            config=config_bundle["config"],
            has_local_config=config_bundle["has_local_config"],
            dry_run=False,
        )

        self.assertEqual(gate["status"], STATUS_BLOCKED)
        self.assertIn(
            "footage_input_process_self_footage_local_path",
            gate["missing_prerequisites"],
        )
        self.assertNotIn("footage_input_hook_human_local_path", gate["missing_prerequisites"])
        self.assertNotIn("footage_input_close_human_local_path", gate["missing_prerequisites"])

    def test_visual_plan_routes_api_human_and_local_process_footage_correctly(self) -> None:
        spec = parse_formal_case_markdown(FORMAL_MAINLINE_CASE_PATH)

        with tempfile.TemporaryDirectory(prefix="formal_mainline_assets_") as temp_dir:
            output_dir = pathlib.Path(temp_dir)
            process_video = output_dir / "inputs" / "process_self_footage.mp4"
            process_video.parent.mkdir(parents=True, exist_ok=True)
            process_video.write_bytes(b"video")

            local_config_path = output_dir / "formal_api_demo.local.toml"
            local_config_path.write_text(
                "\n".join(
                    [
                        "[provider]",
                        'name = "aliyun_bailian"',
                        'region = "cn-beijing"',
                        "",
                        "[auth]",
                        'api_key = "test_api_key"',
                        "",
                        "[tts]",
                        'api_route_family = "aliyun_bailian_cosyvoice"',
                        'model = "cosyvoice-v3-flash"',
                        'voice = "test_voice"',
                        "",
                        "[image_generation]",
                        'model = "wan2.6-image"',
                        "",
                        "[video_generation]",
                        'model = "wan2.7-i2v"',
                        "",
                        "[portrait_detect]",
                        "enabled = true",
                        'model = "liveportrait-detect"',
                        "",
                        "[portrait_video_generation]",
                        "enabled = true",
                        'model = "liveportrait"',
                        "",
                        "[assembly]",
                        'mode = "cloud_only"',
                        'subtitle_mode = "burn_in"',
                        'resolution = "1080x1920"',
                        "fps = 25",
                        "",
                        "[footage_inputs.process_self_footage]",
                        'local_path = "' + str(process_video) + '"',
                        'source_type = "user_screen_recording"',
                    ]
                )
                + "\n",
                encoding="utf-8",
            )
            config = load_formal_config(
                example_config_path=FORMAL_EXAMPLE_CONFIG_PATH,
                local_config_path=local_config_path,
            )["config"]

            def fake_image_generation(*, output_dir, segment_id, **_kwargs):
                asset_path = output_dir / "visual" / f"{segment_id}_image.png"
                asset_path.parent.mkdir(parents=True, exist_ok=True)
                asset_path.write_bytes(b"image")
                return {
                    "status": STATUS_SUCCESS,
                    "task_id": f"img_task_{segment_id}",
                    "asset_path": str(asset_path),
                    "source_url": f"https://dashscope-result.example.com/{segment_id}_image.png",
                    "blocked_reason": "",
                    "failure_reason": "",
                    "error_message": "",
                }

            def fake_liveportrait(*, output_dir, segment_id, **_kwargs):
                asset_path = output_dir / "visual" / f"{segment_id}_portrait.mp4"
                asset_path.parent.mkdir(parents=True, exist_ok=True)
                asset_path.write_bytes(b"portrait-video")
                return {
                    "status": STATUS_SUCCESS,
                    "blocked_reason": "",
                    "failure_reason": "",
                    "error_message": "",
                    "detect": {
                        "status": STATUS_SUCCESS,
                        "blocked_reason": "",
                        "failure_reason": "",
                        "error_message": "",
                        "request_id": f"detect_{segment_id}",
                        "source_image_url": f"https://dashscope-result.example.com/{segment_id}_detect.png",
                    },
                    "generation": {
                        "status": STATUS_SUCCESS,
                        "blocked_reason": "",
                        "failure_reason": "",
                        "error_message": "",
                        "task_id": f"portrait_task_{segment_id}",
                        "request_id": f"portrait_req_{segment_id}",
                        "asset_path": str(asset_path),
                        "source_image_url": f"https://dashscope-result.example.com/{segment_id}_image.png",
                        "source_audio_url": f"https://dashscope-result.example.com/{segment_id}.mp3",
                    },
                }

            with mock.patch(
                "formal_api_demo_core._execute_aliyun_wan_image_generation",
                side_effect=fake_image_generation,
            ) as mocked_image, mock.patch(
                "formal_api_demo_core._execute_aliyun_liveportrait_video_generation",
                side_effect=fake_liveportrait,
            ) as mocked_portrait, mock.patch(
                "formal_api_demo_core._execute_aliyun_wan_video_generation"
            ) as mocked_video, mock.patch("formal_api_demo_core.write_json"):
                visual_generation = build_visual_generation_plan(
                    video_spec=spec,
                    config=config,
                    output_dir=output_dir,
                    visual_gate={"status": STATUS_SUCCESS, "candidate_pool": {}},
                )

            self.assertEqual(visual_generation["status"], STATUS_SUCCESS)
            asset_map = {
                asset["segment_id"]: asset
                for asset in visual_generation["segment_assets"]
            }
            self.assertEqual(
                pathlib.Path(asset_map["seg01"]["video_asset_path"]).name,
                "seg01_portrait.mp4",
            )
            self.assertEqual(asset_map["seg02"]["video_asset_path"], str(process_video))
            self.assertEqual(
                pathlib.Path(asset_map["seg03"]["image_asset_path"]).name,
                "seg03_image.png",
            )
            self.assertEqual(
                pathlib.Path(asset_map["seg04"]["video_asset_path"]).name,
                "seg04_portrait.mp4",
            )
            self.assertEqual(mocked_image.call_count, 3)
            self.assertEqual(mocked_portrait.call_count, 2)
            mocked_video.assert_not_called()

    def test_visual_plan_builds_general_video_prompt_for_styled_human_segments_without_liveportrait(self) -> None:
        spec = parse_formal_case_markdown(FORMAL_MAINLINE_CASE_PATH)
        spec["segments"][0]["style_prompt"] = "Q版 / chibi / 3D 盲盒手办感 / 浅绿色帽子 / 哑光树脂质感"
        spec["segments"][-1]["style_prompt"] = "Q版 / chibi / 3D 盲盒手办感 / 浅绿色帽子 / 哑光树脂质感"

        with tempfile.TemporaryDirectory(prefix="formal_mainline_general_human_") as temp_dir:
            output_dir = pathlib.Path(temp_dir)
            process_video = output_dir / "inputs" / "process_self_footage.mp4"
            process_video.parent.mkdir(parents=True, exist_ok=True)
            process_video.write_bytes(b"video")

            local_config_path = output_dir / "formal_api_demo.local.toml"
            local_config_path.write_text(
                "\n".join(
                    [
                        "[provider]",
                        'name = "aliyun_bailian"',
                        'region = "cn-beijing"',
                        "",
                        "[auth]",
                        'api_key = "test_api_key"',
                        "",
                        "[tts]",
                        'api_route_family = "aliyun_bailian_cosyvoice"',
                        'model = "cosyvoice-v3-flash"',
                        'voice = "test_voice"',
                        "",
                        "[image_generation]",
                        'model = "wan2.6-image"',
                        "",
                        "[video_generation]",
                        'model = "wan2.7-i2v"',
                        "",
                        "[portrait_detect]",
                        "enabled = false",
                        'model = "liveportrait-detect"',
                        "",
                        "[portrait_video_generation]",
                        "enabled = false",
                        'model = "liveportrait"',
                        "",
                        "[assembly]",
                        'mode = "cloud_only"',
                        'subtitle_mode = "burn_in"',
                        'resolution = "1080x1920"',
                        "fps = 25",
                        "",
                        "[footage_inputs.process_self_footage]",
                        'local_path = "' + str(process_video) + '"',
                        'source_type = "user_screen_recording"',
                    ]
                )
                + "\n",
                encoding="utf-8",
            )
            config = load_formal_config(
                example_config_path=FORMAL_EXAMPLE_CONFIG_PATH,
                local_config_path=local_config_path,
            )["config"]

            def fake_image_generation(*, output_dir, segment_id, **_kwargs):
                asset_path = output_dir / "visual" / f"{segment_id}_image.png"
                asset_path.parent.mkdir(parents=True, exist_ok=True)
                asset_path.write_bytes(b"image")
                return {
                    "status": STATUS_SUCCESS,
                    "task_id": f"img_task_{segment_id}",
                    "asset_path": str(asset_path),
                    "source_url": f"https://dashscope-result.example.com/{segment_id}_image.png",
                    "blocked_reason": "",
                    "failure_reason": "",
                    "error_message": "",
                    "selected_candidate_id": "primary",
                    "fallback_events": [],
                }

            def fake_video_generation(*, output_dir, segment_id, prompt, **_kwargs):
                asset_path = output_dir / "visual" / f"{segment_id}_video.mp4"
                asset_path.parent.mkdir(parents=True, exist_ok=True)
                asset_path.write_bytes(b"video")
                return {
                    "status": STATUS_SUCCESS,
                    "task_id": f"video_task_{segment_id}",
                    "asset_path": str(asset_path),
                    "source_url": f"https://dashscope-result.example.com/{segment_id}_video.mp4",
                    "blocked_reason": "",
                    "failure_reason": "",
                    "error_message": "",
                    "selected_candidate_id": "primary",
                    "fallback_events": [],
                    "captured_prompt": prompt,
                }

            with mock.patch(
                "formal_api_demo_core._execute_aliyun_wan_image_generation",
                side_effect=fake_image_generation,
            ), mock.patch(
                "formal_api_demo_core._execute_aliyun_wan_video_generation",
                side_effect=fake_video_generation,
            ) as mocked_video, mock.patch("formal_api_demo_core.write_json"):
                visual_generation = build_visual_generation_plan(
                    video_spec=spec,
                    config=config,
                    output_dir=output_dir,
                    visual_gate={"status": STATUS_SUCCESS, "candidate_pool": {}},
                )

        self.assertEqual(visual_generation["status"], STATUS_SUCCESS)
        human_assets = {
            asset["segment_id"]: asset
            for asset in visual_generation["segment_assets"]
            if asset["carrier"] == "human"
        }
        self.assertIn("Q版", human_assets["seg01"]["image_prompt"])
        self.assertIn("Q版", human_assets["seg01"]["video_prompt"])
        self.assertIn("Q版", human_assets["seg04"]["video_prompt"])
        self.assertEqual(mocked_video.call_count, 2)


if __name__ == "__main__":
    unittest.main()
