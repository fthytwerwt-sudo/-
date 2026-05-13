# Latest

## 20260514｜《AI 到底赚不赚钱》4:3 带 TTS 完整正片候选生成

- `已确认` 本轮生成《今天就说一个事：AI 到底能不能赚钱？》的 `4:3 带 TTS 完整正片候选`，不是字幕版技术样片，也不是纯技术预览。
- `输出目录`：`dist/20260514_AI到底赚不赚钱_4_3_final_candidate/`
- `full.mp4`：`dist/20260514_AI到底赚不赚钱_4_3_final_candidate/full.mp4`，`1440x1080`，时长 `243.85s`，`audio_present = true`，`decode_ok = true`，`technical_validation = passed`。
- `TTS / narration`：已生成 `dist/20260514_AI到底赚不赚钱_4_3_final_candidate/narration.wav`，共 `81` 个 TTS 分段，时长 `243.85s`，`pcm_s16le / 48000Hz / mono`，可被 `ffmpeg` 解码。
- `声音路线`：本轮使用项目既有安全 TTS 路线，目标模型 `qwen3-tts-vc-realtime-2026-01-15`，声音底子为脱敏 `qwen-t...ac19`；`voice_generation_validation = passed_for_generation_needs_human_review`。不得写成 `voice_validation = passed`，不得写成 `final_voice_validated = true`。
- `素材进入时间线`：三段用户真实录屏素材均已读取并进入时间线；`material_02` 承载粽子 / 婚纱样片，`material_01` 承载电商成本倒推，`material_03` 承载 Codex 本地项目执行系统。FocuSee 原始运镜按 `direct_cut_by_script` 保留，不做默认二次 zoom / crop / 重新运镜。
- `内容边界`：`10 分钟 / 22 元 / 半小时 / 20 多` 仍写为用户经验陈述，不写成素材画面直接证明；`material_03` 不写成 Codex 并发执行两个任务；不写 AI 自动赚钱，不写保证收益。
- `已生成` `content_route_card V2（内容路由卡 V2）`：`dist/20260514_AI到底赚不赚钱_4_3_final_candidate/content_route_card_v2.json`，包含开头路线、三段素材证据计划、FocuSee 中段策略、总结卡、TTS 计划和平台风险说明。
- `字幕 / 卡片`：已生成 `captions.srt`、原创梗图感开头、结尾 `judgment_card（判断卡）`；抽帧与安全区检查未发现字幕 / 卡片遮挡核心证据的 must-fix。
- `平台风险初查`：`risk_level = caution`；未命中 `hard_block` 或 `rewrite_required`。本轮已把高风险表达 `自动赚钱` 改写为安全否定表达；发布前仍需人工复审标题、描述和平台 AI 标识。
- `未读取 / 未写出`：未读取 `.env` / `.env.swp`，未打印或写出 API key、token、secret。
- `未修改`：用户原始三段素材、`dist/latest_review_pack/`、当前复审包状态文件、当前发布目标。
- `未推进`：`content_validation = pending_user_chatgpt_review`，`send_ready = false`，`publish_status = not_advanced`，`visual_master_locked`、`voice_validation`、`final_voice_validated` 均不推进。
- `日志`：`codex_log/20260514_ai_money_4_3_final_candidate_assembly.md`
- `下一个目标`：用户 / ChatGPT 对 `full.mp4` 做内容、声音和发布文案复审，决定是否只改一个变量进入下一轮。

## 20260514｜4:3 画面比例技术装配修正

- `已确认` 本轮只做《视频工厂｜OPC 一人公司 AI 闭环验证系统》的 4:3 画面比例技术装配修正，不做内容验证，不推进发布状态，不改原始素材，不调用外部 API。
- `当前目标对象`：仍以 `codex_log/current_publish_target.md` 指向的《我用 AI 做 PPT 踩过的坑》v3.1 / `dist/latest_review_pack/` 为当前复审对象；本轮不覆盖 `dist/latest_review_pack/`，只生成 4:3 技术验证输出。
- `素材验证`：锁定正式工作区内最新可读 FocuSee 4:3 素材 `/Users/fan/Documents/视频工厂/素材录制/内建视网膜显示器 2026-05-14 03-06-26.mp4`；`ffprobe` 结果为 `2498x1874`，比例 `1.332978`，判定接近 `4:3`。
- `已新增` `scripts/四比三装配验证_4_3_assembly_validation.py（4:3 装配验证脚本）`：本地读取素材宽高、阻断非 4:3 素材、以 `scale + pad` 输出 `1440x1080`，不做默认二次 zoom / crop / 重新运镜。
- `已生成` 本地技术验证输出：`dist/20260514_4_3_aspect_ratio_assembly_fix/4_3_assembly_validation_preview.mp4`，`ffprobe` 结果为 `1440x1080`，比例 `1.333333`，`technical_validation = passed_for_4_3_assembly`。
- `已生成` `content_route_card V2（内容路由卡 V2）`：`dist/20260514_4_3_aspect_ratio_assembly_fix/content_route_card_v2.json`，包含 `target_aspect_ratio = 4:3`、素材宽高、`screen_first_opening`、FocuSee 中段直接剪辑策略、字幕安全区和卡片不插入策略。
- `字幕 / 卡片安全区`：本轮技术验证输出未烧字幕、未插总结卡 / 反转卡 / 结果差卡 / Prompt 尾卡；V2 卡中记录后续 4:3 安全区建议，避免字幕或卡片压住中段真实证据。
- `未修改`：用户原始 FocuSee 素材、`dist/latest_review_pack/`、当前复审包状态文件、`.env`、`.env.swp`、API key、token、secret。
- `未推进`：`content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_status（发布状态）`、`voice_validation（声音验证状态）`、`final_voice_validated（最终声音验证状态）`、`visual_master_locked（视觉母版锁定）`。
- `状态边界`：本轮只可写成 `technical_validation = passed_for_4_3_assembly`；`content_validation = not_evaluated`，`send_ready = false`，不得写成内容过线或可发布。
- `日志`：`codex_log/20260514_4_3_aspect_ratio_assembly_fix.md`
- `下一个目标`：在下一轮真实内容执行中，用最终文案时间码把 4:3 FocuSee 素材切成正式段落，并按 4:3 安全区重新判断开头、字幕、卡片和证据窗口。

## 20260514｜content_route_card V2 与机制推理测试样例补全

- `已确认` 本轮只做《视频工厂｜OPC 一人公司 AI 闭环验证系统》的机制推理测试样例与 `content_route_card V2（内容路由卡 V2）` 输出模板补全，不生成视频，不修改媒体，不推进内容状态。
- `已更新` `codex_source/fixtures/mechanism_inference_function_cases.json（机制推理函数测试样例）`：在保留旧 6 个 case 的基础上新增 7 个 case，覆盖 FocuSee 直接剪辑、FocuSee 证据不清 blocked、梗图 GIF 开头、元素娃娃开头、反转卡位置、总结卡位置、卡片打断 FocuSee 证据窗口 blocked。
- `已更新` `GPT数据源/05_文案路由规则.md（文案路由规则）`：新增 `content_route_card V2（内容路由卡 V2）` 标准输出模板，一次性判断 `validation_goal / opening_route_decision / core_evidence / middle_carrier_decision / focusee_middle_editing_decision / card_placement_decision / api_human_usage / ppt_usage / prompt_tail_card_usage / flow_flex_reason / blocked_if`。
- `已轻量同步` `GPT数据源/11_项目状态动作总控器_机制推理层.md（项目状态动作总控器与机制推理层）`：明确 `content_route_card V2` 是 `content_route_inference_function（内容路由推理函数）` 的标准输出模板之一，fixture cases 是新增机制的最小验证样例。
- `已轻量同步` `codex_source/19_project_state_action_router.md（Codex 状态动作路由）`：命中内容执行、视频执行、开头路由、中段剪辑或卡片位置时，Codex 必须输出 `content_route_card V2` 或等效完整字段；缺关键判断不得直接生成视频。
- `已轻量同步` `codex_source/01_execution_rules.md（Codex 执行规则）`：涉及内容执行 / 视频执行 / 文案进入执行时，必须先生成 `content_route_card V2`；缺 `validation_goal / opening_route_decision / core_evidence / middle_carrier_decision / card_placement_decision / flow_flex_reason` 不得进入视频执行；素材来自 FocuSee 时必须额外填写 `focusee_middle_editing_decision`。
- `已轻量同步` `GPT数据源/03_总索引与阅读顺序.md（总索引与阅读顺序）`：补充 `content_route_card V2` 模板位置和覆盖范围，方便新会话从索引定位。
- `未修改`：`dist/latest_review_pack/`、视频 / 图片 / 音频 / 字幕 / 时间线 / TTS / 任何媒体产物、`GPT 数据源/` 历史静态目录。
- `未推进`：`content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_status（发布状态）`、`voice_validation（声音验证状态）`、`final_voice_validated（最终声音验证状态）`、`visual_master_locked（视觉母版锁定）`。
- `未调用`：DeepSeek / 阿里 / TTS / voice cloning / 图片生成 / 视频生成 API。
- `未读取`：`.env`、`.env.swp`、API key、token、secret。
- `状态边界`：fixture 样例写入和 V2 模板写入为 `已确认`；真实视频执行效果仍是 `待验证`，不得写成真实视频任务已验证通过。
- `日志`：`codex_log/20260514_content_route_card_v2_and_fixture_cases.md`
- `下一个目标`：下一条真实视频执行前，用 `content_route_card V2（内容路由卡 V2）` 验证 Codex / ChatGPT 能否一次性判断开头、中段、卡片、证据、API 人物、PPT、Prompt 尾卡和 blocked 条件。

## 20260514｜卡片位置路由机制补全

- `已确认` 本轮只做《视频工厂｜OPC 一人公司 AI 闭环验证系统》的卡片位置路由机制补全，不生成视频，不修改媒体，不推进内容状态。
- `已更新` `GPT数据源/05_文案路由规则.md（文案路由规则）`：新增 `card_placement_decision（卡片位置判断）`，明确总结卡、反转卡、结果差卡和 Prompt 尾卡是文案功能卡，不是固定 shot 模板。
- `已更新` `GPT数据源/07_AI知识类视频价值规则.md（AI 知识类视频价值规则）`：补充卡片只服务观众理解路径，不等于强证据；强证据仍来自用户录制素材、前后对比、步骤截图、结果截图或平台数据。
- `已更新` `GPT数据源/11_项目状态动作总控器_机制推理层.md（项目状态动作总控器与机制推理层）`：`content_route_inference_function（内容路由推理函数）` 接入 `copy_function / reversal_point / conclusion_point / result_diff_point / evidence_window_active / prompt_handoff_needed`，`editing_inference_function（剪辑推理函数）` 接入卡片是否打断证据窗口的判断。
- `已更新` `codex_source/19_project_state_action_router.md（Codex 状态动作路由）`：命中总结卡、反转卡、结果差卡或 Prompt 尾卡位置判断时，必须先输出 `card_placement_decision（卡片位置判断）`，不得固定旧 shot。
- `已更新` `codex_source/01_execution_rules.md（Codex 执行规则）`：视频执行前若涉及卡片位置，缺 `card_placement_decision` 不得直接生成视频；文案没有明确反转点不得强插反转卡，文案没有明确结论 / 下一步不得强插总结卡。
- `已轻量同步` `GPT数据源/06_当前主线锚点_API生成真人_用户录制素材_少量PPT_云端剪辑.md（当前主线锚点）`：修正 `Prompt 引用尾卡` 和结尾总结壳的固定位置误读，改为由 `card_placement_decision` 判断。
- `新规则`：总结卡位置跟随文案收束点、判断结论和下一步动作；反转卡位置跟随认知反转、错误示范、新旧对比和结果差转折；卡片不得抢中段真实录屏证据。
- `保留边界`：v3.1 / round34 / PR #7 B / cute_info_card_route / sassy_reaction_card_route 等历史 reference 只作为参考白名单或历史基线保留，不误删、不废弃、不升级成所有内容固定位置。
- `未修改`：`dist/latest_review_pack/`、视频 / 图片 / 音频 / 字幕 / 时间线 / TTS / 任何媒体产物、`GPT 数据源/` 历史静态目录。
- `未推进`：`content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_status（发布状态）`、`voice_validation（声音验证状态）`、`final_voice_validated（最终声音验证状态）`、`visual_master_locked（视觉母版锁定）`。
- `未调用`：DeepSeek / 阿里 / TTS / voice cloning / 图片生成 / 视频生成 API。
- `未读取`：`.env`、`.env.swp`、API key、token、secret。
- `状态边界`：卡片位置路由机制写入为 `已确认`；真实视频卡片位置长期效果仍是 `待验证`，不得写成已在真实视频任务中长期验证通过。
- `日志`：`codex_log/20260514_card_placement_route_fix.md`
- `下一个目标`：下一条真实内容执行前，用 `card_placement_decision（卡片位置判断）` 验证 Codex / ChatGPT 能否按最终文案、证据窗口和观众理解路径选择卡片类型与位置。

## 20260514｜开头路由机制补全

- `已确认` 本轮只做《视频工厂｜OPC 一人公司 AI 闭环验证系统》的开头路由机制补全，不生成视频，不修改媒体，不推进内容状态。
- `已更新` `GPT数据源/05_文案路由规则.md（文案路由规则）`：在 `content_route_card（内容路由卡）` 中新增 `opening_route_decision（开头路由判断）`，明确先判断开头路线，再执行开头。
- `已更新` `GPT数据源/04_选题与文案规则.md（选题与文案规则）`：选题进入主流程前必须判断开头路线；普通讲解 / 复盘 / 低压陪伴型选题可继续使用元素娃娃开头，争议 / 情绪 / 商业焦虑型且开头超过 `3s` 可优先考虑梗图 GIF 开场。
- `已更新` `GPT数据源/06_当前主线锚点_API生成真人_用户录制素材_少量PPT_云端剪辑.md（当前主线锚点）`：元素娃娃 / 可爱元素主持娃娃保留为合法 opening route，但不得理解成所有内容唯一默认开头。
- `已更新` `GPT数据源/07_AI知识类视频价值规则.md（AI 知识类视频价值规则）`：补充梗图 GIF 开头只负责抓眼、起情绪、抛问题，不算强证据；强证据仍来自用户录制素材、前后对比、步骤截图、结果截图或平台数据。
- `已同步` `GPT数据源/00_项目总述.md（项目总述）` 与 `GPT数据源/08_当前正式事实.md（当前正式事实）`：修正旧“开头人物壳默认统一”事实入口，避免新会话继续误判元素娃娃为所有内容默认开头。
- `已更新` `GPT数据源/11_项目状态动作总控器_机制推理层.md（项目状态动作总控器与机制推理层）`：`content_route_inference_function（内容路由推理函数）` 新增 `opening_duration`、`topic_emotion_level`、`controversy_level`、`evidence_start_strength`、`brand_consistency_need` 等输入信号，并新增四种 opening route 的状态与动作策略。
- `已更新` `codex_source/19_project_state_action_router.md（Codex 状态动作路由）`：Codex 执行侧命中开头路线、元素娃娃开头、梗图 GIF 开场或开头参考图时，必须先输出 `opening_route_decision`，不得绕过判断直接生成开头。
- `已更新` `codex_source/01_execution_rules.md（Codex 执行规则）`：涉及开头时，缺 `opening_route_decision` 不得直接生成视频；选择梗图 GIF 开头必须保留 reference contract / effect target / must_not_copy 边界；选择元素娃娃开头必须说明品牌一致性或轻陪伴理由。
- `已同步` `GPT数据源/01_项目系统提示词.md（项目系统提示词）`：修正系统提示入口中“开头人物壳默认统一”的旧句，避免新会话继续把元素娃娃误判为所有内容默认开头。
- `新规则`：元素娃娃开头保留为合法路线之一，不废弃；梗图 GIF 开场是条件优先路线，不是新唯一默认；开头 GIF 只负责 hook / ask，不负责 proof，不替代中段真实录屏证据。
- `reference 边界`：用户本轮上传抖音截图只继承“漫画冲击线 / 反应姿态 / 大字压屏 / GIF 感 / 快速抛问题”的开头机制，不复刻具体人物、头像、字体、构图或第三方可识别资产。
- `未修改`：`dist/latest_review_pack/`、视频 / 图片 / 音频 / 字幕 / 时间线 / TTS / 任何媒体产物、`GPT 数据源/` 历史静态目录。
- `未推进`：`content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_status（发布状态）`、`voice_validation（声音验证状态）`、`final_voice_validated（最终声音验证状态）`、`visual_master_locked（视觉母版锁定）`。
- `未调用`：DeepSeek / 阿里 / TTS / voice cloning / 图片生成 / 视频生成 API。
- `未读取`：`.env`、`.env.swp`、API key、token、secret。
- `状态边界`：开头路由机制写入为 `已确认`；真实视频开头效果长期稳定性仍是 `待验证`，不得写成已在真实视频任务中验证通过。
- `日志`：`codex_log/20260514_opening_route_mechanism_fix.md`
- `下一个目标`：下一条真实内容执行前，用 `opening_route_decision（开头路由判断）` 验证 Codex / ChatGPT 能否根据内容目标、时长、情绪、争议、证据强度和品牌一致性选择开头路线。

## 20260513｜FocuSee 中段剪辑职责机制修补

- `已确认` 本轮只做《视频工厂｜OPC 一人公司 AI 闭环验证系统》的 FocuSee 中段剪辑职责机制修补，不生成视频，不修改媒体，不推进内容状态。
- `已更新` `GPT数据源/05_文案路由规则.md（文案路由规则）`：新增 `3D-2. FocuSee 自带运镜录屏素材的中段剪辑边界`，明确 FocuSee 自带 `3D Motion（3D 运镜）` / 自动跟随 / 自动观看引导时，默认视为 `recording_layer_motion_baked_in（录制层运镜已内置）`。
- `已更新` `GPT数据源/11_项目状态动作总控器_机制推理层.md（状态动作总控器与机制推理层）`：`editing_inference_function（剪辑推理函数）` 新增 `direct_cut_required`、`keep_original_motion`、`no_secondary_zoom_by_default`、`secondary_zoom_allowed_only_if_evidence_unclear` 等状态与动作策略。
- `已更新` `codex_source/19_project_state_action_router.md（Codex 状态动作路由）`：Codex 执行侧同步 FocuSee 自带运镜素材的 `state_inference / action_policy / not_allowed` 规则。
- `已更新` `codex_source/01_execution_rules.md（Codex 执行规则）`：当素材标记为 `focusee_3d_motion_recording（FocuSee 3D 运镜录屏）` 或 `recording_layer_motion_baked_in（录制层运镜已内置）` 时，Codex 不得默认二次放大、裁切重构视角或把自动放大当成中段剪辑完成标准。
- `新规则`：FocuSee 自带运镜素材默认不再由 Codex 二次 zoom / crop / 重新运镜；Codex 改为按最终文案识别时间码、切分段落、删冗余、保留原始运镜、衔接口播 / 字幕 / 卡片。
- `允许例外`：只有 FocuSee 运镜未覆盖关键证据点、关键文字仍不可读、结果差未展示清楚，或用户明确要求二次剪辑增强时，才允许判断辅助放大 / 定格 / 卡片；仍不得破坏 FocuSee 原有运镜节奏或抢走真实录屏证据。
- `未修改`：`dist/latest_review_pack/`、视频 / 图片 / 音频 / 字幕 / 时间线 / 任何媒体产物、`GPT 数据源/` 历史静态目录。
- `未推进`：`content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_status（发布状态）`、`voice_validation（声音验证状态）`、`final_voice_validated（最终声音验证状态）`、`visual_master_locked（视觉母版锁定）`。
- `未调用`：DeepSeek / 阿里 / TTS / voice cloning / 图片生成 / 视频生成 API。
- `未读取`：`.env`、`.env.swp`、API key、token、secret。
- `状态边界`：FocuSee 录制层运镜职责边界写入为 `已确认`；真实视频任务长期效果仍是 `待验证`，不得写成已在真实 FocuSee 成片中长期验证通过。
- `日志`：`codex_log/20260513_focusee_middle_editing_route_fix.md`
- `下一个目标`：下一条使用 FocuSee 录屏素材的真实执行任务中，验证 Codex 是否能按文案直接剪辑并保留原始 3D 运镜，而不是默认二次放大。

## 20260512｜三大机制推理函数落地

