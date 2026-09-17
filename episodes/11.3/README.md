# 11.3 梯度下降

机制：二维凸碗 \(f(w)=w_1^2+2w_2^2\) 上，光晕旅行者是参数点 \(w\)。沿 \(-\eta\nabla f\) 迈步。中等 \(\eta\) 走进谷底；过大的 \(\eta\) 在陡的那一轴越过谷底。真实 numpy。公式 \(w\leftarrow w-\eta\nabla f\) 只出现一次。

片外说明（不进视频）：[NOTES.md](NOTES.md)

D2L：https://zh.d2l.ai/chapter_optimization/gd.html

```bash
.venv/bin/manim episodes/11.3/scene.py Episode113 \
  -r 1920,1080 --fps 60 --format mp4
```

成片约 30 秒，H.264，无音轨。MP4 放 GitHub Release，不进 Git。
