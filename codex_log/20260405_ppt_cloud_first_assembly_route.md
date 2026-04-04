# 20260405_ppt_cloud_first_assembly_route

## 本轮目标

- 把《视频工厂》当前纯 PPT / 信息卡主线的 assembly 正式口径升级为：
  - `OSS + 云剪 = 默认`
  - `local assembly = fallback / 兜底`
- 同步更新执行层、项目脑、配置、脚本说明和状态语义

## 执行前已确认事实

- 当前主读取分支固定为 `codex/user-readable-map`
- 当前旧口径仍残留“local assembly 默认交付 / cloud assembly optional”
- 用户本轮新增正式事实：
  - OSS 已具备
  - 阿里云剪已具备
- 当前边界仍未改变：
  - 动态 PPT 暂不考虑
  - 数字人继续并行修，但不阻塞纯 PPT 主线
  - 云剪第一轮不是复杂动效路线
- 当前工作树里存在与本轮无关的本地改动：
  - `project_source/00_project_brief.md`
  - `project_source/03_perplexity_prompt_library.md`

## 实际读取

- `AGENTS.md`
- `codex_log/latest.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_source/02_current_execution_context.md`
- `codex_source/03_research_findings_bridge.md`
- `codex_source/05_runtime_and_artifact_rules.md`
- `codex_source/08_branch_sync_and_reading_branch_rules.md`
- `project_source/00_project_brief.md`
- `project_source/01_project_system_prompt.md`
- `project_source/06_project_index.md`
- `project_source/08_quality_baseline_and_90_score_rules.md`
- `project_source/10_formal_api_demo_current_route_patch_20260402.md`
- `project_source/13_stage_and_acceptance_gates.md`
- `project_source/14_content_review_and_loop_governance_rules.md`
- 代码 / 配置 / 测试：
  - `formal_api_demo_core.py`
  - `scripts/assemble_formal_api_demo.py`
  - `config/formal_api_demo.example.toml`
  - `tests/test_formal_api_demo_pipeline.py`

## 实际改动

- 更新执行层：
  - `codex_source/02_current_execution_context.md`
  - `codex_source/03_research_findings_bridge.md`
- 更新项目脑：
  - `project_source/00_project_brief.md`
  - `project_source/01_project_system_prompt.md`
  - `project_source/06_project_index.md`
  - `project_source/08_quality_baseline_and_90_score_rules.md`
  - `project_source/10_formal_api_demo_current_route_patch_20260402.md`
- 更新代码 / 配置 / 测试：
  - `formal_api_demo_core.py`
  - `scripts/assemble_formal_api_demo.py`
  - `config/formal_api_demo.example.toml`
  - `tests/test_formal_api_demo_pipeline.py`
- 更新日志：
  - `codex_log/latest.md`
  - `codex_log/20260405_ppt_cloud_first_assembly_route.md`

## 实际执行

- 把纯 PPT / 信息卡主线的正式主路径从“本地 assembly 默认”改成“OSS + 云剪默认、本地 fallback”
- 删除 / 覆盖仓库中“cloud assembly optional / skipped / 后续增强项”的旧默认表述
- 保留本地 assembly 能力，但明确只在云剪失败、模板异常、上传异常或任务超时时兜底
- 把 `delivery_mode`、assembly gate、脚本说明、示例配置和测试语义同步改成 cloud first / local fallback

## 当前结果

- 仓库正式口径已不再写“纯 PPT 主线默认本地 assembly”
- 当前新口径已经明确：
  - 纯 PPT 主线：`OSS + 云剪 = 默认`
  - `local assembly = fallback`
- 当前仍保留的边界也已写死：
  - 动态 PPT 暂不考虑
  - 数字人继续并行修，但不阻塞纯 PPT 主线
  - 云剪第一轮仍只服务转场统一、字幕安全区、模板化 assembly、片头 / 正文 / 结尾模板化

## 下一步建议

- 若后续继续做纯 PPT / 信息卡主线样片，默认按 cloud first / local fallback 骨架继续验证
- 若要让云剪状态从“主路径语义已升级”进一步进入“代码真实执行成功”，下一轮只聚焦正式 provider assembly implementation
