
# [Qwen2.5-HA-0.5B-Instruct](https://huggingface.co/yunyu1258/qwen2.5-0.5b-ha)

## 介绍

Qwen2.5-HA-0.5B-Instruct 是基于 Qwen2.5-0.5B-Instruct 微调的智能家居模型，参数量约为 5 亿。该模型的主要特点包括：

- **模型类型**：因果语言模型（Causal Language Model）
- **训练阶段**：预训练和后训练
- **架构**：Transformer，采用 RoPE、SwiGLU、RMSNorm、Attention QKV 偏置及绑定词嵌入
- **参数数量**：4.9 亿（非嵌入参数 3.6 亿）
- **层数**：24 层
- **注意力头数（GQA）**：查询头 14，键值头 2
- **上下文长度**：支持完整 32,768 个 token，上限生成 8,192 个 token

该模型在指令理解、长文本生成以及结构化数据理解方面有显著提升，支持包括英语、中文、法语等 29 种语言的多语言能力。该模型经过智能家居数据集微调，设置系统提示词即可结构化输出。

## 可用的 NPU 模型

### Home Assistant 微调模型

#### qwen2.5-ha-0.5b-ctx-ax630c

- 相较基础模型，提供更长上下文，稳定结构化输出 Home Assistant 专用的 json 格式数据
- 支持 1024 长度上下文窗口
- 最长输出 1280 个 token
- 支持平台：LLM630 计算套件、Module LLM 和 Module LLM 套件
- ttft：533.19ms
- 平均生成速度：9.76 token/s

#### 安装

```bash
apt install llm-model-qwen2.5-0.5b-int4-ax630c
```

- [下载 llm-model-qwen2.5-0.5b-int4-ax630c](https://repo.llm.m5stack.com/m5stack-apt-repo/pool/jammy/ax630c/v0.4/llm-model-qwen2.5-0.5B-Int4-ax630c_0.4-m5stack1_arm64.deb)

#### qwen2.5-ha-0.5b-ctx-ax650

- 相较基础模型，提供更长上下文，稳定结构化输出 Home Assistant 专用的 json 格式数据
- 支持 1024 长度上下文窗口
- 最长输出 1280 个 token
- 支持平台：AI Pyramid
- ttft：143.02ms
- 平均生成速度：25.5 token/s

#### 安装

```bash
apt install llm-model-qwen2.5-ha-0.5b-ctx-ax650
```

- [下载 llm-model-qwen2.5-ha-0.5b-ctx-ax650](https://repo.llm.m5stack.com/m5stack-apt-repo/pool/jammy/ax650c/v0.6/llm-model-qwen2.5-HA-0.5B-ctx-ax650_0.6-m5stack1_arm64.deb)