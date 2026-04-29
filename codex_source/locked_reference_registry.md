# 锁定参考登记表 locked_reference_registry

## 1. 文件定位

本文件登记《视频工厂》后续可继承的 `reference（参考）`。

配套规则见：

- `codex_source/14_locked_reference_inheritance_rules.md（锁定参考继承规则）`

当前 registry（登记表）的硬规则：

- `locked（锁定参考）` 只锁用户 / ChatGPT 已明确确认、且有证据路径、适用范围、不适用范围、继承方式和 blocked 条件的局部样板。
- `candidate（候选参考）` 只能作为候选、复审或试继承参考，不得写成用户已确认。
- `failed（失败参考）` 只能作为反例或复盘材料，不得默认继承。
- `historical（历史参考）` 只能帮助理解演化，不自动等同当前标准。
- `candidate_gap（候选缺口）` / `failed_gap（失败缺口）` 用于登记“需要建立正确参考”的缺口，不得被完整成片默认继承。
- PR 自评、技术通过、候选片 `pass_for_candidate_review` 不等于用户 / ChatGPT 明确确认。
- 写入本分支不等于 `codex/user-readable-map（主读取分支）` 正式同步；只有本 PR 合并 / 回流后，才算新聊天默认正式已知。

## 2. 字段说明

| 字段 | 中文备注 |
| --- | --- |
| `reference_id` | 参考编号 |
| `name` | 中文名称 |
| `type` | 类型，如 `opening（开头）` / `subtitle（字幕）` / `tts（文本转语音）` / `zoom（录屏放大）` / `sassy_card（骚萌卡）` |
| `status` | `locked（锁定参考）` / `candidate（候选参考）` / `failed（失败参考）` / `deprecated（废弃参考）` / `historical（历史参考）` / `candidate_gap（候选缺口）` / `failed_gap（失败缺口）` |
| `confirmation_state` | `candidate_reference_pending_confirmation（候选参考待确认）` / `locked_reference_confirmed_by_user（用户确认锁定参考）` / `locked_reference_confirmed_by_chatgpt（ChatGPT 复审确认锁定参考）` / `locked_reference_formal_synced（已同步主读取分支锁定参考）` / `failed_or_pending_reference（失败或待复盘参考）` / `candidate_or_rule_reference（候选规则参考）` |
| `source_pr_or_log` | 来源 PR 或日志 |
| `artifact_path` | 产物路径 |
| `evidence_path` | 证据路径，如 contact sheet（联系表）/ clip（片段）/ audio（音频）/ report（报告） |
| `confirmed_by` | 确认方：`user（用户）` / `ChatGPT（复审）` / `Codex technical only（仅 Codex 技术判断）` |
| `confirmation_quote_or_record` | 确认依据 |
| `applies_to` | 适用范围 |
| `does_not_apply_to` | 不适用范围 |
| `inheritance_rule` | 后续如何继承 |
| `allowed_changes` | 允许修改范围 |
| `blocked_if` | 阻断条件 |
| `last_verified_at` | 最近验证时间 |
| `notes` | 备注 |

## 3. locked_reference（锁定参考）

### 3.1 round34 中段剪辑语法锁定参考

| 字段 | 值 |
| --- | --- |
| `reference_id` | `middle_editing_round34_locked_20260425` |
| `name` | round34 中段剪辑语法锁定参考 |
| `type` | `middle_editing（中段剪辑）` |
| `status` | `locked（锁定参考）` |
| `confirmation_state` | `locked_reference_confirmed_by_user（用户确认锁定参考）` |
| `source_pr_or_log` | `codex_log/latest.md`; `codex_log/current_publish_target.md`; `GPT数据源/08_当前正式事实.md`; `dist/latest_review_pack/review_manifest.md`; `dist/latest_review_pack/cut_map.md` |
| `artifact_path` | `dist/latest_review_pack/middle_preview.mp4` |
| `evidence_path` | `dist/latest_review_pack/cut_map.md`; `dist/latest_review_pack/timeline.json`; `dist/latest_review_pack/cut_contact_sheet.jpg`; `dist/latest_review_pack/summary.json`; `dist/latest_review_pack/review_manifest.md` |
| `confirmed_by` | `user（用户）` |
| `confirmation_quote_or_record` | `已确认` 用户反馈 round34 中段“现在中段没什么问题了”；`codex_log/current_publish_target.md` 记录 `middle_segment_review = 用户暂定通过 / 暂不继续修改中段`；本轮执行单要求追回并登记中段剪辑方式。 |
| `applies_to` | 同类 AI 知识视频中段；需要反面 / 正面分段提示、真实录屏主体、结果差辅助卡时。 |
| `does_not_apply_to` | 无中段录屏证据的视频；探索新剪辑语法；用户明确要求重做中段；需要完全不同叙事结构的题材。 |
| `inheritance_rule` | 同类完整成片默认继承“真实录屏为主体，卡片只做辅助”的中段语法；可继承“反面展示提示卡 -> 反面真实录屏 -> 正面展示提示卡 -> 正面真实录屏 -> 结果差提示卡”的结构；不得自行改成教程式多 shot（多镜头）结构；不得让卡片替代真实录屏证据。 |
| `allowed_changes` | 可根据新素材时长、文案节奏和平台比例调整时间码、字幕文字、卡片文字、压缩比例和局部过渡。 |
| `blocked_if` | 中段真实录屏不再是主体；卡片替代录屏证据；Codex 自行改成教程式多 shot 结构；完整成片未输出 `locked_reference_inheritance_report.md（锁定参考继承报告）`；放大位置与证据点对不上且未获用户授权。 |
| `last_verified_at` | 2026-04-30 |
| `notes` | 锁定的是剪辑语法，不锁具体秒级时间码、具体文案、具体素材长度，也不要求所有题材完全复刻 round34。 |

