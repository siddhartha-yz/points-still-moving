# 11.7 AdaGrad

机制：同一只窄谷 \(f(w)=0.1w_1^2+2w_2^2\)，光晕旅行者是参数点 \(w\)。先看普通梯度下降在陡轴上来回振荡；再写出 \(s\) 与 \(1/\sqrt{s}\)，走得猛的轴步长被压小。同一 \(\eta\)，真实 numpy。等高线只描边。

片外说明（不进视频）：[NOTES.md](NOTES.md)

D2L：https://zh.d2l.ai/chapter_optimization/adagrad.html

```bash
.venv/bin/manim episodes/11.7/scene.py Episode117 \
  -r 1920,1080 --fps 60 --format mp4
```

成片约 32 秒，H.264，无音轨。MP4 放 GitHub Release，不进 Git。
