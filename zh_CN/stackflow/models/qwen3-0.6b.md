# [Qwen3-0.6B](https://huggingface.co/Qwen/Qwen3-0.6B)

## 介绍

Qwen3 是 Qwen 系列最新的大型语言模型，提供稠密（Dense）和专家混合（Mixture-of-Experts, MoE）两种架构。它支持在思考模式和非思考模式之间无缝切换，具备增强的推理和指令跟随能力，拥有优越的人类偏好对齐以实现更自然的对话，支持强大的代理能力以集成各种工具，并支持超过 100 种语言，表现出色的多语言能力。

- **模型类型**：因果语言模型（Causal Language Model）
- **训练阶段**：预训练和后训练
- **参数数量**：6 亿（其中非嵌入层参数 4.4 亿）
- **层数**：28 层
- **注意力头数（GQA）**：查询头 16，键值头 8
- **上下文长度**：32,768

## 可用的 NPU 模型

### 基础模型

#### qwen3-0.6B-ax630c

- 提供 128 长度上下文窗口
- 最长输出 1024 个 token
- 支持平台：LLM630 计算套件、Module LLM 和 Module LLM 套件
- 运行时间（ttft）约 361.81ms
- 平均生成速度约 10.28 token/s

### 安装

```shell
apt install llm-model-qwen3-0.6b-ax630c
```

- [下载 llm-model-qwen3-0.6B-ax630c](https://repo.llm.m5stack.com/m5stack-apt-repo/pool/jammy/ax630c/v0.4/llm-model-qwen3-0.6B-ax630c_0.4-m5stack1_arm64.deb)