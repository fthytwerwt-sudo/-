# 2026-04-02 Codex 侧尾巴清理：动态资料源同步规则

## 本轮目标

- 新增动态资料源同步规则文件
- 清理 `codex_source/01_execution_rules.md` 里的旧口径
- 更新 `codex_log/latest.md`，让最新交接只收口这轮尾巴清理结果

## 执行前已确认事实

- `codex_source/02_current_execution_context.md`
- `codex_source/03_research_findings_bridge.md`
- `codex_source/04_completion_and_review_contract.md`
- `codex_source/05_execution_deviation_and_reality_sync.md`

以上四份文件已经基本补到位，不是本轮主重写对象。

- 当前仓库已经存在 `codex_source/06_execution_gate_and_parallel_rules.md`。
- 因此本轮“动态资料源同步规则”不能占用 `06` 号位，否则会和执行闸门 / 并行规则冲突。
- `codex_source/01_execution_rules.md` 仍残留旧句：
  - “当前若涉及质量增强路线，默认第一优先看用户现成可用的火山引擎 TTS API”
- 这条旧句已经和当前正式主路径口径冲突，必须清掉。

## 实际读取

- `AGENTS.md`
- `codex_log/latest.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_source/02_current_execution_context.md`
- `codex_source/03_research_findings_bridge.md`
- `codex_source/04_completion_and_review_contract.md`
- `codex_source/05_execution_deviation_and_reality_sync.md`
- `codex_source/06_execution_gate_and_parallel_rules.md`
- `project_source/00_project_brief.md`
- `project_source/01_project_system_prompt.md`
- `project_source/03_perplexity_prompt_library.md`
- `project_source/06_project_index.md`
- `project_source/08_quality_baseline_and_90_score_rules.md`
- 全局 skill：
  - `using-superpowers`
  - `verification-before-completion`

## 实际改动

- 新建 `codex_source/09_dynamic_source_sync_rules.md`
  - 新增动态资料源定义
  - 新增三档同步分级：
    - A. 仅参考更新
    - B. 本轮执行更新
    - C. 长期前提更新
  - 分别写清命中条件、是否必须桥接、要写到哪里
  - 明确：
    - GPT 项目源内容不自动视为 Codex 已知
    - 会影响本轮执行的，要进 `03` 或本轮执行单
    - 会影响长期前提的，要同步更新 `02`
- 更新 `codex_source/01_execution_rules.md`
  - 在默认读取顺序中接入 `09_dynamic_source_sync_rules.md`
  - 新增 `EXEC-006F 动态资料源同步规则`
  - 在 `EXEC-008 最小必要背景包` 中清掉旧的火山 TTS 优先口径
  - 将 `EXEC-008` 统一成当前正式主路径：
    - 文本需求
    - 脚本
    - 配音 API
    - 图片 / 视频生成 API
    - 本地 assembly
    - 本地 mp4
    - 人工上传
  - 明确：
    - generation 继续接 API
    - assembly 当前默认走本地
    - cloud assembly 是后续增强项
    - demo 只证明链路跑通，不是质量样片
    - “抖音 90 分标准”是项目内部质量简称，不是平台官方规则
- 更新 `codex_log/latest.md`
  - 改成只收口这轮 Codex 侧尾巴清理结果
  - 写清 `02 ~ 05` 已补到位、本轮补了 `09`、本轮已清理 `01` 旧口径
- 新增本日志
  - 记录尾巴识别、文件命名原因、`01` 的具体清理项和 `latest` 的刷新结果

## 为什么 06 不能占用，要改成 09

- `codex_source/06_execution_gate_and_parallel_rules.md` 已真实存在
- 它负责：
  - 执行闸门
  - 自动补全边界
  - 多 Codex 并行规则
- 本轮新增内容负责的是：
  - GPT 项目源 / ChatGPT 侧动态资料何时必须同步进 Codex
- 两者职责不同
- 如果继续占用 `06`，会把“执行闸门”和“动态资料同步”混成一份
- 因此本轮改用不冲突的 `codex_source/09_dynamic_source_sync_rules.md`

## 01 里具体清了哪些旧口径

- 删掉了这条旧句：
  - “当前若涉及质量增强路线，默认第一优先看用户现成可用的火山引擎 TTS API”
- 没再把“火山 TTS 第一优先”当当前长期默认事实写进最小必要背景包
- 把最小必要背景包改回当前正式主路径，而不是旧的质量增强优先级口径

## 09 里新增了哪些同步规则

- 动态资料源的定义边界
- 三档同步分级
- 每一档的命中条件
- 每一档是否必须桥接进 Codex
- 每一档应该写到哪里
- GPT / ChatGPT 侧内容默认不自动同步给 Codex 的硬规则

## latest 如何更新

- 不再把上轮“02 ~ 05 初次补齐”当 latest 主叙事
- 改为强调：
  - `02 ~ 05` 基本已补到位
  - 本轮新增了 `09`
  - 本轮清理了 `01` 的旧口径
  - 当前 Codex 侧桥接机制已覆盖：
    - 执行前上下文
    - 研究结论桥接
    - 完成与回审契约
    - 执行偏差回写
    - 动态资料源同步规则

## 当前结果

- `codex_source/09_dynamic_source_sync_rules.md` 已真实创建
- `codex_source/01_execution_rules.md` 已不再保留“当前第一优先看火山引擎 TTS API”这类旧句
- `codex_log/latest.md` 已刷新为本轮尾巴清理结果
- 本轮未修改：
  - `formal_api_demo_core.py`
  - `tests/test_formal_api_demo_pipeline.py`
  - `project_source/*` 本体

## 下一步建议

- 以后只要 ChatGPT 侧新增了会影响执行的新内容，先按 `codex_source/09_dynamic_source_sync_rules.md` 判断分级，再决定是写 `03` 还是同步更新 `02`。
- 若未来还要继续清 Codex 侧旧索引，下一轮最值的是单独修 `codex_source/02_codex_index.md`，但这不属于本轮范围。
