# 9.2 长短期记忆网络

机制：记忆元 \(\mathbf{C}\) 是一只持久的水库。遗忘门把旧水按 \(F_t\) 放掉，输入门把候选按 \(I_t\) 灌进去：\(\mathbf{C}_t=F_t\odot C_{t-1}+I_t\odot\tilde C_t\)。输出门再放出 \(\mathbf{H}_t\)。不训练。

片外说明（不进视频）：[NOTES.md](NOTES.md)

D2L：https://zh.d2l.ai/chapter_recurrent-modern/lstm.html

## Render

```bash
python -m manim episodes/09.2/scene.py Episode092 \
  -r 1920,1080 --fps 60 --format mp4
```

成片约 31 秒，H.264，无音轨。MP4 放 GitHub Release，不进 Git。
