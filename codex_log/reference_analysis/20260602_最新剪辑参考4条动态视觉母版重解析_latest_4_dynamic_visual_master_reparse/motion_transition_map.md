# Motion Transition Map

## confirmed_motion_language

- 主转场是 `hard_cut`，不是花哨转场。参考感来自切换对象和注意力路径，不是动效复杂度。
- 高频动态包括：主持人手势、标题弹出、证据窗口硬切、手机内容替换、黄线位置变化、PIP 出现/退场。
- 密集证据段必须插入 `host_reset`、`title_reset` 或 `low_density_bridge`，否则会变成小字堆叠。

## one_second_dynamic_clips

每条参考已抽 8 个 1 秒证据 clips，覆盖 opening、large change、highlight/evidence/bridge/density/late section：

- `dist/reference_analysis/20260602_最新剪辑参考4条动态视觉母版重解析_latest_4_dynamic_visual_master_reparse/reference_01/dynamic_1s_clips/`
- `dist/reference_analysis/20260602_最新剪辑参考4条动态视觉母版重解析_latest_4_dynamic_visual_master_reparse/reference_02/dynamic_1s_clips/`
- `dist/reference_analysis/20260602_最新剪辑参考4条动态视觉母版重解析_latest_4_dynamic_visual_master_reparse/reference_03/dynamic_1s_clips/`
- `dist/reference_analysis/20260602_最新剪辑参考4条动态视觉母版重解析_latest_4_dynamic_visual_master_reparse/reference_04/dynamic_1s_clips/`

## motion rules

1. `host_to_evidence_cut`: 主持人提出判断后 1-3 秒内切入证据窗口。
2. `evidence_window_replace`: 同类证据窗口可以硬切替换，保持位置稳定，降低学习成本。
3. `highlight_move`: 长文本只移动高亮或换高亮行，不让整页乱跳。
4. `density_reset`: 高密证据段结束必须回到主持人/标题/低字数卡。
5. `split_only_if_relation`: 分屏只在 before/after、source/output、reference/result、步骤对照成立时出现。
