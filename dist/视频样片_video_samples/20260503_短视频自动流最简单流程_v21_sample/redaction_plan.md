# redaction_plan｜短视频自动流 V2.1

## 1. 脱敏总原则

- `已确认` 不使用未脱敏火山引擎素材。
- `已确认` 不展示手机号、验证码、API Key 明文、资源 ID、账号信息、URL 中可能暴露账号或资源的信息、密钥、token、secret、AccessKey、临时授权 URL。
- `已确认` 不提交未脱敏截图。

## 2. Segment 08 API 工位

- `type`：`card`
- `visual`：`api_info_card_fallback`
- `decision`：`redaction_blocked_fallback_to_info_card`
- `reason`：自动流程无法保证火山引擎 API 管理页局部零风险脱敏。
- `proof`：API 是流程工位 / 外部能力入口。
- `cannot_prove`：API 已接通、云剪稳定、内容过线。

## 3. Trae 遮挡

- 裁切本地路径。
- 遮挡底部路径与项目列表中不适合展示的信息。
- 保留 SOLO Coder、`/plan`、`/spec`、Updating Tasks、11 待办、项目骨架。

## 4. Codex 遮挡

- 遮挡右侧分支详情。
- 遮挡底部路径。
- 遮挡文件名、巨大 diff 数字、本地任务信息。
- 保留 ffprobe、命令执行、文件变更、Git 操作和报告文件的“检查感”。

## 5. 下一轮如需火山 API 特写

必须先输出并审核：

1. `redaction_preview_contact_sheet.jpg`
2. `redaction_report.md`
3. 敏感项遮挡列表
4. 用户 / ChatGPT 审核结论

未通过前继续使用信息卡 fallback。
