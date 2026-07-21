# Module LLM Arduino 快速上手

## 概述

`Module LLM`模块能够搭配不同的 M5 主控使用，本教程将以`M5Core`系列主控举例如何在`Arduino IDE`中基于 LLM Module 驱动库编程控制 Module LLM。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/llm/llm/llm_module_device_01.jpg" width="70%" />

## 环境安装

1. Arduino IDE 安装： 参考[Arduino IDE安装教程](/zh_CN/arduino/arduino_ide)，完成 IDE 安装。

2. 板管理安装：参考[基本环境搭建教程](/zh_CN/arduino/arduino_board)，完成 M5Stack 板管理安装并选择开发板`M5Core`。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/m5core/quickstart_arduino_core_selectboard.png" width="70%" />

3. 依赖库安装： 参考[库管理安装教程](/zh_CN/arduino/arduino_library)，完成`Module LLM`驱动库安装。(根据提示安装依赖库`M5Unified`)

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/llm/llm/llm_arduino_lib_01.jpg" width="70%" />
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/llm/llm/llm_arduino_lib_02.jpg" width="70%" />

## 程序编译 & 烧录

打开驱动库中的案例程序**kws_asr**, 点击上传按钮，将自动进行程序编译，与程序烧录，案例程序使用的唤醒词为 "HELLO", 等待设备初始化完成，使用关键词进行唤醒。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/llm/llm/llm_arduino_example_01.jpg" width="70%" />
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/llm/llm/llm_arduino_example_02.jpg" width="70%" />
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/llm/llm/llm_arduino_example_03.jpg" width="70%" />
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/llm/llm/llm_arduino_example_04.jpg" width="70%" />

- examples:
  - `kws_asr`: 通过 KWS 实现唤醒 -> 触发 ASR 实现语音转换文本。 (KWS+ASR)
  - `text_assistant`: 通过文本方式输入内容至 LLM 模型，完成推理后以文本形式输出。 (LLM)
  - `tts`: 通过 TTS 单元实现文本转换语音播放。 (TTS)
  - `voice_assistant`: 通过 KWS 实现唤醒 -> 触发 ASR 实现语音转换文本 -> 将其转换内容作为 LLM 输入用作推理 -> 最后将推理输出结果通过 TTS 输出语音。 (KWS+ASR+LLM+TTS)

## 相关链接

- [Module LLM Arduino Lib](https://github.com/m5stack/M5Module-LLM)
- [Module LLM Arduino Lib API](/zh_CN/guide/llm/llm/arduino_api)
