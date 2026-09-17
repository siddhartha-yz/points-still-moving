# 7.2 使用块的网络（VGG）

机制：同一个卷积块叠两次。块内 \(3\times 3\) 卷积（pad 1）保持高宽，块末 \(2\times 2\) 最大汇聚把高宽减半，通道翻倍 \(c=1\to 2\to 4\)。不训练。不画 VGG-11 的十三层塔。

片外说明（不进视频）：[NOTES.md](NOTES.md)

D2L：https://zh.d2l.ai/chapter_convolutional-modern/vgg.html

## Render

```bash
python -m manim episodes/07.2/scene.py Episode072 \
  -r 1920,1080 --fps 60 --format mp4
```

成片约 30 秒，H.264，无音轨。MP4 放 GitHub Release，不进 Git。
