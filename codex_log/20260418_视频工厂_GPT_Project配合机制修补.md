# 20260418｜视频工厂 GPT Project 配合机制修补

## read_files

- `已确认` 已读：
  - `AGENTS.md`
  - 当前仓库本地 `skills/` 状态
  - `codex_source/00_codex_readme.md`
  - `codex_source/01_execution_rules.md`
  - `codex_log/latest.md`
  - `GPT数据源/00_项目总述.md`
  - `GPT数据源/01_项目系统提示词.md`
  - `GPT数据源/03_总索引与阅读顺序.md`
  - `GPT数据源/06_当前主线锚点_API生成真人_用户录制素材_少量PPT_云端剪辑.md`
  - `GPT数据源/08_当前正式事实.md`
  - `GPT数据源/09_目标态计划.md`
  - `codex_log/20260418_豆包vnext_C线元素娃娃能力审计.md`
  - `codex_log/current_publish_target.md`

## skills_check

- `已确认` 当前仓库本地 `skills/` 目录不存在。
- `已确认` 已回退检查全局 `~/.codex/skills`。
- `已确认` `using-superpowers` 已命中并使用：用于先做 skill / 上下文检查，再开始审计与修改。
- `已确认` `context-driven-development` 已命中并使用：用于把项目机制、项目事实与默认接手口径当成需要同步维护的上下文工件处理。
- `已确认` `verification-before-completion` 已命中并使用：用于约束本轮 `git diff --check`、关键文件回读、commit / push、reading branch 校验都必须拿到实际证据后再汇报。

## current_gap_audit

- `已确认` `GPT数据源/01_项目系统提示词.md` 仍以原则性表述为主，尚未把“项目态账号层硬执行”写成强触发规则。
- `已确认` `GPT数据源/08_当前正式事实.md` 仍把 `dist/formal_api_demo_doubao_task_clear_20260412/local_review/final_review_clean.mp4` 写成“当前最新样片状态”，与当前 `vNext` 复审阶段口径不一致。
- `已确认` `GPT数据源/09_目标态计划.md` 尚未写清 C 线进入 `round2` 的前置闸门仍是“角色资产能力”而不是“继续调动作”。
- `已确认` `AGENTS.md` 原文里尚未补出“命中《视频工厂》后，项目态账号层规则不降级；机制问题先答机制层”的最小硬句。
- `已确认` `codex_log/latest.md` 仍以 C 线审计轮为主，没有把本轮“Project 配合机制守门层 / 事实层同步层修补”写成主结论。
- `已确认` `codex_log/latest.md` 与 `codex/user-readable-map` 当前不一致；当前分支里的 C 线能力审计与 `latest` 更新尚未全部同步回 reading branch。
- `已确认` 当前存在旧机制残留：`codex_log/current_publish_target.md` 仍指向 `20260412` 旧样片，并把它写成“当前最新样片已过线”，与当前 `vNext` 复审阶段口径冲突。
- `部分成立` `codex_log/20260418_豆包vnext_C线元素娃娃能力审计.md` 已把 C 线能力边界写清，但在同步回 `codex/user-readable-map` 前，这些结论仍不能自动算项目正式已知。

## modified_files

- `已确认` 本轮计划修改：
  - `GPT数据源/01_项目系统提示词.md`
  - `GPT数据源/08_当前正式事实.md`
  - `GPT数据源/09_目标态计划.md`
  - `AGENTS.md`
  - `codex_log/latest.md`
- `已确认` 本轮计划新增：
  - `codex_log/20260418_视频工厂_GPT_Project配合机制修补.md`
  - `codex_log/20260418_视频工厂_Project指令补丁_账号层硬执行.md`

## rule_mapping

- `已确认` 已压入 `GPT数据源/01_项目系统提示词.md` 的规则：
  - 机制问题先答机制层
  - 项目态账号层规则不降级
  - `feature-only` 未同步不算正式事实
  - 外部资料 / 原感稿执行“保真提取 / 保真收束”，原感层 `[LOCKED]`
  - 路线未证实 / only prototype / demo 感先做能力审计
  - Codex 默认不知道聊天新增信息与外部资料，未桥接不得下发
- `已确认` 已压入 `GPT数据源/08_当前正式事实.md` 的规则：
  - `20260412` 旧样片降为“历史通过样片 / 历史口径”
  - 当前 `vNext` 正式状态、B 线 `E1 / E2 / E3`、C 线 `round1 = passed_for_prototype`
  - 当前项目 / 当前已接模型能力边界与最高优先级 blocker
- `已确认` 已压入 `GPT数据源/09_目标态计划.md` 的规则：
  - C 线进入 `round2` 前先补视频级角色资产能力
  - 最小能力验证只回答 `detect` 与最低可用线两个问题
  - 新资产过不了 `detect` 或仍然明显是 `gif` 感时停止当前路线
- `已确认` 已压入 `AGENTS.md` 的规则：
  - 命中《视频工厂》后，账号层长期规则仍按硬约束执行；机制问题先答机制层
- `已确认` 已压入 `codex_log/latest.md` 的规则：
  - 本轮主结论切换为 Project 配合机制守门层 / 事实层同步层修补
  - 默认接手建议补入本轮 dated log 与 Project 指令补丁文件

## project_instruction_patch_file

- `已确认` 可直接粘贴文件为：`codex_log/20260418_视频工厂_Project指令补丁_账号层硬执行.md`
- `已确认` 该文件只保留可直接粘贴的补丁规则，不写审计过程。

## reading_branch_sync_status

- `已确认` 执行前状态：
  - `codex/user-readable-map` 已落后于当前分支的 `codex_log/latest.md`
  - `codex_log/20260418_豆包vnext_C线元素娃娃能力审计.md` 尚未进入 reading branch
  - 本轮两份新机制文件执行前不存在
- `待验证` 执行后状态：
  - 待本轮 commit / push 完成后，再同步回 `codex/user-readable-map` 并用 `git show codex/user-readable-map:路径` 复核

## remaining_old_mechanisms

- `已确认` `codex_log/current_publish_target.md` 仍保留“旧样片就是当前待发对象”的旧机制口径。
- `已确认` 该文件不在本轮允许修改名单内，因此本轮只显式标记冲突，不在此轮内直接改写。
- `部分成立` reading branch 在本轮同步前，仍会保留部分旧接手口径；本轮同步完成后可以先消除 `latest / 01 / 08 / 09 / patch log` 这一层缺口。

## final_state

- `待验证` 本轮目标是：
  - 生成可直接粘贴的 Project 指令补丁文件
  - 对齐 `01 / 08 / 09 / AGENTS / latest`
  - 同步更新 `codex/user-readable-map`
  - 不新增第 `11` 份 root 执行包