- `已确认` 本轮在《视频工厂｜OPC 一人公司 AI 闭环验证系统》中一次性落地三大机制推理函数：`editing_inference_function（剪辑推理函数）`、`content_route_inference_function（内容路由推理函数）`、`quality_issue_classifier（质量短板分类器）`。
- `已更新` GPT Project / ChatGPT 侧最高机制入口：`GPT数据源/11_项目状态动作总控器_机制推理层.md`，三大函数均补齐 `input_signal -> observed_evidence -> state_inference -> action_policy -> validation_rule -> blocked_if -> feedback_update` 结构。
- `已更新` Codex 执行侧入口：`codex_source/19_project_state_action_router.md`，明确命中剪辑、内容承载、质量复审时，必须先输出对应推理函数；缺函数结果不得生成卡片 / 决策包，不得进入视频执行，不得写 `completed（已完成）`。
- `已更新` Codex 执行规则：`codex_source/01_execution_rules.md`，新增三大机制推理函数前置闸门，要求命中相关任务时先输出函数结果，并把 fixture / 最小样例纳入机制修补完成条件。
- `已同步` `GPT数据源/05_文案路由规则.md`：`content_route_card（内容路由卡）` 明确为 `content_route_inference_function（内容路由推理函数）` 的输出卡；`editing_decision_pack（剪辑决策包）` 明确由 `editing_inference_function（剪辑推理函数）` 推理后生成。
- `已同步` `GPT数据源/07_AI知识类视频价值规则.md`：`quality_lock_card（质量锁卡）` 必须调用 `quality_issue_classifier（质量短板分类器）`，先定位唯一最高优先级短板，再决定下一轮只改一个变量。
- `已同步` `codex_source/00_codex_readme.md`、`GPT数据源/10_OPC一人公司闭环与多AI协作机制.md`、`GPT数据源/01_项目系统提示词.md`、`GPT数据源/03_总索引与阅读顺序.md`，把三函数纳入默认接手、OPC 闭环、GPT Project 系统提示和总索引。
- `已新增` 最小测试样例：`codex_source/fixtures/mechanism_inference_function_cases.json`，覆盖三个函数各 2 个 case：正常判断 + blocked / human_review_required 判断。
- `已确认` 本轮是机制口径、路由口径、执行口径、验收口径补全；不是视频内容口径、发布状态口径、声音最终方案口径或商业化成立口径。
- `边界`：三大函数已写入并通过结构 / 关键词 / fixture 可解析检查后可作为后续任务前置机制；但长期真实任务稳定性仍是 `待验证`，不得写成机制长期稳定验证通过。
- `未修改`：`dist/latest_review_pack/`、视频 / 图片 / 音频 / 时间线 / 字幕 / TTS / 媒体产物、`GPT 数据源/` 历史静态目录。
- `未推进`：`content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_status（发布状态）`、`voice_validation（声音验证状态）`、`final_voice_validated（最终声音验证状态）`、`visual_master_locked（视觉母版锁定）`。
- `未调用`：DeepSeek / 阿里 / TTS / voice cloning / 图片生成 / 视频生成 API。
- `未读取`：`.env`、`.env.swp`、API key、token、secret。
- `日志`：`codex_log/20260512_三大机制推理函数落地_core_inference_functions_landing.md`
- `下一个目标`：用下一条真实内容执行或复审任务验证三大函数能否稳定阻断“只写动作名 / 只写卡片 / 技术通过当内容通过”的旧问题。

## 20260512｜参考到执行落地契约落地

- `已确认` 本轮在《视频工厂｜OPC 一人公司 AI 闭环验证系统》中正式落地 `Reference-to-Execution Contract（参考到执行落地契约）`。
- `已新增` GPT Project / ChatGPT 侧机制文件：`GPT数据源/12_参考到执行落地契约_reference_to_execution_contract.md`，把用户目标、reference、样片、原感稿、外部资料、视觉 / 声音 / 文案 / 剪辑参考转换成 Codex 可执行函数字段与可验收标准。
- `已新增` Codex 执行层机制文件：`codex_source/20_reference_to_execution_contract.md`，规定带 reference 的任务必须先输出 `reference_to_execution_contract`，没有契约不得执行，没有 `deviation_check（偏离检查）` 不得写 `completed（已完成）`。
- `已新增` 最小测试用例：`codex_source/fixtures/reference_to_execution_contract_cases.json`，覆盖 visual、editing、copywriting raw feeling、voice、quality sample、reference missing、state conflict、missing deviation check、Perplexity reference pack 共 9 个 case。
- `已同步` `GPT数据源/03_总索引与阅读顺序.md`、`GPT数据源/01_项目系统提示词.md`、`GPT数据源/10_OPC一人公司闭环与多AI协作机制.md`、`GPT数据源/11_项目状态动作总控器_机制推理层.md`、`codex_source/19_project_state_action_router.md`、`codex_source/00_codex_readme.md`、`codex_source/01_execution_rules.md`、`codex_source/18_deepseek_supply_request_schema.md`、`AGENTS.md`。
- `已确认` `DeepSeek / fallback` 供料包只可辅助携带 `reference_anchor`、`effect_targets`、`function_fields`、`deviation_check`、`done_when_contract`，不得替代正式 reference contract。
- `已生成` GPT Project 最新静态上传包：`/Users/fan/Documents/视频工厂/GPT_Project_上传包_OPC_20260512_reference_contract/`；上传包包含 `12_参考到执行落地契约_reference_to_execution_contract.md`、本轮 dated log、最新 `latest.md` 和当前本地产物路径索引。
- `边界`：本包只是 GPT Project 静态资料包，不代表用户已上传到 GPT Project UI，不代表 GPT Project UI 已同步成功，不代表内容验证通过，不代表 reference 机制长期执行效果已在真实视频任务中稳定验证。
- `未修改`：`dist/latest_review_pack/`、视频 / 图片 / 音频 / 时间线产物、`content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_status（发布状态）`、`voice_validation（声音验证状态）`、`final_voice_validated（最终声音验证状态）`、`visual_master_locked（视觉母版锁定）`。
- `未调用`：DeepSeek / 阿里 / TTS / voice cloning / 图片生成 / 视频生成 API。
- `未读取`：`.env`、API key、token、secret。
- `日志`：`codex_log/20260512_参考到执行落地契约落地.md`
- `下一个目标`：用下一次真实带 reference 的文案 / 视觉 / 剪辑任务验证 `Reference-to-Execution Contract（参考到执行落地契约）` 能否让 Codex 先拆效果目标和执行函数字段，再做偏离检查。

## 20260512｜项目状态动作总控器与机制推理层落地

- `已确认` 本轮把《视频工厂｜OPC 一人公司 AI 闭环验证系统》的最高机制层从审计蓝图落成可执行入口、可调用表、可验证字段、router fixtures 和 GPT Project 静态上传包。
- `已新增` GPT Project / ChatGPT 侧最高机制入口：`GPT数据源/11_项目状态动作总控器_机制推理层.md`，包含 `project_state_table`、`fact_source_arbitration_table`、`trigger_routing_table`、`mechanism_inference_template`、`completion_state_inference`、`feedback_update_rule` 和当前 `seed_state`。
- `已新增` Codex 执行层总控规则：`codex_source/19_project_state_action_router.md`，要求每轮在 `route_decision（路由判断）` 后、具体执行前输出 `state_action_router（项目状态动作总控器）`。
- `已新增` 最小路由测试用例：`codex_source/fixtures/project_state_action_router_cases.json`，覆盖截图 / 数据、最终文案、素材、Codex done、自觉不对、旧口径残留、灰度数据缺失、GPT Project 包落后、DeepSeek fallback 等 9 个场景。
- `已同步` `GPT数据源/03_总索引与阅读顺序.md`、`GPT数据源/01_项目系统提示词.md`、`GPT数据源/10_OPC一人公司闭环与多AI协作机制.md`、`codex_source/00_codex_readme.md`、`codex_source/01_execution_rules.md`、`AGENTS.md`，将最高机制入口从旧 `10 + 1` 口径升级为 `10 份基础执行包 + OPC 总纲 + 状态动作总控器`。
- `已生成` GPT Project 最新静态上传包：`/Users/fan/Documents/视频工厂/GPT_Project_上传包_OPC_20260512_state_router/`；上传包包含 `11_项目状态动作总控器_机制推理层.md` 与本轮 dated log。
- `边界`：本包只是静态资料包，不代表用户已上传到 GPT Project UI，不代表 GPT Project UI 已同步成功，不代表内容验证通过。
- `未修改`：`dist/latest_review_pack/`、视频 / 图片 / 音频 / 时间线产物、`content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_status（发布状态）`、`voice_validation（声音验证状态）`、`final_voice_validated（最终声音验证状态）`、`visual_master_locked（视觉母版锁定）`。
- `未调用`：DeepSeek / 阿里 / TTS / voice cloning / 图片生成 / 视频生成 API。
- `未读取`：`.env`、API key、token、secret。
- `日志`：`codex_log/20260512_项目状态动作总控器与机制推理层落地.md`
- `下一个目标`：把 `editing_inference_function（剪辑推理函数）` 落成同样的信号、状态、动作、验证和反馈链，让中段剪辑不再只停留在动作名。

## 20260512｜机制落地化审计与推理层蓝图

- `已确认` 本轮是《视频工厂｜OPC 一人公司 AI 闭环验证系统》机制落地化审计，不是视频执行、样片修改、内容验证推进或 DeepSeek / 阿里 / TTS API 调用。
- `已确认` 已生成审计报告：`codex_log/20260512_机制落地化审计与推理层蓝图.md`。
- `已确认` 本轮 Must read 文件全部 `read_ok`，当前分支为 `main`；未跟踪 `.env.swp` 未读取、未触碰、未纳入本轮改动。
- `机制落地性结论`：当前项目已有 14 个核心机制；约 4 个具备较完整或局部可执行推理链，约 10 个仍缺统一 `机制推理函数`。
- `P0`：`editing_decision_pack（剪辑决策包）` 已有动作枚举和字段，但缺“什么点该放大 / 不该放大 / 放大会不会切断上下文 / 素材不清时是否 blocked”的推理函数。
- `P0`：`content_route_card（内容路由卡）` 缺从内容类型、素材证据、结果差、平台风险推断承载结构、API 人物次数、PPT / 尾卡使用方式的函数。
- `P0`：`quality_lock_card（质量锁卡）` 缺质量短板归因函数，尚不能稳定判断问题在声音、节奏、剪辑、证据、画面、卡片密度还是人感。
- `部分成立`：`review_loop（复盘闭环）` 是当前最接近推理函数的机制，已有“数据 -> 短板层 -> 单变量动作 -> 指标验证”链条；但 V001 真实数据和缺失字段仍待回填。
- `蓝图`：建议新增 `Mechanism Inference Layer（机制推理层）`，包含 `trigger_router`、`signal_taxonomy`、`state_inference`、`action_policy`、`validation_rule`、`feedback_update` 六个模块。
- `未修改`：`dist/latest_review_pack/`、视频 / 图片 / 音频 / 时间线产物、`content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_status（发布状态）`、`voice_validation（声音验证状态）`、`final_voice_validated（最终声音验证状态）`、`visual_master_locked（视觉母版锁定）`。
- `未调用`：DeepSeek / 阿里 / TTS / voice cloning / 图片生成 / 视频生成 API。
- `未读取`：`.env`、API key、token、secret。
- `下一个目标`：先把 `editing_decision_pack（剪辑决策包）` 补成可执行的 `editing_inference_function（剪辑推理函数）`，让 Codex 能按“信号 -> 状态推测 -> 动作选择 -> 验证 -> 反馈更新”判断中段该放大什么、该保留什么、什么时候必须 blocked。

## 20260512｜GPT Project 最新版上传包生成

- `已确认` 已生成最新版 GPT Project 静态上传包：`/Users/fan/Documents/视频工厂/GPT_Project_上传包_OPC_20260512/`。
- `已确认` 上传包内包含 `上传说明_UPLOAD_MANIFEST.md（上传说明清单）`。
- `已确认` 本包包含 `GPT数据源/` 当前 10 + 1 基础执行包、最新 `codex_log/latest.md`、`Completion Relay Gate（补全接力闸门）` 机制修补日志、`项目残缺审计 project_gap_audit`、GPT Project 短路由说明和当前本地产物路径索引。
- `已确认` `codex_log/current_local_artifact_paths.md` 已将 `gpt_project_upload_package_canonical_path（GPT Project 上传包规范路径）` 更新为 20260512 新包；旧 20260509 包已降级为 `historical_previous_package_not_latest`。
- `状态边界`：本轮只生成静态上传包，不代表用户已上传到 GPT Project UI，不代表 GPT Project UI 已同步成功，不代表当前视频内容已通过，不代表 DeepSeek 长期稳定，不代表多 agent runtime 已跑通，不代表 v3.1 灰度测试完成。
- `未修改`：`dist/latest_review_pack/`、视频 / 图片 / 音频 / 时间线产物、`content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_status（发布状态）`、`voice_validation（声音验证状态）`、`final_voice_validated（最终声音验证状态）`、`visual_master_locked（视觉母版锁定）`。
- `未调用`：DeepSeek / 阿里 / TTS / voice cloning / 图片生成 / 视频生成 API。
- `未读取`：`.env`、API key、token、secret。
- `日志`：`codex_log/20260512_GPT_Project最新版上传包生成.md`
- `下一个目标`：用户将 20260512 新包上传到 GPT Project 后，GPT Project 静态资料与 GitHub `main` 当前机制、补全接力规则和项目残缺审计结果保持一致。

## 20260512｜项目残缺审计 project_gap_audit

- `已确认` 本轮是《视频工厂｜OPC 一人公司 AI 闭环验证系统》项目残缺审计，不是视频执行、样片修改、内容验证推进或 DeepSeek / 阿里 / TTS API 调用。
- `已确认` 已生成审计报告：`codex_log/20260512_项目残缺审计_project_gap_audit.md`。
- `已确认` 本轮 Must read 文件全部 `read_ok`，未发现 missing / unreadable。
- `P0`：`codex_log/current_publish_target.md` 仍残留旧分支 / 旧同步口径，和当前 `main` 主读取分支规则不一致。
- `P0`：v3.1 灰度测试 24h / 72h / 7d 数据仍未回填，无法判断 6000 播放基础门槛、短板层和下一轮唯一变量。
- `P1`：`V001_missing_fields.md` 未真实列出缺失字段，容易把“没有数据”误读成“没有缺失”。
- `P1`：`Completion Relay Gate（补全接力闸门）` 已写入，但长期执行效果仍需真实修补任务验证。
- `P1`：DeepSeek / `execution_supply_pack family` 仍不能写成稳定真实供料链路。
- `未修改`：`dist/latest_review_pack/`、视频 / 图片 / 音频 / 时间线产物、`content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_status（发布状态）`、`voice_validation（声音验证状态）`、`final_voice_validated（最终声音验证状态）`、`visual_master_locked（视觉母版锁定）`。
- `未调用`：DeepSeek / 阿里 / TTS / voice cloning / 图片生成 / 视频生成 API。
- `未读取`：`.env`、API key、token、secret。
- `当前机制状态`：审计报告写入与缺口分级为 `已确认`；`Completion Relay Gate（补全接力闸门）` 长期防止 Codex 做一半提前收工的效果仍是 `待验证`。
- `下一个目标`：先把 `current_publish_target.md` 的旧分支残留和 v3.1 `review_loop` 缺失字段显示修到不会误导新会话，再用这一轮修补反向验证 `Completion Relay Gate（补全接力闸门）` 是否能真正执行到底。

## 20260512｜Completion Relay Gate 补全接力闸门机制修补

- `已确认` 本轮是机制修补，不是视频执行、样片修改、内容验证推进或 DeepSeek / 阿里 / TTS API 调用。
- `已确认` 已新增 / 补强 `Completion Relay Gate（补全接力闸门）`，用于连接 `ChatGPT 横向补全`、`Codex 纵向细化`、`执行后剩余工作反查` 与 `日志 / 当前事实 / 入口规则同步`。
- `已确认` `codex_source/01_execution_rules.md（Codex 执行规则）` 已新增 `2E-2. Completion Relay Gate（补全接力闸门）`，强制输出 `completion_relay_gate`、`required_output_inventory`、`child_task_graph`、`remaining_work_check`、`sync_back_check`。
- `已确认` `codex_source/00_codex_readme.md（Codex 执行层总入口）` 已补入口规则：Codex 收到 ChatGPT 完整执行单 / 横向补全包时，必须先转成任务树和交付清单，执行后反查剩余工作与同步回写。
- `已确认` `GPT数据源/01_项目系统提示词.md（项目系统提示词）` 已补 `GPT -> Codex 补全接力规则`，明确 ChatGPT 横向补全、Codex 纵向拆解与执行到底。
- `已确认` `GPT数据源/10_OPC一人公司闭环与多AI协作机制.md（OPC 多 AI 协作机制）` 已补 `GPT -> Codex 补全接力机制`，明确 DeepSeek 只读供料，不替代 Codex 原文件复核与执行后反查。
- `已确认` `project_source/20_codex_multi_agent_routing_note_for_gpt_project.md（GPT Project 短路由说明）` 仍承担 GPT Project 侧短路由说明，本轮已补 Completion Relay Gate 触发提醒。
- `已确认` `AGENTS.md（仓库入口规则）` 已做轻量入口同步，只补机制入口引用，不改视频动态状态。
- `manual_structure_check`: `passed`
- `keyword_check`: `passed`
- `diff_scope_check`: `passed`
- `forbidden_status_check`: `passed_no_dynamic_status_promotion`
- `api_call_check`: `not_called`
- `secret_read_check`: `not_read`
- `media_generation_check`: `not_generated`
- `未修改`：`dist/latest_review_pack/`、视频 / 图片 / 音频 / 时间线产物、`content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_status（发布状态）`、`voice_validation（声音验证状态）`、`final_voice_validated（最终声音验证状态）`、`visual_master_locked（视觉母版锁定）`。
- `状态边界`：规则写入与结构检查为 `已确认`；长期执行效果仍是 `待验证`，不得写成机制长期稳定。
- `日志`：`codex_log/20260512_补全接力闸门机制修补.md`
- `下一个目标`：用下一次真实多文件执行单验证 `Completion Relay Gate（补全接力闸门）` 能否让 Codex 按任务树执行到底并在收尾前反查剩余工作。

## 20260510｜DeepSeek process env key 安全重跑通过

- `已确认` 已创建本地安全输入脚本：`scripts/run_safe_deepseek_stability_prompt.sh`。
- `已确认` 已通过 macOS Terminal 弹窗运行脚本，用户在 Terminal 内隐藏输入 `DEEPSEEK_API_KEY（DeepSeek API 密钥）`；Codex 对话框未接收 key。
- `已确认` 脚本只在当前进程临时 export key，测试结束后执行 `unset DEEPSEEK_API_KEY`。
- `request_file`: `codex_log/supply_requests/20260510_deepseek_stability_check_request.json`
- `supply_source`: `deepseek_passed`
- `fallback_status`: `not_used`
- `context_pack_validation`: `passed`
- `deepseek_generation_status`: `passed_with_retries`
- `deepseek_actual_participation`: `true`
- `blocked_reason`: `none`
- `env_file_read`: `false`
- `process_env_key_allowed`: `true`
- `process_env_key_present`: `true`
- `api_key_printed`: `false`
- `api_key_written`: `false`
- `key_written_to_env_file`: `false`
- `key_found_in_git_diff`: `false`
- `结果边界`：本轮只证明 DeepSeek 对这个稳定化 request 样例真实供料通过；不代表 DeepSeek 长期稳定真实供料，不代表 `multi-agent runtime（多 agent 运行时）` 已跑通，也不代表内容验证通过。
- `已确认` 本轮未调用阿里 API，未生成图片 / 视频 / 音频。
- `已确认` 本轮未修改发布状态、声音状态或内容验证状态，未推进 `content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_status（发布状态）`、`voice_validation（声音验证状态）` 或 `final_voice_validated（最终声音验证状态）`。
- `日志`：`codex_log/20260510_deepseek_process_env_rerun.md`
- `下一个目标`：进入一条真实文案的小范围素材计划执行，只做计划与供料验证，不调用阿里 API。

## 20260510｜DeepSeek 稳定化检查与 readiness 前置闸门

- `已确认` 本轮目标是稳定 DeepSeek 三态语义，不是强行证明 DeepSeek 每次成功。
- `已确认` 已新增稳定化 request：`codex_log/supply_requests/20260510_deepseek_stability_check_request.json`。
- `已确认` 已新增稳定化日志：`codex_log/20260510_deepseek_stability_check.md`。
- `已确认` 已补齐 `deepseek_readiness_check（DeepSeek 就绪检查）`：后续任何 DeepSeek 相关任务、`execution_supply_pack family（执行供料包族）`、reference / visual route / 多文件机制任务，都必须先输出该检查。
- `已确认` controller 现在稳定输出：
  - `deepseek_readiness_check`
  - `blocked_reason`
  - `env_file_read`
  - `process_env_key_allowed`
  - `process_env_key_present`
  - `not_deepseek_conclusion`
  - `deepseek_actual_participation`
- `已确认` explorer 已补齐 blocked 语义映射：
  - `blocked_missing_process_env_api_key`
  - `blocked_invalid_api_key`
  - `blocked_network_or_timeout`
  - `blocked_invalid_context_pack`
- `test_a_default_mode_supply_source`: `fallback_local_only`
- `test_a_default_mode_not_deepseek_conclusion`: `true`
- `test_b_process_env_key_present`: `false`
- `test_b_process_env_mode_supply_source`: `blocked`
- `test_b_context_pack_validation`: `blocked_missing_process_env_api_key`
- `test_b_deepseek_actual_participation`: `not_tested_missing_process_env_key`
- `blocked_reason`: `missing_process_env_api_key`
- `deepseek_real_supply_status`: `not_passed`
- `fallback_status`: `usable_with_fallback`
- `blocked_status`: `blocked_missing_process_env_key`
- `current_truth`: 当前进程环境没有 `DEEPSEEK_API_KEY`；本轮没有真实 DeepSeek passed，不能写成 DeepSeek 稳定供料。
- `py_compile`: `passed`
- `request_json_parse`: `passed`
- `schema_json_parse`: `passed`
- `forbidden_env_check`: `blocked_before_read`
- `forbidden_media_check`: `blocked_before_read`
- `forbidden_latest_review_pack_check`: `blocked_before_read`
- `env_file_read`: `false`
- `api_key_printed`: `false`
- `api_key_written`: `false`
- `ali_api_called`: `false`
- `image_generated`: `false`
- `video_generated`: `false`
- `已确认` 本轮未修改视频 / 声音 / 发布状态，未推进 `content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_status（发布状态）`、`voice_validation（声音验证状态）` 或 `final_voice_validated（最终声音验证状态）`。
- `边界`：`technical_validation（技术验证）` 只代表脚本、request 和禁止项回归通过；`mechanism_validation（机制验证）` 代表 readiness 与三态语义补齐；`deepseek_supply_validation（DeepSeek 供料验证）` 当前仍是 `blocked_missing_process_env_key`；`content_validation（内容验证）` 未验证且未改变。
- `下一个目标`：用户先把 `DEEPSEEK_API_KEY` 安全注入 process environment，再重跑本稳定化测试；若 DeepSeek passed，再进入一条真实文案的小范围素材计划执行，不调用阿里 API。

