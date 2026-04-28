# 20260429 素材保真检查与细节证据报告

## 本轮目标

- `已确认` 只做《视频工厂》用户录制素材的素材保真检查。
- `已确认` 输出给 `ChatGPT（最终落稿与复审入口）` 使用的素材事实包。
- `已确认` 不剪视频、不生成新 round、不修改 `dist/latest_review_pack/`、不修改 `content_validation`、不修改 `send_ready`。

## 执行前已确认事实

- `已确认` 当前工作目录：`/Users/fan/Documents/视频工厂`。
- `已确认` 当前工作树分支：`fix/no-zoom-completeness-layout`。
- `已确认` 默认主读取分支 `origin/codex/user-readable-map` 存在。
- `已确认` 当前工作树 `dist/latest_review_pack/summary.json` 指向 `round32_全片边框残留与跳切连续性修复`，`content_validation = 待用户 / ChatGPT 最终复审`，`send_ready = false`。
- `已确认` `origin/codex/user-readable-map:GPT数据源/08_当前正式事实.md` 指向 `round34_中段双展示提示卡_正反分段提示修复`，`content_validation = 待用户 / ChatGPT 最终复审`，`send_ready = no`。
- `fact_conflict_detected（事实冲突已发现）` 当前工作树与主读取分支的 latest review round 指向不一致；本轮未覆盖任何状态。

## 实际读取

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_log/latest.md`
- `GPT 数据源/04_选题与文案规则.md`
- `GPT 数据源/05_文案路由规则.md`
- `GPT 数据源/06_当前主线锚点_API生成真人_用户录制素材_少量PPT_云端剪辑.md`
- `GPT 数据源/07_AI知识类视频价值规则.md`
- `GPT 数据源/08_当前事实读取规则.md`
- `origin/codex/user-readable-map:GPT数据源/04_选题与文案规则.md`
- `origin/codex/user-readable-map:GPT数据源/05_文案路由规则.md`
- `origin/codex/user-readable-map:GPT数据源/07_AI知识类视频价值规则.md`
- `origin/codex/user-readable-map:GPT数据源/08_当前正式事实.md`
- 全局 skills：
  - `verification-before-completion`
  - `context-driven-development`
  - `visual-verdict`
  - `writing-router-cn`

## 实际改动

- `已生成` `/Users/fan/Documents/视频工厂/素材检查_reports/20260429_素材保真检查_material_faithful_check/素材保真检查报告_material_faithful_report.md`
- `已生成` `/Users/fan/Documents/视频工厂/素材检查_reports/20260429_素材保真检查_material_faithful_check/素材清单_material_inventory.md`
- `已生成` `/Users/fan/Documents/视频工厂/素材检查_reports/20260429_素材保真检查_material_faithful_check/素材联系表_material_contact_sheet.jpg`
- `已生成` `/Users/fan/Documents/视频工厂/素材检查_reports/20260429_素材保真检查_material_faithful_check/关键帧证据_keyframes_evidence.jpg`
- `已生成` `/Users/fan/Documents/视频工厂/素材检查_reports/20260429_素材保真检查_material_faithful_check/时间码截图_timecode_frames/`
- `已生成` `/Users/fan/Documents/视频工厂/素材检查_reports/20260429_素材保真检查_material_faithful_check/run_summary.json`
- `已更新` `codex_log/latest.md`
- `已新增` `codex_log/20260429_material_faithful_check.md`

## 实际执行

- `已确认` 检查素材目录：
  - `/Users/fan/Documents/视频工厂/素材录制/正面/`
  - `/Users/fan/Documents/视频工厂/素材录制/反面/`
  - `/Users/fan/Documents/视频工厂/素材录制/正面-反面/`
- `已确认` 使用 `mdls`、`afinfo`、OpenCV / Python 完成媒体信息读取、抽帧、联系表与报告生成。
- `已确认` 当前 PATH 未找到 `ffmpeg` / `ffprobe`，本轮未使用。
- `已确认` 两个 MP4 均可打开、可抽帧、包含 HEVC 视频与 AAC stereo 音轨。
- `已确认` 正面录屏约 `745.68s / 3420x2214 / 59.9169fps`。
- `已确认` 反面录屏约 `67.08s / 3420x2214 / 59.8807fps`。

## 当前结果

- `已确认` 反面素材可作为“宽泛问法”证据：`最新方案.pdf` + “帮我把这个方案整理一下” -> 文本型战略整理/执行总案。
- `已确认` 正面素材可作为“明确交付标准后进入 PPT 生成”的证据：可见 `可交付初稿` 检查项、PPT/XML 生成指令、`已完成PPT生成(6m31s)` 与 16 页 PPT 预览。
- `部分成立` 素材可证明结果形态差：文字方案 vs 可预览 PPT deck。
- `不能证明` 最终 PPT 已经用户验收、可直接发布、真实节省固定小时数或工作包已完成沉淀。

## 下一步建议

- `下一个目标`：ChatGPT 基于本轮素材事实包写最终脚本，并保守引用可见事实。
- `补录建议`：若最终稿要写“提效”，建议补录原始 PDF 关键页、正面完整 prompt 输入过程、PPT 关键页翻看、用户验收判断和人工耗时基准。