### 3.2 三类骚萌卡放置规则锁定参考

| 字段 | 值 |
| --- | --- |
| `reference_id` | `sassy_card_three_type_rule_locked_20260428` |
| `name` | 三类骚萌卡放置规则锁定参考 |
| `type` | `sassy_card_rule（骚萌卡规则）` |
| `status` | `locked（锁定参考）` |
| `confirmation_state` | `locked_reference_confirmed_by_user（用户确认锁定参考）` |
| `source_pr_or_log` | PR #8 `方案 B 三类骚萌卡机制与节奏预算`; `origin/codex/sassy-card-structure-budget-20260428:codex_log/20260428_方案B骚萌卡结构机制与节奏预算.md`; `origin/codex/sassy-card-structure-budget-20260428:GPT数据源/05_文案路由规则.md` |
| `artifact_path` | `origin/codex/sassy-card-structure-budget-20260428:GPT数据源/05_文案路由规则.md#8A` |
| `evidence_path` | `origin/codex/sassy-card-structure-budget-20260428:codex_log/20260428_方案B骚萌卡结构机制与节奏预算.md`; `origin/codex/sassy-card-structure-budget-20260428:GPT数据源/05_文案路由规则.md#8A` |
| `confirmed_by` | `user（用户）` |
| `confirmation_quote_or_record` | `已确认` PR #8 记录：正面也需要一张骚萌卡；有反转阶段即可触发；元素娃娃 slogan 后还有一个骚萌卡位置；三张必须风格统一、都要搞笑、且每张承载什么必须在文案路由阶段写清。 |
| `applies_to` | 同类需要 `problem_hook_sassy_card（问题钩子骚萌卡）`、`negative_reversal_sassy_card（反面反转骚萌卡）`、`positive_reversal_sassy_card（正面反转骚萌卡）` 的 AI 知识视频。 |
| `does_not_apply_to` | 用户明确要求本轮不用骚萌卡；没有问题钩子、反转或停顿；素材证据链会被插卡打断；正在探索新的卡片机制。 |
| `inheritance_rule` | `problem_hook_sassy_card（问题钩子骚萌卡）` 负责把问题讲得好笑；`negative_reversal_sassy_card（反面反转骚萌卡）` 负责把翻车讲得好笑；`positive_reversal_sassy_card（正面反转骚萌卡）` 负责把变好讲得好笑；骚萌卡不得替代真实录屏主体，不得只是为了热闹而插卡，不得挤占主体证据链。 |
| `allowed_changes` | 可按文案、题材、时长和素材节奏调整是否三张都出现、具体 punchline（大字笑点文案）、每张时长、角色动作和卡片文案。 |
| `blocked_if` | Codex 把骚萌卡当装饰贴片；三张卡不是统一角色体系；卡片不搞笑或变普通信息卡；为了插卡压缩真实录屏主体；把 PR #7 A 版具体视觉误写成锁定视觉。 |
| `last_verified_at` | 2026-04-30 |
| `notes` | 锁定的是 rule-level locked reference（规则级锁定参考），不是 visual locked reference（视觉锁定参考）；不锁 PR #7 A 版具体角色、具体视觉、具体秒数或每条视频必须三张。 |

### 3.3 20260427 B 版 15 秒停顿梗感 TTS 节奏锁定参考

| 字段 | 值 |
| --- | --- |
| `reference_id` | `tts_15s_b_pacing_locked_20260427` |
| `name` | 20260427 B 版 15 秒停顿梗感 TTS 节奏锁定参考 |
| `type` | `tts_pacing（TTS / 文本转语音节奏）` |
| `status` | `locked（锁定参考）` |
| `confirmation_state` | `locked_reference_confirmed_by_user（用户确认锁定参考）` |
| `source_pr_or_log` | `codex_log/20260427_十五秒文案语速停顿试配.md`; `codex_log/latest.md`; `GPT数据源/08_当前正式事实.md` |
| `artifact_path` | `dist/voice_trials/20260427_十五秒文案语速停顿试配_15s_copy_pacing_trial/B_15秒文案_停顿梗感.wav` |
| `evidence_path` | `dist/voice_trials/20260427_十五秒文案语速停顿试配_15s_copy_pacing_trial/README.md`; `dist/voice_trials/20260427_十五秒文案语速停顿试配_15s_copy_pacing_trial/run_summary.json`; `dist/voice_trials/20260427_十五秒文案语速停顿试配_15s_copy_pacing_trial/B_ffmpeg_decode_check.txt`; `dist/voice_trials/20260427_十五秒文案语速停顿试配_15s_copy_pacing_trial/B_loudnorm_measure.txt`; `codex_log/20260427_十五秒文案语速停顿试配.md` |
| `confirmed_by` | `user（用户）` |
| `confirmation_quote_or_record` | `已确认` `GPT数据源/08_当前正式事实.md` 记录用户更喜欢 20260427 B 版“停顿梗感”方向，后续优先调 `speech_pacing（语速节奏）`、`pause_timing（停顿位置）`、`copy_fit（文案搭配）`；本轮执行单要求仅锁节奏，不锁最终音色。 |
| `applies_to` | 同类 15 秒左右中文口播；需要微反转、轻吐槽、自然口语感、停顿梗感和文案节奏参考时。 |
| `does_not_apply_to` | 最终音色、最终供应商、最终 TTS 成片音轨、非中文视频、用户明确要求换音色 / 重做节奏 / 不使用该声音底子。 |
| `inheritance_rule` | 后续 TTS 任务默认继承 B 版的节奏方向：自然口语、轻吐槽、微反转、停顿梗感；必须输出音频或时间码对照；不得把该 reference 写成最终声音验证通过。 |
| `allowed_changes` | 可调整音色、供应商、文案内容、语速细节、停顿点、响度、降噪和轻微后处理。 |
| `blocked_if` | 写成 `voice_validation（声音验证）= 通过`；写成 `final_voice_validated（最终声音已验证）= true`；无听感对照却声明 TTS 继承通过；完整片没有 TTS 却声明 TTS 通过。 |
| `last_verified_at` | 2026-04-30 |
| `notes` | 锁定的是 TTS pacing（文本转语音节奏），不是 final voice（最终音色）或成片音轨。 |

