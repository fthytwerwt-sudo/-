from __future__ import annotations

import pathlib

from 工作台_workbench_utils import parser_with_force, print_result, write_workspace_from_brief


def build_parser():
    parser = parser_with_force(
        "从 01_场景简报.md 生成 02_工作包正文.md、03_Prompt包.md、04_录制计划.md、05_回审清单.md。"
    )
    parser.add_argument("--brief", type=pathlib.Path, required=True)
    parser.add_argument("--workspace", type=pathlib.Path, required=True)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    result = write_workspace_from_brief(
        brief_path=args.brief,
        workspace=args.workspace,
        force=args.force,
    )
    print_result(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