## 20260510｜真实文案全执行供料链测试与 DeepSeek 安全参与路径

- `已确认` 本轮找到仓库内真实口播文本入口：`dist/latest_review_pack/timeline.json` 的 `voice_text` 字段；本轮只读文本，不读取媒体文件。
- `已确认` 真实文案选择状态为 `closest_available_repo_copy`：它是当前 v3.1 基线时间线中最接近当前真实口播脚本的仓库文本入口。
- `已确认` 已新增真实文案全执行供料链测试日志：`codex_log/20260510_real_copy_execution_supply_chain_test.md`。
- `已确认` 测试包包含：
  - `content_route_card（内容路由卡）`
  - `visual_asset_requirement_pack（视觉素材需求包）`
  - `api_asset_generation_pack（API 素材生成包）`
  - `image_prompt_pack（图片 prompt 包）`
  - `asset_validation_pack（素材验收包）`
  - `assembly_decision_pack（装配决策包）`
  - `editing_decision_pack（剪辑决策包）`
  - `review_pack_test_summary（测试审片回流摘要）`
- `已确认` 已新增 request：
  - `codex_log/supply_requests/20260510_real_copy_execution_supply_chain_request.json`
  - `codex_log/supply_requests/20260510_safe_deepseek_process_env_request.json`
- `已确认` 已建立 DeepSeek 安全真实参与路径：controller 可在显式 `--allow-process-env-api-key` / `DEEPSEEK_ALLOW_PROCESS_ENV_KEY=1` 下，让 explorer 使用 process environment 中已有的 `DEEPSEEK_API_KEY`；同时 `DEEPSEEK_DISABLE_ENV_FILE=1` / `--no-env-file` 禁止读取 `.env`。
- `已确认` 安全路径边界：不读取 `.env`，不打印 key，不写 key，不把 key 放进 prompt / supply pack / manifest / log，只把 key 用作 HTTP Authorization。
- `real_copy_request_validation`: `passed`
- `real_copy_supply_source`: `fallback_local_only`
- `real_copy_not_deepseek_conclusion`: `true`
- `safe_test_A_default_supply_source`: `fallback_local_only`
- `safe_test_B_allow_process_env_supply_source`: `blocked`
- `safe_test_B_context_pack_validation`: `blocked_missing_process_env_api_key`
- `deepseek_actual_participation`: `not_tested_missing_process_env_key`
- `原因`：当前 shell 进程环境没有 `DEEPSEEK_API_KEY`；按本轮安全规则不得读取 `.env` 补救。
- `env_file_read`: `false`
- `api_key_printed`: `false`
- `api_key_written`: `false`
- `py_compile`: `passed`
- `schema_json_parse`: `passed`
- `request_json_parse`: `passed`
- `forbidden_env_check`: `blocked_before_read`
- `forbidden_media_check`: `blocked_before_read`
- `forbidden_latest_review_pack_check`: `blocked_before_read`
- `已确认` 本轮未调用阿里 API，未读取 API key，未生成真实图片 / 视频 / 音频。
- `已确认` 本轮未修改视频 / 声音 / 发布状态，未推进 `content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_status（发布状态）`、`voice_validation（声音验证状态）` 或 `final_voice_validated（最终声音验证状态）`。
- `边界`：本轮只是机制与真实文案小范围供料链测试，不代表阿里 API 图片生成链路已跑通，不代表 DeepSeek 稳定真实供料，不代表 `multi-agent runtime（多 agent 运行时）` 已跑通，不代表真实视频内容通过。
- `安全参与测试日志`：`codex_log/20260510_safe_deepseek_participation_test.md`
- `下一个目标`：如果需要验证真实 DeepSeek API 参与，先把 `DEEPSEEK_API_KEY` 安全注入为 process environment 后，重跑 `safe_deepseek_participation_test`；如果已完成安全注入，再进入一条真实文案的小范围素材计划执行，不调用阿里 API。

## 20260510｜全执行供料包族与 DeepSeek 双重补全测试

- `已确认` 本轮把 DeepSeek + Codex 配合从 `editing_decision_pack（剪辑决策包）` 扩展为 `execution_supply_pack family（执行供料包族）`。
- `已确认` 新增并接入以下供料 action：
  - `visual_asset_requirement_pack（视觉素材需求包）`
  - `api_asset_generation_pack（API 素材生成包）`
  - `image_prompt_pack（图片 prompt 包）`
  - `asset_validation_pack（素材验收包）`
  - `assembly_decision_pack（装配决策包）`
  - 保留并接入 `editing_decision_pack（剪辑决策包）`
- `已确认` action 已同步进入 `codex_source/17_deepseek_supply_controller_protocol.md`、`codex_source/18_deepseek_supply_request_schema.md`、`codex_source/schemas/deepseek_supply_request.schema.json` 和 `scripts/deepseek_supply_controller.py`。
- `已确认` `GPT数据源/05_文案路由规则.md` 已补全：`文案 -> 内容路由 -> 视觉素材需求 -> API 素材生成计划 -> 图片 prompt -> 素材验收 -> 装配决策 -> 剪辑决策 -> 审片回流`。
- `已确认` `GPT数据源/10_OPC一人公司闭环与多AI协作机制.md` 已同步 DeepSeek 只读供料范围；最终执行判断仍在 Codex，内容质量判断仍在 ChatGPT / 用户。
- `已确认` `GPT数据源/07_AI知识类视频价值规则.md` 已补充 AI / API 生成图片与真实证据边界：API 图只能辅助表达，不能冒充真实录屏证据。
- `已确认` Codex 第二层自动补全发现用户点名 fixture 未覆盖 `asset_validation_pack（素材验收包）`，本轮已补增对应 fixture。
- `已确认` 新增 fixtures：
  - `codex_source/fixtures/deepseek_supply_request_visual_asset_requirement_pack_example.json`
  - `codex_source/fixtures/deepseek_supply_request_api_asset_generation_pack_example.json`
  - `codex_source/fixtures/deepseek_supply_request_image_prompt_pack_example.json`
  - `codex_source/fixtures/deepseek_supply_request_asset_validation_pack_example.json`
  - `codex_source/fixtures/deepseek_supply_request_assembly_decision_pack_example.json`
  - `codex_source/fixtures/deepseek_supply_request_bad_forbidden_media_example.json`
  - `codex_source/fixtures/deepseek_supply_request_bad_forbidden_latest_review_pack_example.json`
- `py_compile`: `passed`
- `schema_json_parse`: `passed`
- `fixture_json_parse`: `passed`
- `controller_runs`: `file_map / editing_decision_pack / visual_asset_requirement_pack / api_asset_generation_pack / image_prompt_pack / asset_validation_pack / assembly_decision_pack = passed_with_fallback_local_only`
- `forbidden_env_check`: `blocked_before_read`
- `forbidden_media_check`: `blocked_before_read`
- `forbidden_latest_review_pack_check`: `blocked_before_read`
- `supply_source`: `fallback_local_only`
- `fallback_status`: `used`
- `not_deepseek_conclusion`: `true`
- `deepseek_actual_participation`: `false`
- `原因`：本轮禁止读取 `.env / secret`；controller 因此跳过会读取 `.env` 的 DeepSeek explorer，使用本地兜底供料。
- `dist 输出口径`：`dist/deepseek_supply_controller/*` 是本地运行产物，不作为 GitHub 主事实提交；GitHub 可追溯证据以 `codex_log/20260510_execution_supply_pack_test_evidence.md` 为准。
- `已确认` 本轮未调用阿里 API，未读取 API key，未生成真实图片 / 视频 / 音频。
- `已确认` 本轮未修改视频 / 声音 / 发布状态，未推进 `content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_status（发布状态）`、`voice_validation（声音验证状态）` 或 `final_voice_validated（最终声音验证状态）`。
- `边界`：本轮只是机制与供料样例测试，不代表阿里 API 图片生成链路已跑通，不代表 DeepSeek 稳定真实供料，不代表 `multi-agent runtime（多 agent 运行时）` 已跑通，不代表真实视频内容通过。
- `执行日志`：`codex_log/20260510_全执行供料包族与DeepSeek双重补全测试.md`
- `供料证据日志`：`codex_log/20260510_execution_supply_pack_test_evidence.md`
- `下一个目标`：用一条真实最终文案做小范围执行测试：让 Codex 基于文案先生成视觉素材需求、API 素材生成计划、图片 prompt、素材验收、装配决策和剪辑决策，但仍不直接生成完整大视频，先验证全执行供料链是否能减少漏项和误用素材。

## 20260510｜DeepSeek 深度配合与自动补全闸门

- `已确认` 本轮落地 `Auto-completion gate（自动补全闸门）`，用于阻断 Codex 只完成用户点名任务、遗漏上游判断、供料、三卡、执行中补缺口、执行后风险复核、日志回流或事实同步。
- `已确认` 自动补全闸门已写入 `codex_source/01_execution_rules.md（Codex 执行规则）`，后续触发任务必须输出 `auto_completion_gate` 字段，并检查 `goal_layer / judgment_layer / route_layer / trigger_layer / supply_layer / execution_layer / feedback_layer / validation_layer / sync_layer`。
- `已确认` 本轮新增 DeepSeek action：`editing_decision_pack（剪辑决策包）`，已同步进入：
  - `codex_source/17_deepseek_supply_controller_protocol.md`
  - `codex_source/18_deepseek_supply_request_schema.md`
  - `codex_source/schemas/deepseek_supply_request.schema.json`
  - `scripts/deepseek_supply_controller.py`
- `已确认` 新增可运行样例任务卡：`codex_source/fixtures/deepseek_supply_request_editing_decision_pack_example.json`。
- `已确认` `editing_decision_pack（剪辑决策包）` 只允许基于 Codex 提供的文字化素材样料供料，不直接读取视频、音频、图片或媒体文件，不剪视频，不拍板最终画面质量。
- `已确认` DeepSeek 深度配合流程已写入 `codex_source/17_deepseek_supply_controller_protocol.md`：`route_decision -> Auto-completion gate -> supply_request -> controller -> supply_pack -> Codex 读包 -> Codex 复核原文件 -> 执行 -> after_read_gap / risk_report 复核 -> latest / dated log 回流`。
- `已确认` OPC 上位机制已轻量同步：DeepSeek 仍是只读供料层，供料扩展到执行前文件地图、执行中缺口补读、执行后风险复核和视频执行现场 `editing_decision_pack（剪辑决策包）`；最终执行判断仍在 Codex，方向 / 内容 / 人感 / 下一轮变量仍由 ChatGPT / 用户拍板。
- `py_compile`: `passed`
- `schema_json_parse`: `passed`
- `fixture_json_parse`: `passed`
- `old_action_file_map_compatibility`: `passed`
- `editing_decision_pack_fixture_validation`: `passed`
- `editing_decision_pack_supply_source`: `deepseek_passed`
- `editing_decision_pack_context_pack_validation`: `passed`
- `editing_decision_pack_fallback_status`: `not_used`
- `forbidden_env_check`: `blocked_before_read`
- `forbidden_media_check`: `blocked_before_read`
- `forbidden_latest_review_pack_check`: `blocked_before_read`
- `已确认` 供料输出三件套存在：`dist/deepseek_supply_controller/latest_supply_pack.md`、`latest_supply_pack.json`、`latest_supply_manifest.json`。
- `已确认` manifest 已包含 `action = editing_decision_pack`、`request_validation_status = passed`、`supply_source = deepseek_passed`、`not_deepseek_conclusion = false`、`codex_next_input`。
- `已确认` 本轮只代表机制落地与最小样例验证；不代表 DeepSeek 已稳定真实供料，不代表 `multi-agent runtime（多 agent 运行时）` 已跑通，不代表真实视频剪辑任务已经验证通过。
- `已确认` 本轮未修改视频 / 音频 / 图片等媒体文件，未修改 `dist/latest_review_pack/`，未修改 `codex_log/current_publish_target.md`，未推进 `content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_status（发布状态）` 或声音状态。
- `执行日志`：`codex_log/20260510_DeepSeek深度配合与自动补全闸门.md`
- `下一个目标`：用一个真实小范围视频剪辑 / 录屏放大 / 卡片插入任务验证 `editing_decision_pack（剪辑决策包）` 是否真的能减少 Codex 漏读、误剪和硬套旧 SOP。

## 20260510｜DeepSeek 默认供料模型切换为 v4-flash

- `已确认` 本轮将 DeepSeek readonly explorer 默认供料模型从 `deepseek-v4-pro` 切换为 `deepseek-v4-flash`。
- `已确认` `deepseek-v4-pro` 保留为复杂任务升级模型 / 备用模型。
- `已确认` `.env.example` 已同步为 `DEEPSEEK_MODEL=deepseek-v4-flash`，并新增 `DEEPSEEK_ESCALATION_MODEL=deepseek-v4-pro`。
- `已确认` 本地 `.env` 存在且 `DEEPSEEK_API_KEY = present_nonempty`；本轮只把 `.env` 中 `DEEPSEEK_MODEL` 本地改为 `deepseek-v4-flash`，未打印 API key，未提交 `.env`。
- `smoke_test`: `passed`
- `smoke_test_model`: `deepseek-v4-flash`
- `已确认` 本轮只证明默认模型配置与最小 readonly explorer 链路通过，不代表 DeepSeek 已稳定供料，也不代表 `multi-agent runtime（多 agent 运行时）` 已跑通。
- `已确认` 本轮未修改视频产物、`dist/latest_review_pack/`、`content_validation`、`send_ready`、`publish_status`、声音状态。
- `执行日志`：`codex_log/20260510_DeepSeek默认模型切换为v4flash.md`
- `下一个目标`：用 `deepseek-v4-flash` 跑一次真实小步供料任务，观察是否比 Pro 更稳定或更快。

## 20260510｜视频质量与反馈总控机制 V1

- `已确认` 本轮落地 `视频质量与反馈总控机制 V1`，目标是把《视频工厂》从固定 SOP 倾向收束为“质量机制 + 文案路由 + 复盘反馈”的执行前判断机制。
- `已确认` 三张机制卡已进入执行前机制：
  - `content_route_card（内容路由卡）`
  - `quality_lock_card（质量锁卡）`
  - `review_variable_card（复盘变量卡）`
- `已确认` 已在 `codex_source/01_execution_rules.md（Codex 执行规则）` 写入 `DeepSeek + 三卡机制执行闸门`，后续视频 / 文案 / 复盘 / reference 相关任务必须在 `route_decision（路由判断）` 中判断供料与三卡需求。
- `已确认` DeepSeek / fallback 参与了执行前和执行后两次供料观察：
  - `preflight_request`: `codex_log/supply_requests/20260510_quality_feedback_mechanism_preflight_request.json`
  - `postcheck_request`: `codex_log/supply_requests/20260510_quality_feedback_mechanism_postcheck_request.json`
- `preflight_supply_source`: `fallback_local_only`
- `postcheck_supply_source`: `fallback_local_only`
- `fallback_status`: `used`
- `not_deepseek_conclusion`: `true`
- `deepseek_generation_unstable`: `true`
- `已确认` 本轮未修改视频 / 声音 / 发布状态，未推进 `content_validation（内容验证）`、`send_ready（可发送状态）`、`publish_status（发布状态）` 或声音状态。
- `已确认` 本轮不代表完整 `multi-agent runtime（多 agent 运行时）` 已完成，不代表机制已经被真实发布数据验证，也不代表 DeepSeek 已能稳定完成真实供料。
- `执行日志`：`codex_log/20260510_视频质量与反馈总控机制V1.md`
- `下一个目标`：用三卡机制跑一次真实内容 / 视频任务，不生成大视频，先做内容路由和复盘变量测试。

## 20260509｜DeepSeek 任务卡参与真实机制修正

- `已确认` 本轮新增真实 `supply_request（供料请求任务卡）`：`codex_log/supply_requests/20260509_reference_entry_supply_request.json`。
- `已确认` 已通过 `--request-file` 运行 `scripts/deepseek_supply_controller.py（DeepSeek 供料中控脚本）`，并读取 `dist/deepseek_supply_controller/latest_supply_pack.md`、`latest_supply_pack.json` 和 `latest_supply_manifest.json`。
- `supply_source`: `fallback_local_only`
- `request_validation_status`: `passed`
- `fallback_status`: `used`
- `not_deepseek_conclusion`: `true`
- `已确认` 已基于供料包和原文件复核，只在 `codex_source/00_codex_readme.md` 补强 `reference / locked reference / visual route / fixed_material_anchor / 旧 SOP 风险` 类任务优先走 `supply_request + controller` 的入口说明。
- `已确认` 本轮未修改 `GPT数据源/*`、DeepSeek 脚本、视频产物、`dist/latest_review_pack/`、`content_validation`、`send_ready`、`publish_status`、声音状态。
- `已确认` 本轮不代表 DeepSeek 已稳定供料，也不代表 `multi-agent runtime（多 agent 运行时）` 已跑通。
- `执行日志`：`codex_log/20260509_DeepSeek任务卡参与真实机制修正.md`
- `下一个目标`：下一轮可以用任务卡机制参与一个更真实的 Codex 执行任务。

## 20260509｜DeepSeek 供料请求任务卡机制

- `已确认` 本轮新增 `codex_source/18_deepseek_supply_request_schema.md（DeepSeek 供料请求结构说明）`，定义 DeepSeek 每次供料前必须读取的 `supply_request（供料请求任务卡）`。
- `已确认` 已新增 JSON Schema：`codex_source/schemas/deepseek_supply_request.schema.json`。
- `已确认` 已新增样例任务卡：`codex_source/fixtures/deepseek_supply_request_file_map_example.json`、`codex_source/fixtures/deepseek_supply_request_risk_report_example.json`。
- `已确认` `scripts/deepseek_supply_controller.py` 已支持 `--request-file`，并保持旧 CLI 参数兼容。
- `已确认` request validation 可阻断缺字段 / 非法 action / 非法 trigger / forbidden path；负向 `.env` 请求已 blocked，未读取 `.env`。
- `test_legacy_cli`: `fallback_local_only`
- `test_request_file_map`: `fallback_local_only`
- `test_request_file_risk_report`: `fallback_local_only`
- `negative_test_forbidden_env`: `blocked`
- `已确认` 供料包与 manifest 已写入 `request_id`、`request_validation_status`、`current_goal`、`current_step`、`known_context`、`missing_context`、`decision_needed`。
- `已确认` 本轮未修改业务机制正文、未修改视频产物、`dist/latest_review_pack/`、`content_validation`、`send_ready`、`publish_status`、声音状态。
- `已确认` 本轮不代表 DeepSeek 已稳定供料，也不代表 `multi-agent runtime（多 agent 运行时）` 已跑通。
- `执行日志`：`codex_log/20260509_DeepSeek供料请求任务卡机制.md`
- `下一个目标`：用标准 supply request 参与一次真实 Codex 机制修正任务。

## 20260509｜DeepSeek 供料中控最小机制

- `已确认` 本轮新增 `scripts/deepseek_supply_controller.py（DeepSeek 供料中控脚本）`，把 DeepSeek 从单次供料脚本升级为可触发、可回流、可兜底的最小中控入口。
- `已确认` 已新增 `codex_source/17_deepseek_supply_controller_protocol.md（DeepSeek 供料中控协议）`，写清触发机制、行动机制、范围机制和回流机制。
- `已确认` controller 支持 `file_map`、`risk_report`、`context_summary`、`missing_files`、`auto` 五类 action。
- `已确认` 输出回流路径为 `dist/deepseek_supply_controller/latest_supply_pack.md`、`latest_supply_pack.json`、`latest_supply_manifest.json`。
- `test_file_map`: `deepseek_passed`
- `test_risk_report`: `fallback_local_only`
- `pipeline_status`: `usable_with_fallback`
- `已确认` 本轮未修改业务机制正文、未修改视频产物、`dist/latest_review_pack/`、`content_validation`、`send_ready`、`publish_status`、声音状态。
- `已确认` 本轮不代表 DeepSeek 已稳定供料，也不代表 `multi-agent runtime（多 agent 运行时）` 已跑通。
- `执行日志`：`codex_log/20260509_DeepSeek供料中控最小机制.md`
- `下一个目标`：用 supply controller 参与一次真实 Codex 机制修正任务。

## 20260509｜reference 质量机制锁最小测试

- `已确认` 本轮用 `DeepSeek readonly explorer` 先为 `reference` 质量机制锁修正生成资料包，再由 `Codex` 做最小范围机制修正。
- `已确认` 本轮供料来源是：`fallback_local_only`，不是 DeepSeek 真实任务稳定生成通过。
- `已确认` 已在 `GPT数据源/10_OPC一人公司闭环与多AI协作机制.md`、`GPT数据源/06_当前主线锚点_API生成真人_用户录制素材_少量PPT_云端剪辑.md`、`GPT数据源/05_文案路由规则.md` 进一步写清：锁质量，不锁流程；文案驱动实时路由；`reference`、`locked reference`、`visual route` 不等于固定镜头 SOP。
- `已确认` 本轮未修改机制文件以外的项目正文，未修改视频产物、`dist/latest_review_pack/`、`content_validation`、`send_ready`、`publish_status`、声音状态。
- `执行日志`：`codex_log/20260509_reference质量机制锁最小测试.md`
- `下一个目标`：基于这次最小测试结果，继续推进 `reference` 质量机制锁修正的下一轮收口。

## 20260509｜DeepSeek 只读供料管线稳定性修复

