# 13.5 多尺度目标检测

机制：粗特征图放大感受野、细特征图盯小物体；两层格子同时铺锚。同一张图上 \(4\times 4\)（\(s=0.15\)）打中小物体，\(2\times 2\)（\(s=0.40\)）打不中。光晕旅行者是那颗小物体。不训练。形状只出现一次。

片外说明（不进视频）：[NOTES.md](NOTES.md)

D2L：https://zh.d2l.ai/chapter_computer-vision/multiscale-object-detection.html

```bash
.venv/bin/manim docs/episodes/13.5/scene.py Episode135 \
  --renderer cairo -r 1920,1080 --fps 60 --format mp4
```

成片约 32 秒，H.264，无音轨。MP4 放 GitHub Release，不进 Git。
