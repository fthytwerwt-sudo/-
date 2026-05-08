from __future__ import annotations

import asyncio
import base64
import copy
import json
import pathlib
import shutil
import subprocess
import sys
from typing import Any
import wave

ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import websockets

from formal_api_demo_core import (
    DEFAULT_FORMAL_LOCAL_CONFIG_PATH,
    STATUS_SUCCESS,
    execute_tts_probe,
    load_formal_config,
)

EXAMPLE_CONFIG_PATH = ROOT / "config" / "formal_api_demo.example.toml"
RUNTIME_CONFIG_PATH = pathlib.Path(DEFAULT_FORMAL_LOCAL_CONFIG_PATH)
OUTPUT_DIR = ROOT / "dist" / "20260417_豆包的正确打开方式_vnext"
VOICE_CANDIDATES_DIR = OUTPUT_DIR / "voice_candidates"
REPORT_PATH = OUTPUT_DIR / "voice_route_report.json"
LISTEN_SHEET_PATH = OUTPUT_DIR / "voice_listen_sheet.md"
BLOCKED_SENTINEL_PATH = VOICE_CANDIDATES_DIR / "候选阻塞_blocked.json"
ROUTE_PLAN_PATH = OUTPUT_DIR / "route_plan.json"

POSTPROCESS_FILTER = (
    "highpass=f=80,"
    "lowpass=f=12000,"
    "deesser=i=0.4:m=0.5:f=0.5:s=o,"
    "acompressor=threshold=-18dB:ratio=2.5:attack=20:release=120:makeup=3,"
    "loudnorm=I=-16:TP=-1.5:LRA=7"
)


def resolve_ffmpeg() -> str:
    system_ffmpeg = shutil.which("ffmpeg")
    if system_ffmpeg:
        return system_ffmpeg
    bundled = ROOT / "node_modules" / "ffmpeg-static" / "ffmpeg"
    if bundled.exists():
        return str(bundled)
    raise RuntimeError("缺少 ffmpeg")


def run_command(args: list[str]) -> None:
    subprocess.run(args, check=True)


def load_probe_text() -> str:
    route_plan = json.loads(ROUTE_PLAN_PATH.read_text(encoding="utf-8"))
    return route_plan["blocks"][0]["segments"][0]["voiceover_text"]


def build_minimal_video_spec(probe_text: str) -> dict[str, Any]:
    return {
        "hook": probe_text,
        "segments": [
            {
                "segment_id": "voice_probe",
                "voiceover_text": probe_text,
            }
        ],
    }


def build_base_config() -> dict[str, Any]:
    config_bundle = load_formal_config(EXAMPLE_CONFIG_PATH, RUNTIME_CONFIG_PATH)
    return config_bundle["config"]


def candidate_specs() -> list[dict[str, Any]]:
    return [
        {
            "candidate_id": "A1_qwen3_serena_light",
            "route": "primary",
            "label": "Serena 轻陪伴",
            "provider": "aliyun_bailian",
            "model": "qwen3-tts-instruct-flash-realtime",
            "voice": "Serena",
            "instruction": "你要像轻陪伴的游戏向导一样说话，低压、自然、克制，不要播音腔，不要客服腔，不要装嫩，重点句更稳，句间停顿更自然。",
            "speech_rate": 0.98,
            "pitch_rate": 0.97,
            "volume": 50,
            "postprocess": POSTPROCESS_FILTER,
        },
        {
            "candidate_id": "A2_qwen3_serena_steady",
            "route": "primary",
            "label": "Serena 更克制",
            "provider": "aliyun_bailian",
            "model": "qwen3-tts-instruct-flash-realtime",
            "voice": "Serena",
            "instruction": "你像冷静、低压的中文向导，句子更稳，减少夸张起伏，判断句收得更准，避免任何新闻播音和客服播报感。",
            "speech_rate": 0.94,
            "pitch_rate": 0.95,
            "volume": 48,
            "postprocess": POSTPROCESS_FILTER,
        },
        {
            "candidate_id": "A3_qwen3_cherry_hint",
            "route": "primary",
            "label": "Cherry 轻提醒",
            "provider": "aliyun_bailian",
            "model": "qwen3-tts-instruct-flash-realtime",
            "voice": "Cherry",
            "instruction": "你像一个轻提醒型的中文向导，清楚但不强势，带一点陪伴感，不要广告腔，不要朗读腔，重点词轻轻带出来。",
            "speech_rate": 0.99,
            "pitch_rate": 0.98,
            "volume": 49,
            "postprocess": POSTPROCESS_FILTER,
        },
        {
            "candidate_id": "B1_cosy_plus_longanling",
            "route": "fallback",
            "label": "cosyvoice-v3-plus + longanling_v3",
            "provider": "aliyun_bailian",
            "model": "cosyvoice-v3-plus",
            "voice": "longanling_v3",
            "instruction": "你说话的情感是neutral。",
            "speech_rate": 1.02,
            "pitch_rate": 0.96,
            "volume": 48,
            "postprocess": POSTPROCESS_FILTER,
        },
        {
            "candidate_id": "B2_cosy_flash_longanqin",
            "route": "fallback",
            "label": "cosyvoice-v3-flash + longanqin_v3",
            "provider": "aliyun_bailian",
            "model": "cosyvoice-v3-flash",
            "voice": "longanqin_v3",
            "instruction": "你说话的情感是neutral。",
            "speech_rate": 1.0,
            "pitch_rate": 0.96,
            "volume": 47,
            "postprocess": POSTPROCESS_FILTER,
        },
        {
            "candidate_id": "B3_cosy_flash_longanwen",
            "route": "fallback",
            "label": "cosyvoice-v3-flash + longanwen_v3",
            "provider": "aliyun_bailian",
            "model": "cosyvoice-v3-flash",
            "voice": "longanwen_v3",
            "instruction": "你说话的情感是neutral。",
            "speech_rate": 0.98,
            "pitch_rate": 0.95,
            "volume": 47,
            "postprocess": POSTPROCESS_FILTER,
        },
    ]


