# 2026-04-08 formal_mainline_human_self_footage_shift

## 本轮目标

- 把《视频工厂》正式默认主线从“pure PPT / 信息卡主承载”切到：
  - 人物
  - 用户自己的真实录制素材
  - 少量 PPT / 图片辅助
- 保持正式 assembly 继续走北京区 OSS + 云剪 cloud-only
- 把 AI talking avatar / 数字人口播正式降级为非默认路线
- 若 formal_api_demo 需要最小代码 / case / schema / config 支持，则一起补齐

## 执行前已确认事实

- 当前工作分支：`codex/provider-auto-rotation`
- `codex_log/latest.md` 旧记录已确认：
  - 正式 local config 默认读取源已切到 `/Users/fan/.config/video-factory/formal_api_demo.local.toml`
  - `ai_report_fluff_trap_45s` 已完成正式 generation 与 cloud assembly
  - 当前状态仍是 `task_branch_only`
- 仓库里已有 formal_api_demo cloud-only 组装骨架
- 仓库里已有部分未提交的“新主线”相关文档 / 代码改动，且与本轮目标同向

## 实际读取

- 强制顺序读取：
  - `AGENTS.md`
  - `codex_log/latest.md`
  - `codex_source/00_codex_readme.md`
  - `codex_source/01_execution_rules.md`
  - `codex_source/02_current_execution_context.md`
  - `codex_source/03_research_findings_bridge.md`
  - `codex_source/08_branch_sync_and_reading_branch_rules.md`
  - `project_source/06_project_index.md`
  - `project_source/00_project_brief.md`
  - `project_source/01_project_system_prompt.md`
  - `project_source/08_quality_baseline_and_90_score_rules.md`
  - `project_source/02_scene_mode_templates.md`
  - `project_source/03_perplexity_prompt_library.md`
  - `project_source/05_psychology_execution_rules.md`
  - `project_source/04_review_templates.md`
  - `project_source/16_presentation_routing_rules.md`
  - `project_source/17_white_collar_ppt_style_rules.md`
- 额外补读：
  - `project_source/10_formal_api_demo_current_route_patch_20260402.md`
  - `project_source/10_video_review_record_template.md`
  - `codex_source/07_formal_api_demo_target_plan.md`
  - `formal_api_demo_core.py`
  - `formal_api_demo_cloud_assembly.py`
  - `formal_hybrid_master.py`
  - `config/formal_api_demo.example.toml`
  - `cases/formal_api_demo.md`
  - `cases/formal_api_demo_human_self_footage.md`
  - `cases/formal_api_demo_30s_hybrid.md`
  - `scripts/generate_formal_api_demo.py`
  - `scripts/assemble_formal_api_demo.py`
  - `tests/test_formal_api_demo_pipeline.py`
  - `tests/test_formal_hybrid_master.py`
- skills 检查：
  - 仓库本地 `skills/`：不存在
  - 全局 `~/.codex/skills`：已检查
  - 实际纳入：
    - `using-superpowers`
    - `verification-before-completion`
    - `test-driven-development`（对代码 / 行为改动部分采用 test-first）
  - `brainstorming` 已读取，但其“必须等待用户批准后再实现”的硬门槛与本轮“直接执行落文件”冲突，因此仅采用设计收口，不作为阻塞

## 实际改动

- 项目脑 / 执行层口径继续收口到：
  - 正式默认主线 = 人物 + 自录素材 + 少量 PPT / 图片
  - pure PPT = 次级支路
  - AI talking avatar = 非默认 / 待验证支线
- `formal_api_demo_core.py`
  - 继续沿现有 route/schema 能力收口
  - 新增 `user_provided_local_assets` / `mixed_user_and_api_local_assets` delivery mode 识别
  - `visual_generation` 输出与 next action hint 改成面向正式新主线
  - local preview / local assembly 的弃用说明改成“正式默认主线”口径
- `config/formal_api_demo.example.toml`
  - 增补 `[footage_inputs.*]` 示例
  - 把 cloud project 注释改成“历史命名仍含 ppt，但当前承载的是新主线”
