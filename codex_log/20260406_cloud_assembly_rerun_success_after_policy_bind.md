# 20260406_cloud_assembly_rerun_success_after_policy_bind

## 本轮目标

- 在不改 Python 逻辑、不重跑 generation 的前提下
- 基于用户已在阿里云主账号控制台给 RAM 用户 `video-factory-oss-1` 绑定最小 ICE / 云剪策略这一前提
- 直接做第二次真实 cloud-only assembly 验证
- 并把真实结果写回仓库状态文件后 commit + push

## 执行前确认

- 当前目录：`/Users/fan/Documents/视频工厂`
- 当前分支：`codex/round1`
- 当前 HEAD 起点：`4a5b7f7a29f24445d6f6cef28dcab4b2a85e1d8b`
- 本地仓库 `skills/`：不存在
- 本轮沿用全局：
  - `systematic-debugging`
  - `verification-before-completion`

## 读取与前提确认

- 已复读：
  - `AGENTS.md`
  - `codex_log/latest.md`
  - `codex_source/01_execution_rules.md`
  - `codex_source/02_current_execution_context.md`
  - `codex_source/08_branch_sync_and_reading_branch_rules.md`
  - `project_source/10_formal_api_demo_current_route_patch_20260402.md`
  - `formal_api_demo_core.py`
  - `formal_api_demo_cloud_assembly.py`
  - `scripts/assemble_formal_api_demo.py`
  - `config/formal_api_demo.example.toml`
  - `config/formal_api_demo.local.toml`
  - `dist/formal_api_demo/manifest.json`
- 已确认：
  - `generation.voiceover.status = success`
  - `generation.captions.status = success`
  - `generation.visual_generation.status = success`
  - `segments = 3`
  - `segments.output_slots.visual_uri = 3/3 ready`
  - 本地 `aliyun_oss.access_key_id` / `access_key_secret` 为非占位值

## 本轮实际运行

- 实际命令：
  - `python3 scripts/assemble_formal_api_demo.py --manifest dist/formal_api_demo/manifest.json --local-config config/formal_api_demo.local.toml`
- 本轮实际运行次数：
  - `1`
- 本轮结果分类：
  - `B`

## 真实结果

- 当前主体：RAM 用户 `video-factory-oss-1`
- 本轮已真实成功越过此前的 `ListEditingProjects` 权限层
- 本轮已拿到：
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
  - 无；本轮已真实导出成功

## 补充说明

- 这次成功只说明：
  - 当前任务分支 `codex/round1` 上，pure PPT / 信息卡 cloud-only assembly 已拿到一次真实成功结果
- 这次成功不说明：
  - 主读取分支 `codex/user-readable-map` 已同步
  - 所有后续样片验收与质量判断都已完成

## 本轮仓库状态

- 本轮已更新状态文件并 push 到当前任务分支
- 本轮状态分类应为：
  - `task_branch_only`
- 本轮未同步到：
  - `codex/user-readable-map`
