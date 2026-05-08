from __future__ import annotations

import pathlib

from 工作台_workbench_utils import parser_with_force, print_result, rewrite_recording_plan


def build_parser():
    parser = parser_with_force("根据工作台目录中的 01_场景简报.md 重建 04_录制计划.md。")
    parser.add_argument("--workspace", type=pathlib.Path, required=True)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    result = rewrite_recording_plan(
        workspace=args.workspace,
        force=args.force,
    )
    print_result(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
