# [DeepSeek-R1-Distill-Qwen-1.5B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B)

## 介绍

DeepSeek-R1-Distill-Qwen-1.5B 是在开源模型基础上，通过使用 DeepSeek-R1 生成的样本进行微调的模型，拥有 15 亿参数。该模型的主要特点包括：

- **类型**：因果语言模型（Causal Language Model）
- **训练阶段**：预训练 + 后训练（Pretraining & Post-training）
- **架构**：采用 Transformer，结合 RoPE、SwiGLU、RMSNorm、Attention QKV 偏置以及词嵌入共享
- **参数总数**：15.4 亿（其中非嵌入参数为 13.1 亿）
- **网络层数**：28 层
- **注意力头（GQA）数量**：Q 为 12 个，KV 为 2 个
- **上下文长度**：最多 131,072 tokens，支持生成最多 8,192 tokens

## 可用的 NPU 模型

### 基础模型（Base Model）

**deepseek-r1-1.5B-ax630c**

**基础模型** 提供 128 的上下文窗口，最大输出为 1,024 个 token。

**支持平台**：LLM630 Compute Kit、Module LLM 以及 Module LLM Kit

- 上下文窗口：128
- 最大输出 token 数：1,024
- ttft：1075.04 毫秒
- 平均生成速度：3.57 token/s

#### 安装

```shell
apt install llm-model-deepseek-r1-1.5b-ax630c
```

- [下载 llm-model-deepseek-r1-1.5b-ax630c](https://repo.llm.m5stack.com/m5stack-apt-repo/pool/jammy/ax630c/v0.3/llm-model-deepseek-r1-1.5B-ax630c_0.3-m5stack1_arm64.deb)

### 长上下文模型（Long-Context Model）

**deepseek-r1-1.5B-p256-ax630c**

**长上下文模型** 相较于基础模型，支持更长的上下文，提供 256 的上下文窗口，最大输出仍为 1,024 个 token。

**支持平台**：LLM630 Compute Kit、Module LLM、Module LLM Kit

- 上下文窗口：256
- 最大输出 token 数：1,024
- ttft：3056.86 毫秒
- 平均生成速度：3.57 token/s

#### 安装

```shell
apt install llm-model-deepseek-r1-1.5b-p256-ax630c
```

- [下载 llm-model-deepseek-r1-1.5b-p256-ax630c](https://repo.llm.m5stack.com/m5stack-apt-repo/pool/jammy/ax630c/v0.4/llm-model-deepseek-r1-1.5B-p256-ax630c_0.4-m5stack1_arm64.deb)

