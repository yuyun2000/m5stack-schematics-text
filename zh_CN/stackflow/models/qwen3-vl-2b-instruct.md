# [Qwen3-VL-2B-Instruct](https://huggingface.co/Qwen/Qwen3-VL-2B-Instruct)

## 介绍

Qwen3-VL 是 Qwen 系列中最强大的视觉语言模型。这一代实现了全方位升级：更出色的文本理解与生成能力、更深入的视觉感知与推理能力、更长的上下文长度、更强的空间与视频动态理解能力，以及更强大的智能体交互能力。

## 可用的 NPU 模型

### INT4 量化模型

#### qwen3-vl-2b-int4-ax650

- 提供 1152 长度上下文窗口
- 最长输出 2048 个 token
- 支持平台：AI Pyramid
- 运行时间（ttft）约 159.79ms
- 平均生成速度约 11.93 token/s
- 图像编码尺寸：384×384
- 图像编码时间：190.73 毫秒

### 安装

```shell
apt install llm-model-qwen3-vl-2b-int4-ax650
```

- [下载 llm-model-qwen3-vl-2b-int4-ax650](https://repo.llm.m5stack.com/m5stack-apt-repo/pool/jammy/ax650c/v0.5/llm-model-qwen3-vl-2B-Int4-ax650_0.5-m5stack1_arm64.deb)