# 2026-04-08 codex_side_gpt_project_sync

## 本轮目标

- 把 Codex 侧入口文件、执行前上下文、bridge 与 latest，正式同步到 GPT Project 最新已拍板口径
- 让新会话默认按“人物 + 用户真实录制素材 + 少量 PPT / 图片”理解项目
- 保留北京区 `OSS + 云剪 cloud-only` 为正式主路径
- 不把 `AI talking avatar / 数字人口播` 写回默认主线

## 执行前已确认事实

- 当前工作分支：`codex/provider-auto-rotation`
- 仓库本地 `skills/` 不存在
- 全局 skills 已检查并命中：
  - `using-superpowers`
  - `verification-before-completion`
- `codex_log/latest.md` 已经能看到新版主线摘要
- `codex_source/01_execution_rules.md` 与 `codex_source/02_current_execution_context.md` 已部分接住新主线
- 但 `AGENTS.md`、`codex_source/00_codex_readme.md`、`codex_source/03_research_findings_bridge.md` 和 `latest` 的交接表达仍不够完整

## 实际读取

- `AGENTS.md`
- `codex_log/latest.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_source/02_current_execution_context.md`
- `codex_source/03_research_findings_bridge.md`
- `codex_source/08_branch_sync_and_reading_branch_rules.md`
- 补读：
  - `codex_source/05_runtime_and_artifact_rules.md`
  - 与 formal_api_demo / 路由 / cloud-only 直接相关的当前 codex 侧口径

## 现状审计结论

- `AGENTS.md`
  - 仍没有把当前正式默认主线明确写成“人物 + 用户真实录制素材 + 少量 PPT / 图片”
- `codex_source/00_codex_readme.md`
  - 仍偏抽象，没有把 Codex 执行层必须知道的新主线事实写明
- `codex_source/01_execution_rules.md`
  - 已接住新版主线，但还缺“人物次数由 block 路由决定 / 中段主体默认优先给真实素材承担”的明确表达
- `codex_source/02_current_execution_context.md`
  - 主体口径已改新，但还缺“人物出现次数由 block 路由决定”的显式句子
  - 还需要把历史 cloud-only 成功事实和“新版主线已验证”切开
- `codex_source/03_research_findings_bridge.md`
  - 已有新主线桥接，但还缺一条“这轮是把 GPT Project 最新口径正式同步进 Codex 侧入口文件”的记录
- `codex_log/latest.md`
  - 已写新版主线事实，但还不够突出“这是 Codex 侧入口同步完成”的交接口径

## 实际改动

- `AGENTS.md`
  - 增加当前阶段下的新版主线事实
  - 明确当前不是 pure PPT 默认主线，不是 AI avatar 默认主线
  - 在最小接手集合补充命中新版主线时要读 `project_source/19_human_self_footage_hybrid_mainline_rules.md`
- `codex_source/00_codex_readme.md`
  - 增加 Codex 执行层必须知道的当前主线事实
  - 明确人物次数由 block 路由决定、中段主体默认优先给真实录制素材承担
  - 更新一句话入口
- `codex_source/01_execution_rules.md`
  - 在最小必要背景包里补上：
    - 人物职责
    - 自录素材职责
    - PPT / 图片职责
    - 人物次数由 block 路由决定
- `codex_source/02_current_execution_context.md`
  - 补上“人物出现 1 次还是 2 次，是 block 路由结果”
  - 补上新版主线质量判断重点
  - 把历史 cloud-only 成功事实改写为“云端路径可用”而非“新版主线已验证”
- `codex_source/03_research_findings_bridge.md`
  - 新增 `BRIDGE-20260408-04`
- `codex_log/latest.md`
  - 改成“Codex 侧已完成同步”的交接口径

## 实际执行

- 无代码功能扩展
- 无新增 case / schema / runtime 行为变更
- 本轮只做 Codex 侧入口、上下文、bridge、latest、日志的正式同步

## 当前结果

- 当前 Codex 侧入口文件已不再把项目理解成 pure PPT 默认主线
- 当前 Codex 侧执行前上下文已正式接住：
  - 人物 + 用户真实录制素材 + 少量 PPT / 图片
- 当前 Codex 侧已明确：
  - 人物职责
  - 自录素材职责
  - PPT / 图片职责
  - 人物次数由 block 路由决定
- 当前 Codex 侧仍保留：
  - 北京区 `OSS + 云剪 cloud-only`
  - `local preview / local mp4` 只作辅助存在

## 验证

- `已确认`
  - 手动复读：
    - `AGENTS.md`
    - `codex_source/00_codex_readme.md`
    - `codex_source/01_execution_rules.md`
    - `codex_source/02_current_execution_context.md`
    - `codex_source/03_research_findings_bridge.md`
    - `codex_log/latest.md`
- `已确认`
  - 关键漂移点已被替换：
    - 不再默认 pure PPT 主承载
    - 不再默认 AI avatar 主承载
    - 仍保留 cloud-only 正式主路径
- `未运行`
  - 本轮未改功能代码，因此没有新增运行时命令验证

## 未验证 / 待确认

- `待验证`
  - GPT Project 侧之外是否还有未来新增口径尚未桥接进仓库
- `待验证`
  - 新版主线的真实素材注入与正式云端导出，仍是后续执行问题，不在本轮完成范围

## 下一步建议

1. 若下一轮继续做新版主线执行，直接从 `AGENTS.md` + `codex_log/latest.md` + `codex_source/02_current_execution_context.md` 接手
2. 若下一轮要做真实出片验证，再回到 formal_api_demo 的 `footage_inputs` 与云端 assembly
