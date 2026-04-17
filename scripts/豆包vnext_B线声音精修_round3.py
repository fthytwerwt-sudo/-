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
VOICE_CANDIDATES_DIR = OUTPUT_DIR / "voice_candidates_round3"
VOICE_BUNDLE_DIR = OUTPUT_DIR / "voice_ab_review_bundle_round3"
PROBE_COPY_PATH = VOICE_CANDIDATES_DIR / "probe_copy_round3.txt"
REPORT_PATH = OUTPUT_DIR / "voice_route_report.json"
LISTEN_SHEET_PATH = OUTPUT_DIR / "voice_listen_sheet.md"

PROBE_TEXT = (
    "豆包给你出的方案，\n"
    "你有没有觉得——\n\n"
    "能看，但用不了？\n\n"
    "最后你还是自己重写了一遍？\n\n"
    "这不是豆包的问题。\n\n"
    "是你问的方式，\n"
    "就决定了它\n"
    "只能给你那种结果。"
)

POSTPROCESS_C1_C2 = (
    "highpass=f=80,"
    "lowpass=f=12000,"
    "deesser=i=0.4:m=0.5:f=0.5:s=o,"
    "acompressor=threshold=-18dB:ratio=2:attack=50:release=150:makeup=2,"
    "loudnorm=I=-16:TP=-1.5:LRA=9"
)

POSTPROCESS_C3 = (
    "highpass=f=80,"
    "lowpass=f=12000,"
    "deesser=i=0.4:m=0.5:f=0.5:s=o,"
    "acompressor=threshold=-18dB:ratio=2:attack=50:release=150:makeup=3,"
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
            "candidate_id": "C1",
            "model": "qwen3-tts-instruct-flash-realtime",
            "voice": "Serena",
            "instruction": (
                "说话像一个熟悉这件事的人，在随口告诉朋友一个发现。"
                "语气词（就、其实、然后、还是、但、先、再、所以）要轻，"
                "不要停顿在这些词上，直接滑到后面的实词。"
                "每一句话只有一个重心，重心词稍微稳一点，其他的都轻一点。"
                "不要每个词都一样重，不要字字分明，要有轻重。"
            ),
            "speech_rate": 1.03,
            "pitch_rate": 0.97,
            "volume": 50,
            "postprocess": POSTPROCESS_C1_C2,
            "goal": "主要解决：功能词 / 语气词抬高感",
        },
        {
            "candidate_id": "C2",
            "model": "qwen3-tts-instruct-flash-realtime",
            "voice": "Serena",
            "instruction": (
                "说话节奏不要匀速，要有快区和慢区。"
                "铺垫的部分、功能词的部分，快一点，带过去。"
                "关键判断的部分，稍慢，稍稳，但不是加重，是让人觉得这是真的。"
                "句子和句子之间，不要机械停顿，有时候自然连过去，有时候真的停一下。"
                "停顿要落在语义转折前，不要落在每个标点后。"
                "整体感觉是：这个人知道自己在说什么，所以不用刻意表现。"
            ),
            "speech_rate": 1.05,
            "pitch_rate": 0.97,
            "volume": 50,
            "postprocess": POSTPROCESS_C1_C2,
            "goal": "主要解决：句内快慢层次 / 停顿分布不像真人",
        },
        {
            "candidate_id": "C3",
            "model": "qwen3-tts-instruct-flash-realtime",
            "voice": "Serena",
            "instruction": (
                "你在用语音给一个朋友发一段语音消息，内容是你刚发现的一个东西。"
                "不是在表演，不是在教学，是在分享一个真实的发现。"
                "语速不是均匀的：知道的部分说得快，想让对方想想的部分稍微慢下来。"
                "情绪不用表演，但要在场。"
                "“在场”的意思是：你说这句话的时候你是真的觉得这是真的，不是在念稿。"
                "音调不要高，但不能死平，要有轻微的起伏，来自真实的语气，不是表演的语气。"
            ),
            "speech_rate": 1.04,
            "pitch_rate": 0.98,
            "volume": 52,
            "postprocess": POSTPROCESS_C3,
            "goal": "主要解决：情绪微调不对 / 验证 pitch_rate 0.97 是否压过头",
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
        ("C2", "01_暂定第一名_C2.wav"),
        ("C1", "02_备选_C1.wav"),
        ("C3", "03_淘汰_C3.wav"),
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
                "# 阿里 Round 3 三候选试听说明",
                "",
                "## 当前分类",
                "",
                "1. `暂定第一名`：`C2`",
                "2. `备选`：`C1`",
                "3. `淘汰`：`C3`",
                "",
                "## 连续试听文件",
                "",
                "- `00_三候选顺序连听.wav`",
                "",
                "## 当前未完成的事",
                "",
                "- 四项核心维度仍缺人工听审：",
                "  - `功能词是否还被抬高`",
                "  - `停顿是否还落在每个标点后`",
                "  - `句内快慢层次是否更像真人`",
                "  - `情绪是否更在场`",
                "",
            ]
        ),
        encoding="utf-8",
    )


