# 2026-04-02 formal_api_demo latest 对齐修正

## 本轮目标

- 不改 `formal_api_demo` 主逻辑
- 不扩 `project_source/` 或 `codex_source/`
- 只把 `codex_log/latest.md` 改写成当前 `formal_api_demo` 的真实完成状态

## 为什么这轮只改 latest

- 当前代码、测试、配置注释的主口径已经基本统一。
- 这轮真实缺口不在主逻辑，而在 `codex_log/latest.md` 仍停在执行机制桥接主题，导致新会话接手会先读偏重点。

## latest 之前错在哪

- `latest.md` 把“最近一次完成了什么”写成：
  - `codex_source/02 ~ 05`
  - `codex_source/09_dynamic_source_sync_rules.md`
  - 执行层桥接与动态资料同步
- 这不是当前 `formal_api_demo` 主线的真实完成状态，也不是新会话继续推进视频主线时最该先知道的事实。

## latest 现在怎么改的

- 改成明确围绕 `formal_api_demo` 当前真实状态收口：
  - generation 继续接 API
  - local assembly 默认交付
  - cloud assembly optional / skipped
  - 缺视觉模型时 generation 真实 blocked
  - `overall_status` 依赖 generation + local assembly，而不是 cloud assembly
- 同时把“最近一次真正完成了什么”改写成：
  - 代码 / 测试 / 配置注释已经统一到上述正式口径
- 并把“下一步”收口回视频主线任务，而不是继续补日志或机制文件

## 为什么这轮到这里就该停止

- 本轮目标是 very small fix，只要求把 `latest.md` 对齐到仓库事实。
- 代码、测试、配置文件本轮都不需要再改。
- `latest.md` 与相关代码 / 测试 / 配置注释不冲突后，这轮就已经形成可判断的小闭环，应停止继续扩任务。
