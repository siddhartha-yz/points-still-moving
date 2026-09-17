# 5.1 层和块

机制：层套进 Sequential 块。光晕旅行者 \(\mathbf{x}\) 走进外盒，在每个内盒被改写，再带着 \(\mathbf{o}\) 离开。不训练。

片外说明（不进视频）：[NOTES.md](NOTES.md)

D2L：https://zh.d2l.ai/chapter_deep-learning-computation/model-construction.html

## Render

```bash
python -m manim episodes/05.1/scene.py Episode051 \
  -r 1920,1080 --fps 60 --format mp4
```

成片约 31 秒，H.264，无音轨。MP4 放 GitHub Release，不进 Git。
