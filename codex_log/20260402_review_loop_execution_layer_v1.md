# 2026-04-02 review_loop 执行层 v1

## 1. 本轮目标

为《视频工厂：AI 垂类场景化视频内核》新增一套 repo 内可执行的复盘执行层 `v1`。

本轮目标固定为：

- 建立 `review_loop/` 目录
- 写出复盘执行层模板文件
- 让 Codex 后续能稳定承担：
  - 记录
  - 初检
  - 归档
  - 生成下轮执行单草稿
- 同时明确：
  - 不越权替 ChatGPT 做最终判断拍板
  - 不扩成脚本自动化系统
  - 不改 GPT 数据源正文

## 2. 执行前已确认事实

本轮开始前已确认：

- 当前分支是 `codex/user-readable-map`
- 当前仓库无本地 `skills/` 目录
- 当前仓库内不存在现成的 `review_loop/` 目录
- 当前正式主路径仍是：
  - 文本需求 → 脚本 → 配音 API → 图片 / 视频生成 API → 本地 assembly → 本地 mp4 → 人工上传
- generation 继续接 API
- assembly 当前默认走本地
- cloud assembly 是后续增强项，不是当前硬前置
- demo 只证明链路跑通，不是质量样片
- “抖音 90 分标准”是项目内部质量简称，不是平台官方规则

补充现实情况：

- `project_source/*` 当前已有未提交改动，本轮按用户要求不触碰这些文件

## 3. 实际读取

本轮实际读取了：

- `AGENTS.md`
- `codex_log/latest.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_source/02_current_execution_context.md`
- `codex_source/03_research_findings_bridge.md`
- `codex_source/04_completion_and_review_contract.md`
- `codex_source/05_execution_deviation_and_reality_sync.md`
- `project_source/00_project_brief.md`
- `project_source/04_review_templates.md`
- `project_source/08_quality_baseline_and_90_score_rules.md`

额外检查结果：

- 当前未发现现有复盘系统目录，仅发现与 review 相关的项目脑和执行层文件
- 当前无本地 `skills/`，因此技能检查回退到全局 `~/.codex/skills`

## 4. 实际创建和更新的文件

### 新建

- `review_loop/00_review_loop_readme.md`
- `review_loop/01_review_status_rules.md`
- `review_loop/02_video_record_template.md`
- `review_loop/03_result_dashboard_template.md`
- `review_loop/04_diagnosis_template.md`
- `review_loop/05_dual_review_handoff_template.md`
- `review_loop/06_next_round_task_template.md`
- `codex_log/20260402_review_loop_execution_layer_v1.md`

### 更新

- `codex_log/latest.md`

## 5. 为什么这样分层

本轮没有去改 `project_source/*`，也没有去改 `codex_source/01~09` 的机制正文，原因如下：

- `project_source/` 负责稳定判断层，不适合塞入“发布后怎么落单条复盘文件”的执行模板
- `codex_source/` 负责执行规则层，不适合承载每轮视频复盘使用的模板正文
- `review_loop/` 适合单独承接“视频发布后的执行性复盘”

因此当前分层被固定为：

- `project_source/` 管判断
- `codex_source/` 管执行规则
- `review_loop/` 管发布后复盘执行

这样做的好处是：

- 不混写项目脑和执行模板
- 不把结果看板误写成系统主骨架
- 能直接支持 Codex 落记录、做初检、留归档、写下轮任务草稿
- 同时保留 ChatGPT 的最终判断权

## 6. 当前结果

当前结果为：

- repo 内复盘执行层 `v1` 已落地
- 最小可用文件体系已齐
- 状态口径已固定为：
  - 已确认
  - 部分成立
  - 待验证
- 单条视频记录、结果看板、诊断模板、双审核交接、下轮执行单草稿都已有模板
- `latest.md` 已切换为本轮最新接手摘要

本轮仍明确没有做：

- 自动化采集脚本
- 平台数据回拉
- 自动诊断程序
- 运营闭环扩写
- ChatGPT 判断层改写

## 7. 当前结果对后续的实际意义

后续只要视频开始真实发布，Codex 就可以按固定动作推进：

1. 先建单条视频记录
2. 再补结果字段
3. 再按诊断模板做初检
4. 再按双审核模板交给 ChatGPT
5. 最后生成下轮执行单草稿

这让“复盘”第一次从聊天动作变成仓库内可留痕、可回看、可交接的执行动作。

## 8. 下一步建议

下一步最合理的动作是：

1. 用这套模板跑第一条真实发布视频复盘
2. 检查字段是否够用、哪里还显得太空或太重
3. 再决定是否只补极少量子目录或实例命名规则

停止线仍保持：

- 先用起来
- 不顺手扩成自动化系统
- 不让 Codex 抢 ChatGPT 的最终判断位
