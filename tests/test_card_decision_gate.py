import importlib.util
import json
import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "卡片判断闸门_card_decision_gate.py"
FIXTURE_PATH = ROOT / "codex_source" / "fixtures" / "卡片判断闸门_card_decision_gate_cases.json"


def load_module():
    spec = importlib.util.spec_from_file_location("card_decision_gate", SCRIPT_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def load_case(case_id):
    payload = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    for case in payload["cases"]:
        if case["case_id"] == case_id:
            return case
    raise AssertionError(f"missing fixture case: {case_id}")


class CardDecisionGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_module()

    def run_case(self, case_id):
        case = load_case(case_id)
        return self.module.run_card_decision(
            case["line_groups"],
            video_duration_override=case["video_duration"],
            content_route_card={"fixture": True},
        )

    def selected_types(self, report):
        return [card["card_type"] for card in report["card_decision_dry_run"]["selected_cards"]]

    def test_data_cluster_merges_to_one_data_result_card(self):
        report = self.run_case("data_cluster_merges_to_one_data_result_card")
        self.assertIn("data_result_card", self.selected_types(report))
        selected = [card for card in report["card_decision_dry_run"]["selected_cards"] if card["card_type"] == "data_result_card"]
        self.assertEqual(len(selected), 1)
        self.assertGreater(len(selected[0]["line_group_ids"]), 1)

    def test_multiple_metric_sentences_do_not_split_cards(self):
        report = self.run_case("multiple_metric_sentences_do_not_split_cards")
        selected = [card for card in report["card_decision_dry_run"]["selected_cards"] if card["card_type"] == "data_result_card"]
        self.assertEqual(len(selected), 1)

    def test_over_budget_keeps_data_result_card_over_process_summary_card(self):
        report = self.run_case("over_budget_keeps_data_result_card_over_process_summary_card")
        self.assertIn("data_result_card", self.selected_types(report))
        self.assertNotIn("process_summary_card", self.selected_types(report))
        dropped_types = [card["card_type"] for card in report["card_decision_dry_run"]["dropped_or_merged_cards"]]
        self.assertIn("process_summary_card", dropped_types)

    def test_card_inside_real_evidence_window_is_dropped(self):
        report = self.run_case("card_inside_real_evidence_window_is_dropped")
        blocked = report["card_decision_dry_run"]["evidence_window_protection_result"]["blocked_cards"]
        self.assertTrue(blocked)
        self.assertEqual(blocked[0]["reason"], "card_interrupts_key_evidence")

    def test_hyperframes_route_and_skin_remain_unchanged(self):
        report = self.run_case("hyperframes_route_and_skin_remain_unchanged")
        check = report["card_decision_dry_run"]["hyperframes_unchanged_check"]
        self.assertFalse(check["visual_route_changed"])
        self.assertFalse(check["motion_route_changed"])
        self.assertFalse(check["skin_changed"])

    def test_no_real_data_does_not_generate_data_result_card(self):
        report = self.run_case("no_real_data_does_not_generate_data_result_card")
        self.assertNotIn("data_result_card", self.selected_types(report))
        candidate = report["fourth_episode_card_decision_dry_run"]["add_data_result_card_candidate"]
        self.assertEqual(candidate["selected_or_dropped"], "candidate_blocked_missing_real_metric_values")

    def test_unclear_data_source_blocks_definite_data_card(self):
        report = self.run_case("unclear_data_source_blocks_definite_data_card")
        self.assertNotIn("data_result_card", self.selected_types(report))
        candidate = report["fourth_episode_card_decision_dry_run"]["add_data_result_card_candidate"]
        self.assertEqual(candidate["selected_or_dropped"], "candidate_blocked_data_source_unclear")


if __name__ == "__main__":
    unittest.main()
