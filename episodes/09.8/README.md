# 9.8 束搜索

机制：每步只留束宽 \(k\) 条候选，其余剪掉。贪心是 \(k=1\)。同一张分数表左右对照 \(k=1\) 与 \(k=2\)，剪枝可见。光晕是 \(k=2\) 上活下来的那条束。公式只出现一次。

片外说明（不进视频）：[NOTES.md](NOTES.md)

D2L：https://zh.d2l.ai/chapter_recurrent-modern/beam-search.html

```bash
.venv/bin/manim episodes/09.8/scene.py Episode098 \
  -r 1920,1080 --fps 60 --format mp4
```

成片约 32 秒，H.264，无音轨。MP4 放 GitHub Release，不进 Git。
