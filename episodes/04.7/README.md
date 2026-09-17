# 4.7 正向传播、反向传播和计算图

机制：同一条路上正向再反向。光晕旅行者走 2-D \(\mathbf{x}\) → 2 个 ReLU 隐单元 → 标量 \(\hat{y}\)，单样本 \(\ell=(\hat{y}-y)^2\)。局部梯度作为箭头长在同一批节点上。不训练，不摊权重矩阵。

片外说明（不进视频）：[NOTES.md](NOTES.md)

D2L：https://zh.d2l.ai/chapter_multilayer-perceptrons/backprop.html

## Render

```bash
python -m manim episodes/04.7/scene.py Episode047 \
  -r 1920,1080 --fps 60 --format mp4
```

成片约 31 秒，H.264，无音轨。MP4 放 GitHub Release，不进 Git。
