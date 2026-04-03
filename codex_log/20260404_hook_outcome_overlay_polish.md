# 2026-04-04 hook / outcome overlay 轻量提质

## 本轮目标

- 不重修技术链
- 不重开 `seg02` 主结构
- 只轻量压：
  - Hook 卡片覆盖层
  - 结尾卡片覆盖层

## 执行前已确认事实

- 当前默认主读取分支：
  - `codex/user-readable-map`
- 当前技术主链：
  - `success`
- 当前 A 线质量状态：
  - `quality_passed`
- 当前问题不在技术链和中段成立性，而在：
  - Hook 覆盖层仍偏厚
  - 结尾覆盖层仍偏“系统总结页”

## 当前基线问题

### Hook

- 下半屏存在明显大白底主卡。
- 问题抓手虽然成立，但现场画面被压成背景。
- 当前更像“程序说明页 + 问题对照卡”。

### 结尾

- 整块白底卡加大橙色横幅占屏过重。
- 背景 SOP 板被压成装饰层。
- 当前更像“结果总结页”，不像自然收束。

## 主路线选择

- 保留当前结构。
- 只压 Hook / 结尾布局覆盖层。
- 只重跑 assembly，不重跑 generation。

## 实际改动

- 只修改：
  - [video_builder.swift](/Users/fan/Documents/视频工厂/video_builder.swift)

### Hook 页处理

- 不再使用整块大白底主卡。
- 改成：
  - 更小的双锚点浮动卡
  - 更轻的底部提示条
- 让背景桌面画面重新露出来。

### 结尾页处理

- 不再使用大白底卡 + 大橙色横幅 + 大双卡的重覆盖组合。
- 改成：
  - 更薄的结果条
  - 更小的左右收束卡
  - 更轻的底部说明条
- 让背景 SOP 板和样片缩略图露出更多。

## 实际执行

- `python3 scripts/assemble_formal_api_demo.py --manifest dist/formal_api_demo/manifest.json --local-config config/formal_api_demo.local.toml --out dist/formal_api_demo`
- `python3 -m unittest tests.test_formal_api_demo_pipeline`
- 用本地 ffmpeg 重新抽：
  - Hook 回审帧
  - 结尾回审帧

## 新产物

- 成片：
  - [dist/formal_api_demo/final.mp4](/Users/fan/Documents/视频工厂/dist/formal_api_demo/final.mp4)
- Hook 回审帧：
  - [dist/formal_api_demo/review_frames/final_01_hook_polish.png](/Users/fan/Documents/视频工厂/dist/formal_api_demo/review_frames/final_01_hook_polish.png)
- 结尾回审帧：
  - [dist/formal_api_demo/review_frames/final_04_outcome_polish.png](/Users/fan/Documents/视频工厂/dist/formal_api_demo/review_frames/final_04_outcome_polish.png)

## 轻量提质回审结果

- 1. Hook 卡片覆盖层是否明显下降：
  - `passed`
- 2. 结尾卡片覆盖层是否明显下降：
  - `passed`
- 3. 是否引入新的信息缺失：
  - `no`
- 4. Hook 是否仍成立：
  - `passed`
- 5. 结尾落点是否仍成立：
  - `passed`
- 6. 当前整片是否比上版更接近“真人会发”的视频感：
  - `yes`

## 当前最终状态

- `polish_passed`

## `.gitignore` / `local_only`

- `dist/formal_api_demo/` 仍属于 `.gitignore` / `local_only`
- 因此：
  - `final.mp4`
  - `review_frames/*`
  不会上 GitHub
- 但它们已在本地生成，足以完成本轮验收
- 当前应优先查看：
  - `dist/formal_api_demo/final.mp4`

## 下一轮唯一最关键一步

- 若还要继续轻磨，只做更细的字重 / 条厚度调整即可。
- 当前不需要再开新战场。
