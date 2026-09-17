# 7.5 批量规范化

机制：一小批点减均值、除标准差，得到 \(\hat x\)；先 \(\gamma=1,\beta=0\) 让旅行者停在 0，再做一次固定的 \(\gamma\odot\hat x+\beta\)。不训练，不演移动平均，不摊 4-D 张量。

片外说明（不进视频）：[NOTES.md](NOTES.md)

D2L：https://zh.d2l.ai/chapter_convolutional-modern/batch-norm.html

## Render

```bash
python -m manim episodes/07.5/scene.py Episode075 \
  -r 1920,1080 --fps 60 --format mp4
```

成片约 32 秒，H.264，无音轨。MP4 放 GitHub Release，不进 Git。
