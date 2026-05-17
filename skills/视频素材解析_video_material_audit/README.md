# 视频素材解析 video_material_audit

项目内可复用 skill。命中“素材录制 / 解析视频 / 第几期素材 / 素材审计 / 给 ChatGPT 写素材报告”时，Codex 必须先读取：

```text
skills/视频素材解析_video_material_audit/SKILL.md
```

使用边界：

- 只做素材审计、证据判断、风险判断和 ChatGPT 可写稿报告。
- 不生成视频。
- 不写最终文案。
- 不推进 `content_validation / send_ready / publish_candidate / current_data_goal_anchor ready`。
- 不提交原始视频素材。

推荐输出目录：

- 审计报告：`codex_log/material_audit/<episode>/`
- 本地 contact sheet：`dist/material_audit/<episode>/`