### 3.4 元素娃娃无字开头锚点锁定参考

| 字段 | 值 |
| --- | --- |
| `reference_id` | `opening_reference_element_doll_no_text_locked_20260428` |
| `name` | 元素娃娃无字开头锚点锁定参考 |
| `type` | `opening（开头）` |
| `status` | `locked（锁定参考）` |
| `confirmation_state` | `locked_reference_confirmed_by_user（用户确认锁定参考）` |
| `source_pr_or_log` | PR #9 `固定元素娃娃开头无字锚点`; `origin/codex/opening-anchor-20260428:codex_log/20260428_元素娃娃开头无字锚点固定.md`; `origin/codex/opening-anchor-20260428:素材库_assets/元素娃娃开头锚点_opening_anchor_20260428/README_开头锚点说明.md` |
| `artifact_path` | `origin/codex/opening-anchor-20260428:素材库_assets/元素娃娃开头锚点_opening_anchor_20260428/005_1496_seg01_no_text_inpaint_opening_anchor.mp4` |
| `evidence_path` | `origin/codex/opening-anchor-20260428:素材库_assets/元素娃娃开头锚点_opening_anchor_20260428/README_开头锚点说明.md`; `origin/codex/opening-anchor-20260428:素材库_assets/元素娃娃开头锚点_opening_anchor_20260428/opening_anchor_manifest.json`; `origin/codex/opening-anchor-20260428:codex_log/20260428_元素娃娃开头无字锚点固定.md` |
| `confirmed_by` | `user（用户）` |
| `confirmation_quote_or_record` | `已确认` PR #9 记录用户反馈 `005_1496_seg01_no_text_inpaint.mp4（005_1496_seg01 去字修补版视频）` “完全没问题”；README 记录“该版本以后可固定作为开头素材 / 元素娃娃开头锚点使用”。 |
| `applies_to` | 后续需要元素娃娃开头、slogan 开头、可爱元素主持娃娃 opening anchor（开头锚点）时。 |
| `does_not_apply_to` | 用户明确要求本轮没有开头；用户要求换开头风格；非元素娃娃体系；正式正片整体节奏、声音、内容验证。 |
| `inheritance_rule` | 后续需要元素娃娃开头时，默认优先继承该无字 / 去字修补版开头锚点；Codex 不得自行换未经确认的开头素材，不得重新找未确认开头。 |
| `allowed_changes` | 可调整开头文案、时长裁剪、转场、字幕和与后续片段的拼接；不得替换核心开头素材，除非用户授权。 |
| `blocked_if` | 目标分支或远端无法读取该 artifact；Codex 自行换开头素材；把开头锁定误写成整片内容通过；写 `send_ready（可发送状态）= yes`。 |
| `last_verified_at` | 2026-04-30 |
| `notes` | 该素材当前仍位于 PR #9 分支；本轮只登记 registry（登记表），不复制视频产物。若完整成片任务读不到该远端 artifact，必须 blocked 或先同步素材。 |

## 4. candidate_reference（候选参考）

### 4.1 PR #7 A 版骚萌卡视觉候选

| 字段 | 值 |
| --- | --- |
| `reference_id` | `sassy_card_pr7_a_candidate_20260428` |
| `name` | PR #7 A 版骚萌卡视觉候选 |
| `type` | `sassy_card_visual（骚萌卡视觉）` |
| `status` | `candidate（候选参考）` |
| `confirmation_state` | `candidate_reference_pending_confirmation（候选参考待确认）` |
| `source_pr_or_log` | PR #7 `方案 B V3 骚萌表情版独立反应预览`; `origin/codex/scheme-b-standalone-v3-diagnostics-20260428:codex_log/20260428_方案B独立反应片段V3骚萌表情迭代.md` |
| `artifact_path` | `origin/codex/scheme-b-standalone-v3-diagnostics-20260428:dist/prototypes/20260428_方案B独立反应片段V3_scheme_b_standalone_reaction_v3/方案B独立反应页_骚萌A_static_reaction_page.png` |
| `evidence_path` | `origin/codex/scheme-b-standalone-v3-diagnostics-20260428:dist/prototypes/20260428_方案B独立反应片段V3_scheme_b_standalone_reaction_v3/方案B独立反应V3说明_preview_report.md`; `origin/codex/scheme-b-standalone-v3-diagnostics-20260428:dist/prototypes/20260428_方案B独立反应片段V3_scheme_b_standalone_reaction_v3/run_summary.json`; `origin/codex/scheme-b-standalone-v3-diagnostics-20260428:dist/prototypes/20260428_方案B独立反应片段V3_scheme_b_standalone_reaction_v3/方案B独立反应页_骚萌候选对比_contact_sheet.jpg` |
| `confirmed_by` | `Codex technical only（仅 Codex 技术判断）` |
| `confirmation_quote_or_record` | `已确认` PR #7 A 版被选中进入技术预览；`待验证` 未找到用户明确确认“以后骚萌卡视觉就按这个走”。 |
| `applies_to` | “贱萌 / 得瑟 / 小坏笑 / wink / 捂嘴偷笑”方向的骚萌卡视觉复审。 |
| `does_not_apply_to` | locked visual reference（视觉锁定参考）；用户明确要求更成熟、更克制、更写实或非表情包方向。 |
| `inheritance_rule` | 只能作为视觉候选对照；完整成片中若使用，必须标注为 `candidate（候选参考）`。 |
| `allowed_changes` | 可调整表情夸张度、构图、角色、文案、动效和时长。 |
| `blocked_if` | 把 PR #7 A 版写成用户已确认 locked；忽略用户后续对骚萌视觉的负反馈。 |
| `last_verified_at` | 2026-04-30 |
| `notes` | PR #8 锁定的是放置规则，不锁 PR #7 A 版视觉。 |