- `已确认` 本轮把 `scripts/deepseek_readonly_explorer.py` 从单次最小调用扩展为稳定供料管线：加入输入压缩、三次受控重试、schema 校验和 local fallback。
- `已确认` smoke test 通过：`api_validation = passed`、`deepseek_generation_status = passed`、`context_pack_validation = passed`、`fallback_status = not_used`。
- `部分成立` 真实任务测试未拿到稳定 DeepSeek JSON，但 fallback 成功生成了 Codex 可读资料包。
- `real_task_pipeline_status`: `usable_with_fallback`
- `real_task_generation_status`: `failed`
- `real_task_context_pack_validation`: `fallback_local_only`
- `已确认` 当前可稳定给 Codex 提供资料，但这份真实任务资料包来自 local fallback，不是 DeepSeek passed。
- `已确认` 本轮未修改机制文件正文、未修改视频产物、`dist/latest_review_pack/`、`content_validation`、`send_ready`、`publish_status`、声音状态。
- `执行日志`：`codex_log/20260509_DeepSeek只读供料管线稳定性修复.md`
- `下一个目标`：再让 DeepSeek 供料，Codex 执行 `reference` 质量机制锁修正。

## 20260509｜DeepSeek 只读探索器最小真实任务测试

- `已确认` 本轮只做 DeepSeek readonly explorer 最小真实任务测试，不修改机制文件正文。
- `已确认` 为承载真实任务测试，`scripts/deepseek_readonly_explorer.py` 仅做了最小可逆扩展：支持 `--task`、`--context-file`，并把请求超时提高到 `60s`。
- `部分成立` DeepSeek 已进入真实低风险任务调用阶段，但本轮未产出有效上下文包。
- `deepseek_test_result`: `blocked`
- `原因`：真实任务测试中先后出现 `timeout`、`truncated_json`、`empty_content`；最终输出未能稳定形成四字段上下文包。
- `已确认` 本轮没有出现写文件越权、拍板项目事实或把多 agent runtime 写成已跑通的内容。
- `已确认` 本轮未修改机制文件正文、未修改视频产物、`dist/latest_review_pack/`、`content_validation`、`send_ready`、`publish_status`、声音状态。
- `执行日志`：`codex_log/20260509_DeepSeek只读探索器最小真实任务测试.md`
- `下一个目标`：根据这次 blocked 结果，决定是否进入“reference 质量机制锁”规则修正，或先继续收紧 readonly explorer 的任务输入与输出约束。

## 20260509｜DeepSeek 正式事实口径同步

- `已确认` 本轮只同步 `GPT数据源/08_当前正式事实.md` 的 DeepSeek 正式事实口径。
- `已确认` 已把旧口径 `DeepSeek API 尚未接入` 改写为当前已验证口径：`api_validation = passed`、`context_pack_validation = passed`、`model = deepseek-v4-pro`。
- `已确认` 已同步写清：这只代表 readonly explorer 最小 API 调用链和四字段上下文包结构验证通过，不代表多 agent runtime 已跑通。
- `已确认` 本轮没有重新修改脚本，没有重新推进视频、声音、发布状态，也没有把 `context_pack_validation = passed` 写成生产执行通过。
- `执行日志`：`codex_log/20260509_DeepSeek正式事实口径同步.md`
- `下一个目标`：用 DeepSeek readonly explorer 为一次真实 Codex 任务生成上下文包。

## 20260509｜DeepSeek readonly explorer 输出结构修复

- `已确认` 本轮修复 `scripts/deepseek_readonly_explorer.py` 的输出结构约束。
- `已确认` DeepSeek API 仍使用 `deepseek-v4-pro`。
- `已确认` 已启用 JSON Output，并要求四个顶层字段：`prefetch_context_pack`、`must_read_file_map`、`risk_and_conflict_report`、`candidate_summary`。
- `已确认` 脚本已对四个顶层字段做本地校验，缺任一字段即写 `context_pack_validation = failed_unexpected_output` 并返回非 0。
- `api_validation`: `passed`
- `context_pack_validation`: `passed`
- `已确认` 本轮未修改视频产物、`dist/latest_review_pack/`、`content_validation`、`send_ready`、`publish_status`、声音状态。
- `执行日志`：`codex_log/20260509_DeepSeek只读探索器输出结构修复.md`
- `下一个目标`：用 DeepSeek readonly explorer 为一次真实 Codex 任务生成上下文包。

## 20260509｜DeepSeek readonly explorer API 复测

- `已确认` 本轮只重跑 DeepSeek readonly explorer 最小 API 验证。
- `已确认` `.env` 存在，且 `DEEPSEEK_API_KEY = present_nonempty`；本轮未打印 API key。
- `已确认` 当前模型配置为：`deepseek-v4-pro`。
- `api_validation`: `passed`
- `context_pack_validation`: `failed_unexpected_output`
- `说明`：DeepSeek API 调用链已真实返回成功，但本轮生成的 `latest_prefetch_context_pack.md` 缺少 `risk_and_conflict_report` 与 `candidate_summary` 两个要求字段，因此还不能写成“有效上下文包已通过”。
- `已确认` 这只证明 DeepSeek readonly explorer 最小 API 调用通过，不代表多 agent runtime 已跑通。
- `已确认` 本轮未修改视频产物、`dist/latest_review_pack/`、`content_validation`、`send_ready`、`publish_status`、声音状态。
- `执行日志`：`codex_log/20260509_DeepSeek只读探索器API复测.md`
- `下一个目标`：修正 readonly explorer 输出结构约束后，再用 DeepSeek 为一次真实 Codex 任务生成完整上下文包。

## 20260509｜DeepSeek readonly explorer 模型锁定与最小验证

- `已确认` 已把 DeepSeek readonly explorer 默认模型锁定为：`deepseek-v4-pro`。
- `已确认` 已把 `.env.example` 示例变量更新为：`DEEPSEEK_BASE_URL=https://api.deepseek.com`、`DEEPSEEK_MODEL=deepseek-v4-pro`。
- `已确认` 已新增：
  - `codex_source/16_deepseek_readonly_explorer_rules.md`
  - `scripts/deepseek_readonly_explorer.py`
- `部分成立` 最小只读验证脚本已执行，并已生成本地验证输出：
  `dist/deepseek_readonly_explorer/latest_prefetch_context_pack.md`
- `待验证` 当前真实 API 调用未通过，因为本地 `.env` 中未检测到 `DEEPSEEK_API_KEY`；因此本轮不能写成 `DeepSeek readonly explorer API validation passed`。
- `已确认` 本轮未修改视频产物、`dist/latest_review_pack/`、代码逻辑、`content_validation`、`send_ready`、`publish_status`、声音状态。
- `执行日志`：`codex_log/20260509_DeepSeek只读探索器模型锁定与最小验证.md`
- `下一个目标`：用户先在 `.env` 中补齐 `DEEPSEEK_API_KEY`，再重跑 readonly explorer 最小 API 验证。

## 20260509｜GPT Project 上传包地址修复

- `已确认` 已审计 ChatGPT 之前给出的旧地址与 Codex 新上传包地址不一致问题。
- `已确认` 已生成唯一 GPT Project 上传包目录：
  `/Users/fan/Documents/视频工厂/GPT_Project_上传包_OPC_20260509/`
- `已确认` 以后 GPT Project 上传地址必须由 Codex 本地审计或 `current_local_artifact_paths.md` 给出，ChatGPT 不得凭记忆口头给地址。
- `已确认` 本轮未修改视频产物、代码、当前发布状态、`content_validation`、`send_ready`、声音产物。
- `执行日志`：`codex_log/20260509_GPT_Project上传包地址修复.md`
- `下一个目标`：用户使用 canonical upload package path 上传新版 GPT Project 资料包；上传后 ChatGPT 再按该包检查是否生效。

## 20260509｜OPC 入口读取口径收尾

- `已确认` 已把 `GPT数据源/10_OPC一人公司闭环与多AI协作机制.md` 加入 `AGENTS.md` 的《视频工厂》最小读取顺序。
- `已确认` 已把《视频工厂》正式来源从“10 份执行包”更新为“10 份基础执行包 + 1 份 OPC 总纲机制文件”。
- `已确认` 已把 OPC 上位身份、多 AI 协作分工、DeepSeek 只读供料层、Codex 唯一写入 Integrator、reference 机制锁同步回仓库总入口。
- `已确认` 本轮只修改仓库入口读取口径，未修改视频产物、代码、当前发布状态、`content_validation`、`send_ready`、声音产物。
- `执行日志`：`codex_log/20260509_OPC入口读取口径收尾.md`
- `下一个目标`：基于 OPC 新口径，重新设计内容选题与展示层；如用户确认，再进入 DeepSeek 只读供料层 API 接入验证。

## 20260509｜OPC 一人公司闭环与多 AI 协作机制升级

- `已确认` 本轮只修改项目口径 / 机制 / 路由文件，未执行视频产物、代码、DeepSeek API 或多 agent runtime。
- `已确认` 已新增 OPC 总纲机制文件：`GPT数据源/10_OPC一人公司闭环与多AI协作机制.md`。
- `已确认` 已把项目身份升级为：`OPC 一人公司 AI 闭环验证系统`。
- `已确认` 已把多 AI 协作写成默认架构：`ChatGPT（总控脑 / 判断层）`、`Codex（唯一写入执行层 / Integrator）`、`DeepSeek（只读供料层 / Explorer）`、`Perplexity（外部研究层）`。
- `已确认` 已把 DeepSeek 定义为只读供料层，不写文件、不拍板项目事实、不替代 Codex 验证。
- `已确认` 已保持 Codex 为唯一写入 `Integrator（统一执行者）`。
- `已确认` 已把 `reference（参考）`、`reference_quality_sample（参考质量样片）`、`locked reference（锁定参考）`、`visual route（视觉路由）` 从流程锁升级为机制判断锁：锁质量机制，不锁死固定流程。
- `已确认` 本轮未修改视频产物、声音 / TTS 产物、图片 / 卡片 / 素材产物、`dist/latest_review_pack/`、`content_validation`、`send_ready`、`publish_status`、`voice_validation`、`final_voice_validated`。
- `执行日志`：`codex_log/20260509_OPC一人公司闭环与多AI协作机制升级.md`
- `下一个目标`：基于 OPC 新口径，重新设计内容选题与展示层，并决定是否进入 DeepSeek 只读供料层 API 接入验证。

## 20260509｜口径一致性修复

- `已确认` 已把 `latest.md` 中的新口径继续收口到当前动态事实执行包核心文件里。
- `已确认` 当前唯一远端主线 / 默认主读取分支仍统一为：`main`；`codex/user-readable-map` 只保留在历史日志正文或显式历史分支引用说明里。
- `已确认` 当前项目中心价值仍统一为：`真实 AI 使用经验 + 工作提效实录`。
- `已确认` `场景化专业输出工作包` 仍只作为：`可选沉淀单元 / 产品化承接单元`，不是每条视频默认主目标。
- `已确认` 本轮未修改视频产物、`dist/latest_review_pack/`、`current_publish_target`、`content_validation`、`send_ready`、归档区或任何媒体文件。
- `治理报告`：`治理_reports/20260509_口径一致性修复_branch_and_value_consistency_fix/口径一致性修复报告_branch_and_value_consistency_fix_report.md`
- `执行日志`：`codex_log/20260509_口径一致性修复_branch_and_value_consistency_fix.md`
- `下一个目标`：结束口径修补，回到当前视频工厂主线内容验证与发布后复盘执行。

## 20260509｜main主线与项目中心价值口径统一

- `已确认` 当前唯一远端主线 / 默认主读取分支已统一为：`main`。
- `已确认` 当前项目中心价值已统一为：`真实 AI 使用经验 + 工作提效实录`。
- `已确认` `场景化专业输出工作包` 已降级为：`可选沉淀单元 / 产品化承接单元`，不再要求每条视频默认生成工作包。
- `已确认` 当前内容优先验证：真实经验、工作提效证据、真实录屏、前后变化、小样本平台反馈与发布后复盘。
- `已确认` 本轮未修改视频产物、`dist/latest_review_pack/`、`content_validation`、`send_ready` 或当前发布状态。
- `治理报告`：`治理_reports/20260509_main主线与项目中心价值口径统一_main_branch_and_value_alignment/main主线与项目中心价值口径统一报告_main_branch_and_value_alignment_report.md`
- `执行日志`：`codex_log/20260509_main主线与项目中心价值口径统一_main_branch_and_value_alignment.md`
- `下一个目标`：清理线结束后，回到当前视频工厂主线，继续围绕真实 AI 使用经验、工作提效实录与发布后复盘推进内容验证。

## 20260509｜最终收尾与 GitHub 分支清理

- `已确认` 本地收尾已完成：`GPT 数据源/10_样片参考质量规则_reference_quality_sample_rule.md` 已入库，工作树不再残留未跟踪规则文件。
- `已确认` 历史路径引用已收口：当前正式资料中涉及 `round28 voice clone trial` 的路径已改成 archive-only 外部目录口径；外部 archive 指针文件已存在。
- `已确认` 远端分支已按当前主线清理：当前保留 `main` 为唯一远端主线；`origin/HEAD -> origin/main` 仍作为符号引用存在。
- `说明`：脚本结果中的 `origin` 是远端伪引用，不是实际业务分支；删除返回 `remote ref does not exist`，已记入 blocked，但不影响主线清理完成。
- `治理报告`：`治理_reports/20260509_最终收尾_finalize_slimming_and_branch_cleanup/最终收尾报告_finalize_slimming_and_branch_cleanup.md`
- `下一个目标`：清理线结束，下一步可以回到视频工厂当前主线执行。

## 20260509｜一步瘦身

- `已确认` 已完成《视频工厂》主工作区一步瘦身。
- `已确认` 主工作区体积：`32G -> 1.1G`。
- `已确认` `.git` 体积：`21G -> 927M`。
- `已确认` `素材录制/`：`11G -> 55M`，仅保留当前语音样本锚点。
- `已确认` 已外移的大类：
  - `原始素材归档_raw_recordings_archive/`
  - `旧声音试配_voice_trials_archive/`
  - `旧参考包_reference_packs_archive/`
  - `旧媒体产物_old_media_outputs/`
  - `Git临时包归档_git_tmp_pack_archive/`
- `已确认` 当前仍保留在主工作区的核心对象：
  - `dist/latest_review_pack/` 当前正式入口
  - `dist/20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix/`
  - `复审包_review_packs/` 当前 v31 基线包与 reference 包
  - `素材录制/语音样本_04-25-2026 22-19-11_1.MP4`
  - `dist/voice_trials/20260426_语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis/`
  - `dist/voice_trials/20260427_十五秒文案语速停顿试配_15s_copy_pacing_trial/`
- `已确认` 外部 archive-only 目录：`/Users/fan/Documents/视频工厂归档+删除`
- `已确认` 本轮未删除任何业务文件，未做 history rewrite，未 force push。
- `治理报告`：`治理_reports/20260509_一步瘦身_one_pass_workspace_slimming/一步瘦身报告_one_pass_workspace_slimming_report.md`
- `执行日志`：`codex_log/20260509_一步瘦身_one_pass_workspace_slimming.md`
- `下一个目标`：清理并改写仍残留在正式资料中的历史路径引用，再决定是否继续外移最后 1 组历史 voice clone trial。

## 20260508｜主工作区与外部归档删除区分离

- `已确认` 已创建 archive-only 外部目录：`/Users/fan/Documents/视频工厂归档+删除`。
- `已确认` 已把以下旧媒体 / 旧产物 / 待确认大目录外移出主工作区：
  - `dist/reference_packs/20260427_中段吐槽插入风格_faithful_extract/`
  - `dist/voice_trials/20260425_round28_10s_voice_trial/`
  - `dist/voice_trials/20260426_台湾口语开心降噪试配_taiwan_happy_denoise_trial/`
  - `dist/完整成片_full_videos/`
  - `本地归档_local_archive/`
  - `素材检查_reports/20260429_文案样本节奏提取_copy_sample_rhythm_extract/`
  - `样片报告_sample_reports/`
  - `dist/prototypes/`
  - `dist/20260424_不放大完整可读_no_zoom_completeness/`
  - 内部 archive zone 中已归档的旧媒体 payload
- `已确认` 当前主工作区继续保留：
  - `dist/latest_review_pack/` 当前正式入口
  - `dist/20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix/`
  - `复审包_review_packs/` 当前 v31 基线包与当前 reference 包
  - `素材录制/`
  - `素材库_assets/`
- `已确认` `/Users/fan/Documents/视频工厂归档+删除` 只作为 archive-only 外部目录，不是执行工作区，不是 fresh clone，不是 worktree。
- `下一个目标`：清理并重写内部 archive 指针清单，让后续会话只把外部目录当归档池，不再把内部旧路径当真实存放位置。

## 20260508｜历史产物归档审计与迁移

- `已确认` 已完成第二轮历史产物扫描：`dist/`、`复审包_review_packs/`、`验证_reports/`、`样片报告_sample_reports/`、`素材检查_reports/`、`本地归档_local_archive/`。
- `已确认` 已迁移 1 组明确旧产物候选：`验证_reports/20260503_阿里云剪辑复接验证_after_audit_aliyun_editing_reconnect_validation/` -> `归档删除区_archive_delete_zone/旧产物候选_old_artifact_candidates/验证报告_legacy_validation_reports/...`
- `已确认` 已迁移 3 组本地未跟踪旧媒体输出到：`归档删除区_archive_delete_zone/旧图片视频产物_old_media_artifacts/local_untracked_media/dist/`
- `已确认` 当前继续保留不动：
  - `dist/latest_review_pack/` 当前正式入口
  - `dist/20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix/`
  - `复审包_review_packs/` 当前 v31 基线包与 reference 包
  - `素材录制/`
  - `素材库_assets/`
- `已确认` 本轮未删除任何文件。
- `治理报告`：`治理_reports/20260508_历史产物归档审计与迁移_old_artifacts_archive_audit/历史产物归档审计与迁移报告_old_artifacts_archive_audit_report.md`
- `执行日志`：`codex_log/20260508_历史产物归档审计与迁移_old_artifacts_archive_audit.md`
- `下一个目标`：先拆 `voice_trials/` 与 `reference_packs/` 的 current reference / pure history 边界，再做下一轮更细的历史产物迁移。

## 20260508｜主工作区与归档删除区分离

- `已确认` 已在唯一正式工作区 `/Users/fan/Documents/视频工厂` 内创建 `归档删除区_archive_delete_zone/`。
- `已确认` 已隔离旧口径：`project_source/07_current_formal_facts.md`。
- `已确认` 已隔离旧入口：`codex_source/00_current_repo_audit.md`、`codex_source/02_codex_index.md`、`codex_source/07_formal_api_demo_target_plan.md`。
- `已确认` 已隔离 `dist/latest_review_pack/` 中明确旧副本：
  - 全部 `AI做PPT踩坑_成品候选_v3_*`
  - `AI做PPT踩坑_成品候选_v31_review_manifest.md`
  - `AI做PPT踩坑_成品候选_v31_summary.json`
- `已确认` 当前 P0 / P1 保留不动：`GPT数据源/`、`review_loop/`、`dist/latest_review_pack/` 当前正式入口、当前代码 / 工作台执行层、`素材库_assets/`、`素材录制/`。
- `已确认` 本轮未删除任何文件。
- `治理报告`：`治理_reports/20260508_主工作区与归档删除区分离_main_vs_archive_delete_split/主工作区与归档删除区分离报告_main_vs_archive_delete_split_report.md`
- `执行日志`：`codex_log/20260508_主工作区与归档删除区分离_main_vs_archive_delete_split.md`
- `下一个目标`：先处理 `执行日志_codex_log/` 与 root demo 入口降权，再决定下一轮待归档 / 待删除候选。

## 20260508｜新老文件分区与旧口径污染源审计

- `已确认` 已完成《视频工厂》唯一正式工作区 `/Users/fan/Documents/视频工厂` 的“新老文件分区与旧口径污染源审计”。
- `已确认` 本轮只做只读审计 + 报告落库；未删除、未移动、未重命名任何文件，未修改 `dist/latest_review_pack/`、`current_publish_target`、`content_validation`、`send_ready`、`GPT 数据源/` 或 `GPT数据源/` 当前 10 份执行包。
- `已确认` 当前正式核心区已收束到：`AGENTS.md`、`codex_source/00_codex_readme.md`、`codex_source/01_execution_rules.md`、`codex_log/latest.md`、`codex_log/current_*`、`GPT数据源/`、`review_loop/`、`dist/latest_review_pack/` 与当前代码 / 工作台执行层。
- `已确认` 已发现高风险污染源：
  - `执行日志_codex_log/最新摘要_latest.md` 仍是直播项目旧摘要，但 `AGENTS.md` 默认执行规则仍提到它。
  - `project_source/07_current_formal_facts.md` 仍保留历史“通过 / 可直接发送”样片口径，且仍被 `project_source` 多个入口文件引用。
  - `codex_source/02_codex_index.md`、`00_current_repo_audit.md`、`07_formal_api_demo_target_plan.md` 仍保留启动期 / demo 导航语义。
  - `dist/latest_review_pack/` 内同目录并存当前灰测口径文件与旧 v3 / 旧 v3.1 副本文件。
- `治理报告`：`治理_reports/20260508_新老文件分区与旧口径污染源审计_file_partition_and_stale_context_audit/新老文件分区与旧口径污染源审计报告_file_partition_and_stale_context_audit_report.md`
- `执行日志`：`codex_log/20260508_新老文件分区与旧口径污染源审计_file_partition_and_stale_context_audit.md`
- `下一个目标`：先做入口级旧口径降权与引用修正，再决定哪些历史产物进入归档候选、哪些纯缓存对象进入删除候选。

## 20260505｜复盘到文案调整桥接

- `已确认` 已新增复盘到文案调整桥接规则：`review_loop/09_复盘到文案调整桥接_review_to_copy_revision_bridge.md`。
- `已确认` 已新增文案结构改版包模板：`review_loop/10_文案结构改版包模板_copy_revision_package_template.md`。
- `已确认` 已为 V002《自动流的最简单流程》生成复盘到文案调整桥接记录：`review_loop/records/V002_自动流的最简单流程_douyin_policy_notice/V002_复盘到文案调整桥接_review_to_copy_revision_bridge.md`。
- `已确认` 当前 V002b 仍是安全版文案结构草案，不是最终稿，不是已发布版本。
- `执行日志`：`codex_log/20260505_复盘到文案调整桥接_review_to_copy_revision_bridge.md`
- `下一个目标`：由 ChatGPT / 用户确认 V002b 文案结构，再决定是否进入录制 / 剪辑 / 发布前风险检查。