- `cases/formal_api_demo.md`
  - 显式降级为 pure PPT / 信息卡次级支路样例
- `cases/formal_api_demo_human_self_footage.md`
  - 明确 4 段默认主线样例：
    - `hook_human`
    - `process_self_footage`
    - `result_card`
    - `close_human`
  - `result_card` 改成 `user_media`
- `scripts/generate_formal_api_demo.py`
  - 默认输入改成 `cases/formal_api_demo_human_self_footage.md`
- 日志与桥接文件补齐

## 实际执行

### 1. 测试先行

- 在 `tests/test_formal_api_demo_pipeline.py` 里补：
  - `test_parse_formal_mainline_case_reads_route_fields`
  - `test_generate_non_dry_run_reuses_user_footage_for_formal_mainline_case`

### 2. 红灯定位

- 初始失败点：
  - mainline case 的段数 / asset key 与测试预期不一致
  - new mainline 结果卡仍是 `api_generated`
  - visual generation 成功后 `delivery_mode` 仍固定写成 `api_generated_local_assets`

### 3. 代码与 case 收口

- 把 `result_card` 改成 `user_media`
- 让 `formal_api_demo_core.py` 根据 `segment_assets.asset_origin` 自动区分：
  - `user_provided_local_assets`
  - `mixed_user_and_api_local_assets`
  - `api_generated_local_assets`
- 把 generation / assembly 提示语改成新主线口径

## 当前结果

- 项目脑与执行层的主口径已基本对齐到新主线
- formal_api_demo 的 route / manifest / config example / script default 已能表达并执行新主线
- pure PPT 未删除，但已明确降级为次级支路
- AI talking avatar / 数字人口播已正式写成非默认路线
- 当前仍不能写成“真实新主线已稳定出片”，因为真实人物 / 自录 / 结果卡素材尚未在本轮做一次正式云端导出验证

## 验证

- `已确认`
  - `python3 -m unittest tests.test_formal_api_demo_pipeline.FormalApiDemoPipelineTests.test_parse_formal_mainline_case_reads_route_fields tests.test_formal_api_demo_pipeline.FormalApiDemoPipelineTests.test_generate_non_dry_run_reuses_user_footage_for_formal_mainline_case`
- `已确认`
  - `python3 -m unittest tests.test_formal_api_demo_pipeline.FormalApiDemoPipelineTests.test_parse_formal_case_markdown_reads_core_fields tests.test_formal_api_demo_pipeline.FormalApiDemoPipelineTests.test_generate_non_dry_run_aliyun_bailian_downloads_local_visual_assets tests.test_formal_api_demo_pipeline.FormalApiDemoPipelineTests.test_assemble_dry_run_surfaces_cloud_only_prerequisites tests.test_formal_api_demo_pipeline.FormalApiDemoPipelineTests.test_parse_formal_mainline_case_reads_route_fields tests.test_formal_api_demo_pipeline.FormalApiDemoPipelineTests.test_generate_non_dry_run_reuses_user_footage_for_formal_mainline_case`
- `已确认`
  - `python3 scripts/generate_formal_api_demo.py --input cases/formal_api_demo_human_self_footage.md --dry-run --out /tmp/...`
  - 结果：`route_profile = human_self_footage_light_ppt`，`video_route_strategy = hybrid`

## 未验证 / 阻塞

- `待验证`
  - 真实人物素材、自录素材和结果卡是否已在当前机器齐备
- `待验证`
  - 用真实素材跑一轮正式 cloud assembly 后，成片质量是否达到正式默认主线预期
- `待验证`
  - 当前工作树里已有一批同主题未提交改动，它们与本轮同向，但来源不完全只来自本轮；提交前已按同向结果核对，没有做回退

## 下一步建议

1. 在正式 local config 里补齐 `[footage_inputs.*].local_path`
2. 用真实 hook / 录屏 / 结果卡跑一轮 generation + cloud assembly
3. 导出回审帧并按“正式默认主线回审模板”做下一轮验收
