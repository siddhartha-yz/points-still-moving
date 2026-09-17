# 6.2 互相关 / 卷积层

机制：3×3 核在 4×4 输入上滑动，一个输出格被点亮；乘加与 `numpy` / D2L `corr2d` 一致。核再右移一格，邻居格点亮。不训练，不演偏置，不铺整张特征图。

片外说明（不进视频）：[NOTES.md](NOTES.md)

D2L：https://zh.d2l.ai/chapter_convolutional-neural-networks/conv-layer.html

## Render

```bash
python -m manim episodes/06.2/scene.py Episode062 \
  -r 1920,1080 --fps 60 --format mp4
```

成片约 31 秒，H.264，无音轨。MP4 放 GitHub Release，不进 Git。