## 20260505｜发布前平台风险检查规则

- `已确认` 已基于 V002《自动流的最简单流程》新增发布前平台风险检查规则：`review_loop/08_发布前平台风险检查_pre_publish_platform_risk_check.md`。
- `已确认` V002 不再只作为单条数据记录，也作为第一条发布前平台风险样本；其身份仍是 `policy_distribution_limited（平台审核减推 / 分发受限）` 与 `abnormal_distribution_sample（异常分发样本）`，不是内容失败样本。
- `已确认` 后续 AI 工作流 / AI 教程 / 自动化流程 / 工具操作演示 / 命令行或 IDE 画面展示类视频，发布前必须先检查标题、封面、字幕、画面文字、工具界面、命令行、结尾动作、简介和评论区引导中的平台风险表达。
- `已确认` 已在 `review_loop/00_review_loop_readme.md` 与 `codex_source/00_codex_readme.md` 增加最小入口引用；未修改当前 v3.1 视频状态、`content_validation`、`send_ready`、`dist/latest_review_pack/`、`GPT 数据源/` 或 `GPT数据源/`。
- `执行日志`：`codex_log/20260505_发布前平台风险检查规则_pre_publish_platform_risk_check.md`
- `下一个目标`：后续发布类似 AI 工作流 / 自动化流程类视频前，先输出平台风险检查结果，再决定是否允许发布、必须改写或阻断。

## 20260505｜《自动流的最简单流程》抖音审核减推记录

- `已确认` 已为《自动流的最简单流程》建立独立 `video_id = V002` 发布后复盘记录，未混入 V001 v3.1 灰度测试记录。
- `已确认` 已记录抖音审核通知：`review_result = 减少作品推荐`，`violation_reason = 引导至风险不可控渠道`，`reason_surface = 画面`。
- `已确认` 已记录用户确认数据：播放量 39、点赞 5、收藏 8；计算字段为点赞率 12.82%、收藏率 20.51%、点赞 + 收藏动作率 33.33%。
- `已确认` V002 已标记为 `policy_distribution_limited（平台审核减推 / 分发受限）` 与 `abnormal_distribution_sample（异常分发样本）`；不得作为正常自然流量样本或内容失败结论。
- `已确认` 本轮未修改当前 v3.1 视频状态、`content_validation`、`send_ready`、`dist/latest_review_pack/`、`GPT 数据源/` 或 `GPT数据源/`。
- `执行日志`：`codex_log/20260505_抖音减少推荐审核记录_douyin_reduce_recommendation_notice.md`
- `下一个目标`：ChatGPT / 用户基于 V002 复盘输入判断该样本最终归为排除样本还是可参考异常样本，并拍板下一轮唯一优先改点是否锁定为发布包装 / 风险表达 / 画面触发点。

## 20260505｜大任务闸门 large_task_gate

- `已确认` 本轮只补 `large_task_gate（大任务闸门）` 机制；未修改视频产物、未生成样片、未继续项目清理、未调整剪辑风格、未开发真正 multi-agent 系统。
- `已确认` `AGENTS.md` 已在 `route_decision_gate（执行前路由闸门）` 后补 `### 2.6A 大任务闸门 large_task_gate`。
- `已确认` `codex_source/01_execution_rules.md` 已补 `## 2C. large_task_gate 大任务闸门`，并把 `large_task_gate` 加入 `route_decision（路由判断）` 输出字段。
- `已确认` 规则已写入：任何视频 / 样片 / 成片 / 剪辑对象超过 `3 分钟 / 180 秒`，必须触发 `large_task_gate（大任务闸门）`。
- `已确认` 规则已写入：多文件、多步骤、多验证、多模块，或“写文件 + 检查 + 日志 + push / 同步”等闭环任务，也必须触发 `large_task_gate（大任务闸门）`。
- `已确认` 触发后必须读取 `codex_source/13_execution_lane_and_parallel_rules.md` 与 `project_source/20_codex_multi_agent_routing_note_for_gpt_project.md`，并输出 `lane_recommendation` 与 `parallel_recommendation`。
- `已确认` 规则已明确：触发大任务闸门不等于自动多 agent，不等于默认并发；写入范围重叠、输出路径重叠、对象 / blocker / 验收未锁定时，必须保持或降级为 `serial_only（串行执行）`。
- `已确认` 本轮未修改 `dist/latest_review_pack/`、当前发布状态、`content_validation`、`send_ready`，未处理 `素材录制/`，未新建外部工作区，未执行 Git GC / prune / repack / LFS / history rewrite / force push。
- `执行日志`：`codex_log/20260505_大任务闸门_large_task_gate.md`
- `下一个目标`：后续 Codex 看到超过 3 分钟视频、多文件、多步骤、多验证任务时，先自动触发 `large_task_gate（大任务闸门）` 并完成 lane / parallel 判断。

## 20260505｜Codex 执行前路由闸门

- `已确认` 本轮只把《视频工厂》的 Codex 执行机制升级为 `route_decision_gate（执行前路由闸门）`；未修改视频产物、未生成样片、未继续清理、未处理 `素材录制/`。
- `已确认` `AGENTS.md` 已新增 `## 2.6 Codex 执行前路由闸门 route_decision_gate`，要求每次执行前先输出项目路由、任务类型、责任层级、必读文件、读取状态、允许 / 禁止修改范围、阻断条件和执行许可。
- `已确认` `AGENTS.md` 的默认执行规则已补入：执行前必须先输出并通过 `route_decision（路由判断）`；未通过前不得修改任何文件。
- `已确认` `codex_source/01_execution_rules.md` 已新增 `## 2A. 执行前 route_decision 闸门` 与 `## 2B. 任务类型与必读文件映射`。
- `已确认` 任务类型映射已覆盖：项目文件修改 / 机制修补 / 路由修补、视频样片 / 成片 / 样片回炉、文案写作 / 改写、复盘 / 诊断 / 审核、数据记录 / 灰度复盘、本地文件治理 / 工作区治理、execution lane / multi-agent / parallel 机制。
- `已确认` `codex_source/00_codex_readme.md` 已做最小同步：每次 Codex 执行前必须先通过 `route_decision（路由判断）`。
- `已确认` 本轮未修改 `dist/latest_review_pack/`，未修改当前发布状态、`content_validation`、`send_ready`，未新建外部工作区，未执行 Git GC / prune / repack / LFS / history rewrite / force push。
- `执行日志`：`codex_log/20260505_Codex执行前路由闸门_codex_route_decision_gate.md`
- `下一个目标`：后续新会话在任何文件修改或执行前，先给出 `route_decision（路由判断）` 与 `read_status（读取状态）`，再判断是否允许执行。

## 20260505｜fresh clone 外部目录收回与工作区锁死

- `已确认` 本轮只做 PR #50 fresh clone 审计目录收回与 `single_workspace_rule（单工作区硬规则）` 加固；未继续项目清理，未处理 `素材录制/`，未修改当前视频产物或发布状态。
- `已确认` 外部散目录 `/Users/fan/Documents/视频工厂_fresh_clone_audit_20260504` 已收回到唯一正式工作区内部：`/Users/fan/Documents/视频工厂/本地归档_local_archive/外部工作区回收_external_workspace_recovery_20260504/视频工厂_fresh_clone_audit_20260504`。
- `已确认` `/Users/fan/Documents/视频工厂_fresh_clone_audit_20260504` 已不再作为 `/Users/fan/Documents` 顶层散目录存在。
- `已确认` 回收目录大小约 `975M`，文件数 `633`，目录数 `100`；内部包含嵌套 `.git/`，仅作为归档内容保留，不提交、不当子模块处理。
- `已确认` `.gitignore` 既有规则已忽略 `本地归档_local_archive/`；`git status --short` 未出现 fresh clone 大目录待提交项，因此本轮未改 `.gitignore`。
- `已确认` 已同步加固 `AGENTS.md`、`codex_source/00_codex_readme.md`、`codex_source/01_execution_rules.md`：Codex 不得默认新建 fresh clone、audit clone、clean clone、临时 clone、外部对照 clone、临时 worktree 或任何外部工作区；确需外部目录必须先停止并等待用户明确确认。
- `已确认` 本轮未替换正式工作区，未删除正式工作区，未执行 `git gc` / `git prune` / `git repack`，未执行 Git LFS / history rewrite，未 force push，未修改 `content_validation` 或 `send_ready`。
- `执行日志`：`codex_log/20260505_fresh_clone外部目录收回与工作区锁死_workspace_lock_recovery.md`
- `下一个目标`：新会话默认只在 `/Users/fan/Documents/视频工厂` 唯一正式工作区内执行；如未来确需外部对照，先由 Codex 停止回报并等待用户明确确认。

## 20260504｜PR 合并与 fresh clone 体积对照验证

- `已确认` PR #48「Pre-upgrade delete old Video Factory assets」已合并到 `codex/user-readable-map`，merge commit：`d2df313920e1d7e4f720db279964d6a2324b06a1`。
- `已确认` PR #49「Audit Git history large files without cleanup」已合并到 `codex/user-readable-map`，merge commit：`a1981935e404a78377e121b0643601cad01e483a`。
- `已确认` PR #48 合并前已复核：`fixed_material_anchor（固定素材锚点）` 与 `reference_whitelist（参考白名单）` 已区分；TTS pacing / TTS voice 已区分；round34 中段最小参考、PR #7 B、cute card、TTS pacing、TTS voice candidate 均保留。
- `已确认` PR #49 合并前已复核：它是 Git 历史大文件只读审计，不包含 Git 清理、LFS 迁移、history rewrite 或发布状态修改。
- `已确认` fresh clone 已完成，目录为 `/Users/fan/Documents/视频工厂_fresh_clone_audit_20260504`，当前 checkout 分支为 `codex/user-readable-map`。
- `已确认` 正式工作区 `/Users/fan/Documents/视频工厂` 当前总大小约 `33G`，`.git` 约 `21G`，`.git/objects/pack` 约 `19G`，`素材录制/` 约 `11G`。
- `已确认` fresh clone 当前总大小约 `980M`，`.git` 约 `896M`，`.git/objects/pack` 约 `896M`。
- `已确认` 正式工作区 `.git/objects/pack/tmp_pack_*` 为 `28` 个，约 `15.49 GiB`；fresh clone `tmp_pack_*` 为 `0`，`git count-objects -vH` 显示 `garbage = 0`、`size-garbage = 0 bytes`。
- `结论`：正式工作区 `.git` 约 `21G` 主要来自当前本地 `tmp_pack_*` garbage；fresh clone 已显著变小，因此下一轮优先考虑 clean clone 迁移确认，不建议直接做 Git history rewrite。
- `已确认` 本轮未替换正式工作区，未删除正式工作区，未执行 `git gc` / `git prune` / `git repack` / `git lfs migrate` / `filter-repo` / `filter-branch` / BFG，未 force push，未修改当前发布状态。
- `已确认` `GPT 数据源/10_样片参考质量规则_reference_quality_sample_rule.md` 仍保持 `untracked / frozen / untouched`，本轮未纳入、未删除、未移动、未重命名、未修改。
- `治理报告`：`治理_reports/20260504_fresh_clone体积对照验证_fresh_clone_size_comparison/fresh_clone体积对照验证报告_fresh_clone_size_comparison_report.md`
- `下一个目标`：用户 / ChatGPT 复审 fresh clone 对照报告，再决定是否迁移到 fresh clone 工作区，或继续处理 `素材录制/` 原始素材。

## 20260504｜Git 历史大文件只读审计

- `已确认` 本轮从最新 `codex/user-readable-map` 创建只读审计分支：`codex/git-history-large-files-audit-20260504`。
- `已确认` 本轮只审计 `.git` 历史大文件来源；未删除、未移动、未重命名任何文件。
- `已确认` 未执行 `git gc`、`git prune`、`git repack`、`git lfs migrate`、`filter-repo`、`filter-branch`、BFG 或 force push。
- `已确认` `.git` 当前约 `21G`，`.git/objects` 约 `21G`，`.git/objects/pack` 约 `19G`，`.git/lfs` 不存在。
- `已确认` `git count-objects -vH` 报告 `size-garbage = 15.51 GiB`；`.git/objects/pack/tmp_pack_*` 临时包数量 `28`，合计约 `15.5 GiB`，是本地 `.git` 过大的最大直接来源。
- `已确认` 正式 pack 约 `3.99 GiB`，reachable 历史对象仍包含旧视频、旧音频、旧图片、旧复审包、旧 `dist/` 产物和历史 `node_modules/ffmpeg-static/ffmpeg`。
- `已确认` 当前工作树仍跟踪少量旧 `dist/` / `复审包_review_packs/` / `voice_trials` 媒体文件；本轮只记录，不做删除或迁移。
- `已确认` Git LFS 当前未安装 / 未配置，`.gitattributes` 不存在，本轮未做 LFS 迁移。
- `已确认` 已知冻结未追踪文件 `GPT 数据源/10_样片参考质量规则_reference_quality_sample_rule.md` 保持 `untracked / frozen / untouched`；本轮未纳入、未删除、未移动、未重命名、未修改。
- `推荐路线`：下一轮先做 fresh clone / clean clone 对照验证；如果远端历史仍大，再另起 Git LFS / history rewrite 方案。
- `治理报告`：`治理_reports/20260504_Git历史大文件只读审计_git_history_large_files_audit/Git历史大文件只读审计报告_git_history_large_files_audit_report.md`
- `下一个目标`：用户 / ChatGPT 复审 `.git` 历史大文件审计报告，再决定是否执行 Git LFS / 历史瘦身或重新 clone / 新建干净仓库。

## 20260504｜项目升级前旧资产清库

- `已确认` PR #48 追加清库口径修正：`v31_element_doll_opening_anchor（v3.1 元素娃娃开头锚点）` 是当前唯一 `fixed_material_anchor（固定素材锚点）`，但元素娃娃不是唯一 reference。
- `已确认` reference whitelist 仍保留：`PR7_B_骚萌反应页.png`、cute card、round34 中段剪辑 / 证据窗口、`tts_15s_b_pacing_locked_20260427`、`visual_route_map.json`、`locked_reference_registry.md`；后续按路径索引和 registry 复核后使用。
- `已确认` PR #48 追加 TTS reference whitelist 修正：TTS reference 分为 `tts_pacing_reference（TTS 节奏参考）` 与 `tts_voice_reference（TTS 语音 / 音色参考）`；`voice_sample2_cute_guide_voice_candidate_20260426` 与脱敏 custom voice `qwen-t...ac19` 保留为语音 / 音色候选参考，`target_model = qwen3-tts-vc-realtime-2026-01-15`，但 `voice_validation` 仍为 `pending_user_chatgpt_review`，`final_voice_validated` 仍为 `false`。
- `已确认` round34 旧 817M 本地大包未恢复；但 `dist/latest_review_pack/middle_preview.mp4`、`cut_contact_sheet.jpg`、`problem_windows/30_32s.mp4`、`problem_windows/30_32s_frames.jpg` 均仍存在，并已在路径索引恢复为 `path_exists = true`。
- `已确认` PR #47 已先合并到 `codex/user-readable-map`，合并提交：`20d9419e0a9ad048075a2138c610472df93051be`。
- `已确认` 本轮从合并后的主读取分支创建清库分支：`codex/pre-upgrade-delete-old-assets-20260504`。
- `已确认` 本轮不生成视频，不修改当前发布 / 灰度状态，不把 `content_validation` 写成 `passed`，不把 `send_ready` 写成 `true`。
- `已确认` 当前唯一固定素材锚点收束为：`v31_element_doll_opening_anchor（v3.1 元素娃娃开头锚点）`。
- `已确认` `v31_element_doll_opening_preview（v3.1 元素娃娃开头预览）` 只保留开头预览证据，不代表元素娃娃继续做全片主持。
- `已确认` PR #46 未合并、未关闭、未删除；当前只作为未来流程 / 教学 / 操作拆解类视频升级方向资料，不作为当前 reference。
- `已确认` `GPT 数据源/10_样片参考质量规则_reference_quality_sample_rule.md` 与整个 `GPT 数据源/` 目录本轮冻结不动。
- `已确认` 清理前工作区体积约 `36G`；清理后约 `33G`；释放约 `3G`。其中 `.git/` 约 `21G` 和 `素材录制/` 约 `11G` 本轮按禁止 / 不确定规则未动。
- `已确认` 清理后仍为约 `33G` 的主要原因是 `.git/（Git 系统目录）约 21G` 与 `素材录制/（用户录制原始素材）约 11G` 本轮按安全规则未动；下一轮若继续瘦身，必须分成两条独立任务：`Git 历史 / LFS 瘦身` 和 `原始录屏素材外置 / 删除确认`。
- `已确认` 已从 Git 当前树移除旧 `dist` 噪音目录，包括 20260414 / 20260417 旧视频产物、旧 demo、旧 latest 指针和 v3 dist 产物。
- `已确认` 已删除本地旧大目录 / 缓存：旧元素娃娃 1080P 复审包、旧本地归档、旧本地隔离区、旧 v1/v2/v3 复审包、旧视频样片缓存、临时产物、HyperFrames 测试输出、`node_modules`。
- `已确认` 已更新 `codex_log/current_local_artifact_paths.md`；v3 已删除路径不再保留 `path_exists = true`，round34 中段最小参考证据改用 `dist/latest_review_pack/` 现存文件并恢复为 `path_exists = true`。
- `待验证` `素材录制/` 仍为 blocked_unknown；如需进一步瘦身，需要用户另轮确认哪些原始录制素材可外置 / 删除。
- `治理报告`：`治理_reports/20260504_项目升级前旧资产清库_pre_upgrade_delete_old_assets/项目升级前旧资产清库报告_pre_upgrade_delete_old_assets_report.md`
- `下一个目标`：用户 / ChatGPT 复审清库 PR，确认没有误删保留内核；通过后再进入项目升级机制收口。

## 20260504｜元素娃娃开头保留与旧资产清理

- `已确认` 本轮从最新 `codex/user-readable-map` 创建分支：`codex/keep-element-doll-clean-old-assets-20260504`。
- `已确认` 已将 v3.1 元素娃娃开头锚点补入 `codex_log/current_local_artifact_paths.md`：`v31_element_doll_opening_anchor`。
- `已确认` 已将 v3.1 开头预览补入 `codex_log/current_local_artifact_paths.md`：`v31_element_doll_opening_preview`。
- `已确认` 两个路径均在唯一正式工作区 `/Users/fan/Documents/视频工厂` 内，本轮 `test -f` 验证存在。
- `边界`：元素娃娃只保留开头价值，不代表继续做全片主持，不替代录屏主体，不替代真人判断段。
- `已确认` PR #46 本轮降权为 `parallel_future_flow_teaching_asset（未来流程 / 教学 / 操作拆解类视频升级方向资料）`；本轮未合并、未关闭、未删除，不作为当前 reference，不写成主读取分支正式状态。
- `已确认` `GPT 数据源/10_样片参考质量规则_reference_quality_sample_rule.md` 本轮冻结不动，不纳入、不删除、不移动、不改名。
- `已确认` 已先输出 `cleanup_audit（清理审计）`，再删除 `.DS_Store` Finder 临时文件。
- `部分成立` 删除前原计划排除冻结 / 保护范围，但 `find -delete` 的执行行为导致部分受保护目录内 `.DS_Store` 也被删除；被额外影响的对象仅为 Finder 临时元数据，不是业务文件。
- `已确认` 本轮未生成视频、未修改 `dist/latest_review_pack/` 当前结构地图文件、未修改 `codex_log/current_publish_target.md` 状态字段、未删除任何核心 reference 或 blocked_unknown。
- `已确认` `content_validation` 未写成 `passed`，`send_ready` 未写成 `true`，`voice_validation` 未写成 `final`，当前 v3.1 发布 / 灰度状态未修改。
- `治理报告`：`治理_reports/20260504_元素娃娃开头保留与旧资产清理_keep_element_doll_cleanup_old_assets/元素娃娃开头保留与旧资产清理报告_keep_element_doll_cleanup_old_assets_report.md`
- `下一个目标`：用户 / ChatGPT 复审本轮 PR，确认元素娃娃开头路径索引补充无误、旧资产清理未误删；通过后再进入项目升级前的机制收口。

## 20260503｜阿里云剪辑复接验证 after audit

- `已确认` PR #34「接入 HyperFrames 三类卡片动效边界并审计阿里云剪辑」已合并到 `codex/user-readable-map`，合并提交：`edbe61e512c972d75c786a53f82c9e3db53ecfb2`。
- `已确认` PR #35 已关闭并标记 `Superseded`，未合并。
- `已确认` 本轮从合并 PR #34 后的最新 `codex/user-readable-map` 创建分支：`codex/aliyun-editing-reconnect-validation-after-audit-20260503`。
- `已确认` 已读取前置阿里云剪辑使用审计报告。
- `已确认` 阿里云 OSS + ICE / 云剪最小云端总装链路已真实跑通：OSS 上传、ICE 工程更新、云剪任务提交、轮询、MP4 导出均完成。
- `已确认` 导出样片本地下载后通过 `ffprobe`：12 秒，1080x1920，H.264，AAC。
- `候选判断`：阿里云剪辑可以作为 vNext 云端总装候选继续评估，但本轮不代表正式链路已稳定。
- `已确认` 本轮未修改 v3.1 正片，未修改 `dist/latest_review_pack/` 既有产物，未修改 `current_publish_target`。
- `已确认` 本轮未生成正式视频，未写新文案，未处理 HyperFrames 中段录屏。
- `已确认` 内容验证字段未提升为最终通过态；发送状态字段未提升；未将本地样片、签名链接、原始运行结果或敏感凭据提交进 Git。
- `验证报告`：`验证_reports/20260503_阿里云剪辑复接验证_after_audit_aliyun_editing_reconnect_validation/阿里云剪辑复接验证报告_after_audit_aliyun_editing_reconnect_validation_report.md`
- `下一个目标`：决定是否将阿里云剪辑作为 vNext 云端总装候选推进；若推进，先做 vNext 专用 timeline / manifest 设计和多素材兼容验证。

