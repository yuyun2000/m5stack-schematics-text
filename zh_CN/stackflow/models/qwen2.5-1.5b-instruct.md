# [Qwen2.5-1.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct)

## 介绍

Qwen2.5-1.5B-Instruct 是 Qwen2.5 系列中的一款指令调优语言模型，参数量约为 15.4 亿。该模型的主要特点包括：

- **模型类型**：因果语言模型（Causal Language Model）
- **训练阶段**：预训练和后训练
- **架构**：Transformer，采用 RoPE、SwiGLU、RMSNorm、Attention QKV 偏置及绑定词嵌入
- **参数数量**：15.4 亿（非嵌入参数 13.1 亿）
- **层数**：28 层
- **注意力头数（GQA）**：查询头 12，键值头 2
- **上下文长度**：支持完整 32,768 个 token，上限生成 8,192 个 token

该模型在指令理解、长文本生成以及结构化数据理解方面有显著提升，支持包括英语、中文、法语等 29 种语言的多语言能力。

## 可用的 NPU 模型

### 基础模型

#### qwen2.5-1.5B-ax630c

- 支持 128 长度上下文窗口
- 最长输出 1024 个 token
- 支持平台：LLM630 计算套件、Module LLM 和 Module LLM 套件
- ttft (首次生成时间)：1029.41ms
- 平均生成速度：3.59 token/s

#### 安装

```shell
apt install llm-model-qwen2.5-1.5b-ax630c
```

- [下载 llm-model-qwen2.5-1.5b-ax630c](https://repo.llm.m5stack.com/m5stack-apt-repo/pool/jammy/ax630c/v0.3/llm-model-qwen2.5-1.5B-ax630c_0.3-m5stack1_arm64.deb)

### 长上下文模型

#### qwen2.5-1.5B-p256-ax630c

- 相较基础模型，支持更长上下文窗口
- 256 长度上下文窗口
- 最长输出 1024 个 token
- 支持平台：LLM630 计算套件、Module LLM 和 Module LLM 套件
- ttft：3056.54ms
- 平均生成速度：3.57 token/s

#### 安装

```shell
apt install llm-model-qwen2.5-1.5b-p256-ax630c
```

- [下载 llm-model-qwen2.5-1.5b-p256-ax630c](https://repo.llm.m5stack.com/m5stack-apt-repo/pool/jammy/ax630c/v0.4/llm-model-qwen2.5-1.5B-p256-ax630c_0.4-m5stack1_arm64.deb)

### INT4 量化模型

#### qwen2.5-1.5B-Int4-ax630c

- 相较基础模型，推理速度更快
- 支持 128 长度上下文窗口
- 最长输出 1024 个 token
- 支持平台：LLM630 计算套件、Module LLM 和 Module LLM 套件
- ttft：1219.54ms
- 平均生成速度：4.63 token/s

#### 安装

```shell
apt install llm-model-qwen2.5-1.5b-int4-ax630c
```

- [下载 llm-model-qwen2.5-1.5b-int4-ax630c](https://repo.llm.m5stack.com/m5stack-apt-repo/pool/jammy/ax630c/v0.4/llm-model-qwen2.5-1.5B-Int4-ax630c_0.4-m5stack1_arm64.deb)

#### qwen2.5-1.5B-Int4-ax650

- 相较基础模型，推理速度更快
- 支持 128 长度上下文窗口
- 最长输出 1024 个 token
- 支持平台：AI Pyramid
- ttft：289.06ms
- 平均生成速度：16.77 token/s

#### 安装

```shell
apt install llm-model-qwen2.5-1.5b-int4-ax650
```

- [下载 llm-model-qwen2.5-1.5b-int4-ax650](https://repo.llm.m5stack.com/m5stack-apt-repo/pool/jammy/ax650c/v0.4/llm-model-qwen2.5-1.5B-Int4-ax650_0.4-m5stack1_arm64.deb)