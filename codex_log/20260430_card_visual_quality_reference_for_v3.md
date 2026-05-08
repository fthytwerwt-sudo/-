# 20260430｜v3 卡片清晰质感参考落仓库

## 1. 本轮目标

- `已确认` 本轮只做《视频工厂》v3 前置参考口径落仓库。
- `已确认` 本轮将用户确认的“功能卡 / 结果差卡 / Prompt 引用尾卡清晰质感参考”写入 `codex_source/locked_reference_registry.md（锁定参考登记表）`。
- `已确认` 本轮不生成 v3，不生成视频，不生成音频，不生成图片。
- `已确认` 本轮不修改 `dist/latest_review_pack/（最新审片包）`。
- `已确认` 本轮不修改 `content_validation（内容验证）`。
- `已确认` 本轮不修改 `send_ready（可发送状态）`。

## 2. 读取结果

- `已确认` 任务命中《视频工厂》，不是 `AI 直播前台验证项目`。
- `已确认` 执行目录使用干净工作区：`/Users/fan/Documents/视频工厂_clean_user_readable_map_20260430`。
- `已确认` 未在旧脏工作区 `/Users/fan/Documents/视频工厂` 执行写入。
- `已确认` 已读取 `AGENTS.md（仓库入口规则）`。
- `已确认` 已检查当前仓库本地 `skills/`，未发现本地 `SKILL.md`。
- `已确认` 已检查全局 `~/.codex/skills`，找到并读取 `context-driven-development（上下文驱动开发）` 与 `verification-before-completion（完成前验证）`。
- `已确认` 未找到专门的 markdown / registry skill；`openai-docs` 不适用于本任务。
- `已确认` 已读取 `codex_source/00_codex_readme.md（Codex 执行层总入口）`。
- `已确认` 已读取 `codex_source/01_execution_rules.md（Codex 执行规则）`。
- `已确认` 已读取 `codex_source/14_locked_reference_inheritance_rules.md（锁定参考继承规则）`。
- `已确认` 已读取 `codex_source/locked_reference_registry.md（锁定参考登记表）`。
- `已确认` 已读取 `codex_log/latest.md（最新执行摘要）`。
- `已确认` 已读取 `codex_log/current_publish_target.md（当前复审 / 发布目标）`。
- `已确认` 已读取 `dist/latest_review_pack/summary.json（最新审片包状态摘要）`。
- `已确认` 已读取 `dist/latest_review_pack/review_manifest.md（最新审片包审片入口）`。
- `已确认` 已读取 `codex_log/20260430_locked_reference_registry_full_recovery.md（锁定参考登记表全量追回日志）`。
- `已确认` 已读取 `codex_log/20260427_十五秒文案语速停顿试配.md（B 版 TTS 节奏日志）`。
- `已确认` 已读取 `codex_log/20260426_语音样本2复刻与文案风格解析.md（语音样本2 custom voice 日志）`。
- `已确认` 已读取 registry 中 `sassy_card_pr7_a_candidate_20260428（PR #7 A 版骚萌卡视觉候选）`。
- `已确认` 本地 Git 可读取 PR #7 远端 ref：`origin/codex/scheme-b-standalone-v3-diagnostics-20260428` 的 preview report 与 prototype 路径。

## 3. 用户确认内容

- `已确认` 用户本轮提供的手机竖屏 UI 参考图，Codex 不知道原图，也无法默认读取 ChatGPT 图片上下文。
- `已确认` 用户本轮确认图片引用“完全对”，但本轮真正继承的是视觉质感，不是结构照抄。
- `已确认` 本轮应继承的文字化锚点：
  - 清晰
  - 有质感
  - 干净
  - 留白足
  - 圆角卡片
  - 轻阴影
  - 轻高光
  - 层级舒服
  - 文字清楚
  - 有一点高级 UI 感
- `已确认` 本轮不继承：
  - 底部黑色按钮
  - 电商筛选页
  - `More Filters` 式 CTA
  - 假 App 导航
  - 一堆分类筛选项
  - 英文乱码
  - 真实 UI 照抄

## 4. 写入 registry 的条目

- `已确认` 新增 `card_visual_quality_clean_ui_texture_candidate_20260430（功能卡 / 结果差卡 / Prompt 引用尾卡清晰质感候选参考）`。
- `已确认` 该 reference 的 `status（状态） = candidate（候选参考）`。
- `已确认` 该 reference 的 `confirmation_state（确认状态） = candidate_or_rule_reference（候选规则参考）`。
- `已确认` 该 reference 适用于 v3 的：
  - `function_card（功能卡）`
  - `result_diff_card（结果差卡）`
  - `prompt_tail_card（Prompt 引用尾卡）`
  - 少量 PPT / 卡片承载的信息整理段
  - 需要提升清晰度、质感、层级、可读性的 9:16 竖屏卡片
