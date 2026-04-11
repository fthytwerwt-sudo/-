# 当前执行前上下文

## 1. 文件定位

本文件用于写清“当前阶段长期有效、但 Codex 不能靠聊天记忆默认知道”的执行前上下文。

## 2. 当前阶段

当前阶段 `已确认`：

- 技术闭环已跑通
- 当前重点不是“能不能生成视频”
- 当前重点是内容质量、结构稳定、可复用、可回审、可持续压质量
- 当前主阶段是内容阶段，正往试发阶段过渡

## 3. 当前正式默认主线

当前正式默认主线 `已确认` 为：

- API 生成真人
- 用户录制素材
- 少量 PPT
- 云端剪辑

并且固定按以下方式理解：

- 结构跟着文案走
- `API生成真人段` 出现 1 次还是 2 次，是 block 路由结果
- hook / close 默认优先给 API 真人承担
- 中段主体默认优先给用户录制素材承担
- pure PPT / 信息卡只保留为次级支路
- AI talking avatar / 数字人口播只保留为可选 / 待验证支线

## 4. 当前正式 assembly 口径

当前正式 assembly 口径必须诚实区分为：

- `已确认` 北京区 `OSS + 云剪 cloud-only` 继续是当前正式方向
- `待验证` 该方向是否已在当前 runtime / provider / 配置层稳定跑通，不能由本轮信息同步直接证明
- `已确认` `local preview` / `local mp4` 只能算辅助
- `已确认` 不得把本地预览或本地 mp4 写成正式完成态

## 5. demo 当前身份

当前 demo 的身份 `已确认`：

- demo 只是链路锚点
- demo 不是质量样片
- demo 不能定义整个项目未来质量下限

## 6. AI 知识类内容进入样片前的最低锁定项

进入样片执行前，至少先锁清：

1. 用户看完后能做什么
2. 用户看完后能判断什么
3. 最关键证据是什么
4. 最小行动 / 自检句是什么
5. 对应结尾总结卡类型是什么

否则：

- generation / assembly 成功，也不能写成内容过线

## 7. 当前必须诚实区分

当前执行层必须明确区分：

- 仓库口径已同步
- 新主线样片已验证成立
- 信息层已同步
- runtime / provider / 代码链路已验证成立

本轮如果只完成文档 / 规则 / 接手口径修复，只能说明：

- 仓库口径已同步
- 信息层已同步

不能说明：

- 新主线样片已验证成立
- `云端剪辑 / cloud-only` 已稳定跑通
- `API 生成真人` 已在某条具体 provider 链路验证成立

## 8. 当前主读取分支

当前仓库默认主读取分支固定为：

- `codex/user-readable-map`

只有同步回这个分支，才算新聊天默认正式已知。

## 8A. 当前待发对象 / 当前审核对象固定指针

凡任务命中以下任一情况，默认在 `codex_log/latest.md` 之后优先读：

- 当前待发对象
- 当前最新样片
- 发布线复核
- 当前唯一 blocker
- 只改这一条内容

固定指针文件：

- `codex_log/current_publish_target.md`

若需要当前样片的 Git 可追踪轻量证据，再补读：

- `codex_log/current_publish_target_light_evidence.md`

## 8B. 执行车道与并发建议来源

凡任务命中以下任一情况，默认补读：

- `execution lane`
- `parallel gate`
- 是否适合提速
- 是否适合并发
- `lane_recommendation`
- `parallel_recommendation`

优先读：

- `project_source/20_codex_multi_agent_routing_note_for_gpt_project.md`
- `codex_source/13_execution_lane_and_parallel_rules.md`

必须明确：

- `fast_lane` 不是默认无条件可用
- 并发不是默认无条件可用
- 条件失效时必须降级
- 提速 / 并发不等于 runtime 一定更快

## 9. 当前一句话上下文

当前执行层默认按“API 生成真人 + 用户录制素材 + 少量 PPT + 云端剪辑”理解项目：结构跟着文案走，`API生成真人段` 次数由 block 路由决定，`云端剪辑 / cloud-only` 只先算正式方向，不自动等于 runtime 已稳定跑通；命中当前待发对象 / 当前样片 / 发布线复核时，在 `latest.md` 之后优先看 `codex_log/current_publish_target.md`；命中提速 / 并发判定时，再看 `project_source/20...` 与 `codex_source/13...`；本轮信息同步若完成，只代表仓库信息层已更新，不代表代码、provider 或样片已验证成立。
