# OpenAI API 使用说明

本教程将介绍如何在 **Module LLM** 与 **LLM630 Compute Kit** 中安装不同的模型服务，并在PC端或其他设备上通过标准 OpenAI API 访问调用其模型功能，包含对话生成、语音识别、语音合成等常用场景，助力构建高效的 AI 边缘应用系统。

## 1.准备工作

使用前请参考对应设备的软件更新教程，完成M5Stack apt软件源信息的添加与索引更新。

- [Module LLM 镜像 & 软件升级教程](/zh_CN/guide/llm/llm/image)
- [LLM630 Compute Kit 镜像 & 软件升级教程](/zh_CN/guide/llm/llm630_compute_kit/image)

## 2.依赖库更新

1. 通过UART或SSH方等式访问设备终端，执行下方指令更新apt软件源信息索引。

```bash
apt update
```

2. 更新设备llm底包。

```bash
apt install lib-llm 
```

3. 更新相关依赖包。


``` bash
apt install llm-sys llm-llm llm-vlm llm-whisper llm-melotts llm-openai-api
```

4. 完成以上软件包安装后，重启设备。

```bash
reboot
```

## 3.Python OpenAI

在 PC 上配置好 Python 环境，并通过 pip 安装 OpenAI 官方的 Python 库。后续将基于该库，使用标准 OpenAI API 接口访问 LLM 设备并调用其模型能力。

```bash
pip install openai
```

## 4.功能目录

- [模型列表](/zh_CN/guide/llm/openai_api/models)
- [会话补全](/zh_CN/guide/llm/openai_api/chat_completions)
- [语音转文本](/zh_CN/guide/llm/openai_api/speech_to_text)
- [文本转语音](/zh_CN/guide/llm/openai_api/text_to_speech)
- [Chatbox](/zh_CN/guide/llm/openai_api/chatbox)


