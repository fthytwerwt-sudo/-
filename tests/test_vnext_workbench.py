import pathlib
import subprocess
import sys
import tempfile
import textwrap
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
PYTHON = sys.executable


def _run_script(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [PYTHON, *args],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=True,
    )


class VnextWorkbenchTests(unittest.TestCase):
    def _write_brief(self, workspace: pathlib.Path) -> pathlib.Path:
        brief = workspace / "01_场景简报.md"
        brief.write_text(
            textwrap.dedent(
                """\
                # 样板_营销方案初稿_vnext

                ## 场景名称
                营销方案初稿 vNext

                ## 用户一句糊话
                老板要我下午给一版能直接改的营销方案初稿。

                ## 目标用户
                想用 AI 压出更像可交付物初稿的职场用户。

                ## 失败现场
                只有一句模糊需求，AI 输出看起来很长，但没有目标、边界和动作顺序。

                ## 交付目标
                生成可直接改写的工作包正文、三层 prompt 包、4 段核心录制计划与回审清单。

                ## 当前默认工作包
                场景化专业输出工作包

                ## 开头人物壳
                Minecraft-inspired 原创体素方块风

                ## 结尾总结壳
                Minecraft-inspired 原创体素方块风

                ## Prompt 引用尾卡要引用什么
                主 prompt 的 3 个判断点和修结果 prompt 的 2 个补强动作。

                ## 4段核心录制素材
                1. 原始糊话输入
                2. 主 prompt 执行过程
                3. 修结果 prompt 补强动作
                4. 前后差值与总结收束
                """
            ),
            encoding="utf-8",
        )
        return brief

    def test_generate_workbench_creates_core_outputs_from_brief(self) -> None:
        with tempfile.TemporaryDirectory(prefix="vnext_workbench_") as temp_dir:
            workspace = pathlib.Path(temp_dir)
            brief = self._write_brief(workspace)

            _run_script(
                str(ROOT / "scripts" / "生成工作包_workbench.py"),
                "--brief",
                str(brief),
                "--workspace",
                str(workspace),
                "--force",
            )

            expected_files = [
                workspace / "02_工作包正文.md",
                workspace / "03_Prompt包.md",
                workspace / "04_录制计划.md",
                workspace / "05_回审清单.md",
            ]
            for path in expected_files:
                self.assertTrue(path.exists(), f"missing generated file: {path}")

            prompt_pack = (workspace / "03_Prompt包.md").read_text(encoding="utf-8")
            self.assertIn("第1层：主 prompt", prompt_pack)
            self.assertIn("第2层：修结果 prompt", prompt_pack)
            self.assertIn("第3层：展示与尾卡 prompt", prompt_pack)
            self.assertIn("Prompt 引用尾卡", prompt_pack)

            work_package = (workspace / "02_工作包正文.md").read_text(encoding="utf-8")
            self.assertIn("Minecraft-inspired 原创体素方块风", work_package)

            recording_plan = (workspace / "04_录制计划.md").read_text(encoding="utf-8")
            self.assertIn("4 段核心录制素材", recording_plan)
            self.assertIn("原始糊话输入", recording_plan)

    def test_generate_recording_plan_can_rebuild_plan_file(self) -> None:
        with tempfile.TemporaryDirectory(prefix="vnext_recording_") as temp_dir:
            workspace = pathlib.Path(temp_dir)
            brief = self._write_brief(workspace)

            _run_script(
                str(ROOT / "scripts" / "生成工作包_workbench.py"),
                "--brief",
                str(brief),
                "--workspace",
                str(workspace),
                "--force",
            )
            (workspace / "04_录制计划.md").unlink()

            _run_script(
                str(ROOT / "scripts" / "生成录制计划_workbench.py"),
                "--workspace",
                str(workspace),
                "--force",
            )

            recording_plan = workspace / "04_录制计划.md"
            self.assertTrue(recording_plan.exists())
            self.assertIn("核心素材 1", recording_plan.read_text(encoding="utf-8"))

    def test_result_diff_and_log_writer_create_auxiliary_outputs(self) -> None:
        with tempfile.TemporaryDirectory(prefix="vnext_aux_") as temp_dir:
            workspace = pathlib.Path(temp_dir)
            brief = self._write_brief(workspace)

            _run_script(
                str(ROOT / "scripts" / "生成工作包_workbench.py"),
                "--brief",
                str(brief),
                "--workspace",
                str(workspace),
                "--force",
            )
            _run_script(
                str(ROOT / "scripts" / "结果差对比_workbench.py"),
                "--workspace",
                str(workspace),
                "--force",
            )
            _run_script(
                str(ROOT / "scripts" / "写回日志_workbench.py"),
                "--workspace",
                str(workspace),
                "--output",
                str(workspace / "工作台执行日志.md"),
                "--force",
            )

            diff_file = workspace / "06_结果差对比.md"
            self.assertTrue(diff_file.exists())
            diff_text = diff_file.read_text(encoding="utf-8")
            self.assertIn("普通输入", diff_text)
            self.assertIn("工作包输入", diff_text)

            log_file = workspace / "工作台执行日志.md"
            self.assertTrue(log_file.exists())
            log_text = log_file.read_text(encoding="utf-8")
            self.assertIn("technical_validation", log_text)
            self.assertIn("content_validation", log_text)


if __name__ == "__main__":
    unittest.main()
