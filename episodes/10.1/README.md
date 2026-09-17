# 10.1 注意力提示

机制：查询对键，权重点亮对应的值。热图行是查询、列是键。光晕旅行者是其中一行查询。\(\hat{y}\) 是值的加权和。不训练。不演评分函数。

片外说明（不进视频）：[NOTES.md](NOTES.md)

D2L：https://zh.d2l.ai/chapter_attention-mechanisms/attention-cues.html

## Render

```bash
python -m manim episodes/10.1/scene.py Episode101 \
  -r 1920,1080 --fps 60 --format mp4
```

成片约 32 秒，H.264，无音轨。MP4 放 GitHub Release，不进 Git。
