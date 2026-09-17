# 8.7 通过时间反向传播

机制：把一个标量 RNN 沿六个时间步展开；同一条隐藏状态链先正向
计算，再由终端损失的梯度沿原边反向走回。窗口限制为最后三个状态，
因此梯度在 \(h_4\) 前截断。没有训练或参数更新。

片外说明（不进视频）：[NOTES.md](NOTES.md)

D2L：https://zh.d2l.ai/chapter_recurrent-neural-networks/bptt.html

## Render

```bash
python -m manim --renderer=cairo episodes/08.7/scene.py Episode087 \
  -r 1920,1080 --fps 60 --format mp4
```

成片约 28 秒，H.264，无音轨。场景中的输入、隐藏状态与 BPTT
导数全部由 `scene.py` 的 NumPy 数组计算并在渲染时打印。
