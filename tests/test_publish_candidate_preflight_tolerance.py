from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
MODULE_PATH = SCRIPTS / "发片候选预检套件_publish_candidate_preflight_suite.py"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))
SPEC = importlib.util.spec_from_file_location("publish_candidate_preflight_suite", MODULE_PATH)
assert SPEC and SPEC.loader
preflight_module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(preflight_module)


def _line_group(index: int, **overrides: object) -> dict:
    group = {
        "line_group_id": f"LG{index:02d}",
        "line_ids": [index],
        "narration_text": f"测试句组 {index}",
        "required_material": "source_screen_recording",
        "source_timecode": f"00:{index:02d}-00:{index + 1:02d}",
        "expected_visual": "exact source screen",
        "actual_visual_observed": "exact source screen",
        "allowed_visuals": ["exact source screen"],
        "forbidden_visuals": ["theme-only image"],
        "evidence_strength": "direct",
        "alignment_status": "exact_match",
        "mismatch_reason": "none",
        "repair_action": "none",
        "line_group_type": "process_sentence",
        "is_core_evidence": False,
        "visual_match_type": "exact_match",
    }
    group.update(overrides)
    return group


def _six_line_locked_copy() -> dict:
    return {
        "locked_title": "Codex 到底能不能帮普通人赚钱？",
        "locked_opening_line": "有人选品。",
        "locked_final_script": "\n".join(
            [
                "有人选品。",
                "有人剪视频。",
                "有人看数据。",
                "有人复盘。",
                "有人整理素材。",
                "有人做下一版测试。",
            ]
        ),
        "allowed_copy_changes": ["标点", "换行", "字幕分句", "TTS 停顿"],
        "forbidden_copy_changes": ["删除句子", "改核心判断", "改标题"],
        "copy_change_request_required_if_needed": True,
    }


def _locked_copy_full_payload() -> dict:
    locked = _six_line_locked_copy()
    script = locked["locked_final_script"]
    return {
        "timeline": {"line_groups": [{"line_group_id": "L25", "narration_text": script}]},
        "tts_route_report": {"segment_reports": [{"line_group_id": "L25", "tts_text": script}]},
        "card_placement": {
            "card_groups": [
                {
                    "line_group_id": "L01",
                    "card_role": "title_card",
                    "card_text": {"title": locked["locked_title"], "subtitle": "真实测试"},
                },
                {
                    "line_group_id": "L25",
                    "card_role": "judgment_card",
                    "card_text": {"title": "有人复盘", "subtitle": "有人整理素材"},
                },
            ]
        },
    }


