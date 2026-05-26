# impact_check

1. 本轮是正片候选生成任务：是。
2. 本轮会生成视频：是，生成 `full.mp4`。
3. 本轮会调用 MiniMax / TTS API：是，只允许 MiniMax `speech-2.8-hd / MiniMax/speech-2.8-hd`。
4. 本轮会修改 `dist/`：是，仅新建本轮输出目录。
5. 本轮会修改脚本：是，使用本轮专用 rerun 生成脚本。
6. 本轮会修改文案：否。
7. 本轮不会提交媒体文件到 Git。
8. 本轮会读取 v2 证据复核报告：是。
9. 本轮不会重复使用旧 blocker。
10. 若 blocked，只允许真实 MiniMax / 媒体 / 可读性 / 预检 / Git blocker。
11. API key / token / secret 风险：只读授权存在性，不打印、不写入、不提交。
12. 存在 unrelated dirty files：是，路径限定隔离。
