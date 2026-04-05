# formal_api_demo 当前执行路线补丁（2026-04-05 cloud-only 版）

## 1. 文件定位

本文件用于覆盖当前仓库里与 `formal_api_demo` 执行路线相关的旧口径冲突。

如果以下旧说法仍出现在仓库其他文件、旧日志或旧聊天摘要中：

- 视频 API 暂时不接
- 先纯本地出片
- `local assembly = 默认主路径`
- `OSS + 云剪 = 默认，但 local assembly 仍可 fallback`
- `cloud assembly = optional / skipped / 后续增强项`

则在 `formal_api_demo` 当前阶段，**以本文件为准**。

## 2. 当前最新拍板（高优先级）

当前正式口径已经不是 cloud-first。

当前正式口径是：

- **继续接 TTS API**
- **继续接图片 / 视频生成 API**
- **纯 PPT / 信息卡主线 assembly 正式改为北京区 OSS + 云剪工程唯一主路径**
- **`local assembly` 已退出 pure PPT / 信息卡主线，不再作为 fallback / 兜底 / 应急正常交付**
- **当前暂不考虑动态 PPT，也不扩成复杂 motion design 路线**

## 3. 当前正式主路径

当前 `formal_api_demo` 的正式主路径应理解为：

文本需求
→ 脚本
→ 配音 API
→ 图片 / 视频生成 API
→ 纯 PPT / 信息卡母版
→ 北京区 OSS + 云剪工程 assembly
→ 成片导出
→ 人工上传

必须明确：

- 这里不是“视频 API 暂时不接”
- 这里也不是“当前必须先把动态 PPT 或复杂动效做起来”
- 当前是“**生成层继续走 API，pure PPT 主线的组装层只走北京区 OSS + 云剪工程 cloud-only**”
- 若缺密钥、缺云端参数或缺 provider implementation，必须如实 `blocked`
- 不得再把本地 preview / 本地 mp4 写成 pure PPT 主线的可接受补位结果

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

当前唯一可接受交付路径改成：

- `cloud_assembly` = 当前唯一主路径
- `local_assembly` = 旧路径 / 废弃路径 / 非当前主线

当前要求：

- 当前主线不再使用 `storage.space_name` / `assembly.template_id` 旧字段
- 当前主线改用明确的北京区 OSS / IMS / 云剪工程字段：
  - `aliyun_oss.bucket`
  - `aliyun_oss.region`
  - `aliyun_oss.endpoint`
  - `aliyun_oss.bucket_domain`
  - `aliyun_oss.access_key_id`
  - `aliyun_oss.access_key_secret`
  - `aliyun_oss.prefix_raw`
  - `aliyun_oss.prefix_final`
  - `aliyun_oss.prefix_temp`
  - `aliyun_ims.region`
  - `aliyun_ims.storage_address`
  - `aliyun_ims.cloud_project_name`
- 缺少上述字段时，当前主线必须直接 `blocked`
- 当前升级只适用于纯 PPT / 信息卡主线，不自动外溢到动态 PPT 或数字人主线

## 5. 当前北京区云端状态包

以下信息已确认，可写入 repo：

- OSS bucket：`zvip1-video-beijing`
- OSS region：`cn-beijing`
- OSS endpoint：`oss-cn-beijing.aliyuncs.com`
- OSS bucket domain：`zvip1-video-beijing.oss-cn-beijing.aliyuncs.com`
- OSS ACL：`private`
- RAM 用户：`video-factory-oss-1`
- IMS / ICE / 智能媒体服务：北京区已开通
- 功能体验月包：已生效
- 到期时间：`2026-05-05 05:00:00`
- IMS storage address：`zvip1-video-beijing.oss-cn-beijing.aliyuncs.com`
- 云剪工程名：`video-factory-ppt-master-v1`
- 云剪工程状态：草稿
- 编辑器可打开：是

必须同时明确：

- AccessKey / Secret 已生成，但仅保存在用户本地
- AccessKey / Secret 不得写入 repo
- 当前真实云端导出仍待本地注入密钥后验证

## 6. 当前不再当主线合法结果的东西

以下内容当前仍不采用：

- local preview 冒充正式 assembly success
- local mp4 冒充 pure PPT 主线正常交付
- local fallback 作为“云端先不通也没关系”的默认兜底
- 动态 PPT
- 复杂 motion design
- 高成本视觉特效路线

这不代表旧代码必须立刻完全删除，只代表：

**它们当前不属于 pure PPT / 信息卡主线的合法主链结果。**

## 7. 与旧口径冲突时怎么裁决

若以下几类文件与本文件冲突：

- 旧日志
- 旧执行判断
- 旧聊天接手摘要
- 旧“全本地 / local fallback / cloud optional”表述

在 `formal_api_demo` 当前阶段，默认按以下顺序裁决：

1. 用户本轮最新拍板
2. 本补丁文件
3. 当前代码真实行为
4. 旧日志 / 旧摘要

## 8. 一句话版

当前 `formal_api_demo` 的最新正式路线是：

**视频 API 继续接；pure PPT / 信息卡主线统一走北京区 `OSS + 云剪工程` cloud-only 组装；`local assembly` 已退出主线；真实云端导出仍待本地注入密钥后验证；动态 PPT 仍暂不考虑。**
