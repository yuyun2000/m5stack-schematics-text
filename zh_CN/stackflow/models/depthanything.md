
# [Depth-Anything](https://github.com/DepthAnything/Depth-Anything-V2)

## 安装说明

DepthAnything 是一款用于图像深度估计的模型，能够生成高质量的深度图，可广泛应用于机器人技术、增强现实和计算机视觉等领域。

## 可用的 NPU 模型

### depth-anything-ax630c

**支持平台**：LLM630 Compute Kit、Module LLM 以及 Module LLM Kit

- 该模型支持深度估计任务，可根据输入图像生成高质量的深度图。

### 安装

```shell
apt install llm-model-depth-anything-ax630c
```

- [下载 llm-model-depth-anything-ax630c](https://repo.llm.m5stack.com/m5stack-apt-repo/pool/jammy/ax630c/v0.4/llm-model-depth-anything-ax630c_0.4-m5stack1_arm64.deb)

### depth-anything-npu1-ax630c

**支持平台**：LLM630 Compute Kit、Module LLM 以及 Module LLM Kit

- 该模型支持深度估计任务，可根据输入图像生成高质量的深度图。此模型支持虚拟 NPU，专供于 LLM630 计算套件搭配具有 AI-ISP 功能的摄像头使用。

### 安装

```shell
apt install llm-model-depth-anything-npu1-ax630c
```

- [下载 llm-model-depth-anything-npu1-ax630c](https://repo.llm.m5stack.com/m5stack-apt-repo/pool/jammy/ax630c/v0.4/llm-model-depth-anything-npu1-ax630c_0.4-m5stack1_arm64.deb)