## 20260503｜HyperFrames 卡片动效边界与阿里云剪辑审计

- `已确认` 本轮从最新 `codex/user-readable-map` 创建分支：`codex/hyperframes-card-routing-and-aliyun-edit-audit-20260503`。
- `已确认` 本轮只做 HyperFrames 卡片动效接入规则设计与阿里云剪辑只读审计；未生成视频 / 音频 / 图片，未写新文案，未处理 HyperFrames 中段录屏接入。
- `已确认` 已先读取并核对 `dist/latest_review_pack/visual_route_map.json` 与 `visual_route_validation_report.json`；三类 HyperFrames 卡片动效均可挂回现有 route，未发现 route map 冲突。
- `已确认` 数据卡 / 结果差卡动效归属 `cute_info_card_route`，当前主要对应 `shot15_result_diff_card`；未来灰度数据卡 / 指标卡也只能作为该 route 扩展。
- `已确认` Prompt 引用尾卡动效归属 `cute_info_card_route`，对应 `shot16_low_pressure_ending`，只承担引用、低压收束和承接，不承担主叙事。
- `已确认` 骚萌卡动效版归属 `sassy_reaction_card_route`，对应 `shot03_problem_hook_sassy_card`、`shot05_negative_reversal_sassy_card`、`shot14_positive_reversal_sassy_card`，必须继承 PR #7 B 独立 reaction page 路线。
- `已确认` HyperFrames 当前只是 `card_motion_layer（卡片动效层）`，不是新视觉路由，不是中段录屏叠层，不是整条视频生成层，也不是云端剪辑替代品。
- `部分成立` 阿里云剪辑审计发现仓库仍保留阿里云 ICE / OSS 云端 assembly 代码路径和配置字段，也有历史云剪 / ICE 验证记录。
- `未发现当前实际调用证据` 当前 v3.1 `dist/latest_review_pack/` 未发现阿里云剪辑 / ICE assembly 调用记录；命中的阿里百炼内容属于 TTS / voice clone，不等于剪辑服务。
- `已确认` 本轮未修改 v3.1 正片，未修改 `dist/latest_review_pack/` 既有产物，`content_validation` 保持当前灰度测试口径，`send_ready` 保持 `false`。
- `治理报告`：`治理_reports/20260503_HyperFrames卡片边界与阿里云剪辑审计_hyperframes_card_boundary_aliyun_audit/HyperFrames卡片边界写入报告_hyperframes_card_boundary_report.md`
- `审计报告`：`治理_reports/20260503_HyperFrames卡片边界与阿里云剪辑审计_hyperframes_card_boundary_aliyun_audit/阿里云剪辑使用审计报告_aliyun_edit_usage_audit.md`
- `下一个目标`：ChatGPT 复审本轮 PR 是否可合并；若后续要处理阿里云剪辑保留 / 替换 / 降级，另起单独执行链路决策任务。

## 20260503｜Superpowers 历史工作区清理

- `已确认` PR #32「Enforce Video Factory single workspace cleanup」已 squash merge 到 `codex/user-readable-map`，合并提交：`2d7883a`。
- `已确认` 本轮从最新 `codex/user-readable-map` 创建分支：`codex/superpowers-worktree-cleanup-20260503`。
- `已确认` 本轮只处理两个指定 Superpowers 历史 worktree，不处理 HyperFrames 任务，不生成视频 / 音频 / 图片，不写新文案。
- `已确认` 两个 worktree 的 tracked diff、staged diff、untracked 文件数量均为 clean / `0`。
- `已确认` 两个 worktree 的 commit 均已存在于远端分支，没有未推送提交。
- `已确认` 本轮新增回收文件数量为 `0`，checksum 失败数量为 `0`。
- `已确认` 已执行普通 `git worktree remove` 移除两个历史 worktree；未使用 `--force`，未使用 `rm -rf`。
- `已确认` `git worktree list` 最终只剩 `/Users/fan/Documents/视频工厂`。
- `已确认` `/Users/fan/Documents` 顶层仍只剩 `/Users/fan/Documents/视频工厂`。
- `已确认` `content_validation` 保持发布后灰度测试口径，没有写成内容最终通过；`send_ready` 保持否定状态。
- `治理报告`：`治理_reports/20260503_superpowers工作区清理_superpowers_worktree_cleanup/superpowers_worktree_cleanup_report.md`
- `下一个目标`：后续所有《视频工厂》任务只允许在 `/Users/fan/Documents/视频工厂` 内执行。

## 20260502｜单工作区清理归档

- `已确认` 本轮从 `origin/codex/user-readable-map` 创建治理分支：`codex/single-workspace-cleanup-from-user-readable-map-20260502`。
- `已确认` `/Users/fan/Documents` 顶层《视频工厂》相关目录已清理到只剩：`/Users/fan/Documents/视频工厂`。
- `已确认` 已回收外部目录唯一文件 `442` 个，回收目标为 `/Users/fan/Documents/视频工厂/本地归档_local_archive/外部工作区回收_external_workspace_recovery_20260502/`。
- `已确认` 回收文件 size 与 checksum 全部一致；失败项 `0` 个。
- `已确认` 已安全 `git worktree remove` 干净外部 / 历史 worktree `18` 个；已将 `3` 个非 Git / 损坏临时残留目录移动到唯一工作区内部隔离区。
- `部分成立` `git worktree list` 仍保留 2 个 `/Users/fan/.config/superpowers/worktrees/视频工厂/...` 历史 worktree，因为它们有未跟踪文件，按安全规则标记 `blocked_need_user_review`，本轮未移除。
- `已确认` 已写入 `single_workspace_rule`：以后唯一正式工作区是 `/Users/fan/Documents/视频工厂`；新分支只能在此目录内创建 / 切换；不得默认创建 `/Users/fan/Documents/视频工厂_*` 外部工作区或外部 `git worktree add`。
- `已确认` `codex_log/current_local_artifact_paths.md` 已改为内部路径优先；所有 `canonical_local_path` 均指向 `/Users/fan/Documents/视频工厂` 内部；旧外部路径只保留为 `historical_source_path` 说明。
- `已确认` 本轮未生成视频 / 音频 / 图片，未写新文案，未处理 HyperFrames 卡片边界任务，未修改 v3.1 正片内容，未修改 `dist/latest_review_pack` 既有产物内容。
- `已确认` `content_validation` 未改成 `passed`，`send_ready` 未改成 `true`，本轮未永久删除未回收文件。
- `审计报告`：`治理_reports/20260502_单工作区清理归档_single_workspace_cleanup_archive/单工作区清理归档报告_single_workspace_cleanup_archive_report.md`
- `下一个目标`：用户确认两个 blocked superpowers 历史 worktree 后，另起一轮处理剩余 worktree；后续所有《视频工厂》任务只允许在 `/Users/fan/Documents/视频工厂` 内执行。

## 20260502｜截图数据录入与时间窗分桶机制

- `已确认` 本轮只修《视频工厂》v3.1 发布后灰度测试的数据记录机制；未写新文案、未生成视频、未生成音频、未重新装配全片、未修改 v3.1 视频产物。
- `已确认` 当前工作分支：`codex/v31-screenshot-data-buckets-20260502`。
- `已确认` 截图优先录入机制已接入既有 `review_loop/`，不新建重复复盘系统。
- `已确认` 新增截图录入规则：`review_loop/01_截图数据录入规则_screenshot_data_intake_rules.md`。
- `已确认` 当前 v3.1 视频已建立独立记录目录：`review_loop/records/V001_v31_AI做PPT踩坑_gray_test/`。
- `已确认` 当前 v3.1 主记录：`review_loop/records/V001_v31_AI做PPT踩坑_gray_test/V001_gray_test_record.md`。
- `已确认` 当前截图证据目录：`review_loop/screenshots/V001_v31_AI做PPT踩坑/`。
- `已确认` 旧记录 `review_loop/records/20260502_v31_AI做PPT踩坑_gray_test_record.md` 保留为兼容入口，并指向新的 V001 主记录目录。
- `已确认` 已新增按视频分桶：不同视频必须使用不同 `video_id` 和独立记录目录。
- `已确认` 已新增 `24h / 72h / 7d` 时间窗分桶：不同时间窗不得互相覆盖。
- `已确认` 已新增平台数据 / 留存完播 / 互动 / 账号增长 / 评论 / 私信 / 咨询 / 其他证据分类。
- `已确认` 已新增三份截图提取报告模板、缺失字段记录、给 ChatGPT 的复盘输入文件和 screenshot manifest。
- `已确认` 截图看不清或字段不确定时必须标记 `uncertain_need_human_check`；截图未提供字段必须标记 `missing`；不得硬猜。
- `已确认` Codex 后续只负责截图归档、字段提取、缺失标记、初检和交接；最终判断仍交给 ChatGPT / 用户。
- `已确认` PR #7 B 仍是后续骚萌卡唯一执行参考；PR #7 A 仍只作历史 / candidate 对照。
- `待验证` 发布平台、发布时间、视频链接、24h / 72h / 7 天截图和数据仍待用户提交。
- `下一个目标`：等待用户提交 v3.1 的 24h 截图；Codex 根据截图提取数据并更新 V001 记录；ChatGPT 根据四个复盘问题判断下一轮只改一个变量。

## 新会话接手建议先读

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_log/latest.md`
- `codex_log/current_publish_target.md`
- `codex_log/current_gray_test_target.md`
- `review_loop/00_review_loop_readme.md`
- `review_loop/01_截图数据录入规则_screenshot_data_intake_rules.md`
- `review_loop/07_v31灰度测试指标体系_v31_gray_test_metrics_v1.md`
- `review_loop/records/V001_v31_AI做PPT踩坑_gray_test/README_video_context.md`
- `review_loop/records/V001_v31_AI做PPT踩坑_gray_test/V001_gray_test_record.md`
- `review_loop/screenshots/V001_v31_AI做PPT踩坑/screenshot_manifest.md`
- `GPT数据源/08_当前正式事实.md`

## 20260502｜v3.1 灰度测试指标体系 V1 落仓库

- `已确认` 本轮只做 v3.1 发布后灰度测试指标体系 V1 落仓库，并接入既有 `review_loop/`；未写新文案、未生成视频、未生成音频、未重新装配全片、未修改 v3.1 视频产物。
- `已确认` 当前工作分支：`codex/v31-gray-test-metrics-v1-20260502`。
- `已确认` 当前状态仍为：`publish_status = gray_test_published`、`gray_test_status = active`、`current_phase = post_publish_gray_test`、`content_validation = gray_testing_not_final_passed`。
- `已确认` 新增指标体系文件：`review_loop/07_v31灰度测试指标体系_v31_gray_test_metrics_v1.md`。
- `已确认` 当前灰度测试目标文件：`codex_log/current_gray_test_target.md` 已更新为 24h / 72h / 7 天观察。
- `已确认` 当前 v3.1 单条记录：`review_loop/records/20260502_v31_AI做PPT踩坑_gray_test_record.md` 已补入 7 天播放目标、三类字段和四个复盘问题。
- `已确认` 7 天播放量 6000 是当前小样本阶段基础测试流量门槛，不是最终商业目标。
- `已确认` 指标体系不是运营数据大表，而是下一轮改动定位器。
- `已确认` 四层指标已写入：流量层、内容层、账号增长层、私域 / 客户转化层。
- `已确认` 字段已分为：核心必填字段、辅助观察字段、商业线索出现时才填字段。
- `已确认` 后续复盘默认收成四个问题：是否达到 6000 播放基础门槛、最短板在哪一层、下一轮只改哪一个变量、为什么先改它并看哪个指标。
- `已确认` Codex 在发布后复盘中只做记录、初检、归档和下一轮任务草稿；最终判断仍交给 ChatGPT / 用户。
- `已确认` PR #7 B 仍是后续骚萌卡唯一执行参考；PR #7 A 仍只作历史 / candidate 对照。
- `待验证` 发布平台、发布时间、视频链接、24h / 72h / 7 天数据均待用户回填。
- `下一个目标`：等待用户回填 24h / 72h / 7 天数据；回填后 Codex 做初检，ChatGPT 根据四个复盘问题判断下一轮只改一个变量。

## 新会话接手建议先读

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_log/latest.md`
- `codex_log/current_publish_target.md`
- `codex_log/current_gray_test_target.md`
- `review_loop/07_v31灰度测试指标体系_v31_gray_test_metrics_v1.md`
- `review_loop/records/20260502_v31_AI做PPT踩坑_gray_test_record.md`
- `review_loop/00_review_loop_readme.md`
- `GPT数据源/08_当前正式事实.md`

## 20260502｜v3.1 发片灰度测试与复盘机制接入

- `已确认` 本轮只做 v3.1 发片状态回写、灰度测试目标设定、既有 `review_loop/` 发布后复盘机制接入和仓库口径同步；不写新文案、不生成视频、不生成音频、不重新装配全片。
- `已确认` 当前工作分支：`codex/v31-gray-test-review-loop-20260502`。
- `已确认` 当前阶段已写入：`current_phase = post_publish_gray_test（发布后灰度测试阶段）`。
- `已确认` 当前发布状态已写入：`publish_status = gray_test_published（v3.1 已发片，进入灰度测试）`。
- `已确认` 当前灰度状态已写入：`gray_test_status = active（灰度测试中）`。
- `已确认` 当前发布后复盘要求已写入：`post_publish_review_required = true`。
- `已确认` 当前内容状态已写入：`content_validation = gray_testing_not_final_passed（灰度测试中，不等于内容最终通过）`。
- `已确认` 仍保持：`send_ready = false`、`visual_master_locked = false`、`voice_validation = pending_user_chatgpt_review`、`final_voice_validated = false`、`technical_upgrade_next = true`。
- `已确认` 发布后复盘默认接入既有 `review_loop/`，不新建独立灰度系统。
- `已确认` 新增当前灰度测试目标文件：`codex_log/current_gray_test_target.md`。
- `已确认` 新增 v3.1 单条灰度测试记录：`review_loop/records/20260502_v31_AI做PPT踩坑_gray_test_record.md`。
- `已确认` 24h / 72h、一次只改一个变量、小样本状态、异常样本处理、规律沉淀门槛沿用 `project_source/14_content_review_and_loop_governance_rules.md`。
- `已确认` PR #7 B 仍是后续骚萌卡唯一执行参考；PR #7 A 仍只作历史 / candidate 对照，不能作为后续执行参考。
- `待验证` 发布平台、发布时间、视频链接、24h 数据、72h 数据均待用户回填。
- `下一个目标`：等待用户补充发布平台、发布时间、视频链接和 24h 数据；24h 数据回填后，Codex 做初检，ChatGPT 做质量判断。

