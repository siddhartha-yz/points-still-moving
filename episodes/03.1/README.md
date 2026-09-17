# 3.1 线性回归

机制：直线用小批量 SGD 在点里找位置。高亮样本的残差缩短，最后留下噪声残差。不演解析解，不演损失曲面。

片外说明（不进视频）：[NOTES.md](NOTES.md)

D2L：https://zh.d2l.ai/chapter_linear-networks/linear-regression.html

```bash
.venv/bin/manim episodes/03.1/scene.py Episode031 \
  -r 1920,1080 --fps 60 --format mp4
```

成片约 25 秒，H.264，无音轨。MP4 放 GitHub Release，不进 Git。
