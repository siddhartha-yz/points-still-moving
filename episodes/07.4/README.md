# 7.4 含并行连结的网络（GoogLeNet）

机制：Inception。同一张输入并行走 \(1\times 1\)、\(3\times 3\)、\(5\times 5\) 和 \(3\times 3\) 最大汇聚，再在通道维拼接。光晕圈住一格空间，通道因 concat 变多。不训练。

片外说明（不进视频）：[NOTES.md](NOTES.md)

D2L：https://zh.d2l.ai/chapter_convolutional-modern/googlenet.html

```bash
.venv/bin/manim episodes/07.4/scene.py Episode074 \
  -r 1920,1080 --fps 60 --format mp4 --renderer cairo
```

成片约 33 秒，H.264，无音轨。MP4 放 GitHub Release，不进 Git。
