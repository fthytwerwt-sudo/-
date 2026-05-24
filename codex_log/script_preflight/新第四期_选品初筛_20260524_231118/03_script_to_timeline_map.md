# script_to_timeline_map

## 核心结论

- 本轮已做到 `line_group_level`，不是段落级粗映射。
- 每个 `material_granularity_line` 都绑定了 V001 / V003 / V004 时间码。
- 判断 / 边界句均标注了边界卡或经验判断属性。

| line_group | 类型 | 时间码 | 画面承载 | 对齐状态 | 风险 / 请求 |
|---|---|---|---|---|---|
| LG001 | smooth_line, judgment_boundary_line | V001 00:15-01:24; V003 00:33-00:48; V004 00:27-00:36 | V001 商品卡快速扫过，叠 V003/V004 表格结果一闪，形成“乱翻商品卡 -> 判断表”的对照。 | aligned_with_boundary_card | 无需改核心语义；但字幕要避免“已证明最贵”。 |
| LG002 | material_granularity_line | V001 00:15-01:24; V001 01:36-02:09 | 精选联盟商品卡列表与商品卡近景，重点让观众看到商品卡、价格/佣金/月销等字段位置。 | aligned | 无核心改稿；执行时不读具体数值。 |
| LG003 | judgment_boundary_line | V001 01:36-02:09; V003 00:51-01:30 | 商品卡字段或明细表背景，叠判断卡说明“佣金高不等于值得测”。 | card_supported_boundary_statement | 建议把“可能都不一定回得来”保留为可能性，不改成确定亏损。 |
| LG004 | judgment_boundary_line | V001 02:12-03:24 | 商品页或 AI 分析窗口背景，叠 SKU 复杂判断卡；如画面不显示 SKU，只做经验判断卡。 | card_supported_boundary_statement | 需要 ChatGPT 复核是否改成“还要核 SKU 会不会太复杂”。 |
| LG005 | judgment_boundary_line | V001 01:36-02:09; V003 00:51-01:30 | V001 商品卡/字段页或 V003 明细表，叠“分数/退货风险需复核”卡。 | aligned_with_uncertain_values | 建议把“分一低”保留为泛化风险，不要对应某个商品。 |
| LG006 | material_granularity_line | V001 00:15-01:24 | V001 搜索/浏览流程，按页面动作切：进入页面、搜索、商品卡列表、字段区域。 | aligned | 无。 |
| LG007 | result_transition_line | V001 01:27-01:33; V001 02:12-03:24 | AI/聊天分析窗口叠商品页，表现“把页面信息整理出来”。 | copy_change_request_recommended | 建议 ChatGPT 将“直接让 Codex 操作我的电脑”改为“我让 Codex/AI 先跑一轮选品初筛，把页面信息整理出来”，除非后续补录明确操作画面。 |
| LG008 | material_granularity_line | V001 01:36-02:09; V003 00:51-01:30 | 商品卡近景 + 明细表字段列，逐个高亮字段名。 | aligned | 无核心改稿；执行时避免数值化承诺。 |
| LG009 | result_transition_line | V001 02:12-03:24; V003 00:33-00:48 | 左边商品页/AI 分析，右边或下一镜转到候选方向表。 | aligned_with_result_table | 可把“Codex 做的时候”改为“这轮初筛的结果”以降低自动化承诺。 |
| LG010 | material_granularity_line | V003 00:33-00:48 | 候选方向表局部放大，高亮 rank / category / grade / listing_candidate / video_candidate / key_basis / key_risk / status。 | aligned | 无核心改稿。 |
| LG011 | material_granularity_line | V003 00:51-01:30 | V003 明细表局部放大，高亮 estimated_comm / sales_signal / shop_score / product_score / refund_or_risk / listing_ready / video_ready / reason / evidence_note。 | aligned | 无核心改稿；执行时避免完整公开具体商品数据。 |
| LG012 | judgment_boundary_line | V003 00:33-00:48; V004 00:27-00:36 | 判断卡覆盖 V003/V004 表格背景，明确“不拍板，只缩小复查范围”。 | aligned_boundary_required | 无；本句必须保留。 |
| LG013 | result_transition_line | V004 00:00-00:06; V004 00:27-00:36 | V004 先展示 3 个方向，再切到“先确认 4 个商品卡”的排序/结果。 | aligned | 无核心改稿；“四个”有 V004 支撑，但必须标记为复查对象。 |
| LG014 | material_granularity_line | V004 00:09-00:24 | V004 留下原因画面，框选“佣金/可拍性/价格带/风险/继续核验”等依据。 | aligned_with_value_uncertainty | 把“至少有继续核验的空间”保留；不要改成“最适合我”。 |
| LG015 | material_granularity_line | V004 00:39-00:51 | V004 优先级表高清局部，重点看优先级、商品名、搜什么、复查重点。 | aligned_but_needs_zoom_or_reshoot | 无核心改稿；建议保留“复查表”而非“答案表”。 |
| LG016 | material_granularity_line | V003 00:00-00:06; V003 00:33-00:48; V003 00:51-01:30; V004 00:39-00:51 | Google Drive 文件列表短证据 + 候选表/明细表/复查表局部串联。 | aligned_with_privacy_mask_required | 无核心改稿；“云盘”有证据但必须遮挡。 |
| LG017 | material_granularity_line, judgment_boundary_line | V004 00:27-00:36; V004 00:39-00:51 | V004 复查结论背景 + 总结卡；如聊天框文字不可读，用卡片重述“复查对象/理由/风险/下一步”。 | aligned_if_card_paraphrase | 建议避免“最值得”绝对化，改为“当前更值得先复查”。 |
| LG018 | judgment_boundary_line | V001 01:27-01:33; V003 00:33-00:48; V004 00:27-00:51 | V001 AI 分析窗口 -> V003 表格 -> V004 复查结果，表现从建议到工作流的转换。 | aligned_with_boundary | 建议保留“如果能看页面/整理记录”条件感，不写成全部自动化事实。 |
| LG019 | judgment_boundary_line | card_supported_boundary_statement; V003 00:51-01:30; V004 00:39-00:51 | 大字边界卡覆盖表格背景，节奏放慢。 | aligned_boundary_required | 无；必须保留。 |
| LG020 | smooth_line, result_transition_line | V001 00:15-01:24; V004 00:27-00:51 | V001 商品卡混乱蒙太奇 -> V004 复查表，形成前后变化。 | aligned | 建议不要说“节省多少时间”，当前无量化证据。 |
| LG021 | smooth_line, ending_action | V004 00:39-00:51; card_supported_action_statement | V004 复查表局部 + 结尾行动卡。 | aligned_with_action_card | 建议 ChatGPT 复核“过了这张表，再拍”是否改为“我会先过这张表再拍”，降低普适命令感。 |
