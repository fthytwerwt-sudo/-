# Latest

## 当前主结论

- `已确认` 当前正式分支的唯一正式主线已统一改成：
  - API 生成真人
  - 用户本地录制素材
  - 少量 PPT / 图片辅助
  - 北京区 `OSS + 云剪 cloud-only`
- `已确认` 当前正式分支代码事实已经同时具备：
  - `FORMAL_MAINLINE_CASE_PATH`
  - `footage_inputs.process_self_footage`
  - `liveportrait-detect -> liveportrait`
  - `execute_cloud_only_assembly`
- `已确认` 当前主线相关单测已通过：
  - `tests.test_formal_api_demo_pipeline`
  - `tests.test_formal_mainline_route`
- `已确认` 当前真实 dry-run gate 已通过：
  - `current_missing_prerequisites = []`
  - `current_missing_implementations = []`
- `已确认` 当前真实 generation 仍 blocked 在环境层：
  - `aliyun_bailian_tts_request_failed`
  - `AllocationQuota.FreeTierOnly`

## 当前接手建议先读

1. `AGENTS.md`
2. `codex_source/00_codex_readme.md`
3. `codex_log/latest.md`
4. `codex_source/02_current_execution_context.md`
5. `codex_source/03_research_findings_bridge.md`
6. `project_source/00_project_brief.md`
7. `project_source/16_presentation_routing_rules.md`
8. `project_source/24_human_self_footage_light_ppt_routing_rules.md`
9. `cases/formal_api_demo_human_self_footage.md`
10. `formal_api_demo_core.py`
11. `formal_api_demo_cloud_assembly.py`

## 本轮状态

- 当前工作分支：
  - `codex/api-human-mainline-unify-20260409`
- 当前状态标签：
  - `blocked`
- 当前已完成：
  - 正式主线代码与文档已统一
  - API 真人路径已并回当前正式分支
  - 用户本地素材注入路径已并回当前正式分支
  - 云端 assembly 代码路径已并回当前正式分支
- 当前 blocker：
  - 正式 local config 对应的阿里 TTS 免费额度已耗尽，真实 generation 卡在 `AllocationQuota.FreeTierOnly`

## 当前必须继续明确

- `dist/*` 产物和本地配置仍属于 `local_only`
- 当前 reading branch 还没同步本轮统一改造
- 当前 blocked 发生在环境 / provider 配额层，不是默认主线代码缺失层
