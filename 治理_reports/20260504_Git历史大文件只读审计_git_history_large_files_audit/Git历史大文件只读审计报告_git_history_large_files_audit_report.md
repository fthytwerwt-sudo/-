# Git历史大文件只读审计报告 git_history_large_files_audit_report

## 1. 本轮结论

- 当前工作分支：`codex/git-history-large-files-audit-20260504`
- 主读取分支：`codex/user-readable-map`
- 是否只读审计：`已确认` 是；只读取 `.git` 与 Git 索引 / 对象信息。
- 是否删除文件：`已确认` 否。
- 是否移动 / 重命名文件：`已确认` 否。
- 是否执行 Git GC / prune / repack：`已确认` 否。
- 是否执行历史重写：`已确认` 否。
- 是否执行 Git LFS 迁移：`已确认` 否。
- `.git` 当前体积：`21G`
- `.git/objects` 体积：`21G`
- `.git/objects/pack` 体积：`19G`
- `.git/lfs` 体积，如存在：不存在。

基础体积原始记录：

```text
21G	.git
 21G	.git/objects
 19G	.git/objects/pack
720K	.git/logs
256K	.git/refs
MISSING	.git/lfs
```

关键结论：`.git` 约 `21G` 的最大直接来源不是当前 reachable 历史 blob，而是 Git 报告的 `garbage` / `tmp_pack_*` 临时包文件，合计约 `15.5GiB`。reachable pack 仍包含旧视频 / 旧音频 / 旧图片历史对象，但它们不是本地 `.git` 21G 的最大部分。

## 2. Git 对象总体状态

```text
count: 3514
size: 1.41 GiB
in-pack: 5072
packs: 4
size-pack: 3.99 GiB
prune-packable: 256
garbage: 67
size-garbage: 15.51 GiB
```

`git count-objects -vH` 同时报告了大量 `garbage found` 警告，前几条如下：

```text
warning: garbage found: .git/objects/pack/tmp_pack_59UZeh
warning: garbage found: .git/objects/pack/tmp_pack_IpoaFs
warning: garbage found: .git/objects/pack/tmp_pack_8ybWOH
warning: garbage found: .git/objects/pack/tmp_pack_9C9Tix
warning: garbage found: .git/objects/pack/tmp_pack_L6z8Zr
warning: garbage found: .git/objects/pack/tmp_pack_8jRJmp
warning: garbage found: .git/objects/pack/tmp_pack_XPC4U7
warning: garbage found: .git/objects/pack/tmp_pack_JF2Ytc
warning: garbage found: .git/objects/pack/tmp_pack_7W91vG
warning: garbage found: .git/objects/pack/tmp_pack_NBeRxt
warning: garbage found: .git/objects/pack/tmp_pack_DBGxjw
warning: garbage found: .git/objects/pack/tmp_pack_y67vGC
...
```

字段解释：

- `count`: loose objects（松散对象）数量，本次为 `3514`。
- `size`: loose objects 体积，本次为 `1.41 GiB`。
- `in-pack`: pack 内对象数量，本次为 `5072`。
- `packs`: pack 文件数量，本次为 `4` 个正式 pack。
- `size-pack`: 正式 pack 体积，本次为 `3.99 GiB`。
- `prune-packable`: 已可被 pack 覆盖的 loose object 数量，本次为 `256`。
- `garbage`: Git 识别到的垃圾对象 / 临时包数量，本次为 `67`。
- `size-garbage`: Git 识别到的 garbage 体积，本次为 `15.51 GiB`，这是本地 `.git` 过大的主因。

`.git/objects/pack/` 文件体积：

```text
1.1K	.git/objects/pack/pack-56320aa246892eba448b0a29a23cccceeadd89b3.idx
1.7G	.git/objects/pack/pack-56320aa246892eba448b0a29a23cccceeadd89b3.pack
140K	.git/objects/pack/pack-6a737e1cd52b94b3ff4fd8ca554e67f18d1f04b4.idx
918M	.git/objects/pack/pack-6a737e1cd52b94b3ff4fd8ca554e67f18d1f04b4.pack
20K	.git/objects/pack/pack-6a737e1cd52b94b3ff4fd8ca554e67f18d1f04b4.rev
1.1K	.git/objects/pack/pack-92ab6b920347cb9763fd1012cc90be88097d577b.idx
742M	.git/objects/pack/pack-92ab6b920347cb9763fd1012cc90be88097d577b.pack
1.1K	.git/objects/pack/pack-fcfb2321e0e3489a4a8e656247cd97ce0efe7766.idx
686M	.git/objects/pack/pack-fcfb2321e0e3489a4a8e656247cd97ce0efe7766.pack
189M	.git/objects/pack/tmp_pack_482PcQ
1.0G	.git/objects/pack/tmp_pack_59UZeh
1.1G	.git/objects/pack/tmp_pack_716rWP
560M	.git/objects/pack/tmp_pack_7W91vG
249M	.git/objects/pack/tmp_pack_7csZUV
1.3G	.git/objects/pack/tmp_pack_7d0Wb4
161M	.git/objects/pack/tmp_pack_8jRJmp
257M	.git/objects/pack/tmp_pack_8ybWOH
1.7G	.git/objects/pack/tmp_pack_9C9Tix
118M	.git/objects/pack/tmp_pack_ClH0wR
174M	.git/objects/pack/tmp_pack_D5CALr
597M	.git/objects/pack/tmp_pack_DBGxjw
1.3G	.git/objects/pack/tmp_pack_GE3S52
558M	.git/objects/pack/tmp_pack_GgxYRb
810M	.git/objects/pack/tmp_pack_IhJzEG
54M	.git/objects/pack/tmp_pack_IpoaFs
440M	.git/objects/pack/tmp_pack_JF2Ytc
532M	.git/objects/pack/tmp_pack_L6z8Zr
251M	.git/objects/pack/tmp_pack_NBeRxt
115M	.git/objects/pack/tmp_pack_RYIbhz
1.5G	.git/objects/pack/tmp_pack_T1Oamc
347M	.git/objects/pack/tmp_pack_VM7dV9
319M	.git/objects/pack/tmp_pack_XPC4U7
1.4G	.git/objects/pack/tmp_pack_kOFATu
204M	.git/objects/pack/tmp_pack_ntxNku
30M	.git/objects/pack/tmp_pack_xUsp6L
154M	.git/objects/pack/tmp_pack_y67vGC
265M	.git/objects/pack/tmp_pack_yTbbp3
```

`tmp_pack_*` 临时包合计：`15.5 GiB`，数量：`28`。

| 排名 | 大小 | 文件 |
| --- | ---: | --- |
| 1 | `1.7 GiB` | `.git/objects/pack/tmp_pack_9C9Tix` |
| 2 | `1.5 GiB` | `.git/objects/pack/tmp_pack_T1Oamc` |
| 3 | `1.4 GiB` | `.git/objects/pack/tmp_pack_kOFATu` |
| 4 | `1.3 GiB` | `.git/objects/pack/tmp_pack_GE3S52` |
| 5 | `1.3 GiB` | `.git/objects/pack/tmp_pack_7d0Wb4` |
| 6 | `1.1 GiB` | `.git/objects/pack/tmp_pack_716rWP` |
| 7 | `1.0 GiB` | `.git/objects/pack/tmp_pack_59UZeh` |
| 8 | `810.3 MiB` | `.git/objects/pack/tmp_pack_IhJzEG` |
| 9 | `597.3 MiB` | `.git/objects/pack/tmp_pack_DBGxjw` |
| 10 | `560.1 MiB` | `.git/objects/pack/tmp_pack_7W91vG` |
| 11 | `558.4 MiB` | `.git/objects/pack/tmp_pack_GgxYRb` |
| 12 | `532.0 MiB` | `.git/objects/pack/tmp_pack_L6z8Zr` |
| 13 | `440.1 MiB` | `.git/objects/pack/tmp_pack_JF2Ytc` |
| 14 | `347.3 MiB` | `.git/objects/pack/tmp_pack_VM7dV9` |
| 15 | `319.4 MiB` | `.git/objects/pack/tmp_pack_XPC4U7` |
| 16 | `264.5 MiB` | `.git/objects/pack/tmp_pack_yTbbp3` |
| 17 | `257.1 MiB` | `.git/objects/pack/tmp_pack_8ybWOH` |
| 18 | `250.9 MiB` | `.git/objects/pack/tmp_pack_NBeRxt` |
| 19 | `248.6 MiB` | `.git/objects/pack/tmp_pack_7csZUV` |
| 20 | `204.4 MiB` | `.git/objects/pack/tmp_pack_ntxNku` |
| 21 | `189.1 MiB` | `.git/objects/pack/tmp_pack_482PcQ` |
| 22 | `173.9 MiB` | `.git/objects/pack/tmp_pack_D5CALr` |
| 23 | `161.0 MiB` | `.git/objects/pack/tmp_pack_8jRJmp` |
| 24 | `154.3 MiB` | `.git/objects/pack/tmp_pack_y67vGC` |
| 25 | `118.4 MiB` | `.git/objects/pack/tmp_pack_ClH0wR` |
| 26 | `115.1 MiB` | `.git/objects/pack/tmp_pack_RYIbhz` |
| 27 | `53.9 MiB` | `.git/objects/pack/tmp_pack_IpoaFs` |
| 28 | `30.4 MiB` | `.git/objects/pack/tmp_pack_xUsp6L` |

