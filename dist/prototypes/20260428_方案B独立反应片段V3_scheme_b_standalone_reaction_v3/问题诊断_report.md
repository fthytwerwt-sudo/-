# 方案 B 整页反应片段 V3 问题诊断报告

## 1. 本轮结论

- `已确认` 上一轮 V2 技术上生成成功，但视觉路线不符合用户当前要求。
- `已确认` V2 的核心问题不是 `ffmpeg` 编码问题，而是生成方式与剪辑逻辑问题。
- `已确认` V2 没有使用阿里万相 / 百炼图像生成或图生视频 API。
- `已确认` V2 使用的是本地程序绘图 + 叠加式 compositing，因此看起来像放大的贴图。
- `已确认` 本轮已尝试切换到万相 / DashScope 高质量生成路线，但当前本地配置中的 DashScope key 返回 `HTTP401 / InvalidApiKey`，V3 必须 blocked。
- `已确认` 本轮未继续使用本地 Mac 程序画人物，也未生成低保真替代图。

## 2. 上一轮 V2 人物图像如何生成

- `已确认` V2 不是调用高质量图像生成模型生成。
- `已确认` V2 未调用阿里万相、百炼、图像生成或图生视频 API。
- `已确认` V2 的人物与整页反应图来自 Codex 本地程序绘制：用本地图形绘制方式生成 `方案B整页反应页_full_page_reaction.png` 与透明人物层。
- `已确认` V2 没有提交可复用的独立模型调用脚本；产物记录在上一轮 run_summary 和 preview_report 中。
- `已确认` V2 只生成了 PNG 层和最终 15 秒 MP4，没有生成真正独立的 reaction clip 源视频。

证据路径：

- `/private/tmp/视频工厂_user_readable_map_sync/dist/prototypes/20260428_方案B整页反应版15秒预览_scheme_b_full_page_reaction_v2/run_summary.json`
- `/private/tmp/视频工厂_user_readable_map_sync/dist/prototypes/20260428_方案B整页反应版15秒预览_scheme_b_full_page_reaction_v2/方案B整页反应版说明_preview_report.md`
- `/private/tmp/视频工厂_user_readable_map_sync/codex_log/20260428_方案B整页反应版15秒技术预览.md`

## 3. 上一轮为什么像贴图

- `已确认` 剪辑方式问题：V2 虽然口径写成整页 reaction，但实际是把本地绘制的 reaction 画面合成到录屏片段中，并保留了模糊暗化录屏背景。
- `已确认` 背景问题：V2 report 明确写了“保留一层模糊暗化的录屏背景作为上下文”，这会天然产生 overlay 感。
- `已确认` 片段结构问题：V2 没有形成 `录屏片段 A -> 独立 reaction clip -> 录屏片段 B` 的剪辑结构。
- `已确认` 画面质感问题：人物线条、面部、身体、光影都来自本地程序绘制，质感接近低保真卡通图标，不像高质量生成模型出的整页 reaction。
- `已确认` 视觉层级问题：人物虽然变大，但仍是“角色图层 + 文字 + 放射背景”的局部合成逻辑，观感接近放大的贴图，而不是单独插入的视频镜头。

## 4. 上一轮是否满足“单独插入片段”

- `已确认` 不满足。
- `已确认` V2 的最终 MP4 中 reaction 出现在 `4.52s-5.92s`，持续 `1.40s`，但它不是独立生成的视频片段。
- `已确认` V2 产物中没有 `reaction_clip.mp4` 一类的独立片段文件。
- `已确认` 正确的 V3 结构必须是：录屏片段 A -> 独立 reaction clip -> 录屏片段 B，而不是在录屏上盖一层 PNG / 动画贴图。

## 5. 画质问题主因

- `已确认` 主因是源图质量：本地程序绘图低保真，不是高质量视觉生成模型。
- `已确认` 次因是剪辑结构：overlay compositing 让角色天然像贴图。
- `已确认` 不是单纯 `ffmpeg` 压缩问题；V2 输出为 `720x1280 / 15.00s`，技术解码正常，但源画面美术质量不足。
- `已确认` 没有使用图生视频模型，因此没有模型级动态质感，只能靠本地 bounce / shake 类动作模拟。

## 6. 当前阿里模型能力排查

### 6.1 Key 与配置

