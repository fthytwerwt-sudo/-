# 运行与产物规则

## 1. 文件定位

本文件用于记录当前仓库 demo 最小闭环的真实运行事实与产物判断口径。

它只基于当前仓库中已经存在的内容编写，包括：

- `README.md`
- `cases/demo.md`
- `generate_demo.py`
- `video_builder.swift`
- `tests/test_generate_demo.py`
- `dist/demo/` 现有产物

它不是当前正式主线的总代码能力说明，也不是面向未来所有视频引擎的泛化运行文档。

当前必须额外明确：

- 本文件描述的是 `dist/demo/*` 这条 legacy demo 运行事实
- 当前正式主线已切到：
  - API 生成真人
  - 用户录制素材
  - 少量 PPT / 图片
  - 北京区 `OSS + 云剪 cloud-only` 组装
- 因此 demo 运行事实不能再被偷换成正式主线已验证成立

## 2. 哪些内容是已确认事实，哪些只是规则说明

### 已确认事实

以下内容来自当前真实仓库：

- 默认输入文件路径
- Python 主入口
- Swift 视频构建器存在
- `ffmpeg-static` 依赖存在于 `package.json` / `package-lock.json`
- `dist/demo/` 下已存在脚本、字幕、配音、视频产物
- 当前仓库内无本地 `skills/`
- 当前环境已确认：
  - system `ffmpeg` 不可用
  - Node `v25.6.1` 可用
  - Python `3.9.6` 可用
  - `say` 可用
  - `afconvert` 可用
  - Swift `6.2.3` 可用

### 规则说明

以下内容属于执行层判断口径，不等于代码里已有自动保护：

- 哪些文件同时存在才算“成功”
- 发现部分产物时该如何汇报
- 哪些运行事实当前不应擅自改动
- 若后续要扩展，优先改哪一层

换句话说：

- “已确认事实”来自仓库
- “规则说明”来自 Codex 执行层对这些事实的使用方式

## 3. 当前最小闭环的真实输入

当前最小闭环的核心输入文件是：

- `cases/demo.md`

从当前文件内容可确认，它承载：

- 标题
- 视频参数
- 目标用户
- 原始问题
- 关键动作
- 前后变化
- 结果
- CTA

当前与代码实际强绑定的 demo 约束包括：

- 中文
- 15 秒
- PPT 演示风格
- 9:16 竖屏
- 3 页
- AI 配音
- 简体中文字幕
- 默认结构：问题 → 动作 → 结果

## 4. 当前默认运行入口

根据 `README.md`，当前最小闭环的默认运行入口是：

```bash
python3 generate_demo.py
```

这条信息是当前仓库事实说明，不构成本轮执行授权。

## 5. 当前真实运行链路

当前仓库内可确认的最小闭环链路如下：

1. `generate_demo.py` 读取 `cases/demo.md`
2. `parse_case_markdown()` 解析固定 markdown 字段
3. `build_demo_plan()` 生成 3 页讲解计划、脚本与 narration
4. `build_voice()` 检查系统命令：
   - `say`
   - `afconvert`
   - `swift`
5. `pick_best_voice_rate()` 用多组语速生成分句音频并试算时长
6. `concatenate_wavs()` 拼接 `segment_*.wav` 为 `voice.wav`
7. `resolve_ffmpeg()` 优先找 system `ffmpeg`，找不到再回退到项目内 `node_modules/ffmpeg-static/ffmpeg`
8. 输出 `voice.mp3`
9. `write_script_and_captions()` 输出：
   - `script.txt`
   - `captions.srt`
10. `write_manifest()` 输出 `manifest.json`
11. `build_video()` 调用 `swift video_builder.swift <manifest>`
12. `video_builder.swift` 读取 manifest，渲染静态 9:16 PPT 风格页面并合成音轨
13. 输出 `final.mp4`

## 6. 当前哪些文件分别负责什么

### `cases/demo.md`

- 当前 demo 的唯一内容输入

### `generate_demo.py`

- 解析 markdown
- 生成三页计划
- 生成 narration
- 生成脚本
- 生成字幕
- 生成 manifest
- 调用系统音频工具
- 调用 Swift 渲染器

### `video_builder.swift`

- 读取 manifest
- 渲染静态信息卡页面
- 输出 `video_only.mp4`
- 合成音轨
- 输出 `final.mp4`

### `tests/test_generate_demo.py`

- 覆盖 markdown 核心字段解析
- 覆盖三页计划生成

当前测试未覆盖：

- `say`
- `afconvert`
- `ffmpeg-static`
- Swift 合成
- 最终视频有效性

