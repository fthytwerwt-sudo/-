# 2026-04-04 formal_api_demo seg02 质量修正过线

## 本轮目标

- 正式切回《视频工厂》A 线普通主线质量修正。
- 只围绕 `seg02` 把当前质量线打穿。

## 执行前已确认事实

- 当前默认主读取分支：
  - `codex/user-readable-map`
- 当前技术主链正式状态：
  - `TTS API = success`
  - `图片 API = success`
  - `通用视频 API = success`
  - `真人开口分支 = success`
  - `local assembly = success`
  - `overall 技术主链 = success`
- 当前不再把真人开口链路当 blocker。
- 用户要求补读的
  - `codex_log/20260403_formal_api_demo_quality_review_and_liveportrait_round1.md`
  当前分支不存在。

## 当前质量基线

- 当前工作分支：
  - `codex/round1`
- 当前 HEAD：
  - `f20dcd199ad40371d767784408be45d36f44ff0e`
- 当前工作区里仍有用户侧未提交改动：
  - `project_source/00_project_brief.md`
  - `project_source/01_project_system_prompt.md`
  - `project_source/03_perplexity_prompt_library.md`
  - `project_source/04_review_templates.md`
  - `project_source/06_project_index.md`
  - `project_source/08_quality_baseline_and_90_score_rules.md`
  - `.omx/`
- 本轮未碰上述文件。
- 当前正式产物：
  - [dist/formal_api_demo/final.mp4](/Users/fan/Documents/视频工厂/dist/formal_api_demo/final.mp4)
- `seg02` 原基线承载：
  - [dist/formal_api_demo/visual/seg02_image.png](/Users/fan/Documents/视频工厂/dist/formal_api_demo/visual/seg02_image.png)
  - [dist/formal_api_demo/visual/seg02_video.mp4](/Users/fan/Documents/视频工厂/dist/formal_api_demo/visual/seg02_video.mp4)
- 原 preview 结构问题：
  - `seg02` 被拆成“前态说明 + 后态说明”
  - 观众更容易看到“便签重排 + 覆盖说明层”
  - 不是“一眼就懂的可交接 SOP 接手链路”

## 主路线选择

- 继续优化普通图片 / 视频段生成。
- 不切真人开口。

### 选择原因

- 当前 `seg02_video.mp4` 已经有正确方向的动作雏形。
- 问题在于：
  - 被拆成 before / after 两页
  - 再叠大面积说明层
  - 导致视频证明力被稀释
- 本轮最短路径是把 `seg02` 改成一个单一视频主镜头，让画面先完成证明。

## 实际改动

### 1. `cases/formal_api_demo.md`

- 把 `seg02` 文案改成：
  - `一进 SOP 表，后面这条链就能接手了。`
- 把 `seg02` 画面意图改成：
  - 单一主镜头里，散乱字段和便签被吸附进 SOP 表单，最后出现可交接链路

### 2. `formal_api_demo_core.py`

- 不再把 `seg02` 拆成 before / after 两页。
- `seg02` 现在只保留一页 `process` slide，完整吃 6 秒视频。
- 强化 `seg02` 视频 prompt：
  - 单一固定镜头
  - 散乱字段从四周被吸附进同一张 SOP 表单
  - 末尾必须出现“可交接”状态条

### 3. `video_builder.swift`

- 把 `seg02` 的 media-first 布局继续压轻：
  - 由视频承担主证明
  - 顶部只保留小 badge
  - 底部只保留最小 headline / support / chips / detail
- 去掉大面积 SOP 覆盖层，让视频自己完成“进表 -> 可交接”的证明。

### 4. `tests/test_formal_api_demo_pipeline.py`

- 更新 `seg02` 文案断言。
- 更新 preview slide 断言：
  - `seg02` 现在只是一页 `process`
  - 直接吃视频承载

## 实际执行

### 文本 / 测试验证

- `python3 -m py_compile formal_api_demo_core.py tests/test_formal_api_demo_pipeline.py`
- `python3 -m unittest tests.test_formal_api_demo_pipeline`

