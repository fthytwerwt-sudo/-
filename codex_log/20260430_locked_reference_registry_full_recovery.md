# 20260430｜锁定参考登记表全量追回

## 1. 本轮范围

- `已确认` 本轮只做 `locked_reference_registry（锁定参考登记表）` 全量口径追回、补登记和局部升级。
- `已确认` 本轮不生成视频，不做 v3，不修改任何视频、音频、图片产物。
- `已确认` 本轮不修改 `dist/latest_review_pack（最新审片包）`。
- `已确认` 本轮不修改 `content_validation（内容验证）`。
- `已确认` 本轮不修改 `send_ready（可发送状态）`。
- `已确认` 本轮不清理旧脏 worktree（旧工作区）`/Users/fan/Documents/视频工厂`。

## 2. 读取结果

- `已确认` 执行目录：`/Users/fan/Documents/视频工厂_clean_user_readable_map_20260430`。
- `已确认` 执行分支：`codex/locked-reference-registry-full-recovery-20260430`。
- `已确认` base（基线）：`origin/codex/user-readable-map（主读取分支）`。
- `已确认` 执行前 worktree（工作区）干净，没有旧目录 5114 个未提交残留。
- `已确认` 已读取：
  - `AGENTS.md（仓库入口规则）`
  - `codex_source/00_codex_readme.md（Codex 执行层总入口）`
  - `codex_source/01_execution_rules.md（Codex 执行规则）`
  - `codex_source/12_codex_known_state_three_layer_rules.md（Codex 已知状态三层规则）`
  - `codex_source/14_locked_reference_inheritance_rules.md（锁定参考继承规则）`
  - `codex_source/locked_reference_registry.md（锁定参考登记表）`
  - `codex_log/latest.md（最新执行摘要）`
  - `codex_log/current_publish_target.md（当前复审 / 发布目标）`
- `已确认` 已核对 PR #7 / #8 / #9 / #14 / #15 / #16 相关证据；PR #16 已进入主读取分支。

## 3. 本轮升级为 locked（锁定参考）

### 3.1 `middle_editing_round34_locked_20260425（round34 中段剪辑语法锁定参考）`

- `已确认` 从原 `middle_editing_round34_candidate_20260425（round34 中段剪辑语法候选）` 升级为 `locked（锁定参考）`。
- 锁定范围：
  - 真实录屏为主体。
  - 卡片只做辅助。
  - 卡片可做段落提示、情绪标点、结果收束。
  - 不允许 Codex 自行改成教程式多 shot（多镜头）结构。
  - 不允许卡片替代真实录屏证据。
- 不锁定范围：
  - 不锁具体秒级时间码。
  - 不锁具体文案。
  - 不锁具体素材长度。
  - 不要求所有视频完全复刻 round34。
  - 不要求所有题材都套用 round34。
- 证据：
  - `codex_log/current_publish_target.md`
  - `dist/latest_review_pack/review_manifest.md`
  - `dist/latest_review_pack/cut_map.md`
  - `dist/latest_review_pack/middle_preview.mp4`

### 3.2 `sassy_card_three_type_rule_locked_20260428（三类骚萌卡放置规则锁定参考）`

- `已确认` 从原 `sassy_card_three_type_rules_pr8_candidate_20260428（三类骚萌卡规则候选）` 升级为 rule-level `locked（规则级锁定参考）`。
- 锁定范围：
  - `problem_hook_sassy_card（问题钩子骚萌卡）` 负责把问题讲得好笑。
  - `negative_reversal_sassy_card（反面反转骚萌卡）` 负责把翻车讲得好笑。
  - `positive_reversal_sassy_card（正面反转骚萌卡）` 负责把变好讲得好笑。
  - 有问题钩子、反转、停顿、情绪标点时触发。
  - 不允许骚萌卡替代真实录屏主体。
  - 不允许只为了热闹而插卡。
- 不锁定范围：
  - 不锁 PR #7 A 版具体视觉。
  - 不锁每条视频必须三张。
  - 不锁具体 punchline（大字笑点文案）。
  - 不锁具体角色或秒数。
- 证据：
  - `origin/codex/sassy-card-structure-budget-20260428:codex_log/20260428_方案B骚萌卡结构机制与节奏预算.md`
  - `origin/codex/sassy-card-structure-budget-20260428:GPT数据源/05_文案路由规则.md`

### 3.3 `tts_15s_b_pacing_locked_20260427（20260427 B 版 15 秒停顿梗感 TTS 节奏锁定参考）`

- `已确认` 从原 `tts_15s_b_pacing_candidate_20260427（B 版 TTS 节奏候选）` 升级为节奏级 `locked（锁定参考）`。
- 锁定范围：
  - `speech_pacing（语速节奏）`
  - `pause_timing（停顿位置）`
  - `copy_fit（文案搭配）`
  - 微反转
  - 轻吐槽
  - 自然口语感
  - 停顿梗感
- 不锁定范围：
  - 不锁最终音色。
  - 不锁最终供应商。
  - 不锁最终 TTS 成片音轨。
  - 不写 `voice_validation（声音验证）= 通过`。
  - 不写 `final_voice_validated（最终声音已验证）= true`。
