import pathlib
import tempfile
import unittest
from unittest import mock


from formal_hybrid_master import (
    build_hybrid_routing_plan,
    build_slide_specs,
    generate_visual_assets,
    load_or_generate_voiceover,
    normalize_generation_models,
)


class FormalHybridMasterTests(unittest.TestCase):
    def test_normalize_generation_models_fills_blank_defaults(self) -> None:
        config = {
            "image_generation": {"model": ""},
            "video_generation": {"model": ""},
        }

        normalized = normalize_generation_models(config)

        self.assertEqual(normalized["image_generation"]["model"], "wan2.6-image")
        self.assertEqual(normalized["video_generation"]["model"], "wan2.6-t2v")

    def test_build_hybrid_routing_plan_matches_formal_master_goal(self) -> None:
        plan = build_hybrid_routing_plan()

        self.assertEqual(plan["video_scene"], "AI 项目讲解")
        self.assertEqual(plan["video_route_strategy"], "hybrid")
        self.assertEqual(len(plan["blocks"]), 3)
        self.assertEqual(plan["blocks"][0]["block_carrier"], "human")
        self.assertEqual(plan["blocks"][1]["block_carrier"], "mixed")
        self.assertEqual(plan["blocks"][2]["block_carrier"], "human_with_overlay")

    def test_build_slide_specs_uses_video_background_for_human_blocks(self) -> None:
        video_spec = {
            "segments": [
                {
                    "segment_id": "seg01",
                    "caption_text": "开头判断",
                    "visual_intent": "真人开场",
                    "timeline": {"planned_duration_seconds": 9.0},
                },
                {
                    "segment_id": "seg02",
                    "caption_text": "结构证据",
                    "visual_intent": "结构变化",
                    "timeline": {"planned_duration_seconds": 12.0},
                },
                {
                    "segment_id": "seg03",
                    "caption_text": "结尾收束",
                    "visual_intent": "真人收束",
                    "timeline": {"planned_duration_seconds": 9.0},
                },
            ]
        }
        asset_map = {
            "seg01": {"video": "/tmp/seg01.mp4", "image": None},
            "seg02": {"video": "/tmp/seg02.mp4", "image": None},
            "seg03": {"video": "/tmp/seg03.mp4", "image": None},
        }

        slides = build_slide_specs(video_spec=video_spec, asset_map=asset_map)

        self.assertEqual([slide["role"] for slide in slides], ["hook", "process", "outcome"])
        self.assertEqual(slides[0]["background_video_path"], "/tmp/seg01.mp4")
        self.assertIsNone(slides[0]["background_image_path"])
        self.assertEqual(slides[1]["background_video_path"], "/tmp/seg02.mp4")
        self.assertEqual(slides[2]["background_video_path"], "/tmp/seg03.mp4")

    def test_generate_visual_assets_reuses_existing_segment_video(self) -> None:
        video_spec = {
            "segments": [
                {
                    "segment_id": "seg01",
                    "timeline": {"planned_duration_seconds": 9.0},
                }
            ]
        }

        with tempfile.TemporaryDirectory(prefix="hybrid_visual_reuse_") as temp_dir:
            output_dir = pathlib.Path(temp_dir)
            existing_video = output_dir / "visual" / "seg01_video.mp4"
            existing_video.parent.mkdir(parents=True, exist_ok=True)
            existing_video.write_bytes(b"existing-video")

            with mock.patch("formal_hybrid_master._execute_aliyun_wan_video_generation") as mocked:
                asset_map = generate_visual_assets(
                    video_spec=video_spec,
                    config={"video_generation": {"model": "wan2.6-t2v"}},
                    output_dir=output_dir,
                )

            mocked.assert_not_called()
            self.assertEqual(asset_map["seg01"]["video"], str(existing_video))

    def test_load_or_generate_voiceover_reuses_existing_audio_bundle(self) -> None:
        video_spec = {
            "segments": [
                {"segment_id": "seg01"},
                {"segment_id": "seg02"},
            ]
        }

        with tempfile.TemporaryDirectory(prefix="hybrid_voice_reuse_") as temp_dir:
            output_dir = pathlib.Path(temp_dir)
            tts_dir = output_dir / "tts"
            tts_dir.mkdir(parents=True, exist_ok=True)
            existing_bundle = tts_dir / "formal_voiceover.mp3"
            existing_bundle.write_bytes(b"bundle")
            (tts_dir / "segment_seg01.mp3").write_bytes(b"seg01")
            (tts_dir / "segment_seg02.mp3").write_bytes(b"seg02")

            with mock.patch("formal_hybrid_master.execute_formal_voiceover_generation") as mocked:
                voiceover = load_or_generate_voiceover(
                    video_spec=video_spec,
                    config={},
                    output_dir=output_dir,
                )

            mocked.assert_not_called()
            self.assertEqual(voiceover["status"], "success")
            self.assertEqual(voiceover["audio_path"], str(existing_bundle))


if __name__ == "__main__":
    unittest.main()
