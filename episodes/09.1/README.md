# 9.1 门控循环单元（GRU）

机制：更新门 \(Z_t\) 按分量在旧隐状态 \(H_{t-1}\) 与候选 \(\tilde H_t\) 之间做凸组合，得到 \(H_t\)。不训练。

D2L：https://zh.d2l.ai/chapter_recurrent-modern/gru.html

## Render

```bash
python -m manim episodes/09.1/scene.py Episode091 --renderer=cairo \
  -r 1920,1080 --fps 60 --format mp4
```
