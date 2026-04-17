# 元素娃娃线 round1 技术验收

- `technical_validation`：`passed_for_prototype`
- `content_validation`：`blocked`

## 已成立能力

- `已确认` 不是静态图：逐帧角色位置、头部姿态、嘴型和手势都发生变化
- `已确认` 不是轻微浮动：存在明确进入动作、判断动作和收束动作
- `已确认` 动态层 1：嘴型 / 口部开合
- `已确认` 动态层 2：手臂指向 + 头部点头
- `已确认` 额外动态：眨眼

## 仍未成立

- `待验证` 还不能证明已可直接替换主线 `seg01_hook / seg07_close_shell`
- `待验证` 当前口型仍属于音频能量驱动，不是更细的 viseme 级嘴型

## 结论

- `已确认` 当前仓库现在已经存在一条对体素娃娃成立的真动态路线：分层 2D 资产 + 时间线驱动 + 音频能量嘴型。
- `已确认` 本轮结果只算技术样片，不算主线内容过线。

## 输出

- `/Users/fan/Documents/视频工厂/dist/20260417_豆包的正确打开方式_vnext/host_motion_prototype_round1/renders/元素娃娃技术样片_round1.mp4`
- `/Users/fan/Documents/视频工厂/dist/20260417_豆包的正确打开方式_vnext/host_motion_prototype_round1/renders/元素娃娃技术样片_round1.gif`
- `/Users/fan/Documents/视频工厂/dist/20260417_豆包的正确打开方式_vnext/host_motion_prototype_round1/timeline/动作时间线_round1.json`
