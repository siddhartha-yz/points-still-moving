# 4.4 欠拟合和过拟合

机制：同一份带噪声的一维训练点，一次多项式错过点云，六次多项式穿过每个训练点却偏离留出的旅行者。数字只来自 `numpy.polyfit`。不演训练循环，不演右侧损失表。

片外说明（不进视频）：[NOTES.md](NOTES.md)

D2L：https://zh.d2l.ai/chapter_multilayer-perceptrons/underfit-overfit.html

```bash
.venv/bin/manim episodes/04.4/scene.py Episode044 \
  -r 1920,1080 --fps 60 --format mp4
```

成片约 28 秒，H.264，无音轨。MP4 放 GitHub Release，不进 Git。
