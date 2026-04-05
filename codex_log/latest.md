# Latest

## 当前主结论

- 2026-04-05 已把 pure PPT / 信息卡主线从“`OSS + 云剪 = 默认主路径`、`local assembly = fallback`”正式升级为：
  - `北京区 OSS + 云剪工程 = 唯一 assembly 主路径`
  - `local assembly / local mp4` 已退出 pure PPT / 信息卡主线，不再作为 fallback / 兜底 / 应急正常交付
- 这次升级当前只适用于 pure PPT / 信息卡主线，不自动扩到动态 PPT、数字人 / 真人口播并行分支或复杂 motion design 路线。
- 当前真实边界已经收口为：
  - OSS / IMS / 云剪工程的非密钥参数已写回 repo
  - AccessKey / Secret 仍只保存在用户本地
  - 正式云端导出仍待本地注入密钥后验证
  - `provider_assembly_implementation` 当前仍未真实跑通

## 本轮关键执行事实

- 这轮已经把执行层、项目脑、配置模板、代码与测试统一收口到 cloud-only：
  - `formal_api_demo_core.py`
  - `scripts/assemble_formal_api_demo.py`
  - `config/formal_api_demo.example.toml`
  - `tests/test_formal_api_demo_pipeline.py`
  - `codex_source/01_execution_rules.md`
  - `codex_source/02_current_execution_context.md`
  - `codex_source/03_research_findings_bridge.md`
  - `project_source/00_project_brief.md`
  - `project_source/01_project_system_prompt.md`
  - `project_source/06_project_index.md`
  - `project_source/08_quality_baseline_and_90_score_rules.md`
  - `project_source/10_formal_api_demo_current_route_patch_20260402.md`
  - `codex_log/latest.md`
- 这轮新增完整执行日志：
  - `codex_log/20260405_ppt_cloud_only_assembly_route.md`
- 当前代码层已经改为：
  - assembly gate 改查 OSS / IMS / 云剪工程显式字段
  - pure PPT 主线不再从 `run_assembly_pipeline()` 进入本地 preview / 本地 mp4 补位
  - 缺密钥、缺云端参数或缺 provider implementation 时直接 `blocked`
  - `space_name` / `template_id` 旧前提已退出当前主线配置

## 当前外部已确认状态包

- OSS bucket：`zvip1-video-beijing`
- OSS region：`cn-beijing`
- OSS endpoint：`oss-cn-beijing.aliyuncs.com`
- OSS bucket domain：`zvip1-video-beijing.oss-cn-beijing.aliyuncs.com`
- OSS ACL：`private`
- RAM 用户：`video-factory-oss-1`
- IMS / ICE / 智能媒体服务：北京区已就绪
- 功能体验月包有效期：`2026-05-05 05:00:00`
- IMS storage address：`zvip1-video-beijing.oss-cn-beijing.aliyuncs.com`
- 云剪工程：`video-factory-ppt-master-v1`
- 云剪工程状态：草稿
- 编辑器可打开：是

## 本轮实际验证

- 已复读命中的规则、项目脑、执行上下文、代码、配置与测试文件。
- 已执行：
  - `python3 -m unittest tests.test_formal_api_demo_pipeline`
  - `git diff --check`
- 当前验证结果：
  - `30` 个测试通过
  - `git diff --check` 通过

## 当前交接提醒

- 仓库口径已经改成 cloud-only，但这不等于真实云端导出已经成功。
- 下一步若继续推进，只需要在本地注入真实 AccessKey / Secret，然后针对北京区 OSS + 云剪工程执行最小真实导出验证。
