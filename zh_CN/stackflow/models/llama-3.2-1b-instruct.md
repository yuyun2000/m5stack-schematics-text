
# [Llama-3.2-1B-Instruct](https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct)

## 介绍

Llama 3.2 是一组多语言大语言模型（LLM），包括 1B 和 3B 参数规模的预训练及指令微调生成模型（文本输入/输出）。  
Llama 3.2 的指令微调版本专为多语言对话场景优化，支持如检索增强问答（RAG）、摘要等任务。  
该系列模型在多个行业通用基准测试中超越了大量开源与闭源聊天模型。

## 可用的 NPU 模型

### 基础模型

#### llama3.2-1B-prefill-ax630c

**基础模型** 提供 128 令牌上下文窗口和最多 1,024 个输出令牌。

**支持平台**：LLM630 Compute Kit、Module LLM、Module LLM Kit

- 上下文窗口：128
- 最大输出令牌数：1,024
- 首令牌延迟（ttft）：891ms
- 平均生成速度：4.48 token/s

#### 安装

```shell
apt install llm-model-llama3.2-1b-prefill-ax630c
```

- [下载 llm-model-llama3.2-1b-prefill-ax630c](https://repo.llm.m5stack.com/m5stack-apt-repo/pool/jammy/ax630c/v0.2/llm-model-llama3.2-1B-prefill-ax630c_0.2-m5stack1_arm64.deb)

---

### 长上下文模型

#### llama3.2-1B-p256-ax630c

**长上下文模型** 相较于基础模型提供更大的上下文处理能力，支持 256 令牌上下文窗口。

**支持平台**：LLM630 Compute Kit、Module LLM、Module LLM Kit

- 上下文窗口：256
- 最大输出令牌数：1,024
- 首令牌延迟（ttft）：2601.11ms
- 平均生成速度：4.49 token/s

#### 安装

```shell
apt install llm-model-llama3.2-1b-p256-ax630c
```

- [下载 llm-model-llama3.2-1b-p256-ax630c](https://repo.llm.m5stack.com/m5stack-apt-repo/pool/jammy/ax630c/v0.4/llm-model-llama3.2-1B-p256-ax630c_0.4-m5stack1_arm64.deb)


