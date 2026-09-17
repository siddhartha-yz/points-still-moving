# 7.6 残差网络

机制：残差块。主路两段仿射得到 \(F(x)\)，捷径把 \(x\) 绕开 \(F\) 抄过来，相加后再 ReLU：\(y=\mathrm{relu}(F(x)+x)\)。\(F(x)\) 接近 0 时 \(y\) 贴着 \(x\)。不训练。

片外说明（不进视频）：[NOTES.md](NOTES.md)

D2L：https://zh.d2l.ai/chapter_convolutional-modern/resnet.html

```bash
.venv/bin/manim episodes/07.6/scene.py Episode076 \
  -r 1920,1080 --fps 60 --format mp4
```

成片约 33 秒，H.264，无音轨。MP4 放 GitHub Release，不进 Git。
