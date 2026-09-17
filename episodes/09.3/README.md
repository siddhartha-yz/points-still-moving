# 9.3 深度循环神经网络

机制：隐状态同时交给下一时间步和下一层。\(H_t^{(l)}\) 吃 \(H_t^{(l-1)}\) 和 \(H_{t-1}^{(l)}\)。两层 × 三个时间步。光晕旅行者是上层那一个单元。不训练。公式只出现一次。

片外说明（不进视频）：[NOTES.md](NOTES.md)

D2L：https://zh.d2l.ai/chapter_recurrent-modern/deep-rnn.html

```bash
.venv/bin/manim docs/episodes/09.3/scene.py Episode093 \
  --renderer cairo -r 1920,1080 --fps 60 --format mp4
```

成片约 32 秒，H.264，无音轨。MP4 放 GitHub Release，不进 Git。
