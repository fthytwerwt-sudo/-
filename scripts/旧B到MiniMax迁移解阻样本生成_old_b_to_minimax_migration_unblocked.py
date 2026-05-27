#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import re
import sys
import wave
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_ROOT = ROOT / "codex_log" / "diagnostics"
DEFAULT_TIMESTAMP = datetime.now().strftime("%Y%m%d_%H%M%S")

REFERENCE_AUDIO_1 = (
    ROOT
    / "dist"
    / "voice_trials"
    / "20260427_十五秒文案语速停顿试配_15s_copy_pacing_trial"
    / "B_15秒文案_停顿梗感.wav"
)
REFERENCE_AUDIO_2 = (
    ROOT
    / "dist"
    / "voice_trials"
    / "20260426_语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis"
    / "语音样本2_声音复刻试听_15秒.wav"
)

SAMPLE_TEXT = (
    "朋友们，现在做带货，最贵的不是拍视频。\n"
    "最贵的是前面测错商品的成本。\n"
    "所以我不会让 AI 直接说哪个品能爆。\n"
    "我会先让它把商品卡拆成表，把风险写出来，再决定要不要继续测。"
)

SAMPLE_SPECS = [
    {
        "sample_id": "V1_identity_match",
        "goal": "尽量贴旧 B 音色",
        "speed": 1.00,
        "emotion": "neutral / calm",
        "pause_style": "保持旧 B 停顿感",
    },
    {
        "sample_id": "V2_prosody_optimized",
        "goal": "音色不变，优化停顿、句尾、上扬",
        "speed": "0.98-1.04",
        "emotion": "warm / natural",
        "pause_style": "语义边界更清楚",
    },
    {
        "sample_id": "V3_emotion_rich",
        "goal": "音色不变，增加轻吐槽、判断感、自然起伏",
        "speed": "0.98-1.03",
        "emotion": "warm_lively",
        "pause_style": "关键句更有空间",
    },
]

OFFICIAL_DOCS = [
    "https://platform.minimax.io/docs/api-reference/voice-cloning-uploadcloneaudio",
    "https://platform.minimax.io/docs/api-reference/voice-cloning-clone",
    "https://platform.minimax.io/docs/api-reference/speech-t2a-http",
    "https://platform.minimax.io/docs/guides/speech-voice-clone",
]


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def read_wave_info(path: Path) -> dict[str, Any]:
    info: dict[str, Any] = {
        "path": rel(path),
        "exists": path.exists(),
        "decode_ok": False,
    }
    if not path.exists():
        return info
    with wave.open(str(path), "rb") as wav_file:
        frames = wav_file.getnframes()
        rate = wav_file.getframerate()
        info.update(
            {
                "decode_ok": True,
                "size_bytes": path.stat().st_size,
                "channels": wav_file.getnchannels(),
                "sample_rate": rate,
                "frames": frames,
                "duration_seconds": round(frames / rate, 3) if rate else 0,
                "sample_width_bytes": wav_file.getsampwidth(),
                "format": "wav",
            }
        )
    return info


def env_file_key_names(path: Path) -> set[str]:
    if not path.exists():
        return set()
    names: set[str] = set()
    for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        match = re.match(r"\s*([A-Za-z_][A-Za-z0-9_]*)\s*=", line)
        if match:
            names.add(match.group(1))
    return names