## 新会话接手建议先读

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_log/latest.md`
- `codex_log/current_publish_target.md`
- `codex_log/current_gray_test_target.md`
- `review_loop/records/20260502_v31_AI做PPT踩坑_gray_test_record.md`
- `review_loop/00_review_loop_readme.md`
- `GPT数据源/08_当前正式事实.md`

## 20260502｜v3.1 当前基线切换与旧 PR 降噪

- `已确认` 本轮只做当前基线切换、v3.1 有效产物回流、旧 PR 降噪和仓库口径同步；不重新生成视频、不重新生成音频、不重新生成图片、不重新装配全片。
- `已确认` 已从最新 `codex/user-readable-map` 创建工作分支：`codex/v31-current-baseline-sync-20260502`。
- `已确认` PR #24 不能原样合并：它基于 PR #22 head，会回退 PR #25 的旧口径归档与入口清理结果。
- `已确认` 已安全回流 PR #24 的 v3.1 有效产物：`dist/20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix/`、`复审包_review_packs/20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix/`、`dist/latest_review_pack/` 中的 v3.1 当前入口。
- `已确认` 当前最新视频基线切换为：`current_video_baseline = v3.1`。
- `已确认` 后续升级 / 修改 / 技术优化 / GPT 文案侧回炉默认基于：`future_iteration_base = v3.1`。
- `已确认` v3 只保留为历史候选 / 对照，不再作为后续默认修改基础。
- `已确认` v3.1 仍不可发送：`send_ready = false`。
- `已确认` v3.1 内容没有写成通过：`content_validation = pending_user_chatgpt_review_or_not_passed_copywriting_side`。
- `已确认` PR #7 B 版 `PR7_B_骚萌反应页.png` 是后续骚萌卡唯一执行参考；读不到 PR #7 B 必须 blocked，不得回退 PR #7 A。
- `已确认` PR #7 A 只保留为历史 / candidate 对照，不能再作为任何后续骚萌卡执行参考。
- `已确认` PR #22 / PR #23 / PR #24 均已写入降噪口径：不得直接合并，不得覆盖当前 v3.1 基线。

## 20260502｜仓库清理与旧口径归档

- `已确认` 本轮只做仓库清理、旧口径归档、入口口径重写和执行噪音删除；不生成 v3.1，不生成新视频，不生成新音频，不重新装配全片。
- `已确认` 已从 `codex/user-readable-map` 创建清理分支：`codex/repo-cleanup-old-context-20260502`。
- `已确认` 当前入口继续写明 v3 技术层为 `v3_technical_milestone = reached_for_current_stage`，技术线未锁定，下一步仍需技术升级。
- `已确认` v3 内容未过线，主要在 GPT 文案侧；`content_validation = not_passed_user_review_gpt_copywriting_side`，`send_ready = false`，`visual_master_locked = false`。
- `已确认` PR #7 B 仍是后续骚萌卡执行参考；读不到 PR #7 B 必须 blocked，不得回退 PR #7 A。
- `已确认` PR #7 A 已降权为历史 / candidate 对照；v3 生成时的 PR #7 A 痕迹已在 metadata 中标为 `legacy_generation_candidate_references`，不再放在可继承候选参考字段里。
- `已确认` 新增归档目录：`归档_archive/旧口径_old_context_20260502/`，归档 PR #22 原始待复审口径、PR #23 原始 PR #7 A 优先判断、可爱卡片旧 route suggestion。
- `已确认` 更新 `AGENTS.md`、`codex_source/00_codex_readme.md`、`codex_source/01_execution_rules.md`，明确归档目录只作复盘证据，不作为当前默认事实入口。
- `已确认` 本地原始脏工作区只删除 `dist/routeA_frame_*.png` 这 10 张未引用临时帧；素材、复审包、v3 证据、PR7_B、可爱卡片参考图均未删除。
- `已确认` 本轮必须 commit、push、创建 PR，并在验证通过后合并到 `codex/user-readable-map`，合并后清理口径才算新聊天默认正式已知。

## 20260501｜v3 技术里程碑与 v3.1 视觉参考锁定

- `已确认` 本轮只做仓库口径回写、reference registry 修补、v3.1 视觉路由前置规则同步和主读取分支回流；未生成 v3.1、未生成新视频、未生成新音频、未重新装配全片。
- `已确认` 用户已复审《我用 AI 做 PPT 踩过的坑》v3：技术层只能写为 `v3_technical_milestone = reached_for_current_stage（当前阶段技术里程碑达成）`，不得写成技术线最终锁定。
- `已确认` 下一步仍需要 `technical_upgrade_next = true（技术升级）`，`technical_baseline_locked = false（技术基线未锁定）`。
- `已确认` v3 内容未过线，主要问题在 GPT 文案侧；状态写为 `content_validation = not_passed_user_review_gpt_copywriting_side`，不得写 `passed` 或仅写 `pending_user_chatgpt_review`。
- `已确认` `send_ready = false`，`visual_master_locked = false`，`visual_master_candidate = true`。
- `已确认` PR #7 B 版 `PR7_B_骚萌反应页.png` 已写为后续骚萌卡执行参考；读不到 PR #7 B 必须 `blocked`，不得回退 PR #7 A。
- `已确认` PR #7 A 保留为历史 / candidate 对照，不删除、不升级 locked、不再作为下一轮 v3.1 后续骚萌卡执行参考。
- `已确认` 新增 route-level locked references：`sassy_card_pr7_b_visual_locked_20260501`、`cute_prompt_card_route_locked_20260501`、`cute_info_card_route_locked_20260501`。
- `已确认` 新增 v3.1 前置规则文件：`codex_source/15_v31视觉路由规则_v31_visual_routing_rules.md`。
- `已确认` 下一轮 v3.1 必须先输出并验证 `visual_route_map.json（视觉路由表）`；route map 通过前不得生成全片。
- `已确认` 三条视觉路由已写清：`cute_prompt_card_route（可爱段落提示卡路由）`、`cute_info_card_route（可爱信息卡路由）`、`sassy_reaction_card_route（骚萌反应卡路由）`。
- `已确认` 本轮同步了 PR #22 v3 latest review pack 的既有产物作为当前复审对象，但只改状态口径，不生成新产物。
- `已确认` 本轮新增 dated log：`codex_log/20260501_v3技术里程碑与v31视觉参考锁定.md`。
- `已确认` 只有 commit / push / 合并到 `codex/user-readable-map` 后，上述口径才算新聊天默认正式已知。

## 20260430｜v3 功能卡 / 结果差卡 / 尾卡清晰质感参考落仓库

- `已确认` 本轮只做 v3 前置参考口径落仓库，不生成 v3，不生成视频，不生成音频，不生成图片。
- `已确认` 新增 `card_visual_quality_clean_ui_texture_candidate_20260430（功能卡 / 结果差卡 / Prompt 引用尾卡清晰质感候选参考）`。
- `已确认` 该参考只作为 `candidate（候选参考）`，不是 `locked_reference（锁定参考）`，不是 `visual_master_reference（视觉母版参考）`。
- `已确认` 该参考用于 v3 的功能卡、结果差卡、Prompt 引用尾卡，以及少量 PPT / 卡片承载的信息整理段。
- `已确认` 该参考只继承清晰质感：干净、留白、圆角、轻阴影、轻高光、层级舒服、文字清楚、有一点高级 UI 感。
- `已确认` 该参考不继承底部黑色按钮、电商筛选页、`More Filters` 式 CTA、假 App 导航、一堆分类筛选项、英文乱码或真实 UI 照抄。
- `已确认` 当前没有 `visual_master_reference（视觉母版锁定参考）`；v3 若按该方向生成并通过用户 / ChatGPT 复审，后续才可能反向成为视觉母版候选。
- `已确认` 字幕本轮先不上；PR #15 v2 字幕仍是 `failed_reference（失败参考）`，不得继承为字幕标准。
- `已确认` PR #7 A 版骚萌卡视觉仍是 `candidate（候选参考）`；20260430 “v3 可先以它作为视觉参考”的旧口径已被 20260501 用户最新确认覆盖，后续骚萌卡执行参考改为 PR #7 B。
- `已确认` TTS 节奏 reference 仍是 `tts_15s_b_pacing_locked_20260427（B 版 15 秒停顿梗感 TTS 节奏锁定参考）`；最近 custom voice（脱敏标识 `qwen-t...ac19`）仍是声音底子候选，最终音色待验证。
- `已确认` 本轮新增 dated log：`codex_log/20260430_card_visual_quality_reference_for_v3.md`。
- `已确认` 本轮未修改 `dist/latest_review_pack/（最新审片包）`，未修改 `content_validation（内容验证）`，未修改 `send_ready（可发送状态）`。
- `待验证` 只有本轮分支 / PR 合并或同步回 `codex/user-readable-map（主读取分支）` 后，该参考口径才算新聊天默认正式已知。

## 20260430｜video-metadata-probe skill 安装与配置

- `已确认` 本轮安装并验证 `Homebrew（Mac 包管理器）`：`/opt/homebrew/bin/brew`，版本 `Homebrew 5.1.8`。
- `已确认` 本轮安装并验证 `ffmpeg（音视频工具套件）`：`/opt/homebrew/bin/ffmpeg`，版本 `ffmpeg version 8.1`。
- `已确认` 本轮安装并验证 `ffprobe（视频信息读取工具）`：`/opt/homebrew/bin/ffprobe`，版本 `ffprobe version 8.1`。
- `已确认` 已创建全局 `video-metadata-probe（视频元数据检查）` skill：`/Users/fan/.codex/skills/video-metadata-probe/`。
- `已确认` skill 包含 `SKILL.md（skill 说明文件）`、`scripts/probe_video.sh（视频元数据检查脚本）`、`examples/README.md（使用示例）`。
- `已确认` 已用 `round34_middle_preview（round34 中段预览样片）` 做冒烟测试：`/Users/fan/Documents/视频工厂_clean_user_readable_map_20260430/dist/latest_review_pack/middle_preview.mp4`。
- `已确认` 冒烟测试结果：`28.520000s / 720x1280 / 25.000fps / h264 / aac / 2ch / decodable = true / fallback_used = false / validation_status = passed`。
- `已确认` 冒烟测试只代表 `technical_validation（技术验证）`、`metadata_validation（元数据验证）`、`audio_validation（音频验证）`，不代表 `content_validation（内容验证）` 通过。
- `已确认` 本轮未生成视频，未修改视频 / 音频 / 图片，未修改 `dist/latest_review_pack（最新审片包）`，未修改 `content_validation（内容验证）`，未修改 `send_ready（可发送状态）`。
- `待验证` 本轮日志分支 / PR 合并回 `codex/user-readable-map（主读取分支）` 后，skill 安装记录才成为主读取分支正式已知。

## 20260430｜本地真实路径索引机制

- `已确认` 本轮新增 `codex_log/current_local_artifact_paths.md（当前本地产物路径索引）`，记录 Codex 已在本机验证存在的本地审片 / 复审产物路径。
- `已确认` 后续 ChatGPT / Codex 给用户本地可打开路径时，必须优先读取该索引。
- `已确认` `summary.json（状态摘要）` / `review_manifest.md（审片入口）` 中的路径只能作为线索，不能直接当真实可打开路径输出。
- `已确认` 只有索引中 `path_exists = true（路径存在）` 的记录，才能作为用户可打开路径输出；缺失或超过 24 小时未验证时，必须写成“路径待本地复核”。
- `已确认` 已验证 clean worktree 首选路径存在：`/Users/fan/Documents/视频工厂_clean_user_readable_map_20260430/dist/latest_review_pack/middle_preview.mp4`、`problem_windows/30_32s.mp4`、`problem_windows/30_32s_frames.jpg`、`cut_contact_sheet.jpg`、`full.mp4`。
- `已确认` `no_zoom_completeness` 两张 1x PNG 与布局指标 JSON 在 clean worktree 指定路径未命中；本轮只在旧脏 worktree 中验证到备选打开路径，已标注不得作为默认执行路径。
- `部分成立` 视频文件已完成 `test -f` 与 `stat`；本机没有 `ffprobe`，本轮已尝试但命令不可用，时长 / 分辨率用 macOS `mdls` 只读补充。
- `已确认` 已在 `codex_source/00_codex_readme.md（Codex 执行层总入口）` 和 `codex_source/01_execution_rules.md（Codex 执行规则）` 接入本地路径索引读取规则。
- `已确认` 本轮未生成视频，未修改视频 / 音频 / 图片，未修改 `dist/latest_review_pack（最新审片包）` 内容本体，未修改 `content_validation（内容验证）`，未修改 `send_ready（可发送状态）`。
- `待验证` 本轮 PR 合并 / 同步回 `codex/user-readable-map（主读取分支）` 后，该路径索引机制才成为新聊天默认正式已知。

## 20260430｜中段放大剪辑参考锁定

- `已确认` 本轮只更新 `codex_source/locked_reference_registry.md（锁定参考登记表）` 和日志，不生成视频、不修改视频产物。
- `已确认` 用户已看片确认：这一轮 `middle_preview（中段预览样片）` 的放大剪辑是对的，可以作为参考样本。
- `已确认` 用户确认样本路径：`/Users/fan/Documents/视频工厂_clean_user_readable_map_20260430/dist/latest_review_pack/middle_preview.mp4`；repo relative（仓库相对路径）为 `dist/latest_review_pack/middle_preview.mp4`。
- `已确认` 新增 `middle_zoom_reference_confirmed_middle_preview_20260430（用户确认的中段放大剪辑锁定参考）`。
- `已确认` 该 reference 的 `status（状态） = locked（锁定参考）`，`confirmation_state（确认状态） = locked_reference_confirmed_by_user（用户确认锁定参考）`。
- `已确认` 锁定范围为同类中段录屏证据展示的放大剪辑方式、证据窗口选择方式和关键文字可读尺度；不锁所有视频的固定秒级时间码。
- `已确认` `zoom_pr15_v2_failed_20260430（PR #15 v2 放大位置失败参考）` 仍保持 `failed（失败参考）`；后续完整成片不得继承 PR #15 的失败放大位置。
- `已确认` `zoom_reference_missing_20260430（正确放大方式缺失历史记录）` 已标记为 `deprecated（已废弃缺口）`，并注明主要中段放大缺口已由新的 locked reference 补足。
- `已确认` 本轮不修改 `dist/latest_review_pack（最新审片包）`，不修改 `content_validation（内容验证）`，不修改 `send_ready（可发送状态）`。
- `待验证` 本轮分支 / PR 合并回 `codex/user-readable-map（主读取分支）` 后，该 middle zoom locked reference 才成为新聊天默认正式已知。

## 20260430｜锁定参考登记表全量追回

- `已确认` 本轮只补全并升级 `codex_source/locked_reference_registry.md（锁定参考登记表）`，不生成视频、不做 v3、不修改现有视频产物。
- `已确认` 本轮新增日志：`codex_log/20260430_locked_reference_registry_full_recovery.md（锁定参考登记表全量追回日志）`。
- `已确认` 第一批升级为 `locked（锁定参考）`：
  - `middle_editing_round34_locked_20260425（round34 中段剪辑语法锁定参考）`
  - `sassy_card_three_type_rule_locked_20260428（三类骚萌卡放置规则锁定参考）`
  - `tts_15s_b_pacing_locked_20260427（20260427 B 版 15 秒停顿梗感 TTS 节奏锁定参考）`
  - `opening_reference_element_doll_no_text_locked_20260428（元素娃娃无字开头锚点锁定参考）`
- `已确认` `sassy_card_pr7_a_candidate_20260428（PR #7 A 版骚萌卡视觉候选）` 仍保持 `candidate（候选参考）`，不升级为视觉锁定参考。
- `已确认` 新增候选 / 缺口登记：体素元素娃娃视觉母版候选、round34 粉色樱花提示卡候选、功能卡 / 结果差卡候选、Prompt 引用尾卡规则候选、语音样本2声音底子候选、字幕标准缺口、正确放大方式缺口。
- `已确认` PR #15 v2 字幕、layout / 背景、TTS 缺失仍保持 `failed（失败参考）`；新增 PR #15 v2 放大位置失败参考。
- `已确认` 20260412 历史通过样片仍保持 `historical（历史参考）`，不升级为当前默认母版。
- `已确认` 本轮不修改 `dist/latest_review_pack/（最新审片包）`，不修改 `content_validation（内容验证）`，不修改 `send_ready（可发送状态）`。
- `待验证` 本轮分支 / PR 合并回 `codex/user-readable-map（主读取分支）` 后，第一批 locked reference 才成为新聊天默认正式已知。

## 20260430｜锁定参考继承机制修补

- `已确认` 本轮不生成新视频，不修改现有视频，不创建成片候选。
- `已确认` 本轮只修机制：新增 locked_reference（锁定参考）定义、晋升条件、默认继承规则、完整成片前置读取、继承报告、summary 字段和 blocked 条件。
- `已确认` 当前仓库审计结论为 `locked_reference_inheritance_missing（缺少锁定参考继承机制）`：已有 reference pack / 声音参考锚点 / 当前审片包等相近机制，但没有统一 locked reference registry、强制继承报告和未继承 blocked 条件。
- `已确认` 新增规则文件：`codex_source/14_locked_reference_inheritance_rules.md`。
- `已确认` 新增登记表：`codex_source/locked_reference_registry.md`。
- `已确认` 初始 registry 没有任何 `locked` reference；只登记 `candidate`、`failed`、`historical`，避免把候选或失败样本误写成正式继承样板。
- `已确认` 初始 registry 已登记 round34 中段剪辑语法候选、PR #7 A 版骚萌卡视觉候选、PR #8 三类骚萌卡规则候选、PR #15 v2 字幕 / layout / TTS 失败参考、20260427 B 版 15 秒 TTS 节奏候选、20260412 历史通过样片。
- `已确认` 已接入读取链路：完整成片 / 成品候选片 / 技术预览升级 / 样片回炉 / 字幕 / TTS / 卡片 / 放大 / 剪辑 / 视觉母版修正任务，后续必须先读 locked reference 规则和 registry。
- `已确认` 若读不到 locked reference 规则或 registry，或未继承已锁定 reference，必须 `blocked`，不得写成候选片完成。
- `已确认` 后续完整成片 / 成品候选片 / 样片回炉必须输出 `locked_reference_inheritance_report.md（锁定参考继承报告）`。
- `已确认` 本轮不修改 `dist/latest_review_pack/`，不修改 `content_validation`，不修改 `send_ready`。
- `待验证` 本机制当前只在工作分支 / PR 中成立；合并或同步回 `codex/user-readable-map` 后，才算主读取分支正式已知。

## 20260427｜中段吐槽插入风格视觉证据补齐

- `已确认` 本轮只是补齐上一轮 reference pack 的轻量视觉证据，用于待 ChatGPT / 用户复审。
- `已确认` 本轮新增 / 同步视觉证据：
  - `dist/reference_packs/20260427_中段吐槽插入风格_faithful_extract/视觉证据_关键帧联系表_keyframes_contact_sheet.jpg`
  - `dist/reference_packs/20260427_中段吐槽插入风格_faithful_extract/视觉证据_吐槽三连帧_punchline_triptych.jpg`
  - `dist/reference_packs/20260427_中段吐槽插入风格_faithful_extract/视觉证据_第一次吐槽前后_context_01.jpg`
  - `dist/reference_packs/20260427_中段吐槽插入风格_faithful_extract/视觉证据_第二次吐槽前后_context_02.jpg`
  - `dist/reference_packs/20260427_中段吐槽插入风格_faithful_extract/视觉证据_第三次吐槽前后_context_03.jpg`
  - `dist/reference_packs/20260427_中段吐槽插入风格_faithful_extract/视觉证据_GIF式吐槽动态预览_visual_punchline_preview.mp4`
- `已确认` 本轮新增报告：
  - `dist/reference_packs/20260427_中段吐槽插入风格_faithful_extract/画面层保真补充_visual_punchline_report.md`
  - `dist/reference_packs/20260427_中段吐槽插入风格_faithful_extract/视觉证据补齐_run_summary.json`
- `待验证` GIF 式吐槽画面层仍待 ChatGPT / 用户复审；本轮不代表最终口径。
- `已确认` 本轮不改视频，不生成新 round，不替换音轨，不修改 `dist/latest_review_pack/`。
- `已确认` 本轮不改变 `content_validation（内容验证）`，不改变 `send_ready（可发送状态）`。
- `已确认` 本轮不修改 `GPT数据源/04_选题与文案规则.md`、`GPT数据源/05_文案路由规则.md`、`GPT数据源/07_AI知识类视频价值规则.md`、`GPT数据源/08_当前正式事实.md`。
- `已确认` 原始 50MB MP4、完整 `frames/` 目录、音频副本与波形图未提交；本轮只提交筛选后的轻量视觉证据。

## 20260427｜中段吐槽插入风格参考包同步

- `已确认` 本轮只是把上一轮本地“中段吐槽插入风格高保真提取”文本 reference_pack 同步到 `codex/user-readable-map`，用于待 ChatGPT / 用户复审。
- `已确认` 本轮新增 / 同步文本报告路径：
  - `dist/reference_packs/20260427_中段吐槽插入风格_faithful_extract/素材清单_assets_inventory.md`
  - `dist/reference_packs/20260427_中段吐槽插入风格_faithful_extract/audio_reference_note.md`
  - `dist/reference_packs/20260427_中段吐槽插入风格_faithful_extract/scene_index.md`
  - `dist/reference_packs/20260427_中段吐槽插入风格_faithful_extract/吐槽插入风格_reference_pack.md`
  - `dist/reference_packs/20260427_中段吐槽插入风格_faithful_extract/给ChatGPT的素材汇报_material_report.md`
  - `dist/reference_packs/20260427_中段吐槽插入风格_faithful_extract/run_summary.json`
- `已确认` 本轮同步源来自上一轮本地分析包：`/Users/fan/Documents/视频工厂/dist/reference_packs/20260427_中段吐槽插入风格_faithful_extract/`。
- `已确认` 上一轮本地分析包生成于 `fix/no-zoom-completeness-layout`，不是主读取分支；本轮已在 `codex/user-readable-map` 重新同步文本报告。
- `已确认` 上一轮存在路径漂移风险：上一轮分支中无空格 `GPT数据源/` 缺失，只读到 `GPT 数据源/`；本轮已在 `codex/user-readable-map` 读取无空格 `GPT数据源/` 当前执行包。
- `待验证` 吐槽插入风格仍待 ChatGPT / 用户复审；本轮不代表最终口径。
- `已确认` 本轮不写入正式风格规则，不改视频，不生成新 round，不修改 `dist/latest_review_pack/`。
- `已确认` 本轮不改变 `content_validation`，不改变 `send_ready`。
- `已确认` 本轮未提交二进制证据文件：`keyframes_contact_sheet.jpg`、`audio/reference_audio.m4a`、`audio_waveform.png`、`frames/`；本轮只同步 Markdown / JSON 文本报告。

## 20260427｜文案生产流程与 B 版声音口径固化

- `已确认` 本轮只做《视频工厂》文案生产流程、最终风格锚点、声音 B 版暂定口径的规则落仓库；未生成新音频、新视频，未修改现有样片，未替换全片音轨。
- `已确认` 已在 `GPT数据源/04_选题与文案规则.md（当前文案规则）` 写入后续默认文案生产流程：`Perplexity（外部参考检索 / 研究工具）` 输出 `reference pack（参考包）` 与 `raw feeling draft（原感初稿）` -> 用户录制素材 -> `Codex（执行代理）` 做素材技术检查与细节证据报告 -> `ChatGPT（最终落稿与复审入口）` 写最终落稿 -> `Codex（执行代理）` 按最终稿执行。
- `已确认` 已明确 `Perplexity（外部参考检索 / 研究工具）` 只负责参考包 / 原感初稿，不是最终稿；不得直接进入执行。
- `已确认` 已在 `GPT数据源/05_文案路由规则.md（当前文案路由）` 写入 `Codex（执行代理）` 素材细节汇报标准：不能只报“素材存在 / 技术通过”，必须写清素材里有什么、在哪一秒、发生了什么、能证明什么，并给 `ChatGPT（最终落稿与复审入口）` 可写稿的细节。
- `已确认` 已在 `GPT数据源/07_AI知识类视频价值规则.md（当前价值规则）` 写入最终稿细节标准：最终稿必须尽量具体到真实工具 / 网站、页面、按钮、输入动作、生成结果、前后对比、失败点和下一步怎么做。
- `已确认` 已在 `GPT数据源/04_选题与文案规则.md（当前文案规则）` 写入最终文案风格锚点：用户确认的“用字更自然版长稿” + 20260427 B 版“停顿梗感”试听方向；风格为微反转、说话带梗、自然口语、生活观察起手、轻吐槽、避免 AI 感硬词，不写课程腔 / 广告腔 / 鸡血腔。
- `已确认` 已在 `GPT数据源/08_当前正式事实.md（当前正式事实）` 写入当前声音暂定口径：用户更喜欢 20260427 B 版“停顿梗感”方向；新样本2 `custom voice（自定义音色）` 脱敏标识 `qwen-t...ac19` 可继续作为当前声音底子。
- `已确认` 后续声音主要调 `speech_pacing（语速节奏）`、`pause_timing（停顿位置）`、`copy_fit（文案搭配）`；暂不优先重做 `voice cloning（声音复刻）`，暂不优先换音色。
- `待验证` B 版只是当前优先试听方向，不是最终成片音轨，不能写最终音色已定，不能写 `voice_validation_status（声音验证状态） = 通过`。
- `已确认` 未修改 `GPT 数据源/（GPT Project 协作规则包）`，未把 B 版暂定声音这种动态状态写入静态协作包。
- `已确认` 新增日志：`codex_log/20260427_文案生产流程与B版声音口径固化.md（本轮日期日志）`。
- `已确认` 当前视频状态未改变：
  - `latest_review_pack = round34_中段双展示提示卡_正反分段提示修复`
  - `technical_validation = 通过`
  - `middle_segment_review = 用户暂定通过 / 暂不继续修改中段`
  - `content_validation = 待用户 / ChatGPT 最终复审`
  - `full_content_validation = 待用户 / ChatGPT 最终复审`
  - `send_ready = no`

## 20260427｜十五秒文案语速停顿试配

- `已确认` 本轮只做《视频工厂》声音文案适配试听；未换音色、未重做 voice cloning、未重新裁剪 / 上传样本、未替换全片音轨。
- `已确认` 用户本轮确认方向已记录：新样本2音色底子可以继续用，后续主要调语速、停顿和文案搭配；偏好“微反转 + 说话带梗 + 自然口语”；需避免类似“下一步从哪打”的 AI 感硬词。
- `已确认` 使用新样本2 custom voice：`qwen-t...ac19`（脱敏）；`model / target_model = qwen3-tts-vc-realtime-2026-01-15`。
- `已确认` 本轮只通过 custom voice list 解析既有 voice，未重新 `create_custom_voice`；未使用 Serena；未使用上一轮 A / B custom voice。
- `已确认` 新增输出目录：`dist/voice_trials/20260427_十五秒文案语速停顿试配_15s_copy_pacing_trial/`。
- `已确认` A 版文案为自然节奏，去空白字数 `93`；B 版文案为停顿梗感，去空白字数 `97`；两版均未命中本轮禁用硬词。
- `已确认` 已生成 A / B 两条声音试听：
  - A：`A_15秒文案_自然节奏.wav`，`17.20s / wav / pcm_s16le / 24000 Hz / mono / mean_volume -23.9 dB / loudnorm.input_i -23.92 LUFS`
  - B：`B_15秒文案_停顿梗感.wav`，`16.32s / wav / pcm_s16le / 24000 Hz / mono / mean_volume -23.4 dB / loudnorm.input_i -23.67 LUFS`
- `已确认` A / B 均可被 `ffmpeg` 解码，且时长均在 13-18 秒范围内。
- `已确认` A / B API 原始输出已在目标范围内，本轮未使用 `atempo`。
- `已确认` 脱敏请求、音频验证与运行摘要已落盘：`A_voice_clone_tts_request_debug_sanitized.json`、`B_voice_clone_tts_request_debug_sanitized.json`、`A_ffmpeg_decode_check.txt`、`B_ffmpeg_decode_check.txt`、`A_volumedetect.txt`、`B_volumedetect.txt`、`A_loudnorm_measure.txt`、`B_loudnorm_measure.txt`、`run_summary.json`。
- `已确认` 新增日志：`codex_log/20260427_十五秒文案语速停顿试配.md`。
- `待验证` 本轮只证明 `technical_generation` 通过；A / B 的语速、停顿、轻吐槽和文案搭配是否合适，仍待用户 / ChatGPT 听感复审。
- `已确认` 当前视频状态未改变：
  - `latest_review_pack = round34_中段双展示提示卡_正反分段提示修复`
  - `technical_validation = 通过`
  - `middle_segment_review = 用户暂定通过 / 暂不继续修改中段`
  - `content_validation = 待用户 / ChatGPT 最终复审`
  - `full_content_validation = 待用户 / ChatGPT 最终复审`
  - `send_ready = no`

