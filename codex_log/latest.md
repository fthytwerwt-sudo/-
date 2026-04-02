# Latest

## 本轮最新完成

- 已新增 `review_loop/` 目录
- 已建立 repo 内的复盘执行层 `v1`
- 当前这套复盘执行层只做：
  - 记录
  - 初检
  - 归档
  - 生成下轮执行单草稿
- 当前明确不做：
  - GPT 数据源重写
  - 自动化采集脚本
  - 平台运营闭环
  - Codex 越权替 ChatGPT 做最终判断

## 当前三级分工

- `project_source/`
  - 负责稳定判断层
  - 负责项目身份、阶段、边界、场景、结构、质量口径、回审模板
- `codex_source/`
  - 负责执行规则层
  - 负责读取顺序、执行边界、验证口径、汇报契约
- `review_loop/`
  - 负责视频发布后的复盘执行层
  - 负责单条记录、结果看板、初步诊断、双审核交接、下轮执行单草稿

## 本轮新增文件

- `review_loop/00_review_loop_readme.md`
- `review_loop/01_review_status_rules.md`
- `review_loop/02_video_record_template.md`
- `review_loop/03_result_dashboard_template.md`
- `review_loop/04_diagnosis_template.md`
- `review_loop/05_dual_review_handoff_template.md`
- `review_loop/06_next_round_task_template.md`

## 当前最关键下一步

- 先按这套模板跑第一批真实发布视频的复盘记录
- 由 Codex 负责把单条记录、结果字段、初检交接和下轮草稿落文件
- 由 ChatGPT 继续负责最终问题层判断和下一轮唯一最优先改点拍板

## 新会话建议先读

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_log/latest.md`
- `review_loop/00_review_loop_readme.md`
- `review_loop/01_review_status_rules.md`
