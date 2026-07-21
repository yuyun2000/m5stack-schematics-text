# [InternVL3-1B](https://huggingface.co/OpenGVLab/InternVL3-1B)

## 介绍

InternVL3 是一款先进的多模态大语言模型（MLLM）系列，展现出卓越的整体性能。与 InternVL 2.5 相比，InternVL3 在多模态感知与推理能力方面表现更为出色，同时进一步扩展了其多模态能力，涵盖工具使用、GUI 智能体、工业图像分析、三维视觉感知等多个方向。

## 可用的 NPU 模型

### 基础模型（Base Model）

#### internvl3-1B-448-ax630c

**基础模型** 提供 1024 的上下文窗口，最大可输出 1280 个 token。

**支持平台**：LLM630 Compute Kit、Module LLM 以及 Module LLM Kit

- 上下文窗口：1024
- 最大输出 token 数：1280
- 首次生成延迟（ttft）：534.95 毫秒
- 平均生成速度：9.78 token/s
- 图像编码尺寸：448×448
- 图像编码时间：2267.89 毫秒

### 安装

```shell
apt install llm-model-internvl3-1b-448-ax630c
```

- [下载 llm-model-internvl3-1b-448-ax630c](https://repo.llm.m5stack.com/m5stack-apt-repo/pool/jammy/ax630c/v0.6/llm-model-internvl3-1B-448-ax630c_0.6-m5stack1_arm64.deb)

#### internvl3-1B-448-ax650

**基础模型** 提供 2048 的上下文窗口，最大可输出 2048 个 token。

**支持平台**：AI Pyramid

- 上下文窗口：2048
- 最大输出 token 数：2048
- 首次生成延迟（ttft）： 142.32 毫秒
- 平均生成速度： 26.67 token/s
- 图像编码尺寸：448×448
- 图像编码时间： 393.08 毫秒

### 安装

```shell
apt install llm-model-internvl3-1b-448-ax630c
```

- [下载 llm-model-internvl3-1b-448-ax630c](https://repo.llm.m5stack.com/m5stack-apt-repo/pool/jammy/ax630c/v0.6/llm-model-internvl3-1B-448-ax630c_0.6-m5stack1_arm64.deb)