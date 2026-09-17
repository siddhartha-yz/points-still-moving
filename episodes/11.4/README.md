# 11.4 随机梯度下降

机制：同一只 11.3 的椭圆碗，同一起点。先沿完整 \(\nabla f\) 走进谷；再从同一点用单样本 \(\nabla f_i\) 重走，轨迹在谷里抖动。光晕旅行者是参数 \(w\)。公式 \(w\leftarrow w-\eta\nabla f_i\) 只出现一次。真实 numpy。

片外说明（不进视频）：[NOTES.md](NOTES.md)

D2L：https://zh.d2l.ai/chapter_optimization/sgd.html

```bash
.venv/bin/manim episodes/11.4/scene.py Episode114 \
  -r 1920,1080 --fps 60 --format mp4
```

成片约 35 秒，H.264，无音轨。MP4 放 GitHub Release，不进 Git。
