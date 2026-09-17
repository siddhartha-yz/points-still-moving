# 11.10 Adam

机制：同一只 11.6 的窄谷，同一起点、同一 \(\eta\)。先沿单样本 SGD 横着振荡；再从同一点用 Adam（一阶矩动量 + 二阶矩 RMSProp，偏差校正后迈步）。光晕旅行者是参数 \(w\)。公式 \(w\leftarrow w-\eta\hat v/(\sqrt{\hat s}+\varepsilon)\) 只出现一次。真实 numpy。淡蓝 SGD 轨迹留到最后一帧。

片外说明（不进视频）：[NOTES.md](NOTES.md)

D2L：https://zh.d2l.ai/chapter_optimization/adam.html

```bash
.venv/bin/manim episodes/11.10/scene.py Episode1110 \
  -r 1920,1080 --fps 60 --format mp4
```

成片约 32 秒，H.264，无音轨。MP4 放 GitHub Release，不进 Git。
