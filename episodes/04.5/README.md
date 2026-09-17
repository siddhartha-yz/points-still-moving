# 4.5 权重衰减

机制：同一条高容量曲线先在 \(\lambda=0\) 时穿过训练点并偏离留出的旅行者，再被 \(\lambda\|\mathbf{w}\|^2\) 拉回光滑，旅行者残差缩短。不演逐步 SGD，不演 \(L_1\)。

片外说明（不进视频）：[NOTES.md](NOTES.md)

D2L：https://zh.d2l.ai/chapter_multilayer-perceptrons/weight-decay.html

```bash
.venv/bin/manim episodes/04.5/scene.py Episode045 \
  -r 1920,1080 --fps 60 --format mp4
```

成片约 28 秒，H.264，无音轨。MP4 放 GitHub Release，不进 Git。
