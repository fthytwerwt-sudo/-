# formal_api_demo 当前执行路线补丁（2026-04-05 更新）

## 1. 文件定位

本文件用于覆盖当前仓库里与 `formal_api_demo` 执行路线相关的旧口径冲突。

如果以下旧说法仍出现在仓库其他文件、旧日志或旧聊天摘要中：

- 视频 API 暂时不接
- 先纯本地出片
- `local assembly = 默认主路径`
- `cloud assembly = optional / skipped / 后续增强项`

则在 `formal_api_demo` 当前阶段，**以本文件为准**。

## 2. 当前最新拍板（高优先级）

当前正式口径不是“全本地、不接视频 API”。

当前正式口径是：

- **继续接 TTS API**
- **继续接图片 / 视频生成 API**
- **纯 PPT / 信息卡主线默认 assembly 路径升级为 `OSS + 云剪`**
- **`local assembly` 只保留为 fallback / 兜底路径**
- **当前暂不考虑动态 PPT，也不扩成复杂 motion design 路线**

## 3. 当前正式主路径

当前 `formal_api_demo` 的正式主路径应理解为：

文本需求
→ 脚本
→ 配音 API
→ 图片 / 视频生成 API
→ 纯 PPT / 信息卡母版
→ OSS + 云剪 assembly
→ 成片导出
→ 人工上传

必须明确：

- 这里不是“视频 API 暂时不接”
- 这里也不是“当前必须先把动态 PPT 或复杂动效做起来”
- 当前是“**生成层继续走 API，纯 PPT 主线的组装层默认走 OSS + 云剪，本地 assembly 仅作 fallback**”

## 4. generation 层与 assembly 层的最新分工

### A. generation 层

当前仍属于正式主链的一部分：

- TTS API
- 图片生成 API
- 视频生成 API
- 脚本 / 字幕 / 视觉计划

当前要求：

- 不要把 `image_generation.model` / `video_generation.model` 写成永远不重要
- 不要把视频 API 降成“暂时完全不接”
- generation 层仍应继续推进

### B. assembly 层

当前默认交付路径改成：

- `cloud_assembly` = 当前主路径
- `local_assembly` = fallback / 兜底路径

当前要求：

- `storage.space_name` / `assembly.template_id` 现在属于默认主路径前提
- 不得再把 `storage.space_name` / `assembly.template_id` 写成 optional
- 只有在云剪失败、模板异常、上传异常或任务超时时，才允许回退本地 assembly
- 当前升级只适用于纯 PPT / 信息卡主线，不自动外溢到动态 PPT 或数字人主线

## 5. 当前不再当硬前置的东西

以下内容当前仍不采用：

- 动态 PPT
- 复杂 motion design
- 高成本视觉特效路线

这不代表它们被永久删除，只代表：

**它们当前不属于纯 PPT 主线第一轮默认组装目标。**

## 6. 当前最实在的执行判断

当前阶段最重要的是：

1. generation 继续推进 API 化
2. 纯 PPT 主线的 assembly 默认走 `OSS + 云剪`
3. 本地 assembly 只保留 fallback / 兜底
4. 云剪第一轮只服务转场统一、字幕安全区、模板化 assembly、片头 / 正文 / 结尾模板化

## 7. 与旧口径冲突时怎么裁决

若以下几类文件与本文件冲突：

- 旧日志
- 旧执行判断
- 旧聊天接手摘要
- 旧“全本地 / 暂不接视频 API”表述

在 `formal_api_demo` 当前阶段，默认按以下顺序裁决：

1. 用户本轮最新拍板
2. 本补丁文件
3. 当前代码真实行为
4. 旧日志 / 旧摘要

## 8. 一句话版

当前 `formal_api_demo` 的最新正式路线是：

**视频 API 继续接；纯 PPT / 信息卡主线默认走 `OSS + 云剪` 组装，本地 assembly 只作 fallback；动态 PPT 仍暂不考虑。**
