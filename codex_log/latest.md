# Latest

## 当前主结论

- 2026-04-06 pure PPT / 信息卡主线仍保持 cloud-only：
  - `北京区 OSS + 云剪工程 = 唯一 assembly 主路径`
  - `local assembly / local mp4` 已退出 pure PPT / 信息卡主线，不再作为 fallback / 兜底 / 应急正常交付
- 当前代码层已从“只有 gate / plan / blocked 占位”推进到：
  - `provider_assembly_implementation` 已接入
  - `run_assembly_pipeline()` 在前提齐全时会真实进入 cloud assembly 执行器
  - cloud assembly 执行器当前已补上：
    - OSS 上传
    - 云剪工程解析
    - 时间线生成
    - `UpdateEditingProject`
    - `SubmitMediaProducingJob`
    - `GetMediaProducingJob` 轮询
    - 导出结果解析
- 当前真实边界仍然保持诚实：
  - OSS / IMS / 云剪工程的非密钥参数已写回 repo
  - 本地配置文件已整理好，用户只需手填真实密钥
  - `config/formal_api_demo.local.toml` 属于 `.gitignore` / `local_only`
  - 第二次真实 cloud-only assembly 重跑已成功，不是聊天推断
  - 当前成功事实只成立于任务分支 `codex/round1`
  - 当前还不能把“正式主读取分支已同步”写成 success

## 当前最新真实重跑结论

- 本轮在分支 `codex/round1`、起始 HEAD `4a5b7f7a29f24445d6f6cef28dcab4b2a85e1d8b` 上，已真实执行：
  - `python3 scripts/assemble_formal_api_demo.py --manifest dist/formal_api_demo/manifest.json --local-config config/formal_api_demo.local.toml`
- 真实结果：成功
- 结果分类：`B`
- 当前调用主体：RAM 用户 `video-factory-oss-1`
- 当前已拿到：
  - `project_id = a139456cf3334509b20192f3203d75bc`
  - `job_id = f45c6af448f44f0794f71ae9f26a1d1e`
  - `media_id = 47b0a400311c71f1a8c3e7f7d45b6302`
  - `output_url = oss://zvip1-video-beijing/video-factory/final/20260405T182130Z/formal_api_demo.mp4`
  - `media_url = https://zvip1-video-beijing.oss-cn-beijing.aliyuncs.com/video-factory/final/20260405T182130Z/formal_api_demo.mp4`
- 当前关键 RequestId：
  - `ListEditingProjects = 6BB9B394-4045-5EE6-A65F-E3BB37FEB8AB`
  - `UpdateEditingProject = D2FB8219-F052-5373-8D3C-3F090684EC79`
  - `SubmitMediaProducingJob = 41971ECA-4C97-543D-BA8C-971092D2AA59`
  - `GetMediaProducingJob = 51770EE3-C359-505B-9987-92E14079BE12`
- 当前精确卡点：
  - 无；本轮已真实越过权限层并完成导出
- 当前状态标签：
  - `repo_status_updated`
  - `task_branch_only`

## 本轮关键执行事实

- 本轮实际改动：
  - `formal_api_demo_core.py`
    - 接入 `_execute_cloud_only_assembly`
    - assembly gate 不再把 `provider_assembly_implementation` 视为固定缺失
    - assembly result summary 改按真实 cloud assembly 结果出值
  - `formal_api_demo_cloud_assembly.py`
    - 新增云端 assembly 实现模块
    - 包含 OSS 上传、云剪工程解析、Timeline 构造、OpenAPI 请求签名、导出轮询与结果解析
  - `tests/test_formal_api_demo_pipeline.py`
    - 把“visual assets ready 仍 blocked”旧断言升级为“进入 cloud assembly 并返回 success”
  - `config/formal_api_demo.local.toml`
    - 已重写为 cloud-only 本地占位模板
    - 只保留用户手填字段，不再保留旧 `space_name` / `template_id` / `cloud` 旧口径

## 当前外部已确认状态包

- OSS bucket：`zvip1-video-beijing`
- OSS region：`cn-beijing`
- OSS endpoint：`oss-cn-beijing.aliyuncs.com`
- OSS bucket domain：`zvip1-video-beijing.oss-cn-beijing.aliyuncs.com`
- OSS ACL：`private`
- RAM 用户：`video-factory-oss-1`
- IMS / ICE / 智能媒体服务：北京区已就绪
- 功能体验月包有效期：`2026-05-05 05:00:00`
- IMS storage address：`zvip1-video-beijing.oss-cn-beijing.aliyuncs.com`
- 云剪工程：`video-factory-ppt-master-v1`
- 云剪工程状态：草稿
- 编辑器可打开：是
- 当前 RAM 用户：`video-factory-oss-1`

## 本轮实际验证

- 已按读取范围复读命中的规则、项目脑、执行上下文、代码、配置与测试文件。
- 已执行：
  - `python3 -m unittest tests.test_formal_api_demo_pipeline.FormalApiDemoPipelineTests.test_assemble_non_dry_run_executes_cloud_assembly_when_visual_assets_ready`
  - `python3 -m unittest tests.test_formal_api_demo_pipeline`
  - `python3 -m py_compile formal_api_demo_core.py formal_api_demo_cloud_assembly.py scripts/assemble_formal_api_demo.py`
  - `git diff --check`
- 此后新增真实权限审计 / 真实 assembly 验证：
  - `python3 scripts/assemble_formal_api_demo.py --manifest dist/formal_api_demo/manifest.json --local-config config/formal_api_demo.local.toml`
  - 基于本地 AccessKey 的 `STS GetCallerIdentity`
  - 基于本地 AccessKey 的只读 RAM 审计：
    - `GetUser`
    - `ListUsers`
    - `ListPoliciesForUser`
  - 基于本地 AccessKey 的最小 ICE 复现：
    - `ListEditingProjects`
- 本轮新增真实重跑：
  - `python3 scripts/assemble_formal_api_demo.py --manifest dist/formal_api_demo/manifest.json --local-config config/formal_api_demo.local.toml`
- 当前验证结果：
  - `30` 个测试通过
  - `py_compile` 通过
  - `git diff --check` 通过
  - 当前主体仍是 RAM 用户 `video-factory-oss-1`
  - 本轮真实重跑已完成
  - 已拿到真实 `project_id` / `job_id` / `media_id`
  - 已拿到真实 OSS final 路径与可访问 `media_url`
  - `uploaded_assets_count = 6`
  - `cloud_timeline.json` 已生成

## 当前交接提醒

- 仓库口径仍然是 cloud-only，而且代码已经接到真实云端 assembly 主链。
- 当前任务分支已经拿到真实云端导出成功结果，但这不等于主读取分支已同步。
- 若后续继续推进，下一步应围绕成片验收、样片回看和主读取分支回流策略来处理，而不是再回到权限 blocker。
- `config/formal_api_demo.local.toml` 是 `.gitignore` / `local_only`：
  - 不会上传到 GitHub
  - 但它已经准备好，用户无需自己设计字段结构
