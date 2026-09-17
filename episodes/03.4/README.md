# 3.4 softmax回归

机制：同一颗高亮 \(\mathbf{x}\) 先做前向 \(o = Wx + b\)，再 softmax 成非负且和为 1 的概率。最大项的次序不变；不演交叉熵，不训练。

片外说明（不进视频）：[NOTES.md](NOTES.md)

D2L：https://zh.d2l.ai/chapter_linear-networks/softmax-regression.html

## Render

```bash
python -m manim episodes/03.4/scene.py Episode034 \
  -r 1920,1080 --fps 60 --format mp4
```

成片约 25 秒，H.264，无音轨。MP4 放 GitHub Release，不进 Git。
