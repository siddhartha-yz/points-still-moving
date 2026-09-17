# 11.2 凸性

机制：凸碗 \(f(x)=0.5x^2\) 上任意两点的弦都在曲面上方；非凸的 \(g(x)=\cos(\pi x)\) 弦会穿到曲面底下，并多出一口坑。光晕旅行者是弦上的一点 \(z=\lambda x+(1-\lambda)x'\)。真实 numpy。公式 \(f(z)\le\lambda f(x)+(1-\lambda)f(x')\) 只出现一次。

片外说明（不进视频）：[NOTES.md](NOTES.md)

D2L：https://zh.d2l.ai/chapter_optimization/convexity.html

```bash
.venv/bin/manim episodes/11.2/scene.py Episode112 \
  -r 1920,1080 --fps 60 --format mp4
```

成片约 32 秒，H.264，无音轨。MP4 放 GitHub Release，不进 Git。
