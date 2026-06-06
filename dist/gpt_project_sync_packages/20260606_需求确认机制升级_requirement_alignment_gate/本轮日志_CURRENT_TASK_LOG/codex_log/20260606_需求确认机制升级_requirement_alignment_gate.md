# 20260606 需求确认机制升级

## 任务目标

本轮只做《视频工厂》GPT Project 配合机制升级：当用户提出问题、修改、修复、纠偏、需求不清楚、机制调整、执行方式变化、判断标准变化或失败反馈路由变化时，GPT Project / ChatGPT 先做五层需求确认，再决定是否下发 Codex。

本轮不做视频，不生成文案，不生成下一条视频执行 prompt，不修改任何视频产物。

## 用户确认的触发边界

触发：

- 遇到问题。
- 需求不清楚。
- 需要修改、修复、纠偏、优化或调整机制。
- 新需求可能和旧流程、旧机制、旧默认执行方式、旧判断标准或失败反馈路由冲突。

不触发：

- 正常执行。
- 正常做视频。
- 已进入已确认流程，且没有异常反馈或新冲突。
- 用户明确说“这轮只执行，别确认”，且不存在明显冲突、风险或需求不清。

## 写入机制

新增 / 补强状态：

- `requirement_alignment_needed（需求对齐必需）`

五层确认链：

1. `目标层`：这次到底要服务什么结果，本轮不解决什么。
2. `机制层`：什么情况触发、禁止、降级，旧机制如何处理。
3. `流程层`：确认后按什么步骤执行，哪些由 ChatGPT 判断，哪些由 Codex 执行，哪些需要用户确认。
4. `判断标准层`：做到什么算通过，什么算失败，技术 / 内容 / 审美 / 人感 / 状态推进必须分开。
5. `反馈层`：失败后回目标层、机制层、流程层、素材层、reference 层、验收层，还是路线重判。

冲突提醒：

- 新需求是否和旧执行方式冲突。
- 旧机制是否需要降权、替换、保留为历史或只作为 fallback。
- 如果不处理冲突，Codex 是否会继续按旧流程执行。

商品案例边界：

- 商品案例只作为解释示例，不写成《视频工厂》当前正式主线。
- 当前项目身份仍是 `OPC 一人公司 AI 闭环验证系统`，默认价值仍是 `真实 AI 使用经验 + 工作提效实录`。

## 修改文件

- `GPT数据源/11_项目状态动作总控器_机制推理层.md`
- `GPT数据源/01_项目系统提示词.md`
- `codex_source/00_codex_readme.md`
- `codex_log/latest.md`
- `codex_log/20260606_需求确认机制升级_requirement_alignment_gate.md`

## 未修改文件与未推进项

- 未修改 `dist/` 视频产物。
- 未修改 `public/`。
- 未修改 `review_loop/records/`。
- 未修改 `review_loop/screenshots/`。
- 未生成新视频。
- 未生成正式文案。
- 未生成下一条视频执行 prompt。
- 未推进 `content_validation / send_ready / publish_status_success / voice_validation / final_voice_validated / visual_master_locked / current_data_goal_anchor ready`。

## 验证结果

- `grep requirement_alignment_needed`: passed
- `grep 正常执行 / 正常做视频`: passed
- `grep 五层字段`: passed
- `商品案例误写检查`: passed，新增内容只写解释示例和否定边界，未写成正式主线
- `forbidden status promotion check`: passed，按本轮 diff 窄检查，未推进禁止状态
- `git diff --check`: passed
- `secret scan`: passed

## Git 状态

- `branch = main`
- `unrelated_dirty_files = public/`
- `commit_sha = 8d64f62a31f6a741934b2e21e1fcfca28bc4f80c`
- `pushed = true`
- `remote_head_verified = true`

## GPT Project 同步包追加生成

- `sync_package_generated = true`
- `gpt_project_upload_package_canonical_path = /Users/fan/Documents/视频工厂/dist/gpt_project_sync_packages/20260606_需求确认机制升级_requirement_alignment_gate/`
- `upload_manifest_path = /Users/fan/Documents/视频工厂/dist/gpt_project_sync_packages/20260606_需求确认机制升级_requirement_alignment_gate/上传说明_UPLOAD_MANIFEST.md`
- `current_local_artifact_paths_updated = true`
- `package_based_on_commit = 8d64f62a31f6a741934b2e21e1fcfca28bc4f80c`
- `ready_for_user_upload = true_after_manifest_and_path_verification`
- `upload_boundary = local_package_generated_only_not_user_uploaded`
