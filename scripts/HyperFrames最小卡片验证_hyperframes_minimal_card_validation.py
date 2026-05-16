#!/usr/bin/env python3
"""Generate the minimal HyperFrames card validation artifacts.

This script creates one HyperFrames composition at a time, renders it through
the real `npx hyperframes` CLI, and records whether the run is a real runtime
validation or a blocked result. It does not read secrets or call project APIs.
"""

from __future__ import annotations

import json
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
PROJECT_DIR = REPO_ROOT / "dist" / "hyperframes_minimal_validation"
JUDGMENT_DIR = PROJECT_DIR / "01_judgment_card"
SUMMARY_DIR = PROJECT_DIR / "02_summary_card"
SOURCE_DIR = PROJECT_DIR / "source"
LOG_DIR = PROJECT_DIR / "runtime_logs"

TITLE = "AI 的正确用法，大家直接冲就行了"
JUDGMENT_TEXT = "AI 的正确用法：先判断，再执行"
SUMMARY_TEXT = "目标说清楚，下一步能验证，就可以冲"
HYPERFRAMES_CMD = ["npx", "--yes", "hyperframes@0.6.12"]


@dataclass(frozen=True)
class CardSpec:
    card_type: str
    motion_type: str
    text: str
    accent: str
    output_dir: Path
    output_name: str
    duration: float
    eyebrow: str
    support: str
    tone: str


def run_command(args: list[str], cwd: Path, log_name: str, timeout: int = 180) -> dict:
    result = subprocess.run(
        args,
        cwd=cwd,
        text=True,
        capture_output=True,
        timeout=timeout,
        check=False,
    )
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    log_path = LOG_DIR / log_name
    log_path.write_text(
        "\n".join(
            [
                "$ " + " ".join(args),
                "",
                "exit_code: " + str(result.returncode),
                "",
                "STDOUT:",
                result.stdout,
                "",
                "STDERR:",
                result.stderr,
            ]
        ),
        encoding="utf-8",
    )
    return {
        "command": args,
        "exit_code": result.returncode,
        "stdout": result.stdout,
        "stderr": result.stderr,
        "log_path": str(log_path.relative_to(REPO_ROOT)),
    }


def write_design() -> None:
    design = """# DESIGN

## Style Prompt

Warm editorial AI knowledge card style with a bright ivory canvas, ink-black
Chinese typography, soft coral and teal accents, layered paper-light panels,
subtle motion, and generous negative space. The card should feel like a refined
formal-operation insert, not a slide deck or a sales cover.

## Colors

- Canvas: #F8F4EC
- Ink: #1D1A17
- Muted ink: #6E655B
- Coral accent: #A83B31
- Teal accent: #0F665F
- Warm line: #E8D8C3

## Typography

- Primary: Arial, sans-serif
- Numeric / labels: Arial, sans-serif

## Motion Rules

- Light motion only: breathe, gentle reveal, keyword emphasis, small floating
  accent marks.
- Do not shake, bounce aggressively, flash, or crowd the evidence window.

## What NOT to Do

- Do not create a black background with white text.
- Do not make a generic PPT title slide.
- Do not use a course-sales layout or hard CTA.
- Do not add unsupported metrics, data claims, or platform results.
"""
    (PROJECT_DIR / "DESIGN.md").write_text(design, encoding="utf-8")


