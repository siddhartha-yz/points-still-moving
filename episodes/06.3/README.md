# 6.3 填充和步幅

机制：同一核，填充让输出格子长出边缘，步幅让核跳格、格子变少。输出高宽跟 numpy 的 \(\lfloor(n-k+2p)/s\rfloor+1\) 一致。不训练。

片外说明（不进视频）：[NOTES.md](NOTES.md)

D2L：https://zh.d2l.ai/chapter_convolutional-neural-networks/padding-and-strides.html

```bash
.venv/bin/manim episodes/06.3/scene.py Episode063 \
  -r 1920,1080 --fps 60 --format mp4
```

成片约 33 秒，H.264，无音轨。MP4 放 GitHub Release，不进 Git。
