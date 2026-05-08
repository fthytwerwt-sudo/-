# 20260408_ai_report_rewrite_trap_50s_root_cause_guardrail

## 本轮目标

- 对刚完成的 50 秒样片做根因级排查。
- 查清：
  - 为什么没有真正的可见真人出镜
  - 为什么结尾总结卡没有按“步骤 + 易错点”方向表达
- 补最小 guardrail，避免下一轮把“技术可行”误写成“内容达标”。

## 用户本轮明确结论

- `已确认` 用户明确判断：
  - 这条视频只能说技术上可行
  - 内容上完全不合格
  - 问题 1：没有真人出镜
  - 问题 2：结尾总结不是“操作步骤 + 易错点清晰列出”的风格
  - 用户当前不接受继续沿这条质量口径往下走
- 本轮不得为现有样片辩护，只能把这个判断作为正式输入继续排查。

## 实际读取

- `AGENTS.md`
- `codex_log/latest.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_source/02_current_execution_context.md`
- `codex_source/03_research_findings_bridge.md`
- `project_source/24_human_self_footage_light_ppt_routing_rules.md`
- `cases/ai_report_rewrite_trap_50s.md`
- `codex_log/20260408_ai_report_rewrite_trap_50s_real_footage_cloud_sample.md`
- `config/formal_api_demo.example.toml`
- `formal_api_demo_core.py`
- `formal_api_demo_cloud_assembly.py`
- `tests/test_formal_api_demo_pipeline.py`
- 本地正式配置 `~/.config/video-factory/formal_api_demo.local.toml`（读取时屏蔽密钥）
- 本地样片 `dist/formal_api_demo/final.mp4`
- 本地回审帧 `dist/formal_api_demo/review_frames/`
- 本地素材 `素材录制/1.mov`、`素材录制/2.mov`、`素材录制/3.mov`
- 本地仓库 `skills/`：不存在
- 全局 skill：
  - `systematic-debugging`
  - `test-driven-development`
  - `verification-before-completion`
  - `using-superpowers`

## 证据

### 素材证据

- `素材录制/1.mov`
  - `39.38s`
  - HEVC + AAC
  - `3366x2180`
  - 抽帧为屏幕 / 浏览器 / 工作流画面，不是可见真人出镜
- `素材录制/2.mov`
  - `49.28s`
  - HEVC + AAC
  - `3366x2180`
  - 抽帧为屏幕 / ChatGPT 工作流画面，最适合 `process_self_footage`
- `素材录制/3.mov`
  - `38.20s`
  - HEVC + AAC
  - `3366x2180`
  - 抽帧为屏幕 / 浏览器 / 工作流画面，不是可见真人收束

### 配置证据

本轮排查时，本机正式配置映射为：

```toml
[footage_inputs.hook_human]
local_path = "/Users/fan/Documents/视频工厂/素材录制/1.mov"
source_type = "user_screen_recording"

[footage_inputs.process_self_footage]
local_path = "/Users/fan/Documents/视频工厂/素材录制/2.mov"
source_type = "user_screen_recording"

[footage_inputs.result_card]
local_path = "/Users/fan/Documents/视频工厂/dist/formal_api_demo/visual/result_card_ai_report_rewrite_trap_cn.png"
source_type = "user_ppt_image"

[footage_inputs.close_human]
local_path = "/Users/fan/Documents/视频工厂/素材录制/3.mov"
source_type = "user_screen_recording"
```

这说明 `hook_human` 和 `close_human` 在配置层已经是屏幕录制，不是可见真人。

### case 证据

`cases/ai_report_rewrite_trap_50s.md` 中：

- 第 1 段：
  - `段载体：human`
  - `素材键：hook_human`
  - 但画面意图又写了“若实际画面是屏幕录制而非可见人物，回审中必须标记为素材层不足”
- 第 3 段：
  - `段目标：结果卡 / 总结卡，把核心判断收束成可记住的落点`
  - `配音文案：AI 最容易骗你的，不是写不好。是写得太像对了。真正该补的，不是再多生成一版，而是把“能交的判断”继续追出来。`
  - `画面意图：克制的深色结果卡，只显影关键判断`
- 第 4 段：
  - `段载体：human`
  - `素材键：close_human`
  - 但画面意图同样允许“若实际画面不适合人物收束，正式质量判断不得写成已达标”

这说明 case 层已经把“最低可执行占位”写进了 human 槽位，导致技术验证和内容达标混在一起。

### 代码证据

旧逻辑中：

- `_segment_requires_local_media()` 只把 `carrier in {human, self_footage}` 判断成“需要本地素材”
- `_resolve_footage_input()` 只读取：
  - `local_path`
  - `source_type`
  - `media_kind`
- `_evaluate_visual_generation_gate()` 只检查：
  - `local_path` 是否存在
  - 文件是否存在
- 旧逻辑没有检查：
  - `carrier=human` 对应素材是否人工确认 `human_on_camera`
  - `source_type=user_screen_recording` 是否不允许占用 human 槽位

所以当前代码会把“有视频文件”误当成“human 槽位可用”。

## 根因分层

### 素材层

- 主因。
- 用户提供的 3 段素材本身没有明显可见真人出镜。
- 其中 `2.mov` 适合中段过程，`1.mov` 和 `3.mov` 不适合承担人物 hook / close。

### case / 文案层