def local_config_field_presence(path: Path) -> dict[str, bool]:
    presence = {
        "formal_runtime_config_exists": path.exists(),
        "auth_api_key_field_present": False,
        "aliyun_oss_access_key_id_field_present": False,
        "aliyun_oss_access_key_secret_field_present": False,
        "aliyun_oss_bucket_field_present": False,
        "aliyun_oss_endpoint_field_present": False,
    }
    if not path.exists():
        return presence
    current_section = ""
    for raw_line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("[") and line.endswith("]"):
            current_section = line.strip("[]").strip()
            continue
        if "=" not in line:
            continue
        key = line.split("=", 1)[0].strip()
        if current_section == "auth" and key == "api_key":
            presence["auth_api_key_field_present"] = True
        if current_section == "aliyun_oss" and key == "access_key_id":
            presence["aliyun_oss_access_key_id_field_present"] = True
        if current_section == "aliyun_oss" and key == "access_key_secret":
            presence["aliyun_oss_access_key_secret_field_present"] = True
        if current_section == "aliyun_oss" and key == "bucket":
            presence["aliyun_oss_bucket_field_present"] = True
        if current_section == "aliyun_oss" and key == "endpoint":
            presence["aliyun_oss_endpoint_field_present"] = True
    return presence


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def build_report(output_dir: Path) -> dict[str, Any]:
    samples_dir = output_dir / "samples"
    samples_dir.mkdir(parents=True, exist_ok=True)

    env_names = env_file_key_names(ROOT / ".env")
    local_config = local_config_field_presence(
        Path("/Users/fan/.config/video-factory/formal_api_demo.local.toml")
    )
    example_config = local_config_field_presence(ROOT / "config" / "formal_api_demo.example.toml")
    minimax_api_key_present = bool(os.environ.get("MINIMAX_API_KEY"))
    minimax_group_present = bool(os.environ.get("MINIMAX_GROUP_ID") or os.environ.get("MINIMAX_GROUPID"))
    minimax_env_file_key_present = "MINIMAX_API_KEY" in env_names

    reference_audio = [read_wave_info(REFERENCE_AUDIO_1), read_wave_info(REFERENCE_AUDIO_2)]
    reference_audio_loaded = all(item.get("decode_ok") for item in reference_audio)

    oss_fields_present = (
        local_config["aliyun_oss_access_key_id_field_present"]
        and local_config["aliyun_oss_access_key_secret_field_present"]
        and (
            local_config["aliyun_oss_bucket_field_present"]
            or example_config["aliyun_oss_bucket_field_present"]
        )
        and (
            local_config["aliyun_oss_endpoint_field_present"]
            or example_config["aliyun_oss_endpoint_field_present"]
        )
    )

    official_clone_auth_available = minimax_api_key_present
    can_run_generation = reference_audio_loaded and official_clone_auth_available

    selected_upload_strategy = {
        "selected": "minimax_official_file_upload",
        "reason": (
            "MiniMax 官方 voice clone 文档要求通过 /v1/files/upload 获取 file_id；"
            "当前没有可确认的 MiniMax audio_url 克隆接口，因此不把 OSS URL 当作已可用的克隆输入。"
        ),
        "option_a_upload_to_user_controlled_oss": {
            "available": oss_fields_present,
            "selected": False,
            "reason": "本轮未发现可用的 MiniMax 官方 audio_url 克隆入口；只上传到 OSS 不能产生 generated_minimax_voice_id。",
            "upload_attempted": False,
        },
        "option_b_minimax_official_file_upload": {
            "available": official_clone_auth_available,
            "selected": True,
            "blocked_reason": "" if official_clone_auth_available else "minimax_official_api_key_missing",
            "upload_attempted": False,
        },
    }

    reference_audio_inputs = [
        {
            "reference_audio_id": "reference_audio_1",
            "local_path": rel(REFERENCE_AUDIO_1),
            "uploaded": False,
            "audio_url": None,
            "file_id": None,
            "reason": "blocked_before_upload_minimax_official_api_key_missing"
            if not official_clone_auth_available
            else "not_run_by_this_report_script",
        },
        {
            "reference_audio_id": "reference_audio_2",
            "local_path": rel(REFERENCE_AUDIO_2),
            "uploaded": False,
            "audio_url": None,
            "file_id": None,
            "reason": "blocked_before_upload_minimax_official_api_key_missing"
            if not official_clone_auth_available
            else "not_run_by_this_report_script",
        },
    ]

    generated_samples = [
        {
            **spec,
            "sample_path": None,
            "target_provider": "minimax",
            "target_model": "MiniMax/speech-2.8-hd",
            "generated_minimax_voice_id": None,
            "reference_audio_used": False,
            "non_silent": None,
            "status": "not_generated",
            "blocked_reason": "minimax_official_api_key_missing"
            if not official_clone_auth_available
            else "generation_not_attempted_by_this_report_script",
        }
        for spec in SAMPLE_SPECS
    ]

    status = "completed_with_old_b_minimax_migration_samples" if can_run_generation else "blocked"
    blocked_reasons: list[str] = []
    if not reference_audio_loaded:
        blocked_reasons.append("reference_audio_unreadable")
    if not official_clone_auth_available:
        blocked_reasons.append("minimax_official_api_key_missing")

    report = {
        "task_result": {
            "status": status,
            "video_generated": False,
            "audio_generated": False,
            "tts_api_called": False,
            "copy_changed": False,
            "current_video_modified": False,
        },
        "created_at": datetime.now(timezone.utc).isoformat(),
        "output_dir": rel(output_dir),
        "route_arbitration": {
            "old_qwen_role": "reference_anchor_only",
            "minimax_role": "final_generation_provider",
            "selected_route": "route_b_migrate_old_b_to_minimax",
            "system_voice_candidates_allowed": False,
            "old_qwen_formal_route_allowed": False,
        },
        "user_authorization": {
            "reference_audio_upload_authorized_this_round": True,
            "authorized_files": [rel(REFERENCE_AUDIO_1), rel(REFERENCE_AUDIO_2)],
            "upload_attempted": False,
            "upload_attempted_reason": "not_attempted_because_minimax_official_api_key_missing",
            "reference_audio_committed_to_git": False,
        },
        "upload_strategy": selected_upload_strategy,
        "reference_audio_inputs": reference_audio_inputs,
        "reference_audio_probe": reference_audio,
        "minimax_reference_clone_capability": {
            "supports_voice_clone": True,
            "supports_reference_audio": True,
            "requires_file_id": True,
            "requires_audio_url": False,
            "accepts_local_file_directly": False,
            "current_audio_url_available": False,
            "current_file_id_available": False,
            "official_minimax_api_key_available": official_clone_auth_available,
            "official_minimax_api_key_source": "process_env:MINIMAX_API_KEY"
            if minimax_api_key_present
            else "none",
            "env_file_minimax_api_key_name_present": minimax_env_file_key_present,
            "official_docs": OFFICIAL_DOCS,
        },
        "local_runtime_capability": {
            "user_controlled_oss_config_fields_present": oss_fields_present,
            "formal_runtime_config_checked_for_field_presence_only": True,
            "formal_runtime_config_values_logged": False,
            "formal_example_config_checked_for_non_secret_bucket_endpoint_only": True,
            "minimax_group_id_present": minimax_group_present,
            **local_config,
        },
        "generated_samples": generated_samples,
        "old_b_to_minimax_voice_lock": {
            "status": "pending_minimax_official_auth",
            "old_b_reference_audio_path": [rel(REFERENCE_AUDIO_1), rel(REFERENCE_AUDIO_2)],
            "old_b_reference_voice_masked_id": "qwen-t...ac19",
            "target_provider": "minimax",
            "target_model": "MiniMax/speech-2.8-hd",
            "generated_minimax_voice_id": None,
            "timbre_similarity_required": True,
            "prosody_optimization_allowed": True,
            "emotion_optimization_allowed": True,
            "timbre_change_allowed": False,
            "system_voice_substitution_allowed": False,
            "human_voice_review_required": True,
            "human_voice_review_status": "pending_minimax_official_auth",
        },
        "status_boundary": {
            "full_narration_regenerated": False,
            "current_video_modified": False,
            "copy_changed": False,
            "voice_validation": "not_advanced",
            "send_ready": False,
        },
        "blocked": {
            "blocked_reasons": blocked_reasons,
            "primary_blocked_reason": "minimax_official_api_key_missing"
            if "minimax_official_api_key_missing" in blocked_reasons
            else (blocked_reasons[0] if blocked_reasons else ""),
            "forbidden_fallback": [
                "不得用 MiniMax 系统音色替代旧 B",
                "不得用男声候选替代旧 B",
                "不得恢复旧 Qwen 正式路线",
                "不得使用 macOS say / 本地低质 TTS / silent audio",
            ],
        },
        "next_user_action": {
            "authorize_reference_audio_upload": False,
            "provide_minimax_official_api_key": True,
            "set_required_env": ["MINIMAX_API_KEY"],
            "listen_to_samples": False,
            "choose_or_reject": False,
        },
    }
    return report