class PublishCandidateToleranceTests(unittest.TestCase):
    def test_near_equivalent_one_non_core_line_allowed(self) -> None:
        groups = [_line_group(index) for index in range(1, 21)]
        groups[3].update(
            {
                "visual_match_type": "near_equivalent",
                "alignment_status": "near_equivalent",
                "substitute_visual_used": "same-screen later scroll state",
                "substitute_material_id": "V003",
                "substitute_timecode": "00:04-00:05",
                "why_extremely_close": "same product table and same claim, later scroll state",
                "claim_preserved": True,
                "viewer_inference_preserved": True,
                "replacement_material_extremely_close": True,
            }
        )
        result = preflight_module.line_visual_tolerance_preflight({"line_groups": groups}, None)
        self.assertEqual(result["status"], "passed")
        self.assertEqual(result["near_equivalent_material_substitution_report"]["near_equivalent_count"], 1)
        self.assertEqual(result["near_equivalent_material_substitution_report"]["near_equivalent_ratio"], 0.05)

    def test_core_evidence_substitution_blocked(self) -> None:
        groups = [
            _line_group(
                1,
                line_group_type="candidate_table",
                is_core_evidence=True,
                visual_match_type="near_equivalent",
                alignment_status="near_equivalent",
                substitute_visual_used="similar table from another candidate",
                replacement_material_extremely_close=True,
                claim_preserved=True,
                viewer_inference_preserved=True,
            )
        ]
        result = preflight_module.line_visual_tolerance_preflight({"line_groups": groups}, None)
        self.assertEqual(result["status"], "blocked")
        self.assertIn("core_evidence_mismatch_count_gt_0", result["blocked_reasons"])

    def test_whole_video_drift_blocked(self) -> None:
        groups = [
            _line_group(1, visual_match_type="near_equivalent", alignment_status="near_equivalent", replacement_material_extremely_close=True),
            _line_group(2, visual_match_type="near_equivalent", alignment_status="near_equivalent", replacement_material_extremely_close=True),
            _line_group(3, whole_video_drift_detected=True),
        ]
        result = preflight_module.line_visual_tolerance_preflight({"line_groups": groups}, None)
        self.assertEqual(result["status"], "blocked")
        self.assertIn("whole_video_drift_detected", result["blocked_reasons"])
        self.assertIn("consecutive_near_equivalent_groups_gt_1", result["blocked_reasons"])

    def test_minor_flaw_allowed_but_candidate_still_review_required(self) -> None:
        summary = {
            "locked_copy_preserved": True,
            "minimax_voice_gate_passed": True,
            "line_visual_tolerance_passed": True,
            "core_evidence_mismatch_count": 0,
            "subtitle_card_overlap_check_passed": True,
            "visual_evidence_readability_passed": True,
            "completion_truth_preflight_passed": True,
            "review_pack_complete": True,
            "minor_flaws": ["tiny_timing_imperfection"],
            "send_ready": False,
        }
        result = preflight_module.publish_candidate_user_standard_preflight(summary)
        self.assertEqual(result["status"], "passed")
        self.assertTrue(result["publish_candidate_ready_for_human_review"])
        self.assertFalse(result["send_ready_allowed"])

    def test_locked_copy_subtitle_truncation_blocks(self) -> None:
        locked = _six_line_locked_copy()
        payload = _locked_copy_full_payload()
        truncated_subtitle = "\n".join(
            [
                "有人选品。",
                "有人剪视频。",
                "有人看数据。",
                "有人复盘。",
            ]
        )

        result = preflight_module.locked_copy_diff_preflight(
            locked,
            {},
            {},
            {},
            None,
            timeline=payload["timeline"],
            tts_route_report=payload["tts_route_report"],
            final_srt_text=truncated_subtitle,
            final_ass_text=f"Dialogue: 0,0:00:00.00,0:00:04.00,Default,,0,0,0,,{truncated_subtitle}",
            burned_subtitle_text=truncated_subtitle,
            card_placement=payload["card_placement"],
        )

        self.assertEqual(result["status"], "blocked")
        self.assertIn("subtitle_copy_match", result["failed_subchecks"])
        subtitle_result = result["subchecks"]["subtitle_copy_match"]
        self.assertEqual(subtitle_result["failure_type"], "subtitle_truncates_locked_copy")
        self.assertEqual(subtitle_result["missing_text"], "有人整理素材。有人做下一版测试。")

    def test_locked_copy_split_subtitle_full_text_passes(self) -> None:
        locked = _six_line_locked_copy()
        payload = _locked_copy_full_payload()
        split_srt = """1
00:00:00,000 --> 00:00:02,000
有人选品。
有人剪视频。

2
00:00:02,000 --> 00:00:04,000
有人看数据。
有人复盘。

3
00:00:04,000 --> 00:00:06,000
有人整理素材。
有人做下一版测试。
"""
        split_ass = (
            "Dialogue: 0,0:00:00.00,0:00:06.00,Default,,0,0,0,,"
            "有人选品。\\N有人剪视频。\\N有人看数据。\\N有人复盘。\\N有人整理素材。\\N有人做下一版测试。"
        )

        result = preflight_module.locked_copy_diff_preflight(
            locked,
            {},
            {},
            {},
            None,
            timeline=payload["timeline"],
            tts_route_report=payload["tts_route_report"],
            final_srt_text=split_srt,
            final_ass_text=split_ass,
            burned_subtitle_text=locked["locked_final_script"],
            card_placement=payload["card_placement"],
        )

        self.assertEqual(result["status"], "passed")
        self.assertEqual(result["subchecks"]["subtitle_copy_match"]["status"], "passed")
        self.assertEqual(result["subchecks"]["ass_copy_match"]["status"], "passed")
        self.assertEqual(result["subchecks"]["burned_subtitle_copy_match"]["status"], "passed")


if __name__ == "__main__":
    unittest.main()
