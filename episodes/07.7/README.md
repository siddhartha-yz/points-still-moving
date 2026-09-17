# 7.7 稠密连接网络

机制：稠密块。每层输出在通道维拼到所有前层，\(x\leftarrow[x,f(x)]\)，不是相加。光晕旅行者是正在变长的拼接张量。不训练。

片外说明（不进视频）：[NOTES.md](NOTES.md)

D2L：https://zh.d2l.ai/chapter_convolutional-modern/densenet.html

```bash
.venv/bin/manim episodes/07.7/scene.py Episode077 \
  -r 1920,1080 --fps 60 --format mp4 --renderer=cairo
```

成片约 32 秒，H.264，无音轨。MP4 放 GitHub Release，不进 Git。