def scene_html(
    spec: CardSpec,
    *,
    start: float,
    scene_id: str,
    include_transition: bool,
) -> str:
    accent_secondary = "#0F665F" if spec.accent == "#A83B31" else "#A83B31"
    transition = ""
    if include_transition:
        transition = f"""
        <div id="{scene_id}-wipe" class="transition-wipe" data-layout-ignore></div>
        """
    return f"""
      <section
        id="{scene_id}"
        class="scene {spec.card_type} clip"
        data-start="{start:.2f}"
        data-duration="{spec.duration:.2f}"
        data-track-index="1"
        data-layout-allow-overflow
      >
        <div class="grain" data-layout-ignore></div>
        <div class="halo halo-one" data-layout-ignore></div>
        <div class="halo halo-two" data-layout-ignore></div>
        <div class="scene-content">
          <div class="meta-row">
            <span class="eyebrow">{spec.eyebrow}</span>
            <span class="route">cute_info_card_route</span>
          </div>
          <div class="statement-card">
            <div class="accent-rail"></div>
            <div class="text-stack">
              <p class="locked-title">{TITLE}</p>
              <h1 class="main-text" data-locked-text="{spec.text}">
                {format_locked_text(spec.text, spec.card_type)}
              </h1>
              <p class="support">{spec.support}</p>
            </div>
          </div>
          <div class="bottom-row">
            <span class="tone">{spec.tone}</span>
            <span class="dot"></span>
            <span class="boundary">internal_diagnostic_only</span>
          </div>
        </div>
        {transition}
      </section>
      <script>
        tl.from("#{scene_id} .eyebrow", {{ y: 22, opacity: 0, duration: 0.45, ease: "power3.out" }}, {start + 0.18});
        tl.from("#{scene_id} .route", {{ x: 18, opacity: 0, duration: 0.45, ease: "sine.out" }}, {start + 0.24});
        tl.from("#{scene_id} .statement-card", {{ y: 34, scale: 0.985, opacity: 0, duration: 0.62, ease: "expo.out" }}, {start + 0.28});
        tl.from("#{scene_id} .accent-rail", {{ scaleY: 0, opacity: 0, duration: 0.55, transformOrigin: "top", ease: "back.out(1.2)" }}, {start + 0.42});
        tl.from("#{scene_id} .main-text .phrase", {{ y: 20, opacity: 0, duration: 0.48, stagger: 0.08, ease: "power2.out" }}, {start + 0.52});
        tl.from("#{scene_id} .support", {{ y: 16, opacity: 0, duration: 0.42, ease: "circ.out" }}, {start + 0.82});
        tl.from("#{scene_id} .bottom-row", {{ y: 14, opacity: 0, duration: 0.38, ease: "sine.out" }}, {start + 1.0});
        tl.to("#{scene_id} .statement-card", {{ y: -4, duration: 1.4, repeat: {max(1, int(spec.duration // 1.4))}, yoyo: true, ease: "sine.inOut" }}, {start + 1.15});
        tl.to("#{scene_id} .halo-one", {{ x: 24, y: -14, scale: 1.04, duration: 1.5, repeat: {max(1, int(spec.duration // 1.5))}, yoyo: true, ease: "sine.inOut" }}, {start + 0.3});
        tl.to("#{scene_id} .halo-two", {{ x: -18, y: 12, scale: 1.03, duration: 1.7, repeat: {max(1, int(spec.duration // 1.7))}, yoyo: true, ease: "sine.inOut" }}, {start + 0.35});
        tl.to("#{scene_id} .keyword", {{ color: "{spec.accent}", duration: 0.5, repeat: 2, yoyo: true, ease: "sine.inOut" }}, {start + 1.22});
        tl.to("#{scene_id} .secondary-keyword", {{ color: "{accent_secondary}", duration: 0.55, repeat: 2, yoyo: true, ease: "sine.inOut" }}, {start + 1.38});
        {transition_timeline(scene_id, start, spec.duration) if include_transition else ""}
      </script>
    """


def transition_timeline(scene_id: str, start: float, duration: float) -> str:
    wipe_time = start + duration - 0.55
    return f"""
        tl.fromTo("#{scene_id}-wipe", {{ xPercent: -105 }}, {{ xPercent: 105, duration: 0.55, ease: "power2.inOut" }}, {wipe_time});
    """


def format_locked_text(text: str, card_type: str) -> str:
    if card_type == "judgment_card":
        return (
            '<span class="phrase">AI 的正确用法：</span>'
            '<span class="phrase keyword">先判断</span>'
            '<span class="phrase secondary-keyword">再执行</span>'
        )
    return (
        '<span class="phrase keyword">目标说清楚</span>'
        '<span class="phrase">下一步能验证</span>'
        '<span class="phrase secondary-keyword">就可以冲</span>'
    )


