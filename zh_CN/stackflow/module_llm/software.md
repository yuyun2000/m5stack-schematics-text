# Module LLM 软件包更新

\#> 软件包更新 | 用于应用程序安装和升级，使用 apt 软件包管理工具下载和更新功能单元，具体请参考以下操作。

## 1. 准备工作

- 参考 [Module LLM - Config](/zh_CN/stackflow/module_llm/config)教程，学习如何为 Module LLM 配置网络与文件传输。并通过 ADB / UART / SSH 等方式访问设备终端。

## 2. 更新软件源

1\. 复制以下指令，添加 GPG 密钥并将 M5Stack 的软件源信息添加到系统的软件源列表中。

```bash
wget -qO /etc/apt/keyrings/StackFlow.gpg https://repo.llm.m5stack.com/m5stack-apt-repo/key/StackFlow.gpg
echo 'deb [arch=arm64 signed-by=/etc/apt/keyrings/StackFlow.gpg] https://repo.llm.m5stack.com/m5stack-apt-repo jammy ax630c' > /etc/apt/sources.list.d/StackFlow.list
```

2\. 执行 apt update 命令来更新软件包索引。

```bash
apt update
```

## 3. 安装软件包

1. 查看可用 llm deb 包列表。其中以`llm-model-name`格式命名的为模型包，以`llm-name`命名的为功能单元包。

```bash
apt list | grep llm
```

2. 根据需求使用 apt 指令安装软件包， 如安装 llm-whisper 包。注意：模型将占用较大空间，建议按需安装。

```bash
apt install llm-whisper
```

有关软件包详细信息可访问[StackFlow Github](https://github.com/m5stack/StackFlow/tree/dev/projects/llm_framework)软件包列表查看。其中包含模型配置 json 文件，将展示该模型来源 (homepage)，功能与数据格式。

## 4. 依赖包介绍

### lib-llm

- 提供软件运行所需的环境。

```shell
apt install lib-llm
```

- [下载 lib-llm deb](https://repo.llm.m5stack.com/m5stack-apt-repo/pool/jammy/ax630c/v1.8/lib-llm_1.8-m5stack1_arm64.deb)

### llm-sys

- 提供 StackFlow 的基础功能。

```shell
apt install llm-sys
```

- [下载 llm-sys deb](https://repo.llm.m5stack.com/m5stack-apt-repo/pool/jammy/ax630c/v1.6/llm-sys_1.6-m5stack1_arm64.deb)

## 5. 功能模块介绍

### llm-audio

- 提供统一的声卡管理。

```shell
apt install llm-audio
```

- [下载 llm-audio deb](https://repo.llm.m5stack.com/m5stack-apt-repo/pool/jammy/ax630c/v1.6/llm-audio_1.6-m5stack1_arm64.deb)

### llm-camera

- 提供统一的摄像头管理。

```shell
apt install llm-camera
```

- [下载 llm-camera deb](https://repo.llm.m5stack.com/m5stack-apt-repo/pool/jammy/ax630c/v1.9/llm-camera_1.9-m5stack1_arm64.deb)

### llm-kws

- 提供关键词检测功能。

```shell
apt install llm-kws
```

- [下载 llm-kws deb](https://repo.llm.m5stack.com/m5stack-apt-repo/pool/jammy/ax630c/v1.9/llm-kws_1.9-m5stack1_arm64.deb)

### llm-vad

- 提供语音活动检测功能。

```shell
apt install llm-vad
```

- [下载 llm-vad deb](https://repo.llm.m5stack.com/m5stack-apt-repo/pool/jammy/ax630c/v1.8/llm-vad_1.8-m5stack1_arm64.deb)

### llm-asr

- 提供自动语音识别功能。

```shell
apt install llm-asr
```

- [下载 llm-asr deb](https://repo.llm.m5stack.com/m5stack-apt-repo/pool/jammy/ax630c/v1.7/llm-asr_1.7-m5stack1_arm64.deb)

### llm-whisper

- 提供语音转文本功能。

```shell
apt install llm-whisper
```

- [下载 llm-whisper deb](https://repo.llm.m5stack.com/m5stack-apt-repo/pool/jammy/ax630c/v1.8/llm-whisper_1.8-m5stack1_arm64.deb)

### llm-llm

- 提供文本生成能力。

```shell
apt install llm-llm
```

- [下载 llm-llm deb](https://repo.llm.m5stack.com/m5stack-apt-repo/pool/jammy/ax630c/v1.9/llm-llm_1.9-m5stack1_arm64.deb)

### llm-vlm

- 提供多模态文本生成能力。

```shell
apt install llm-vlm
```

- [下载 llm-vlm deb](https://repo.llm.m5stack.com/m5stack-apt-repo/pool/jammy/ax630c/v1.9/llm-vlm_1.9-m5stack1_arm64.deb)

### llm-tts

- 提供文本转语音功能。

```shell
apt install llm-tts
```

- [下载 llm-tts deb](https://repo.llm.m5stack.com/m5stack-apt-repo/pool/jammy/ax630c/v1.6/llm-tts_1.6-m5stack1_arm64.deb)

### llm-melotts

- 提供文本转语音功能。

```shell
apt install llm-melotts
```

- [下载 llm-melotts deb](https://repo.llm.m5stack.com/m5stack-apt-repo/pool/jammy/ax630c/v1.9/llm-melotts_1.9-m5stack1_arm64.deb)

