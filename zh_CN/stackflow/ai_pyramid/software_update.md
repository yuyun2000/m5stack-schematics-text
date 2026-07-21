# AI Pyramid 软件包更新

## 1. 准备工作

出厂镜像已经预置 M5Stack APT 源，如需手动添加。参考以下步骤。

```bash
wget -qO /etc/apt/keyrings/StackFlow.gpg https://repo.llm.m5stack.com/m5stack-apt-repo/key/StackFlow.gpg
echo 'deb [arch=arm64 signed-by=/etc/apt/keyrings/StackFlow.gpg] https://repo.llm.m5stack.com/m5stack-apt-repo jammy ax650c' > /etc/apt/sources.list.d/StackFlow.list
```

## 2. 更新软件源

#### 步骤 1：更新软件列表

执行 "apt update" 更新软件列表：

```bash
apt update
```

## 3. 安装软件包

#### 步骤 1：查看可用软件包

查看可用 llm deb 包列表。其中以`llm-model-name`格式命名的为模型包，以`llm-name`命名的为功能单元包。

```bash
apt list | grep llm-
```

#### 步骤 2：安装所需软件包

根据需求使用 apt 指令安装软件包， 如安装 llm-cosy-voice 包。注意：模型将占用较大空间，建议按需安装。

```bash
apt install llm-cosy-voice
```

## 4. 软件包说明

### lib-llm

- 提供软件运行所需的环境。

```shell
apt install lib-llm
```

### llm-sys

- 提供 StackFlow 的基础服务。

```shell
apt install llm-sys
```

## 5. 功能模块介绍

### llm-audio

- 提供统一的声卡管理服务。

```shell
apt install llm-audio
```

### llm-camera

- 提供统一的摄像头管理服务。

```shell
apt install llm-camera
```

### llm-kws

- 提供关键词检测服务。

```shell
apt install llm-kws
```

### llm-asr

- 提供文本转语音服务

```shell
apt install llm-asr
```

### llm-llm

- 提供本地大模型服务。

```shell
apt install llm-llm
```

- [下载 llm-llm deb](https://repo.llm.m5stack.com/m5stack-apt-repo/pool/jammy/ax630c/v1.9/llm-llm_1.9-m5stack1_arm64.deb)

### llm-vlm

- 提供本地多模态大模型服务。

```shell
apt install llm-vlm
```

### llm-melotts

- 提供文本转语音服务。

```shell
apt install llm-melotts
```

### llm-cosy-voice

- 提供音色克隆及文本转语音服务。

```shell
apt install llm-cosy-voice
```

### llm-openai-api

- 提供兼容 OpenAI 的 API 服务，可用于 STT, TTS, LLM/VLM 的快速调用。 

```shell
apt install llm-openai-api
```