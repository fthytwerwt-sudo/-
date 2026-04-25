# Latest

## 20260426｜下一个目标与中文英文命名规则补丁

- `已确认` 本轮只做规则补丁，不做目录迁移，不执行 `git mv`，不重命名任何已有文件或文件夹。
- `已确认` 执行位置已校准到主读取分支 worktree：`/private/tmp/视频工厂_user_readable_map_sync`，当前分支为 `codex/user-readable-map`。
- `已确认` 已写入最终汇报和交接口径：最后一栏统一使用“下一个目标”，不再默认使用“下一步行动建议”。
- `已确认` 已写入新增业务文件 / 业务文件夹命名规则：默认使用“中文 + 英文”，推荐格式为 `中文名_english_name`。
- `已确认` 已有文件和已有文件夹本轮不追溯改名；工具链强制英文名保留为例外，且例外不得扩大到普通业务目录和业务文件。
- `已确认` 本轮不修改视频、音频、图片、原始素材、生成脚本或测试脚本。
- `已确认` 当前视频状态未改变：
  - `latest_review_pack = round34_中段双展示提示卡_正反分段提示修复`
  - `content_validation = 待用户 / ChatGPT 最终复审`
  - `full_content_validation = 待用户 / ChatGPT 最终复审`
  - `send_ready = no`
- `已确认` 提交前本地验证已通过；远端同步状态以本轮收尾的 `git show origin/codex/user-readable-map:路径` 复读验证为准。

## 20260426｜round28 声音复刻试配继续执行

- `已确认` 本轮继续上轮被阿里百炼 `Arrearage` 阻塞的 voice cloning（声音复刻）路线；不重回 `Serena` 系统音色，不修改视频，不替换全片音轨，不生成新视频 round。
- `已确认` 复用上轮合规复刻输入样本：`dist/voice_trials/20260425_round28_voice_clone_trial/语音样本_复刻输入_10-20秒.wav`，参数仍为 `17.00s / wav / pcm_s16le / 24000 Hz / mono / 816078 bytes`。
- `已确认` 阿里账户本轮不再返回 `Arrearage`；用户 prompt 指定的 `vf_r28_clone_20260426` 因超过官方 `preferred_name` 16 字符限制返回 `InvalidParameter`，已按官方约束改用 `vfr28clone0426`。
- `已确认` 已创建测试 custom voice，脱敏标识：`qwen-t...de43`；创建模型为 `qwen-voice-enrollment`，`target_model = qwen3-tts-vc-realtime-2026-01-15`。
- `已确认` 已使用该 custom voice 生成 1 条 round28 声音复刻 trial：`dist/voice_trials/20260425_round28_voice_clone_trial/round28_声音复刻试配_10-15秒.wav`。
- `已确认` 输出音频验证：`12.96s / wav / pcm_s16le / 24000 Hz / mono / 622124 bytes`，可被 `ffmpeg` 解码；`mean_volume = -23.5 dB`，`loudnorm.input_i = -23.57 LUFS`。
- `已确认` 脱敏请求记录：
  - `dist/voice_trials/20260425_round28_voice_clone_trial/voice_clone_request_debug_sanitized.json`
  - `dist/voice_trials/20260425_round28_voice_clone_trial/voice_clone_tts_request_debug_sanitized.json`
- `待验证` 本轮只证明 voice cloning trial 已生成；是否明显比上一轮 `Serena` 更接近用户样本，仍待用户 / ChatGPT 听感复审。
- `已确认` 当前视频状态未改变：
  - `latest_review_pack = round34_中段双展示提示卡_正反分段提示修复`
  - `content_validation = 待用户 / ChatGPT 最终复审`
  - `full_content_validation = 待用户 / ChatGPT 最终复审`
  - `send_ready = no`

## 20260425｜round28 声音复刻最小试配

- `已确认` 用户授权已到位；本轮允许上传裁剪后的合规样本到阿里百炼声音复刻接口，仅用于《视频工厂》最小声音复刻试配。
- `已确认` 已生成合规复刻输入样本：`dist/voice_trials/20260425_round28_voice_clone_trial/语音样本_复刻输入_10-20秒.wav`，参数为 `17.00s / wav / pcm_s16le / 24000 Hz / mono / 816078 bytes`。
- `已确认` 本轮实际走的是 `qwen-voice-enrollment -> qwen3-tts-vc-realtime-2026-01-15` 的声音复刻路线，没有回退到 `Serena` 系统音色。
- `已确认` 当前阻塞点发生在 `create_custom_voice` 阶段：阿里百炼返回 `400 / Arrearage`，未创建成功 custom voice，未生成新的声音复刻试配音频。
- `已确认` 脱敏请求记录：`dist/voice_trials/20260425_round28_voice_clone_trial/voice_clone_request_debug_sanitized.json`。
- `已确认` 复刻试配日志：`codex_log/20260425_round28_声音复刻最小试配.md`。
- `待验证` 账户恢复后，可直接复用本轮合规裁剪样本继续创建 custom voice；当前声音仍待验证。
- `已确认` 当前视频状态未改变：
  - `latest_review_pack = round34_中段双展示提示卡_正反分段提示修复`
  - `content_validation = 待用户 / ChatGPT 最终复审`
  - `full_content_validation = 待用户 / ChatGPT 最终复审`
  - `send_ready = no`

