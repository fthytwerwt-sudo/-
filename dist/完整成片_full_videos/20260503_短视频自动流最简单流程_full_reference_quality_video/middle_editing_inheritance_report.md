# middle_editing_inheritance_report

- status：partial_blocked_before_final_assembly
- 是否读取 round34 中段剪辑参考：true
- 是否读取中段放大参考：true
- 是否继承：partial，已在 cut map 和 prepared_visuals 中按时间码预处理；未进入最终云剪成片
- 中段主体是否为用户录制素材：partial，manifest 中用户素材段已准备，但没有 final_video
- 是否输出 contact sheet：true
- 偏差是否阻断完整片：true，项目 TTS / API visual quota 阻断完整片

| 段落 | 素材 | 时间码 | 裁切/放大 | 遮挡 | 证明什么 | 不能证明什么 |
| --- | --- | --- | --- | --- | --- | --- |
| seg02 | 豆包素材.mp4 | 00:00:16-00:00:24 | 是 | 否 | 用户一句需求输入 | 不能证明 Trae 已执行 |
| seg04 | 豆包素材.mp4 | 00:01:28-00:02:00 | 是 | 否 | 豆包拆方案 | 不能证明工程跑通 |
| seg06 | 豆包素材.mp4 | 00:02:40-00:04:08 | 是 | 否 | 豆包输出 Trae prompt | 不能证明脚本运行成功 |
| seg07 | trae 素材.mp4 | 00:00:32-00:01:52 | 是 | 底部路径遮挡 | Trae SOLO / Updating Tasks / 11 个待办 | 不能证明代码运行成功 |
| seg08 | trae 素材.mp4 | 00:02:00-00:02:40 | 是 | 底部路径遮挡 | vlog_automation_workflow 项目骨架 | 不能证明 app 已跑通 |
| seg14 | codex 素材.mp4 | 00:02:56-00:03:08 | 是 | 右侧与底部遮挡 | Codex 执行检查线索 | 不能证明内容过线 |
