# 10.6 自注意力和位置编码

机制：四个词元同时当 \(q,k,v\)。光晕旅行者作为查询，对全部键做 \(\alpha=\mathrm{softmax}(qk^{\top}/\sqrt{d})\)，\(\hat y\) 是加权后的值。右侧 \(4\times 4\) 热图用透明度表示全部查询的权重，不是数字表。不训练。不演位置编码。

片外说明（不进视频）：[NOTES.md](NOTES.md)

D2L：https://zh.d2l.ai/chapter_attention-mechanisms/self-attention-and-positional-encoding.html

## Render

```bash
python -m manim episodes/10.6/scene.py Episode106 \
  -r 1920,1080 --fps 60 --format mp4
```

成片约 30 秒，H.264，无音轨。MP4 放 GitHub Release，不进 Git。
