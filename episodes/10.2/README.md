# 10.2 注意力汇聚：Nadaraya-Watson 核回归

机制：查询越靠近哪个键，那个值的权重越大；\(\hat{y}\) 是值的加权和。光晕旅行者是查询 \(q\)。高斯核 softmax，和为 1。不训练，这条曲线就是估计器。

片外说明（不进视频）：[NOTES.md](NOTES.md)

D2L：https://zh.d2l.ai/chapter_attention-mechanisms/nadaraya-waston.html

## Render

```bash
python -m manim episodes/10.2/scene.py Episode102 \
  -r 1920,1080 --fps 60 --format mp4
```

成片约 27 秒，H.264，无音轨。MP4 放 GitHub Release，不进 Git。