## 7. 当前真实依赖与环境前提

### 系统能力依赖

当前代码真实依赖以下系统能力：

- `python3`
- macOS `say`
- macOS `afconvert`
- `swift`
- Swift 框架：
  - `AVFoundation`
  - `AppKit`
  - `CoreImage`

### 项目内依赖

当前项目内关键依赖包括：

- `generate_demo.py`
- `video_builder.swift`
- `package.json`
- `package-lock.json`
- `node_modules/ffmpeg-static/ffmpeg`

### 当前已确认环境前提

已确认的环境事实是：

- system `ffmpeg` 不可用
- Node `v25.6.1` 可用
- Python `3.9.6` 可用
- `say` 可用
- `afconvert` 可用
- Swift `6.2.3` 可用

因此当前执行层必须把以下内容当事实：

- 不能假设 system `ffmpeg` 可用
- 当前 MP3 输出依赖项目内 `ffmpeg-static`
- 当前路线更依赖 macOS 原生能力，而不是跨平台方案

## 8. 当前真实产物路径与名称

### 已确认存在的最终产物

当前 `dist/demo/` 下已确认存在：

- `dist/demo/script.txt`
- `dist/demo/captions.srt`
- `dist/demo/voice.mp3`
- `dist/demo/final.mp4`

### 运行过程中会出现的中间产物

从当前代码可确认会生成或可能留下：

- `segment_*.aiff`
- `segment_*.wav`
- `voice.wav`
- `manifest.json`
- `video_only.mp4`

### 清理行为

从当前代码可确认：

- 只有当 `build_video(manifest_path)` 返回 `True` 时
  - `voice.wav` 会被删除
  - `manifest.json` 会被删除
- `video_only.mp4` 在 Swift 成功导出后会被删除

这意味着：

- 成功运行后，中间文件可能不保留
- 失败运行后，部分中间文件可能残留

## 9. 成功判定标准

### 最低成功标准

至少同时满足以下 4 项，才可判定本次最小闭环成功：

1. `dist/demo/script.txt` 存在
2. `dist/demo/captions.srt` 存在
3. `dist/demo/voice.mp3` 存在
4. `dist/demo/final.mp4` 存在

### 更可靠的成功标准

除“文件存在”外，还应确认：

1. `script.txt` 确实是三页脚本文本
2. `captions.srt` 含有效时间轴
3. `voice.mp3` 是有效音频文件
4. `final.mp4` 是有效 MP4 文件

### 明确不能单独依赖的判断

以下任一项都不足以单独证明整条链路成功：

- 测试通过
- Python 命令退出
- 某个中间文件生成过
- `voice.mp3` 已存在

特别注意：

从当前代码可确认，`build_video()` 在以下情况会返回 `False` 而不是抛出顶层错误：

- `video_builder.swift` 缺失
- Swift 子进程执行失败

而 `main()` 在这种分支下不会主动抛出新错误。

所以：

- 不能只根据脚本退出状态判定 `final.mp4` 已成功生成
- 必须实际检查最终产物

## 10. 当前质量基线与增强优先级

### 1. 当前 demo 的真实身份

- 当前 demo 只用于证明本地链路能跑通
- 当前 demo 是最小闭环验证件 / 运行锚点
- 当前 demo 不具备质量参考价值
- 当前 demo 不得被当作当前阶段的质量样片

### 2. 当前质量问题的真实判断

- 当前最主要问题不是“能不能生成视频”
- 而是“当前 demo 质量太差，无法作为质量参考件”
- 因此当前阶段不能继续以旧 demo 为质量基线讨论“下限标准”

### 3. “抖音 90 分标准”的真实定义

- 这是项目内部简称
- 不是平台官方评分体系
- 它指的是“接近抖音知识类 / AI 类 / 无人出镜短视频可推荐门槛”的质量水位
- 它更接近创作者 / 操盘手行业经验口径，不是官方数字评分
- 执行层不得把这句话写成官方规则或平台正式标准

### 4. 当前第一优先质量增强路线

- 当前第一优先是用户现成可用的火山引擎 TTS API
- 目标是先解决配音 demo 感 / 系统播报感
- 当前先接 TTS，不默认同时扩其他火山能力
- 当前“火山引擎一套”仅代表供应商统一优先，不代表本轮一次性接入整套能力

### 5. 当前“90 分标准”的执行层判断口径

#### 必须过线项

- 配音不再明显像系统播报
- 字幕与配音基本同步
- 开头 3 秒有效
- 内容不像说明书
- 画面不只是静态轮播
- 前后变化能被看懂
- 结尾有落点

#### 一票否决项

