# 6.5 汇聚层

机制：\(2\times 2\) 窗口在 \(4\times 4\) 图上按步幅 2 滑动。先最大汇聚（窗口里只留赢家，输出格写下 `max`），再同一组窗口做平均汇聚（四格都亮，输出格写下 `avg`）。分辨率从 \(4\times 4\) 掉到 \(2\times 2\)。不训练，没有可学参数。

片外说明（不进视频）：[NOTES.md](NOTES.md)

D2L：https://zh.d2l.ai/chapter_convolutional-neural-networks/pooling.html

```bash
.venv/bin/manim episodes/06.5/scene.py Episode065 \
  -r 1920,1080 --fps 60 --format mp4
```

成片约 28 秒，H.264，无音轨。MP4 放 GitHub Release，不进 Git。
