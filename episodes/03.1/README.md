# 3.1 线性回归

机制：直线用小批量 SGD 在点里找位置。高亮样本的残差线段缩短，最后留下与观测噪声一致的残差。不演解析解，不演损失曲面。

片外说明（不进视频）：[NOTES.md](NOTES.md)。B 站简介可直接从该文件末段复制。

D2L：https://zh.d2l.ai/chapter_linear-networks/linear-regression.html

`scene.py` 是点、噪声、SGD 轨迹、直线和屏幕数值的唯一计算来源。18 次更新，`|B| = 4`，`η = 0.035`。

```bash
.venv/bin/manim episodes/03.1/scene.py Episode031 \
  -r 1920,1080 --fps 60 --format mp4
```

成片约 24 秒，H.264，无音轨。MP4 放 GitHub Release，不进 Git。
