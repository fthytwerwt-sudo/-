# middle_segment_cut_map_v2

| segment | 素材 | 时间码 | 证据点 | 必须可读内容 | crop 策略 | 是否允许运动 | 不能证明什么 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `seg02` | `/Users/fan/Documents/视频工厂/素材录制/最新素材/豆包素材.mp4` | `16.0s` | 用户只输入一句“我想用 Trae 做一个短视频自动流” | 豆包输入区 | `crop_x=960, crop_y=60, crop_w=1500, crop_h=2100, scale=fit_to_936x1320, anchor_area=豆包输入区` | `fixed_window_only` | 不能证明 Trae 已执行 |
| `seg04` | `/Users/fan/Documents/视频工厂/素材录制/最新素材/豆包素材.mp4` | `88.0s` | 从 0 基础轻量版到无人值守版、核心流程工位 | 豆包方案标题和流程列表 | `crop_x=930, crop_y=60, crop_w=1560, crop_h=2100, scale=fit_to_936x1320, anchor_area=豆包方案标题和流程列表` | `fixed_window_only` | 不能证明工程已跑通 |
| `seg06` | `/Users/fan/Documents/视频工厂/素材录制/最新素材/豆包素材.mp4` | `232.0s` | Trae Vlog 自动流核心搭建 Prompt 与模块清单 | prompt 标题和模块列表 | `crop_x=930, crop_y=60, crop_w=1560, crop_h=2100, scale=fit_to_936x1320, anchor_area=prompt 标题和模块列表` | `fixed_window_only` | 不能证明脚本运行成功 |
| `seg07` | `/Users/fan/Documents/视频工厂/素材录制/最新素材/trae 素材.mp4` | `80.0s` | Prompt 进入 Trae，出现 Updating Tasks 和 11 个待办 | Trae 输入区 / 任务区 | `crop_x=960, crop_y=60, crop_w=1560, crop_h=2100, scale=fit_to_936x1320, anchor_area=Trae 输入区 / 任务区` | `fixed_window_only` | 不能证明代码运行成功 |
| `seg08` | `/Users/fan/Documents/视频工厂/素材录制/最新素材/trae 素材.mp4` | `120.0s` | vlog_automation_workflow 项目骨架和目录文件 | Trae 文件目录区域 | `crop_x=1800, crop_y=60, crop_w=1500, crop_h=2100, scale=fit_to_936x1320, anchor_area=Trae 文件目录区域` | `fixed_window_only` | 不能证明 app 已跑通 |
| `seg14` | `/Users/fan/Documents/视频工厂/素材录制/最新素材/codex 素材.mp4` | `176.0s` | Codex 执行检查：命令、文件变更、报告线索 | 安全命令 / 报告区域 | `crop_x=500, crop_y=60, crop_w=1560, crop_h=2100, scale=fit_to_936x1320, anchor_area=安全命令 / 报告区域` | `fixed_window_only` | 不能证明内容过线 |
