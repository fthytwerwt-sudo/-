# 展示路由规则

## 1. 文件定位

本文件用于把《视频工厂》的展示路由写成统一判断框架。

它解决的是：

- 一条视频整体应该偏什么主承载
- 每个 block 应该由谁承担
- 失败时如何回退
- 回审时如何判断是内容不过线，还是路由选错

它不是：

- 固定模板
- 固定真人次数模板
- 固定时长模板

## 2. 当前阶段边界

当前展示路由必须按以下边界理解：

- 当前主阶段是内容阶段，正往试发阶段过渡
- 当前正式默认主线是：
  - API 生成真人
  - 用户本地录制素材
  - 少量 PPT / 图片辅助
  - 云端剪辑
- 结构跟着文案走，不先预设整条视频固定载体顺序
- 人物出现 1 次还是 2 次，是 block 路由结果，不是预设模板
- 中段主体默认优先交给真实素材承担
- pure PPT / 信息卡仍可保留，但只属于次级支路
- AI talking avatar / 数字人口播，不再是默认主线
- 正式 assembly 继续固定为北京区 `OSS + 云剪 cloud-only`

## 3. 正式判断顺序

展示路由必须按以下顺序判断，不得跳步：

1. 先判内容类型
2. 再判整条视频的主价值
3. 再判观众最先需要接住什么
4. 再拆 block 职责
5. 最后才判每个 block 由谁承担

明确禁止：

- 先按个人偏好选真人或 PPT
- 因为“真人更高级”就默认真人
- 因为“PPT 更稳”就默认 PPT
- 因为当前 demo 是 15 秒，就把所有结构写死

## 4. 路由单位

展示路由的正式执行单位是 `block`。

整条视频只负责给出主策略，不负责把所有 block 压成同一种承载。

正式输出至少包含：

```text
video_routing_plan
- video_scene
- video_goal
- primary_value
- audience_need_first
- route_profile
- blocks
  - block_id
  - block_goal
  - block_need_first
  - block_carrier
  - asset_requirement
  - why_this_carrier
- fallback_rules
- review_diagnosis
```

## 5. L1：整条视频层

L1 负责回答：

- 这条视频整体更像什么内容
- 默认主承载应该偏什么

当前默认推荐值 `已确认`：

- `video_route_strategy = hybrid`
- `route_profile = api_human_local_footage_light_ppt_cloud_editing`

补充说明：

- `route_profile = api_human_local_footage_light_ppt_cloud_editing` 是当前正式默认主线
- `route_profile = pure_ppt_secondary` 只表示次级支路，不是默认主线

## 6. L2：block 层

L2 负责回答“每个 block 由谁承担”。

常见 block 职责与默认承载映射如下：

- 信任建立 -> `human`（默认由 API 真人承担）
- 关键判断 / 转折 -> `human`（默认由 API 真人承担）
- 过程演示 / 过程证据 -> `self_footage`
- 前后变化 / 现场感 -> `self_footage`
- 关键词显影 / 结构整理 / 结果句 -> `ppt_or_image`
- 结尾收束 / 最小行动 -> `human` 或 `summary_card`

L2 硬规则：

- 路由的真正执行单位是 block，不是整条视频的固定套路
- 人物出现 1 次还是 2 次，不预设
- 中段主体默认优先给真实素材承担
- PPT / 图片只负责整理、显影、总结，不抢主体叙事

## 7. L3：回退层

若当前展示形式不成立，默认按以下顺序回退：

- `human` 不成立：
  - 优先回退到 `hybrid`
  - 若当前更缺结构而不是信任，再回退到 `ppt_or_image`
- `self_footage` 不成立：
  - 优先补真实素材
  - 若短期无法补齐，只能诚实标记 `待素材注入验证`
  - 不得直接把整条视频偷换回 pure PPT 默认主线
- `hybrid` 不成立：
  - 优先保住 block 职责，再压回单一路由
- `ppt_or_image` 不成立：
  - 优先减负，只保留关键词、结果句、总结卡
  - 不得扩成培训课件感大段主体叙事

## 8. L4：回审层

L4 负责回答：

- 当前问题到底是内容不过线，还是路由选错
- 下一轮应继续同一路由，还是切路由

回审必问问题：

1. 这条内容更需要先接住“谁在说”，还是“过程证据”？
2. 中段主体是不是已经交给真实素材承担？
3. PPT / 图片是不是只做了整理 / 显影 / 总结？
4. 人物次数是不是由 block 职责推出来的，而不是模板强塞的？
5. 当前问题到底是内容不过线，还是展示路由错误？

## 9. 当前一句话规则

当前展示路由默认按“API 生成真人 + 用户本地录制素材 + 少量 PPT / 图片 + 云端剪辑”理解：结构跟着文案走，人物次数由 block 决定，hook / close 默认优先给 API 真人承担，中段主体默认优先给用户本地素材承担，pure PPT 与 AI talking avatar 都不再是默认主线。