def build_candidate_config(base_config: dict[str, Any], spec: dict[str, Any]) -> dict[str, Any]:
    config = copy.deepcopy(base_config)
    config.setdefault("provider", {})
    config.setdefault("tts", {})
    config["provider"]["name"] = "aliyun_bailian"
    config["tts"]["api_route_family"] = "aliyun_bailian_cosyvoice"
    config["tts"]["model"] = spec["model"]
    config["tts"]["voice"] = spec["voice"]
    config["tts"]["instruction"] = spec["instruction"]
    config["tts"]["speech_rate"] = spec["speech_rate"]
    config["tts"]["pitch_rate"] = spec["pitch_rate"]
    config["tts"]["volume"] = spec["volume"]
    config["tts"]["response_format"] = "mp3"
    return config


def postprocess_audio(ffmpeg: str, raw_path: pathlib.Path, processed_path: pathlib.Path, filter_graph: str) -> None:
    processed_path.parent.mkdir(parents=True, exist_ok=True)
    run_command(
        [
            ffmpeg,
            "-y",
            "-i",
            str(raw_path),
            "-af",
            filter_graph,
            "-ar",
            "48000",
            "-ac",
            "1",
            str(processed_path),
        ]
    )


async def _recv_until_session_ready(ws: Any) -> None:
    while True:
        event = json.loads(await ws.recv())
        event_type = event.get("type")
        if event_type in {"session.created", "session.updated"}:
            return
        if event_type == "error":
            raise RuntimeError(json.dumps(event.get("error", {}), ensure_ascii=False))


async def _qwen_realtime_synthesize(
    *,
    api_key: str,
    model: str,
    voice: str,
    instruction: str,
    text: str,
    output_wav_path: pathlib.Path,
) -> dict[str, Any]:
    url = f"wss://dashscope.aliyuncs.com/api-ws/v1/realtime?model={model}"
    headers = {"Authorization": f"Bearer {api_key}"}
    chunks: list[bytes] = []
    request_debug = {
        "provider": "aliyun_bailian",
        "api_route_family": "aliyun_qwen_realtime_websocket",
        "request_method": "WEBSOCKET",
        "base_url": url,
        "sdk_call": "websockets.connect",
        "voice": voice,
        "instructions_present": bool(instruction.strip()),
        "response_format": "pcm",
        "sample_rate": 24000,
    }

    async with websockets.connect(url, additional_headers=headers) as ws:
        await ws.send(
            json.dumps(
                {
                    "type": "session.update",
                    "session": {
                        "mode": "commit",
                        "voice": voice,
                        "instructions": instruction,
                        "optimize_instructions": True,
                        "language_type": "Chinese",
                        "response_format": "pcm",
                        "sample_rate": 24000,
                    },
                },
                ensure_ascii=False,
            )
        )
        await _recv_until_session_ready(ws)
        await ws.send(json.dumps({"type": "input_text_buffer.append", "text": text}, ensure_ascii=False))
        await ws.send(json.dumps({"type": "input_text_buffer.commit"}, ensure_ascii=False))

        while True:
            event = json.loads(await ws.recv())
            event_type = event.get("type")
            if event_type == "response.audio.delta":
                chunks.append(base64.b64decode(event.get("delta", "")))
            elif event_type == "response.done":
                break
            elif event_type == "error":
                raise RuntimeError(json.dumps(event.get("error", {}), ensure_ascii=False))

        try:
            await ws.send(json.dumps({"type": "session.finish"}, ensure_ascii=False))
        except Exception:
            pass

    output_wav_path.parent.mkdir(parents=True, exist_ok=True)
    with wave.open(str(output_wav_path), "wb") as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(24000)
        wav_file.writeframes(b"".join(chunks))
    return request_debug