def make_index(specs: list[CardSpec]) -> str:
    duration = sum(spec.duration for spec in specs) + (0.35 if len(specs) > 1 else 0)
    scene_blocks: list[str] = []
    start = 0.0
    for index, spec in enumerate(specs):
        scene_id = f"scene-{index + 1}"
        include_transition = index < len(specs) - 1
        scene_blocks.append(scene_html(spec, start=start, scene_id=scene_id, include_transition=include_transition))
        start += spec.duration
    html = f"""<!doctype html>
<html lang="zh-CN" data-resolution="landscape">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1920, height=1080" />
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
    <style>
      * {{
        margin: 0;
        padding: 0;
        box-sizing: border-box;
      }}
      html,
      body {{
        width: 1920px;
        height: 1080px;
        overflow: hidden;
        background: #F8F4EC;
        color: #1D1A17;
        font-family: Arial, sans-serif;
      }}
      #root {{
        width: 1920px;
        height: 1080px;
        position: relative;
        overflow: hidden;
        background:
          radial-gradient(circle at 14% 18%, rgba(168, 59, 49, 0.18), transparent 28%),
          radial-gradient(circle at 86% 78%, rgba(15, 102, 95, 0.16), transparent 30%),
          linear-gradient(135deg, #F8F4EC 0%, #FCFAF5 48%, #EFE1CF 100%);
      }}
      .scene {{
        position: absolute;
        inset: 0;
        width: 1920px;
        height: 1080px;
        overflow: hidden;
      }}
      .scene-content {{
        width: 100%;
        height: 100%;
        padding: 118px 156px 112px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        gap: 34px;
      }}
      .meta-row,
      .bottom-row {{
        display: flex;
        align-items: center;
        justify-content: space-between;
        min-height: 52px;
        font-size: 26px;
        color: #6E655B;
        letter-spacing: 0;
      }}
      .eyebrow,
      .route,
      .tone,
      .boundary {{
        padding: 12px 18px;
        border: 1px solid rgba(29, 26, 23, 0.10);
        border-radius: 8px;
        background: rgba(255, 252, 245, 0.66);
        backdrop-filter: blur(12px);
      }}
      .statement-card {{
        position: relative;
        min-height: 570px;
        padding: 70px 82px;
        display: grid;
        grid-template-columns: 18px 1fr;
        gap: 42px;
        align-items: center;
        border-radius: 8px;
        border: 1px solid rgba(29, 26, 23, 0.12);
        background:
          linear-gradient(145deg, rgba(255, 252, 245, 0.90), rgba(247, 237, 222, 0.84)),
          repeating-linear-gradient(90deg, rgba(29, 26, 23, 0.035) 0 1px, transparent 1px 92px);
        box-shadow:
          0 34px 88px rgba(62, 47, 35, 0.16),
          inset 0 1px 0 rgba(255, 255, 255, 0.72);
      }}
      .accent-rail {{
        width: 16px;
        height: 100%;
        border-radius: 999px;
        background: linear-gradient(180deg, #A83B31, #0F665F);
        box-shadow: 0 0 28px rgba(168, 59, 49, 0.24);
      }}
      .text-stack {{
        display: flex;
        flex-direction: column;
        gap: 28px;
      }}
      .locked-title {{
        max-width: 1060px;
        font-size: 34px;
        line-height: 1.35;
        color: #6E655B;
      }}
      .main-text {{
        display: flex;
        flex-wrap: wrap;
        align-items: baseline;
        gap: 18px 28px;
        max-width: 1280px;
        font-size: 96px;
        line-height: 1.13;
        font-weight: 800;
        letter-spacing: 0;
      }}
      .phrase {{
        display: inline-block;
        white-space: nowrap;
      }}
      .support {{
        max-width: 970px;
        font-size: 34px;
        line-height: 1.45;
        color: #6E655B;
      }}
      .dot {{
        width: 12px;
        height: 12px;
        border-radius: 50%;
        background: #A83B31;
      }}
      .grain {{
        position: absolute;
        inset: 0;
        opacity: 0.13;
        background-image:
          linear-gradient(rgba(29, 26, 23, 0.12) 1px, transparent 1px),
          linear-gradient(90deg, rgba(29, 26, 23, 0.10) 1px, transparent 1px);
        background-size: 96px 96px;
      }}
      .halo {{
        position: absolute;
        width: 520px;
        height: 520px;
        border-radius: 50%;
        filter: blur(8px);
        opacity: 0.42;
      }}
      .halo-one {{
        left: -120px;
        top: 120px;
        background: radial-gradient(circle, rgba(168, 59, 49, 0.22), transparent 62%);
      }}
      .halo-two {{
        right: -110px;
        bottom: 90px;
        background: radial-gradient(circle, rgba(15, 102, 95, 0.20), transparent 62%);
      }}
      .transition-wipe {{
        position: absolute;
        top: 0;
        bottom: 0;
        left: 0;
        width: 120%;
        background: linear-gradient(90deg, transparent, rgba(248, 244, 236, 0.96) 24%, rgba(168, 59, 49, 0.22) 50%, rgba(248, 244, 236, 0.96) 76%, transparent);
        transform: translateX(-110%);
      }}
      .summary_card .accent-rail {{
        background: linear-gradient(180deg, #0F665F, #A83B31);
      }}
      .summary_card .dot {{
        background: #0F665F;
      }}
    </style>
  </head>
  <body>
    <main
      id="root"
      data-composition-id="main"
      data-start="0"
      data-duration="{duration:.2f}"
      data-width="1920"
      data-height="1080"
    >
      <script>
        window.__timelines = window.__timelines || {{}};
        const tl = gsap.timeline({{ paused: true }});
      </script>
      {''.join(scene_blocks)}
      <script>
        window.__timelines["main"] = tl;
      </script>
    </main>
  </body>
</html>
"""
    return html