### 4.2 体素元素娃娃视觉母版候选

| 字段 | 值 |
| --- | --- |
| `reference_id` | `visual_master_voxel_element_doll_candidate_20260430` |
| `name` | 体素元素娃娃视觉母版候选 |
| `type` | `visual_master（视觉母版）` |
| `status` | `candidate（候选参考）` |
| `confirmation_state` | `candidate_reference_pending_confirmation（候选参考待确认）` |
| `source_pr_or_log` | `GPT数据源/06_当前主线锚点_API生成真人_用户录制素材_少量PPT_云端剪辑.md`; `GPT数据源/07_AI知识类视频价值规则.md`; `GPT数据源/08_当前正式事实.md` |
| `artifact_path` | `GPT数据源/08_当前正式事实.md` |
| `evidence_path` | `GPT数据源/06_当前主线锚点_API生成真人_用户录制素材_少量PPT_云端剪辑.md`; `GPT数据源/07_AI知识类视频价值规则.md`; `GPT数据源/08_当前正式事实.md` |
| `confirmed_by` | `user_direction_record（用户方向记录）` |
| `confirmation_quote_or_record` | `已确认` 当前 vNext 开头 / 结尾壳默认统一为 `Minecraft-inspired 原创体素方块风`，主持壳方向收窄为 `可爱元素主持娃娃`；`待验证` 尚未找到完整视觉母版锁定产物。 |
| `applies_to` | vNext 开头人物壳、结尾总结壳、元素主持娃娃视觉方向。 |
| `does_not_apply_to` | 完整片视觉母版 locked；PR #15 v2 背景 / layout；真实 Minecraft 官方资产复用。 |
| `inheritance_rule` | 可作为视觉方向候选；完整成片不得自行换成不相关背景风格；若无具体视觉母版产物，必须在继承报告中标注为 candidate。 |
| `allowed_changes` | 可继续补完整 visual master（视觉母版）、接入具体截图 / contact sheet（联系表）和样片。 |
| `blocked_if` | 把抽象视觉方向写成完整视觉母版 locked；使用官方 Minecraft 资产；沿用 PR #15 v2 被否定的背景风格。 |
| `last_verified_at` | 2026-04-30 |
| `notes` | 当前是方向候选，不是可直接继承的完整视觉母版。 |

### 4.3 round34 粉色樱花提示卡候选

| 字段 | 值 |
| --- | --- |
| `reference_id` | `prompt_card_pink_sakura_round34_candidate_20260430` |
| `name` | round34 粉色樱花提示卡候选 |
| `type` | `prompt_card_visual（提示卡视觉）` |
| `status` | `candidate（候选参考）` |
| `confirmation_state` | `candidate_reference_pending_confirmation（候选参考待确认）` |
| `source_pr_or_log` | `dist/latest_review_pack/review_manifest.md`; `dist/latest_review_pack/cut_map.md`; `GPT数据源/08_当前正式事实.md`; `codex_log/current_publish_target.md` |
| `artifact_path` | `dist/latest_review_pack/反面展示提示卡_单帧.png`; `dist/latest_review_pack/正面展示提示卡_单帧.png` |
| `evidence_path` | `dist/latest_review_pack/图二参考图.png`; `dist/latest_review_pack/正反提示卡_并排对比.png`; `dist/latest_review_pack/review_manifest.md`; `dist/latest_review_pack/cut_map.md` |
| `confirmed_by` | `user_partial_middle_segment_review（用户中段暂定接受）` |
| `confirmation_quote_or_record` | `已确认` round34 反面 / 正面提示卡按用户同步图二重构为粉色樱花柔和展示牌风格；中段整体被用户暂定接受；`待验证` 这不等于全片视觉母版 locked。 |
| `applies_to` | round34 同类反面 / 正面展示提示卡、段落提示卡。 |
| `does_not_apply_to` | 全片背景风格、骚萌卡视觉、字幕标准、完整 visual master（视觉母版）。 |
| `inheritance_rule` | 可作为提示卡视觉候选；用于同类段落提示时需保持 9:16 竖屏、柔和展示牌、图二风格对照。 |
| `allowed_changes` | 可改标题、副标题、时长、留白、字体排版和配色细节。 |
| `blocked_if` | 把它写成全片背景 locked；卡片替代真实录屏主体；与用户已接受的 round34 中段结构冲突。 |
| `last_verified_at` | 2026-04-30 |
| `notes` | 该条补足背景 / 卡片风格散落口径，但仍是局部 candidate。 |

### 4.4 round34 功能卡 / 结果差卡候选参考

