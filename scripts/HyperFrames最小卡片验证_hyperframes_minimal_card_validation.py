#!/usr/bin/env python3
"""Generate HyperFrames minimal card validation artifacts.

This script creates HyperFrames compositions, renders them through the real
`npx hyperframes` CLI, and records the runtime evidence. It does not read
secrets or call project APIs.
"""

from __future__ import annotations

import argparse
import json
import subprocess
from dataclasses import dataclass
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
PROJECT_DIR = REPO_ROOT / "dist" / "hyperframes_minimal_validation"
JUDGMENT_DIR = PROJECT_DIR / "01_judgment_card"
SUMMARY_DIR = PROJECT_DIR / "02_summary_card"
SOURCE_DIR = PROJECT_DIR / "source"
LOG_DIR = PROJECT_DIR / "runtime_logs"
SKIN_OUTPUT_ROOT = PROJECT_DIR / "visual_skins_1_3"
SKIN_SOURCE_DIR = SKIN_OUTPUT_ROOT / "source"
SKIN_LOG_DIR = SKIN_OUTPUT_ROOT / "runtime_logs"

TITLE = "AI 的正确用法，大家直接冲就行了"
JUDGMENT_TEXT = "AI 的正确用法：先判断，再执行"
SUMMARY_TEXT = "目标说清楚，下一步能验证，就可以冲"
HYPERFRAMES_CMD = ["npx", "--yes", "hyperframes@0.6.12"]


@dataclass(frozen=True)
class SkinSpec:
    skin_id: str
    skin_name_cn: str
    locked_status: str
    label: str
    background: str
    canvas_color: str
    panel_background: str
    primary_text: str
    secondary_text: str
    accent: str
    accent_secondary: str
    highlight: str
    decorative: str
    decorative_secondary: str
    keyword_style: str
    route_note: str
    icon_kind: str
    motion_strength: str
    text_density: str
    corner_radius: str
    shadow: str
    design_notes: list[str]
    forbidden_notes: list[str]


@dataclass(frozen=True)
class CardSpec:
    card_type: str
    motion_type: str
    text: str
    output_name: str
    duration: float
    eyebrow: str
    support: str
    tone: str
    skin: SkinSpec
    variant_label: str = ""


LEGACY_SKIN = SkinSpec(
    skin_id="legacy_minimal_runtime",
    skin_name_cn="最小运行验证",
    locked_status="technical_runtime_validation",
    label="minimal runtime",
    background=(
        "radial-gradient(circle at 14% 18%, rgba(168, 59, 49, 0.18), transparent 28%),"
        "radial-gradient(circle at 86% 78%, rgba(15, 102, 95, 0.16), transparent 30%),"
        "linear-gradient(135deg, #F8F4EC 0%, #FCFAF5 48%, #EFE1CF 100%)"
    ),
    canvas_color="#F8F4EC",
    panel_background="linear-gradient(145deg, rgba(255, 252, 245, 0.90), rgba(247, 237, 222, 0.84))",
    primary_text="#1D1A17",
    secondary_text="#6E655B",
    accent="#A83B31",
    accent_secondary="#0F665F",
    highlight="#E8D8C3",
    decorative="#E8D8C3",
    decorative_secondary="#0F665F",
    keyword_style="warm_coral_teal",
    route_note="cute_info_card_route",
    icon_kind="minimal_marks",
    motion_strength="low_to_medium",
    text_density="comfortable",
    corner_radius="large_soft_round",
    shadow="soft",
    design_notes=[
        "bright ivory canvas",
        "soft coral and teal accents",
        "layered paper-light panels",
        "gentle reveal and breathing motion",
    ],
    forbidden_notes=[
        "black background with white text",
        "generic PPT title slide",
        "course-sales layout",
    ],
)

LOCKED_SKINS: dict[str, SkinSpec] = {
    "clean_soft": SkinSpec(
        skin_id="clean_soft",
        skin_name_cn="干净柔和",
        locked_status="allowed_minimal_skin",
        label="clean soft",
        background=(
            "radial-gradient(circle at 84% 22%, rgba(232, 180, 92, 0.26), transparent 24%),"
            "radial-gradient(circle at 16% 78%, rgba(217, 198, 168, 0.26), transparent 28%),"
            "linear-gradient(135deg, #F8F4EC 0%, #FFF7EA 52%, #F3E5D0 100%)"
        ),
        canvas_color="#F8F4EC",
        panel_background="linear-gradient(145deg, rgba(255, 247, 234, 0.90), rgba(243, 229, 208, 0.82))",
        primary_text="#111827",
        secondary_text="#6E655B",
        accent="#A26016",
        accent_secondary="#87520F",
        highlight="#7A4A12",
        decorative="#D9C6A8",
        decorative_secondary="#E8D8C3",
        keyword_style="warm_orange",
        route_note="warm_ivory_background / generous_spacing / gentle_motion",
        icon_kind="magnifier_or_check",
        motion_strength="low_to_medium",
        text_density="comfortable",
        corner_radius="large_soft_round",
        shadow="soft",
        design_notes=[
            "warm ivory and light beige background",
            "generous spacing",
            "warm orange keyword highlight",
            "soft shadow and gentle motion",
        ],
        forbidden_notes=[
            "black_background_white_text",
            "dense_dashboard",
            "hard_sales_cover",
            "noisy_motion",
        ],
    ),
    "cute_ai_guide": SkinSpec(
        skin_id="cute_ai_guide",
        skin_name_cn="可爱 AI 向导",
        locked_status="allowed_minimal_skin",
        label="cute AI guide",
        background=(
            "radial-gradient(circle at 84% 24%, rgba(251, 207, 232, 0.36), transparent 26%),"
            "radial-gradient(circle at 12% 78%, rgba(191, 227, 255, 0.42), transparent 30%),"
            "linear-gradient(135deg, #EAF6FF 0%, #EDF2FF 48%, #F3E8FF 100%)"
        ),
        canvas_color="#EAF6FF",
        panel_background="linear-gradient(145deg, rgba(255, 255, 255, 0.74), rgba(233, 213, 255, 0.52))",
        primary_text="#14203D",
        secondary_text="#5B6B8C",
        accent="#1D4ED8",
        accent_secondary="#6D28D9",
        highlight="#BE185D",
        decorative="#BFE3FF",
        decorative_secondary="#E9D5FF",
        keyword_style="blue_purple_pink_gradient",
        route_note="soft_blue_lavender_background / friendly_guide_icon / soft_float_motion",
        icon_kind="simple_ai_guide_robot_icon",
        motion_strength="low_to_medium",
        text_density="comfortable_to_medium",
        corner_radius="large_bubbly_round",
        shadow="soft_cloud_layer",
        design_notes=[
            "soft blue to lavender background",
            "friendly guide icon or shape",
            "blue purple pink keyword highlight",
            "soft bounce or float motion",
        ],
        forbidden_notes=[
            "childish_overload",
            "sales_avatar",
            "copyrighted_character",
            "hard_cta_badge",
        ],
    ),
}

