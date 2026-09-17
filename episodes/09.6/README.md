# 9.6 编码器-解码器架构

机制：变长输入压成固定形状状态 \(c\in\mathbb{R}^2\)，解码器再按时间一步吐一个变长输出。3 进 2 出。光晕旅行者是 \(c\)。不训练。

片外说明（不进视频）：[NOTES.md](NOTES.md)

D2L：https://zh.d2l.ai/chapter_recurrent-modern/encoder-decoder.html

```bash
.venv/bin/manim episodes/09.6/scene.py Episode096 \
  -r 1920,1080 --fps 60 --format mp4 --renderer cairo
```

成片约 32 秒，H.264，无音轨。MP4 放 GitHub Release，不进 Git。
