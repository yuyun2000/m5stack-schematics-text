# [Qwen2.5-Coder-0.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-0.5B-Instruct)

## 介绍

Qwen2.5-Coder-0.5B-Instruct 是专注于代码的 Qwen 大语言模型，在 **代码生成**、**代码推理** 和 **代码修复** 方面有显著提升。该模型的主要特点包括：

- **模型类型**：因果语言模型（Causal Language Model）
- **训练阶段**：预训练和后训练
- **架构**：采用 Transformer，包含 RoPE、SwiGLU、RMSNorm、Attention QKV 偏置及绑定词嵌入
- **参数数量**：4.9 亿（非嵌入参数 3.6 亿）
- **层数**：24 层
- **注意力头数（GQA）**：查询头 14，键值头 2
- **上下文长度**：完整支持 32,768 个 token，上限生成 8,192 个 token

## 可用的 NPU 模型

### 基础模型

#### qwen2.5-coder-0.5b-ax630c

- 提供 128 长度上下文窗口
- 最长输出 1024 个 token
- 支持平台：LLM630 计算套件、Module LLM 和 Module LLM 套件

### 安装

```shell
apt install llm-model-qwen2.5-coder-0.5b-ax630c
```

- [下载 llm-model-qwen2.5-coder-0.5b-ax630c](https://repo.llm.m5stack.com/m5stack-apt-repo/pool/jammy/ax630c/v0.2/llm-model-qwen2.5-coder-0.5B-ax630c_0.2-m5stack1_arm64.deb)