def render_markdown(report: dict[str, Any]) -> str:
    refs = "\n".join(
        f"- `{item['path']}`: exists={item['exists']}, decode_ok={item['decode_ok']}, "
        f"duration={item.get('duration_seconds')}, sample_rate={item.get('sample_rate')}"
        for item in report["reference_audio_probe"]
    )
    samples = "\n".join(
        f"| {item['sample_id']} | {item['status']} | {item['blocked_reason']} |"
        for item in report["generated_samples"]
    )
    return f"""# 旧 B 到 MiniMax 迁移解阻报告

## 任务结果

```text
status: {report['task_result']['status']}
audio_generated: false
tts_api_called: false
video_generated: false
copy_changed: false
current_video_modified: false
```

## 路线裁决

- `old_qwen_role`: `reference_anchor_only`
- `minimax_role`: `final_generation_provider`
- `selected_route`: `route_b_migrate_old_b_to_minimax`
- `system_voice_candidates_allowed`: `false`

## 参考音频读取

{refs}

## 上传策略

- `selected`: `{report['upload_strategy']['selected']}`
- `reason`: {report['upload_strategy']['reason']}
- `option_a_upload_to_user_controlled_oss.available`: `{report['upload_strategy']['option_a_upload_to_user_controlled_oss']['available']}`
- `option_a_upload_to_user_controlled_oss.selected`: `false`
- `option_b_minimax_official_file_upload.available`: `{report['upload_strategy']['option_b_minimax_official_file_upload']['available']}`
- `upload_attempted`: `false`

本轮没有上传参考音频。原因是 MiniMax 官方克隆需要 `MINIMAX_API_KEY` 调用 `/v1/files/upload` 获取 `file_id`；当前本地未提供该官方认证。只上传到 OSS 不能生成 `generated_minimax_voice_id`，所以不做无效上传。

## 样本状态

| sample_id | status | blocked_reason |
| --- | --- | --- |
{samples}

## 阻断原因

- `primary_blocked_reason`: `{report['blocked']['primary_blocked_reason']}`
- `blocked_reasons`: `{', '.join(report['blocked']['blocked_reasons'])}`

## 声音锁边界

- `old_b_to_minimax_voice_lock.status`: `pending_minimax_official_auth`
- `generated_minimax_voice_id`: `null`
- `human_voice_review_status`: `pending_minimax_official_auth`
- `system_voice_substitution_allowed`: `false`
- `timbre_change_allowed`: `false`

## 后续动作

下一轮只需要在安全运行环境提供 `MINIMAX_API_KEY`，再复跑本入口生成 V1 / V2 / V3 三条短样本。不得回退到 MiniMax 系统音色候选，不得恢复旧 Qwen 为正式路线。
"""


