from __future__ import annotations

import argparse
import json
import pathlib
import sys


ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from formal_hybrid_master import (  # noqa: E402
    HYBRID_CASE_PATH,
    HYBRID_OUTPUT_DIR,
    render_formal_hybrid_master,
)
from formal_api_demo_core import (  # noqa: E402
    DEFAULT_FORMAL_LOCAL_CONFIG_PATH,
    FORMAL_EXAMPLE_CONFIG_PATH,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="生成 30 秒 hybrid 正式母版：真人承载 + 结构证据 + 本地 final.mp4。"
    )
    parser.add_argument("--input", type=pathlib.Path, default=HYBRID_CASE_PATH)
    parser.add_argument("--example-config", type=pathlib.Path, default=FORMAL_EXAMPLE_CONFIG_PATH)
    parser.add_argument("--local-config", type=pathlib.Path, default=DEFAULT_FORMAL_LOCAL_CONFIG_PATH)
    parser.add_argument("--out", type=pathlib.Path, default=HYBRID_OUTPUT_DIR)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    result = render_formal_hybrid_master(
        input_path=args.input,
        example_config_path=args.example_config,
        local_config_path=args.local_config,
        output_dir=args.out,
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
