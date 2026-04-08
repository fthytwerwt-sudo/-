# 20260409_gpt_project_value_rules_bridge

## 本轮目标

- 把 GPT Project 侧新增 / 重写的 4 份规则文件，正式桥接进 codex 侧执行层。
- 让后续 Codex 在脚本、block 路由、结尾卡选择、样片是否值得进入执行、样片验收时，按新版价值规则工作。
- 更新 `latest`、写日志、commit 并 push 当前分支。

## 执行前已确认事实

- 本轮是项目文件修改任务，不改代码能力、不改 tests、不改 case、不改 config 的运行逻辑。
- 当前仓库默认主线仍是：
  - 人物
  - 用户真实录制素材
  - 少量 PPT / 图片辅助
- 当前正式 assembly 仍固定为北京区 `OSS + 云剪 cloud-only`。

## 实际读取

- `AGENTS.md`
- `codex_log/latest.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_source/02_current_execution_context.md`
- `codex_source/03_research_findings_bridge.md`
- `project_source/08_quality_baseline_and_90_score_rules.md`
- `project_source/02_scene_mode_templates.md`
- `project_source/05_psychology_execution_rules.md`
- `project_source/16_presentation_routing_rules.md`
- `project_source/24_human_self_footage_light_ppt_routing_rules.md`
- `codex_source/07_formal_api_demo_target_plan.md`
- 本地仓库 `skills/`：不存在
- 全局 skill：
  - `verification-before-completion`
  - `using-superpowers`
  - `systematic-debugging`

## 真实仓库状态冲突

- `已确认`
  - `project_source/08_quality_baseline_and_90_score_rules.md` 当前分支存在
- `待同步`
  - `project_source/21_topic_selection_and_copywriting_rules.md` 当前分支不存在
  - `project_source/22_copy_mode_routing_rules.md` 当前分支不存在
  - `project_source/25_ai_knowledge_video_value_rules.md` 当前分支不存在

因此本轮只能写成：

- GPT Project 正式规则已桥接进 codex 侧
- 不能写成 project_source 已全量同步完成
- 不能写成这些规则已经被样片验证成立

## 缺口审计结论

本轮审计前，codex 侧存在以下缺口：

- `顶层入口缺口`
  - `codex_source/00_codex_readme.md` 未明确“4 类内容不同价值交付 / 不同结尾卡”
- `当前执行上下文缺口`
  - `codex_source/02_current_execution_context.md` 未显式写入“看完必须有收获”的价值底线
  - 未显式写入样片前四问
- `bridge 缺口`
  - `codex_source/03_research_findings_bridge.md` 未桥接这轮 GPT Project 新规则
- `latest 接手缺口`
  - 新会话无法从 `latest` 一眼读到：
    - 4 类内容不同交付
    - 不同结尾卡
    - 不同证据线
    - “技术可行 ≠ 内容过线”

## 实际改动

- 修改：
  - `codex_source/00_codex_readme.md`
    - 补入口级说明
    - 新增对 `codex_source/11_ai_knowledge_video_value_bridge.md` 的读取提示与文件说明
  - `codex_source/01_execution_rules.md`
    - 新增样片类任务执行前四锁
    - 新增读取 `codex_source/11_ai_knowledge_video_value_bridge.md` 的条件
  - `codex_source/02_current_execution_context.md`
    - 新增 AI 知识类内容价值底线
    - 新增 4 类内容不同价值交付与结尾卡映射
  - `codex_source/03_research_findings_bridge.md`
    - 新增 `BRIDGE-20260409-01`
  - `codex_log/latest.md`
    - 改写为新版价值规则接手摘要
- 新增：
  - `codex_source/11_ai_knowledge_video_value_bridge.md`
  - `codex_log/20260409_gpt_project_value_rules_bridge.md`

## 为什么需要新增 bridge 文件

- 当前分支缺失 `project_source/21/22/25`
- 仅改 `00/01/02/03/latest` 容易让后续会话只看到摘要，丢失 4 类内容的完整映射
- 因此新增 `codex_source/11_ai_knowledge_video_value_bridge.md` 作为“缺失 project_source 文件的 codex 侧稳定承接点”
- 它不是新增项目脑正文，只是执行层桥接件

## 当前结果

- `已确认`
  - codex 侧现在已经明确知道：
    - AI 项目讲解 / AI 方法分享 / AI 学习实操 / AI 案例拆解 的交付不同
    - 不同类型内容的结尾卡不同
    - 不同类型内容的证据线不同
    - “看完必须有收获”是正式过线要求
    - 没有动作 / 没有判断 / 没有证据 / 没有自检，不算过线
- `部分成立`
  - 当前 project_source 只同步了 `08`
  - `21/22/25` 仍待后续真实回流到当前分支

## 实际验证

- `git diff --check`
- `rg` 核对以下关键词已进入 codex 侧：
  - `AI 项目讲解 / AI 方法分享 / AI 学习实操 / AI 案例拆解`
  - `judgment_card / steps_error_card / steps_card`
  - `看完后能做什么 / 看完后能判断什么 / 证据是什么 / 最小行动或自检句是什么`

## 下一步建议

- 若下一轮继续做样片或脚本，先读：
  - `codex_source/11_ai_knowledge_video_value_bridge.md`
  - `codex_source/02_current_execution_context.md`
  - `codex_log/latest.md`
- 若下一轮需要把 GPT Project 规则完整回流到 project_source，再单独补 `project_source/21/22/25` 真文件，不在本轮假装已同步。
