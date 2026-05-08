# 当前仓库审计

## 审计边界

- 审计对象：`/Users/fan/Documents/视频工厂`
- 审计方式：只读检查真实存在的本地文件，不重跑脚本、不生成视频
- 本轮没有读取任何不存在的 `project_source/*` 文件
- 本轮没有修改任何代码文件

## 1. 已实际读取的真实文件

### 本地规范与说明

- `AGENTS.md`
- `README.md`

### 代码与依赖

- `package.json`
- `package-lock.json`
- `generate_demo.py`
- `video_builder.swift`
- `tests/test_generate_demo.py`

### 输入与产物

- `cases/demo.md`
- `dist/demo/script.txt`
- `dist/demo/captions.srt`

### 已确认存在但未按二进制内容展开读取

- `dist/demo/voice.mp3`
- `dist/demo/final.mp4`

### 当前已存在的 Codex 文档

- `codex_source/00_current_repo_audit.md`
- `codex_source/01_codex_source_plan.md`
- `codex_source/02_codex_index.md`

## 2. 已确认存在 / 不存在的目录与文件层

### 已确认存在

- `cases/`
- `dist/`
- `dist/demo/`
- `codex_source/`

### 已确认不存在

- `project_source/`
- 本地 `skills/` 目录
- `.git/`

## 3. 当前仓库真实存在的关键文件分别是什么

### 约束与说明层

- `AGENTS.md`
  - 当前仓库唯一明确的本地执行约束
  - 约束 demo 为中文、15 秒、PPT 风格、案例讲解
- `README.md`
  - 最小使用说明
  - 明确输入是 `cases/demo.md`，输出在 `dist/demo/`

### 代码链路层

- `generate_demo.py`
  - Python 主入口
  - 负责解析 markdown、生成脚本与字幕、调用配音和视频构建流程
- `video_builder.swift`
  - Swift 视频构建程序
  - 负责绘制静态 PPT 风格页面并合成最终视频
- `tests/test_generate_demo.py`
  - 最小单测
  - 覆盖 markdown 解析和 3 页计划生成
- `package.json`
  - 只声明了 `ffmpeg-static`
- `package-lock.json`
  - 锁定 Node 依赖

### 输入层

- `cases/demo.md`
  - 当前 demo 的唯一内容输入

### 产物层

- `dist/demo/script.txt`
- `dist/demo/captions.srt`
- `dist/demo/voice.mp3`
- `dist/demo/final.mp4`

### 文档层

- `codex_source/00_current_repo_audit.md`
- `codex_source/01_codex_source_plan.md`
- `codex_source/02_codex_index.md`

说明：

- 这说明当前仓库已经有一个启动中的 `codex_source/`
- 但仍然完全没有 `project_source/`

## 4. 哪些属于代码链路

- `generate_demo.py`
- `video_builder.swift`
- `tests/test_generate_demo.py`
- `package.json`
- `package-lock.json`
- `node_modules/ffmpeg-static/ffmpeg`

## 5. 哪些属于产物

- `dist/demo/script.txt`
- `dist/demo/captions.srt`
- `dist/demo/voice.mp3`
- `dist/demo/final.mp4`

## 6. 最小闭环是怎么跑通的

### 输入进入方式

- 内容从 `cases/demo.md` 进入
- `generate_demo.py` 将其解析成固定字段：
  - 标题
  - 视频参数
  - 目标用户
  - 原始问题
  - 关键动作
  - 前后变化
  - 结果
  - CTA

### 脚本与讲解生成

- `build_demo_plan()` 把输入压成固定 3 页结构
- 形成 3 段讲解文本：
  - 第 1 页：问题
  - 第 2 页：动作
  - 第 3 页：结果
- 同时准备：
  - `script.txt`
  - caption 列表

### 配音生成

- 使用 macOS `say` 生成分句音频
- 使用 macOS `afconvert` 转成 WAV
- 遍历多组语速，使总时长尽量贴近 15 秒
- 通过项目内 `ffmpeg-static` 输出 `voice.mp3`

### 字幕生成

- 依据真实音频时长写出 `captions.srt`
- 当前已确认字幕为 3 条，时间轴覆盖约 15 秒

### 视频生成

- `generate_demo.py` 写出 `manifest.json`
- `video_builder.swift` 读取 manifest
- 按 1080x1920、10fps 绘制 3 页静态 PPT 风格卡片
- 先导出纯视频
- 再与 `voice.mp3` 合成 `final.mp4`

### 当前可确认的闭环

`cases/demo.md`
→ `generate_demo.py`
→ 脚本 / 字幕 / manifest
→ `say` + `afconvert` + `ffmpeg-static`
→ `video_builder.swift`
→ `dist/demo/final.mp4`

## 7. 当前仓库更像什么阶段

结论：

- 当前仓库更像“最小 demo 仓库”
- 还不是“可复用内核仓库”

原因：

- 输入路径固定：`cases/demo.md`
- 输出路径固定：`dist/demo/`
- 脚本结构固定为 3 页
- 风格固定为简单 PPT 卡片页
- 依赖本地 macOS 系统能力
- 只有一个 demo 场景，没有抽象成多场景内核

## 8. 当前最明显缺口

### 项目脑层缺口

- 当前仓库没有 `project_source/`
- 因此没有本地项目脑入口、系统提示、场景模板、回审模板等文件

### Codex 执行层缺口

- 虽然 `codex_source/` 已存在
- 但还缺少真正可执行的入口与规则文件
- 例如：
  - Codex 层总说明
  - 执行边界
  - 运行与产物规则
  - skill 使用规则
  - 交付汇报规则

### 复用层缺口

- 当前没有 scene mode 抽象
- 当前没有多种脚本结构
- 当前没有把 demo 升成可复用视频内核的配置层

## 审计结论

这套仓库已经证明：

- 一个 15 秒中文 PPT 风格案例视频最小闭环是能跑通的
- 当前代码链路、输入文件、产物文件都是真实存在的

但当前仓库仍明确停留在：

- 已跑通的 demo
- 尚未补齐项目脑文件
- 尚未补齐 Codex 执行规则文件

因此下一轮最合理的方向，不是去假设不存在的 `project_source/*` 内容，而是先把缺失文件清单和建档顺序明确下来，再按顺序补齐。