def write_card_manifest(spec: CardSpec, output_path: Path, status: str, command_result: dict) -> None:
    manifest = {
        "artifact_type": "hyperframes_minimal_card_validation",
        "internal_diagnostic_only": True,
        "title": TITLE,
        "card_type": spec.card_type,
        "text": spec.text,
        "hyperframes_required": True,
        "hyperframes_runtime_status": "found_and_callable" if status == "passed" else "blocked",
        "actual_output_type": "real_hyperframes_motion" if status == "passed" else "blocked",
        "motion_type": spec.motion_type,
        "route": "cute_info_card_route",
        "output_path": str(output_path.relative_to(REPO_ROOT)) if output_path.exists() else "",
        "validation_status": status,
        "render_log": command_result["log_path"],
        "must_not_claim": [
            "content_validation_passed",
            "send_ready",
            "publish_candidate",
            "visual_master_locked",
        ],
    }
    (spec.output_dir / f"{spec.card_type}_manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def write_root_manifest(card_results: list[dict], combined_result: dict, check_results: list[dict]) -> None:
    manifest = {
        "artifact_type": "hyperframes_minimal_card_validation",
        "title": TITLE,
        "technical_runtime_validation": "passed"
        if all(item["validation_status"] == "passed" for item in card_results) and combined_result["validation_status"] == "passed"
        else "blocked",
        "hyperframes_minimal_artifact": "generated"
        if all(item["validation_status"] == "passed" for item in card_results) and combined_result["validation_status"] == "passed"
        else "blocked",
        "internal_diagnostic_only": True,
        "actual_output_type": "real_hyperframes_motion"
        if all(item["validation_status"] == "passed" for item in card_results) and combined_result["validation_status"] == "passed"
        else "blocked",
        "hyperframes_runtime_status": "found_and_callable"
        if all(item["validation_status"] == "passed" for item in card_results) and combined_result["validation_status"] == "passed"
        else "blocked",
        "runtime_entry": "npx --yes hyperframes@0.6.12 render",
        "runtime_adapter": str(Path("scripts/HyperFrames最小卡片验证_hyperframes_minimal_card_validation.py")),
        "cards": card_results,
        "combined_preview": combined_result,
        "check_results": check_results,
        "must_not_claim": [
            "content_validation_passed",
            "send_ready",
            "publish_candidate",
            "visual_master_locked",
        ],
    }
    (PROJECT_DIR / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def write_review_manifest(card_results: list[dict], combined_result: dict, check_results: list[dict]) -> None:
    status = (
        "passed"
        if all(item["validation_status"] == "passed" for item in card_results)
        and combined_result["validation_status"] == "passed"
        else "blocked"
    )
    lines = [
        "# HyperFrames 最小卡片验证 review_manifest",
        "",
        f"- `title`: {TITLE}",
        "- `artifact_type`: `hyperframes_minimal_card_validation`",
        "- `internal_diagnostic_only`: true",
        f"- `technical_runtime_validation`: `{status}`",
        f"- `hyperframes_runtime_status`: `{'found_and_callable' if status == 'passed' else 'blocked'}`",
        "- `runtime_entry`: `npx --yes hyperframes@0.6.12 render`",
        "- `fallback_static_card`: false",
        "- `content_validation`: not_advanced",
        "- `send_ready`: false",
        "- `publish_candidate`: false",
        "- `visual_master_locked`: false",
        "",
        "## Cards",
    ]
    for item in card_results:
        lines.extend(
            [
                "",
                f"### {item['card_type']}",
                f"- `text`: {item['text']}",
                f"- `motion_type`: {item['motion_type']}",
                f"- `output_path`: `{item['output_path']}`",
                f"- `validation_status`: `{item['validation_status']}`",
            ]
        )
    lines.extend(
        [
            "",
            "## Combined Preview",
            f"- `output_path`: `{combined_result['output_path']}`",
            f"- `validation_status`: `{combined_result['validation_status']}`",
            "",
            "## Runtime Checks",
        ]
    )
    for result in check_results:
        lines.append(f"- `{result['name']}`: exit_code={result['exit_code']}, log=`{result['log_path']}`")
    lines.extend(
        [
            "",
            "## Status Boundary",
            "",
            "- 本产物不是正式视频。",
            "- 本产物不是正式发布候选片。",
            "- 本产物不推进 `content_validation`。",
            "- 本产物不推进 `send_ready`。",
            "- 本产物不锁定视觉母版。",
        ]
    )
    (PROJECT_DIR / "review_manifest.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def render_variant(name: str, specs: list[CardSpec], output_path: Path) -> dict:
    html = clean_text(make_index(specs))
    (PROJECT_DIR / "index.html").write_text(html, encoding="utf-8")
    SOURCE_DIR.mkdir(parents=True, exist_ok=True)
    (SOURCE_DIR / f"{name}.html").write_text(html, encoding="utf-8")

    lint = run_command(HYPERFRAMES_CMD + ["lint"], PROJECT_DIR, f"{name}_lint.log", timeout=120)
    inspect = run_command(HYPERFRAMES_CMD + ["inspect", "--samples", "8"], PROJECT_DIR, f"{name}_inspect.log", timeout=180)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    render = run_command(
        HYPERFRAMES_CMD
        + [
            "render",
            "--output",
            str(output_path),
            "--quality",
            "draft",
            "--fps",
            "30",
            "--workers",
            "1",
        ],
        PROJECT_DIR,
        f"{name}_render.log",
        timeout=420,
    )
    validation_status = "passed" if lint["exit_code"] == 0 and inspect["exit_code"] == 0 and render["exit_code"] == 0 and output_path.exists() else "blocked"
    return {
        "name": name,
        "validation_status": validation_status,
        "output_path": str(output_path.relative_to(REPO_ROOT)) if output_path.exists() else "",
        "lint": lint,
        "inspect": inspect,
        "render": render,
    }


def clean_text(value: str) -> str:
    return "\n".join(line.rstrip() for line in value.splitlines()) + "\n"


def main() -> int:
    PROJECT_DIR.mkdir(parents=True, exist_ok=True)
    JUDGMENT_DIR.mkdir(parents=True, exist_ok=True)
    SUMMARY_DIR.mkdir(parents=True, exist_ok=True)
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    write_design()

    judgment = CardSpec(
        card_type="judgment_card",
        motion_type="judgment_card_motion",
        text=JUDGMENT_TEXT,
        accent="#A83B31",
        output_dir=JUDGMENT_DIR,
        output_name="judgment_card.mp4",
        duration=3.2,
        eyebrow="judgment card",
        support="先把判断边界说清，再进入可验证执行。",
        tone="light motion / keyword emphasis",
    )
    summary = CardSpec(
        card_type="summary_card",
        motion_type="summary_card_motion",
        text=SUMMARY_TEXT,
        accent="#0F665F",
        output_dir=SUMMARY_DIR,
        output_name="summary_card.mp4",
        duration=3.2,
        eyebrow="summary card",
        support="把目标、验证、下一步收在一句话里。",
        tone="soft close / low pressure",
    )

    judgment_output = JUDGMENT_DIR / judgment.output_name
    summary_output = SUMMARY_DIR / summary.output_name
    combined_output = PROJECT_DIR / "combined_preview.mp4"

    judgment_run = render_variant("judgment_card", [judgment], judgment_output)
    summary_run = render_variant("summary_card", [summary], summary_output)
    combined_run = render_variant("combined_preview", [judgment, summary], combined_output)

    write_card_manifest(judgment, judgment_output, judgment_run["validation_status"], judgment_run["render"])
    write_card_manifest(summary, summary_output, summary_run["validation_status"], summary_run["render"])

    card_results = [
        {
            "card_type": judgment.card_type,
            "text": judgment.text,
            "hyperframes_required": True,
            "hyperframes_runtime_status": "found_and_callable" if judgment_run["validation_status"] == "passed" else "blocked",
            "actual_output_type": "real_hyperframes_motion" if judgment_run["validation_status"] == "passed" else "blocked",
            "motion_type": judgment.motion_type,
            "output_path": str(judgment_output.relative_to(REPO_ROOT)) if judgment_output.exists() else "",
            "validation_status": judgment_run["validation_status"],
        },
        {
            "card_type": summary.card_type,
            "text": summary.text,
            "hyperframes_required": True,
            "hyperframes_runtime_status": "found_and_callable" if summary_run["validation_status"] == "passed" else "blocked",
            "actual_output_type": "real_hyperframes_motion" if summary_run["validation_status"] == "passed" else "blocked",
            "motion_type": summary.motion_type,
            "output_path": str(summary_output.relative_to(REPO_ROOT)) if summary_output.exists() else "",
            "validation_status": summary_run["validation_status"],
        },
    ]
    combined_result = {
        "output_path": str(combined_output.relative_to(REPO_ROOT)) if combined_output.exists() else "",
        "validation_status": combined_run["validation_status"],
        "actual_output_type": "real_hyperframes_motion" if combined_run["validation_status"] == "passed" else "blocked",
    }
    check_results = [
        {"name": "judgment_lint", **judgment_run["lint"]},
        {"name": "judgment_inspect", **judgment_run["inspect"]},
        {"name": "judgment_render", **judgment_run["render"]},
        {"name": "summary_lint", **summary_run["lint"]},
        {"name": "summary_inspect", **summary_run["inspect"]},
        {"name": "summary_render", **summary_run["render"]},
        {"name": "combined_lint", **combined_run["lint"]},
        {"name": "combined_inspect", **combined_run["inspect"]},
        {"name": "combined_render", **combined_run["render"]},
    ]
    write_root_manifest(card_results, combined_result, check_results)
    write_review_manifest(card_results, combined_result, check_results)
    return 0 if all(item["validation_status"] == "passed" for item in card_results) and combined_result["validation_status"] == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