- `已确认` 环境变量中未发现以下 key：
  - `DASHSCOPE_API_KEY`
  - `DASHSCOPE_API_KEY_CN`
  - `BAILIAN_API_KEY`
  - `ALIBABA_CLOUD_ACCESS_KEY_ID`
  - `ALIBABA_CLOUD_ACCESS_KEY_SECRET`
- `已确认` 原始项目工作区存在未跟踪本地配置：`/Users/fan/Documents/视频工厂/config/formal_api_demo.local.toml`。
- `已确认` 该本地配置中存在 `auth.api_key` 字段、`provider = aliyun_bailian`、`image_generation.enabled = true`、`video_generation.enabled = true`。
- `已确认` 本轮没有打印、提交或泄露任何 key。

### 6.2 现有脚本能力

- `已确认` 项目已有 DashScope / 阿里视觉生成 helper：
  - `formal_api_demo_core.py`
- `已确认` 项目已有图像 / 视频生成相关脚本：
  - `scripts/元素娃娃线_round3_切换wan2.7与s2v闭环.py`
  - `scripts/元素娃娃线_round4_s2v_detect过检优化.py`
  - `scripts/元素娃娃线_round5_s2v_detect过检优化.py`
- `已确认` 现有脚本中出现模型：
  - `wan2.7-image-pro`
  - `wan2.7-image`
  - `wan2.7-i2v`
  - `wan2.2-s2v`
  - `wan2.2-s2v-detect`

### 6.3 本轮 API 实测结果

- `已确认` 本轮用现有 DashScope helper 尝试 `wan2.7-image-pro`。
- `已确认` `wan2.7-image-pro` 创建任务失败：`HTTP401 / InvalidApiKey`。
- `已确认` 本轮继续尝试 fallback `wan2.7-image`。
- `已确认` `wan2.7-image` 创建任务失败：`HTTP401 / InvalidApiKey`。
- `已确认` 因图像生成阶段已失败，本轮未进入 `wan2.7-i2v` 图生视频阶段。
- `已确认` 已保存脱敏尝试摘要：`wan_generation_attempts_sanitized.json`。

## 7. 正确 V3 路线

1. `图像生成模型`
   - 用阿里万相 / DashScope 生成高质量 9:16 整页 reaction page。
   - 推荐模型优先级：`wan2.7-image-pro` -> `wan2.7-image`。
   - 输出应是高质量原创 Q 版 AI 向导反应页，胸口无 `AI`，无文字 logo，不照抄已有 IP。

2. `图生视频模型`
   - 用 `wan2.7-i2v` 或可用的万相图生视频模型，把 reaction page 变成 1.5-2 秒独立片段。
   - 模型最短若只能生成 2 秒，则由 Codex 裁剪到 `1.4s-1.6s`。

3. `Codex 装配`
   - Codex 只负责调用模型、保存生成结果、裁剪、拼接、抽帧和报告。
   - 正确结构必须是：`round34 录屏片段 A -> 独立 reaction clip -> round34 录屏片段 B`。
   - 禁止再用本地程序绘制人物，禁止用录屏半透明 overlay 冒充整页 reaction。

4. `复审`
   - 生成后仍必须交给 ChatGPT / 用户复审人物表情、搞笑强度、画质和插入节奏。
   - 不能把技术生成成功写成方案 B 最终口径。

## 8. 本轮 V3 状态

- `已确认` V3 当前状态：`blocked`。
- `已确认` blocked 原因：本地配置存在 API key 字段，但 DashScope 实测返回 `HTTP401 / InvalidApiKey`。
- `已确认` 本轮未生成高质量整页反应图、未生成独立 reaction clip、未生成 15 秒 V3 预览。
- `已确认` 本轮不改正式 full、不改 `dist/latest_review_pack/`、不改 `content_validation`、不改 `send_ready`。

## 9. 下一步补齐建议

1. 在本地重新配置可用的 DashScope / 百炼 API key。
2. 建议优先使用环境变量或更新未跟踪本地配置，不能把 key 写进仓库。
3. 重新运行 V3 生成脚本：
   - `FORMAL_API_DEMO_LOCAL_CONFIG=/Users/fan/Documents/视频工厂/config/formal_api_demo.local.toml python3 scripts/方案B独立反应片段V3_wan_generation.py`
4. 生成成功后再进入独立片段装配与 15 秒预览验证。
