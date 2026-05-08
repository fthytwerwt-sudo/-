# 2026-04-04 formal_api_demo A 线普通主线质量修正 round2

## 本轮目标

- 切回 A 线普通主线质量修正。
- 直接执行到：
  - 当前质量线过线
  - 或把新的真实 blocker 压到最具体
- 不停在计划、建议、审计或复盘层。

## 执行前真实基线

- 当前分支：
  - `codex/round1`
- 当前 HEAD：
  - `5aab536fda6b2a564359171d72d60d3cd2bb3800`
- 用户给出的默认读取分支是：
  - `codex/user-readable-map`
- 当前分支与用户默认读取分支不一致。
- 当前工作区里还存在用户侧未提交改动：
  - `project_source/00_project_brief.md`
  - `project_source/01_project_system_prompt.md`
  - `project_source/03_perplexity_prompt_library.md`
  - `project_source/04_review_templates.md`
  - `project_source/06_project_index.md`
  - `project_source/08_quality_baseline_and_90_score_rules.md`
  - `.omx/`
- 本轮未改这些文件。
- 用户要求先读的
  - `codex_log/20260403_formal_api_demo_quality_review_and_liveportrait_round1.md`
  在当前分支不存在。
- 当前正式产物现状：
  - 历史 `dist/formal_api_demo` 里原先没有 `final.mp4`
  - 只有 `assembly/formal_api_demo_preview.mp4`
  - `seg02` 当时没有真实视觉素材落地
  - `preview_manifest.json` 只是一版 3 页文字卡样片

## 本轮主路线选择

- 选择：
  - 继续优化普通图片 / 视频主线，不切真人开口
- 选择原因：
  - 当前工作区里已经有可用的普通 generation 主链：
    - `wan2.6-image`
    - `wan2.6-t2v`
  - 当前工作区没有可直接复用的 liveportrait 成品或成片目录。
  - 本轮质量缺口集中在 `seg02` 的视觉证明不足，不值得切到真人支线开新战场。

## 命中的 skill

- `systematic-debugging`
  - 先确认当前 `seg02` 为什么不成立，再改，不猜。
- `test-driven-development`
  - 先补失败测试，约束 `seg02` 文案、preview 结构、本地 `final.mp4` 交付。
- `verification-before-completion`
  - 先跑 `py_compile` / `unittest` / 真实 generation / 真实 assembly，再给状态结论。

## 实际改动

### 1. `cases/formal_api_demo.md`

- 保住 Hook 与结尾不动。
- 把 `seg02` 配音 / 字幕从：
  - `先把目标、输入、输出压成 SOP，再让生成和组装按流程跑。`
  改成：
  - `目标、输入、输出一拉齐，这条链就接上了。`
- 把 `seg01 / seg02 / seg03` 的画面意图从偏“信息卡 / 说明卡”改成更像真实工作流场景与收束结果。

### 2. `formal_api_demo_core.py`

- 把图片 / 视频 prompt 从明确的 “PPT 卡片式信息层级” 改成：
  - 真实工作台 / 白板 / 便签 / SOP 表单导向
  - 明确禁止只做静态卡片切页
- 把 preview slide 结构从 3 页改成 4 页：
  - `seg01` hook
  - `seg02` before
  - `seg02` after
  - `seg03` outcome
- `seg02 after` 显式吃：
  - `background_video_path = dist/formal_api_demo/visual/seg02_video.mp4`
- 恢复当前阶段本地交付语义：
  - preview 成功后，本地 assembly 记为 `success`
  - 正式交付件落到 `dist/formal_api_demo/final.mp4`
- 更新 assembly summary：
  - `artifact_paths.final_video` 指向 `dist/formal_api_demo/final.mp4`
  - `current_missing_*` 在 overall success 时不再残留 cloud 缺口

### 3. `video_builder.swift`

- 让组装器能读取：
  - `background_image_path`
  - `background_video_path`
- 为 `seg02 after` 新增 media-first 过渡布局：
  - 先用真实视频做主画面
  - 再叠加更小的 SOP 表单 / 结构行，而不是整张大白卡硬盖住
- 让 `seg01 / seg03` 能吃图片背景，降低纯白底卡片感。

### 4. `tests/test_formal_api_demo_pipeline.py`

- 新增 / 更新测试，锁住：
  - `seg02` 新文案
  - preview 结构必须拆成 before / after
  - 本地 assembly 成功后必须落 `final.mp4`
  - visual assets ready 时 `assembly_status = success`

## 实际运行的命令

- 测试与静态验证：
  - `python3 -m py_compile formal_api_demo_core.py tests/test_formal_api_demo_pipeline.py`
  - `python3 -m unittest tests.test_formal_api_demo_pipeline`
- 真实 generation 第 1 轮：
  - `python3 scripts/generate_formal_api_demo.py --local-config <temp runtime config with wan2.6-image + wan2.6-t2v> --out dist/formal_api_demo`
- 真实 assembly 第 1 轮：
  - `python3 scripts/assemble_formal_api_demo.py --manifest dist/formal_api_demo/manifest.json --local-config <same temp runtime config> --out dist/formal_api_demo`
