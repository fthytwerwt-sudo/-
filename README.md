# 15秒案例视频 Demo

这是一个最小可用的中文案例视频 demo。
输入固定是 `cases/demo.md`，输出会生成到 `dist/demo/`。

## 你后续怎么复用
1. 直接替换 `cases/demo.md` 里的内容。
2. 在当前目录运行：

```bash
python3 generate_demo.py
```

3. 生成结果看这里：
   `dist/demo/script.txt`
   `dist/demo/captions.srt`
   `dist/demo/voice.mp3`
   `dist/demo/final.mp4`

## 这个 demo 用了什么
- 文本解析：Python 标准库
- 配音：macOS 自带 `say`
- 音频中转：macOS 自带 `afconvert`
- mp3 输出：项目内置 `ffmpeg-static`
- 视频合成：Swift + AVFoundation

## 适合什么场景
先验证“能不能稳定跑出一条最小案例视频”。
这版刻意保持简单：3页、PPT风格、中文讲解、无复杂动画。
