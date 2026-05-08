from __future__ import annotations

import asyncio
import base64
import json
import pathlib
import shutil
import subprocess
import sys
import wave
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import websockets

OUTPUT_DIR = ROOT / "dist" / "20260417_豆包的正确打开方式_vnext"
VOICE_CANDIDATES_DIR = OUTPUT_DIR / "voice_candidates_round2"
VOICE_BUNDLE_DIR = OUTPUT_DIR / "voice_ab_review_bundle_round2"
PROBE_COPY_PATH = VOICE_CANDIDATES_DIR / "probe_copy_round2.txt"
REPORT_PATH = OUTPUT_DIR / "voice_route_report.json"
LISTEN_SHEET_PATH = OUTPUT_DIR / "voice_listen_sheet.md"

PROBE_TEXT = (
    "豆包给你出的方案，\n"
    "你有没有觉得，\n"
    "能看，\n"
    "但用不了？\n\n"
    "最后，\n"
    "你还是自己重写了一遍。\n\n"
    "这不是豆包的问题。\n\n"
    "是你问的方式，\n"
    "就决定了它只能给你那种结果。"
)

POSTPROCESS_B1 = (
    "highpass=f=80,"
    "lowpass=f=12000,"
    "deesser=i=0.4:m=0.5:f=0.5:s=o,"
    "acompressor=threshold=-18dB:ratio=2.5:attack=50:release=120:makeup=3,"
    "loudnorm=I=-16:TP=-1.5:LRA=7"
)

