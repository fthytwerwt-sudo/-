#!/usr/bin/env python3
"""Check the local guided proof video toolchain without reading secrets."""

from __future__ import annotations

import importlib
import json
import os
import shutil
import subprocess
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
VALIDATION_DIR = ROOT / "dist" / "toolchain_validation"
STATUS_PATH = VALIDATION_DIR / "toolchain_status.json"

HOMEBREW_LIB = Path("/opt/homebrew/lib")
if HOMEBREW_LIB.exists():
    # System python3 on macOS may not search Homebrew dylib paths. CairoSVG
    # loads cairo during import, so the library path must be set first.
    os.environ.setdefault("DYLD_LIBRARY_PATH", str(HOMEBREW_LIB))


def run_command(args: list[str], timeout: int = 30) -> dict[str, Any]:
    try:
        completed = subprocess.run(
            args,
            cwd=ROOT,
            text=True,
            capture_output=True,
            timeout=timeout,
            check=False,
        )
        return {
            "ok": completed.returncode == 0,
            "returncode": completed.returncode,
            "stdout": completed.stdout.strip()[-2000:],
            "stderr": completed.stderr.strip()[-2000:],
        }
    except FileNotFoundError as exc:
        return {"ok": False, "returncode": None, "stdout": "", "stderr": str(exc)}
    except subprocess.TimeoutExpired as exc:
        return {
            "ok": False,
            "returncode": None,
            "stdout": (exc.stdout or "").strip()[-2000:],
            "stderr": f"timeout: {exc}",
        }


def import_status(module_name: str, label: str) -> dict[str, Any]:
    try:
        module = importlib.import_module(module_name)
        return {
            "label": label,
            "ok": True,
            "version": getattr(module, "__version__", "version_unknown"),
        }
    except Exception as exc:
        return {"label": label, "ok": False, "error": f"{exc.__class__.__name__}: {exc}"}


def load_package_json() -> dict[str, Any]:
    package_path = ROOT / "package.json"
    if not package_path.exists():
        return {}
    with package_path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def ffmpeg_ass_status() -> dict[str, Any]:
    filters = run_command(["ffmpeg", "-hide_banner", "-filters"])
    buildconf = run_command(["ffmpeg", "-hide_banner", "-buildconf"])
    filter_text = f"{filters.get('stdout', '')}\n{filters.get('stderr', '')}"
    build_text = f"{buildconf.get('stdout', '')}\n{buildconf.get('stderr', '')}"
    ass_filter = any(
        token in filter_text
        for token in (" ass ", "\n ass ", " subtitles ", "\n subtitles ")
    )
    libass = "libass" in build_text.lower()
    return {
      "ass_ready": bool(ass_filter and libass),
      "ass_or_subtitles_filter_found": bool(ass_filter),
      "libass_enabled": bool(libass),
      "ass_role": "fallback_only_not_primary",
      "remotion_caption_layer_primary": True,
    }


