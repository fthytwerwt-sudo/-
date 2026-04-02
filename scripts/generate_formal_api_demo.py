from __future__ import annotations

import argparse
import json
import pathlib
import sys


ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from formal_api_demo_core import (  # noqa: E402
    DEFAULT_FORMAL_LOCAL_CONFIG_PATH,
    DEFAULT_FORMAL_OUTPUT_DIR,
    FORMAL_CASE_PATH,
    FORMAL_EXAMPLE_CONFIG_PATH,
    run_generation_pipeline,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="正式版 API 视频 demo 生成入口。当前正式主线要求 generation 同时包含配音 API 与图片/视频 API；若 visual provider 尚未真实接通，则 generation 必须诚实 blocked。visual plan / preview storyboard 仅是辅助产物，不代表 generation success。"
    )
    parser.add_argument("--input", type=pathlib.Path, default=FORMAL_CASE_PATH)
    parser.add_argument(
        "--example-config",
        type=pathlib.Path,
        default=FORMAL_EXAMPLE_CONFIG_PATH,
    )
    parser.add_argument(
        "--local-config",
        type=pathlib.Path,
        default=DEFAULT_FORMAL_LOCAL_CONFIG_PATH,
    )
    parser.add_argument("--out", type=pathlib.Path, default=DEFAULT_FORMAL_OUTPUT_DIR)
    parser.add_argument("--dry-run", action="store_true")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    result = run_generation_pipeline(
        input_path=args.input,
        example_config_path=args.example_config,
        local_config_path=args.local_config,
        output_dir=args.out,
        dry_run=args.dry_run,
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
