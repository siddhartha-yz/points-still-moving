# 11.8 RMSProp 算法

机制：在同一只窄谷 \(f(w)=0.1w_1^2+2w_2^2\) 中，从同一个参数点
开始比较 AdaGrad 和 RMSProp。AdaGrad 累积全部平方梯度，步长逐渐
缩小；RMSProp 用平方梯度的指数移动平均，因此继续沿谷底行走。
没有训练或参数更新。

片外说明（不进视频）：[NOTES.md](NOTES.md)

D2L：https://zh.d2l.ai/chapter_optimization/rmsprop.html

```bash
.venv/bin/manim --renderer=cairo episodes/11.8/scene.py Episode118 \
  -r 1920,1080 --fps 60 --format mp4
```

成片约 28 秒，H.264，无音轨。路径、累计平方梯度、移动平均与最后
的 \(w,f(w)\) 全部由 `scene.py` 的 NumPy 计算，并在渲染时打印。