## 3. 历史最大 blob TOP 100

| 排名 | 大小 | blob SHA | 路径 | 文件类型 | 当前工作树是否仍存在 | 判断 |
| --- | ---: | --- | --- | --- | --- | --- |
| 1 | `43.5 MiB` | `b6ee62bc619a` | `node_modules/ffmpeg-static/ffmpeg` | other | 否 | 仅历史对象 |
| 2 | `37.1 MiB` | `68fa9be24dec` | `dist/20260417_豆包的正确打开方式_vnext/host_full_video_formal_prompt_product_round12d_final_fix/renders/主持壳正式正片_round12d_final_fix.mp4` | video | 否 | 仅历史对象 |
| 3 | `35.9 MiB` | `ae8856abf2f7` | `dist/20260417_豆包的正确打开方式_vnext/host_full_video_formal_prompt_product_round14_latest_fix/renders/主持壳正式正片_round14_latest_fix.mp4` | video | 否 | 仅历史对象 |
| 4 | `31.3 MiB` | `eed28ee71de6` | `dist/20260417_豆包的正确打开方式_vnext/host_full_video_formal_prompt_product_round12/renders/主持壳正式正片_round12.mp4` | video | 否 | 仅历史对象 |
| 5 | `29.0 MiB` | `ac3c250b540b` | `dist/20260417_豆包的正确打开方式_vnext/round19_round16_baseline_direct_fix/audit/seg01_round16_vs_round19_compare.mp4` | video | 否 | 仅历史对象 |
| 6 | `27.7 MiB` | `2fa64bf9cc33` | `dist/20260417_豆包的正确打开方式_vnext/round15_seg05_replaced/renders/主持壳正式正片_round15_seg05_replaced.mp4` | video | 否 | 仅历史对象 |
| 7 | `27.3 MiB` | `131ca90a1e1c` | `dist/20260417_豆包的正确打开方式_vnext/round16_seg05_continuity_light_fix/renders/主持壳正式正片_round16_seg05_continuity_light_fix.mp4` | video | 否 | 仅历史对象 |
| 8 | `21.6 MiB` | `d2507b965a5f` | `dist/20260414_豆包高效用法_cartoon_ip_formal/local_review/final_review_clean.mp4` | video | 是 | 当前仍存在 |
| 9 | `21.6 MiB` | `5a6c58220274` | `dist/20260417_豆包的正确打开方式_vnext/round19_round16_baseline_direct_fix/renders/主持壳正式正片_round19_round16_baseline_direct_fix.mp4` | video | 否 | 仅历史对象 |
| 10 | `18.0 MiB` | `bf5f468184b8` | `dist/20260417_豆包的正确打开方式_vnext/host_full_video_minimal_closure_round11b/renders/主持壳整片最小闭环_round11b.mp4` | video | 否 | 仅历史对象 |
| 11 | `17.5 MiB` | `c2e9faaf1da4` | `dist/20260417_豆包的正确打开方式_vnext/host_full_video_minimal_closure_round11/renders/主持壳整片最小闭环_round11.mp4` | video | 否 | 仅历史对象 |
| 12 | `17.3 MiB` | `c4d004fb84a4` | `dist/20260417_豆包的正确打开方式_vnext/round17_seg01_replaced/audit/seg01_round16_reference.mp4` | video | 否 | 仅历史对象 |
| 13 | `17.3 MiB` | `ecdeda9047e7` | `dist/20260417_豆包的正确打开方式_vnext/host_full_video_minimal_closure_round11b/renders/主持壳整片最小闭环_round11b.mp4` | video | 否 | 仅历史对象 |
| 14 | `16.0 MiB` | `c374f7429e6f` | `复审包_review_packs/20260429_AI做PPT踩坑_技术预览_v1_ai_ppt_pitfall_preview_v1/AI做PPT踩坑_技术预览_v1_full.mp4` | video | 否 | 仅历史对象 |
| 15 | `14.2 MiB` | `785673d8ce4d` | `dist/20260417_豆包的正确打开方式_vnext/host_shell_ali_wan26_i2v_probe_round10/renders/主持壳阿里wan26_i2v_probe_round10_main.mp4` | video | 否 | 仅历史对象 |
| 16 | `12.5 MiB` | `a5a0bd3e41e3` | `dist/20260417_豆包的正确打开方式_vnext/round19_round16_baseline_direct_fix/audit/seg01_round19_new.mp4` | video | 否 | 仅历史对象 |
| 17 | `11.6 MiB` | `4a1af5abc96b` | `dist/20260417_豆包的正确打开方式_vnext/round15_seg05_replaced/audit/seg05_round14_old.mp4` | video | 否 | 仅历史对象 |
| 18 | `11.2 MiB` | `e6a5c6f03238` | `dist/20260417_豆包的正确打开方式_vnext/round20_主持壳补链收口_720p锁定/renders/主持壳正式正片_round20_主持壳补链收口_720p锁定.mp4` | video | 否 | 仅历史对象 |
| 19 | `10.7 MiB` | `7193d00e47f2` | `dist/20260417_豆包的正确打开方式_vnext/round21_主持壳提亮过渡平顺化_720p续锁/renders/主持壳正式正片_round21_主持壳提亮过渡平顺化_720p续锁.mp4` | video | 否 | 仅历史对象 |
| 20 | `10.3 MiB` | `3a967cb59380` | `dist/20260417_豆包的正确打开方式_vnext/round22_中段剪辑全面修复/renders/主持壳正式正片_round22_中段剪辑全面修复.mp4` | video | 否 | 仅历史对象 |
| 21 | `9.2 MiB` | `85041d37a31f` | `dist/20260417_豆包的正确打开方式_vnext/round23_主证据锁定修复/renders/主持壳正式正片_round23_主证据锁定修复.mp4` | video | 否 | 仅历史对象 |
| 22 | `9.0 MiB` | `dd179af430d6` | `dist/20260417_豆包的正确打开方式_vnext/round24_完整信息锚定修复/renders/主持壳正式正片_round24_完整信息锚定修复.mp4` | video | 否 | 仅历史对象 |
| 23 | `8.9 MiB` | `f8bae3017708` | `素材库_assets/元素娃娃开头锚点_opening_anchor_20260428/005_1496_seg01_no_text_inpaint_opening_anchor.mp4` | video | 是 | 当前仍存在 |
| 24 | `8.8 MiB` | `05ff4c6328d0` | `dist/20260417_豆包的正确打开方式_vnext/round25_镜头类型路由修复/renders/主持壳正式正片_round25_镜头类型路由修复.mp4` | video | 否 | 仅历史对象 |
| 25 | `8.8 MiB` | `4ef1d1020664` | `dist/20260417_豆包的正确打开方式_vnext/round26_验收纠偏/renders/主持壳正式正片_round26_验收纠偏.mp4` | video | 否 | 仅历史对象 |
| 26 | `8.7 MiB` | `465358b90a23` | `dist/20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix/AI做PPT踩坑_成品候选_v31_full.mp4` | video | 是 | 当前仍存在 |
| 27 | `8.5 MiB` | `fd91cb6a5bb3` | `复审包_review_packs/20260430_AI做PPT踩坑_成品标准候选_v2_ai_ppt_pitfall_finished_candidate_v2/AI做PPT踩坑_成品标准候选_v2_full.mp4` | video | 否 | 仅历史对象 |
| 28 | `8.5 MiB` | `8cf5733a5da2` | `dist/latest_review_pack/AI做PPT踩坑_成品候选_v3_full.mp4` | video | 是 | 当前仍存在 |
| 29 | `8.5 MiB` | `33140f02ebe5` | `dist/20260417_豆包的正确打开方式_vnext/round31_一镜到底录屏证据链重构/renders/主持壳正式正片_round31_一镜到底录屏证据链重构.mp4` | video | 否 | 仅历史对象 |
| 30 | `8.3 MiB` | `c21b10ddd1cf` | `dist/20260417_豆包的正确打开方式_vnext/round28_完整可读终修/renders/主持壳正式正片_round28_完整可读终修.mp4` | video | 否 | 仅历史对象 |
| 31 | `8.3 MiB` | `dc831c9b6f8f` | `dist/20260417_豆包的正确打开方式_vnext/round27_首拍完整信息块修复/renders/主持壳正式正片_round27_首拍完整信息块修复.mp4` | video | 否 | 仅历史对象 |
| 32 | `8.3 MiB` | `b6ceff8cf0f6` | `dist/20260417_豆包的正确打开方式_vnext/round29_中段图片页风格与正反差修复/renders/主持壳正式正片_round29_中段图片页风格与正反差修复.mp4` | video | 否 | 仅历史对象 |
| 33 | `8.2 MiB` | `7421339dcb4b` | `dist/20260417_豆包的正确打开方式_vnext/round30_中段图片卡贴合整片视觉风格修复/renders/主持壳正式正片_round30_中段图片卡贴合整片视觉风格修复.mp4` | video | 否 | 仅历史对象 |
| 34 | `7.4 MiB` | `37e378c7472e` | `dist/20260417_豆包的正确打开方式_vnext/round34_中段双展示提示卡_正反分段提示修复/renders/主持壳正式正片_round34_中段双展示提示卡_正反分段提示修复.mp4` | video | 是 | 当前仍存在 |
| 35 | `7.2 MiB` | `2be2404224d3` | `dist/20260417_豆包的正确打开方式_vnext/round33_正反展示提示卡补齐与风格统一/renders/主持壳正式正片_round33_正反展示提示卡补齐与风格统一.mp4` | video | 否 | 仅历史对象 |
| 36 | `6.9 MiB` | `e23f43d022b8` | `dist/20260417_豆包的正确打开方式_vnext/round32_全片边框残留与跳切连续性修复/renders/主持壳正式正片_round32_全片边框残留与跳切连续性修复.mp4` | video | 否 | 仅历史对象 |
| 37 | `6.7 MiB` | `699312b0b24f` | `素材检查_reports/20260429_文案样本节奏提取_copy_sample_rhythm_extract/intermediate/文案样本_audio_16k_mono.wav` | audio | 是 | 当前仍存在 |
| 38 | `6.4 MiB` | `4e4800c0dd34` | `dist/20260417_豆包的正确打开方式_vnext/round20_主持壳补链收口_720p锁定/audit/seg01_round19_old.mp4` | video | 否 | 仅历史对象 |
| 39 | `6.2 MiB` | `a2412d873b2d` | `dist/20260417_豆包的正确打开方式_vnext/round21_主持壳提亮过渡平顺化_720p续锁/renders/seg01_preview_round21_主持壳提亮过渡平顺化_720p续锁.mp4` | video | 否 | 仅历史对象 |
| 40 | `6.1 MiB` | `fad05014ebf4` | `dist/20260417_豆包的正确打开方式_vnext/host_full_video_formal_prompt_product_round12c_hotfix/renders/主持壳正式正片_round12c_hotfix.mp4` | video | 否 | 仅历史对象 |
| 41 | `5.7 MiB` | `199c4fdbac7e` | `治理_reports/20260502_单工作区审计_single_workspace_audit/audit_inventory.json` | json | 否 | 仅历史对象 |
| 42 | `5.7 MiB` | `db128db75195` | `dist/20260417_豆包的正确打开方式_vnext/round20_主持壳补链收口_720p锁定/audit/seg01_round20_new.mp4` | video | 否 | 仅历史对象 |
| 43 | `5.2 MiB` | `92cd5f3dbeea` | `dist/20260417_豆包的正确打开方式_vnext/round21_主持壳提亮过渡平顺化_720p续锁/audit/seg01_round21_new.mp4` | video | 否 | 仅历史对象 |
| 44 | `5.2 MiB` | `daa6ef8fba99` | `dist/20260417_豆包的正确打开方式_vnext/local_review/final_review.mp4` | video | 是 | 当前仍存在 |
| 45 | `5.1 MiB` | `8131e6bd996d` | `dist/20260414_豆包高效用法_cartoon_ip_formal/visual/seg01_video.mp4` | video | 是 | 当前仍存在 |
| 46 | `4.9 MiB` | `a5f27e1ee281` | `dist/20260417_豆包的正确打开方式_vnext/round15_seg05_replaced/audit/seg05_round15_new.mp4` | video | 否 | 仅历史对象 |
| 47 | `4.7 MiB` | `499d168953fd` | `dist/20260417_豆包的正确打开方式_vnext/local_review/final_review_clean.mp4` | video | 是 | 当前仍存在 |
| 48 | `4.6 MiB` | `074c7a789322` | `dist/20260417_豆包的正确打开方式_vnext/round16_seg05_continuity_light_fix/audit/seg05_round16_new.mp4` | video | 否 | 仅历史对象 |
| 49 | `4.2 MiB` | `db72b437c34e` | `dist/prototypes/20260428_方案B独立反应片段V3_scheme_b_standalone_reaction_v3/方案B独立反应页_骚萌A_static_reaction_page_raw_from_wan.png` | image | 否 | 仅历史对象 |
| 50 | `4.2 MiB` | `5c5e03de6589` | `dist/formal_api_demo_doubao_task_clear_20260412_repair_v1/local_review/final_review.mp4` | video | 否 | 仅历史对象 |
| 51 | `4.1 MiB` | `a998ffff395d` | `dist/20260417_豆包的正确打开方式_vnext/tts/voiceover_combined.wav` | audio | 是 | 当前仍存在 |
| 52 | `4.0 MiB` | `010a5e501a2e` | `dist/formal_api_demo_doubao_task_clear_20260412_repair_v1/local_review/final_review_clean.mp4` | video | 否 | 仅历史对象 |
| 53 | `3.9 MiB` | `4ec8644950cd` | `dist/20260417_豆包的正确打开方式_vnext/voice_ab_review_bundle_round3/00_三候选顺序连听.wav` | audio | 是 | 当前仍存在 |
| 54 | `3.8 MiB` | `1b30a1f7974e` | `dist/prototypes/20260428_方案B独立反应片段V3_scheme_b_standalone_reaction_v3/方案B独立反应页_骚萌B_static_reaction_page_raw_from_wan.png` | image | 否 | 仅历史对象 |
| 55 | `3.8 MiB` | `dfaeae2819ba` | `dist/20260417_豆包的正确打开方式_vnext/voice_ab_review_bundle_round4/00_三候选顺序连听.wav` | audio | 是 | 当前仍存在 |
| 56 | `3.8 MiB` | `2a5abecc0c5d` | `dist/20260417_豆包的正确打开方式_vnext/round18_aliyun_unblock_and_identity_fix/renders/slot02_turn_fix_c.mp4` | video | 否 | 仅历史对象 |
| 57 | `3.7 MiB` | `67ffd60f02a5` | `dist/20260417_豆包的正确打开方式_vnext/voice_ab_review_bundle/00_三候选顺序连听.wav` | audio | 是 | 当前仍存在 |
| 58 | `3.7 MiB` | `95f18a4cf2f7` | `dist/20260417_豆包的正确打开方式_vnext/voice_ab_review_bundle_round2/00_三候选顺序连听.wav` | audio | 是 | 当前仍存在 |
| 59 | `3.7 MiB` | `6cbc2ebc563f` | `治理_reports/20260502_单工作区清理归档_single_workspace_cleanup_archive/audit_raw_initial.json` | json | 是 | 当前仍存在 |
| 60 | `3.6 MiB` | `7ba090f10365` | `dist/formal_api_demo_doubao_task_clear_20260412_repair_v1/visual/seg02_doubao_evidence_repair.mp4` | video | 否 | 仅历史对象 |
| 61 | `3.4 MiB` | `3cab0001f0ef` | `dist/prototypes/20260428_方案B独立反应片段V3_scheme_b_standalone_reaction_v3/方案B独立反应页_static_reaction_page_raw_from_wan.png` | image | 否 | 仅历史对象 |
| 62 | `3.3 MiB` | `14a7bb5e24c8` | `dist/20260417_豆包的正确打开方式_vnext/host_full_video_formal_prompt_product_round12b_hotfix/renders/主持壳正式正片_round12b_hotfix.mp4` | video | 否 | 仅历史对象 |
| 63 | `3.1 MiB` | `abfab4a068f9` | `dist/20260417_豆包的正确打开方式_vnext/round16_seg05_continuity_light_fix/renders/slot05_continuity_b.mp4` | video | 否 | 仅历史对象 |
| 64 | `3.1 MiB` | `af53e7902559` | `dist/20260417_豆包的正确打开方式_vnext/round22_中段剪辑全面修复/audit/中段_before_after_round21_vs_round22.mp4` | video | 否 | 仅历史对象 |
| 65 | `3.0 MiB` | `301919cafdf1` | `dist/20260417_豆包的正确打开方式_vnext/host_motion_asset_gate_round5/assets/候选A_round5_软脸主持肖像_wan2.7-image-pro_raw.png` | image | 是 | 当前仍存在 |
| 66 | `3.0 MiB` | `9c7642465e13` | `dist/20260417_豆包的正确打开方式_vnext/host_motion_asset_gate_round4/assets/候选B_弱化方块切面主持娃娃_wan2.7-image-pro_raw.png` | image | 是 | 当前仍存在 |
| 67 | `3.0 MiB` | `fe8d0160495e` | `dist/20260417_豆包的正确打开方式_vnext/host_motion_asset_gate_round4/assets/候选A_大脸正脸主持娃娃_wan2.7-image-pro_raw.png` | image | 是 | 当前仍存在 |
| 68 | `2.9 MiB` | `6748ad391e0e` | `dist/20260417_豆包的正确打开方式_vnext/host_motion_asset_gate_round4/assets/候选D_卡通数字人肖像版_wan2.7-image-pro_raw.png` | image | 是 | 当前仍存在 |
| 69 | `2.9 MiB` | `9384dd360bc1` | `dist/20260417_豆包的正确打开方式_vnext/host_shell_exact_reference_alignment_round9d/assets/主持壳静帧设定_round9d.png` | image | 否 | 仅历史对象 |
| 70 | `2.9 MiB` | `6b064c2b9b37` | `dist/20260417_豆包的正确打开方式_vnext/round20_主持壳补链收口_720p锁定/renders/slot03_yield_fix_a.mp4` | video | 否 | 仅历史对象 |
| 71 | `2.9 MiB` | `d70692cea454` | `dist/20260417_豆包的正确打开方式_vnext/host_motion_asset_gate_round4/assets/候选C_半体素软面部主持娃娃_wan2.7-image-pro_raw.png` | image | 是 | 当前仍存在 |
| 72 | `2.8 MiB` | `fa40272305b8` | `dist/prototypes/20260428_方案B独立反应片段V3_scheme_b_standalone_reaction_v3/方案B独立反应片段_骚萌_reaction_clip_raw_from_wan.mp4` | video | 否 | 仅历史对象 |
| 73 | `2.8 MiB` | `1bcba2e3748a` | `dist/20260417_豆包的正确打开方式_vnext/host_motion_asset_gate_round3/assets/候选B_软体素主持娃娃_v2_wan2.7-image-pro_raw.png` | image | 是 | 当前仍存在 |
| 74 | `2.7 MiB` | `0b104be316b9` | `dist/20260417_豆包的正确打开方式_vnext/round21_主持壳提亮过渡平顺化_720p续锁/renders/seg05_preview_round21_主持壳提亮过渡平顺化_720p续锁.mp4` | video | 否 | 仅历史对象 |
| 75 | `2.7 MiB` | `dd01c121a2c9` | `dist/20260417_豆包的正确打开方式_vnext/round15_alibaba_route_switch_probe/renders/node03_closure_exit_收束_给出口_wan2_6_r2v.mp4` | video | 否 | 仅历史对象 |
| 76 | `2.6 MiB` | `f9a443a40a71` | `dist/20260417_豆包的正确打开方式_vnext/round17_seg01_replaced/renders/slot01_pain_fix_a.mp4` | video | 否 | 仅历史对象 |
| 77 | `2.5 MiB` | `cdbfe07184fb` | `复审包_review_packs/20260430_骚萌卡历史样本复审_sassy_card_reference_review/PR7_骚萌15秒预览.mp4` | video | 是 | 当前仍存在 |
| 78 | `2.5 MiB` | `17b5f0bbe8fd` | `dist/20260417_豆包的正确打开方式_vnext/round20_主持壳补链收口_720p锁定/audit/seg05_round19_old.mp4` | video | 否 | 仅历史对象 |
| 79 | `2.4 MiB` | `4cb7bcdf707a` | `dist/20260417_豆包的正确打开方式_vnext/round15_alibaba_route_switch_probe/renders/node02_judgment_breakthrough_判断_点破_wan2_6_r2v.mp4` | video | 否 | 仅历史对象 |
| 80 | `2.4 MiB` | `ace9359afca3` | `dist/20260417_豆包的正确打开方式_vnext/round21_主持壳提亮过渡平顺化_720p续锁/audit/seg05_round21_new.mp4` | video | 否 | 仅历史对象 |
| 81 | `2.3 MiB` | `d34ceba809b9` | `复审包_review_packs/20260429_AI做PPT踩坑_技术预览_v1_ai_ppt_pitfall_preview_v1/shot00_opening_hello_wave_preview.mp4` | video | 否 | 仅历史对象 |
| 82 | `2.3 MiB` | `097672aff025` | `dist/20260417_豆包的正确打开方式_vnext/reference/round9d_exact_reference.png` | image | 否 | 仅历史对象 |
| 83 | `2.2 MiB` | `9a753beca44d` | `dist/20260417_豆包的正确打开方式_vnext/round20_主持壳补链收口_720p锁定/audit/seg05_round20_new.mp4` | video | 否 | 仅历史对象 |
| 84 | `2.2 MiB` | `a119b42a5c45` | `dist/20260417_豆包的正确打开方式_vnext/round23_主证据锁定修复/audit/中段_before_after_round22_vs_round23.mp4` | video | 否 | 仅历史对象 |
| 85 | `2.1 MiB` | `513858155377` | `dist/20260417_豆包的正确打开方式_vnext/round15_alibaba_route_switch_probe/renders/node01_pain_stuck_痛点_卡住_wan2_6_r2v.mp4` | video | 否 | 仅历史对象 |
| 86 | `2.1 MiB` | `9cd00973c956` | `dist/20260417_豆包的正确打开方式_vnext/host_motion_asset_gate_round3/assets/候选A_正脸主持娃娃_v2_wan2.7-image-pro_raw.png` | image | 是 | 当前仍存在 |
| 87 | `2.0 MiB` | `48b8e8f0d45c` | `复审包_review_packs/20260430_骚萌卡历史样本复审_sassy_card_reference_review/PR15_v2_sassy_cards/positive_reversal_sassy_card.png` | image | 是 | 当前仍存在 |
| 88 | `2.0 MiB` | `67db4b222405` | `复审包_review_packs/20260430_骚萌卡历史样本复审_sassy_card_reference_review/PR15_v2_sassy_cards/negative_reversal_sassy_card.png` | image | 是 | 当前仍存在 |
| 89 | `2.0 MiB` | `86761b75cb63` | `复审包_review_packs/20260430_骚萌卡历史样本复审_sassy_card_reference_review/PR15_v2_sassy_cards/problem_hook_sassy_card.png` | image | 是 | 当前仍存在 |
| 90 | `2.0 MiB` | `939e83989143` | `dist/20260417_豆包的正确打开方式_vnext/round18_aliyun_unblock_and_identity_fix/renders/slot02_turn_fix_d.mp4` | video | 否 | 仅历史对象 |
| 91 | `2.0 MiB` | `85df8214f1b4` | `dist/20260414_豆包高效用法_cartoon_ip_formal/素材切片_clips/seg02_豆包动作位_scene12_vfill.mp4` | video | 是 | 当前仍存在 |
| 92 | `2.0 MiB` | `9c01d21c6785` | `dist/20260417_豆包的正确打开方式_vnext/round20_主持壳补链收口_720p锁定/renders/slot05_closure_fix_a.mp4` | video | 否 | 仅历史对象 |
| 93 | `1.9 MiB` | `368049bc24a7` | `dist/20260417_豆包的正确打开方式_vnext/host_motion_asset_gate_round5/assets/候选A_round5_软脸主持肖像_wan2.7-image-pro_review_1080x1920.png` | image | 是 | 当前仍存在 |
| 94 | `1.9 MiB` | `1137ab535d95` | `dist/20260417_豆包的正确打开方式_vnext/round22_中段剪辑全面修复/audit/中段_before_round21.mp4` | video | 否 | 仅历史对象 |
| 95 | `1.9 MiB` | `fa66c8dfb721` | `dist/20260417_豆包的正确打开方式_vnext/host_motion_asset_gate_round4/assets/候选B_弱化方块切面主持娃娃_wan2.7-image-pro_review_1080x1920.png` | image | 是 | 当前仍存在 |
| 96 | `1.9 MiB` | `8770eb5c2377` | `dist/20260417_豆包的正确打开方式_vnext/host_motion_asset_gate_round4/assets/候选A_大脸正脸主持娃娃_wan2.7-image-pro_review_1080x1920.png` | image | 是 | 当前仍存在 |
| 97 | `1.8 MiB` | `05c99fe010ba` | `dist/20260417_豆包的正确打开方式_vnext/round31_一镜到底录屏证据链重构/audit/中段_before_after_round30_vs_round31.mp4` | video | 否 | 仅历史对象 |
| 98 | `1.8 MiB` | `51a9c33af66b` | `dist/20260414_豆包高效用法_cartoon_ip_formal/素材切片_clips/seg03_豆包动作位_scene3_vfill.mp4` | video | 是 | 当前仍存在 |
| 99 | `1.8 MiB` | `03ce29b5bb0a` | `dist/20260417_豆包的正确打开方式_vnext/round23_主证据锁定修复/audit/中段_before_round22.mp4` | video | 否 | 仅历史对象 |
| 100 | `1.8 MiB` | `53e02952f2f2` | `dist/20260417_豆包的正确打开方式_vnext/round16_seg05_continuity_light_fix/renders/slot05_continuity_a.mp4` | video | 否 | 仅历史对象 |

