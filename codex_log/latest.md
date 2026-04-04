# Latest

## 当前主结论

- 2026-04-05 已把纯 PPT / 信息卡主线的 assembly 默认路径正式升级为：
  - `OSS + 云剪 = 默认主路径`
  - `local assembly = fallback / 兜底路径`
- 这次升级当前只适用于纯 PPT / 信息卡母版主线，不自动扩到动态 PPT 或数字人主线。
- 当前仍明确：
  - 数字人 / 真人口播分支继续并行修，但不阻塞纯 PPT 主线
  - 当前暂不考虑动态 PPT
  - 云剪第一轮仍只服务转场统一、字幕安全区、模板化 assembly、片头 / 正文 / 结尾模板化
  - 不是复杂 motion design / 高成本视觉特效路线

## 本轮关键执行事实

- 本轮同时更新了执行层口径、项目脑口径、组装脚本说明、示例配置和 assembly 状态语义。
- 旧口径中“local default / cloud optional”的位置，已经在以下文件中改口：
  - `formal_api_demo_core.py`
  - `scripts/assemble_formal_api_demo.py`
  - `config/formal_api_demo.example.toml`
  - `tests/test_formal_api_demo_pipeline.py`
  - `project_source/01_project_system_prompt.md`
  - `project_source/00_project_brief.md`
  - `project_source/06_project_index.md`
  - `project_source/08_quality_baseline_and_90_score_rules.md`
  - `project_source/10_formal_api_demo_current_route_patch_20260402.md`
  - `codex_source/02_current_execution_context.md`
  - `codex_source/03_research_findings_bridge.md`
  - `codex_log/latest.md`
- 本轮新增完整执行日志：
  - `codex_log/20260405_ppt_cloud_first_assembly_route.md`
- 当前新的默认执行口径已收口为：
  - 纯 PPT / 信息卡主线默认走 `OSS + 云剪` 组装
  - 本地 assembly 只在云剪失败、模板异常、上传异常或任务超时时兜底
  - 仓库不再把本地 mp4 写成默认主交付语义

## 本轮实际改动（仓库内）

- 更新项目脑口径：
  - `project_source/00_project_brief.md`
  - `project_source/01_project_system_prompt.md`
  - `project_source/06_project_index.md`
  - `project_source/08_quality_baseline_and_90_score_rules.md`
  - `project_source/10_formal_api_demo_current_route_patch_20260402.md`
- 更新执行层当前上下文：
  - `codex_source/02_current_execution_context.md`
  - `codex_source/03_research_findings_bridge.md`
- 更新代码与配置口径：
  - `formal_api_demo_core.py`
  - `scripts/assemble_formal_api_demo.py`
  - `config/formal_api_demo.example.toml`
  - `tests/test_formal_api_demo_pipeline.py`
- 更新最新交接摘要：
  - `codex_log/latest.md`
- 新增执行日志：
  - `codex_log/20260405_ppt_cloud_first_assembly_route.md`

## 本轮实际验证

- 已复读命中的规则与边界文件：
  - `AGENTS.md`
  - `codex_source/00_codex_readme.md`
  - `codex_log/latest.md`
  - `codex_source/01_execution_rules.md`
  - `codex_source/02_current_execution_context.md`
  - `codex_source/08_branch_sync_and_reading_branch_rules.md`
  - `project_source/01_project_system_prompt.md`
  - `project_source/00_project_brief.md`
  - `project_source/06_project_index.md`
  - `project_source/08_quality_baseline_and_90_score_rules.md`
  - `project_source/13_stage_and_acceptance_gates.md`
  - `project_source/14_content_review_and_loop_governance_rules.md`
- 本轮为口径与状态语义更新；
  - 以目标文件差异审阅、`git diff --check` 和 assembly 相关测试作为本轮验证
