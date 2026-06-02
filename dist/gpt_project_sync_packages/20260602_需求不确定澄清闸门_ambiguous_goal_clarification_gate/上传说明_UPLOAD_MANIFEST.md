# GPT Project 上传说明｜需求不确定澄清闸门

## 1. 文件定位

本目录是给 GPT Project 上传的资料同步包，用于同步 2026-06-02 新增的 `ambiguous_goal_clarification_needed（需求不确定，需要澄清）` 与 `ambiguous_reference_goal_gate（参考目标歧义闸门）`。

本包只同步机制资料，不是视频产物，不是媒体包，不是运行日志大包。

## 2. 建议上传文件

上传本目录下全部 Markdown 文件和两个子目录：

- `上传说明_UPLOAD_MANIFEST.md`
- `同步说明_SYNC_SUMMARY.md`
- `变更文件清单_CHANGED_FILES.md`
- `本轮机制补丁_MECHANISM_PATCH.md`
- `状态边界_STATUS_BOUNDARY.md`
- `项目入口文件_PROJECT_ENTRY_FILES/`
- `Codex执行层镜像_CODEX_MIRROR_FILES/`

## 3. 上传后 GPT Project 读取方式

GPT Project 后续命中 `1:1 / 像对标 / 高级感 / 按这个效果做 / 不是一回事 / 完全不像 / 感觉不像 / 差点意思` 时，先读取：

1. `项目入口文件_PROJECT_ENTRY_FILES/11_项目状态动作总控器_机制推理层.md`
2. `项目入口文件_PROJECT_ENTRY_FILES/12_参考到执行落地契约_reference_to_execution_contract.md`
3. `本轮机制补丁_MECHANISM_PATCH.md`

如果需要继续下发 Codex，再对照：

4. `Codex执行层镜像_CODEX_MIRROR_FILES/19_project_state_action_router.md`
5. `Codex执行层镜像_CODEX_MIRROR_FILES/20_reference_to_execution_contract.md`

## 4. 本包不包含

- 视频文件
- 图片素材
- 音频
- 源视频
- `dist/latest_review_pack/`
- secret
- API key
- token
- 大量历史日志
- 无关 `public/` 文件

## 5. 边界

本包生成不代表用户已经上传到 GPT Project UI，不代表 GPT Project UI 已同步成功，不代表机制已被长期真实任务验证。
