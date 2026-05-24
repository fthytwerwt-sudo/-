# copy_change_request_if_any

copy_change_request = required_before_formal_video_execution

## CCR001｜LG007｜“直接操作电脑”证据不足时需降级
- line_group_id: LG007
- current_text: 我直接让 Codex 操作我的电脑，先帮我跑一轮选品初筛。
- issue: 现有证据主要支持 AI/聊天窗口分析页面和结果整理，不足以证明完整无人值守电脑操作。
- repo_evidence: V001 01:27-01:33；V001 02:12-03:24。
- suggested_revision: 我让 Codex / AI 先跑一轮选品初筛，把页面里的商品卡信息整理出来。
- blocked_if_not_changed: 如果没有补录明确操作电脑画面，不能用“直接操作我的电脑”作为硬事实。

## CCR002｜LG004｜SKU 复杂不能伪装成画面事实
- line_group_id: LG004
- current_text: 但 SKU 太复杂，观众看完根本不知道该买哪一款。
- issue: 现有时间码不一定清晰显示 SKU 复杂度。
- repo_evidence: V001 02:12-03:24 为商品页/分析窗口，SKU 证明弱。
- suggested_revision: 有些品还要核 SKU 会不会太复杂，观众会不会不知道该买哪款。
- blocked_if_not_changed: 若无 SKU 局部补录，只能作为经验风险句。

## CCR003｜LG014 / LG017｜“最值得”要保留复查口径
- line_group_id: LG014, LG017
- current_text: 目前最值得先复查的是哪几个商品。
- issue: “最值得”容易被理解为最终推荐。
- repo_evidence: V004 00:27-00:51 支持复查优先级，不支持最终商品结论。
- suggested_revision: 当前更值得先复查的是哪几个商品。
- blocked_if_not_changed: 必须保留“复查”二字，不能改成“最适合/最值得拍”。

## CCR004｜LG003 / LG005｜成本、转化、售后只能写可能性
- line_group_id: LG003, LG005
- current_text: 时间成本可能回不来；转化也可能卡住；后面全是售后坑。
- issue: 这些是选品经验判断，不能绑定为某个商品事实。
- repo_evidence: V001 商品卡字段、V003 明细表字段支持风险维度，不支持具体商业结果。
- suggested_revision: 保留“可能/需要核/风险”表达，不写成确定结果。
- blocked_if_not_changed: 若字幕或卡片删掉“可能”，会变成过度承诺或负面断言。

## CCR005｜LG016｜云盘画面必须遮挡
- line_group_id: LG016
- current_text: 放到云盘里，我打开以后能看到清清楚楚的记录。
- issue: V003 Drive 画面可能暴露账号、路径、文件名。
- repo_evidence: V003 00:00-00:06；V003 表格段。
- suggested_revision: 可保留云盘表格表达，但正片必须遮挡账号/路径/敏感文件名。
- blocked_if_not_changed: 隐私不可遮挡时，禁止使用 Drive 文件列表画面。

## CCR006｜LG021｜结尾动作建议降低命令感
- line_group_id: LG021
- current_text: 过了这张表，再拍。没过这张表，就别浪费时间拍视频。
- issue: 作为泛化命令略强，可能像绝对方法论。
- repo_evidence: V004 复查表支持个人流程，不支持普适商业规则。
- suggested_revision: 我会先过这张表，再决定要不要拍；没过这张表，就先别急着拍。
- blocked_if_not_changed: 若作为强命令，需要保留“初筛/复查/我会”的语气边界。