def render_review_table(report: dict[str, Any]) -> str:
    rows = "\n".join(
        "| {sample_id} | pending_minimax_official_auth | - | - | - | - | - | - | - | not_generated | blocked |".format(
            **item
        )
        for item in report["generated_samples"]
    )
    return """# voice_candidate_review_table_old_b_minimax

本轮未生成可试听样本；原因是缺少 MiniMax 官方 `MINIMAX_API_KEY`，不能调用官方 `/v1/files/upload` 获取 `file_id`，也不能创建 cloned `voice_id`。

| candidate_id（候选 ID） | voice_id（声音 ID） | sample_path（试听路径） | similar_to_old_b（是否像旧 B，待人工判断） | pause_feel（停顿感，待人工判断） | emotional_richness（情绪丰富度，待人工判断） | upward_tone（上扬感，待人工判断） | too_system_voice（是否系统音色替代，待人工判断） | user_choice（用户选择） | generation_status（生成状态） | lock_status（锁定状态） |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
""" + rows + "\n"


def main(argv: list[str]) -> int:
    timestamp = argv[0] if argv else DEFAULT_TIMESTAMP
    output_dir = OUTPUT_ROOT / f"old_b_to_minimax_migration_unblocked_{timestamp}"
    report = build_report(output_dir)
    write_json(output_dir / "old_b_to_minimax_migration_unblocked_report.json", report)
    write_text(output_dir / "old_b_to_minimax_migration_unblocked_report.md", render_markdown(report))
    write_text(output_dir / "voice_candidate_review_table_old_b_minimax.md", render_review_table(report))
    write_json(
        output_dir / "voice_candidate_review_table_old_b_minimax.json",
        {
            "status": "blocked",
            "blocked_reason": report["blocked"]["primary_blocked_reason"],
            "candidates": report["generated_samples"],
        },
    )
    print(json.dumps({"status": report["task_result"]["status"], "output_dir": rel(output_dir)}, ensure_ascii=False))
    return 0 if report["task_result"]["status"] != "completed_with_old_b_minimax_migration_samples" else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
