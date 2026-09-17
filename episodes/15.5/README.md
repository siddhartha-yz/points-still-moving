# 15.5 自然语言推断：使用注意力

机制：前提每个词查询假设的键。光晕旅行者是一个前提词元，对三个假设键做 \(\alpha=\mathrm{softmax}(a B^{\top}/\sqrt{d})\)，\(\beta\) 是加权后的假设，再由对齐得到未训练的三向分数 \(e/c/n\)。不训练。不摊 \(W\)。

片外说明（不进视频）：[NOTES.md](NOTES.md)

D2L：https://zh.d2l.ai/chapter_natural-language-processing-applications/natural-language-inference-attention.html

## Render

```bash
python -m manim episodes/15.5/scene.py Episode155 \
  -r 1920,1080 --fps 60 --format mp4
```

成片约 31 秒，H.264，无音轨。MP4 放 GitHub Release，不进 Git。
