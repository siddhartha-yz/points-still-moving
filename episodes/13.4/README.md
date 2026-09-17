# 13.4 锚框

机制：一个格子铺出不同形状的锚框，与真框算 \(\mathrm{IoU}=|A\cap y|/|A\cup y|\)。光晕圈住 IoU 更大的那只锚。不训练。

片外说明（不进视频）：[NOTES.md](NOTES.md)

D2L：https://zh.d2l.ai/chapter_computer-vision/anchor.html

## Render

```bash
python -m manim episodes/13.4/scene.py Episode134 \
  -r 1920,1080 --fps 60 --format mp4
```

成片约 28 秒，H.264，无音轨。MP4 放 GitHub Release，不进 Git。
