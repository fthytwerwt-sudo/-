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
  - 首次真实 cloud-only assembly 已执行，不是聊天推断
  - 当前还不能把“已真实导出成功”写成 success

## 当前最新真实运行结论

- 本轮在分支 `codex/round1`、起始 HEAD `75178a35bd4e0d87e3d423f0a9aaaaa7f826f24b` 上，已真实执行：
  - `python3 scripts/assemble_formal_api_demo.py --manifest dist/formal_api_demo/manifest.json --local-config config/formal_api_demo.local.toml`
- 真实结果：失败
- 精确失败层：`ListEditingProjects`
- 当前调用主体：RAM 用户 `video-factory-oss-1`
- 当前主因：缺少最小 ICE / 云剪权限
- 建议最小权限：
  - `ice:ListEditingProjects`
  - `ice:UpdateEditingProject`
  - `ice:SubmitMediaProducingJob`
  - `ice:GetMediaProducingJob`
- 当前未重跑原因：
  - 本轮已确认当前主体没有 RAM 管理权限
  - 无法直接在本机给 `video-factory-oss-1` 挂策略
- 当前状态标签：
  - `repo_status_updated`

## 当前最新权限复核结论

- 本轮在分支 `codex/round1`、起始 HEAD `d9d634b292ce6e6155446d08af10098cd979079e` 上，已重新做最小权限前置检查，不是聊天推断：
  - `STS GetCallerIdentity`
  - `ICE ListEditingProjects`
- 当前调用主体仍是：RAM 用户 `video-factory-oss-1`
- 当前 `ice:ListEditingProjects` 仍未通过：
  - 返回：`403 Forbidden`
  - RequestId：`435BE7F3-4126-528E-8B87-5E55DC9B0C29`
- 本轮路径判断：
  - 走 `路径 B`
  - 因权限状态未变化，本轮未重跑 assembly
- 当前状态标签：
  - `permission_pending_recheck`

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
- 当前验证结果：
  - `30` 个测试通过
  - `py_compile` 通过
  - `git diff --check` 通过
  - 真实 assembly 已执行
  - `uploaded_assets_count = 6`
  - `cloud_timeline.json` 已生成
  - ICE `ListEditingProjects` 返回 `403 Forbidden`
  - STS 已确认当前主体为 RAM 用户 `video-factory-oss-1`
  - 只读 RAM API 也返回 `403 NoPermission`
  - 本轮新增权限复核：
    - 当前主体仍是 RAM 用户 `video-factory-oss-1`
    - `ice:ListEditingProjects` 仍返回 `403 Forbidden`
    - 因权限未生效，本轮未重跑 assembly

## 当前交接提醒

- 仓库口径仍然是 cloud-only，而且代码已经接到真实云端 assembly 主链。
- 当前不再是“等填密钥”，而是：
  - 等具备 RAM 管理权限的主体给 `video-factory-oss-1` 挂最小 ICE / 云剪策略
- 当前权限复核仍未通过，因此本轮不做无效重跑。
- 策略挂好后再优先重跑：
  - `python3 scripts/assemble_formal_api_demo.py --manifest dist/formal_api_demo/manifest.json --local-config config/formal_api_demo.local.toml`
- `config/formal_api_demo.local.toml` 是 `.gitignore` / `local_only`：
  - 不会上传到 GitHub
  - 但它已经准备好，用户无需自己设计字段结构