def rank_successes(results: list[dict[str, Any]]) -> dict[str, Any] | None:
    successes = [item for item in results if item["status"] == STATUS_SUCCESS]
    if not successes:
        return None
    route_priority = {"primary": 0, "fallback": 1}
    voice_priority = {
        "A1_qwen3_serena_light": 0,
        "A2_qwen3_serena_steady": 1,
        "A3_qwen3_cherry_hint": 2,
        "B1_cosy_plus_longanling": 3,
        "B2_cosy_flash_longanqin": 4,
        "B3_cosy_flash_longanwen": 5,
    }
    return sorted(
        successes,
        key=lambda item: (
            route_priority.get(item["route"], 99),
            voice_priority.get(item["candidate_id"], 999),
        ),
    )[0]


def build_listen_sheet(results: list[dict[str, Any]], selected: dict[str, Any] | None, probe_text: str) -> str:
    lines = [
        "# 阿里内部声音候选听审单",
        "",
        "## 统一测试文案",
        "",
        "```text",
        probe_text,
        "```",
        "",
        "## 候选结果",
        "",
        "| 候选 | 路线 | 模型 | 音色 | 状态 | 备注 |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for item in results:
        note = item.get("blocked_reason") or item.get("error_message") or "已落盘，待人工试听"
        lines.append(
            f"| `{item['candidate_id']}` | `{item['route']}` | `{item['model']}` | `{item['voice']}` | `{item['status']}` | {note} |"
        )
    lines.extend(
        [
            "",
            "## 四项核心维度",
            "",
            "- `自然度`：`待验证`，需要人工试听确认。",
            "- `向导感`：`待验证`，需要人工试听确认。",
            "- `停顿与韵律`：`待验证`，需要人工试听确认。",
            "- `播音腔 / AI 感`：`待验证`，需要人工试听确认。",
            "",
        ]
    )
    if selected is None:
        lines.extend(
            [
                "## 当前结论",
                "",
                "- `已确认` 阿里内部已按本轮优先顺序排尽，但没有产出可进入听审的合格候选。",
            ]
        )
    else:
        lines.extend(
            [
                "## 当前结论",
                "",
                f"- `推测` 机器侧暂定主路线：`{selected['model']} + {selected['voice']}`。",
                "- `待验证` 该结论仍需人工试听，不得直接写成最终过线。",
            ]
        )
    return "\n".join(lines) + "\n"


def build_report(results: list[dict[str, Any]], selected: dict[str, Any] | None, probe_text: str) -> dict[str, Any]:
    overall_status = "success" if selected is not None else "blocked"
    if selected is None:
        blocked_reason = "阿里内部已按本轮优先顺序排尽，但未产出可进入听审的成功候选。"
    else:
        blocked_reason = ""
    return {
        "schema_version": "video_factory_voice_route_report/v2",
        "task_object": "《豆包的正确打开方式》vNext",
        "lane": "B线｜声音线（阿里体系内先排尽）",
        "status": overall_status,
        "report_status": "已确认" if selected is not None else "部分成立",
        "provider_scope": "aliyun_only",
        "probe_text": probe_text,
        "priority_order": [item["candidate_id"] for item in results],
        "results": results,
        "selected_route": None
        if selected is None
        else {
            "status": "推测",
            "candidate_id": selected["candidate_id"],
            "model": selected["model"],
            "voice": selected["voice"],
            "route": selected["route"],
            "selection_reason": "按本轮优先级排序，在真实成功候选中优先选择 qwen3 主路线，再选阿里内部 fallback；该结果仍需人工试听确认。",
            "why_others_rejected": [
                {
                    "candidate_id": item["candidate_id"],
                    "reason": item.get("blocked_reason") or item.get("error_message") or "优先级低于暂定主路线，待人工听审再决定是否保留。",
                }
                for item in results
                if item["candidate_id"] != selected["candidate_id"]
            ],
        },
        "blocked_reason": blocked_reason,
        "dimension_status": {
            "自然度": "待验证" if selected is not None else "blocked",
            "向导感": "待验证" if selected is not None else "blocked",
            "停顿与韵律": "待验证" if selected is not None else "blocked",
            "播音腔 / AI 感": "待验证" if selected is not None else "blocked",
        },
    }


def main() -> int:
    ffmpeg = resolve_ffmpeg()
    base_config = build_base_config()
    probe_text = load_probe_text()
    video_spec = build_minimal_video_spec(probe_text)
    VOICE_CANDIDATES_DIR.mkdir(parents=True, exist_ok=True)

    results: list[dict[str, Any]] = []
    for spec in candidate_specs():
        candidate_dir = VOICE_CANDIDATES_DIR / spec["candidate_id"]
        candidate_dir.mkdir(parents=True, exist_ok=True)
        config = build_candidate_config(base_config, spec)
        request_debug: dict[str, Any] = {}
        if spec["model"] == "qwen3-tts-instruct-flash-realtime":
            raw_audio_path = candidate_dir / f"{spec['candidate_id']}_raw.wav"
            try:
                request_debug = asyncio.run(
                    _qwen_realtime_synthesize(
                        api_key=str(base_config["auth"]["api_key"]),
                        model=spec["model"],
                        voice=spec["voice"],
                        instruction=spec["instruction"],
                        text=probe_text,
                        output_wav_path=raw_audio_path,
                    )
                )
                probe = {
                    "status": STATUS_SUCCESS,
                    "request_id": None,
                    "request_debug": request_debug,
                    "blocked_reason": "",
                    "error_message": "",
                    "failure_reason": "",
                }
            except Exception as exc:
                probe = {
                    "status": "failed",
                    "request_id": None,
                    "request_debug": request_debug,
                    "blocked_reason": str(exc),
                    "error_message": str(exc),
                    "failure_reason": "aliyun_qwen_realtime_request_failed",
                }
        else:
            probe = execute_tts_probe(
                video_spec=video_spec,
                config=config,
                output_dir=candidate_dir,
                probe_text=probe_text,
                probe_text_source="vnext_hook_voiceover",
                output_stem=spec["candidate_id"],
            )
            raw_audio_path = candidate_dir / "tts" / f"{spec['candidate_id']}.mp3"
        processed_audio_path = candidate_dir / f"{spec['candidate_id']}_processed.wav"
        candidate_result = {
            "candidate_id": spec["candidate_id"],
            "route": spec["route"],
            "provider": spec["provider"],
            "model": spec["model"],
            "voice": spec["voice"],
            "instruction": spec["instruction"],
            "speech_rate": spec["speech_rate"],
            "pitch_rate": spec["pitch_rate"],
            "volume": spec["volume"],
            "postprocess": spec["postprocess"],
            "status": probe["status"],
            "request_id": probe.get("request_id"),
            "request_debug": probe.get("request_debug", {}),
            "raw_audio_path": str(raw_audio_path) if raw_audio_path.exists() else None,
            "processed_audio_path": None,
            "blocked_reason": probe.get("blocked_reason", ""),
            "error_message": probe.get("error_message", ""),
            "failure_reason": probe.get("failure_reason", ""),
        }
        if probe["status"] == STATUS_SUCCESS and raw_audio_path.exists():
            postprocess_audio(ffmpeg, raw_audio_path, processed_audio_path, spec["postprocess"])
            candidate_result["processed_audio_path"] = str(processed_audio_path)
        (candidate_dir / "candidate_result.json").write_text(
            json.dumps(candidate_result, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        results.append(candidate_result)

    selected = rank_successes(results)
    report = build_report(results, selected, probe_text)
    REPORT_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    LISTEN_SHEET_PATH.write_text(build_listen_sheet(results, selected, probe_text), encoding="utf-8")

    if selected is None:
        BLOCKED_SENTINEL_PATH.write_text(
            json.dumps(
                {
                    "status": "blocked",
                    "report_status": "已确认",
                    "generated_candidates": [],
                    "blocked_reason": [item.get("blocked_reason") or item.get("error_message") for item in results],
                    "note": "当前目录未产出成功候选；保留各候选子目录与失败结果。",
                },
                ensure_ascii=False,
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
    elif BLOCKED_SENTINEL_PATH.exists():
        BLOCKED_SENTINEL_PATH.unlink()

    print(json.dumps({"report": str(REPORT_PATH), "selected": selected}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