结果：

- `Ran 28 tests`
- `OK`

### 真实 generation

- `python3 scripts/generate_formal_api_demo.py --local-config <temp runtime config with wan2.6-image + wan2.6-t2v> --out dist/formal_api_demo`

结果：

- `generation_status = success`
- `visual_generation_status = success`
- `seg02_video.mp4` 真实落地

### 真实 assembly

- `python3 scripts/assemble_formal_api_demo.py --manifest dist/formal_api_demo/manifest.json --local-config <same temp runtime config> --out dist/formal_api_demo`

结果：

- `overall_status = success`
- `assembly_status = success`
- `local_assembly_status = success`
- `artifact_paths.final_video = dist/formal_api_demo/final.mp4`

### 回审帧

- 重新抽取：
  - [dist/formal_api_demo/review_frames/final_01_hook.png](/Users/fan/Documents/视频工厂/dist/formal_api_demo/review_frames/final_01_hook.png)
  - [dist/formal_api_demo/review_frames/final_02_seg02_mid.png](/Users/fan/Documents/视频工厂/dist/formal_api_demo/review_frames/final_02_seg02_mid.png)
  - [dist/formal_api_demo/review_frames/final_03_seg02_late.png](/Users/fan/Documents/视频工厂/dist/formal_api_demo/review_frames/final_03_seg02_late.png)
  - [dist/formal_api_demo/review_frames/final_04_outcome.png](/Users/fan/Documents/视频工厂/dist/formal_api_demo/review_frames/final_04_outcome.png)
  - [dist/formal_api_demo/review_frames/seg02_video_01.png](/Users/fan/Documents/视频工厂/dist/formal_api_demo/review_frames/seg02_video_01.png)
  - [dist/formal_api_demo/review_frames/seg02_video_02.png](/Users/fan/Documents/视频工厂/dist/formal_api_demo/review_frames/seg02_video_02.png)

## 新产物

- 正式成片：
  - [dist/formal_api_demo/final.mp4](/Users/fan/Documents/视频工厂/dist/formal_api_demo/final.mp4)
- 当前 `seg02` 主证明素材：
  - [dist/formal_api_demo/visual/seg02_video.mp4](/Users/fan/Documents/视频工厂/dist/formal_api_demo/visual/seg02_video.mp4)
- 当前 preview 清单：
  - [dist/formal_api_demo/assembly/preview_manifest.json](/Users/fan/Documents/视频工厂/dist/formal_api_demo/assembly/preview_manifest.json)

## 质量线 5 条逐条结果

- 1. `seg02` 变化真正被看见：
  - `passed`
  - 当前 `seg02` 是单一视频主镜头，能直接看见：
    - 散乱字段
    - 进入 SOP 表
    - 最终出现“可交接”状态
- 2. 中段文案不再像说明书：
  - `passed`
  - 当前文案变成结果句，而不是机制说明句
- 3. demo / PPT 感明显下降：
  - `passed`
  - 当前中段已不再靠 before / after 说明卡撑住
  - 视频自己承担了主证明
- 4. Hook 仍成立：
  - `passed`
- 5. 结尾落点仍成立：
  - `passed`

## 当前最终状态

- `quality_passed`

## `.gitignore` 边界

- `dist/formal_api_demo/` 当前被 `.gitignore` 忽略。
- 因此以下产物属于 `local_only`：
  - `dist/formal_api_demo/final.mp4`
  - `dist/formal_api_demo/visual/seg02_video.mp4`
  - `dist/formal_api_demo/review_frames/*`
- 它们不会上传到 GitHub。
- 这不阻断本轮代码 / 日志 / 规则同步回主读取分支。
- 但只看 GitHub 的新会话无法直接打开这些本地二进制产物。

## 下一轮唯一最关键一步

- 若继续做 A 线提质，优先再压：
  - Hook 和结尾的卡片覆盖层
  让整支片子的卡片感继续下降，而不是回头重修技术链。
