# 点还在动

D2L 无声可视化。B 站系列名 **点还在动**，副标题 **D2L 无声可视化**。

素材与章节顺序跟 [《动手学深度学习》中文版](https://zh.d2l.ai/) 走。观众是已经读过对应小节的初学者，不是零基础。片内不讲课：没有旁白、没有中文句子、没有「这里是 softmax」。只有符号、维数、正在变化的数，以及半秒章节号。

## 约定

- 一集一个机制，约 20–40 秒，1920×1080，60 fps，静音。
- 默剧主角是同一颗带光晕的样本 \(\mathbf{x}\)：连续的是视觉身份，不是同一个数据集故事。3.1 的 \(y\) 是标量，3.4 的 \(y\) 是独热；看过 D2L 的人知道这不是同一道题。
- 点云颜色表示原始分组，不伪装成分类结果。网络不必是训练好的，除非那一集的机制就是训练。
- 单集自洽。连看时能认出同一颗光晕点。简介写 D2L 链接，不写「请先看上一集」。
- 正片在 `episodes/`。`experiments/` 是技法试验，不进系列目录。
- 成片 MP4 放 GitHub Release，不进 Git 历史。

## 试点（尚未制作）

| 集 | D2L | 机制 |
| --- | --- | --- |
| `episodes/03.1` | [3.1 线性回归](https://zh.d2l.ai/chapter_linear-networks/linear-regression.html) | 直线用小批量 SGD 在点里找位置；高亮样本的残差缩短；留下噪声残差 |
| `episodes/03.4` | [3.4 softmax回归](https://zh.d2l.ai/chapter_linear-networks/softmax-regression.html) | 前向 \(\mathbf{o}=W\mathbf{x}+b\) → softmax；分数可负，概率非负且和为 1；不塞交叉熵、不假装已训练 |

从第 3 章重走。第 1–2 章和「从零实现」小节不做正片。现有 2→2→2 前向片在 `experiments/`，更接近 4.1 的一小段，只当技法试验。

## 渲染

```bash
sudo apt-get install -y $(cat apt-packages.txt)
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

成片参数：`-r 1920,1080 --fps 60 --format mp4`。

## 许可

MIT。内容结构对齐 D2L，动画是独立的无声可视化，不是教材再版。
