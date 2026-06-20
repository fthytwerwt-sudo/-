# 同步说明｜engineering_line_collaboration_gate（工程线协作闸门）

## 1. 本轮修正

本轮把原来的协作方式：

```text
把规则塞进 prompt，希望 AI 不要忘
```

升级为：

```text
用户给目标 / 红线 / 验收
ChatGPT 做任务层级与工程深度路由
Codex 把工程线落成文件 / 字段 / 节点 / 样例 / 验证 / 记录
```

## 2. 新增机制入口

- `engineering_line_collaboration_gate（工程线协作闸门）`
- `engineering_worth_question（值不值得工程化的入口问题）`
- `engineering_depth_router（工程深度路由器）`
- `decision_authority_matrix（决策权矩阵）`
- `per_file_detail_plan_gate（单文件细节方案闸门）`
- `execution_budget_gate（执行预算闸门）`
- `collaboration_effectiveness_check（协作有效性检查）`

## 3. 核心原则

`simple_tasks_stay_simple_complex_tasks_become_engineering_line（简单任务保持简单，复杂任务进入工程线）`。

不是每个任务都跑完整 13 层工程线：

- 简单任务走 `L0_light_chat（轻量聊天）`。
- 小修或小机制判断走 `L1_task_card（任务卡）`。
- 稳定节点 / 单脚本 / 单机制文件走 `L2_node_contract（节点契约）`。
- 长期多节点系统走 `L3_system_line（系统工程线）`。

## 4. 协作分工

- 用户：负责 `project_goal_change（项目目标改变）`、业务红线、验收标准、降级授权、发布或交付决策。
- ChatGPT：负责判断 `task_layer（任务层级）`、`engineering_depth（工程深度）`、缺失锚点、能否下发 Codex、Codex 回报真实性复审。
- Codex：负责补齐文件字段、`schema（数据契约）`、`fixture（测试样例）`、`validator（校验器）`、`failure_route（失败路由）`、`trace_log（链路记录）` 和低风险实现。

## 5. 本包边界

本包只同步机制文件、Codex 执行入口、日志和 GPT Project 上传资料，不生成媒体，不调用 TTS / 图片 / 视频 / 外部 API，不修改 `dist/latest_review_pack/`，不推进任何发布、内容、声音、视觉母版、发送或生产可用状态。
