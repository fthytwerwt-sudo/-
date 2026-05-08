# 20260406_ppt_cloud_assembly_provider_impl

## 本轮目标

- 把 pure PPT / 信息卡主线里原本固定缺失的 `provider_assembly_implementation` 真正接到代码主链
- 让用户只需要在本地配置文件填写真实 AccessKey / Secret
- 然后就能继续做“北京区 OSS + 云剪工程”的最小真实导出验证

## 执行前已确认事实

- pure PPT / 信息卡主线当前正式口径已经是 cloud-only
- 北京区 OSS / IMS / 云剪工程的非密钥参数已确认并已写入 repo
- 当前云剪工程名：`video-factory-ppt-master-v1`
- AccessKey / Secret 只保存在用户本地，不得写入 repo
- `config/formal_api_demo.local.toml` 已存在，但内容仍是旧口径、旧字段、坏格式和不可直接交付状态

## 实际读取

- `AGENTS.md`
- `codex_log/latest.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_source/02_current_execution_context.md`
- `codex_source/03_research_findings_bridge.md`
- `codex_source/07_formal_api_demo_target_plan.md`
- `codex_source/08_branch_sync_and_reading_branch_rules.md`
- `project_source/00_project_brief.md`
- `project_source/10_formal_api_demo_current_route_patch_20260402.md`
- `formal_api_demo_core.py`
- `scripts/assemble_formal_api_demo.py`
- `config/formal_api_demo.example.toml`
- `config/formal_api_demo.local.toml`
- `tests/test_formal_api_demo_pipeline.py`

## 真实缺口定位

- 当前缺口不在配置字段定义层
- 当前缺口也不在 gate / plan / summary 层
- 当前真实缺口是：
  - `evaluate_assembly_gate()` 把 `provider_assembly_implementation` 固定记成缺失
  - `run_assembly_pipeline()` 没有任何真实 cloud assembly 执行分支
  - 没有 OSS 上传
  - 没有云剪工程解析
  - 没有 Timeline 构造
  - 没有 `UpdateEditingProject`
  - 没有 `SubmitMediaProducingJob`
  - 没有 `GetMediaProducingJob` 轮询
  - 没有导出结果解析

## 实际改动

### 代码

- `formal_api_demo_cloud_assembly.py`
  - 新增独立的 cloud assembly 实现模块
  - 接入：
    - OSS 上传
    - OSS 签名下载 URL 生成
    - 阿里云 ICE OpenAPI RPC 签名请求
    - 云剪工程列表解析
    - `UpdateEditingProject`
    - `SubmitMediaProducingJob`
    - `GetMediaProducingJob` 轮询
    - 时间线构造
    - 导出 OSS final 路径 / media URL 解析
- `formal_api_demo_core.py`
  - `run_assembly_pipeline()` 在前提齐全时正式调用 `_execute_cloud_only_assembly`
  - assembly gate 不再把 `provider_assembly_implementation` 固定记为缺失
  - assembly result summary 改读真实 cloud assembly 结果，而不是只读 gate 状态
  - `known_issues` 新增 cloud assembly 汇总
  - `next_action_hint` 改成“填本地密钥后执行真实云端导出验证”

### 测试

- `tests/test_formal_api_demo_pipeline.py`
  - 把“visual assets ready 仍 blocked”旧断言升级为：
    - `run_assembly_pipeline()` 进入 cloud assembly 分支
    - cloud assembly status = `success`
    - `artifact_paths.final_video` 返回 OSS final 路径

### 本地配置

- `config/formal_api_demo.local.toml`
  - 已整份重写为 cloud-only 占位模板
  - 只保留用户手填字段与当前主线实际字段
  - 去掉旧 `space_name` / `template_id` / `cloud` 旧口径
  - 文件仍是 `.gitignore` / `local_only`

## 本轮验证

- red/green：
  - `python3 -m unittest tests.test_formal_api_demo_pipeline.FormalApiDemoPipelineTests.test_assemble_non_dry_run_executes_cloud_assembly_when_visual_assets_ready`
- 全量现有 pipeline 测试：
  - `python3 -m unittest tests.test_formal_api_demo_pipeline`
- 语法校验：
  - `python3 -m py_compile formal_api_demo_core.py formal_api_demo_cloud_assembly.py scripts/assemble_formal_api_demo.py`
- diff 健康检查：
  - `git diff --check`

## 当前结果

- `provider_assembly_implementation` 已不再只是固定缺失占位
- 代码主链已能在前提齐全时进入真实 cloud assembly 执行器
- 本地配置文件已准备好，用户只需打开并填写：
  - `aliyun_oss.access_key_id`
  - `aliyun_oss.access_key_secret`
- 当前仍必须保持诚实：
  - 真实云端导出尚未在本轮完成
  - 目前没有真实 `job_id` / `media_id` / 导出成功回执
  - 这些值必须等用户填完本地密钥后再跑一次真实导出验证才能确认

## 继续验证命令

- 最小真实云端导出验证：
  - `python3 scripts/assemble_formal_api_demo.py --manifest dist/formal_api_demo/manifest.json --local-config config/formal_api_demo.local.toml`

## 下一步建议

- 用户先在本地配置文件填写真实 OSS AccessKey / Secret，然后立即执行一次最小真实云端导出验证，把真实 `job_id` / `media_id` / 输出路径继续回写仓库。
