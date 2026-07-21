# [InternVL2_5-1B-MPO](https://huggingface.co/OpenGVLab/InternVL2_5-1B-MPO)

## 介绍

InternVL 2.5 是一款多模态大语言模型（MLLM）系列，基于 InternVL 2.0 构建，在保留核心模型架构的基础上，在训练策略、测试方法和数据质量方面进行了显著优化。

## 可用的 NPU 模型

### 基础模型（Base Model）

#### internvl2.5-1B-364-ax630c

**基础模型** 提供 256 的上下文窗口，最大可输出 1,024 个 token。

**支持平台**：LLM630 Compute Kit、Module LLM 以及 Module LLM Kit

- 上下文窗口：256
- 最大输出 token 数：1,024
- 首次生成延迟（ttft）：1117.27 毫秒
- 平均生成速度：10.56 token/s
- 图像编码尺寸：364×364
- 图像编码时间：1164.61 毫秒

### 安装

```shell
apt install llm-model-internvl2.5-1b-364-ax630c
```

- [下载 llm-model-internvl2.5-1b-364-ax630c](https://repo.llm.m5stack.com/m5stack-apt-repo/pool/jammy/ax630c/v0.4/llm-model-internvl2.5-1B-364-ax630c_0.4-m5stack1_arm64.deb)

#### internvl2.5-1B-448-ax650

**基础模型** 提供 320 的上下文窗口，最大可输出 1,024 个 token。

**支持平台**：AI Pyramid

- 上下文窗口：320
- 最大输出 token 数：1,024
- 首次生成延迟（ttft）：433.87 毫秒
- 平均生成速度：29.48 token/s
- 图像编码尺寸：448×448
- 图像编码时间：362.22 毫秒

### 安装

```shell
apt install llm-model-internvl2.5-1b-448-ax650
```

- [下载 llm-model-internvl2.5-1b-448-ax650](https://repo.llm.m5stack.com/m5stack-apt-repo/pool/jammy/ax650c/v0.4/llm-model-internvl2.5-1B-448-ax650_0.4-m5stack1_arm64.deb)