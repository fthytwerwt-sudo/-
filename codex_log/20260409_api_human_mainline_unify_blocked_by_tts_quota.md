# 2026-04-09 API 真人主线统一改造（blocked）

## 本轮目标

- 把《视频工厂》当前唯一正式主需求统一改成：
  - API 生成真人
  - 用户本地录制素材
  - 少量 PPT
  - 云端剪辑
- 要求 GPT Project 资料、仓库 project_source / codex_source 口径、当前正式分支代码路径、reading branch 接手口径最终对齐

## 本轮已完成

### 1. 代码主线已统一

- `formal_api_demo_core.py`
  - 恢复并保留 `execute_cloud_only_assembly`
  - 恢复并保留 `FORMAL_MAINLINE_CASE_PATH`
  - 恢复并保留 `footage_inputs`
  - 恢复并保留 `liveportrait-detect -> liveportrait`
  - 把默认主线 route profile 改成：
    - `api_human_local_footage_light_ppt_cloud_editing`
  - 把本地素材要求收紧为：
    - 只默认要求 `process_self_footage`
  - 把 hook / close 改成默认走 API 真人
- `formal_api_demo_cloud_assembly.py`
  - 已回到当前正式改造分支
- `cases/formal_api_demo_human_self_footage.md`
  - 已重写为 API 真人 + 本地素材 + 轻 PPT + 云端剪辑主线 case
- `scripts/generate_formal_api_demo.py`
  - 默认入口仍走 `FORMAL_MAINLINE_CASE_PATH`
  - 文案描述已改成 API 真人主线
- `scripts/assemble_formal_api_demo.py`
  - 文案描述已改成 API 真人主线

### 2. 项目口径已统一

- 已更新：
  - `AGENTS.md`
  - `codex_source/00_codex_readme.md`
  - `codex_source/02_current_execution_context.md`
  - `codex_source/03_research_findings_bridge.md`
  - `codex_source/05_runtime_and_artifact_rules.md`
  - `codex_source/07_formal_api_demo_target_plan.md`
  - `project_source/00_project_brief.md`
  - `project_source/01_project_system_prompt.md`
  - `project_source/03_perplexity_prompt_library.md`
  - `project_source/04_review_templates.md`
  - `project_source/06_project_index.md`
  - `project_source/08_quality_baseline_and_90_score_rules.md`
  - `project_source/10_formal_api_demo_current_route_patch_20260402.md`
  - `project_source/16_presentation_routing_rules.md`
  - `project_source/19_human_self_footage_hybrid_mainline_rules.md`
  - `project_source/24_human_self_footage_light_ppt_routing_rules.md`

### 3. 测试已统一

- 新增：
  - `tests/test_formal_mainline_route.py`
- 更新：
  - `tests/test_formal_api_demo_pipeline.py`
- 当前通过：
  - `python3 -m unittest tests.test_formal_api_demo_pipeline tests.test_formal_mainline_route`

## 主线验证结果

### A. dry-run gate

- 已通过：
  - `current_missing_prerequisites = []`
  - `current_missing_implementations = []`
- 说明：
  - API 真人路径
  - 本地素材注入路径
  - 云端 assembly 路径
  在当前正式分支中已进入同一套默认主线路由

### B. 真实 generation

- 结果：
  - `blocked`
- 真实失败点：
  - `aliyun_bailian_tts_request_failed`
  - 远端返回：
    - `AllocationQuota.FreeTierOnly`
- 说明：
  - 这不是代码缺失
  - 这不是 route 没接通
  - 这是 provider / 配额层阻塞

## 当前为什么仍是 blocked

最高优先级 blocker：

- 默认正式 local config 对应的阿里 TTS 真实调用，在本轮真实 generation 时返回：
  - `AllocationQuota.FreeTierOnly`

因此当前无法继续把：

- API 真人生成
- 配音
- 云端 assembly

整条正式主线写成“已真实跑通”。

## 这轮不能再承诺的事

- 不能承诺“当前正式主线已真实跑通”
- 不能承诺“reading branch 已可直接按真实跑通状态接手”
- 不能承诺“云端正式成片已验证成功”

## 本轮结论

- 代码主线：已统一
- 文档主线：已统一
- tests：已统一并通过
- 真实 provider 运行：被 TTS 配额阻塞
- 本轮总状态：
  - `blocked`