## 4. 当前工作树最大跟踪文件 TOP 100

| 排名 | 大小 | 路径 | 文件类型 | 是否建议继续 Git 跟踪 | 原因 |
| --- | ---: | --- | --- | --- | --- |
| 1 | `21.6 MiB` | `dist/20260414_豆包高效用法_cartoon_ip_formal/local_review/final_review_clean.mp4` | video | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 2 | `8.7 MiB` | `复审包_review_packs/20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix/AI做PPT踩坑_成品候选_v31_full.mp4` | video | 谨慎保留 | 当前复审 / reference 证据，若瘦身应先迁 LFS 或保留最小证据 |
| 3 | `8.7 MiB` | `dist/latest_review_pack/full.mp4` | video | 谨慎保留 | 当前复审 / reference 证据，若瘦身应先迁 LFS 或保留最小证据 |
| 4 | `8.7 MiB` | `dist/latest_review_pack/AI做PPT踩坑_成品候选_v31_full.mp4` | video | 谨慎保留 | 当前复审 / reference 证据，若瘦身应先迁 LFS 或保留最小证据 |
| 5 | `8.7 MiB` | `dist/20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix/AI做PPT踩坑_成品候选_v31_full.mp4` | video | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 6 | `8.5 MiB` | `dist/latest_review_pack/AI做PPT踩坑_成品候选_v3_full.mp4` | video | 谨慎保留 | 当前复审 / reference 证据，若瘦身应先迁 LFS 或保留最小证据 |
| 7 | `7.4 MiB` | `dist/20260417_豆包的正确打开方式_vnext/round34_中段双展示提示卡_正反分段提示修复/renders/主持壳正式正片_round34_中段双展示提示卡_正反分段提示修复.mp4` | video | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 8 | `5.2 MiB` | `dist/20260417_豆包的正确打开方式_vnext/local_review/final_review.mp4` | video | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 9 | `5.1 MiB` | `dist/20260414_豆包高效用法_cartoon_ip_formal/visual/seg05_video.mp4` | video | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 10 | `5.1 MiB` | `dist/20260414_豆包高效用法_cartoon_ip_formal/visual/seg01_video.mp4` | video | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 11 | `4.7 MiB` | `dist/20260417_豆包的正确打开方式_vnext/local_review/final_review_clean.mp4` | video | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 12 | `4.1 MiB` | `dist/20260417_豆包的正确打开方式_vnext/tts/voiceover_combined.wav` | audio | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 13 | `3.9 MiB` | `dist/20260417_豆包的正确打开方式_vnext/voice_ab_review_bundle_round3/00_三候选顺序连听.wav` | audio | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 14 | `3.8 MiB` | `dist/20260417_豆包的正确打开方式_vnext/voice_ab_review_bundle_round4/00_三候选顺序连听.wav` | audio | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 15 | `3.7 MiB` | `dist/20260417_豆包的正确打开方式_vnext/voice_ab_review_bundle_round2/00_三候选顺序连听.wav` | audio | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 16 | `3.7 MiB` | `dist/20260417_豆包的正确打开方式_vnext/voice_ab_review_bundle/00_三候选顺序连听.wav` | audio | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 17 | `3.7 MiB` | `治理_reports/20260502_单工作区清理归档_single_workspace_cleanup_archive/audit_raw_initial.json` | json | 否 / 可归档 | 大型审计 JSON，默认读取成本高 |
| 18 | `3.0 MiB` | `dist/20260417_豆包的正确打开方式_vnext/host_motion_asset_gate_round5/assets/候选A_round5_软脸主持肖像_wan2.7-image-pro_raw.png` | image | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 19 | `3.0 MiB` | `dist/20260417_豆包的正确打开方式_vnext/host_motion_asset_gate_round4/assets/候选B_弱化方块切面主持娃娃_wan2.7-image-pro_raw.png` | image | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 20 | `3.0 MiB` | `dist/20260417_豆包的正确打开方式_vnext/host_motion_asset_gate_round4/assets/候选A_大脸正脸主持娃娃_wan2.7-image-pro_raw.png` | image | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 21 | `2.9 MiB` | `dist/20260417_豆包的正确打开方式_vnext/host_motion_asset_gate_round4/assets/候选D_卡通数字人肖像版_wan2.7-image-pro_raw.png` | image | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 22 | `2.9 MiB` | `dist/20260417_豆包的正确打开方式_vnext/host_motion_asset_gate_round4/assets/候选C_半体素软面部主持娃娃_wan2.7-image-pro_raw.png` | image | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 23 | `2.8 MiB` | `dist/20260417_豆包的正确打开方式_vnext/host_motion_asset_gate_round3/assets/候选B_软体素主持娃娃_v2_wan2.7-image-pro_raw.png` | image | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 24 | `2.1 MiB` | `dist/20260417_豆包的正确打开方式_vnext/host_motion_asset_gate_round3/assets/候选A_正脸主持娃娃_v2_wan2.7-image-pro_raw.png` | image | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 25 | `2.0 MiB` | `dist/20260414_豆包高效用法_cartoon_ip_formal/素材切片_clips/seg02_豆包动作位_scene12_vfill.mp4` | video | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 26 | `1.9 MiB` | `dist/20260417_豆包的正确打开方式_vnext/host_motion_asset_gate_round5/assets/候选A_round5_软脸主持肖像_wan2.7-image-pro_review_1080x1920.png` | image | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 27 | `1.9 MiB` | `dist/20260417_豆包的正确打开方式_vnext/host_motion_asset_gate_round4/assets/候选B_弱化方块切面主持娃娃_wan2.7-image-pro_review_1080x1920.png` | image | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 28 | `1.9 MiB` | `dist/20260417_豆包的正确打开方式_vnext/host_motion_asset_gate_round4/assets/候选A_大脸正脸主持娃娃_wan2.7-image-pro_review_1080x1920.png` | image | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 29 | `1.8 MiB` | `dist/20260414_豆包高效用法_cartoon_ip_formal/素材切片_clips/seg03_豆包动作位_scene3_vfill.mp4` | video | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 30 | `1.8 MiB` | `dist/20260417_豆包的正确打开方式_vnext/host_motion_asset_gate_round4/assets/候选D_卡通数字人肖像版_wan2.7-image-pro_review_1080x1920.png` | image | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 31 | `1.8 MiB` | `dist/20260417_豆包的正确打开方式_vnext/host_motion_asset_gate_round4/assets/候选C_半体素软面部主持娃娃_wan2.7-image-pro_review_1080x1920.png` | image | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 32 | `1.8 MiB` | `dist/20260417_豆包的正确打开方式_vnext/segments/02_seg02_negative.mp4` | video | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 33 | `1.7 MiB` | `dist/20260417_豆包的正确打开方式_vnext/host_motion_asset_gate_round3/assets/候选B_软体素主持娃娃_v2_wan2.7-image-pro_review_1080x1920.png` | image | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 34 | `1.6 MiB` | `dist/20260417_豆包的正确打开方式_vnext/segments/03_seg03_positive_strategy.mp4` | video | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 35 | `1.5 MiB` | `dist/latest_review_pack/middle_preview.mp4` | video | 谨慎保留 | 当前复审 / reference 证据，若瘦身应先迁 LFS 或保留最小证据 |
| 36 | `1.5 MiB` | `dist/20260417_豆包的正确打开方式_vnext/round34_中段双展示提示卡_正反分段提示修复/renders/中段preview_round34_中段双展示提示卡_正反分段提示修复.mp4` | video | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 37 | `1.3 MiB` | `dist/20260417_豆包的正确打开方式_vnext/voice_candidates_round3/C1/C1_processed.wav` | audio | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 38 | `1.3 MiB` | `dist/20260417_豆包的正确打开方式_vnext/voice_ab_review_bundle_round3/02_备选_C1.wav` | audio | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 39 | `1.3 MiB` | `dist/20260417_豆包的正确打开方式_vnext/voice_candidates_round4/E2/E2_processed.wav` | audio | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 40 | `1.3 MiB` | `dist/20260417_豆包的正确打开方式_vnext/voice_ab_review_bundle_round4/02_备选_E2.wav` | audio | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 41 | `1.3 MiB` | `dist/20260417_豆包的正确打开方式_vnext/voice_candidates/A2_qwen3_serena_steady/A2_qwen3_serena_steady_processed.wav` | audio | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 42 | `1.3 MiB` | `dist/20260417_豆包的正确打开方式_vnext/voice_ab_review_bundle/02_备选_A2_qwen3_serena_steady.wav` | audio | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 43 | `1.3 MiB` | `dist/20260417_豆包的正确打开方式_vnext/voice_candidates_round3/C3/C3_processed.wav` | audio | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 44 | `1.3 MiB` | `dist/20260417_豆包的正确打开方式_vnext/voice_ab_review_bundle_round3/03_淘汰_C3.wav` | audio | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 45 | `1.3 MiB` | `复审包_review_packs/20260430_骚萌卡历史样本复审_sassy_card_reference_review/PR7_A_骚萌反应页.png` | image | 谨慎保留 | 当前复审 / reference 证据，若瘦身应先迁 LFS 或保留最小证据 |
| 46 | `1.3 MiB` | `dist/20260417_豆包的正确打开方式_vnext/voice_candidates_round2/B3/B3_processed.wav` | audio | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 47 | `1.3 MiB` | `dist/20260417_豆包的正确打开方式_vnext/voice_ab_review_bundle_round2/03_淘汰_B3.wav` | audio | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 48 | `1.3 MiB` | `dist/20260417_豆包的正确打开方式_vnext/voice_candidates_round4/E1/E1_processed.wav` | audio | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 49 | `1.3 MiB` | `dist/20260417_豆包的正确打开方式_vnext/voice_candidates_round2/B1/B1_processed.wav` | audio | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 50 | `1.3 MiB` | `dist/20260417_豆包的正确打开方式_vnext/voice_ab_review_bundle_round4/01_暂定第一名_E1.wav` | audio | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 51 | `1.3 MiB` | `dist/20260417_豆包的正确打开方式_vnext/voice_ab_review_bundle_round2/01_暂定第一名_B1.wav` | audio | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 52 | `1.3 MiB` | `复审包_review_packs/20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix/shot00_opening_hello_wave_preview.mp4` | video | 谨慎保留 | 当前复审 / reference 证据，若瘦身应先迁 LFS 或保留最小证据 |
| 53 | `1.3 MiB` | `dist/latest_review_pack/shot00_opening_hello_wave_preview.mp4` | video | 谨慎保留 | 当前复审 / reference 证据，若瘦身应先迁 LFS 或保留最小证据 |
| 54 | `1.3 MiB` | `dist/20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix/shot00_opening_hello_wave_preview.mp4` | video | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 55 | `1.3 MiB` | `dist/20260417_豆包的正确打开方式_vnext/voice_candidates_round3/C2/C2_processed.wav` | audio | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 56 | `1.3 MiB` | `dist/20260417_豆包的正确打开方式_vnext/voice_ab_review_bundle_round3/01_暂定第一名_C2.wav` | audio | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 57 | `1.2 MiB` | `dist/20260417_豆包的正确打开方式_vnext/voice_candidates/A1_qwen3_serena_light/A1_qwen3_serena_light_processed.wav` | audio | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 58 | `1.2 MiB` | `dist/20260417_豆包的正确打开方式_vnext/voice_ab_review_bundle/01_暂定第一名_A1_qwen3_serena_light.wav` | audio | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 59 | `1.2 MiB` | `dist/20260417_豆包的正确打开方式_vnext/voice_candidates_round2/B2/B2_processed.wav` | audio | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 60 | `1.2 MiB` | `dist/20260417_豆包的正确打开方式_vnext/voice_ab_review_bundle_round2/02_备选_B2.wav` | audio | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 61 | `1.2 MiB` | `dist/20260417_豆包的正确打开方式_vnext/voice_candidates/A3_qwen3_cherry_hint/A3_qwen3_cherry_hint_processed.wav` | audio | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 62 | `1.2 MiB` | `dist/20260417_豆包的正确打开方式_vnext/voice_ab_review_bundle/03_淘汰_A3_qwen3_cherry_hint.wav` | audio | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 63 | `1.2 MiB` | `dist/20260417_豆包的正确打开方式_vnext/voice_candidates_round4/E3/E3_processed.wav` | audio | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 64 | `1.2 MiB` | `dist/20260417_豆包的正确打开方式_vnext/voice_ab_review_bundle_round4/03_淘汰_E3.wav` | audio | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 65 | `1.1 MiB` | `dist/20260417_豆包的正确打开方式_vnext/host_motion_asset_gate_round3/assets/候选A_正脸主持娃娃_v2_wan2.7-image-pro_review_1080x1920.png` | image | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 66 | `1.1 MiB` | `复审包_review_packs/20260430_骚萌卡历史样本复审_sassy_card_reference_review/PR7_B_骚萌反应页.png` | image | 谨慎保留 | 当前复审 / reference 证据，若瘦身应先迁 LFS 或保留最小证据 |
| 67 | `1.1 MiB` | `复审包_review_packs/20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix/references/PR7_B_骚萌反应页.png` | image | 谨慎保留 | 当前复审 / reference 证据，若瘦身应先迁 LFS 或保留最小证据 |
| 68 | `1.1 MiB` | `dist/20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix/references/PR7_B_骚萌反应页.png` | image | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 69 | `1.1 MiB` | `dist/latest_review_pack/before_after.mp4` | video | 谨慎保留 | 当前复审 / reference 证据，若瘦身应先迁 LFS 或保留最小证据 |
| 70 | `1.1 MiB` | `dist/20260417_豆包的正确打开方式_vnext/round34_中段双展示提示卡_正反分段提示修复/audit/round33_vs_round34_中段提示卡_before_after.mp4` | video | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 71 | `1.1 MiB` | `dist/20260414_豆包高效用法_cartoon_ip_formal/visual/seg05_image.png` | image | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 72 | `1.1 MiB` | `dist/20260414_豆包高效用法_cartoon_ip_formal/visual/seg01_image.png` | image | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 73 | `1.1 MiB` | `dist/voice_trials/20260426_语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis/语音样本2_完整转写输入_24k_mono.wav` | audio | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 74 | `920.1 KiB` | `dist/20260417_豆包的正确打开方式_vnext/tts/seg03_positive_strategy.wav` | audio | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 75 | `825.0 KiB` | `dist/voice_trials/20260426_台湾口语开心降噪试配_taiwan_happy_denoise_trial/A_沿用音色_台湾口语开心_API原始_未节奏校准.wav` | audio | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 76 | `806.3 KiB` | `dist/voice_trials/20260427_十五秒文案语速停顿试配_15s_copy_pacing_trial/A_15秒文案_自然节奏_API原始.wav` | audio | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 77 | `806.3 KiB` | `dist/voice_trials/20260427_十五秒文案语速停顿试配_15s_copy_pacing_trial/A_15秒文案_自然节奏.wav` | audio | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 78 | `797.0 KiB` | `dist/voice_trials/20260426_语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis/语音样本2_转写输入_24k_mono.wav` | audio | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 79 | `797.0 KiB` | `dist/voice_trials/20260426_语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis/语音样本2_复刻输入_10-20秒.wav` | audio | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 80 | `797.0 KiB` | `dist/voice_trials/20260426_台湾口语开心降噪试配_taiwan_happy_denoise_trial/B_复刻输入样本_轻降噪.wav` | audio | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 81 | `797.0 KiB` | `dist/voice_trials/20260425_round28_voice_clone_trial/语音样本_复刻输入_10-20秒.wav` | audio | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 82 | `776.3 KiB` | `dist/voice_trials/20260426_台湾口语开心降噪试配_taiwan_happy_denoise_trial/B_重建音色_台湾口语开心_API原始_未节奏校准.wav` | audio | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 83 | `765.0 KiB` | `dist/voice_trials/20260427_十五秒文案语速停顿试配_15s_copy_pacing_trial/B_15秒文案_停顿梗感_API原始.wav` | audio | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 84 | `765.0 KiB` | `dist/voice_trials/20260427_十五秒文案语速停顿试配_15s_copy_pacing_trial/B_15秒文案_停顿梗感.wav` | audio | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 85 | `754.8 KiB` | `dist/20260417_豆包的正确打开方式_vnext/tts/seg02_negative.wav` | audio | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 86 | `713.4 KiB` | `复审包_review_packs/20260430_可爱风格卡片页参考核查_cute_card_reference_audit/图二参考图.png` | image | 谨慎保留 | 当前复审 / reference 证据，若瘦身应先迁 LFS 或保留最小证据 |
| 87 | `713.4 KiB` | `dist/latest_review_pack/图二参考图.png` | image | 谨慎保留 | 当前复审 / reference 证据，若瘦身应先迁 LFS 或保留最小证据 |
| 88 | `713.4 KiB` | `dist/20260417_豆包的正确打开方式_vnext/round34_中段双展示提示卡_正反分段提示修复/inputs/图二参考图.png` | image | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 89 | `690.0 KiB` | `dist/20260417_豆包的正确打开方式_vnext/voice_candidates_round3/C1/C1_raw.wav` | audio | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 90 | `679.6 KiB` | `dist/20260417_豆包的正确打开方式_vnext/round34_中段双展示提示卡_正反分段提示修复/audit/problem_windows/30_40s.mp4` | video | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 91 | `678.8 KiB` | `dist/20260417_豆包的正确打开方式_vnext/voice_candidates_round4/E2/E2_raw.wav` | audio | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 92 | `675.0 KiB` | `dist/20260417_豆包的正确打开方式_vnext/voice_candidates/A2_qwen3_serena_steady/A2_qwen3_serena_steady_raw.wav` | audio | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 93 | `667.5 KiB` | `dist/20260417_豆包的正确打开方式_vnext/voice_candidates_round3/C3/C3_raw.wav` | audio | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 94 | `665.9 KiB` | `dist/voice_trials/20260426_台湾口语开心降噪试配_taiwan_happy_denoise_trial/B_重建音色_台湾口语开心_轻降噪.wav` | audio | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 95 | `665.9 KiB` | `dist/voice_trials/20260426_台湾口语开心降噪试配_taiwan_happy_denoise_trial/B_重建音色_台湾口语开心_原始.wav` | audio | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 96 | `664.9 KiB` | `dist/voice_trials/20260426_台湾口语开心降噪试配_taiwan_happy_denoise_trial/A_沿用音色_台湾口语开心_轻降噪.wav` | audio | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 97 | `664.9 KiB` | `dist/voice_trials/20260426_台湾口语开心降噪试配_taiwan_happy_denoise_trial/A_沿用音色_台湾口语开心_原始.wav` | audio | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 98 | `652.5 KiB` | `dist/20260417_豆包的正确打开方式_vnext/voice_candidates_round2/B3/B3_raw.wav` | audio | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 99 | `648.8 KiB` | `dist/20260417_豆包的正确打开方式_vnext/voice_candidates_round4/E1/E1_raw.wav` | audio | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |
| 100 | `648.8 KiB` | `dist/20260417_豆包的正确打开方式_vnext/voice_candidates_round2/B1/B1_raw.wav` | audio | 否 / 建议 LFS | 媒体产物会放大 Git 历史，适合 LFS 或外部存储 |

