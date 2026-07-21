
# [SmolVLM-500M-Instruct](https://huggingface.co/HuggingFaceTB/SmolVLM-500M-Instruct)

## 介绍

SmolVLM-500M 是 SmolVLM 系列中的一个小型多模态模型。它可以接受任意序列的图像和文本输入，输出文本结果。  
该模型注重效率，能够回答有关图像的问题、描述视觉内容或转录文本。  
其轻量级架构使其适合在设备端运行，同时在多模态任务中保持较强性能。  
推理时对显存需求较低，仅需约1.23GB GPU显存即可处理一张图像。

## 可用的 NPU 模型

### 基础模型

#### smolvlm-500M-ax630c

- 提供 128 长度的上下文窗口  
- 最大输出 1,024 个 token  
- 支持平台：LLM630 计算套件、Module LLM 和 Module LLM 套件  
- 首次推理时间（ttft）：365.69 毫秒  
- 平均生成速度：13.14 token/s  
- 图像编码尺寸：512×512  
- 图像编码时间：838.30 毫秒

### 安装

```shell
apt install llm-model-smolvlm-500m-ax630c
```

- [下载 llm-model-smolvlm-500m-ax630c](https://repo.llm.m5stack.com/m5stack-apt-repo/pool/jammy/ax630c/v0.4/llm-model-smolvlm-500M-ax630c_0.4-m5stack1_arm64.deb)

```
