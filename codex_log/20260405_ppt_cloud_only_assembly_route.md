# 20260405_ppt_cloud_only_assembly_route

## 本轮目标

- 把《视频工厂》pure PPT / 信息卡主线从：
  - `OSS + 云剪 = 默认主路径`
  - `local assembly = fallback / 兜底`
- 进一步升级为：
  - `北京区 OSS + 云剪工程 = 唯一 assembly 主路径`
  - `local assembly / local mp4` 不再作为 pure PPT 主线 fallback / 兜底 / 应急正常交付

## 执行前已确认事实

- OSS 已具备：
  - bucket：`zvip1-video-beijing`
  - region：`cn-beijing`
  - endpoint：`oss-cn-beijing.aliyuncs.com`
  - bucket domain：`zvip1-video-beijing.oss-cn-beijing.aliyuncs.com`
  - ACL：`private`
- RAM 项目专用用户：`video-factory-oss-1`
- AccessKey 已生成，但只保存在用户本地，不得写入 repo
- IMS / ICE / 智能媒体服务北京区已就绪
- 功能体验月包有效期到：`2026-05-05 05:00:00`
- IMS storage address：`zvip1-video-beijing.oss-cn-beijing.aliyuncs.com`
- 当前云剪工程：`video-factory-ppt-master-v1`
- 当前云剪工程状态：草稿
- 编辑器可打开：是
- 这次升级只适用于 pure PPT / 信息卡主线，不扩到动态 PPT、数字人 / 真人口播并行分支或复杂特效路线

## 实际读取

- `AGENTS.md`
- `codex_log/latest.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_source/02_current_execution_context.md`
- `codex_source/03_research_findings_bridge.md`
- `codex_source/08_branch_sync_and_reading_branch_rules.md`
- `project_source/00_project_brief.md`
- `project_source/01_project_system_prompt.md`
- `project_source/06_project_index.md`
- `project_source/08_quality_baseline_and_90_score_rules.md`
- `project_source/10_formal_api_demo_current_route_patch_20260402.md`
- `project_source/13_stage_and_acceptance_gates.md`
- `project_source/14_content_review_and_loop_governance_rules.md`
- `formal_api_demo_core.py`
- `scripts/assemble_formal_api_demo.py`
- `config/formal_api_demo.example.toml`
- `tests/test_formal_api_demo_pipeline.py`

## 实际改动

### 代码 / 测试 / 配置

- `formal_api_demo_core.py`
  - 纯 PPT 主线的 `run_assembly_pipeline()` 不再进入本地 preview / 本地 mp4 补位
  - assembly gate 改查显式 OSS / IMS / 云剪工程字段
  - `space_name` / `template_id` 旧前提已退出当前主线
  - 缺密钥、缺云端参数或缺 `provider_assembly_implementation` 时直接 `blocked`
  - `local_fallback_used` / `local_mp4_fallback` 旧主线语义已移除
- `tests/test_formal_api_demo_pipeline.py`
  - 先改测试锁定 cloud-only 语义
  - 不再接受 pure PPT 主线回落本地 mp4 为成功
  - 新增对 OSS AccessKey / IMS cloud project 等前提字段的断言
- `config/formal_api_demo.example.toml`
  - 新增 `[aliyun_oss]` / `[aliyun_ims]` 字段
  - 逐项写明字段用途、是否必填、当前是否已确认
  - 保留非密钥已确认值
  - AccessKey / Secret 仍用占位，不入 repo
- `scripts/assemble_formal_api_demo.py`
  - 命令入口描述改为 cloud-only 口径

### 执行层 / 项目脑 / 日志

- `codex_source/01_execution_rules.md`
  - 当前正式主线路由改成北京区 OSS + 云剪工程唯一主路径
- `codex_source/02_current_execution_context.md`
  - 当前执行前上下文改成 cloud-only
  - 写回北京区 OSS / IMS / 云剪工程状态包
  - 明确真实边界只剩“本地注入密钥后验证真实导出”
- `codex_source/03_research_findings_bridge.md`
  - 新增 cloud-only 与外部状态包桥接记录
  - 把旧 cloud-first 记录降为历史覆盖态
- `project_source/00_project_brief.md`
  - 当前正式状态改成 cloud-only
- `project_source/01_project_system_prompt.md`
  - ChatGPT 侧主线路由改成北京区 OSS + 云剪工程唯一主路径
- `project_source/06_project_index.md`
  - 导航说明改成“local fallback 已失效”
- `project_source/08_quality_baseline_and_90_score_rules.md`
  - 质量规则里的 assembly 口径改成 cloud-only
- `project_source/10_formal_api_demo_current_route_patch_20260402.md`
  - 整体重写为 cloud-only 版路线补丁
- `codex_log/latest.md`
  - 收口到最新 cloud-only 交接摘要

## 实际执行

- 先把测试改成新口径，再执行红灯验证：
  - `python3 -m unittest -v tests.test_formal_api_demo_pipeline.FormalApiDemoPipelineTests.test_assemble_dry_run_surfaces_cloud_only_prerequisites`
  - `python3 -m unittest -v tests.test_formal_api_demo_pipeline.FormalApiDemoPipelineTests.test_assemble_non_dry_run_blocks_when_generation_is_still_blocked`
  - `python3 -m unittest -v tests.test_formal_api_demo_pipeline.FormalApiDemoPipelineTests.test_assemble_non_dry_run_blocks_even_when_visual_assets_ready`
- 红灯暴露出的旧行为：
  - gate 仍查 `space_name` / `template_id`
  - 主线仍可能落到本地 preview / 本地 mp4 语义
- 完成代码 / 配置 / 文档改写后，执行：
  - `python3 -m unittest tests.test_formal_api_demo_pipeline`
  - `git diff --check`

## 当前结果

- pure PPT / 信息卡主线在 repo 内已正式改成 cloud-only
- `local assembly / local mp4` 已退出 pure PPT 主线可接受结果
- 北京区 OSS / IMS / 云剪工程的非密钥状态包已桥接回 repo
- AccessKey / Secret 仍只保存在用户本地，没有进入 repo
- 当前真实边界仍保持诚实：
  - `provider_assembly_implementation` 尚未真实跑通
  - 正式云端导出仍待本地注入密钥后验证

## 下一步建议

- 在本地注入真实 OSS AccessKey / Secret 后，只做一次最小真实云端导出验证，并把任务 ID / output ID / 导出结果继续回写仓库。
