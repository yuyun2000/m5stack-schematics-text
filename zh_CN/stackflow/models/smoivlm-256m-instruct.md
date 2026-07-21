# [SmolVLM-256M-Instruct](https://huggingface.co/HuggingFaceTB/SmolVLM-256M-Instruct)

## 介绍

SmolVLM-256M 是全球最小的多模态模型。它可以接受任意序列的图像和文本输入，输出文本结果。\
该模型注重效率，能够回答有关图像的问题、描述视觉内容或转录文本。\
其轻量级架构使其适合在设备端运行，同时在多模态任务中保持较强性能。\
推理时对显存需求低于 1GB GPU 显存即可处理一张图像。

## 可用的 NPU 模型

### 基础模型

#### smolvlm-256M-ax630c

- 提供 128 长度的上下文窗口
- 最大输出 1,024 个 token
- 支持平台：LLM630 计算套件、Module LLM 和 Module LLM 套件
- 首次推理时间（ttft）：185.75 毫秒
- 平均生成速度：30.16 token/s
- 图像编码尺寸：512×512
- 图像编码时间：799.11 毫秒

### 安装

```shell
apt install llm-model-smolvlm-256m-ax630c
```

- [下载 llm-model-smolvlm-256m-ax630c](https://repo.llm.m5stack.com/m5stack-apt-repo/pool/jammy/ax630c/v0.4/llm-model-smolvlm-256M-ax630c_0.4-m5stack1_arm64.deb)