## 5. 大文件来源归因

| 来源目录 | 历史对象估计体积 | 当前工作树体积 | 主要文件类型 | 判断 |
| --- | ---: | ---: | --- | --- |
| `dist/其他历史产物/` | `852.5 MiB` | `179.5 MiB` | video, image, audio | 历史媒体产物主来源，适合后续 LFS / 历史瘦身评估 |
| `素材检查_reports/` | `44.8 MiB` | `0 B` | image, audio, text | 按文件价值细分 |
| `node_modules/` | `44.5 MiB` | `0 B` | other, text, json | 依赖二进制误入历史，应避免跟踪 |
| `复审包_review_packs/` | `40.3 MiB` | `16.1 MiB` | video, image, text | 复审证据来源，需保留最小证据或迁 LFS |
| `dist/latest_review_pack/` | `13.8 MiB` | `32.6 MiB` | video, image, json | 按文件价值细分 |
| `dist/voice_trials/` | `11.1 MiB` | `14.0 MiB` | audio, json, text | 历史媒体产物主来源，适合后续 LFS / 历史瘦身评估 |
| `治理_reports/` | `10.3 MiB` | `4.5 MiB` | json, text | 按文件价值细分 |
| `素材库_assets/` | `8.9 MiB` | `0 B` | video, json | 含当前锚点，需白名单保护 |
| `codex_log/` | `6.8 MiB` | `1.3 MiB` | text, audio | 按文件价值细分 |
| `repo_root` | `6.3 MiB` | `364.1 KiB` | other, text, json | 按文件价值细分 |
| `scripts/` | `2.8 MiB` | `396.1 KiB` | other | 按文件价值细分 |
| `tests/` | `2.8 MiB` | `176.2 KiB` | other | 按文件价值细分 |
| `codex_source/` | `1.9 MiB` | `250.1 KiB` | text | 按文件价值细分 |
| `归档_archive/` | `1.3 MiB` | `5.2 KiB` | text, json | 按文件价值细分 |
| `review_loop/` | `1019.3 KiB` | `60.0 KiB` | image, text, other | 按文件价值细分 |
| `project_source/` | `1000.4 KiB` | `251.7 KiB` | text | 按文件价值细分 |
| `GPT数据源/` | `557.0 KiB` | `81.3 KiB` | text | 按文件价值细分 |
| `config/` | `169.9 KiB` | `13.3 KiB` | other, json | 按文件价值细分 |
| `cases/` | `165.2 KiB` | `33.2 KiB` | text | 按文件价值细分 |
| `GPT 数据源/` | `66.9 KiB` | `20.1 KiB` | text | 按文件价值细分 |

