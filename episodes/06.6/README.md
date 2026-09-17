# 6.6 LeNet

机制：同一颗光晕样本走过卷积 → 汇聚 → 卷积 → 汇聚 → 展平 → 全连接。输入是可读的 \(8\times 8\)，不是 \(28\times 28\) 看板。权重随机但写死，不训练，最后停在 logits \(\mathbf{o}\)，不做 softmax，不假装分类对了。

片外说明（不进视频）：[NOTES.md](NOTES.md)

D2L：https://zh.d2l.ai/chapter_convolutional-neural-networks/lenet.html

```bash
.venv/bin/manim episodes/06.6/scene.py Episode066 \
  -r 1920,1080 --fps 60 --format mp4
```

成片约 32 秒，H.264，无音轨。MP4 放 GitHub Release，不进 Git。
