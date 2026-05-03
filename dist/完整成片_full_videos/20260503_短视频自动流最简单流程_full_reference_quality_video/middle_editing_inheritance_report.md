# middle_editing_inheritance_report

- status：passed
- 是否读取 round34 中段剪辑参考：true
- 是否读取中段放大参考：true
- 是否继承：true
- 中段主体是否为用户录制素材：true
- 是否输出 contact sheet：true
- 是否进入最终云剪成片：true
- 中段放大/缩小机制：passed；6 个中段录屏段落已从静态 cover 改为 middle_reference_zoom* 动态 crop_x 证据窗口
- 云剪后复核：passed；从云端下载后的 full_video.mp4 重抽帧确认中段窗口仍在最终片中
- middle_zoom_contact_sheet：`/Users/fan/Documents/视频工厂/dist/完整成片_full_videos/20260503_短视频自动流最简单流程_full_reference_quality_video/middle_zoom_contact_sheet.jpg`
- local_reference_assembly_used：false；云剪成片已保留中段放大裁切标准，本轮未启用本地总装版
- 偏差是否阻断完整片：false

| 段落 | 素材 | 时间码 | 裁切/放大 | 遮挡 | 证明什么 | 不能证明什么 |
| --- | --- | --- | --- | --- | --- | --- |
| seg02 | 豆包素材.mp4 | 00:00:16-00:00:24 | 是 | 否 | 用户一句需求输入 | 不能证明 Trae 已执行 |
| seg04 | 豆包素材.mp4 | 00:01:28-00:02:00 | 是 | 否 | 豆包拆方案 | 不能证明工程跑通 |
| seg06 | 豆包素材.mp4 | 00:02:40-00:04:08 | 是 | 否 | 豆包输出 Trae prompt | 不能证明脚本运行成功 |
| seg07 | trae 素材.mp4 | 00:00:32-00:01:52 | 是 | 底部路径遮挡 | Trae SOLO / Updating Tasks / 11 个待办 | 不能证明代码运行成功 |
| seg08 | trae 素材.mp4 | 00:02:00-00:02:40 | 是 | 底部路径遮挡 | vlog_automation_workflow 项目骨架 | 不能证明 app 已跑通 |
| seg14 | codex 素材.mp4 | 00:02:56-00:03:08 | 是 | 右侧与底部遮挡 | Codex 执行检查线索 | 不能证明内容过线 |

中段主体由用户录制素材承担，卡片只做边界说明和总结辅助。
