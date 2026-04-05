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
  - 本轮已对真实导出成片做初检式验收，但这仍不是最终拍板
  - 本轮已产出一版保守型视觉修正候选片，但这仍是任务分支内的候选样片，不是正式回流结果

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

## 当前最新成片初检结论

- 本轮已对真实导出产物做初检式验收，不是只看导出记录。
- 当前初检结论：
  - `task_branch_success_but_need_acceptance_fix`
- 当前最高优先级问题层：
  - `画面表现层`
- 当前为什么这样判断：
  - 开头 3 秒有效，问题点能被快速看懂
  - 中段有推进，前后变化可见
  - 结尾有落点
  - 但整体画面仍带较明显的 demo / 样机感，与当前 pure PPT / 信息卡母版要求的“白领咨询报告感 / 体面专业感 / 信息高效感”仍有差距
- 当前是否建议进入正式回流讨论：
  - `暂不建议`
- 当前状态标签：
  - `task_branch_only`

## 当前最新保守型视觉修正结论

- 当前工作分支：
  - `codex/round1-visual-pass-conservative`
- 本轮在不改 generation、不改 assembly 主链的前提下，对本地预览渲染模板做了保守型视觉修正。
- 新候选成片位置：
  - `dist/formal_api_demo_visual_pass_conservative/final.mp4`
- 新证据包位置：
  - `dist/formal_api_demo_visual_pass_conservative/review_frames/`
- 当前一句话自检：
  - demo 感已明显下降，整体更接近“白领咨询报告感 / 体面专业感 / 信息高效感”，但首屏背景里红色问题字样仍稍重，当前仍不建议直接进入正式主读取分支回流。
- 当前状态标签：
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
- 本轮新增成片初检：
  - 以真实导出文件为准生成本地验收证据包
  - 本地验收目录：
    - `dist/formal_api_demo/review_frames/`
  - 关键证据：
    - `cloud_export_final.mp4`
    - `frame_start.jpg`
    - `frame_middle.jpg`
    - `frame_end.jpg`
    - `contact_sheet.jpg`
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
  - 真实导出成片已拉到本地并可读取
  - 初检元数据：
    - 时长 `15.0s`
    - 分辨率 `1080x1920`
    - 文件大小 `3602005 bytes`
    - 视频流 / 音频流均存在
  - 初检判断：
    - 技术导出成立
    - 内容初检暂不建议直接回流正式主读取分支
- 本轮新增保守型视觉修正：
  - 基于现有 `preview_manifest.json`、现有配音和现有 3 段结构
  - 只调整 `video_builder.swift` 中与画面表现层直接相关的 hook / process / outcome 叠层样式
  - 未修改：
    - `formal_api_demo_core.py`
    - `formal_api_demo_cloud_assembly.py`
    - generation 逻辑
    - assembly 主链逻辑
  - 新候选片技术结果：
    - 时长 `15.0s`
    - 分辨率 `1080x1920`
    - 文件大小 `15922005 bytes`
    - 视频流 / 音频流均存在
  - 新证据包：
    - `frame_start.jpg`
    - `frame_middle.jpg`
    - `frame_end.jpg`
    - `contact_sheet.jpg`

## 当前交接提醒

- 仓库口径仍然是 cloud-only，而且代码已经接到真实云端 assembly 主链。
- 当前任务分支已经拿到真实云端导出成功结果，但这不等于主读取分支已同步。
- 当前保守型视觉修正版已产出，但首屏红色问题字样仍是最明显残余短板。
- 若后续继续推进，下一步应优先围绕“首屏问题字样仍偏重”做一次更小范围的画面收口，再决定是否进入正式回流讨论。
- `config/formal_api_demo.local.toml` 是 `.gitignore` / `local_only`：
  - 不会上传到 GitHub
  - 但它已经准备好，用户无需自己设计字段结构