## 6. 当前 `.git` 变大的主因

- `已确认` 最大主因是 `.git/objects/pack/tmp_pack_*` 与其他 garbage 对象：`git count-objects -vH` 报告 `size-garbage = 15.51 GiB`，`tmp_pack_*` 文件合计约 `15.5 GiB`。
- `已确认` 正式 pack 仍有 `3.99 GiB`，其中可见旧视频、旧音频、旧图片、旧复审包与旧 dist 产物。
- `已确认` reachable 历史最大 blob 包括历史 `node_modules/ffmpeg-static/ffmpeg`、`dist/20260417_豆包的正确打开方式_vnext/` 多轮 MP4、`复审包_review_packs/` 旧 v1/v2/v3 full video、旧 voice trial WAV、旧图片候选等。
- `已确认` 当前工作树仍跟踪不少媒体文件，尤其是旧 `dist/20260414...`、旧 `dist/20260417...`、`dist/latest_review_pack/`、`复审包_review_packs/` 和 voice trial 音频。
- 普通删除工作树文件只会让当前树变小；如果历史对象还被 commit / branch / tag / reflog / pack 保留，`.git` 不会立即变小。
- 这里还有更直接的本地原因：存在大量 Git garbage / tmp_pack；但本轮禁止 `git gc` / `prune` / `repack`，所以只记录，不清理。

