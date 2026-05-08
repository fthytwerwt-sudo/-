# main主线与项目中心价值口径统一报告

## 1. 本轮目标
- 统一《视频工厂》当前唯一远端主线 / 默认主读取分支为：`main`
- 统一当前项目中心价值为：`真实 AI 使用经验 + 工作提效实录`
- 将 `场景化专业输出工作包` 降级为：`可选沉淀单元 / 产品化承接单元`
- 保持视频产物、发布状态、`content_validation`、`send_ready`、`dist/latest_review_pack/` 不变

## 2. 修改前冲突
- 当前入口链中的 `AGENTS.md`、`codex_source/00_codex_readme.md`、`codex_source/01_execution_rules.md` 仍把 `codex/user-readable-map` 写成当前默认主读取分支或当前同步目标。
- 当前规则层中的 `codex_source/02_current_execution_context.md`、`03_research_findings_bridge.md`、`08_branch_sync_and_reading_branch_rules.md`、`12_codex_known_state_three_layer_rules.md`、`14_locked_reference_inheritance_rules.md`、`locked_reference_registry.md` 仍把旧分支写成当前正式同步目标。
- 当前事实与文案规则层中的 `GPT数据源/00`、`01`、`04`、`05`、`07`、`08`、`09` 仍保留“项目中心价值 = 场景化专业输出工作包”或“每条视频默认要长成工作包”的旧口径。
- `review_loop/records/` 已经出现“真实 AI 使用经验 + 结果差 + 工作提效实录”新口径，但当前正式入口层没有统一接住，导致入口层和复盘层口径打架。

## 3. 修改后口径

### 3.1 主线与同步口径
- `已确认` 当前唯一远端主线 / 默认主读取分支统一为：`main`
- `已确认` 当前“正式已知 / 默认接手已知 / 当前同步目标”统一改写为：`同步到 main`
- `已确认` 旧 `codex/user-readable-map` 只允许保留在历史日志或显式 `historical_branch_reference（历史分支引用）` 说明里

### 3.2 项目中心价值口径
- `已确认` 当前项目中心价值统一为：`真实 AI 使用经验 + 工作提效实录`
- `已确认` 当前视频默认角色统一为：`真实经验证明壳 / 提效证据入口壳`
- `已确认` `场景化专业输出工作包` 统一降级为：`可选沉淀单元 / 产品化承接单元`
- `已确认` 不再要求每条视频默认生成完整工作包
- `已确认` 当前优先验证：真实经验、工作提效证据、真实录屏、前后变化、小样本平台反馈、发布后复盘

### 3.3 文案与价值规则口径
- `已确认` 选题前置条件从“能自然长成工作包”改成“能提供真实 AI 使用经验 / 工作提效证据 / 前后变化”
- `已确认` `内容表达文案` 默认交付改成：内容表达结构包 + `4 段核心录制素材` + 结果差证明点 + 发布前风险检查要点
- `已确认` `三层 prompt 包`、`Prompt 引用尾卡`、`工作包正文 / 回审清单` 改成可选沉淀结构，不再是每条发布验证内容的硬前置
- `已确认` 只有出现高收藏 / 高评论 / 明确咨询 / 稳定可复用流程 / 强结果差时，才建议继续沉淀工作包

## 4. 修改文件清单
- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_source/02_current_execution_context.md`
- `codex_source/03_research_findings_bridge.md`
- `codex_source/08_branch_sync_and_reading_branch_rules.md`
- `codex_source/12_codex_known_state_three_layer_rules.md`
- `codex_source/14_locked_reference_inheritance_rules.md`
- `codex_source/locked_reference_registry.md`
- `codex_log/latest.md`
- `GPT数据源/00_项目总述.md`
- `GPT数据源/01_项目系统提示词.md`
- `GPT数据源/03_总索引与阅读顺序.md`
- `GPT数据源/04_选题与文案规则.md`
- `GPT数据源/05_文案路由规则.md`
- `GPT数据源/07_AI知识类视频价值规则.md`
- `GPT数据源/08_当前正式事实.md`
- `GPT数据源/09_目标态计划.md`

## 5. 保留不动文件清单
- `dist/latest_review_pack/`
- `codex_log/current_publish_target.md`
- `codex_log/current_publish_target_light_evidence.md`
- `GPT 数据源/`
- `/Users/fan/Documents/视频工厂归档+删除`
- 所有媒体、样片、音频、图片、原始素材
- 所有 `content_validation`、`send_ready`、当前发布状态字段

## 6. 未修改历史日志说明
- `codex_log/latest.md` 顶部追加了当前统一摘要，但没有大面积重写历史正文。
- `codex_log/latest.md` 中仍保留了大量 `codex/user-readable-map` 历史记录；这些条目仅代表历史执行事实，不再代表当前主线。
- 当前 grep 结果中保留的 `codex/user-readable-map` 只来自：
  - `codex_log/latest.md` 历史日志正文
  - `codex_source/00_codex_readme.md` 中对 `historical_branch_reference（历史分支引用）` 的显式说明

## 7. 验证结果
- `grep -R "codex/user-readable-map" -n AGENTS.md codex_source GPT数据源 codex_log/latest.md review_loop`
  - 当前规则层已不再把它写成默认主线；剩余命中只在 `codex_log/latest.md` 历史正文与 `codex_source/00_codex_readme.md` 的历史引用说明中
- `grep -R "当前项目中心价值.*场景化专业输出工作包" -n GPT数据源 AGENTS.md codex_source`
  - 无命中
- `grep -R "真实 AI 使用经验" -n GPT数据源 AGENTS.md codex_source codex_log/latest.md review_loop`
  - 当前入口、事实、文案、价值、latest 与 review_loop 记录均已命中
- `grep -R "工作提效实录" -n GPT数据源 AGENTS.md codex_source codex_log/latest.md review_loop`
  - 当前入口、事实、文案、价值、latest 与 review_loop 记录均已命中
- `python3 -m unittest discover -s tests -p 'test*.py'`
  - `已确认` `62 tests` 通过

## 8. 仍需用户确认项
- `已确认` 当前“工作包降级”为默认职责降级，不等于工作包路线被删除。
- `待用户确认` 后续若要继续向产品化承接推进，需要用户单独判断哪些高反馈内容值得沉淀为工作包，而不是让仓库默认每条都进入该路线。
- `待用户确认` 当前 `codex_log/current_publish_target.md` 仍保留历史主读取分支口径；由于本轮禁止修改该文件，它被视为已知尾巴，需另起一轮状态指针清理。