- `已确认` 该 reference 不适用于：
  - 字幕样式
  - 中段真实录屏主体
  - 骚萌卡角色视觉
  - API 生成真人 / 元素娃娃开头
  - 电商筛选页 UI
  - App 导航页
  - 底部 CTA 按钮
  - `More Filters` 式按钮结构
  - 密集列表型筛选项
- `已确认` 该 reference 只能继承质感：干净、清楚、轻阴影、轻高光、层级分明、文字清晰、不糊、不脏、不像普通 PPT 模板。
- `已确认` 该 reference 必须融合《视频工厂》当前体素 / 元素娃娃风格，不能变成真实 App 筛选页。

## 5. 本轮 v3 前置锚点

- `已确认` 当前没有 `visual_master_reference（视觉母版锁定参考）`。
- `已确认` registry 中当前只有 `visual_master_voxel_element_doll_candidate_20260430（体素元素娃娃视觉母版候选）`，不是 locked。
- `已确认` v3 如果做出来符合用户标准，后续才可能反向成为视觉母版候选；当前不能写成已有视觉母版。
- `已确认` 当前没有正确 `subtitle_reference（字幕锁定参考）`。
- `已确认` PR #15 v2 字幕仍是 `failed_reference（失败参考）`，不得继承。
- `已确认` 用户本轮确认 v3 先不上字幕，本轮不建立字幕标准。
- `已确认` `sassy_card_three_type_rule_locked_20260428（三类骚萌卡放置规则锁定参考）` 锁定的是放置 / 职责规则，不是视觉样式。
- `已确认` `sassy_card_pr7_a_candidate_20260428（PR #7 A 版骚萌卡视觉候选）` 仍是 candidate；用户本轮确认 v3 骚萌卡视觉先以 PR #7 A 版作为参考，但不得写成 locked。
- `已确认` `tts_15s_b_pacing_locked_20260427（B 版 15 秒停顿梗感 TTS 节奏锁定参考）` 锁定的是节奏、停顿、轻吐槽和文案搭配方向。
- `已确认` 最近 custom voice（自定义音色）为 `qwen-t...ac19`，来自语音样本2链路，可与 B 版停顿梗感节奏配合作为 v3 前置参考。
- `待验证` custom voice 仍不是最终音色；不得写最终声音通过，不得写 `final_voice_validated = true`。

## 6. 同步补充的交叉引用

- `已确认` `function_result_diff_card_round34_candidate_20260430（round34 功能卡 / 结果差卡候选参考）` 已补充引用 `card_visual_quality_clean_ui_texture_candidate_20260430` 作为后续 v3 质感候选参考。
- `已确认` `prompt_tail_card_rule_candidate_20260430（Prompt 引用尾卡规则候选参考）` 已补充引用 `card_visual_quality_clean_ui_texture_candidate_20260430` 作为后续 v3 质感候选参考。
- `已确认` `sassy_card_pr7_a_candidate_20260428（PR #7 A 版骚萌卡视觉候选）` 已补充本轮用户确认：v3 可先作为候选参考使用，但不升级 locked。
- `已确认` `tts_15s_b_pacing_locked_20260427（B 版 15 秒停顿梗感 TTS 节奏锁定参考）` 与 `voice_sample2_cute_guide_voice_candidate_20260426（语音样本2可爱女生向导音候选）` 已补充“节奏 locked、音色待验证”的边界。

## 7. 本轮未做事项

- `已确认` 本轮没有生成 v3。
- `已确认` 本轮没有生成任何视频、音频或图片。
- `已确认` 本轮没有调用阿里 / DashScope / TTS / 图像生成 API。
- `已确认` 本轮没有修改 `dist/latest_review_pack/（最新审片包）`。
- `已确认` 本轮没有修改 `content_validation（内容验证）`。
- `已确认` 本轮没有修改 `send_ready（可发送状态）`。
- `已确认` 本轮没有把 candidate 写成 locked。
- `已确认` 本轮没有把 TTS 写成最终声音通过。

## 8. 下一个目标

下一轮应基于 `locked_reference_registry（锁定参考登记表）` 先生成 v3 执行前锚点表，明确 `locked_reference（锁定参考）`、`candidate_reference（候选参考）`、`failed_reference（失败参考）` 和本轮文字锚点，再决定是否下发 v3 生成任务。