## 7. 可选瘦身方案比较

| 方案 | 动作 | 预计收益 | 风险 | 是否推荐 | 需要用户确认 |
| --- | --- | --- | --- | --- | --- |
| 重新 clone 干净仓库 | 另建一个全新 clone，或当前目录外验证 clone 体积；不改远端历史 | 若远端没有这些本地 garbage，预计可直接避开约 `15.5GiB` garbage；但仍会下载远端历史 pack | 需要重新确认本地未追踪 / 未推送 / 本地配置；不能丢 GPT 静态包冻结文件 | `推荐作为第一步只读验证 / 低风险瘦身` | 需要 |
| Git LFS 迁移 | 对视频 / 音频 / 大图片配置 LFS，并迁移历史或仅未来新增 | 未来收益稳定；历史迁移才会明显减小远端历史 | 历史迁移需要重写提交；所有协作者要重新 clone；PR / 分支可能受影响 | `中期推荐，但先不要直接执行历史迁移` | 必须 |
| Git history rewrite | 用 `git filter-repo` / BFG 删除或迁移历史大文件 | 可清掉旧 dist / review pack / node_modules 历史对象 | 高风险；改变 commit SHA；需要 force push；所有分支 / PR 都要协调 | `仅在备份和冻结窗口后执行` | 必须 |
| 新建干净仓库 | 只把当前保留内核导入新 repo，旧 repo 归档 | 可获得最干净历史和最小默认读取 | 历史断裂；issue / PR / branch 关联迁移成本高 | `可作为备选长期方案` | 必须 |
| 本地 GC / prune | 在当前 repo 执行 GC / prune / 清理 garbage | 可能释放本地 `15.5GiB` garbage | 本轮禁止；执行前需备份，且要确认不会影响未推送对象 | `可作为下一轮本地瘦身专项评估` | 必须 |

