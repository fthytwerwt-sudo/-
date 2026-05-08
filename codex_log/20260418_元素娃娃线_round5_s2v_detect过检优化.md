# 20260418｜元素娃娃线 round5 s2v detect 过检优化

## read_files

- `已确认` 已读：
  - `AGENTS.md`
  - `codex_source/00_codex_readme.md`
  - `codex_source/01_execution_rules.md`
  - `codex_log/latest.md`
  - `GPT数据源/01_项目系统提示词.md`
  - `GPT数据源/08_当前正式事实.md`
  - `GPT数据源/09_目标态计划.md`
  - `codex_log/20260418_豆包vnext_C线元素娃娃能力审计.md`
  - `codex_log/20260418_元素娃娃线_round3_切换wan2.7与s2v闭环.md`
  - `codex_log/20260418_元素娃娃线_round4_s2v_detect过检优化.md`
  - `dist/20260417_豆包的正确打开方式_vnext/host_motion_asset_gate_round4/audit/最小闸门审计_round4.md`
  - `formal_api_demo_core.py`
  - `scripts/元素娃娃线_round4_s2v_detect过检优化.py`
  - `~/.config/video-factory/formal_api_demo.local.toml`

## skills_check

- `已确认` 当前仓库本地 `skills/` 目录不存在。
- `已确认` 已回退检查全局 `~/.codex/skills`。
- `已确认` 已检查：
  - `using-superpowers`
  - `context-driven-development`
  - `verification-before-completion`
  - `systematic-debugging`
- `已确认` 本轮实际采用：
  - `using-superpowers`
  - `systematic-debugging`
  - `verification-before-completion`
- `部分成立` `context-driven-development` 已检查，但本轮未进入 `conductor/` 上下文工件维护。

## round4_delta_direction

- `已确认` round4 之后，本轮唯一主方向固定为：
  - 继续向 `候选C_半体素软面部主持娃娃` 靠近
  - 但进一步去掉玩偶感 / 娃娃感
  - 让脸更像卡通数字人肖像
  - 继续增大脸部占比并强化眼白 / 虹膜 / 鼻孔 / 唇形
- `已确认` 本轮同时修正了一个真实代码问题：
  - round3 / round4 自定义 `wan2.2-s2v-detect` 解析误读了 `output.pass`
  - 实际可用字段是：`output.check_pass`

## asset_candidate_changes

- `已确认` 本轮独立目录已建立：
  - `dist/20260417_豆包的正确打开方式_vnext/host_motion_asset_gate_round5/`
- `已确认` 本轮建立了：
  - `assets/`
  - `detect_probe/`
  - `audit/`
- `已确认` 本轮按“逐张生成、逐张 detect、谁先过谁停”执行。
- `已确认` 第 1 张新资产就已满足 detect：
  - `候选A_round5_软脸主持肖像`
- `已确认` 由于首张已过检，本轮没有继续批量生成 B / C / D / E。
- `已确认` 该资产由 `wan2.7-image-pro` 真实成功生成：
  - [候选A_round5_软脸主持肖像_wan2.7-image-pro_review_1080x1920.png](/Users/fan/Documents/视频工厂/dist/20260417_豆包的正确打开方式_vnext/host_motion_asset_gate_round5/assets/候选A_round5_软脸主持肖像_wan2.7-image-pro_review_1080x1920.png)

## detect_probe_result

- `已确认` 当前过检资产已锁定为：
  - `候选A_round5_软脸主持肖像`
- `已确认` `wan2.2-s2v-detect` 返回：
  - `status = success`
  - `request_id = fb58d3d5-1fbe-949d-ac3e-dc152b016cb1`
- `已确认` 当前最小完成目标已达成：
  - 至少 1 张新资产通过 detect

## optional_s2v_smoke_test

- `已确认` 本轮额外做了 1 次最短 `wan2.2-s2v` smoke test。
- `已确认` smoke test 返回：
  - `status = success`
  - 已落出最小视频：
    - [候选A_round5_软脸主持肖像_video.mp4](/Users/fan/Documents/视频工厂/dist/20260417_豆包的正确打开方式_vnext/host_motion_asset_gate_round5/s2v_probe/visual/候选A_round5_软脸主持肖像_video.mp4)
  - 已落出联系表：
    - [s2v_smoke_contact_sheet.jpg](/Users/fan/Documents/视频工厂/dist/20260417_豆包的正确打开方式_vnext/host_motion_asset_gate_round5/audit/s2v_smoke_contact_sheet.jpg)
- `已确认` 但这只代表：
  - 新路线 detect gate + smoke route 已成立
- `已确认` 这不代表：
  - 主线可用
  - 高质量视频级样片已成立

## technical_validation

- `已确认` `passed_for_detect_gate`
- `已确认` 理由：
  - 至少 1 张新资产真实过检
  - 可选最短 smoke test 也真实成功

## content_validation

- `已确认` `blocked`
- `已确认` 理由：
  - 当前还没有对 round5 smoke 视频做正式质量判断
  - 还没有确认是否摆脱 `gif / 图片动起来`
  - 还没有确认口型 / 头部 / 动作是否达到主持壳最低可用线

## recommended_next_route

- `已确认` 当前不要回退到旧 `wan2.6-image -> liveportrait`。
- `已确认` 当前新路线已至少跨过：
  - `detect gate`
  - `smoke route`
- `已确认` 下一步最值路线应转到：
  1. 审 round5 smoke 视频是否仍像 `gif / 图片动起来`
  2. 审口型 / 头部 / 动作是否达到主持壳最低可用线
  3. 若不过线，再继续沿新路线修资产和参数

## git_commit_and_push_status

- `待验证` 本日志落盘时尚未提交 / 推送。

## reading_branch_sync_status

- `待验证` 本日志落盘时尚未同步回 `codex/user-readable-map`。
