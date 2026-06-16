"""Normalize user input into adapter workflow intents."""

from __future__ import annotations

from dataclasses import dataclass


SAMPLE_INPUTS: dict[str, str] = {
    "copy_to_video": "帮我把这个文案做成视频",
    "material_audit": "解析素材，看哪些能用",
    "editing_execution": "继续剪辑执行",
    "operation_data_review": "根据数据复盘下一条怎么改",
    "reference_to_execution": "按这个参考视频效果做",
    "adapter_infrastructure": "继续 agent-service-toolkit 适配",
}


INTENT_TO_WORKFLOW: dict[str, str] = {
    "copy_to_video": "copy_to_video_workflow",
    "material_audit": "material_audit_workflow",
    "editing_execution": "editing_execution_workflow",
    "operation_data_review": "operation_data_review_workflow",
    "reference_to_execution": "reference_to_execution_workflow",
    "adapter_infrastructure": "adapter_infrastructure_workflow",
}


@dataclass(frozen=True)
class CleanedTask:
    raw_input: str
    normalized_input: str
    intent: str
    workflow: str
    recognized_sample: str
    signals: tuple[str, ...]

    def to_dict(self) -> dict[str, object]:
        return {
            "raw_input": self.raw_input,
            "normalized_input": self.normalized_input,
            "intent": self.intent,
            "workflow": self.workflow,
            "recognized_sample": self.recognized_sample,
            "signals": list(self.signals),
        }


def normalize_input(user_input: str) -> str:
    return " ".join(user_input.strip().split()).lower()


def clean_task(user_input: str) -> CleanedTask:
    normalized = normalize_input(user_input)
    exact_samples = {normalize_input(text): key for key, text in SAMPLE_INPUTS.items()}
    if normalized in exact_samples:
        intent = exact_samples[normalized]
        return CleanedTask(
            raw_input=user_input,
            normalized_input=normalized,
            intent=intent,
            workflow=INTENT_TO_WORKFLOW[intent],
            recognized_sample=intent,
            signals=("exact_sample_match",),
        )

    keyword_rules: tuple[tuple[str, tuple[str, ...]], ...] = (
        ("adapter_infrastructure", ("agent-service-toolkit", "适配", "adapter")),
        ("reference_to_execution", ("参考", "样片", "reference")),
        ("operation_data_review", ("复盘", "数据", "下一条", "24h", "72h", "7d")),
        ("editing_execution", ("剪辑", "执行", "timeline")),
        ("material_audit", ("素材", "解析", "能用")),
        ("copy_to_video", ("文案", "做成视频", "视频")),
    )
    for intent, keywords in keyword_rules:
        hits = tuple(keyword for keyword in keywords if keyword in normalized)
        if hits:
            return CleanedTask(
                raw_input=user_input,
                normalized_input=normalized,
                intent=intent,
                workflow=INTENT_TO_WORKFLOW[intent],
                recognized_sample="keyword_match",
                signals=hits,
            )

    return CleanedTask(
        raw_input=user_input,
        normalized_input=normalized,
        intent="unknown",
        workflow="adapter_infrastructure_workflow",
        recognized_sample="unrecognized",
        signals=("fallback_to_adapter_infrastructure",),
    )