## 8. 推荐路线

- 主路线：先做“安全 fresh clone / clean clone 对照验证”，不要先重写历史。
- 为什么：本次 `.git` 最大问题是本地 garbage / `tmp_pack_*`，fresh clone 很可能绕开约 `15.5GiB` 本地垃圾，风险远低于 history rewrite。
- 做到哪算完：新 clone 能打开主读取分支、保留当前 reference whitelist / 当前日志、体积显著低于当前 `.git 21G`，且 GPT 静态包冻结项另行处理不丢失。
- 风险：新 clone 不会自动带走本地未追踪文件、local config、未推送分支；需要先列清单。
- 执行前必须备份什么：当前整个 `/Users/fan/Documents/视频工厂`，尤其是未追踪 `GPT 数据源/10_样片参考质量规则_reference_quality_sample_rule.md`、本地 only 文件、未推送分支清单、当前 PR 链接。

备选路线：若 fresh clone 后远端历史仍然过大，再另起 Git LFS / history rewrite 方案评审；执行前必须冻结 PR、备份仓库、确认所有协作入口，并接受 commit SHA 改写和 force push 风险。

## 9. 已知冻结未追踪文件

- `GPT 数据源/10_样片参考质量规则_reference_quality_sample_rule.md`
- 状态：`untracked / frozen / untouched`
- 本轮处理：未纳入、未删除、未移动、未重命名、未修改。
- 后续处理：另起 GPT Project 静态包整理任务。

