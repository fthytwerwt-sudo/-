import importlib.util
import json
import pathlib
import tempfile
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "素材证据闸门_material_evidence_gate.py"
FIXTURE_PATH = ROOT / "codex_source" / "fixtures" / "素材证据闸门_material_evidence_gate_cases.json"


def load_module():
    spec = importlib.util.spec_from_file_location("material_evidence_gate", SCRIPT_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def load_fixture():
    return json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))


class MaterialEvidenceGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_module()
        cls.fixture = load_fixture()

    def run_case(self, case_id):
        case = next(item for item in self.fixture["cases"] if item["case_id"] == case_id)
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = pathlib.Path(tmp)
            material_report = tmp_path / "material_detail_report.md"
            timeline = tmp_path / "script_to_timeline_map.json"
            output_dir = tmp_path / "out"
            material_report.write_text(self.fixture["material_report_md"], encoding="utf-8")
            timeline.write_text(json.dumps({"line_groups": case["line_groups"]}, ensure_ascii=False), encoding="utf-8")
            return self.module.run_material_evidence_gate(
                material_report=material_report,
                timeline=timeline,
                output_dir=output_dir,
            )

    def first_entry(self, result):
        return result["line_group_evidence_gate_report"]["line_group_evidence_gate"][0]

    def preflight(self, result):
        return result["auto_storyboard_preflight_report"]["auto_storyboard_preflight_report"]

    def test_direct_match_process_material(self):
        entry = self.first_entry(self.run_case("direct_match_process_material"))
        self.assertEqual(entry["evidence_match_status"], "direct_match")

    def test_proxy_match_transition_background(self):
        entry = self.first_entry(self.run_case("proxy_match_transition_background"))
        self.assertEqual(entry["evidence_match_status"], "proxy_match")

    def test_card_required_for_unproved_judgment(self):
        entry = self.first_entry(self.run_case("card_required_for_unproved_judgment"))
        self.assertEqual(entry["evidence_match_status"], "card_required")
        self.assertIn("card_required_unresolved", entry["blocked_if"])

    def test_card_required_resolved_for_judgment(self):
        entry = self.first_entry(self.run_case("card_required_resolved_for_judgment"))
        self.assertEqual(entry["evidence_match_status"], "card_required_resolved")

    def test_blocked_no_evidence(self):
        preflight = self.preflight(self.run_case("blocked_no_evidence"))
        self.assertEqual(preflight["blocked_no_evidence_count"], 1)
        self.assertFalse(preflight["auto_edit_allowed"])

    def test_selected_material_in_cannot_support(self):
        preflight = self.preflight(self.run_case("selected_material_in_cannot_support"))
        self.assertEqual(preflight["selected_material_in_cannot_support_count"], 1)
        self.assertFalse(preflight["auto_edit_allowed"])

    def test_privacy_high_selected(self):
        preflight = self.preflight(self.run_case("privacy_high_selected"))
        self.assertEqual(preflight["privacy_high_selected_count"], 1)
        self.assertFalse(preflight["auto_edit_allowed"])

    def test_data_sentence_without_source(self):
        preflight = self.preflight(self.run_case("data_sentence_without_source"))
        self.assertEqual(preflight["data_sentence_without_source_count"], 1)
        self.assertFalse(preflight["auto_edit_allowed"])

    def test_action_sentence_hard_mapped_to_recording(self):
        preflight = self.preflight(self.run_case("action_sentence_hard_mapped_to_recording"))
        self.assertEqual(preflight["action_sentence_without_card_or_direct_visual_count"], 1)
        self.assertFalse(preflight["auto_edit_allowed"])

    def test_render_blocked_when_auto_edit_false(self):
        result = self.run_case("render_blocked_when_auto_edit_false")
        with self.assertRaises(RuntimeError):
            self.module.assert_render_allowed(result["auto_storyboard_preflight_report"])


if __name__ == "__main__":
    unittest.main()
