# 8.4 循环神经网络

机制：同一个隐状态 \(h_t=\phi(W_{xh}x_t+W_{hh}h_{t-1}+b)\) 被三个 token 依次改写，旧的 \(h\) 留下淡影与轨迹。光晕在当前 \(x_t\) 上。不训练，不演输出层，不演 BPTT。

片外说明（不进视频）：[NOTES.md](NOTES.md)

D2L：https://zh.d2l.ai/chapter_recurrent-neural-networks/rnn.html

```bash
.venv/bin/manim episodes/08.4/scene.py Episode084 \
  -r 1920,1080 --fps 60 --format mp4
```

成片约 32 秒，H.264，无音轨。MP4 放 GitHub Release，不进 Git。
