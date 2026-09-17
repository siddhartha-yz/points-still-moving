# 4.8 数值稳定性和模型初始化

机制：sigmoid 把隐层激活堆到 0 或 1 附近，反向 \(|\partial\ell/\partial h|\) 往输入方向缩成短针。同一条仿射+sigmoid 链，不训练，不把 \(W\) 摊在屏幕上。可选的后半拍：更好尺度的初始化把激活拉回斜率还在的区段。

片外说明（不进视频）：[NOTES.md](NOTES.md)

D2L：https://zh.d2l.ai/chapter_multilayer-perceptrons/numerical-stability-and-init.html

## Render

```bash
python -m manim episodes/04.8/scene.py Episode048 \
  -r 1920,1080 --fps 60 --format mp4
```

成片约 32 秒，H.264，无音轨。MP4 放 GitHub Release，不进 Git。