def main() -> int:
    VALIDATION_DIR.mkdir(parents=True, exist_ok=True)

    package_json = load_package_json()
    dependencies = package_json.get("dependencies", {})
    scripts = package_json.get("scripts", {})

    node = run_command(["node", "-v"])
    npm = run_command(["npm", "-v"])
    remotion_cli = run_command(["npx", "--no-install", "remotion", "versions"])
    ffmpeg = run_command(["ffmpeg", "-version"])
    ffprobe = run_command(["ffprobe", "-version"])
    ass = ffmpeg_ass_status()

    python_imports = {
        "cv2": import_status("cv2", "OpenCV"),
        "numpy": import_status("numpy", "numpy"),
        "pysubs2": import_status("pysubs2", "pysubs2"),
        "cairosvg": import_status("cairosvg", "CairoSVG"),
        "PIL": import_status("PIL", "Pillow"),
    }

    still_path = VALIDATION_DIR / "remotion_still.png"
    clip_path = VALIDATION_DIR / "remotion_5s.mp4"
    ffprobe_clip = (
        run_command([
            "ffprobe",
            "-v",
            "error",
            "-show_format",
            "-show_streams",
            str(clip_path),
        ])
        if clip_path.exists()
        else {"ok": False, "stderr": "missing remotion_5s.mp4"}
    )

    remotion_dependencies = [
        "react",
        "react-dom",
        "remotion",
        "@remotion/media",
        "@remotion/captions",
        "@remotion/renderer",
    ]
    deps_present = {name: name in dependencies for name in remotion_dependencies}
    python_visual_ready = all(item["ok"] for item in python_imports.values())
    remotion_ready = (
        node["ok"]
        and npm["ok"]
        and remotion_cli["ok"]
        and all(deps_present.values())
        and (ROOT / "remotion" / "index.tsx").exists()
    )
    ffmpeg_ready = bool(ffmpeg["ok"] and ffprobe["ok"])
    outputs_ready = bool(still_path.exists() and clip_path.exists() and ffprobe_clip["ok"])
    minimum_ready = bool(remotion_ready and ffmpeg_ready and python_visual_ready and outputs_ready)

    blocked_if = []
    if not node["ok"]:
        blocked_if.append("node_unavailable")
    if not npm["ok"]:
        blocked_if.append("npm_unavailable")
    if not remotion_cli["ok"]:
        blocked_if.append("remotion_cli_unavailable")
    if not all(deps_present.values()):
        blocked_if.append("remotion_dependencies_missing")
    if not still_path.exists():
        blocked_if.append("remotion_still_missing")
    if not clip_path.exists():
        blocked_if.append("remotion_5s_clip_missing")
    if not ffmpeg_ready:
        blocked_if.append("ffmpeg_or_ffprobe_unavailable")
    if not python_visual_ready:
        blocked_if.append("python_visual_import_failed")

    status = {
        "toolchain_status": {
            "remotion_ready": remotion_ready,
            "ffmpeg_ready": ffmpeg_ready,
            "ass_ready": ass["ass_ready"],
            "python_visual_ready": python_visual_ready,
            "minimum_guided_proof_ready": minimum_ready,
            "blocked_if": blocked_if,
        },
        "checks": {
            "node": node,
            "npm": npm,
            "package_json_exists": (ROOT / "package.json").exists(),
            "remotion_dependencies": deps_present,
            "remotion_cli": remotion_cli,
            "scripts": {
                "vf:remotion:still": "vf:remotion:still" in scripts,
                "vf:remotion:render5s": "vf:remotion:render5s" in scripts,
                "vf:toolchain:check": "vf:toolchain:check" in scripts,
            },
            "remotion_outputs": {
                "still": str(still_path.relative_to(ROOT)),
                "still_exists": still_path.exists(),
                "clip": str(clip_path.relative_to(ROOT)),
                "clip_exists": clip_path.exists(),
                "ffprobe_clip_ok": ffprobe_clip["ok"],
            },
            "ffmpeg": ffmpeg,
            "ffprobe": ffprobe,
            "ass": ass,
            "python_imports": python_imports,
            "python_runtime_paths": {
                "homebrew_lib": str(HOMEBREW_LIB),
                "homebrew_lib_exists": HOMEBREW_LIB.exists(),
                "dyld_library_path_set_for_self_check": os.environ.get("DYLD_LIBRARY_PATH") == str(HOMEBREW_LIB),
            },
            "validation_dir_exists": VALIDATION_DIR.exists(),
            "secret_policy": {
                "env_file_read": False,
                "secret_read": False,
                "external_api_called": False,
            },
        },
    }

    with STATUS_PATH.open("w", encoding="utf-8") as handle:
        json.dump(status, handle, ensure_ascii=False, indent=2)
        handle.write("\n")

    print("toolchain_status（工具链状态）:")
    for key, value in status["toolchain_status"].items():
        print(f"  {key}: {value}")
    print(f"  status_path: {STATUS_PATH.relative_to(ROOT)}")
    return 0 if minimum_ready else 2


if __name__ == "__main__":
    raise SystemExit(main())
