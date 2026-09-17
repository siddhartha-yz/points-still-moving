# 14.1 词嵌入（word2vec）

机制：跳元。中心词向量 \(\mathbf{v}_c\) 拉近窗口内上下文 \(\mathbf{u}_o\)；独热彼此正交。四个 2-D 词向量，只训一对 \((c,o)\)。光晕旅行者是中心词。

片外说明（不进视频）：[NOTES.md](NOTES.md)

D2L：https://zh.d2l.ai/chapter_natural-language-processing-pretraining/word2vec.html

```bash
.venv/bin/manim episodes/14.1/scene.py Episode141 \
  -r 1920,1080 --fps 60 --format mp4 --renderer=cairo
```

成片约 32 秒，H.264，无音轨。MP4 放 GitHub Release，不进 Git。