## 20260426｜语音样本2复刻与文案风格解析

- `已确认` 本轮重开新语音样本链路，未沿用上一轮 A / B 声音试配结果；上一轮 A / B 只保留为失败参考。
- `已确认` 已定位用户新样本：`/Users/fan/Documents/视频工厂/素材录制/语音样本 2.MP4`，候选数量为 `1`，未回退使用旧样本。
- `已确认` 新样本只读解析：`23.16s / mov,mp4,m4a,3gp,3g2,mj2 / hevc / aac / 44100 Hz / stereo / mean_volume -13.3 dB / loudnorm.input_i -10.26 LUFS`。
- `已确认` 已生成分析副本与复刻输入：
  - `dist/voice_trials/20260426_语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis/语音样本2_分析副本.m4a`
  - `dist/voice_trials/20260426_语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis/语音样本2_复刻输入_10-20秒.wav`
- `已确认` 复刻输入样本为 `17.00s / wav / pcm_s16le / 24000 Hz / mono / 816078 bytes`，从原 MP4 `2.0s` 起连续裁剪。
- `已确认` 已用新样本创建新的测试 custom voice，脱敏标识：`qwen-t...ac19`；`model = qwen-voice-enrollment`，`target_model = qwen3-tts-vc-realtime-2026-01-15`，`preferred_name = vfsample20426`。
- `已确认` 已生成 1 条新样本声音复刻试听 trial：`dist/voice_trials/20260426_语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis/语音样本2_声音复刻试听_15秒.wav`。
- `已确认` 试听 trial 可被 `ffmpeg` 解码：`13.60s / wav / pcm_s16le / 24000 Hz / mono / mean_volume -23.8 dB / loudnorm.input_i -23.72 LUFS`。
- `已确认` 已尝试并完成完整 MP4 自动 ASR 转写，模型为 `paraformer-realtime-v2`；转写文件：`dist/voice_trials/20260426_语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis/语音样本2_转写文本_transcript.md`。
- `待验证` 自动转写尚未人工校对，可能存在误识别；文案风格记录只能作为本轮 reference style，不能写成唯一标准风格。
- `已确认` 已新增高保真文案风格记录：`codex_log/20260426_语音样本2_文案风格高保真记录.md`。
- `已确认` 已新增音频参考报告：`codex_log/20260426_语音样本2_audio_reference_report.md`。
- `已确认` 已新增执行日志：`codex_log/20260426_语音样本2复刻与文案风格解析.md`。
- `已确认` 已新增本轮脚本：`scripts/语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis.py`。
- `待验证` 本轮只证明 `technical_generation` 通过；`voice_validation_status` 仍为待用户 / ChatGPT 听感复审。
- `已确认` 当前视频状态未改变：
  - `latest_review_pack = round34_中段双展示提示卡_正反分段提示修复`
  - `technical_validation = 通过`
  - `middle_segment_review = 用户暂定通过 / 暂不继续修改中段`
  - `content_validation = 待用户 / ChatGPT 最终复审`
  - `full_content_validation = 待用户 / ChatGPT 最终复审`
  - `send_ready = no`

## 20260426｜台湾口语开心降噪声音第二轮试配

- `已确认` 本轮只生成《视频工厂》声音第二轮最小对照 trial；未修改视频、未替换全片音轨、未生成新视频 round。
- `已确认` 用户本轮听感反馈已保真记录：
  1. 情绪上面还不够开心的那种。
  2. 需要把口语改成台湾的口音。
  3. 现在生成的环境音有点吵，需要降噪。
- `已确认` 新增本轮输出目录：`dist/voice_trials/20260426_台湾口语开心降噪试配_taiwan_happy_denoise_trial/`。
- `已确认` A 版沿用当前 custom voice（脱敏：`qwen-t...de43`），使用台湾口语文本 + 开心轻快 instructions 生成，并保留：
  - `A_沿用音色_台湾口语开心_API原始_未节奏校准.wav`
  - `A_沿用音色_台湾口语开心_原始.wav`
  - `A_沿用音色_台湾口语开心_轻降噪.wav`
- `已确认` B 版先对复刻输入样本做轻降噪，再重新创建测试 custom voice（脱敏：`qwen-t...bb3b`），使用同一文本 + 同一 instructions 生成，并保留：
  - `B_复刻输入样本_轻降噪.wav`
  - `B_重建音色_台湾口语开心_API原始_未节奏校准.wav`
  - `B_重建音色_台湾口语开心_原始.wav`
  - `B_重建音色_台湾口语开心_轻降噪.wav`
- `已确认` 因固定文案较长，API 直出分别为 `17.60s` / `16.56s`；本轮保留 API 直出审计文件，同时用 `atempo` 生成 10-15 秒未降噪节奏校准版。
- `已确认` 四个正式对照输出均可被 `ffmpeg` 解码：
  - A 原始：`14.18s / wav / pcm_s16le / 24000 Hz / mono / mean_volume -22.8 dB / loudnorm.input_i -22.13 LUFS`
  - A 轻降噪：`14.18s / wav / pcm_s16le / 24000 Hz / mono / mean_volume -23.3 dB / loudnorm.input_i -22.64 LUFS`
  - B 原始：`14.20s / wav / pcm_s16le / 24000 Hz / mono / mean_volume -22.4 dB / loudnorm.input_i -22.40 LUFS`
  - B 轻降噪：`14.20s / wav / pcm_s16le / 24000 Hz / mono / mean_volume -22.7 dB / loudnorm.input_i -22.65 LUFS`
- `已确认` 脱敏请求与验证记录已落盘：`custom_voice_list_debug_sanitized.json`、`A_voice_clone_tts_request_debug_sanitized.json`、`B_重建音色_create_custom_voice_request_debug_sanitized.json`、`B_voice_clone_tts_request_debug_sanitized.json`、`run_summary.json`。
- `已确认` 新增脚本：`scripts/声音第二轮台湾口语开心降噪_trial_round2.py`。
- `已确认` 新增日志：`codex_log/20260426_台湾口语开心降噪声音试配.md`。
- `待验证` 本轮只证明 `technical_generation` 通过；A / B 是否更开心、是否像台湾口语、降噪后是否仍自然，仍待用户 / ChatGPT 听感复审。
- `已确认` 当前视频状态未改变：
  - `latest_review_pack = round34_中段双展示提示卡_正反分段提示修复`
  - `technical_validation = 通过`
  - `middle_segment_review = 用户暂定通过 / 暂不继续修改中段`
  - `content_validation = 待用户 / ChatGPT 最终复审`
  - `full_content_validation = 待用户 / ChatGPT 最终复审`
  - `send_ready = no`

## 20260426｜GPT Project 协作规则包更新

- `已确认` 本轮只更新 `GPT 数据源/`，将其定位改为 GPT Project 协作规则包；它只负责告诉 ChatGPT 如何协作、如何读 GitHub、如何处理冲突，不再承载动态当前事实。
- `已确认` 当前项目事实和执行状态的主事实源仍是 GitHub 当前文件；当前 round、`latest_review_pack`、`content_validation`、`send_ready`、声音试配状态都必须从 GitHub 当前文件读取。
- `已确认` 本轮在 `codex/user-readable-map` worktree 中新增并跟踪 `GPT 数据源/` 10 份文件；未修改 `GPT数据源/` 当前 10 份执行包。
- `已确认` `GPT 数据源/08_当前正式事实.md` 未纳入新包；新第 8 份文件为 `GPT 数据源/08_当前事实读取规则.md`，专门记录当前事实读取顺序和冲突裁决。
- `已确认` 本轮未修改视频、音频、图片、原始素材、生成脚本、测试脚本、`dist/latest_review_pack/*` 或 `dist/voice_trials/*`。
- `已确认` 本轮不改变当前视频与声音状态；声音试配和全片内容复审仍以 GitHub 当前文件为准。
- `下一个目标`：后续 ChatGPT 先按 `GPT 数据源/` 协作规则接手，再从 GitHub 当前文件读取项目事实。

## 20260426｜下一个目标与中文英文命名规则补丁

- `已确认` 本轮只做规则补丁，不做目录迁移，不执行 `git mv`，不重命名任何已有文件或文件夹。
- `已确认` 执行位置已校准到主读取分支 worktree：`/private/tmp/视频工厂_user_readable_map_sync`，当前分支为 `codex/user-readable-map`。
- `已确认` 已写入最终汇报和交接口径：最后一栏统一使用“下一个目标”，不再默认使用“下一步行动建议”。
- `已确认` 已写入新增业务文件 / 业务文件夹命名规则：默认使用“中文 + 英文”，推荐格式为 `中文名_english_name`。
- `已确认` 已有文件和已有文件夹本轮不追溯改名；工具链强制英文名保留为例外，且例外不得扩大到普通业务目录和业务文件。
- `已确认` 本轮不修改视频、音频、图片、原始素材、生成脚本或测试脚本。
- `已确认` 当前视频状态未改变：
  - `latest_review_pack = round34_中段双展示提示卡_正反分段提示修复`
  - `content_validation = 待用户 / ChatGPT 最终复审`
  - `full_content_validation = 待用户 / ChatGPT 最终复审`
  - `send_ready = no`
- `已确认` 提交前本地验证已通过；远端同步状态以本轮收尾的 `git show origin/codex/user-readable-map:路径` 复读验证为准。

## 20260426｜round28 声音复刻试配继续执行

- `已确认` 本轮继续上轮被阿里百炼 `Arrearage` 阻塞的 voice cloning（声音复刻）路线；不重回 `Serena` 系统音色，不修改视频，不替换全片音轨，不生成新视频 round。
- `已确认` 复用上轮合规复刻输入样本：`dist/voice_trials/20260425_round28_voice_clone_trial/语音样本_复刻输入_10-20秒.wav`，参数仍为 `17.00s / wav / pcm_s16le / 24000 Hz / mono / 816078 bytes`。
- `已确认` 阿里账户本轮不再返回 `Arrearage`；用户 prompt 指定的 `vf_r28_clone_20260426` 因超过官方 `preferred_name` 16 字符限制返回 `InvalidParameter`，已按官方约束改用 `vfr28clone0426`。
- `已确认` 已创建测试 custom voice，脱敏标识：`qwen-t...de43`；创建模型为 `qwen-voice-enrollment`，`target_model = qwen3-tts-vc-realtime-2026-01-15`。
- `已确认` 已使用该 custom voice 生成 1 条 round28 声音复刻 trial：`dist/voice_trials/20260425_round28_voice_clone_trial/round28_声音复刻试配_10-15秒.wav`。
- `已确认` 输出音频验证：`12.96s / wav / pcm_s16le / 24000 Hz / mono / 622124 bytes`，可被 `ffmpeg` 解码；`mean_volume = -23.5 dB`，`loudnorm.input_i = -23.57 LUFS`。
- `已确认` 脱敏请求记录：
  - `dist/voice_trials/20260425_round28_voice_clone_trial/voice_clone_request_debug_sanitized.json`
  - `dist/voice_trials/20260425_round28_voice_clone_trial/voice_clone_tts_request_debug_sanitized.json`
- `待验证` 本轮只证明 voice cloning trial 已生成；是否明显比上一轮 `Serena` 更接近用户样本，仍待用户 / ChatGPT 听感复审。
- `已确认` 当前视频状态未改变：
  - `latest_review_pack = round34_中段双展示提示卡_正反分段提示修复`
  - `content_validation = 待用户 / ChatGPT 最终复审`
  - `full_content_validation = 待用户 / ChatGPT 最终复审`
  - `send_ready = no`

## 20260425｜round28 声音复刻最小试配

- `已确认` 用户授权已到位；本轮允许上传裁剪后的合规样本到阿里百炼声音复刻接口，仅用于《视频工厂》最小声音复刻试配。
- `已确认` 已生成合规复刻输入样本：`dist/voice_trials/20260425_round28_voice_clone_trial/语音样本_复刻输入_10-20秒.wav`，参数为 `17.00s / wav / pcm_s16le / 24000 Hz / mono / 816078 bytes`。
- `已确认` 本轮实际走的是 `qwen-voice-enrollment -> qwen3-tts-vc-realtime-2026-01-15` 的声音复刻路线，没有回退到 `Serena` 系统音色。
- `已确认` 当前阻塞点发生在 `create_custom_voice` 阶段：阿里百炼返回 `400 / Arrearage`，未创建成功 custom voice，未生成新的声音复刻试配音频。
- `已确认` 脱敏请求记录：`dist/voice_trials/20260425_round28_voice_clone_trial/voice_clone_request_debug_sanitized.json`。
- `已确认` 复刻试配日志：`codex_log/20260425_round28_声音复刻最小试配.md`。
- `待验证` 账户恢复后，可直接复用本轮合规裁剪样本继续创建 custom voice；当前声音仍待验证。
- `已确认` 当前视频状态未改变：
  - `latest_review_pack = round34_中段双展示提示卡_正反分段提示修复`
  - `content_validation = 待用户 / ChatGPT 最终复审`
  - `full_content_validation = 待用户 / ChatGPT 最终复审`
  - `send_ready = no`

## 20260425｜round28 声音试配失败排查

- `已确认` 用户已听审 `dist/voice_trials/20260425_round28_10s_voice_trial/round28_声音试配_10-15秒.m4a`，反馈为：和样本完全不一样，非常生硬，一听就是 AI。
- `已确认` 本轮只做声音路线诊断；未生成新音频，未修改视频 / 图片 / 原始素材 / 当前 trial 音频 / 脚本，未调用 TTS API，未上传用户样本。
- `已确认` 当前 trial 请求体为 `qwen3-tts-instruct-flash-realtime + Serena` 系统音色 + 指令控制；请求体里没有用户样本、custom voice、voice cloning 或 voice design 字段。
- `已确认` 失败主因：用户样本没有实际进入生成链路，当前路线只能做系统音色的风格指令控制，不能复刻用户样本声纹。
- `部分成立` 文案韵律和后处理可能放大生硬 / AI 感，但不是“完全不像样本”的主因。
- `待验证` 下一轮最值路线是：先取得用户明确授权，再走 `voice cloning（声音复刻）` 最小试配；若用户不授权上传样本，则退而走 `voice design（声音设计）`，不要继续盲调 `Serena`。
- `已确认` 诊断日志：`codex_log/20260425_round28_声音试配失败排查.md`。
- `已确认` 当前视频状态未改变：
  - `latest_review_pack = round34_中段双展示提示卡_正反分段提示修复`
  - `content_validation = 待用户 / ChatGPT 最终复审`
  - `full_content_validation = 待用户 / ChatGPT 最终复审`
  - `send_ready = no`

## 20260425｜round28 最小声音试配

- `已确认` 本轮只生成 1 条 10-15 秒声音 trial（试配）音频；未修改任何视频、图片、原始素材、当前成片音轨或视频装配脚本。
- `已确认` 使用 round28 文案来源：`dist/20260417_豆包的正确打开方式_vnext/round28_完整可读终修/subtitles/round28_完整可读终修.srt`。
- `已确认` 本轮试配文案取自 round28 字幕第 1 段 + 第 5 段首句：
  - `最费时间的，不是做汇报页。是第一行根本写不出来。后来我换上调好的提示词，直接砍掉空转。区别不是豆包，是那段提示词。`
- `已确认` 真实使用 TTS：`aliyun_bailian / aliyun_qwen_realtime_websocket / qwen3-tts-instruct-flash-realtime / Serena`。
- `已确认` 输出音频：`dist/voice_trials/20260425_round28_10s_voice_trial/round28_声音试配_10-15秒.m4a`。
- `已确认` 音频基础验证：`13.00s`、`aac (LC)`、`48000 Hz / mono`、`mean_volume = -16.4 dB`、`loudnorm.input_i = -16.25 LUFS`，可被 `ffmpeg` 解码。
- `已确认` 当前视频状态未改变：
  - `latest_review_pack = round34_中段双展示提示卡_正反分段提示修复`
  - `content_validation = 待用户 / ChatGPT 最终复审`
  - `full_content_validation = 待用户 / ChatGPT 最终复审`
  - `send_ready = no`
- `待验证` 该 trial 只回答声音方向是否接近“低压、清楚、有一点可爱感的女生游戏向导音”；用户 / ChatGPT 听感复审前，不得写成最终音色、最终 TTS 或声音验证通过。

## 20260425｜语音样本只读排查与声音参考锚点

- `已确认` 本轮任务只做语音样本定位、音频基础参数分析、声音参考锚点落地与仓库口径更新；不改视频、不替换旁白、不生成新 round、不做 TTS 试配。
- `已确认` 当前 latest_review_pack 仍指向：`round34_中段双展示提示卡_正反分段提示修复`。
- `已确认` 用户语音样本已通过兜底搜索命中：`/Users/fan/Documents/视频工厂/素材录制/语音样本_04-25-2026 22-19-11_1.MP4`。
- `已确认` 样本用于记录 `可爱女生向导音` 的 reference anchor（参考锚点）；它不等于最终 TTS 方案已确定，也不等于声音内容验证通过。
- `部分成立` `ffmpeg` 可用并已完成分析用音频副本提取、`volumedetect`、`astats`、`silencedetect` 与 `loudnorm` 初步测量；`ffprobe` 未在本机可执行路径中命中，本轮元数据读取降级使用 `ffmpeg` 输入信息。
- `已确认` 音频基础参数报告：`codex_log/20260425_语音样本_audio_reference_report.md`。
- `已确认` 分析文本输出目录：`codex_log/audio_reference/20260425_语音样本/`。
- `已确认` 当前视频状态未改变：
  - `content_validation = 待用户 / ChatGPT 最终复审`
  - `full_content_validation = 待用户 / ChatGPT 最终复审`
  - `send_ready = no`
- `待验证` 下一步声音动作是基于该样本做 10-15 秒最小声音试配，再和当前视频开头 / 结尾主持壳做听感匹配复审；不得直接全片替换。

## 20260425｜round34 中段双展示提示卡正反分段提示修复

- `已确认` 当前视频工作分支为 `codex/doubao-vnext-direct-fix-20260417`；该分支当前由 Git worktree `/private/tmp/视频工厂_round28_complete_readability` 持有。
- `已确认` 本轮新开 `round34_中段双展示提示卡_正反分段提示修复`，只做 `latest_review_pack` 中段局部修复；未重构整条视频。
- `已确认` 用户本轮同步的图二参考图可读取：`/Users/fan/Desktop/截屏2026-04-25 18.11.07.png`，尺寸 `908x492`。
- `已确认` 两张提示卡已按图二粉色樱花柔和展示牌风格重构为 720x1280、9:16 竖屏：
  - 《反面展示》：`先看旧做法：一句糊话，结果怎么变泛`
  - 《正面展示》：`再看工作包后：结果怎么一步步落成`
- `已确认` round34 中段结构为：反面展示提示卡 -> 反面真实录屏 -> 正面展示提示卡 -> 正面真实录屏 -> 结果差提示卡。
- `已确认` 反面录屏与正面录屏仍由用户真实录屏承担，源时间码与 round33 一致，未裁短、未替换、未重录。
- `已确认` 开头主持壳、回场主持壳、`judgment_card`、Prompt 引用尾卡均未重做；未调用阿里 API，未重新生成元素娃娃，未修改原始录屏素材。
- `已确认` `latest_review_pack` 已更新指向：
  - `round34_中段双展示提示卡_正反分段提示修复`
- `已确认` 当前审片包口径：
  - `middle_segment_review = 用户暂定通过 / 暂不继续修改中段`
  - `border_residue_validation = 通过`
  - `jump_cut_validation = 通过`
  - `technical_validation = 通过`
  - `content_validation = 待用户 / ChatGPT 最终复审`
  - `send_ready = no`
- `已确认` 用户已打开实际可用本地审片包路径：`/private/tmp/视频工厂_round28_complete_readability/dist/latest_review_pack/`。
- `已确认` 用户最新反馈为“现在中段没什么问题了”，仓库口径记录为：round34 中段结构暂定接受，当前不继续修改中段。
- `已确认` 中段暂定接受只代表 `middle_segment_review` 暂定收束，不代表全片 `content_validation` 通过。
- `待验证` round34 内容最终是否过线仍需用户 / ChatGPT 人工复审。
- `禁止误写` 不得把技术扫描通过写成内容最终通过；不得写 `send_ready = yes`；不得把云端剪辑写成稳定跑通。

## 当前最新审片入口

- 当前可打开本地审片包：`/private/tmp/视频工厂_round28_complete_readability/dist/latest_review_pack/`
- `dist/latest_review_pack/review_manifest.md`
- `dist/latest_review_pack/summary.json`
- `dist/latest_review_pack/full.mp4`
- `dist/latest_review_pack/middle_preview.mp4`
- `dist/latest_review_pack/before_after.mp4`
- `dist/latest_review_pack/图二参考图.png`
- `dist/latest_review_pack/反面展示提示卡_单帧.png`
- `dist/latest_review_pack/正面展示提示卡_单帧.png`
- `dist/latest_review_pack/正反提示卡_并排对比.png`
- `dist/latest_review_pack/problem_windows/30_32s.mp4`
- `dist/latest_review_pack/cut_contact_sheet.jpg`

## 新会话接手建议先读

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `GPT数据源/08_当前正式事实.md`
- `codex_log/current_publish_target.md`
- `codex_log/current_publish_target_light_evidence.md`
- `dist/latest_review_pack/review_manifest.md`
- `dist/latest_review_pack/summary.json`
- `codex_log/20260425_round34_中段双展示提示卡_正反分段提示修复.md`
- `codex_log/20260425_round34_中段暂定通过与本地审片路径修正.md`
