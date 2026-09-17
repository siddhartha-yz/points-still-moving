# 10.3 注意力评分函数

机制：同一组 \(q,k,v\) 上两种评分 \(a(q,k)\)。先 \(a\) 再 softmax 成权重，再加权求和。加性与缩放点积给出两套不同的 \(\alpha\)。光晕旅行者是查询。不训练。

片外说明（不进视频）：[NOTES.md](NOTES.md)

D2L：https://zh.d2l.ai/chapter_attention-mechanisms/attention-scoring-functions.html

## Render

```bash
python -m manim episodes/10.3/scene.py Episode103 \
  --renderer cairo -r 1920,1080 --fps 60 --format mp4
```

成片约 38 秒，H.264，无音轨。MP4 放 GitHub Release，不进 Git。