| 字段 | 值 |
| --- | --- |
| `reference_id` | `function_result_diff_card_round34_candidate_20260430` |
| `name` | round34 功能卡 / 结果差卡候选参考 |
| `type` | `function_card（功能卡）`; `result_diff_card（结果差卡）` |
| `status` | `candidate（候选参考）` |
| `confirmation_state` | `candidate_or_rule_reference（候选规则参考）` |
| `source_pr_or_log` | `dist/latest_review_pack/cut_map.md`; `GPT数据源/05_文案路由规则.md`; `GPT数据源/07_AI知识类视频价值规则.md`; PR #8 规则日志 |
| `artifact_path` | `dist/latest_review_pack/cut_map.md#shot06_result_diff_card` |
| `evidence_path` | `dist/latest_review_pack/cut_map.md`; `GPT数据源/05_文案路由规则.md`; `GPT数据源/07_AI知识类视频价值规则.md` |
| `confirmed_by` | `rule_evidence（规则证据）` |
| `confirmation_quote_or_record` | `已确认` round34 `shot06_result_diff_card（结果差提示卡）` 保留并负责收住判断；PR #8 记录三张骚萌卡启用时判断卡可合并进结果差卡；`待验证` 视觉母版尚未锁定。 |
| `applies_to` | 需要结果差证明点、功能判断、结论收束的少量 PPT / 卡片段落。 |
| `does_not_apply_to` | 骚萌卡搞笑职责；中段真实录屏主体；完整 visual master（视觉母版）。 |
| `inheritance_rule` | 结果差卡负责收住判断，不继续搞笑；功能卡 / 判断卡不得替代真实录屏证据。 |
| `allowed_changes` | 可调整文案、布局、信息密度、和 judgment_card（判断总结卡）的合并方式。 |
| `blocked_if` | 结果差卡变成骚萌卡；功能卡挤占录屏主体；没有结果差证明点却强行做卡。 |
| `last_verified_at` | 2026-04-30 |
| `notes` | 有职责规则，缺用户确认的统一视觉母版产物。 |

### 4.5 Prompt 引用尾卡规则候选参考

| 字段 | 值 |
| --- | --- |
| `reference_id` | `prompt_tail_card_rule_candidate_20260430` |
| `name` | Prompt 引用尾卡规则候选参考 |
| `type` | `ending（结尾）`; `prompt_tail_card（Prompt 引用尾卡）` |
| `status` | `candidate（候选参考）` |
| `confirmation_state` | `candidate_or_rule_reference（候选规则参考）` |
| `source_pr_or_log` | `GPT数据源/05_文案路由规则.md`; `GPT数据源/06_当前主线锚点_API生成真人_用户录制素材_少量PPT_云端剪辑.md`; `GPT数据源/08_当前正式事实.md`; `dist/latest_review_pack/cut_map.md` |
| `artifact_path` | `dist/latest_review_pack/cut_map.md#shot09_prompt_tail` |
| `evidence_path` | `GPT数据源/05_文案路由规则.md`; `GPT数据源/06_当前主线锚点_API生成真人_用户录制素材_少量PPT_云端剪辑.md`; `dist/latest_review_pack/cut_map.md` |
| `confirmed_by` | `rule_evidence（规则证据）` |
| `confirmation_quote_or_record` | `已确认` `Prompt 引用尾卡` 默认只承担产品单元引用 / 承接，不承担主叙事；round34 cut_map 记录 `shot09_prompt_tail` 不承担主叙事和中段证据。 |
| `applies_to` | 结尾总结之后的 Prompt / 工作包引用尾卡。 |
| `does_not_apply_to` | 主叙事、中段证据、结果差证明、完整低压结尾 locked。 |
| `inheritance_rule` | 仅作引用 / 承接，不重复讲结论，不替代主体内容。 |
| `allowed_changes` | 可调整尾卡文案、引用内容、展示时长和版式。 |
| `blocked_if` | Prompt 引用尾卡承担主叙事；重复讲结论；被写成完整 ending locked 视觉样板。 |
| `last_verified_at` | 2026-04-30 |
| `notes` | 当前是规则候选，缺锁定视觉产物。 |

### 4.6 语音样本2可爱女生向导音候选

| 字段 | 值 |
| --- | --- |
| `reference_id` | `voice_sample2_cute_guide_voice_candidate_20260426` |
| `name` | 语音样本2可爱女生向导音候选 |
| `type` | `tts_voice_base（TTS / 文本转语音声音底子）` |
| `status` | `candidate（候选参考）` |
| `confirmation_state` | `candidate_reference_pending_confirmation（候选参考待确认）` |
| `source_pr_or_log` | `codex_log/20260426_语音样本2复刻与文案风格解析.md`; `codex_log/20260426_语音样本2_audio_reference_report.md`; `GPT数据源/08_当前正式事实.md`; `codex_log/latest.md` |
| `artifact_path` | `dist/voice_trials/20260426_语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis/语音样本2_声音复刻试听_15秒.wav` |
| `evidence_path` | `dist/voice_trials/20260426_语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis/README.md`; `dist/voice_trials/20260426_语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis/run_summary.json`; `codex_log/20260426_语音样本2复刻与文案风格解析.md` |
| `confirmed_by` | `user_direction_record（用户方向记录）` |
| `confirmation_quote_or_record` | `已确认` 当前 vNext 声音目标收窄为 `可爱女生向导音`；新样本2 custom voice（自定义音色）脱敏标识可继续作为当前声音底子；`待验证` 该声音仍未完成最终听感复审。 |
| `applies_to` | TTS 声音底子候选、可爱女生向导音方向复审。 |
| `does_not_apply_to` | 最终音色 locked、TTS 内容验证通过、完整片最终音轨。 |
| `inheritance_rule` | 仅作为声音底子候选；与 `tts_15s_b_pacing_locked_20260427（B 版节奏锁定参考）` 配合时，必须区分“音色候选”和“节奏锁定”。 |
| `allowed_changes` | 可更换音色、重做复刻、调整降噪和后处理。 |
| `blocked_if` | 写成 final voice（最终音色）；写 `voice_validation（声音验证）= 通过`；把自定义音色候选当成 TTS 节奏 locked。 |
| `last_verified_at` | 2026-04-30 |
| `notes` | 声音底子仍是 candidate；节奏参考另见 B 版 locked。 |

## 5. failed_reference（失败参考）

### 5.1 PR #15 v2 字幕失败参考