def write_listen_sheet(results: list[dict[str, Any]]) -> None:
    lines = [
        "# 阿里内部声音候选听审单",
        "",
        "## Round 3 probe 文案",
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
            "- `功能词是否还被抬高`：听“就 / 还是 / 但 / 先 / 再 / 所以”是不是仍然被读得太重。",
            "- `停顿是否还落在每个标点后`：听停顿是不是机械卡在逗号句号，而不是落在语义转折前。",
            "- `句内快慢层次是否更像真人`：听铺垫部分是否更顺滑带过，关键判断是否更稳。",
            "- `情绪是否更在场`：听它像不像一个真的在分享发现的人，而不是在念稿。",
            "",
            "## 当前分类",
            "",
            "- `暂定第一名`：`C2`",
            "- `备选`：`C1`",
            "- `淘汰`：`C3`",
            "",
            "## 当前结论",
            "",
            "- `推测` 当前轮暂定第一名：`C2`。",
            "- `推测` 当前轮备选：`C1`。",
            "- `推测` 当前轮淘汰：`C3`。",
            "- `待验证` 上述结论仍需人工听审，不得直接写成最终过线。",
            "",
            "## Round 3 AB review bundle",
            "",
            f"- `{VOICE_BUNDLE_DIR / '01_暂定第一名_C2.wav'}`",
            f"- `{VOICE_BUNDLE_DIR / '02_备选_C1.wav'}`",
            f"- `{VOICE_BUNDLE_DIR / '03_淘汰_C3.wav'}`",
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
                "schema_version": "video_factory_voice_route_report/v4",
                "task_object": "《豆包的正确打开方式》vNext",
                "lane": "B线｜声音线（阿里体系内先排尽）",
                "round": "round3",
                "status": "candidate_ranked",
                "report_status": "已确认",
                "provider_scope": "aliyun_only",
                "probe_copy_path": str(PROBE_COPY_PATH),
                "probe_text": PROBE_TEXT,
                "results": results,
                "selected_route": {
                    "status": "暂定第一名",
                    "candidate_id": "C2",
                    "model": "qwen3-tts-instruct-flash-realtime",
                    "voice": "Serena",
                    "reason": "更直接处理当前最核心问题：句内快慢层次与停顿分布不像真人。"
                },
                "backup_route": {
                    "status": "备选",
                    "candidate_id": "C1",
                    "model": "qwen3-tts-instruct-flash-realtime",
                    "voice": "Serena",
                    "reason": "更偏功能词抬高修正，可作为备选。"
                },
                "rejected_route": {
                    "status": "淘汰",
                    "candidate_id": "C3",
                    "model": "qwen3-tts-instruct-flash-realtime",
                    "voice": "Serena",
                    "reason": "当前主要承担情绪与 pitch 微调对照，不作为这轮主导路线。"
                },
                "voice_ab_review_bundle_round3": {
                    "path": str(VOICE_BUNDLE_DIR),
                    "files": [
                        str(VOICE_BUNDLE_DIR / "00_三候选顺序连听.wav"),
                        str(VOICE_BUNDLE_DIR / "01_暂定第一名_C2.wav"),
                        str(VOICE_BUNDLE_DIR / "02_备选_C1.wav"),
                        str(VOICE_BUNDLE_DIR / "03_淘汰_C3.wav"),
                        str(VOICE_BUNDLE_DIR / "试听说明.md"),
                    ],
                },
                "dimension_status": {
                    "功能词是否还被抬高": "待人工听审",
                    "停顿是否还落在每个标点后": "待人工听审",
                    "句内快慢层次是否更像真人": "待人工听审",
                    "情绪是否更在场": "待人工听审",
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
