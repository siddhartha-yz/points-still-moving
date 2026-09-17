# 4.6 暂退法

机制：训练时按 \(p\) 把旅行者的隐单元随机置零；推断时全部打开，并乘保留概率 \(1-p\)。不训练权重，不演 inverted dropout 的训练缩放。

片外说明（不进视频）：[NOTES.md](NOTES.md)

D2L：https://zh.d2l.ai/chapter_multilayer-perceptrons/dropout.html

## Render

```bash
python -m manim episodes/04.6/scene.py Episode046 \
  -r 1920,1080 --fps 60 --format mp4
```

成片约 32 秒，H.264，无音轨。MP4 放 GitHub Release，不进 Git。
