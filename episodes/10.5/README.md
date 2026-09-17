# 10.5 多头注意力

机制：同一组词元上两个头先各自投影再做注意力，权重图案不同；头拼接后经 \(W_o\) 变回 \(\hat y\)。光晕旅行者是查询。不训练，不演自注意力热图，不演位置编码。

片外说明（不进视频）：[NOTES.md](NOTES.md)

D2L：https://zh.d2l.ai/chapter_attention-mechanisms/multihead-attention.html

```bash
.venv/bin/manim episodes/10.5/scene.py Episode105 \
  -r 1920,1080 --fps 60 --format mp4
```

成片约 32 秒，H.264，无音轨。MP4 放 GitHub Release，不进 Git。
