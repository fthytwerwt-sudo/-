# 元素娃娃线 round1 最小技术方案

## 角色层

- 头部主层：`head_base.png`
- 身体主层：`body.png`
- 嘴型层：`mouth_closed / mouth_mid / mouth_open`
- 第二动态层：`arm_down / arm_point`
- 额外层：`blink_overlay`

## 动作语法

- `进入动作`：0.0s-0.6s，角色从左侧滑入并完成落位
- `动态层1`：嘴型按音频能量三档驱动
- `动态层2`：判断段切换为指向手势，头部轻点头
- `判断动作`：2.0s-3.2s arm_point + head tilt
- `收束动作`：3.2s 之后头部回正，手臂回落

## 测试音频

- 复用当前 vNext 正式线已有短口播：`voice_candidates_round4/E1/E1_processed.wav` 前 4.2 秒

## 验证目标

- 不是静态图
- 不是全图轻微浮动
- 至少两种动态层同时成立
- 进入 / 判断 / 收束 三段成立
