
# [openbuddy-llama3.2-1b-v23.1-131k](https://huggingface.co/OpenBuddy/openbuddy-llama3.2-1b-v23.1-131k)

## 介绍

OpenBuddy 是一款面向全球用户的强大开源多语言聊天机器人模型，重点支持对话式 AI 和无缝的多语言交互，包括英语、中文等多种语言。

该模型基于 Tii 的 Falcon 和 Facebook 的 LLaMA 模型，经过微调，扩展了词汇表，添加了更多常用字符，并增强了词嵌入表现。结合多轮对话数据集训练，OpenBuddy 能够回答问题并执行多语言翻译任务，表现稳定可靠。

## 可用 NPU 模型

### 基础模型

#### openbuddy-llama3.2-1B-ax630c

- 128 上下文窗口
- 最长输出 1,024 个 token
- 支持平台：LLM630 计算套件、Module LLM 和 Module LLM 套件
- ttft（首次生成时间）：891.02ms
- 平均生成速度：4.52 token/s

### 安装

```bash
apt install llm-model-openbuddy-llama3.2-1b-ax630c
```

- [下载 llm-model-openbuddy-llama3.2-1B-ax630c](https://repo.llm.m5stack.com/m5stack-apt-repo/pool/jammy/ax630c/v0.2/llm-model-openbuddy-llama3.2-1B-ax630c_0.2-m5stack1_arm64.deb)

```