- 证据：
  - `codex_log/20260427_十五秒文案语速停顿试配.md`
  - `GPT数据源/08_当前正式事实.md`
  - `dist/voice_trials/20260427_十五秒文案语速停顿试配_15s_copy_pacing_trial/B_15秒文案_停顿梗感.wav`

### 3.4 `opening_reference_element_doll_no_text_locked_20260428（元素娃娃无字开头锚点锁定参考）`

- `已确认` 新增并登记为 `locked（锁定参考）`。
- 锁定范围：
  - 元素娃娃无字 / 去字修补版开头锚点。
  - 后续需要元素娃娃开头时，默认优先继承该素材。
  - 不允许 Codex 自行换未经确认的开头素材。
- 不锁定范围：
  - 不代表所有视频都必须有开头。
  - 不代表该开头等于内容通过。
  - 不代表 `send_ready（可发送状态）= yes`。
  - 不锁具体开场文案必须相同。
- 证据：
  - `origin/codex/opening-anchor-20260428:codex_log/20260428_元素娃娃开头无字锚点固定.md`
  - `origin/codex/opening-anchor-20260428:素材库_assets/元素娃娃开头锚点_opening_anchor_20260428/README_开头锚点说明.md`
  - `origin/codex/opening-anchor-20260428:素材库_assets/元素娃娃开头锚点_opening_anchor_20260428/005_1496_seg01_no_text_inpaint_opening_anchor.mp4`
- `已确认` 本轮只登记引用，不复制视频产物。

## 4. 本轮保持 candidate（候选参考）

- `sassy_card_pr7_a_candidate_20260428（PR #7 A 版骚萌卡视觉候选）`
  - 原因：未找到用户明确确认“以后骚萌卡视觉就按这个走”。
- `visual_master_voxel_element_doll_candidate_20260430（体素元素娃娃视觉母版候选）`
  - 原因：已有方向口径，但缺完整视觉母版锁定产物。
- `prompt_card_pink_sakura_round34_candidate_20260430（round34 粉色樱花提示卡候选）`
  - 原因：有局部提示卡证据，但不等于全片视觉母版。
- `function_result_diff_card_round34_candidate_20260430（round34 功能卡 / 结果差卡候选参考）`
  - 原因：有职责规则，缺用户确认的统一视觉母版产物。
- `prompt_tail_card_rule_candidate_20260430（Prompt 引用尾卡规则候选参考）`
  - 原因：有职责规则，缺锁定视觉产物。
- `voice_sample2_cute_guide_voice_candidate_20260426（语音样本2可爱女生向导音候选）`
  - 原因：声音底子可继续用，但不是最终音色验证通过。

## 5. 本轮补充 failed（失败参考）与 gap（缺口参考）

- `subtitle_pr15_v2_failed_20260430（PR #15 v2 字幕失败参考）`
  - 保持 `failed（失败参考）`。
- `layout_pr15_v2_failed_20260430（PR #15 v2 layout / 背景失败参考）`
  - 保持 `failed（失败参考）`。
- `tts_pr15_v2_failed_20260430（PR #15 v2 TTS 缺失失败参考）`
  - 保持 `failed（失败参考）`。
- `zoom_pr15_v2_failed_20260430（PR #15 v2 放大位置失败参考）`
  - 新增 `failed（失败参考）`。
- `subtitle_reference_missing_20260430（字幕标准缺失记录）`
  - 新增 `failed_gap（失败缺口）`。
- `zoom_reference_missing_20260430（正确放大方式缺失记录）`
  - 新增 `failed_gap（失败缺口）`。

## 6. 仍缺证据

- `subtitle_reference（字幕参考）`：缺正确字幕样板、位置、字号、背景、安全区和截图证据。
- `zoom_reference（录屏放大方式参考）`：缺被用户确认的正确放大帧、contact sheet（联系表）、时间码和裁切框。
- `visual_master_reference（视觉母版参考）`：缺完整视觉母版锁定产物。
- `sassy_card_visual_reference（骚萌卡视觉参考）`：PR #7 A 版仍未锁定为默认视觉。
- `ending_reference（结尾参考）`：Prompt 引用尾卡有规则，缺视觉锁定样板。

## 7. 边界确认

- `已确认` 本轮不生成视频。
- `已确认` 本轮不修改 `dist/latest_review_pack（最新审片包）`。
- `已确认` 本轮不修改 `content_validation（内容验证）`。
- `已确认` 本轮不修改 `send_ready（可发送状态）`。
- `已确认` 本轮不修改 `GPT数据源/（项目执行包 / 当前事实层）`。
- `已确认` 本轮不修改 `GPT 数据源/（GPT Project 静态协作包）`。
- `已确认` 本轮不复制 PR #9 的开头视频素材，只在 registry 中登记远端证据路径。

## 8. 下一个目标

下一轮应基于本 registry（登记表）规划 v3 前置继承检查，或先补字幕标准、视觉母版、zoom reference（录屏放大方式参考）这三个仍缺证据的样板。