## 20260425｜round28 声音试配失败排查

- `已确认` 用户已听审 `dist/voice_trials/20260425_round28_10s_voice_trial/round28_声音试配_10-15秒.m4a`，反馈为：和样本完全不一样，非常生硬，一听就是 AI。
- `已确认` 本轮只做声音路线诊断；未生成新音频，未修改视频 / 图片 / 原始素材 / 当前 trial 音频 / 脚本，未调用 TTS API，未上传用户样本。
- `已确认` 当前 trial 请求体为 `qwen3-tts-instruct-flash-realtime + Serena` 系统音色 + 指令控制；请求体里没有用户样本、custom voice、voice cloning 或 voice design 字段。
- `已确认` 失败主因：用户样本没有实际进入生成链路，当前路线只能做系统音色的风格指令控制，不能复刻用户样本声纹。
- `部分成立` 文案韵律和后处理可能放大生硬 / AI 感，但不是“完全不像样本”的主因。
- `待验证` 下一轮最值路线是：先取得用户明确授权，再走 `voice cloning（声音复刻）` 最小试配；若用户不授权上传样本，则退而走 `voice design（声音设计）`，不要继续盲调 `Serena`。
- `已确认` 诊断日志：`codex_log/20260425_round28_声音试配失败排查.md`。
- `已确认` 当前视频状态未改变：
  - `latest_review_pack = round34_中段双展示提示卡_正反分段提示修复`
  - `content_validation = 待用户 / ChatGPT 最终复审`
  - `full_content_validation = 待用户 / ChatGPT 最终复审`
  - `send_ready = no`

## 20260425｜round28 最小声音试配

- `已确认` 本轮只生成 1 条 10-15 秒声音 trial（试配）音频；未修改任何视频、图片、原始素材、当前成片音轨或视频装配脚本。
- `已确认` 使用 round28 文案来源：`dist/20260417_豆包的正确打开方式_vnext/round28_完整可读终修/subtitles/round28_完整可读终修.srt`。
- `已确认` 本轮试配文案取自 round28 字幕第 1 段 + 第 5 段首句：
  - `最费时间的，不是做汇报页。是第一行根本写不出来。后来我换上调好的提示词，直接砍掉空转。区别不是豆包，是那段提示词。`
- `已确认` 真实使用 TTS：`aliyun_bailian / aliyun_qwen_realtime_websocket / qwen3-tts-instruct-flash-realtime / Serena`。
- `已确认` 输出音频：`dist/voice_trials/20260425_round28_10s_voice_trial/round28_声音试配_10-15秒.m4a`。
- `已确认` 音频基础验证：`13.00s`、`aac (LC)`、`48000 Hz / mono`、`mean_volume = -16.4 dB`、`loudnorm.input_i = -16.25 LUFS`，可被 `ffmpeg` 解码。
- `已确认` 当前视频状态未改变：
  - `latest_review_pack = round34_中段双展示提示卡_正反分段提示修复`
  - `content_validation = 待用户 / ChatGPT 最终复审`
  - `full_content_validation = 待用户 / ChatGPT 最终复审`
  - `send_ready = no`
- `待验证` 该 trial 只回答声音方向是否接近“低压、清楚、有一点可爱感的女生游戏向导音”；用户 / ChatGPT 听感复审前，不得写成最终音色、最终 TTS 或声音验证通过。

## 20260425｜语音样本只读排查与声音参考锚点

- `已确认` 本轮任务只做语音样本定位、音频基础参数分析、声音参考锚点落地与仓库口径更新；不改视频、不替换旁白、不生成新 round、不做 TTS 试配。
- `已确认` 当前 latest_review_pack 仍指向：`round34_中段双展示提示卡_正反分段提示修复`。
- `已确认` 用户语音样本已通过兜底搜索命中：`/Users/fan/Documents/视频工厂/素材录制/语音样本_04-25-2026 22-19-11_1.MP4`。
- `已确认` 样本用于记录 `可爱女生向导音` 的 reference anchor（参考锚点）；它不等于最终 TTS 方案已确定，也不等于声音内容验证通过。
- `部分成立` `ffmpeg` 可用并已完成分析用音频副本提取、`volumedetect`、`astats`、`silencedetect` 与 `loudnorm` 初步测量；`ffprobe` 未在本机可执行路径中命中，本轮元数据读取降级使用 `ffmpeg` 输入信息。
- `已确认` 音频基础参数报告：`codex_log/20260425_语音样本_audio_reference_report.md`。
- `已确认` 分析文本输出目录：`codex_log/audio_reference/20260425_语音样本/`。
- `已确认` 当前视频状态未改变：
  - `content_validation = 待用户 / ChatGPT 最终复审`
  - `full_content_validation = 待用户 / ChatGPT 最终复审`
  - `send_ready = no`
