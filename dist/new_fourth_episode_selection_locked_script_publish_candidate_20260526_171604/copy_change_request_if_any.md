# copy_change_request_if_any

`copy_change_request_required = true`

但本轮用户明确锁定文案且禁止改写，所以 Codex 不能自行修改，必须 blocked。

## Required If User Wants To Proceed Without补录

1. 将“我直接让 Codex 操作我的电脑，先帮我跑一轮选品初筛。”改为素材可支撑的表达，例如“我让 Codex / AI 先跑一轮选品初筛，把页面里的商品卡信息整理出来。”
2. 将“它是真的开始在我的电脑上操作。先进入选品页面。再输入品类词。然后一张一张翻商品卡。”改为可由现有页面/表格证据支撑的表达，或补录真实操作过程。
3. SKU 复杂度相关句子需要补素材，否则应改成“还要核 SKU 会不会太复杂”。

`copy_blocker = locked_copy_cannot_be_changed_by_codex`
