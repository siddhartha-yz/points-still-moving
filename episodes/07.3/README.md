# 7.3 网络中的网络（NiN）

机制：\(1\times 1\) 卷积当逐像素 MLP（通道混合，空间尺寸不变），再全局平均汇聚压成类别向量。光晕先圈住一个空间格，再落到一个类别 logit。不训练。

片外说明（不进视频）：[NOTES.md](NOTES.md)

D2L：https://zh.d2l.ai/chapter_convolutional-modern/nin.html

## Render

```bash
python -m manim episodes/07.3/scene.py Episode073 \
  -r 1920,1080 --fps 60 --format mp4
```

成片约 32 秒，H.264，无音轨。MP4 放 GitHub Release，不进 Git。
