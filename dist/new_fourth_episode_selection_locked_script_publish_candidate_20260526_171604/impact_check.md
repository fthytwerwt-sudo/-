# impact_check

1. 本轮是否是视频执行任务：是，`locked_copy_video_execution + publish_candidate_delivery`。
2. 本轮是否会生成媒体：只有在全部闸门通过时才会生成；当前闸门已阻断，未生成 `full.mp4 / narration.wav / captions.srt`。
3. 本轮是否会调用 MiniMax / TTS API：已调用 MiniMax 百炼代理做最小路线验证；未生成全片 TTS。
4. 本轮是否会修改 `dist/`：是，写入本轮 blocked review pack 与 MiniMax 路线 smoke 报告。
5. 本轮是否会修改脚本：否。
6. 本轮是否会修改机制文件：否。
7. 本轮是否会修改用户文案：否；锁稿未改。
8. 本轮是否会读取旧新第四期 preflight 包：是，只作为素材时间码和风险参考，不作为最终映射。
9. 本轮是否会复用旧稿：否。
10. 本轮是否会触碰旧 B / Qwen 语音脚本：只读取/遵守路线禁令，不用其生成正片。
11. 本轮是否会提交媒体产物：不会提交大媒体；MiniMax smoke 小音频只作为诊断文件，不作为候选片。
12. 本轮是否存在 secret / API key / token 风险：存在 API runtime 调用风险；本轮未打印或写入 key，报告只写 masked source。
13. 本轮如果达不到正片候选，blocked 条件是什么：核心动作画面证据不足、表格/复查表可读性未过、SKU 风险证据不足、MiniMax 候选旁白未生成且路线 smoke 总状态 blocked、preflight suite 任一 gate failed。
