# Module LLM - LLM 生成式对话

该示例演示了如何在 Arduino 平台上利用 M5ModuleLLM 库调用 LLM 实现生成式对话功能。示例使用 USB 串口进行通信，通过串口终端程序向模块发送问题与获取响应。

## 准备工作

1. 参考[Module LLM Arduino 快速上手](/zh_CN/stackflow/module_llm/arduino)，完成基础环境搭建与 M5ModuleLLM 驱动库的安装。

2. 参考[Module LLM 软件包更新教程](/zh_CN/stackflow/module_llm/software)，完成以下模型包的安装。

```shell
apt install llm-llm
```

```shell
apt install llm-model-qwen2.5-0.5b-prefill-20e
```

3. 以下示例使用到的硬件设备包含：

- [Module LLM Kit](https://shop.m5stack.com/products/m5stack-llm-large-language-model-module-kit-ax630c)
- [CoreS3](https://shop.m5stack.com/products/m5stack-cores3-esp32s3-lotdevelopment-kit)

## LLM CoreS3

```cpp
/*
 * SPDX-FileCopyrightText: 2024 M5Stack Technology CO LTD
 *
 * SPDX-License-Identifier: MIT
 */
#include <Arduino.h>
#include <M5Unified.h>
#include <M5ModuleLLM.h>

#define CommSerialPort Serial

M5ModuleLLM module_llm;
String llm_work_id;
String received_question;
bool question_ok;

void setup()
{
    M5.begin();
    M5.Display.setTextSize(2);
    M5.Display.setTextScroll(true);

    /* Init usb serial */
    CommSerialPort.begin(115200);

    /* Init module serial port */
    int rxd = M5.getPin(m5::pin_name_t::port_c_rxd);
    int txd = M5.getPin(m5::pin_name_t::port_c_txd);
    Serial2.begin(115200, SERIAL_8N1, rxd, txd);

    /* Init module */
    module_llm.begin(&Serial2);

    /* Make sure module is connected */
    M5.Display.printf(">> Check ModuleLLM connection..\n");
    while (1) {
        if (module_llm.checkConnection()) {
            break;
        }
    }

    /* Reset ModuleLLM */
    M5.Display.printf(">> Reset ModuleLLM..\n");
    module_llm.sys.reset();

    /* Setup LLM module and save returned work id */
    M5.Display.printf(">> Setup llm..\n");
    m5_module_llm::ApiLlmSetupConfig_t llm_config;
    llm_config.max_token_len = 1023;
    llm_config.setParam("enable_temperature", true);
    llm_config.setParam("temperature", 0.7f);

    llm_config.setParam("enable_top_p_sampling", true);
    llm_config.setParam("top_p", 0.9f);

    llm_config.setParam("enable_top_k_sampling", true);
    llm_config.setParam("top_k", 50);

    llm_config.setParam("enable_repetition_penalty", true);
    llm_config.setParam("repetition_penalty", 1.05f);
    llm_config.setParam("penalty_window", 20);

    llm_work_id = module_llm.llm.setup(llm_config);

    M5.Display.printf(">> Setup finish\n");
    M5.Display.printf(">> Try send your question via usb serial port\n");
    M5.Display.setTextColor(TFT_GREEN);
    M5.Display.printf("e.g. \nHi, What's your name?\n");
    M5.Display.printf("(end with CRLF \\r\\n)\n\n");
}

void loop()
{
    /* Check comm serial port and get received question */
    question_ok = false;
    if (CommSerialPort.available()) {
        while (CommSerialPort.available()) {
            char in_char = (char)CommSerialPort.read();
            received_question += in_char;

            /* Check if question finish */
            if (received_question.endsWith("\r\n")) {
                received_question.remove(received_question.length() - 2);
                question_ok = true;
                break;
            }
        }
    }

    /* If question is ready */
    if (question_ok) {
        M5.Display.setTextColor(TFT_GREEN);
        M5.Display.printf("<< %s\n", received_question.c_str());
        M5.Display.setTextColor(TFT_YELLOW);
        M5.Display.printf(">> ");
        CommSerialPort.printf("<< \"%s\"\n", received_question.c_str());
        CommSerialPort.print(">> ");

        /* Push question to LLM module and wait inference result */
        module_llm.llm.inferenceAndWaitResult(llm_work_id, received_question.c_str(), [](String& result) {
            /* Show result on screen and usb serial */
            M5.Display.printf("%s", result.c_str());
            CommSerialPort.print(result);
        });

        /* Clear for next question */
        received_question.clear();

        M5.Display.println();
        CommSerialPort.println();
    }

    delay(20);
}
```
?> 注意 'temperature', 'top_p', 'top_k', 'repetition_penalty' 等参数配置，仅在软件版本 llm_llm >= 1.9 生效，请参考参考[Module LLM 软件包更新教程](/zh_CN/stackflow/module_llm/software)，对 ModuleLLM 预装的软件底包升级。

1. 将代码上传到 CoreS3。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1131/module_llm_chat_cores3_demo_01.jpg" width="70%">

2. 在 Arduino IDE 中打开串口监视器，并将波特率设置为 115200，并配置 "换行符 \r\n"。在串口监视器中输入文本并按 Enter 键发送。 Module LLM 将处理输入内容并返回响应。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1131/module_llm_chat_cores3_demo_02.jpg" width="70%">

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1131/module_llm_chat_cores3_demo_03.jpg" width="70%">
