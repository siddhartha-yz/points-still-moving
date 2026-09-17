# 6.4 多输入多输出通道

机制：两个输入薄片各做一次互相关，再相加成一根输出。\(O_c=\sum_i (X_i * K_{c,i})\)。光晕圈住被写成的那一格。不训练。可选第二拍：两个输出通道叠成两张图。

片外说明（不进视频）：[NOTES.md](NOTES.md)

D2L：https://zh.d2l.ai/chapter_convolutional-neural-networks/channels.html

## Render

```bash
python -m manim episodes/06.4/scene.py Episode064 \
  -r 1920,1080 --fps 60 --format mp4
```

成片约 32 秒，H.264，无音轨。MP4 放 GitHub Release，不进 Git。
