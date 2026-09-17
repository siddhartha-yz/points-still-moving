# 4.1 多层感知机

机制：一颗 2-D 样本先做 \(z=W_1x+b_1\)（可负），再 \(h=\mathrm{relu}(z)\) 把负数夹成 0，然后 \(o=W_2h+b_2\)。两个隐单元。不训练，不演反向传播，不塞 softmax。

片外说明（不进视频）：[NOTES.md](NOTES.md)

D2L：https://zh.d2l.ai/chapter_multilayer-perceptrons/mlp.html

## Render

```bash
python -m manim episodes/04.1/scene.py Episode041 \
  -r 1920,1080 --fps 60 --format mp4
```

成片约 30 秒，H.264，无音轨。MP4 放 GitHub Release，不进 Git。
