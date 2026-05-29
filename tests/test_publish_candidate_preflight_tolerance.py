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


class PublishCandidateToleranceTests(unittest.TestCase):
    def test_editing_profile_id_missing_blocks(self) -> None:
        result = preflight_module.editing_profile_preflight({"line_groups": []}, None)
        self.assertEqual(result["status"], "blocked")
        self.assertIn("profile_id_missing_in_script_to_shot_execution_map", result["blocked_reasons"])

    def test_placeholder_profile_without_inheritance_blocks(self) -> None:
        execution_map = {
            "profile_id": "ecommerce_profile_v1",
            "profile_registry": {
                "ecommerce_profile_v1": {
                    "video_type": "ecommerce",
                    "status": "placeholder_pending_detail",
                    "parent_profile": "none",
                    "fill_later": True,
                }
            },
        }
        result = preflight_module.editing_profile_preflight(execution_map, None)
        self.assertEqual(result["status"], "blocked")
        self.assertIn("profile_placeholder_used_without_inheritance", result["blocked_reasons"])

    def test_default_editing_profile_valid_passes(self) -> None:
        result = preflight_module.editing_profile_preflight({"profile_id": "default_general_content_v1"}, None)
        self.assertEqual(result["status"], "passed")
        self.assertFalse(result["profile_detail_pending"])

    def test_daily_tutorial_editing_profile_valid_passes(self) -> None:
        result = preflight_module.editing_profile_preflight({"profile_id": "daily_tutorial_profile_v1"}, None)
        self.assertEqual(result["status"], "passed")
        self.assertEqual(result["selected_profile"]["video_type"], "daily_tutorial")
        self.assertEqual(result["selected_profile"]["status"], "draft_profile_ready_for_first_real_video_test")
        self.assertFalse(result["profile_detail_pending"])

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


if __name__ == "__main__":
    unittest.main()
