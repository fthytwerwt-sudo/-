from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "正片候选TTS路线_publish_candidate_tts_route.py"
SPEC = importlib.util.spec_from_file_location("publish_candidate_tts_route", MODULE_PATH)
assert SPEC and SPEC.loader
route_module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(route_module)


def _summary(status: str = "publish_candidate_ready_for_human_review") -> dict:
    return {
        "status": status,
        "publish_candidate_ready_for_human_review": status == "publish_candidate_ready_for_human_review",
    }


class PublishCandidateVoiceGateTests(unittest.TestCase):
    def test_publish_candidate_with_minimax_speech_2_8_hd_passes(self) -> None:
        result = route_module.validate_publish_candidate_tts_route(
            {
                "tts_route_report": {
                    "actual_tts_provider": "minimax",
                    "actual_tts_model": "speech-2.8-hd",
                    "selected_route": "minimax_official_api",
                    "is_minimax_speech_2_8_hd": True,
                    "audio_present": True,
                    "non_silent": True,
                    "fallback_tts_used": False,
                }
            },
            _summary(),
        )
        self.assertEqual(result["voice_route_validation"], "passed_minimax")
        self.assertEqual(result["blocked_reasons"], [])

    def test_publish_candidate_with_aliyun_qwen_tts_fails(self) -> None:
        result = route_module.validate_publish_candidate_tts_route(
            {
                "tts_route_report": {
                    "actual_tts_provider": "aliyun_bailian",
                    "actual_tts_model": "qwen3-tts-vc-realtime-2026-01-15",
                    "selected_route": "aliyun_qwen_realtime_websocket_voice_clone",
                    "audio_present": True,
                    "non_silent": True,
                }
            },
            _summary(),
        )
        self.assertEqual(result["voice_route_validation"], "failed_non_minimax_voice")
        self.assertIn("failed_non_minimax_voice", result["blocked_reasons"])

    def test_publish_candidate_with_macos_say_fails(self) -> None:
        result = route_module.validate_publish_candidate_tts_route(
            {
                "tts_route_report": {
                    "actual_tts_provider": "macos_say",
                    "actual_tts_model": "say",
                    "selected_route": "local",
                    "audio_present": True,
                    "non_silent": True,
                    "macos_say_used": True,
                }
            },
            _summary(),
        )
        self.assertEqual(result["voice_route_validation"], "failed_non_minimax_voice")
        self.assertIn("macos_say_used_for_publish_candidate", result["blocked_reasons"])

    def test_minimax_route_unavailable_blocks_publish_candidate(self) -> None:
        result = route_module.validate_publish_candidate_tts_route(
            {
                "tts_route_report": {
                    "actual_tts_provider": "minimax",
                    "actual_tts_model": "speech-2.8-hd",
                    "selected_route": "minimax_official_api",
                    "is_minimax_speech_2_8_hd": True,
                    "audio_present": False,
                    "non_silent": False,
                }
            },
            _summary(),
        )
        self.assertEqual(result["voice_route_validation"], "blocked_minimax_unavailable")
        self.assertIn("audio_not_generated_or_missing", result["blocked_reasons"])

    def test_internal_diagnostic_can_use_non_minimax_only_if_not_publish_candidate(self) -> None:
        result = route_module.validate_publish_candidate_tts_route(
            {
                "tts_route_report": {
                    "actual_tts_provider": "aliyun_bailian",
                    "actual_tts_model": "qwen3-tts-vc-realtime-2026-01-15",
                    "audio_present": True,
                    "non_silent": True,
                }
            },
            {
                "status": "internal_diagnostic_only",
                "publish_candidate_ready_for_human_review": False,
            },
        )
        self.assertEqual(result["voice_route_validation"], "internal_diagnostic_only")
        self.assertIs(result["full_video_can_only_be_internal_diagnostic"], True)
        self.assertEqual(result["blocked_reasons"], [])


if __name__ == "__main__":
    unittest.main()
