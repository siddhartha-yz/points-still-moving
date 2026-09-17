# 11.11 学习率调度器

机制：同一只椭圆碗 \(f(w)=w_1^2+2w_2^2\)，光晕旅行者是参数点 \(w\)。步长 \(\eta(t)\) 先线性热身再余弦衰减。公式 \(w\leftarrow w-\eta(t)\nabla f\) 只出现一次。\(\eta\) 写在调度曲线上方的固定口袋里。真实 numpy。不训练网络。

片外说明（不进视频）：[NOTES.md](NOTES.md)

D2L：https://zh.d2l.ai/chapter_optimization/lr-scheduler.html

```bash
.venv/bin/manim episodes/11.11/scene.py Episode1111 \
  -r 1920,1080 --fps 60 --format mp4 --renderer cairo
```

成片约 33 秒，H.264，无音轨。MP4 放 GitHub Release，不进 Git。
