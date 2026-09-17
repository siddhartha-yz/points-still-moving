# 13.3 目标检测和边界框

机制：物体用矩形框住。两角 \((x_1,y_1,x_2,y_2)\) 与中心加宽高 \((c_x,c_y,w,h)\) 在同一只框上互转。光晕旅行者是框的中心。图像坐标：原点左上，\(y\) 向下。

片外说明（不进视频）：[NOTES.md](NOTES.md)

D2L：https://zh.d2l.ai/chapter_computer-vision/bounding-box.html

## Render

```bash
python -m manim episodes/13.3/scene.py Episode133 \
  -r 1920,1080 --fps 60 --format mp4
```

成片约 27 秒，H.264，无音轨。MP4 放 GitHub Release，不进 Git。
