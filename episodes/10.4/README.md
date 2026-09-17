# 10.4 Bahdanau 注意力

机制：解码器当前隐状态 \(s_{t'-1}\) 当查询，编码器各步 \(h_t\) 当键和值。注意力对齐源序列，上下文 \(c_{t'}=\sum_t\alpha(s_{t'-1},h_t)h_t\)。光晕旅行者是查询。加性评分，未训练。三步编码器、两步解码器。

片外说明（不进视频）：[NOTES.md](NOTES.md)

D2L：https://zh.d2l.ai/chapter_attention-mechanisms/bahdanau-attention.html

## Render

```bash
python -m manim episodes/10.4/scene.py Episode104 \
  -r 1920,1080 --fps 60 --format mp4
```

成片约 32 秒，H.264，无音轨。MP4 放 GitHub Release，不进 Git。