- `待验证` 下一步声音动作是基于该样本做 10-15 秒最小声音试配，再和当前视频开头 / 结尾主持壳做听感匹配复审；不得直接全片替换。

## 20260425｜round34 中段双展示提示卡正反分段提示修复

- `已确认` 当前视频工作分支为 `codex/doubao-vnext-direct-fix-20260417`；该分支当前由 Git worktree `/private/tmp/视频工厂_round28_complete_readability` 持有。
- `已确认` 本轮新开 `round34_中段双展示提示卡_正反分段提示修复`，只做 `latest_review_pack` 中段局部修复；未重构整条视频。
- `已确认` 用户本轮同步的图二参考图可读取：`/Users/fan/Desktop/截屏2026-04-25 18.11.07.png`，尺寸 `908x492`。
- `已确认` 两张提示卡已按图二粉色樱花柔和展示牌风格重构为 720x1280、9:16 竖屏：
  - 《反面展示》：`先看旧做法：一句糊话，结果怎么变泛`
  - 《正面展示》：`再看工作包后：结果怎么一步步落成`
- `已确认` round34 中段结构为：反面展示提示卡 -> 反面真实录屏 -> 正面展示提示卡 -> 正面真实录屏 -> 结果差提示卡。
- `已确认` 反面录屏与正面录屏仍由用户真实录屏承担，源时间码与 round33 一致，未裁短、未替换、未重录。
- `已确认` 开头主持壳、回场主持壳、`judgment_card`、Prompt 引用尾卡均未重做；未调用阿里 API，未重新生成元素娃娃，未修改原始录屏素材。
- `已确认` `latest_review_pack` 已更新指向：
  - `round34_中段双展示提示卡_正反分段提示修复`
- `已确认` 当前审片包口径：
  - `middle_segment_review = 用户暂定通过 / 暂不继续修改中段`
  - `border_residue_validation = 通过`
  - `jump_cut_validation = 通过`
  - `technical_validation = 通过`
  - `content_validation = 待用户 / ChatGPT 最终复审`
  - `send_ready = no`
- `已确认` 用户已打开实际可用本地审片包路径：`/private/tmp/视频工厂_round28_complete_readability/dist/latest_review_pack/`。
- `已确认` 用户最新反馈为“现在中段没什么问题了”，仓库口径记录为：round34 中段结构暂定接受，当前不继续修改中段。
- `已确认` 中段暂定接受只代表 `middle_segment_review` 暂定收束，不代表全片 `content_validation` 通过。
- `待验证` round34 内容最终是否过线仍需用户 / ChatGPT 人工复审。
- `禁止误写` 不得把技术扫描通过写成内容最终通过；不得写 `send_ready = yes`；不得把云端剪辑写成稳定跑通。

## 当前最新审片入口

- 当前可打开本地审片包：`/private/tmp/视频工厂_round28_complete_readability/dist/latest_review_pack/`
- `dist/latest_review_pack/review_manifest.md`
- `dist/latest_review_pack/summary.json`
- `dist/latest_review_pack/full.mp4`
- `dist/latest_review_pack/middle_preview.mp4`
- `dist/latest_review_pack/before_after.mp4`
- `dist/latest_review_pack/图二参考图.png`
- `dist/latest_review_pack/反面展示提示卡_单帧.png`
- `dist/latest_review_pack/正面展示提示卡_单帧.png`
- `dist/latest_review_pack/正反提示卡_并排对比.png`
- `dist/latest_review_pack/problem_windows/30_32s.mp4`
- `dist/latest_review_pack/cut_contact_sheet.jpg`

## 新会话接手建议先读

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `GPT数据源/08_当前正式事实.md`
- `codex_log/current_publish_target.md`
- `codex_log/current_publish_target_light_evidence.md`
- `dist/latest_review_pack/review_manifest.md`
- `dist/latest_review_pack/summary.json`
- `codex_log/20260425_round34_中段双展示提示卡_正反分段提示修复.md`
- `codex_log/20260425_round34_中段暂定通过与本地审片路径修正.md`
