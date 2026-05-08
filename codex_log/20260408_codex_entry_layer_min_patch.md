# 2026-04-08 codex_entry_layer_min_patch

## 本轮目标

- 只做 Codex 侧入口层最小收口
- 修 `AGENTS.md`
- 修 `codex_source/00_codex_readme.md`
- 修 `codex_source/02_current_execution_context.md` 的旧锚点文件名引用
- 修 `codex_source/03_research_findings_bridge.md` 的旧锚点文件名引用
- 刷新 `codex_log/latest.md`

## 执行前已确认事实

- `codex_log/latest.md` 已明确新版主线：
  - 人物
  - 用户真实录制素材
  - 少量 PPT / 图片辅助
- `codex_source/01_execution_rules.md` 已切到新版主线
- `codex_source/02_current_execution_context.md` 已切到新版主线
- `codex_source/03_research_findings_bridge.md` 已有 `BRIDGE-20260408-03`
- 但当前仓库里仍有入口漂移：
  - `AGENTS.md` 仍没把 block 路由和结构跟文案走写清
  - `codex_source/00_codex_readme.md` 仍没把 GPT 新锚点文件名切过来
  - `codex_source/02_current_execution_context.md` / `codex_source/03_research_findings_bridge.md` 仍引用旧锚点文件名

## 实际读取

- `AGENTS.md`
- `codex_log/latest.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_source/02_current_execution_context.md`
- `codex_source/03_research_findings_bridge.md`
- 本地 skill 检查：无本地 `skills/`
- 全局 skill 检查：
  - `using-superpowers`
  - `verification-before-completion`

## 实际改动

- `AGENTS.md`
  - 补入：
    - 结构跟着文案走
    - 人物出现 1 次还是 2 次由 block 路由决定
  - 把新版主线锚点引用改到 `24_human_self_footage_light_ppt_routing_rules.md`
- `codex_source/00_codex_readme.md`
  - 补入：
    - 结构跟着文案走
    - 人物次数由 block 路由决定
    - 旧 pure PPT 入口不能再冲淡 cloud-only 主路径
  - 把锚点引用改到 `24_human_self_footage_light_ppt_routing_rules.md`
  - 同时显式注明：若仓库 `project_source` 尚未同步该文件名，以 Codex 侧 `latest + bridge` 口径为准
- `codex_source/02_current_execution_context.md`
  - 旧引用 `19_...` 改到 `24_...`
- `codex_source/03_research_findings_bridge.md`
  - 旧引用 `19_...` 改到 `24_...`
- `codex_log/latest.md`
  - 补一句：
    - `当前 codex 入口层已完成新版主线收口`
  - 同时如实写清：
    - Codex 侧引用已切到 `24_*`
    - 但当前仓库 `project_source` 文件名本身还没同步

## 现实冲突与处理

- `已确认`
  - 当前仓库里真实存在的是：
    - 旧锚点文件名版本
- `已确认`
  - 用户本轮要求 Codex 侧统一改成：
    - `project_source/24_human_self_footage_light_ppt_routing_rules.md`
- 本轮处理方式：
  - 只同步 Codex 侧锚点名
  - 不改 `project_source/*`
  - 在 `latest.md` 和本轮日志里明确标注该冲突

## 验证

- `已确认`
  - 复读核对：
    - `AGENTS.md`
    - `codex_source/00_codex_readme.md`
    - `codex_source/02_current_execution_context.md`
    - `codex_source/03_research_findings_bridge.md`
    - `codex_log/latest.md`
- `已确认`
  - `git diff --check` 通过
- `已确认`
  - 关键旧引用搜索已只剩 project_source 正文本身，不再留在 Codex 侧入口文件

## 当前结果

- 新会话按 `AGENTS -> 00 -> latest` 接手时，不会再先被旧 pure PPT 入口带偏
- Codex 侧对 GPT 新锚点文件名的引用已切换完成
- 当前仍不能写成“新版主线已真实验证跑通”

## 下一步建议

1. 若后续要彻底消除锚点文件名冲突，需要单独同步 `project_source/*`
2. 下一轮若继续做执行，不需要再修入口层，直接按新版主线推进即可