- 关键帧抽取 / 回审：
  - `.../node_modules/ffmpeg-static/ffmpeg -ss ... -i dist/formal_api_demo/final.mp4 ...`
  - `.../node_modules/ffmpeg-static/ffmpeg -ss ... -i dist/formal_api_demo/visual/seg02_video.mp4 ...`
- 真实 generation 第 2 轮：
  - `python3 scripts/generate_formal_api_demo.py --local-config <temp runtime config with wan2.6-image + wan2.6-t2v> --out dist/formal_api_demo`
- 真实 assembly 第 2 轮：
  - `python3 scripts/assemble_formal_api_demo.py --manifest dist/formal_api_demo/manifest.json --local-config <same temp runtime config> --out dist/formal_api_demo`

## 真实产物

- 正式本地交付件：
  - [dist/formal_api_demo/final.mp4](/Users/fan/Documents/视频工厂/dist/formal_api_demo/final.mp4)
- 预览组装：
  - [dist/formal_api_demo/assembly/formal_api_demo_preview.mp4](/Users/fan/Documents/视频工厂/dist/formal_api_demo/assembly/formal_api_demo_preview.mp4)
  - [dist/formal_api_demo/assembly/preview_manifest.json](/Users/fan/Documents/视频工厂/dist/formal_api_demo/assembly/preview_manifest.json)
- 视觉资产：
  - [dist/formal_api_demo/visual/seg01_image.png](/Users/fan/Documents/视频工厂/dist/formal_api_demo/visual/seg01_image.png)
  - [dist/formal_api_demo/visual/seg02_image.png](/Users/fan/Documents/视频工厂/dist/formal_api_demo/visual/seg02_image.png)
  - [dist/formal_api_demo/visual/seg02_video.mp4](/Users/fan/Documents/视频工厂/dist/formal_api_demo/visual/seg02_video.mp4)
  - [dist/formal_api_demo/visual/seg03_image.png](/Users/fan/Documents/视频工厂/dist/formal_api_demo/visual/seg03_image.png)
- 回审帧：
  - [dist/formal_api_demo/review_frames/final_01_hook.png](/Users/fan/Documents/视频工厂/dist/formal_api_demo/review_frames/final_01_hook.png)
  - [dist/formal_api_demo/review_frames/final_02_seg02_before.png](/Users/fan/Documents/视频工厂/dist/formal_api_demo/review_frames/final_02_seg02_before.png)
  - [dist/formal_api_demo/review_frames/final_03_seg02_after.png](/Users/fan/Documents/视频工厂/dist/formal_api_demo/review_frames/final_03_seg02_after.png)
  - [dist/formal_api_demo/review_frames/final_04_outcome.png](/Users/fan/Documents/视频工厂/dist/formal_api_demo/review_frames/final_04_outcome.png)

## 本轮两次真实回审结论

- 第 1 轮回审结论：
  - `still_blocked`
  - blocker：
    - 更像“卡片归位 / 便签重排”
    - 不是“可交接 SOP 成型”
- 第 2 轮回审结论：
  - `still_blocked`
  - blocker 进一步压实为：
    - `seg02` 仍没有把“散乱现场 -> 结构化 SOP 接手链路”的可感知变化做成一眼看懂
    - 观众更像看到“便签重新摆了一下 + 继续讲概念”
    - 不是“明确收拢 / 归位 / 可接手”

## 质量线 5 条逐条结果

- 1. `seg02` 必须让观众直观看到“散乱 -> 结构化 SOP”的变化：
  - `failed`
  - before 有了，但 after 仍更像卡片/便签重排，不像 SOP 接手链路成型
- 2. 中段文案不再像抽象方法说明书：
  - `failed`
  - 比旧版更短，但仍偏解释层，像制作说明，不像 demo 结果自身在说话
- 3. 整支视频 demo / PPT 感必须明显下降：
  - `partial_but_not_enough`
  - 已低于纯 3 页白底卡片，但前两张仍明显依赖静态卡片和覆盖层硬撑
- 4. Hook 和结尾落点要保住：
  - Hook：`passed`
  - Ending：`passed`
- 5. 当前已跑通的技术链不能被打回去：
  - `passed`
  - generation success
  - local assembly success
  - `final.mp4` 已真实落出

## 当前最终状态

- `still_blocked`

## 当前最具体 blocker

- `seg02` 仍未形成“结构化证据”：
  - 观众能看到“散乱”
  - 也能看到一些对齐后的字段
  - 但看不到“这份 SOP 现在已经能交接、能流转、能往下跑”的一眼式证明
- 本轮没有再卡在技术链：
  - 不是 TTS
  - 不是图片 API
  - 不是通用视频 API
  - 不是本地 assembly
- 当前 blocker 已压到质量表达层，而不是技术主链层

## 下一轮唯一最关键一步

- 不再让 `seg02` 先讲一句话、再摆几张卡。
- 直接把 `seg02` 改成“散乱字段被吸附到 SOP 表单的单一主动作镜头”，让画面自己先完成证明，再让文案退到补充层。
