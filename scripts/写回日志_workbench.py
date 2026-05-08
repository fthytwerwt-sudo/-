from __future__ import annotations

import pathlib

from 工作台_workbench_utils import parser_with_force, print_result, write_execution_log


def build_parser():
    parser = parser_with_force("根据工作台目录写回最小执行日志骨架。")
    parser.add_argument("--workspace", type=pathlib.Path, required=True)
    parser.add_argument("--output", type=pathlib.Path, default=None)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    output_path = args.output or (args.workspace / "工作台执行日志.md")
    result = write_execution_log(
        workspace=args.workspace,
        output_path=output_path,
        force=args.force,
    )
    print_result(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
