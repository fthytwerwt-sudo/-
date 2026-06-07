# 同步说明｜implementation_design_layer（实现设计层）

## 1. 本轮修正

本轮把原来的需求对齐链：

```text
目标层 -> 机制层 -> 流程层 -> 判断标准层 -> 反馈层
```

升级为：

```text
目标层 -> 机制层 -> 实现设计层 -> 流程层 -> 判断标准层 -> 反馈层
```

核心目标是避免 ChatGPT 在用户确认需求后直接下发 Codex prompt，却没有先判断 Codex 当前是否具备可执行工具路线、fallback 和验收标准。

## 2. 新增机制入口

- `implementation_design_layer（实现设计层）`
- `implementation_design_needed（需要实现设计层）`
- `blocked_need_implementation_design_layer`
- `implementation_design_request（实现设计请求）`

## 3. 关键约束

- Codex 不能把未验证的能力写成已确认能力。
- Codex 不能把 fallback 写成原目标已完成。
- Codex 不能把技术最小运行通过写成审美达标或内容通过。
- 对于卡片类视觉任务，`HyperFrames` 只能作为待验证首选路线，`image2` 只能作为待探测能力，静态 fallback 必须说明损失和授权边界。

## 4. 本包边界

本包只同步机制文件和日志，不生成媒体，不调用 TTS / 图片 / 视频生成 API，不修改 `dist/latest_review_pack/`，不推进任何发布、内容、声音或发送状态。
