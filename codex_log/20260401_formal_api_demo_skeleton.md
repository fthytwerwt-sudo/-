# 20260401 Formal Api Demo Skeleton

## 本轮目标

- 把正式版 API demo 的最小骨架、输入输出契约、manifest / result_summary schema、Gate 校验框架真实落进仓库
- 让仓库进入“下一轮一旦补齐火山凭证与配置，就能开始真实 API 接入”的状态
- 明确本轮只完成骨架与 dry-run / blocked 路径，不把正式版云端链路写成已跑通

## 执行前已确认事实

- 当前仓库已确认跑通的真实链路仍是本地 demo：
  - `cases/demo.md` → `generate_demo.py` → `say / afconvert / ffmpeg-static` → `video_builder.swift` → `dist/demo/`
- `codex_source/07_formal_api_demo_target_plan.md` 已定义正式版目标态，但不是当前仓库已跑通事实
- 当前没有提供火山正式凭证，因此本轮不接真实 API，只允许落骨架、契约、Gate 与 dry-run / blocked 路径
- 当前工作区里存在不属于本轮的 `project_source/*` 脏改动与未跟踪文件，必须避开，不得带进 commit

## 实际读取

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_source/05_runtime_and_artifact_rules.md`
- `codex_source/07_formal_api_demo_target_plan.md`
- `codex_log/latest.md`
- `codex_log/20260401_formal_api_demo_target_plan_upgrade.md`
- `generate_demo.py`
- `tests/test_generate_demo.py`
- `.gitignore`
- 全局 skill：
  - `~/.codex/skills/test-driven-development/SKILL.md`
  - `~/.codex/skills/python-testing-patterns/SKILL.md`
  - `~/.codex/skills/python-project-structure/SKILL.md`
  - `~/.codex/skills/python-configuration/SKILL.md`

## 实际改动

### 新建

- `cases/formal_api_demo.md`
  - 新增正式版输入骨架示例，固定主题、总时长、视频比例、目标场景、目标用户、全局质量要求、Hook、结尾落点与三段式结构
- `config/formal_api_demo.example.toml`
  - 新增正式版 example 配置骨架，预留 provider、region、鉴权、TTS、图像 / 视频生成、组装、存储、输出、轮询和质量 Gate 参数位
- `formal_api_demo_core.py`
  - 新增正式版核心 helper，负责 markdown 解析、配置读取、Gate 评估、manifest / result_summary schema 构建和 json 产物写入
- `scripts/generate_formal_api_demo.py`
  - 新增正式版生成脚本入口，当前只支持输入解析、generation gate、manifest 与 result_summary 输出
- `scripts/assemble_formal_api_demo.py`
  - 新增正式版组装脚本入口，当前只支持 manifest 读取、assembly gate、assembly plan 与 result_summary 输出
- `tests/test_formal_api_demo_pipeline.py`
  - 新增最小测试，覆盖输入解析、缺字段报错、generate dry-run、assemble dry-run 与无 local 配置时非 dry-run blocked

### 修改

- `.gitignore`
  - 忽略 `config/formal_api_demo.local.toml`
  - 忽略 `dist/formal_api_demo/`
- `codex_log/latest.md`
  - 更新当前阶段为“正式版目标态已进入最小骨架搭建阶段”
  - 写清当前已落骨架与 Gate，但正式 API 仍未接入

## 实际执行

- 先新增骨架测试，再补核心 helper 与两个入口脚本，按最小 contract 驱动实现
- 定义并落地：
  - `formal_api_demo_manifest/v1`
  - `formal_api_demo_result_summary/v1`
  - `generation_gate`
  - `assembly_gate`
- 将 dry-run 路径设计成：
  - 真实解析输入与配置
  - 真实产出 json 结构化产物
  - 状态只允许是 `planned`
- 将非 dry-run 的无前提路径设计成：
  - 明确写 `blocked`
  - 明确写 `blocked_reason`
  - 不回退到本地 demo 链路

## 验证结果

- 运行测试：
  - `python3 -m unittest tests.test_formal_api_demo_pipeline`
  - 结果：通过，`Ran 5 tests`
- 运行生成 dry-run：
  - `python3 scripts/generate_formal_api_demo.py --dry-run --out /tmp/formal_api_demo_cli`
  - 结果：成功产出 `manifest.json`、`generation_gate.json`、`result_summary.json`
- 运行组装 dry-run：
  - `python3 scripts/assemble_formal_api_demo.py --dry-run --manifest /tmp/formal_api_demo_cli/manifest.json --out /tmp/formal_api_demo_cli`
  - 结果：成功产出 `assembly_gate.json`、`assembly_plan.json`、`result_summary.json`
- 运行非 dry-run 阻塞验证：
  - `python3 scripts/generate_formal_api_demo.py --out /tmp/formal_api_demo_blocked`
  - 结果：明确返回 `blocked`，并写出缺失前提，不假装 success

## 当前结果

- 正式版最小骨架已经落库：
  - 输入骨架
  - example 配置骨架
  - 核心 contract / helper / gate 框架
  - generate / assemble 入口脚本
  - 最小测试
- 当前 dry-run 已可作为“骨架验收”入口：
  - 能解析 formal input
  - 能写 manifest / gate / assembly plan / result_summary
  - 能把缺失前提明确写成 `planned` 或 `blocked`
- 当前仍不能写成正式链路已跑通，因为缺少：
  - 火山正式凭证
  - 本地私有配置
  - 空间名与资源存储实值
  - 组装模板 / 导出参数实值
  - 真实 provider 实现

## 下一步建议

- 下一轮应优先补本地私有配置文件与真实 provider 占位接入，再进入“接 API 前验收”
- 在用户未提供火山凭证、空间名、组装模板等真实前提前，本仓库只能继续推进 Gate、契约和 provider 接口封装，不得声称正式云端链路已跑通
