# Latest

## 当前主结论

- `已确认` 当前轮正式对象仍是：
  - `《豆包的正确打开方式》vNext`
  - 输出目录：`dist/20260417_豆包的正确打开方式_vnext/`
- `已确认` 本轮已按“并行三线”收口：
  - A 线：证据线
  - B 线：声音线
  - C 线：动态主持壳线
- `已确认` 当前轮 `technical_validation`：
  - `passed`
- `已确认` 当前轮 `content_validation`：
  - `blocked`
- `已确认` 当前轮不要进入最终样片组装。

## 三线结果

1. `lane_A_evidence`
   - `部分成立`
   - 正面 / XML / PPT 证据位已收窄到静音可理解窗口
   - 反面仍缺用户点名原句级证据
2. `lane_B_voice`
   - `部分成立`
   - 阿里主路线 `qwen3-tts-instruct-flash-realtime + Serena/Cherry` 已落出 3 组候选
   - 阿里内部 fallback 已排尽并记录失败原因
   - 当前仍缺人工听审定版
3. `lane_C_host_motion`
   - `blocked`
   - 当前共享壳仍是假动态
   - `liveportrait` 对当前体素壳最小实测返回 `No human face detected.`

## 当前 blocker

1. `部分成立` 反面仍缺用户点名原句级证据
2. `部分成立` 阿里主路线已建立，但 3 组候选仍缺人工听审定版
3. `已确认` 当前体素娃娃主持壳没有可直接复用的真动态路线

## 本轮产出

1. `dist/20260417_豆包的正确打开方式_vnext/evidence_map.json`
2. `dist/20260417_豆包的正确打开方式_vnext/evidence_notes.md`
3. `dist/20260417_豆包的正确打开方式_vnext/voice_route_report.json`
4. `dist/20260417_豆包的正确打开方式_vnext/voice_listen_sheet.md`
5. `dist/20260417_豆包的正确打开方式_vnext/voice_candidates/*`
6. `dist/20260417_豆包的正确打开方式_vnext/host_motion_audit.md`
7. `dist/20260417_豆包的正确打开方式_vnext/host_motion_min_spec.md`
8. `dist/20260417_豆包的正确打开方式_vnext/host_motion_prototype/liveportrait_probe_result.json`
9. `codex_log/20260417_豆包vnext并行三线执行.md`

## 下一轮唯一建议

- `已确认` 先补反面证据并对 3 组阿里候选做人审定版，不进入最终样片组装
- `已确认` 动态主持壳转成独立能力线

## 当前默认接手建议先读

1. `AGENTS.md`
2. `codex_source/00_codex_readme.md`
3. `codex_log/latest.md`
4. `codex_log/20260417_豆包vnext并行三线执行.md`
5. `dist/20260417_豆包的正确打开方式_vnext/evidence_map.json`
6. `dist/20260417_豆包的正确打开方式_vnext/voice_route_report.json`
7. `dist/20260417_豆包的正确打开方式_vnext/voice_listen_sheet.md`
8. `dist/20260417_豆包的正确打开方式_vnext/host_motion_audit.md`
9. `dist/20260417_豆包的正确打开方式_vnext/result_summary.json`