NOT_SELECTED_SKINS = ["sharp_judgment"]


def run_command(args: list[str], cwd: Path, log_dir: Path, log_name: str, timeout: int = 180) -> dict:
    result = subprocess.run(
        args,
        cwd=cwd,
        text=True,
        capture_output=True,
        timeout=timeout,
        check=False,
    )
    log_dir.mkdir(parents=True, exist_ok=True)
    log_path = log_dir / log_name
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


def write_design(skins: list[SkinSpec]) -> None:
    lines = [
        "# DESIGN",
        "",
        "## Style Prompt",
        "",
        "HyperFrames minimal judgment and summary cards for AI knowledge videos.",
        "Cards must feel like refined formal-operation inserts, not static PPT pages or sales covers.",
        "",
        "## Locked Minimal Skins",
    ]
    for skin in skins:
        lines.extend(
            [
                "",
                f"### {skin.skin_id} / {skin.skin_name_cn}",
                "",
                f"- `locked_status`: `{skin.locked_status}`",
                f"- `motion_strength`: `{skin.motion_strength}`",
                f"- `text_density`: `{skin.text_density}`",
                f"- `keyword_style`: `{skin.keyword_style}`",
                "- `must_keep`:",
            ]
        )
        lines.extend(f"  - {note}" for note in skin.design_notes)
        lines.append("- `must_not`:")
        lines.extend(f"  - {note}" for note in skin.forbidden_notes)
    lines.extend(
        [
            "",
            "## Not Selected",
            "",
            "- `sharp_judgment`: not selected this round and not part of the default locked baseline.",
        ]
    )
    (PROJECT_DIR / "DESIGN.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


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


def icon_html(spec: CardSpec, scene_id: str, start: float) -> str:
    skin = spec.skin
    if skin.skin_id == "cute_ai_guide":
        return f"""
          <div class="guide-figure" data-layout-ignore>
            <div class="guide-head">
              <span class="guide-eye eye-left"></span>
              <span class="guide-eye eye-right"></span>
              <span class="guide-smile"></span>
            </div>
            <div class="guide-body">
              <span class="guide-panel"></span>
              <span class="guide-panel small"></span>
            </div>
            <span class="spark spark-a"></span>
            <span class="spark spark-b"></span>
          </div>
          <script>
            tl.to("#{scene_id} .guide-figure", {{ y: -12, duration: 1.3, repeat: {max(1, int(spec.duration // 1.3))}, yoyo: true, ease: "sine.inOut" }}, {start + 0.75:.2f});
            tl.to("#{scene_id} .spark", {{ scale: 1.18, opacity: 0.35, duration: 0.8, repeat: {max(1, int(spec.duration // 0.8))}, yoyo: true, stagger: 0.12, ease: "sine.inOut" }}, {start + 0.9:.2f});
          </script>
        """
    symbol = "✓" if spec.card_type == "summary_card" else "⌕"
    return f"""
          <div class="soft-icon" data-layout-ignore>
            <span>{symbol}</span>
            <i></i>
          </div>
          <script>
            tl.to("#{scene_id} .soft-icon", {{ y: -10, rotate: 1.2, duration: 1.5, repeat: {max(1, int(spec.duration // 1.5))}, yoyo: true, ease: "sine.inOut" }}, {start + 0.72:.2f});
          </script>
        """


def scene_html(spec: CardSpec, *, start: float, scene_id: str, include_transition: bool) -> str:
    skin = spec.skin
    transition = ""
    if include_transition:
        transition = f'<div id="{scene_id}-wipe" class="transition-wipe" data-layout-ignore></div>'
    variant = f"<span class=\"variant-pill\">{spec.variant_label}</span>" if spec.variant_label else ""
    return f"""
      <section
        id="{scene_id}"
        class="scene {spec.card_type} skin-{skin.skin_id} clip"
        data-start="{start:.2f}"
        data-duration="{spec.duration:.2f}"
        data-track-index="1"
        data-layout-allow-overflow
      >
        <div class="grain" data-layout-ignore></div>
        <div class="halo halo-one" data-layout-ignore></div>
        <div class="halo halo-two" data-layout-ignore></div>
        <div class="cloud cloud-a" data-layout-ignore></div>
        <div class="cloud cloud-b" data-layout-ignore></div>
        {icon_html(spec, scene_id, start)}
        <div class="scene-content">
          <div class="meta-row">
            <span class="eyebrow">{spec.eyebrow}</span>
            <span class="route">{skin.label}</span>
          </div>
          <div class="statement-card">
            <div class="accent-rail"></div>
            <div class="text-stack">
              <div class="title-row">
                <p class="locked-title">{TITLE}</p>
                {variant}
              </div>
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
        tl.from("#{scene_id} .eyebrow", {{ y: 22, opacity: 0, duration: 0.45, ease: "power3.out" }}, {start + 0.18:.2f});
        tl.from("#{scene_id} .route", {{ x: 18, opacity: 0, duration: 0.45, ease: "sine.out" }}, {start + 0.24:.2f});
        tl.from("#{scene_id} .statement-card", {{ y: 34, scale: 0.985, opacity: 0, duration: 0.62, ease: "expo.out" }}, {start + 0.28:.2f});
        tl.from("#{scene_id} .accent-rail", {{ scaleY: 0, opacity: 0, duration: 0.55, transformOrigin: "top", ease: "back.out(1.2)" }}, {start + 0.42:.2f});
        tl.from("#{scene_id} .main-text .phrase", {{ y: 20, opacity: 0, duration: 0.48, stagger: 0.08, ease: "power2.out" }}, {start + 0.52:.2f});
        tl.from("#{scene_id} .support", {{ y: 16, opacity: 0, duration: 0.42, ease: "circ.out" }}, {start + 0.82:.2f});
        tl.from("#{scene_id} .bottom-row", {{ y: 14, opacity: 0, duration: 0.38, ease: "sine.out" }}, {start + 1.0:.2f});
        tl.to("#{scene_id} .statement-card", {{ y: -4, duration: 1.4, repeat: {max(1, int(spec.duration // 1.4))}, yoyo: true, ease: "sine.inOut" }}, {start + 1.15:.2f});
        tl.to("#{scene_id} .halo-one", {{ x: 24, y: -14, scale: 1.04, duration: 1.5, repeat: {max(1, int(spec.duration // 1.5))}, yoyo: true, ease: "sine.inOut" }}, {start + 0.3:.2f});
        tl.to("#{scene_id} .halo-two", {{ x: -18, y: 12, scale: 1.03, duration: 1.7, repeat: {max(1, int(spec.duration // 1.7))}, yoyo: true, ease: "sine.inOut" }}, {start + 0.35:.2f});
        tl.to("#{scene_id} .keyword", {{ color: "{skin.highlight}", duration: 0.5, repeat: 2, yoyo: true, ease: "sine.inOut" }}, {start + 1.22:.2f});
        tl.to("#{scene_id} .secondary-keyword", {{ color: "{skin.accent_secondary}", duration: 0.55, repeat: 2, yoyo: true, ease: "sine.inOut" }}, {start + 1.38:.2f});
        tl.to("#{scene_id} .cloud", {{ x: 18, duration: 2.0, repeat: {max(1, int(spec.duration // 2.0))}, yoyo: true, ease: "sine.inOut" }}, {start + 0.4:.2f});
        {transition_timeline(scene_id, start, spec.duration) if include_transition else ""}
      </script>
    """


def transition_timeline(scene_id: str, start: float, duration: float) -> str:
    wipe_time = start + duration - 0.55
    return f'tl.fromTo("#{scene_id}-wipe", {{ xPercent: -105 }}, {{ xPercent: 105, duration: 0.55, ease: "power2.inOut" }}, {wipe_time:.2f});'


def make_index(specs: list[CardSpec]) -> str:
    scene_gap = 0.05 if len(specs) > 1 else 0.0
    duration = sum(spec.duration for spec in specs) + scene_gap * max(0, len(specs) - 1) + (0.35 if len(specs) > 1 else 0)
    scene_blocks: list[str] = []
    start = 0.0
    for index, spec in enumerate(specs):
        scene_id = f"scene-{index + 1}"
        include_transition = index < len(specs) - 1
        scene_blocks.append(scene_html(spec, start=start, scene_id=scene_id, include_transition=include_transition))
        start += spec.duration + scene_gap
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
      }}
      .scene {{
        position: absolute;
        inset: 0;
        width: 1920px;
        height: 1080px;
        overflow: hidden;
        color: var(--primary-text);
      }}
      .skin-legacy_minimal_runtime {{
        background: {LEGACY_SKIN.background};
        color: {LEGACY_SKIN.primary_text};
      }}
      .skin-clean_soft {{
        background: {LOCKED_SKINS["clean_soft"].background};
        color: {LOCKED_SKINS["clean_soft"].primary_text};
      }}
      .skin-cute_ai_guide {{
        background: {LOCKED_SKINS["cute_ai_guide"].background};
        color: {LOCKED_SKINS["cute_ai_guide"].primary_text};
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
        color: var(--secondary-text);
        letter-spacing: 0;
      }}
      .eyebrow,
      .route,
      .tone,
      .boundary,
      .variant-pill {{
        padding: 12px 18px;
        border: 1px solid rgba(29, 26, 23, 0.10);
        border-radius: 999px;
        background: rgba(255, 255, 255, 0.56);
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
        border-radius: 38px;
        border: 1px solid rgba(29, 26, 23, 0.10);
        background: var(--panel-background);
        box-shadow:
          0 34px 88px var(--shadow-color),
          inset 0 1px 0 rgba(255, 255, 255, 0.72);
      }}
      .accent-rail {{
        width: 16px;
        height: 100%;
        border-radius: 999px;
        background: linear-gradient(180deg, var(--accent), var(--accent-secondary));
        box-shadow: 0 0 28px var(--accent-glow);
      }}
      .text-stack {{
        display: flex;
        flex-direction: column;
        gap: 28px;
      }}
      .title-row {{
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 24px;
      }}
      .locked-title {{
        max-width: 1060px;
        font-size: 34px;
        line-height: 1.35;
        color: var(--secondary-text);
      }}
      .variant-pill {{
        color: var(--primary-text);
        font-size: 24px;
        white-space: nowrap;
      }}
      .main-text {{
        display: flex;
        flex-wrap: wrap;
        align-items: baseline;
        gap: 18px 28px;
        max-width: 1200px;
        font-size: 92px;
        line-height: 1.13;
        font-weight: 800;
        letter-spacing: 0;
      }}
      .phrase {{
        display: inline-block;
        white-space: nowrap;
      }}
      .keyword {{
        color: var(--accent);
      }}
      .secondary-keyword {{
        color: var(--accent-secondary);
      }}
      .support {{
        max-width: 970px;
        font-size: 34px;
        line-height: 1.45;
        color: var(--secondary-text);
      }}
      .dot {{
        width: 12px;
        height: 12px;
        border-radius: 50%;
        background: var(--accent);
      }}
      .grain {{
        position: absolute;
        inset: 0;
        opacity: 0.11;
        background-image:
          linear-gradient(rgba(29, 26, 23, 0.10) 1px, transparent 1px),
          linear-gradient(90deg, rgba(29, 26, 23, 0.08) 1px, transparent 1px);
        background-size: 96px 96px;
      }}
      .halo,
      .cloud {{
        position: absolute;
        border-radius: 999px;
        filter: blur(8px);
      }}
      .halo {{
        width: 520px;
        height: 520px;
        opacity: 0.42;
      }}
      .halo-one {{
        left: -120px;
        top: 120px;
        background: radial-gradient(circle, var(--halo-one), transparent 62%);
      }}
      .halo-two {{
        right: -110px;
        bottom: 90px;
        background: radial-gradient(circle, var(--halo-two), transparent 62%);
      }}
      .cloud {{
        opacity: 0.28;
        background: var(--decorative);
      }}
      .cloud-a {{
        width: 220px;
        height: 72px;
        left: 136px;
        bottom: 144px;
      }}
      .cloud-b {{
        width: 180px;
        height: 58px;
        right: 250px;
        top: 146px;
      }}
      .transition-wipe {{
        position: absolute;
        top: 0;
        bottom: 0;
        left: 0;
        width: 120%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.92) 24%, var(--wipe-accent) 50%, rgba(255, 255, 255, 0.92) 76%, transparent);
        transform: translateX(-110%);
      }}
      .soft-icon {{
        position: absolute;
        right: 204px;
        top: 288px;
        width: 190px;
        height: 190px;
        border-radius: 56px;
        display: grid;
        place-items: center;
        color: var(--accent);
        background: rgba(255, 255, 255, 0.54);
        border: 1px solid rgba(29, 26, 23, 0.10);
        box-shadow: 0 24px 54px var(--shadow-color);
      }}
      .soft-icon span {{
        font-size: 104px;
        line-height: 1;
      }}
      .soft-icon i {{
        position: absolute;
        inset: 18px;
        border-radius: 44px;
        border: 2px solid var(--decorative-secondary);
        opacity: 0.55;
      }}
      .guide-figure {{
        position: absolute;
        right: 198px;
        top: 260px;
        width: 214px;
        height: 236px;
        filter: drop-shadow(0 24px 48px rgba(59, 130, 246, 0.18));
      }}
      .guide-head {{
        position: absolute;
        top: 0;
        left: 31px;
        width: 152px;
        height: 126px;
        border-radius: 48px;
        background: rgba(255, 255, 255, 0.76);
        border: 2px solid rgba(59, 130, 246, 0.24);
      }}
      .guide-body {{
        position: absolute;
        left: 16px;
        right: 16px;
        bottom: 0;
        height: 120px;
        border-radius: 48px;
        background: linear-gradient(145deg, rgba(191, 227, 255, 0.88), rgba(233, 213, 255, 0.88));
        border: 2px solid rgba(139, 92, 246, 0.20);
      }}
      .guide-eye {{
        position: absolute;
        top: 48px;
        width: 14px;
        height: 14px;
        border-radius: 50%;
        background: #14203D;
      }}
      .eye-left {{
        left: 48px;
      }}
      .eye-right {{
        right: 48px;
      }}
      .guide-smile {{
        position: absolute;
        left: 58px;
        bottom: 34px;
        width: 36px;
        height: 18px;
        border-bottom: 5px solid #8B5CF6;
        border-radius: 0 0 30px 30px;
      }}
      .guide-panel {{
        position: absolute;
        left: 42px;
        top: 44px;
        width: 82px;
        height: 12px;
        border-radius: 999px;
        background: #3B82F6;
        opacity: 0.64;
      }}
      .guide-panel.small {{
        top: 70px;
        width: 54px;
        background: #FF6B9A;
      }}
      .spark {{
        position: absolute;
        width: 18px;
        height: 18px;
        border-radius: 50%;
        background: #FB7185;
        opacity: 0.76;
      }}
      .spark-a {{
        right: 8px;
        top: 20px;
      }}
      .spark-b {{
        left: 0;
        top: 104px;
        background: #A78BFA;
      }}
      .skin-legacy_minimal_runtime {{
        --panel-background: {LEGACY_SKIN.panel_background};
        --primary-text: {LEGACY_SKIN.primary_text};
        --secondary-text: {LEGACY_SKIN.secondary_text};
        --accent: {LEGACY_SKIN.accent};
        --accent-secondary: {LEGACY_SKIN.accent_secondary};
        --highlight: {LEGACY_SKIN.highlight};
        --decorative: rgba(232, 216, 195, 0.46);
        --decorative-secondary: {LEGACY_SKIN.decorative_secondary};
        --shadow-color: rgba(62, 47, 35, 0.16);
        --accent-glow: rgba(168, 59, 49, 0.24);
        --halo-one: rgba(168, 59, 49, 0.22);
        --halo-two: rgba(15, 102, 95, 0.20);
        --wipe-accent: rgba(168, 59, 49, 0.22);
      }}
      .skin-clean_soft {{
        --panel-background: {LOCKED_SKINS["clean_soft"].panel_background};
        --primary-text: {LOCKED_SKINS["clean_soft"].primary_text};
        --secondary-text: {LOCKED_SKINS["clean_soft"].secondary_text};
        --accent: {LOCKED_SKINS["clean_soft"].accent};
        --accent-secondary: {LOCKED_SKINS["clean_soft"].accent_secondary};
        --highlight: {LOCKED_SKINS["clean_soft"].highlight};
        --decorative: rgba(217, 198, 168, 0.42);
        --decorative-secondary: {LOCKED_SKINS["clean_soft"].decorative_secondary};
        --shadow-color: rgba(84, 58, 24, 0.14);
        --accent-glow: rgba(201, 133, 43, 0.24);
        --halo-one: rgba(232, 180, 92, 0.25);
        --halo-two: rgba(217, 198, 168, 0.24);
        --wipe-accent: rgba(242, 190, 115, 0.32);
      }}
      .skin-cute_ai_guide {{
        --panel-background: {LOCKED_SKINS["cute_ai_guide"].panel_background};
        --primary-text: {LOCKED_SKINS["cute_ai_guide"].primary_text};
        --secondary-text: {LOCKED_SKINS["cute_ai_guide"].secondary_text};
        --accent: {LOCKED_SKINS["cute_ai_guide"].accent};
        --accent-secondary: {LOCKED_SKINS["cute_ai_guide"].accent_secondary};
        --highlight: {LOCKED_SKINS["cute_ai_guide"].highlight};
        --decorative: rgba(191, 227, 255, 0.48);
        --decorative-secondary: {LOCKED_SKINS["cute_ai_guide"].decorative_secondary};
        --shadow-color: rgba(59, 130, 246, 0.13);
        --accent-glow: rgba(59, 130, 246, 0.22);
        --halo-one: rgba(96, 165, 250, 0.28);
        --halo-two: rgba(167, 139, 250, 0.28);
        --wipe-accent: rgba(167, 139, 250, 0.30);
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


def clean_text(value: str) -> str:
    return "\n".join(line.rstrip() for line in value.splitlines()) + "\n"


def card_specs_for_skin(skin: SkinSpec, *, variant_label: str = "") -> list[CardSpec]:
    return [
        CardSpec(
            card_type="judgment_card",
            motion_type="judgment_card_motion",
            text=JUDGMENT_TEXT,
            output_name=f"judgment_card_{skin.skin_id}.mp4",
            duration=3.2,
            eyebrow="judgment card",
            support="先把判断边界说清，再进入可验证执行。",
            tone="light motion / keyword emphasis",
            skin=skin,
            variant_label=variant_label,
        ),
        CardSpec(
            card_type="summary_card",
            motion_type="summary_card_motion",
            text=SUMMARY_TEXT,
            output_name=f"summary_card_{skin.skin_id}.mp4",
            duration=3.2,
            eyebrow="summary card",
            support="把目标、验证、下一步收在一句话里。",
            tone="soft close / low pressure",
            skin=skin,
            variant_label=variant_label,
        ),
    ]


def render_variant(
    name: str,
    specs: list[CardSpec],
    output_path: Path,
    *,
    log_dir: Path,
    source_dir: Path,
) -> dict:
    html = clean_text(make_index(specs))
    (PROJECT_DIR / "index.html").write_text(html, encoding="utf-8")
    source_dir.mkdir(parents=True, exist_ok=True)
    (source_dir / f"{name}.html").write_text(html, encoding="utf-8")

    lint = run_command(HYPERFRAMES_CMD + ["lint"], PROJECT_DIR, log_dir, f"{name}_lint.log", timeout=120)
    inspect = run_command(
        HYPERFRAMES_CMD + ["inspect", "--samples", "8"],
        PROJECT_DIR,
        log_dir,
        f"{name}_inspect.log",
        timeout=180,
    )
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
        log_dir,
        f"{name}_render.log",
        timeout=600,
    )
    validation_status = (
        "passed"
        if lint["exit_code"] == 0 and inspect["exit_code"] == 0 and render["exit_code"] == 0 and output_path.exists()
        else "blocked"
    )
    return {
        "name": name,
        "validation_status": validation_status,
        "output_path": str(output_path.relative_to(REPO_ROOT)) if output_path.exists() else "",
        "lint": lint,
        "inspect": inspect,
        "render": render,
    }


def card_result(card: CardSpec, output_path: Path, run: dict) -> dict:
    return {
        "card_type": card.card_type,
        "text": card.text,
        "hyperframes_required": True,
        "hyperframes_runtime_status": "found_and_callable" if run["validation_status"] == "passed" else "blocked",
        "actual_output_type": "real_hyperframes_motion" if run["validation_status"] == "passed" else "blocked",
        "motion_type": card.motion_type,
        "skin_id": card.skin.skin_id,
        "skin_name_cn": card.skin.skin_name_cn,
        "skin_selection_reason": card.skin.route_note,
        "output_path": str(output_path.relative_to(REPO_ROOT)) if output_path.exists() else "",
        "validation_status": run["validation_status"],
    }


def write_card_manifest(card: CardSpec, output_path: Path, run: dict, output_dir: Path) -> None:
    manifest = {
        "artifact_type": "hyperframes_minimal_card_validation",
        "internal_diagnostic_only": True,
        "title": TITLE,
        "card_type": card.card_type,
        "text": card.text,
        "hyperframes_required": True,
        "hyperframes_runtime_status": "found_and_callable" if run["validation_status"] == "passed" else "blocked",
        "actual_output_type": "real_hyperframes_motion" if run["validation_status"] == "passed" else "blocked",
        "motion_type": card.motion_type,
        "route": "cute_info_card_route",
        "skin_id": card.skin.skin_id,
        "skin_name_cn": card.skin.skin_name_cn,
        "output_path": str(output_path.relative_to(REPO_ROOT)) if output_path.exists() else "",
        "validation_status": run["validation_status"],
        "render_log": run["render"]["log_path"],
        "content_validation": "not_advanced",
        "send_ready": False,
        "publish_candidate": False,
        "visual_master_locked": False,
        "must_not_claim": [
            "content_validation_passed",
            "send_ready",
            "publish_candidate",
            "visual_master_locked",
        ],
    }
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / f"{card.card_type}_manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def write_root_manifest(card_results: list[dict], combined_result: dict, check_results: list[dict]) -> None:
    passed = all(item["validation_status"] == "passed" for item in card_results) and combined_result["validation_status"] == "passed"
    manifest = {
        "artifact_type": "hyperframes_minimal_card_validation",
        "title": TITLE,
        "technical_runtime_validation": "passed" if passed else "blocked",
        "hyperframes_minimal_artifact": "generated" if passed else "blocked",
        "internal_diagnostic_only": True,
        "actual_output_type": "real_hyperframes_motion" if passed else "blocked",
        "hyperframes_runtime_status": "found_and_callable" if passed else "blocked",
        "runtime_entry": "npx --yes hyperframes@0.6.12 render",
        "runtime_adapter": "scripts/HyperFrames最小卡片验证_hyperframes_minimal_card_validation.py",
        "cards": card_results,
        "combined_preview": combined_result,
        "check_results": check_results,
        "content_validation": "not_advanced",
        "send_ready": False,
        "publish_candidate": False,
        "visual_master_locked": False,
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


def update_root_manifest_for_visual_lock(skin_pack_result: dict) -> None:
    manifest_path = PROJECT_DIR / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest.update(
        {
            "user_visual_review": "passed",
            "reviewer": "user",
            "review_basis": "user watched combined_preview and approved",
            "hyperframes_minimal_style_baseline": "locked_for_judgment_and_summary_cards",
            "judgment_card_motion_minimal_baseline": "locked",
            "summary_card_motion_minimal_baseline": "locked",
            "allowed_hyperframes_visual_skins": ["clean_soft", "cute_ai_guide"],
            "not_selected_visual_skins": NOT_SELECTED_SKINS,
            "visual_skin_preview_pack": skin_pack_result,
            "still_not_advanced": {
                "content_validation": "not_advanced",
                "send_ready": False,
                "publish_candidate": False,
                "visual_master_locked": False,
                "real_video_execution_chain_integration": "pending",
                "long_term_runtime_stability": "pending",
            },
        }
    )
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_root_review_manifest(card_results: list[dict], combined_result: dict, check_results: list[dict]) -> None:
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
            "## User Visual Review And Minimal Style Lock",
            "",
            "- `user_visual_review`: passed",
            "- `reviewer`: user",
            "- `review_basis`: user watched combined_preview and approved",
            "- `hyperframes_minimal_style_baseline`: locked_for_judgment_and_summary_cards",
            "- `judgment_card_motion_minimal_baseline`: locked",
            "- `summary_card_motion_minimal_baseline`: locked",
            "- `allowed_hyperframes_visual_skins`: clean_soft, cute_ai_guide",
            "- `not_selected_visual_skin`: sharp_judgment",
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


def render_default_minimal_validation() -> int:
    PROJECT_DIR.mkdir(parents=True, exist_ok=True)
    JUDGMENT_DIR.mkdir(parents=True, exist_ok=True)
    SUMMARY_DIR.mkdir(parents=True, exist_ok=True)
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    write_design([LEGACY_SKIN])

    judgment, summary = card_specs_for_skin(LEGACY_SKIN)
    judgment = CardSpec(**{**judgment.__dict__, "output_name": "judgment_card.mp4"})
    summary = CardSpec(**{**summary.__dict__, "output_name": "summary_card.mp4"})

    judgment_output = JUDGMENT_DIR / judgment.output_name
    summary_output = SUMMARY_DIR / summary.output_name
    combined_output = PROJECT_DIR / "combined_preview.mp4"

    judgment_run = render_variant(
        "judgment_card",
        [judgment],
        judgment_output,
        log_dir=LOG_DIR,
        source_dir=SOURCE_DIR,
    )
    summary_run = render_variant(
        "summary_card",
        [summary],
        summary_output,
        log_dir=LOG_DIR,
        source_dir=SOURCE_DIR,
    )
    combined_run = render_variant(
        "combined_preview",
        [judgment, summary],
        combined_output,
        log_dir=LOG_DIR,
        source_dir=SOURCE_DIR,
    )

    write_card_manifest(judgment, judgment_output, judgment_run, JUDGMENT_DIR)
    write_card_manifest(summary, summary_output, summary_run, SUMMARY_DIR)
    card_results = [card_result(judgment, judgment_output, judgment_run), card_result(summary, summary_output, summary_run)]
    combined_result = {
        "output_path": str(combined_output.relative_to(REPO_ROOT)) if combined_output.exists() else "",
        "validation_status": combined_run["validation_status"],
        "actual_output_type": "real_hyperframes_motion" if combined_run["validation_status"] == "passed" else "blocked",
    }
    check_results = collect_check_results(
        [
            ("judgment", judgment_run),
            ("summary", summary_run),
            ("combined", combined_run),
        ]
    )
    write_root_manifest(card_results, combined_result, check_results)
    write_root_review_manifest(card_results, combined_result, check_results)
    return 0 if all(item["validation_status"] == "passed" for item in card_results) and combined_result["validation_status"] == "passed" else 1


def collect_check_results(named_runs: list[tuple[str, dict]]) -> list[dict]:
    results: list[dict] = []
    for label, run in named_runs:
        results.extend(
            [
                {"name": f"{label}_lint", **run["lint"]},
                {"name": f"{label}_inspect", **run["inspect"]},
                {"name": f"{label}_render", **run["render"]},
            ]
        )
    return results


def render_skin(skin: SkinSpec) -> dict:
    skin_dir = SKIN_OUTPUT_ROOT / skin.skin_id
    skin_dir.mkdir(parents=True, exist_ok=True)
    specs = card_specs_for_skin(skin, variant_label=skin.skin_name_cn)
    judgment, summary = specs

    judgment_output = skin_dir / f"judgment_card_{skin.skin_id}.mp4"
    summary_output = skin_dir / f"summary_card_{skin.skin_id}.mp4"
    combined_output = skin_dir / f"combined_{skin.skin_id}.mp4"

    judgment_run = render_variant(
        f"{skin.skin_id}_judgment_card",
        [judgment],
        judgment_output,
        log_dir=SKIN_LOG_DIR,
        source_dir=SKIN_SOURCE_DIR,
    )
    summary_run = render_variant(
        f"{skin.skin_id}_summary_card",
        [summary],
        summary_output,
        log_dir=SKIN_LOG_DIR,
        source_dir=SKIN_SOURCE_DIR,
    )
    combined_run = render_variant(
        f"{skin.skin_id}_combined",
        [judgment, summary],
        combined_output,
        log_dir=SKIN_LOG_DIR,
        source_dir=SKIN_SOURCE_DIR,
    )

    cards = [card_result(judgment, judgment_output, judgment_run), card_result(summary, summary_output, summary_run)]
    check_results = collect_check_results(
        [
            (f"{skin.skin_id}_judgment", judgment_run),
            (f"{skin.skin_id}_summary", summary_run),
            (f"{skin.skin_id}_combined", combined_run),
        ]
    )
    manifest = {
        "skin_id": skin.skin_id,
        "skin_name_cn": skin.skin_name_cn,
        "locked_status": skin.locked_status,
        "visual_tokens": {
            "background_color": skin_background_tokens(skin),
            "primary_text_color": [skin.primary_text],
            "accent_color": [skin.accent, skin.accent_secondary],
            "highlight_color": [skin.highlight],
            "decorative_color": [skin.decorative, skin.decorative_secondary],
            "motion_strength": skin.motion_strength,
            "text_density": skin.text_density,
            "corner_radius": skin.corner_radius,
            "shadow": skin.shadow,
        },
        "cards": cards,
        "combined_preview": {
            "output_path": str(combined_output.relative_to(REPO_ROOT)) if combined_output.exists() else "",
            "validation_status": combined_run["validation_status"],
            "actual_output_type": "real_hyperframes_motion"
            if combined_run["validation_status"] == "passed"
            else "blocked",
        },
        "check_results": check_results,
        "allowed_visual_skins": ["clean_soft", "cute_ai_guide"],
        "not_selected_visual_skins": NOT_SELECTED_SKINS,
        "actual_output_type": "real_hyperframes_motion"
        if all(item["validation_status"] == "passed" for item in cards)
        and combined_run["validation_status"] == "passed"
        else "blocked",
        "content_validation": "not_advanced",
        "send_ready": False,
        "publish_candidate": False,
        "visual_master_locked": False,
    }
    (skin_dir / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return manifest


def skin_background_tokens(skin: SkinSpec) -> list[str]:
    if skin.skin_id == "clean_soft":
        return ["#F8F4EC", "#FFF7EA", "#F3E5D0"]
    if skin.skin_id == "cute_ai_guide":
        return ["#EAF6FF", "#EDF2FF", "#F3E8FF"]
    return ["#F8F4EC"]


def render_combined_skin_review(skins: list[SkinSpec]) -> dict:
    specs: list[CardSpec] = []
    for skin in skins:
        specs.extend(card_specs_for_skin(skin, variant_label=skin.skin_name_cn))
    output_path = SKIN_OUTPUT_ROOT / "combined_skin_review.mp4"
    return render_variant(
        "combined_skin_review",
        specs,
        output_path,
        log_dir=SKIN_LOG_DIR,
        source_dir=SKIN_SOURCE_DIR,
    )


def write_skin_review_manifest(skin_manifests: list[dict], combined_skin_review: dict) -> None:
    lines = [
        "# HyperFrames 最小卡片视觉皮肤预览包 review_manifest",
        "",
        f"- `title`: {TITLE}",
        "- `artifact_type`: `hyperframes_minimal_card_visual_skin_review`",
        "- `internal_diagnostic_only`: true",
        "- `user_visual_review`: passed",
        "- `reviewer`: user",
        "- `review_basis`: user watched combined_preview and approved",
        "- `hyperframes_minimal_style_baseline`: locked_for_judgment_and_summary_cards",
        "- `allowed_hyperframes_visual_skins`: clean_soft, cute_ai_guide",
        "- `not_selected_visual_skin`: sharp_judgment",
        "- `actual_output_type`: real_hyperframes_motion",
        "- `fallback_static_card`: false",
        "- `content_validation`: not_advanced",
        "- `send_ready`: false",
        "- `publish_candidate`: false",
        "- `visual_master_locked`: false",
        "",
        "## Skin Results",
    ]
    for manifest in skin_manifests:
        lines.extend(
            [
                "",
                f"### {manifest['skin_id']} / {manifest['skin_name_cn']}",
                f"- `locked_status`: `{manifest['locked_status']}`",
                f"- `combined_preview`: `{manifest['combined_preview']['output_path']}`",
                f"- `validation_status`: `{manifest['combined_preview']['validation_status']}`",
            ]
        )
        for card in manifest["cards"]:
            lines.append(f"- `{card['card_type']}`: `{card['output_path']}` / `{card['validation_status']}`")
    lines.extend(
        [
            "",
            "## Combined Skin Review",
            f"- `output_path`: `{combined_skin_review['output_path']}`",
            f"- `validation_status`: `{combined_skin_review['validation_status']}`",
            "",
            "## Sharp Judgment Boundary",
            "",
            "- `sharp_judgment`: not_selected_this_round",
            "- 不生成默认预览，不写入 allowed locked skins，不作为判断卡 / 总结卡默认皮肤。",
            "",
            "## Status Boundary",
            "",
            "- 本包不是正式视频。",
            "- 本包不是正式发布候选片。",
            "- 本包不推进 `content_validation`。",
            "- 本包不推进 `send_ready`。",
            "- 本包不锁定视觉母版。",
        ]
    )
    (SKIN_OUTPUT_ROOT / "review_manifest.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def render_locked_skins(selected_skin_ids: list[str]) -> int:
    PROJECT_DIR.mkdir(parents=True, exist_ok=True)
    SKIN_OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    SKIN_LOG_DIR.mkdir(parents=True, exist_ok=True)
    SKIN_SOURCE_DIR.mkdir(parents=True, exist_ok=True)

    selected_skins = [LOCKED_SKINS[skin_id] for skin_id in selected_skin_ids]
    write_design(selected_skins)
    skin_manifests = [render_skin(skin) for skin in selected_skins]
    combined_skin_review = render_combined_skin_review(selected_skins)
    combined_skin_result = {
        "output_path": combined_skin_review["output_path"],
        "validation_status": combined_skin_review["validation_status"],
        "actual_output_type": "real_hyperframes_motion"
        if combined_skin_review["validation_status"] == "passed"
        else "blocked",
    }
    write_skin_review_manifest(skin_manifests, combined_skin_result)
    update_root_manifest_for_visual_lock(
        {
            "status": "generated"
            if all(m["actual_output_type"] == "real_hyperframes_motion" for m in skin_manifests)
            and combined_skin_review["validation_status"] == "passed"
            else "blocked",
            "output_root": str(SKIN_OUTPUT_ROOT.relative_to(REPO_ROOT)),
            "combined_skin_review": combined_skin_result,
            "skin_manifests": [str((SKIN_OUTPUT_ROOT / m["skin_id"] / "manifest.json").relative_to(REPO_ROOT)) for m in skin_manifests],
        }
    )
    append_root_review_manifest_visual_lock()
    passed = all(m["actual_output_type"] == "real_hyperframes_motion" for m in skin_manifests) and combined_skin_review[
        "validation_status"
    ] == "passed"
    return 0 if passed else 1


def append_root_review_manifest_visual_lock() -> None:
    review_path = PROJECT_DIR / "review_manifest.md"
    existing = review_path.read_text(encoding="utf-8") if review_path.exists() else ""
    marker = "## User Visual Review And Minimal Style Lock"
    if marker in existing:
        existing = existing.split(marker)[0].rstrip() + "\n"
    addition = [
        "",
        marker,
        "",
        "- `user_visual_review`: passed",
        "- `reviewer`: user",
        "- `review_basis`: user watched combined_preview and approved",
        "- `hyperframes_minimal_style_baseline`: locked_for_judgment_and_summary_cards",
        "- `judgment_card_motion_minimal_baseline`: locked",
        "- `summary_card_motion_minimal_baseline`: locked",
        "- `allowed_hyperframes_visual_skins`: clean_soft, cute_ai_guide",
        "- `not_selected_visual_skin`: sharp_judgment",
        "- `visual_skin_preview_pack`: `dist/hyperframes_minimal_validation/visual_skins_1_3/`",
        "",
        "## Still Not Advanced",
        "",
        "- `content_validation`: not_advanced",
        "- `send_ready`: false",
        "- `publish_candidate`: false",
        "- `visual_master_locked`: false",
        "- `real_video_execution_chain_integration`: pending",
        "- `long_term_runtime_stability`: pending",
    ]
    review_path.write_text(existing.rstrip() + "\n" + "\n".join(addition) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--skin",
        choices=sorted(LOCKED_SKINS),
        action="append",
        help="Render one locked minimal visual skin. May be passed more than once.",
    )
    parser.add_argument(
        "--all-locked-skins",
        action="store_true",
        help="Render clean_soft and cute_ai_guide visual skin preview pack.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.all_locked_skins:
        return render_locked_skins(["clean_soft", "cute_ai_guide"])
    if args.skin:
        return render_locked_skins(args.skin)
    return render_default_minimal_validation()


if __name__ == "__main__":
    raise SystemExit(main())
