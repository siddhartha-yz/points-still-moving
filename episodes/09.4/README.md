# 9.4 双向循环神经网络

机制：前向 \(\overrightarrow h_t\) 与后向 \(\overleftarrow h_t\) 在每个时间步拼接。短序列先左到右、再右到左，然后在一个 \(t\) 上收成光晕向量 \(H_t=[\overrightarrow h_t,\overleftarrow h_t]\)。不训练，不演输出层。

片外说明（不进视频）：[NOTES.md](NOTES.md)

D2L：https://zh.d2l.ai/chapter_recurrent-modern/bi-rnn.html

```bash
.venv/bin/manim episodes/09.4/scene.py Episode094 \
  -r 1920,1080 --fps 60 --format mp4 --renderer cairo
```

成片约 30 秒，H.264，无音轨。MP4 放 GitHub Release，不进 Git。