| 字段 | 值 |
| --- | --- |
| `reference_id` | `subtitle_pr15_v2_failed_20260430` |
| `name` | PR #15 v2 字幕失败参考 |
| `type` | `subtitle（字幕）` |
| `status` | `failed（失败参考）` |
| `confirmation_state` | `failed_or_pending_reference（失败或待复盘参考）` |
| `source_pr_or_log` | PR #15 `AI 做 PPT 踩坑成品标准候选 v2`; `origin/codex/ai-ppt-pitfall-finished-candidate-v2-20260430:codex_log/20260430_AI做PPT踩坑成品标准候选v2.md`; 当前执行单用户反馈 |
| `artifact_path` | `origin/codex/ai-ppt-pitfall-finished-candidate-v2-20260430:复审包_review_packs/20260430_AI做PPT踩坑_成品标准候选_v2_ai_ppt_pitfall_finished_candidate_v2/AI做PPT踩坑_成品标准候选_v2_captions.srt` |
| `evidence_path` | `origin/codex/ai-ppt-pitfall-finished-candidate-v2-20260430:复审包_review_packs/20260430_AI做PPT踩坑_成品标准候选_v2_ai_ppt_pitfall_finished_candidate_v2/AI做PPT踩坑_成品标准候选_v2_review_manifest.md`; `origin/codex/ai-ppt-pitfall-finished-candidate-v2-20260430:复审包_review_packs/20260430_AI做PPT踩坑_成品标准候选_v2_ai_ppt_pitfall_finished_candidate_v2/AI做PPT踩坑_成品标准候选_v2_summary.json` |
| `confirmed_by` | `user_negative_feedback（用户负反馈）` |
| `confirmation_quote_or_record` | `已确认` 当前执行单记录用户认为 PR #15 v2 “字幕样式不是标准”。 |
| `applies_to` | 复盘 PR #15 v2 为什么不能作为字幕标准。 |
| `does_not_apply_to` | 后续完整成片默认字幕继承。 |
| `inheritance_rule` | 不得继承为字幕标准；后续字幕需另建或追回被确认的 `subtitle_reference（字幕参考）`。 |
| `allowed_changes` | 只能作为反例分析，不得作为默认样式微调起点，除非用户明确要求基于它修改。 |
| `blocked_if` | 把 PR #15 v2 字幕写成 locked；完整片沿用该字幕样式却声明继承通过。 |
| `last_verified_at` | 2026-04-30 |
| `notes` | PR #15 自评 candidate review 不等于用户确认。 |

### 5.2 PR #15 v2 layout / 背景风格失败参考

| 字段 | 值 |
| --- | --- |
| `reference_id` | `layout_pr15_v2_failed_20260430` |
| `name` | PR #15 v2 layout / 背景风格失败参考 |
| `type` | `visual_master（视觉母版）` |
| `status` | `failed（失败参考）` |
| `confirmation_state` | `failed_or_pending_reference（失败或待复盘参考）` |
| `source_pr_or_log` | PR #15 `AI 做 PPT 踩坑成品标准候选 v2`; 当前执行单用户反馈 |
| `artifact_path` | `origin/codex/ai-ppt-pitfall-finished-candidate-v2-20260430:复审包_review_packs/20260430_AI做PPT踩坑_成品标准候选_v2_ai_ppt_pitfall_finished_candidate_v2/layout_gate_report.md` |
| `evidence_path` | `origin/codex/ai-ppt-pitfall-finished-candidate-v2-20260430:复审包_review_packs/20260430_AI做PPT踩坑_成品标准候选_v2_ai_ppt_pitfall_finished_candidate_v2/layout_gate_report.md`; `origin/codex/ai-ppt-pitfall-finished-candidate-v2-20260430:复审包_review_packs/20260430_AI做PPT踩坑_成品标准候选_v2_ai_ppt_pitfall_finished_candidate_v2/quality_gates_report.md`; `origin/codex/ai-ppt-pitfall-finished-candidate-v2-20260430:复审包_review_packs/20260430_AI做PPT踩坑_成品标准候选_v2_ai_ppt_pitfall_finished_candidate_v2/AI做PPT踩坑_成品标准候选_v2_cut_map.md` |
| `confirmed_by` | `user_negative_feedback（用户负反馈）` |
| `confirmation_quote_or_record` | `已确认` 当前执行单记录用户认为 PR #15 v2 “背景风格被换掉”。 |
| `applies_to` | 复盘 PR #15 v2 layout / 背景为什么不能作为当前视觉母版标准。 |
| `does_not_apply_to` | 后续完整成片默认视觉母版继承。 |
| `inheritance_rule` | 不得继承为 `visual_master_reference（视觉母版参考）`；需要另行锁定已确认视觉母版。 |
| `allowed_changes` | 只能作为失败样本复盘。 |
| `blocked_if` | 把 PR #15 layout gate pass 写成用户确认；后续成片继续换背景风格且未授权。 |
| `last_verified_at` | 2026-04-30 |
| `notes` | layout gate 是候选审核工具输出，不代表最终内容 / 风格通过。 |

### 5.3 PR #15 v2 TTS 缺失失败参考

