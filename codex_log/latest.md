# Latest

## 当前主结论

- `已确认` 2026-04-08 刚完成的 50 秒样片只能作为“真实素材注入 + 北京区 OSS + 云剪 cloud-only 技术链路可行”证据，不能作为内容达标样片。
- `已确认` 用户本轮明确判定：
  - 内容上完全不合格
  - 主要问题 1：没有真正的可见真人出镜
  - 主要问题 2：结尾总结卡不是用户要的“步骤 + 易错点”表达
  - 不接受继续沿这条质量口径往下走
- `已确认` 本轮已补最小 guardrail：
  - `carrier=human` 的本地素材必须在 `formal_api_demo.local.toml` 里显式标记 `verified_role="human_on_camera"`
  - `verified_role="screen_recording"` 不得静默占用 `hook_human / close_human`
  - 当前本机配置会被 generation gate 阻断，而不是继续生成新样片

## 根因摘要

- `素材层主因`
  - `素材录制/1.mov`、`2.mov`、`3.mov` 都是屏幕录制 / ChatGPT 工作流画面，不是明显可见真人半身口播。
- `case / 文案层放大器`
  - `cases/ai_report_rewrite_trap_50s.md` 明确写了 `1.mov` 与 `3.mov` 可作为 `hook / close` 的“最低可执行占位”，导致技术执行优先于内容质量。
  - 第 3 段写的是“核心判断收束”，配音文案也是判断句，因此结果卡自然生成成“判断式结果卡”，不是“步骤 + 易错点列表”。
- `配置层放大器`
  - 本机正式配置此前把 `hook_human` / `close_human` 指向屏幕录制，并写成 `source_type="user_screen_recording"`，但没有更硬的角色校验字段。
- `代码 guardrail 层放大器`
  - 旧逻辑只检查本地路径是否存在，不检查 `carrier=human` 是否真的由可见真人素材承担。
- `样片验收层表面现象`
  - 云端链路成功、50 秒时长正确，但这只能说明技术可行，不能说明内容达标。

## 本轮实际 guardrail

- 已更新：
  - `formal_api_demo_core.py`
  - `config/formal_api_demo.example.toml`
  - `tests/test_formal_api_demo_pipeline.py`
- 已更新本机配置：
  - `~/.config/video-factory/formal_api_demo.local.toml`
- 当前本机配置的素材角色：
  - `hook_human` → `verified_role="screen_recording"`
  - `process_self_footage` → `verified_role="screen_recording"`
  - `result_card` → `verified_role="ppt_image"`
  - `close_human` → `verified_role="screen_recording"`
- 当前验证命令：
  - `python3 scripts/generate_formal_api_demo.py --input cases/ai_report_rewrite_trap_50s.md --out dist/_guardrail_probe_20260408`
- 当前验证结果：
  - `overall_status = blocked`
  - blocked reason 包含：
    - `footage_input_hook_human_verified_role_human_on_camera`
    - `footage_input_close_human_verified_role_human_on_camera`
- `已确认` 当前相关测试：
  - `python3 -m unittest tests.test_formal_api_demo_pipeline tests.test_formal_hybrid_master`
  - `46` tests passed

## 下一轮改“步骤 + 易错点总结卡”的最小落点

- 最小必须改：
  - `cases/ai_report_rewrite_trap_50s.md`
    - 第 3 段 `段目标 / 配音文案 / 字幕文案 / 画面意图` 改为“步骤 + 易错点列表”
  - result_card 生成模板 / 生成脚本
    - 当前结果卡是一次性本地 PNG，不是仓库模板；下一轮若要可复用，必须把模板落到脚本或 case 派生逻辑里
  - `~/.config/video-factory/formal_api_demo.local.toml`
    - `result_card` 指向新的步骤型结果卡图片
- 不建议只改图片：
  - 因为当前 case 第 3 段文案本身就是判断句，只改图会造成旁白与画面断连。

## 当前接手建议先读

1. `AGENTS.md`
2. `codex_source/00_codex_readme.md`
3. `codex_log/latest.md`
4. `codex_log/20260408_ai_report_rewrite_trap_50s_root_cause_guardrail.md`
5. `cases/ai_report_rewrite_trap_50s.md`
6. `formal_api_demo_core.py`
7. `config/formal_api_demo.example.toml`
8. `tests/test_formal_api_demo_pipeline.py`
9. 若继续跑本机样片，再检查 `~/.config/video-factory/formal_api_demo.local.toml`

## 当前工作分支与状态

- 当前工作分支：
  - `codex/provider-auto-rotation`
- 当前状态标签：
  - `task_branch_only`
- 当前必须继续明确：
  - 本轮结果尚未同步回 `codex/user-readable-map`
  - 仓库正式状态仍未更新到主读取分支
  - `dist/*` 样片产物和本地配置均为 `local_only`