- 放大器。
- case 为了跑通技术链路，写入了“最低可执行占位”的描述。
- 第 3 段文案本身就是判断式总结，不是步骤式总结。

### 路由层

- 放大器。
- `carrier=human` 被当成槽位语义，而不是被强制绑定到“可见真人出镜”的素材事实。

### 配置层

- 放大器。
- 本地配置把 `hook_human / close_human` 指向屏幕录制素材，并且此前没有 `verified_role` 字段。

### 代码 guardrail 层

- 放大器。
- 旧代码只校验本地路径存在，不校验 `human` 素材角色。
- 因此 pipeline 允许技术链路通过。

### 样片验收层

- 表面现象。
- 最终样片确实 50 秒、云端导出成功、音轨存在，但这只是技术可行，不是内容达标。

## 结果卡偏差根因

- 直接原因：
  - 第 3 段 case 写的是“核心判断收束”
  - 配音 / 字幕文案也是判断句
  - 本地生成的 PNG 也按这些判断句排版
- 根因层级：
  - `case / 文案层` 是主因
  - `result_card 生成模板层` 是放大器
  - `样片验收层` 只是表面现象
- 结论：
  - 下一轮不能只换图，必须先把 case 第 3 段改成“步骤 + 易错点列表型总结卡”的文本和画面意图。

## 本轮实际 guardrail

采用方案 A。

### 配置层

已在本机正式配置里补：

```toml
[footage_inputs.hook_human]
verified_role = "screen_recording"

[footage_inputs.process_self_footage]
verified_role = "screen_recording"

[footage_inputs.result_card]
verified_role = "ppt_image"

[footage_inputs.close_human]
verified_role = "screen_recording"
```

该配置属于 `local_only`，不会提交 GitHub。

### example 配置层

已在 `config/formal_api_demo.example.toml` 说明：

- `verified_role = "human_on_camera"` 才允许进入 `carrier=human`
- `verified_role = "screen_recording"` 适合 `self_footage`
- `verified_role = "ppt_image"` 适合结果卡

### 代码层

已在 `formal_api_demo_core.py` 增加：

- `_resolve_footage_input()` 读取 `verified_role`
- `_evaluate_visual_generation_gate()` 对 `carrier=human` 强制要求：
  - `verified_role == "human_on_camera"`
- `build_visual_generation_plan()` 做同样防守，避免绕过 gate 直接构建 visual asset
- 当 human role guardrail 触发时，non-dry-run generation 不再先调用 TTS，避免在内容前提已经失败时继续消耗 TTS 额度

### 测试层

已在 `tests/test_formal_api_demo_pipeline.py` 增加：

- `test_generation_gate_blocks_screen_recording_in_human_carrier_slots`
- `test_generation_pipeline_skips_tts_when_human_footage_role_is_blocked`

## 实际验证

- 已先运行新增红测，确认旧逻辑失败：
  - `test_generation_gate_blocks_screen_recording_in_human_carrier_slots` 旧逻辑返回 `success`，测试失败
  - `test_generation_pipeline_skips_tts_when_human_footage_role_is_blocked` 旧逻辑仍调用 TTS，测试失败
- 修复后已运行：
  - `python3 -m unittest tests.test_formal_api_demo_pipeline.FormalApiDemoPipelineTests.test_generation_gate_blocks_screen_recording_in_human_carrier_slots`
  - `python3 -m unittest tests.test_formal_api_demo_pipeline.FormalApiDemoPipelineTests.test_generation_pipeline_skips_tts_when_human_footage_role_is_blocked`
- 当前本机配置验证命令：
  - `python3 scripts/generate_formal_api_demo.py --input cases/ai_report_rewrite_trap_50s.md --out dist/_guardrail_probe_20260408`
- 当前验证结果：
  - `overall_status = blocked`
  - `blocked_reason = 缺少视觉生成前提：footage_input_hook_human_verified_role_human_on_camera、footage_input_close_human_verified_role_human_on_camera`
  - `tts_probe_status = blocked`
  - `voiceover_status = blocked`
  - 未再触发 TTS quota 错误
- 全量相关测试：
  - `python3 -m unittest tests.test_formal_api_demo_pipeline tests.test_formal_hybrid_master`
  - `46` tests passed
- diff 检查：
  - `git diff --check`
  - 无输出

## 下一轮最小改动建议

若目标是“步骤 + 易错点总结卡”，最小应改：

1. `cases/ai_report_rewrite_trap_50s.md`
   - 第 3 段改成步骤卡：
     - 步骤 1：先追交付对象要什么
     - 步骤 2：再压重点 / 判断 / 取舍 / 结论
     - 易错点：不要只让 AI 再生成一版
     - 易错点：不要被“像能交”骗过
2. result_card 生成模板 / 生成脚本
   - 当前结果卡是一次性本地 PNG
   - 下一轮若要稳定复用，必须把“步骤 + 易错点”模板落到脚本或可复用渲染逻辑
3. `~/.config/video-factory/formal_api_demo.local.toml`
   - `result_card.local_path` 指向新的步骤型结果卡
4. 若继续坚持人物 hook / close：
   - 必须换成 `verified_role="human_on_camera"` 的可见真人素材

## 当前状态

- 根因排查：
  - `已完成`
- 最小 guardrail：
  - `已完成`
- 新样片：
  - 本轮未生成新样片，符合任务目标
- 同步状态：
  - `task_branch_only`
- 未同步回：
  - `codex/user-readable-map`