| 字段 | 值 |
| --- | --- |
| `reference_id` | `tts_pr15_v2_failed_20260430` |
| `name` | PR #15 v2 TTS 缺失失败参考 |
| `type` | `tts（TTS / 文本转语音）` |
| `status` | `failed（失败参考）` |
| `confirmation_state` | `failed_or_pending_reference（失败或待复盘参考）` |
| `source_pr_or_log` | PR #15 `AI 做 PPT 踩坑成品标准候选 v2`; 当前执行单用户反馈 |
| `artifact_path` | `origin/codex/ai-ppt-pitfall-finished-candidate-v2-20260430:复审包_review_packs/20260430_AI做PPT踩坑_成品标准候选_v2_ai_ppt_pitfall_finished_candidate_v2/AI做PPT踩坑_成品标准候选_v2_summary.json` |
| `evidence_path` | `origin/codex/ai-ppt-pitfall-finished-candidate-v2-20260430:复审包_review_packs/20260430_AI做PPT踩坑_成品标准候选_v2_ai_ppt_pitfall_finished_candidate_v2/AI做PPT踩坑_成品标准候选_v2_summary.json`; `origin/codex/ai-ppt-pitfall-finished-candidate-v2-20260430:复审包_review_packs/20260430_AI做PPT踩坑_成品标准候选_v2_ai_ppt_pitfall_finished_candidate_v2/quality_gates_report.md` |
| `confirmed_by` | `user_negative_feedback（用户负反馈）` |
| `confirmation_quote_or_record` | `已确认` 当前执行单记录用户认为 PR #15 v2 “没有 TTS”；PR #15 summary 也标记 `temporary_no_voice_preview（临时无声音预览）`。 |
| `applies_to` | 复盘无 TTS 候选片不能作为 TTS 参考。 |
| `does_not_apply_to` | 后续完整成片默认 TTS 节奏继承。 |
| `inheritance_rule` | 不得继承；完整成片若需要 TTS，必须读取已确认 TTS reference 或 blocked。 |
| `allowed_changes` | 可作为“缺失 TTS”反例记录。 |
| `blocked_if` | 后续完整片无 TTS 却声明 TTS 通过；把 temporary_no_voice_preview 写成 TTS reference。 |
| `last_verified_at` | 2026-04-30 |
| `notes` | 本条不是声音风格参考，是失败状态参考。 |

### 5.4 PR #15 v2 放大位置失败参考

| 字段 | 值 |
| --- | --- |
| `reference_id` | `zoom_pr15_v2_failed_20260430` |
| `name` | PR #15 v2 放大位置失败参考 |
| `type` | `zoom（录屏放大）` |
| `status` | `failed（失败参考）` |
| `confirmation_state` | `failed_or_pending_reference（失败或待复盘参考）` |
| `source_pr_or_log` | PR #15 `AI 做 PPT 踩坑成品标准候选 v2`; 当前执行单用户反馈 |
| `artifact_path` | `origin/codex/ai-ppt-pitfall-finished-candidate-v2-20260430:复审包_review_packs/20260430_AI做PPT踩坑_成品标准候选_v2_ai_ppt_pitfall_finished_candidate_v2/AI做PPT踩坑_成品标准候选_v2_cut_map.md` |
| `evidence_path` | `origin/codex/ai-ppt-pitfall-finished-candidate-v2-20260430:复审包_review_packs/20260430_AI做PPT踩坑_成品标准候选_v2_ai_ppt_pitfall_finished_candidate_v2/AI做PPT踩坑_成品标准候选_v2_contact_sheet.jpg`; `origin/codex/ai-ppt-pitfall-finished-candidate-v2-20260430:复审包_review_packs/20260430_AI做PPT踩坑_成品标准候选_v2_ai_ppt_pitfall_finished_candidate_v2/AI做PPT踩坑_成品标准候选_v2_cut_map.md` |
| `confirmed_by` | `user_negative_feedback（用户负反馈）` |
| `confirmation_quote_or_record` | `已确认` 当前执行单记录用户认为 PR #15 v2 “中段录屏放大位置对不上号”。 |
| `applies_to` | 复盘 PR #15 v2 zoom / crop（录屏放大 / 裁切）为什么不能作为放大方式参考。 |
| `does_not_apply_to` | 后续完整成片默认 zoom reference（录屏放大方式参考）。 |
| `inheritance_rule` | 不得继承 PR #15 v2 的 zoom / crop 方式；后续必须建立帧级 zoom reference 或 blocked。 |
| `allowed_changes` | 只能作为失败样本复盘。 |
| `blocked_if` | 沿用 PR #15 v2 放大位置；没有帧级对照却声明 zoom 继承通过。 |
| `last_verified_at` | 2026-04-30 |
| `notes` | 当前尚未定位正确 zoom locked reference。 |

## 6. gap_reference（缺口参考）

### 6.1 字幕标准缺失记录

| 字段 | 值 |
| --- | --- |
| `reference_id` | `subtitle_reference_missing_20260430` |
| `name` | 字幕标准缺失记录 |
| `type` | `subtitle_gap（字幕缺口）` |
| `status` | `failed_gap（失败缺口）` |
| `confirmation_state` | `failed_or_pending_reference（失败或待复盘参考）` |
| `source_pr_or_log` | 当前 registry 全量追回审计；PR #15 用户负反馈 |
| `artifact_path` | `待确认` |
| `evidence_path` | `codex_source/locked_reference_registry.md#subtitle_pr15_v2_failed_20260430`; 当前执行单 |
| `confirmed_by` | `user_negative_feedback（用户负反馈）` |
| `confirmation_quote_or_record` | `已确认` PR #15 字幕不是标准；`待验证` 未找到用户确认过的正确字幕样板。 |
| `applies_to` | 后续字幕修正、完整成片前置检查。 |
| `does_not_apply_to` | 任何默认字幕继承。 |
| `inheritance_rule` | 不得继承；后续必须先建立正确字幕样板。 |
| `allowed_changes` | 可补 artifact_path、evidence_path、字号、位置、背景、安全区、字幕密度和样片截图。 |
| `blocked_if` | 完整成片需要字幕但 registry 仍没有正确 subtitle_reference（字幕参考）；沿用 PR #15 字幕。 |
| `last_verified_at` | 2026-04-30 |
| `notes` | 这是缺口记录，不是 candidate 样板。 |

### 6.2 正确放大方式缺失记录

