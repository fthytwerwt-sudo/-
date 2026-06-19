# Minimum Loop Project Adjustment Backlog

```yaml
project_adjustment_backlog（项目调整待办）:
  status（状态）: recorded_only_pending_user_chatgpt_discussion（仅记录，等待用户 / ChatGPT 商议）
  current_round（本轮）: V006_human_review_minimum_loop（V006 人审最小闭环）
  current_round_action（本轮动作）: record_only_do_not_fix（只记录，不修复）
  last_updated（最后更新）: 2026-06-18
  items（事项）:
    - item（事项）: current_task_selector（当前任务选择器）
      problem（问题是什么）: 需要把“继续既有候选人审”和“启动下一条新视频”拆成显式选择。
      why_affects_minimum_loop（为什么影响最小闭环）: 如果没有显式选择，V006 人审、下一条新视频、旧候选复用会混成同一条执行链。
      why_not_fix_this_round（本轮为什么不修）: 用户明确要求本轮先继续 V006 人审最小闭环，4 个入口问题之后再和 ChatGPT 商议。
      later_decision_needed（之后要决定什么）: 是否新增一个最小任务选择字段；默认值如何设定；由用户、ChatGPT 还是 Codex 在哪一层选择。
      current_status（当前状态）: backlog_recorded_only（仅记录）
    - item（事项）: prewrite_copy_decision_card（写前文案决策卡）
      problem（问题是什么）: 新视频进入候选前必须有目标、标题、核心判断、允许改动和禁止改动。
      why_affects_minimum_loop（为什么影响最小闭环）: 没有写前卡，Codex 无法判断文案可执行性，也容易越权改语义。
      why_not_fix_this_round（本轮为什么不修）: 本轮不启动新视频，不生成新候选，不需要建立新视频写前卡。
      later_decision_needed（之后要决定什么）: 写前卡字段、触发条件、谁确认、缺字段时是否 blocked。
      current_status（当前状态）: backlog_recorded_only（仅记录）
    - item（事项）: material_binding_card（素材绑定卡）
      problem（问题是什么）: 素材必须绑定当前任务，不能默认继承旧候选素材。
      why_affects_minimum_loop（为什么影响最小闭环）: 缺绑定会让旧候选素材被误当成新任务证据，破坏 source_readback 和素材证据链。
      why_not_fix_this_round（本轮为什么不修）: 本轮只审 V006 既有候选，不替换素材，不做新素材装配。
      later_decision_needed（之后要决定什么）: 素材绑定卡字段、旧素材复用条件、缺素材时是否允许无素材 preflight 包。
      current_status（当前状态）: backlog_recorded_only（仅记录）
    - item（事项）: authorization_card（授权卡）
      problem（问题是什么）: 真实 RAG、TTS、外部 API、媒体生成必须逐项写明 allowed / forbidden。
      why_affects_minimum_loop（为什么影响最小闭环）: 授权不清会让 Codex 误启真实外部调用、TTS 或媒体生成，也会把 probe / dry run 误写成真实产出。
      why_not_fix_this_round（本轮为什么不修）: 本轮不调用外部 API，不调用 TTS，不真实调用 DashVector / Chroma，不生成媒体。
      later_decision_needed（之后要决定什么）: 默认授权是否全部 false、授权字段格式、授权有效期、每轮如何回读。
      current_status（当前状态）: backlog_recorded_only（仅记录）
```

## Boundary（边界）

- 本文件只是待商议 backlog（待办清单），不是机制实现。
- 本轮未新增 schema（结构契约）、fixture（测试样例）或 probe（探测脚本）。
- 本轮未修改 `codex_source/`、`GPT数据源/` 或 V006 复审包。
