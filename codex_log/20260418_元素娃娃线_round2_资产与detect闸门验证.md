# 20260418｜元素娃娃线 round2 资产与 detect 闸门验证

## read_files

- `已确认` 已读：
  - `AGENTS.md`
  - `codex_source/00_codex_readme.md`
  - `codex_source/01_execution_rules.md`
  - `codex_source/08_branch_sync_and_reading_branch_rules.md`
  - `codex_log/latest.md`
  - `GPT数据源/01_项目系统提示词.md`
  - `GPT数据源/08_当前正式事实.md`
  - `GPT数据源/09_目标态计划.md`
  - `dist/20260417_豆包的正确打开方式_vnext/host_motion_audit.md`
  - `codex_log/20260418_元素娃娃线_round1_技术样片.md`
  - `codex_log/20260418_豆包vnext_C线元素娃娃能力审计.md`
  - `dist/20260417_豆包的正确打开方式_vnext/host_motion_prototype_round1/audit/最小技术方案_round1.md`
  - `dist/20260417_豆包的正确打开方式_vnext/host_motion_prototype_round1/audit/技术验收_round1.md`
  - `formal_api_demo_core.py`
  - `~/.config/video-factory/formal_api_demo.local.toml`

## skills_check

- `已确认` 当前仓库本地 `skills/` 目录不存在。
- `已确认` 已回退检查全局 `~/.codex/skills`。
- `已确认` 已检查：
  - `using-superpowers`
  - `context-driven-development`
  - `verification-before-completion`
  - `systematic-debugging`
  - `brainstorming`
- `已确认` 本轮实际采用：
  - `using-superpowers`
  - `systematic-debugging`
  - `verification-before-completion`
- `部分成立` `context-driven-development` 已检查但本轮未进入 `conductor/` 上下文工件维护。
- `部分成立` `brainstorming` 已检查但本轮未单独启用设计审批流；原因是用户已把路线、边界和验收固定到“asset gate + 最小 detect/liveportrait 闭环”。

## connected_provider_recheck

- `已确认` 当前代码默认正式配置入口仍是：
  - `~/.config/video-factory/formal_api_demo.local.toml`
- `已确认` 当前 provider / 模型开关仍成立：
  - `provider.name = aliyun_bailian`
  - `image_generation.enabled = true`
  - `image_generation.model = wan2.6-image`
  - `video_generation.enabled = true`
  - `video_generation.model = wan2.7-i2v`
  - `portrait_detect.enabled = true`
  - `portrait_detect.model = liveportrait-detect`
  - `portrait_video_generation.enabled = true`
  - `portrait_video_generation.model = liveportrait`
- `已确认` 相关真实代码入口仍成立：
  - `_execute_aliyun_wan_image_generation(...)`
  - `_execute_aliyun_liveportrait_detect(...)`
  - `_execute_aliyun_liveportrait_video_generation(...)`
- `已确认` 本轮新建独立执行脚本：
  - `scripts/元素娃娃线_round2_资产与detect闸门验证.py`
- `已确认` 本轮真实调用结果显示：
  - provider 配置不是纸面存在
  - 真实阻塞点出现在 `wan2.6-image` create task 前
- `已确认` 真实报错为：
  - `AllocationQuota.FreeTierOnly`
  - 含义是当前阿里侧免费额度 / 计费模式把 `wan2.6-image` 挡住了
- `已确认` 这不是：
  - 本地配置缺失
  - `portrait_detect` 未接
  - `liveportrait` 未接
  - 新脚本 prompt 参数未生效

## asset_candidate_summary

- `已确认` 本轮独立目录已建立：
  - `dist/20260417_豆包的正确打开方式_vnext/host_motion_asset_gate_round2/`
- `已确认` 目录结构已建立：
  - `assets/`
  - `detect_probe/`
  - `liveportrait_probe/`
  - `audit/`
- `已确认` 本轮计划中的 2 套新资产候选为：
  - `候选A_正脸主持娃娃`
  - `候选B_软体素主持娃娃`
- `已确认` 两套候选都已写入明确 prompt 与设计目标，但都未能真正落出图片资产。
- `已确认` 失败原因一致：
  - `wan2.6-image` 真实调用返回 `HTTP403`
  - 错误码指向 `AllocationQuota.FreeTierOnly`
- `已确认` 因此本轮“新建 1 到 2 套视频级主持娃娃资产候选”这一项未完成。
- `已确认` 审计文件已生成：
  - `dist/20260417_豆包的正确打开方式_vnext/host_motion_asset_gate_round2/audit/asset_gate_summary.json`
  - `dist/20260417_豆包的正确打开方式_vnext/host_motion_asset_gate_round2/audit/最小闸门审计_round2.md`

## detect_gate_result

- `已确认` 本轮没有进入 `liveportrait-detect`。
- `已确认` 原因不是 detect 本身报错，而是 detect 前置所需的新资产没有生成出来。
- `已确认` 因此当前对“detect 能不能过”的回答只能写成：
  - `待验证`
- `已确认` 但本轮已新增一个更上游的真实 blocker：
  - `image_generation` 当前不可用

## liveportrait_min_run_result

- `已确认` 本轮没有进入最小 `liveportrait` 闭环。
- `已确认` 原因：
  - 没有成功落出的新资产候选
  - 根据当前轮次 stop line，不应在无新资产前提下继续拿旧体素壳硬跑
- `已确认` 因此当前对“是否摆脱图片动起来 / gif 感”的回答只能写成：
  - `待验证`

## technical_validation

- `已确认` `blocked`
- `已确认` blocked 点不在 `liveportrait`，而在本轮 asset gate 的最前置一步：
  - `wan2.6-image` 不可用

## content_validation

- `已确认` `blocked`
- `已确认` 原因：
  - 本轮没有新资产
  - 没有 detect
  - 没有 `liveportrait`
  - 因而不存在可供内容回审的新 C 线结果

## recommended_next_route

- `已确认` 当前不要继续做 `round2` 样片。
- `已确认` 当前最优先不是调动作，不是调口型，而是先恢复“视频级主持娃娃资产创建能力”。
- `已确认` 下一步优先级应写成：
  1. 先解决 `wan2.6-image` 的真实可用性
  2. 或补一个当前仓库已接、可稳定产出 detect 友好主持娃娃正脸资产的替代图片路线
  3. 新资产真实落出后，再重跑本轮 `detect -> liveportrait` 最小闭环

## git_commit_and_push_status

- `待验证` 本日志落盘时尚未提交 / 推送。

## reading_branch_sync_status

- `待验证` 本日志落盘时尚未同步回 `codex/user-readable-map`。
