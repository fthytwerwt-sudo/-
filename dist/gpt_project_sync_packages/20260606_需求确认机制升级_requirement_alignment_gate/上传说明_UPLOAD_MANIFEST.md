# GPT Project 上传说明｜需求确认机制升级

## 1. 文件定位

本目录是给 GPT Project 直接整包上传的资料同步包，用于同步 2026-06-06 新增 / 补强的 `requirement_alignment_needed（需求对齐必需）` 机制。

本包基于 Git commit：

`8d64f62a31f6a741934b2e21e1fcfca28bc4f80c`

本包只同步机制资料、主读入口、当前 latest 日志和必要索引，不是视频产物，不是媒体包，不是运行输出大包。

## 2. 用户上传哪个目录

请上传整个目录：

`/Users/fan/Documents/视频工厂/dist/gpt_project_sync_packages/20260606_需求确认机制升级_requirement_alignment_gate/`

该目录包含 `上传说明_UPLOAD_MANIFEST.md`，可直接作为 GPT Project 同步入口。

## 3. 建议上传内容

上传本目录下全部 Markdown 文件和三个子目录：

- `上传说明_UPLOAD_MANIFEST.md`
- `同步说明_SYNC_SUMMARY.md`
- `变更文件清单_CHANGED_FILES.md`
- `本轮机制补丁_MECHANISM_PATCH.md`
- `状态边界_STATUS_BOUNDARY.md`
- `项目主读文件_GPT_PROJECT_MAIN_READ_FILES/`
- `Codex执行层镜像_CODEX_MIRROR_FILES/`
- `当前日志与索引_CURRENT_LOGS_AND_INDEXES/`
- `本轮日志_CURRENT_TASK_LOG/`

## 4. 上传后 GPT Project 读取方式

GPT Project 后续遇到问题、修改、修复、纠偏、需求不清楚、机制调整、执行方式变化、判断标准变化或失败反馈路由变化时，优先读取：

1. `项目主读文件_GPT_PROJECT_MAIN_READ_FILES/GPT数据源/11_项目状态动作总控器_机制推理层.md`
2. `项目主读文件_GPT_PROJECT_MAIN_READ_FILES/GPT数据源/01_项目系统提示词.md`
3. `本轮机制补丁_MECHANISM_PATCH.md`
4. `当前日志与索引_CURRENT_LOGS_AND_INDEXES/codex_log/latest.md`

如果需要继续下发 Codex，再对照：

5. `Codex执行层镜像_CODEX_MIRROR_FILES/codex_source/00_codex_readme.md`
6. `Codex执行层镜像_CODEX_MIRROR_FILES/codex_source/19_project_state_action_router.md`

## 5. 本包不包含

- 视频文件
- 图片素材
- 音频
- 源视频
- `dist/latest_review_pack/`
- secret
- API key
- token
- 无关 `public/` 文件
- 大量历史日志

## 6. 边界

本包生成不代表用户已经上传到 GPT Project UI，不代表 GPT Project UI 已同步成功，不代表机制已被长期真实任务验证。

本包不推进 `content_validation / send_ready / publish_status_success / voice_validation / final_voice_validated / visual_master_locked / current_data_goal_anchor ready`。
