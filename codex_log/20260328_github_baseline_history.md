# 20260328 GitHub Baseline History

## 1. 本轮目标

- 基于当前真实仓库状态，补写《视频工厂》仓库从本地 git 初始化到 GitHub baseline 建立的首条执行日志。
- 让新聊天框和新 Codex 会话不再主要依赖聊天记忆，而是可以先从仓库内日志接手。

## 2. 执行前已确认事实

- 当前仓库已经是 git 仓库。
- 当前分支是 `main`，并已跟踪 `origin/main`。
- 远程仓库是 `https://github.com/fthytwerwt-sudo/-.git`。
- 当前最新提交是 `5b4db1e5d78b1169c5f51bbb45b6e186d2eb4686`。
- 当前仓库已经完成 GitHub baseline push。
- 当前仓库无本地 `skills/` 目录。

## 3. 实际读取

- 顶层与执行层规则：
  - `AGENTS.md`
  - `codex_source/00_codex_readme.md`
  - `codex_source/01_execution_rules.md`
- 项目导航与项目背景：
  - `project_source/00_project_brief.md`
  - `project_source/06_project_index.md`
- 仓库状态与历史：
  - `git status --short --branch`
  - `git remote -v`
  - `git branch -vv`
  - `git log --oneline --decorate`
  - `git rev-parse HEAD`
- 基线清理过程中已核对的仓库事实：
  - `dist/demo/` 内容
  - 被 git 跟踪的 `node_modules/`
  - 被 git 跟踪的 `.DS_Store`
  - 生成型二进制产物与可审阅文本样例的差异

## 4. 实际改动

- 完成了本地 git 初始化，并建立 `main` 分支。
- 创建了 baseline 初始化提交：
  - `6a57bbd chore: initialize video-factory local baseline`
- 新增 `.gitignore`，并完成仓库卫生清理：
  - 停止跟踪 `node_modules/`
  - 停止跟踪 `.DS_Store`
  - 停止跟踪 `dist/demo/final.mp4`
  - 停止跟踪 `dist/demo/voice.mp3`
  - 保留 `dist/demo/script.txt`
  - 保留 `dist/demo/captions.srt`
- 创建了清理提交：
  - `9cae192 chore: clean baseline repo hygiene`
- 升级了根目录 `AGENTS.md`，使其从早期 demo 说明升级为 Codex 顶层入口规则。
- 创建了规则升级提交：
  - `5b4db1e docs: upgrade agents codex entry rules`
- 绑定了用户提供的远程仓库地址：
  - `origin -> https://github.com/fthytwerwt-sudo/-.git`
- 修复了本地 HTTPS 认证链，并完成首次 baseline push 到 `origin/main`。

## 5. 实际执行

- 先确认当前目录最初不是 git 仓库，然后执行 `git init -b main` 建立本地仓库。
- 把当前仓库现状纳入 baseline，并创建本地初始化提交。
- 发现 baseline 中包含不适合进入 GitHub 协作链路的内容后，新增 `.gitignore` 并清理跟踪项。
- 确认 `dist/demo/script.txt` 与 `dist/demo/captions.srt` 仍具审阅价值，因此保留。
- 升级 `AGENTS.md`，补入分层、默认读取顺序、GitHub / PR 线路与真实性要求。
- 根据用户给定的仓库地址绑定 `origin`。
- 先经历过旧 HTTPS 凭证 403 与 SSH 不可用的问题，后续通过清理 `osxkeychain` 旧凭证并在本地终端重新输入新的 fine-grained token 完成认证。
- 成功执行 `git push -u origin main`，并建立本地 `main` 对 `origin/main` 的跟踪关系。

## 6. 当前结果

- 当前仓库已进入 GitHub 协作基线状态。
- `main` 与 `origin/main` 指向同一提交：
  - `5b4db1e5d78b1169c5f51bbb45b6e186d2eb4686`
- 当前远程仓库地址是：
  - `https://github.com/fthytwerwt-sudo/-.git`
- 后续仓库型任务不再应直接在 `main` 上推进，而应默认走：
  - 先看现状 → 开分支改 → 提 PR → 跑 checks → AI 复审 → 用户拍板
- 当前执行日志机制已开始落到仓库内，后续交接优先看 `codex_log/`，不再主要依赖聊天记忆。

## 7. 下一步建议

- 后续任何仓库型任务都从新分支开始，不直接改 `main`。
- 每次有真实执行结果时，都新增一条 `codex_log/YYYYMMDD_task_name.md`，并刷新 `codex_log/latest.md`。
- 若下一轮继续推进视频链路或执行层规则，先读：
  - `AGENTS.md`
  - `project_source/06_project_index.md`
  - `codex_source/00_codex_readme.md`
  - `codex_source/01_execution_rules.md`
  - `codex_log/latest.md`