当前状态记录：

```text
## codex/git-history-large-files-audit-20260504
?? "GPT \346\225\260\346\215\256\346\272\220/10_\346\240\267\347\211\207\345\217\202\350\200\203\350\264\250\351\207\217\350\247\204\345\210\231_reference_quality_sample_rule.md"
```

## 10. 本轮未执行动作确认

- 未删除。
- 未移动。
- 未重命名。
- 未执行 Git GC。
- 未执行 Git prune。
- 未执行 Git repack。
- 未执行 Git LFS migrate。
- 未执行 filter-repo / filter-branch / BFG。
- 未 force push。
- 未修改当前发布状态。
- 未生成视频、音频或图片。

## 11. Git LFS 当前状态

```text
git-lfs not installed or git lfs unavailable
.gitattributes missing
LFS ls-files unavailable or no LFS configured
```

判断：当前仓库没有可用 Git LFS 配置；后续若要引入 LFS，应先做策略设计，不应直接迁移历史。

## 12. Git 同步

- commit SHA：待提交后填写。
- 是否已 push：待提交后填写。
- PR 链接：待创建后填写。
- 是否已同步到 `codex/user-readable-map`：否，本轮审计 PR 不自动合并。

## 13. 下一个目标

用户 / ChatGPT 复审 `.git` 历史大文件审计报告，再决定是否执行 Git LFS / 历史瘦身或重新 clone / 新建干净仓库。