- 明显机械配音
- 字幕和配音明显不同步
- 全程像 PPT 轮播 / demo 演示
- 开头 3 秒没有钩子
- 内容高度模板化、像批量生产
- 画面明显低质或 AI 瑕疵
- 看完整条仍不知道表达什么

### 6. 当前路线停止线

- 当前不扩到平台发布 API
- 当前不扩到自动化运营
- 当前不扩到直播 / 平台化软件 / 数字人默认主承载
- 当前不把图生视频当第一优先
- 当前先把“机械配音”这一票否决项打掉，再看下一层质量增强

## 11. 常见失败点与如实反馈方式

以下失败点都有明确的当前仓库依据。

### 失败点 1：系统工具缺失

`generate_demo.py` 会显式检查：

- `say`
- `afconvert`
- `swift`

若缺失，会抛出：

- `RuntimeError("缺少系统命令：<tool>")`

如实反馈方式：

- 写明缺哪个命令
- 写明因此卡在配音或视频阶段
- 不把“前置环境缺失”写成“代码失败”

### 失败点 2：`ffmpeg` 无法解析

当前代码会优先找 system `ffmpeg`，找不到再找项目内 `ffmpeg-static`。

若两者都不可用，会抛出：

- `RuntimeError("缺少 ffmpeg，可通过 npm install 安装本项目依赖后再运行。")`

如实反馈方式：

- 写明 system `ffmpeg` 不可用是当前环境事实
- 写明是否缺少项目内 `node_modules/ffmpeg-static/ffmpeg`

### 失败点 3：输入 markdown 不完整但未必硬失败

当前 `parse_case_markdown()` 会解析固定标题，但不会对所有字段做强校验。

这意味着：

- `cases/demo.md` 缺字段时，流程不一定立刻报错
- 但脚本、字幕、页面内容可能退化为空或变弱

如实反馈方式：

- 把它归类为“输入内容问题”或“输入约束不满足”
- 不要因为脚本还能跑就写成“内容链路正常”

### 失败点 4：音频片段未生成

若没有可拼接的 WAV 片段，代码会抛出：

- `RuntimeError("没有可拼接的音频片段")`

如实反馈方式：

- 写明失败发生在配音拼接阶段
- 不要泛化成“整个视频系统不可用”

### 失败点 5：视频阶段部分失败

从当前代码可确认，若 Swift 渲染失败，可能出现：

- `script.txt` 已生成
- `captions.srt` 已生成
- `voice.mp3` 已生成
- `final.mp4` 不存在
- `manifest.json` / `voice.wav` 可能残留

如实反馈方式：

- 写成“文本与配音成功，视频合成未完成”
- 不要写成“整体已跑通”

### 失败点 6：测试通过但整链路未验证

当前测试仅覆盖：

- 字段解析
- 三页计划生成

如实反馈方式：

- 若只跑了测试，只能说“解析与计划层通过”
- 不能外推为“出片链路通过”

## 12. 当前哪些运行事实不应擅自改动

在未先更新项目脑与执行契约前，不应擅自改动：

- 默认输入 `cases/demo.md`
- 默认输出目录 `dist/demo/`
- 当前四件套最终产物集合
- 当前 3 页 demo 事实
- 当前依赖项目内 `ffmpeg-static` 的事实
- 当前以 macOS `say` / `afconvert` / `swift` 为核心的链路事实

更不能直接：

- 把 demo 自动升成多场景引擎
- 把当前结构误写成未来唯一结构
- 先重写 `video_builder.swift` 再谈抽象

## 13. 如果后续要扩到可复用内核，先改哪一层

如果后续要从当前 demo 扩到多场景可复用内核，推荐顺序是：

1. 先改 `project_source/`
   - 场景模式
   - 项目边界
   - 结构定义
2. 再改 `codex_source/`
   - 输入输出契约
   - 运行规则
   - 验证口径
3. 再改 Python 侧
   - 输入解析
   - 计划生成
   - 产物组织
4. 最后才评估是否需要调整 Swift 渲染层

当前最不应直接乱动的层是：

- `video_builder.swift`

原因是：

- 当前主要瓶颈不是“画面引擎太弱”
- 而是“场景抽象与执行契约还没先稳定”

## 14. 当前一句话规则

当前最小闭环的真实运行事实可以概括为：

**`cases/demo.md` → `generate_demo.py` → `say` / `afconvert` / 项目内 `ffmpeg-static` → `video_builder.swift` → `dist/demo/` 四件套产物。**

Codex 后续如果要动这条链路，必须先确认自己动的是哪一层；只要还没验证到 `final.mp4`，就不能把整条链路写成“已成功”。
