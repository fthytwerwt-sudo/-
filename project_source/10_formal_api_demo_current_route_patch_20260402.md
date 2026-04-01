# formal_api_demo 当前执行路线补丁（2026-04-02）

## 1. 文件定位

本文件用于覆盖当前仓库里与 `formal_api_demo` 执行路线相关的旧口径冲突。

如果以下旧说法仍出现在仓库其他文件、旧日志或旧聊天摘要中：

- 视频 API 暂时不接
- 先纯本地出片
- 只有把云端模板工厂 / 云端 assembly 跑通，当前阶段才算成立

则在 `formal_api_demo` 当前阶段，**以本文件为准**。

## 2. 当前最新拍板（高优先级）

当前正式口径不是“全本地、不接视频 API”。

当前正式口径是：

- **继续接 TTS API**
- **继续接图片 / 视频生成 API**
- **但最终默认交付路径是本地 assembly**
- **云端模板工厂 / 云端 assembly 降级为后续增强项，不是当前 0-1 硬前置**

## 3. 当前正式主路径

当前 `formal_api_demo` 的正式主路径应理解为：

文本需求
→ 脚本
→ 配音 API
→ 图片 / 视频生成 API
→ 本地 assembly
→ 本地 mp4
→ 人工上传

必须明确：

- 这里不是“视频 API 暂时不接”
- 这里也不是“当前必须先把云端模板工厂 / 云端 assembly 跑通”
- 当前是“**生成层继续走 API，组装层当前默认走本地**”

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

- `local_assembly` = 当前主路径
- `cloud_assembly` = optional / skipped / 后续增强项

当前要求：

- 本地 assembly 成功后，当前阶段应允许整体成功
- `storage.space_name` / `assembly.template_id` 未配置时，不应反向卡死当前本地主链

## 5. 当前不再当硬前置的东西

以下内容当前仍有价值，但不再是当前阶段的硬前置：

- `storage.space_name`
- `assembly.template_id`
- ICE 模板工厂
- 云端 assembly
- 云端剪辑模板路线

这不代表它们被永久删除，只代表：

**它们当前属于后续增强项，不得先于“API 生成 + 本地 assembly 出片”成为主阻塞。**

## 6. 当前最实在的执行判断

当前阶段最重要的是：

1. generation 继续推进 API 化
2. assembly 保证本地 mp4 稳定交付
3. 先把整条 0-1 跑顺
4. 后续如果值得，再继续接云端 assembly

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

**视频 API 继续接，但默认本地 assembly 交付；云端模板工厂 / 云端 assembly 不再是当前阶段硬前置。**