| 字段 | 值 |
| --- | --- |
| `reference_id` | `zoom_reference_missing_20260430` |
| `name` | 正确放大方式缺失记录 |
| `type` | `zoom_gap（录屏放大缺口）` |
| `status` | `failed_gap（失败缺口）` |
| `confirmation_state` | `failed_or_pending_reference（失败或待复盘参考）` |
| `source_pr_or_log` | 当前 registry 全量追回审计；PR #15 用户负反馈 |
| `artifact_path` | `待确认` |
| `evidence_path` | `codex_source/locked_reference_registry.md#zoom_pr15_v2_failed_20260430`; 当前执行单 |
| `confirmed_by` | `user_negative_feedback（用户负反馈）` |
| `confirmation_quote_or_record` | `已确认` PR #15 放大位置失败；`待验证` 未找到当前被确认的正确 zoom reference（录屏放大方式参考）。 |
| `applies_to` | 后续录屏放大修正、完整成片前置检查。 |
| `does_not_apply_to` | 默认 zoom 继承。 |
| `inheritance_rule` | 不得继承；后续必须建立帧级 zoom reference（录屏放大方式参考）。 |
| `allowed_changes` | 可补 frame（帧）、contact sheet（联系表）、时间码、裁切框和对照说明。 |
| `blocked_if` | 完整成片需要录屏放大但没有正确 zoom reference；沿用 PR #15 失败放大方式。 |
| `last_verified_at` | 2026-04-30 |
| `notes` | 这是缺口记录，不是 candidate 样板。 |

## 7. historical_reference（历史参考）

### 7.1 20260412 API demo clean 历史通过样片

| 字段 | 值 |
| --- | --- |
| `reference_id` | `historical_api_demo_clean_sample_20260412` |
| `name` | 20260412 API demo clean 历史通过样片 |
| `type` | `historical_video_sample（历史视频样片）` |
| `status` | `historical（历史参考）` |
| `confirmation_state` | `candidate_reference_pending_confirmation（候选参考待确认）` |
| `source_pr_or_log` | `codex_log/latest.md`; `GPT数据源/08_当前正式事实.md` |
| `artifact_path` | `dist/formal_api_demo_doubao_task_clear_20260412/local_review/final_review_clean.mp4` |
| `evidence_path` | `GPT数据源/08_当前正式事实.md`; 历史日志记录 |
| `confirmed_by` | `historical_user_acceptance（历史用户接受）` |
| `confirmation_quote_or_record` | `已确认` 该样片在 20260412 历史口径下曾被接受；`待验证` 不代表当前 vNext 完整成片默认母版。 |
| `applies_to` | 理解项目演化、历史 demo 口径和已跑通过的技术链路。 |
| `does_not_apply_to` | 当前 vNext 默认视觉母版、字幕标准、TTS 标准、骚萌卡标准或录屏放大标准。 |
| `inheritance_rule` | 只能作为 historical reference（历史参考）；不得自动继承为当前 locked reference（锁定参考）。 |
| `allowed_changes` | 可作为历史对照被引用。 |
| `blocked_if` | 把历史通过样片直接写成当前完整成片 locked visual master（视觉母版锁定参考）。 |
| `last_verified_at` | 2026-04-30 |
| `notes` | 历史通过不等于当前机制锁定。 |

## 8. 当前不得升级项

- `sassy_card_pr7_a_candidate_20260428（PR #7 A 版骚萌卡视觉候选）`：保持 `candidate（候选参考）`，因为未找到用户明确确认“以后骚萌卡视觉就按这个走”。
- `subtitle_pr15_v2_failed_20260430（PR #15 v2 字幕失败参考）`：保持 `failed（失败参考）`，因为用户指出字幕样式不是标准。
- `layout_pr15_v2_failed_20260430（PR #15 v2 layout / 背景失败参考）`：保持 `failed（失败参考）`，因为用户指出背景风格被换掉。
- `tts_pr15_v2_failed_20260430（PR #15 v2 TTS 缺失失败参考）`：保持 `failed（失败参考）`，因为用户指出没有 TTS。
- `zoom_pr15_v2_failed_20260430（PR #15 v2 放大位置失败参考）`：保持 `failed（失败参考）`，因为用户指出放大位置对不上号。
- `historical_api_demo_clean_sample_20260412（20260412 历史通过样片）`：保持 `historical（历史参考）`，因为历史通过不等于当前默认母版。

## 9. 当前仍需补证据的缺口

- `subtitle_reference（字幕参考）`：未找到正确字幕样板；后续必须建立标准字幕位置、字号、背景、安全区和对照截图。
- `zoom_reference（录屏放大方式参考）`：未找到正确放大样板；后续必须建立帧级 zoom reference。
- `visual_master_reference（视觉母版参考）`：已有体素元素娃娃方向和 round34 局部提示卡风格，但仍缺完整视觉母版锁定产物。
- `sassy_card_visual_reference（骚萌卡视觉参考）`：PR #7 A 版仍是候选，尚未锁定为默认视觉。
- `ending_reference（结尾参考）`：已有 Prompt 引用尾卡职责规则，但缺锁定视觉产物。

## 10. 更新规则

每次新增或修改 reference，必须同步更新：

1. 本 registry（登记表）。
2. 对应证据路径。
3. 对应执行日志。
4. 若升级为新聊天默认正式已知，必须同步回 `codex/user-readable-map（主读取分支）`。

升级为 `locked（锁定参考）` 时，必须保留：

- `confirmation_quote_or_record（确认依据）`
- `applies_to（适用范围）`
- `does_not_apply_to（不适用范围）`
- `inheritance_rule（继承方式）`
- `allowed_changes（允许修改范围）`
- `blocked_if（阻断条件）`

不得只写“已确认”。
