# 20260424｜不放大完整可读布局修复

## 1. 任务结论

- `已确认` 本轮修复目标是：每一拍在 1x 不放大默认视图下，至少完整显示本拍应该表达的全部信息。
- `已确认` 本轮没有修改《视频工厂》正式主线。
- `已确认` 本轮没有把 `云端剪辑` 写成已稳定跑通事实。

## 2. 本轮读取

- `已确认` 已读取 `AGENTS.md`。
- `已确认` 已读取 `codex_source/00_codex_readme.md`。
- `已确认` 已读取 `codex_log/latest.md`。
- `已确认` 已读取 `codex_source/01_execution_rules.md`。
- `已确认` 已读取 `GPT 数据源/00_项目总述.md`。
- `已确认` 已读取 `GPT 数据源/01_项目系统提示词.md`。
- `已确认` 已读取 `GPT 数据源/02_术语定义与状态边界.md`。
- `已确认` 已读取 `GPT 数据源/03_总索引与阅读顺序.md`。
- `已确认` 已读取 `GPT 数据源/05_文案路由规则.md`。
- `已确认` 已读取 `GPT 数据源/06_当前主线锚点_API生成真人_用户录制素材_少量PPT_云端剪辑.md`。
- `已确认` 已读取 `GPT 数据源/08_当前正式事实.md`。
- `已确认` 已读取 `codex_source/05_runtime_and_artifact_rules.md`。
- `已确认` 已读取 `generate_demo.py`、`video_builder.swift`、`tests/test_generate_demo.py`。
- `已确认` 仓库本地 `skills/` 目录未找到相关 skill，已回退读取全局 `systematic-debugging` 与 `verification-before-completion`。
- `待验证` `codex_source/02_current_execution_context.md`、`codex_source/03_research_findings_bridge.md`、`codex_log/current_publish_target.md`、`codex_log/current_publish_target_light_evidence.md` 在当前分支可见范围内未找到。

## 3. 根因判断

- `已确认` 当前 `main` 可追踪代码中的真实最小渲染链路是：`cases/demo.md -> generate_demo.py -> video_builder.swift -> dist/demo/`。
- `已确认` 旧链路在写 manifest 前没有 `no_zoom_completeness` 检查，因此文本高度超过单拍容量时不会先拆拍。
- `已确认` 旧 Swift 渲染器按固定正文行高绘制，长行换行后存在被正文矩形裁切的风险。
- `已确认` 旧链路没有输出 `layout_metrics`，无法区分 `technical_validation` 与 `content_validation`。
- `部分成立` 用户截图中的专用标签文案 `当前在看 / 正确做法 / 拆两拍` 未在当前 `main` 可追踪源码中命中；本轮以仓库当前可确认渲染入口做机制修复和最小验证样例。

## 4. 修改内容

- `generate_demo.py`
  - 新增渲染前高度估算、`safe_area` 容量检查、自动拆拍、`layout_metrics` 输出。
  - 新增 `--layout-fixture`，用于生成接近用户截图的 1x review 最小验证样例。
- `video_builder.swift`
  - 正文绘制改为按实际文字高度计算，不再用固定 110px 文本框硬画。
  - 新增 `reviewImageDir` / `reviewOnly`，可直接导出 1x 默认视图 PNG。
  - 修正 review PNG 为 1080x1920 的 1x 输出，避免 Retina 2x 导出误判。
  - 提升标题可读性，并让 footer 文本避开右侧页码区。
- `tests/test_generate_demo.py`
  - 新增 no_zoom validation fixture 测试，锁定超高信息块必须在渲染前拆成多拍。
- `.gitignore`
  - 忽略默认 demo 运行时生成的本地 review 图与布局指标，避免每次验证后留下无关脏文件；本轮正式复审产物保留在 dated validation 目录。
- `dist/20260424_不放大完整可读_no_zoom_completeness/`
  - 新增本轮人工复审用 1x 默认视图 review 图与 `layout_metrics`。

## 5. 验证结果

- `已确认` `python3 -m unittest tests/test_generate_demo.py` 通过，3 个测试通过。
- `已确认` `python3 generate_demo.py --layout-fixture` 通过，生成 2 张 1x review 图。
- `已确认` `python3 generate_demo.py` 通过，默认 demo 链路仍可生成 `final.mp4`。
- `已确认` `git diff --check` 通过。
- `已确认` 最小验证样例 `layout_metrics` 关键结果：
  - `split_count = 2`
  - `any_overflow = false`
  - 第 1 拍 `body_height = 895`，`safe_area_available_height = 904`
  - 第 2 拍 `body_height = 670`，`safe_area_available_height = 904`

## 6. 验证产物

- `dist/20260424_不放大完整可读_no_zoom_completeness/1x默认视图_review_frames/01_1x默认视图_no_zoom.png`
- `dist/20260424_不放大完整可读_no_zoom_completeness/1x默认视图_review_frames/02_1x默认视图_no_zoom.png`
- `dist/20260424_不放大完整可读_no_zoom_completeness/布局指标_layout_metrics.json`
- `dist/20260424_不放大完整可读_no_zoom_completeness/验证清单_manifest.json`

## 7. validation 状态

- `technical_validation`：`已确认` 通过本轮测试、fixture 生成、默认 demo 生成与 `git diff --check`。
- `content_validation`：`部分成立` 本轮最小验证图在 1x 默认视图下未见裁切，但真实用户截图专用生成链路未在当前 `main` 可追踪源码中找到，仍建议用户复审两张 1x 图。
- `remaining_blockers`：`待验证` 若实际 vNext 截图链路来自未提交脚本，需要把同一规则接入该入口后再复审。