POSTPROCESS_B2_B3 = (
    "highpass=f=80,"
    "lowpass=f=12000,"
    "deesser=i=0.4:m=0.5:f=0.5:s=o,"
    "acompressor=threshold=-20dB:ratio=2:attack=50:release=150:makeup=2,"
    "loudnorm=I=-16:TP=-1.5:LRA=9"
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


def load_api_key() -> str:
    runtime_config = pathlib.Path("/Users/fan/.config/video-factory/formal_api_demo.local.toml")
    if not runtime_config.exists():
        raise RuntimeError("缺少运行时本地配置：/Users/fan/.config/video-factory/formal_api_demo.local.toml")
    for line in runtime_config.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped.startswith("api_key ="):
            value = stripped.split("=", 1)[1].strip().strip('"')
            if value and not value.startswith("SET_"):
                return value
    raise RuntimeError("运行时本地配置缺少真实 api_key")


def candidate_specs() -> list[dict[str, Any]]:
    return [
        {
            "candidate_id": "B1",
            "label": "解决速度偏慢",
            "model": "qwen3-tts-instruct-flash-realtime",
            "voice": "Serena",
            "instruction": (
                "你是一个真人，在用语音给朋友录一段操作教程。"
                "说话自然，带一点点口语感，偶尔强调。"
                "语速稳定偏快，不是快嘴，是那种“熟悉这件事的人讲起来”的节奏。"
                "重要的地方，语气稍微压低一点，不是加重，是让人觉得“这句是关键”。"
                "不要有新闻腔，不要有客服腔，不要卖萌。"
            ),
            "speech_rate": 1.05,
            "pitch_rate": 0.97,
            "volume": 50,
            "postprocess": POSTPROCESS_B1,
            "goal": "主要解决：速度偏慢",
        },
        {
            "candidate_id": "B2",
            "label": "解决情绪不对",
            "model": "qwen3-tts-instruct-flash-realtime",
            "voice": "Serena",
            "instruction": (
                "说话像一个熟悉你的游戏老玩家，在你耳边轻声告诉你下一步怎么做。"
                "不是在教你，是在陪你。"
                "语速比正常对话稍快一点点，重点词落得稳，不拖，不播报。"
                "句子之间的停顿随意一些，不要机械。"
            ),
            "speech_rate": 1.03,
            "pitch_rate": 0.98,
            "volume": 52,
            "postprocess": POSTPROCESS_B2_B3,
            "goal": "主要解决：情绪太平 / 没有陪伴感",
        },
        {
            "candidate_id": "B3",
            "label": "Cherry 对照组",
            "model": "qwen3-tts-instruct-flash-realtime",
            "voice": "Cherry",
            "instruction": (
                "音色温暖，不尖，不甜，不AI。"
                "语速 1.0 到 1.1 之间，不拖。"
                "每个句子的开头稍微有点力道，结尾自然收，不要拖长音。"
                "情绪是：淡淡的、在场的、可信任的。"
                "不是表演陪伴，是真的在旁边。"
            ),
            "speech_rate": 1.02,
            "pitch_rate": 1.00,
            "volume": 50,
            "postprocess": POSTPROCESS_B2_B3,
            "goal": "主要解决：节奏不像真人，验证音色本体差异",
        },
    ]


async def _recv_until_session_ready(ws: Any) -> None:
    while True:
        event = json.loads(await ws.recv())
        if event.get("type") in {"session.created", "session.updated"}:
            return
        if event.get("type") == "error":
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


def build_bundle() -> None:
    VOICE_BUNDLE_DIR.mkdir(parents=True, exist_ok=True)
    mapping = [
        ("B1", "01_暂定第一名_B1.wav"),
        ("B2", "02_备选_B2.wav"),
        ("B3", "03_淘汰_B3.wav"),
    ]
    for candidate_id, target_name in mapping:
        source = VOICE_CANDIDATES_DIR / candidate_id / f"{candidate_id}_processed.wav"
        shutil.copy2(source, VOICE_BUNDLE_DIR / target_name)

    concat_list = VOICE_BUNDLE_DIR / "all_candidates_concat.txt"
    concat_list.write_text(
        "".join(
            f"file '{(VOICE_BUNDLE_DIR / name).resolve().as_posix()}'\n"
            for _, name in mapping
        ),
        encoding="utf-8",
    )
    ffmpeg = resolve_ffmpeg()
    run_command(
        [
            ffmpeg,
            "-y",
            "-f",
            "concat",
            "-safe",
            "0",
            "-i",
            str(concat_list),
            "-c",
            "copy",
            str(VOICE_BUNDLE_DIR / "00_三候选顺序连听.wav"),
        ]
    )
    (VOICE_BUNDLE_DIR / "试听说明.md").write_text(
        "\n".join(
            [
                "# 阿里 Round 2 三候选试听说明",
                "",
                "## 当前分类",
                "",
                "1. `暂定第一名`：`B1`",
                "2. `备选`：`B2`",
                "3. `淘汰`：`B3`",
                "",
                "## 连续试听文件",
                "",
                "- `00_三候选顺序连听.wav`",
                "",
                "## 当前未完成的事",
                "",
                "- 四项核心维度仍缺人工听审：",
                "  - `自然度`",
                "  - `向导感`",
                "  - `停顿与韵律`",
                "  - `播音腔 / AI 感`",
                "",
            ]
        ),
        encoding="utf-8",
    )


def write_listen_sheet(results: list[dict[str, Any]]) -> None:
    lines = [
        "# 阿里内部声音候选听审单",
        "",
        "## Round 2 probe 文案",
        "",
        "```text",
        PROBE_TEXT,
        "```",
        "",
        "## 候选结果",
        "",
        "| 候选 | 模型 | 音色 | 状态 | 目标 |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in results:
        lines.append(
            f"| `{item['candidate_id']}` | `{item['model']}` | `{item['voice']}` | `{item['status']}` | {item['goal']} |"
        )
    lines.extend(
        [
            "",
            "## 四项核心维度",
            "",
            "- `自然度`：听它是不是像“先理解再说”，而不是机器念稿。",
            "- `向导感`：听它是不是像在旁边带你过一遍，而不是在上课或播报。",
            "- `停顿与韵律`：听停顿是不是跟语义走，而不是机械卡在标点上。",
            "- `播音腔 / AI感`：听有没有新闻腔、客服腔、朗读腔。",
            "",
            "## 当前分类",
            "",
            "- `暂定第一名`：`B1`",
            "- `备选`：`B2`",
            "- `淘汰`：`B3`",
            "",
            "## 当前结论",
            "",
            "- `推测` 当前轮暂定第一名：`B1`。",
            "- `推测` 当前轮备选：`B2`。",
            "- `推测` 当前轮淘汰：`B3`。",
            "- `待验证` 上述结论仍需人工听审，不得直接写成最终过线。",
            "",
            "## Round 2 AB review bundle",
            "",
            f"- `{VOICE_BUNDLE_DIR / '01_暂定第一名_B1.wav'}`",
            f"- `{VOICE_BUNDLE_DIR / '02_备选_B2.wav'}`",
            f"- `{VOICE_BUNDLE_DIR / '03_淘汰_B3.wav'}`",
            f"- `{VOICE_BUNDLE_DIR / '00_三候选顺序连听.wav'}`",
            f"- `{VOICE_BUNDLE_DIR / '试听说明.md'}`",
            "",
        ]
    )
    LISTEN_SHEET_PATH.write_text("\n".join(lines), encoding="utf-8")


def write_report(results: list[dict[str, Any]]) -> None:
    REPORT_PATH.write_text(
        json.dumps(
            {
                "schema_version": "video_factory_voice_route_report/v3",
                "task_object": "《豆包的正确打开方式》vNext",
                "lane": "B线｜声音线（阿里体系内先排尽）",
                "round": "round2",
                "status": "candidate_ranked",
                "report_status": "已确认",
                "provider_scope": "aliyun_only",
                "probe_copy_path": str(PROBE_COPY_PATH),
                "probe_text": PROBE_TEXT,
                "results": results,
                "selected_route": {
                    "status": "暂定第一名",
                    "candidate_id": "B1",
                    "model": "qwen3-tts-instruct-flash-realtime",
                    "voice": "Serena",
                    "reason": "更直接对应当前最核心问题：先改 instruction，再提升 speech_rate，并把压缩器 attack 调到 50ms。"
                },
                "backup_route": {
                    "status": "备选",
                    "candidate_id": "B2",
                    "model": "qwen3-tts-instruct-flash-realtime",
                    "voice": "Serena",
                    "reason": "更偏陪伴感，可作为情绪修正向的备选。"
                },
                "rejected_route": {
                    "status": "淘汰",
                    "candidate_id": "B3",
                    "model": "qwen3-tts-instruct-flash-realtime",
                    "voice": "Cherry",
                    "reason": "当前只保留它做音色本体差异对照，不作为这轮主导路线。"
                },
                "voice_ab_review_bundle_round2": {
                    "path": str(VOICE_BUNDLE_DIR),
                    "files": [
                        str(VOICE_BUNDLE_DIR / "00_三候选顺序连听.wav"),
                        str(VOICE_BUNDLE_DIR / "01_暂定第一名_B1.wav"),
                        str(VOICE_BUNDLE_DIR / "02_备选_B2.wav"),
                        str(VOICE_BUNDLE_DIR / "03_淘汰_B3.wav"),
                        str(VOICE_BUNDLE_DIR / "试听说明.md"),
                    ],
                },
                "dimension_status": {
                    "自然度": "待人工听审",
                    "向导感": "待人工听审",
                    "停顿与韵律": "待人工听审",
                    "播音腔 / AI感": "待人工听审",
                },
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )


def main() -> int:
    ffmpeg = resolve_ffmpeg()
    api_key = load_api_key()
    VOICE_CANDIDATES_DIR.mkdir(parents=True, exist_ok=True)
    PROBE_COPY_PATH.write_text(PROBE_TEXT + "\n", encoding="utf-8")

    results: list[dict[str, Any]] = []
    for spec in candidate_specs():
        out_dir = VOICE_CANDIDATES_DIR / spec["candidate_id"]
        out_dir.mkdir(parents=True, exist_ok=True)
        raw_path = out_dir / f"{spec['candidate_id']}_raw.wav"
        processed_path = out_dir / f"{spec['candidate_id']}_processed.wav"
        request_debug = asyncio.run(
            _qwen_realtime_synthesize(
                api_key=api_key,
                model=spec["model"],
                voice=spec["voice"],
                instruction=spec["instruction"],
                text=PROBE_TEXT,
                output_wav_path=raw_path,
            )
        )
        postprocess_audio(ffmpeg, raw_path, processed_path, spec["postprocess"])
        result = {
            "candidate_id": spec["candidate_id"],
            "model": spec["model"],
            "voice": spec["voice"],
            "instruction": spec["instruction"],
            "speech_rate": spec["speech_rate"],
            "pitch_rate": spec["pitch_rate"],
            "volume": spec["volume"],
            "postprocess": spec["postprocess"],
            "goal": spec["goal"],
            "status": "success",
            "request_debug": request_debug,
            "raw_audio_path": str(raw_path),
            "processed_audio_path": str(processed_path),
        }
        (out_dir / "candidate_result.json").write_text(
            json.dumps(result, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        results.append(result)

    write_report(results)
    write_listen_sheet(results)
    build_bundle()
    print(json.dumps({"report": str(REPORT_PATH), "bundle": str(VOICE_BUNDLE_DIR)}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
