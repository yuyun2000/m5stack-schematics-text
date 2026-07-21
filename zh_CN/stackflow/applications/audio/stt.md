# Module LLM - 语音转文本

该示例演示了如何使用 M5ModuleLLM 库通过 Whisper 模型执行关键词唤醒（KWS）、语音活动检测（VAD）和自动语音识别（ASR）。

## 准备工作

1. 参考[Module LLM Arduino 快速上手](/zh_CN/stackflow/module_llm/arduino)，完成基础环境搭建与 M5ModuleLLM 驱动库的安装。

2. 参考[Module LLM 软件包更新教程](/zh_CN/stackflow/module_llm/software)，完成以下模型包和软件包的安装。

```shell
apt install llm-whisper llm-kws llm-vad
```

```shell
apt install llm-model-whisper-tiny llm-model-silero-vad llm-model-sherpa-onnx-kws-zipformer-gigaspeech-3.3m-2024-01-01
```

- [Whisper-tiny 模型详细介绍](/zh_CN/stackflow/models/whisper-tiny)。

3. 以下示例使用到的硬件设备包含：

- [Module LLM](https://shop.m5stack.com/products/m5stack-llm-large-language-model-module-kit-ax630c)
- [CoreS3](https://shop.m5stack.com/products/m5stack-cores3-esp32s3-lotdevelopment-kit)

## STT CoreS3

```cpp
/*
* SPDX-FileCopyrightText: 2024 M5Stack Technology CO LTD
*
* SPDX-License-Identifier: MIT
*/
#include <Arduino.h>
#include <M5Unified.h>
#include <M5ModuleLLM.h>

M5ModuleLLM module_llm;

/* Must be capitalized */
String wake_up_keyword = "HELLO";
String kws_work_id;
String vad_work_id;
String whisper_work_id;
String language;

void setup()
{
    M5.begin();
    M5.Display.setTextSize(2);
    M5.Display.setTextScroll(true);

    language = "en_US";

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

    /* Setup Audio module */
    M5.Display.printf(">> Setup audio..\n");
    module_llm.audio.setup();

    /* Setup KWS module and save returned work id */
    M5.Display.printf(">> Setup kws..\n");
    m5_module_llm::ApiKwsSetupConfig_t kws_config;
    kws_config.kws = wake_up_keyword;
    kws_work_id    = module_llm.kws.setup(kws_config, "kws_setup", language);

    /* Setup VAD module and save returned work id */
    M5.Display.printf(">> Setup vad..\n");
    m5_module_llm::ApiVadSetupConfig_t vad_config;
    vad_config.input = {"sys.pcm", kws_work_id};
    vad_work_id      = module_llm.vad.setup(vad_config, "vad_setup");

    /* Setup Whisper module and save returned work id */
    M5.Display.printf(">> Setup whisper..\n");
    m5_module_llm::ApiWhisperSetupConfig_t whisper_config;
    whisper_config.input    = {"sys.pcm", kws_work_id, vad_work_id};
    whisper_config.language = "en";
    whisper_work_id = module_llm.whisper.setup(whisper_config, "whisper_setup");

    M5.Display.printf(">> Setup ok\n>> Say \"%s\" to wakeup\n", wake_up_keyword.c_str());
}

void loop()
{
    /* Update ModuleLLM */
    module_llm.update();

    /* Handle module response messages */
    for (auto& msg : module_llm.msg.responseMsgList) {
        /* If KWS module message */
        if (msg.work_id == kws_work_id) {
            M5.Display.setTextColor(TFT_GREENYELLOW);
            M5.Display.printf(">> Keyword detected\n");
        }

        /* If ASR module message */
        if (msg.work_id == whisper_work_id) {
            /* Check message object type */
            if (msg.object == "asr.utf-8") {
                /* Parse message json and get ASR result */
                JsonDocument doc;
                deserializeJson(doc, msg.raw_msg);
                String asr_result = doc["data"].as<String>();

                M5.Display.setTextColor(TFT_YELLOW);
                M5.Display.printf(">> %s\n", asr_result.c_str());
            }
        }
    }

    /* Clear handled messages */
    module_llm.msg.responseMsgList.clear();
}
```

1. 将代码上传到 CoreS3。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1131/module_llm_stt_cores3_demo_01.jpg" width="70%">

2. 等待初始化完成，使用唤醒词 hello 进行唤醒。将显示 检测到 "Keyword detected"。完成唤醒后，继续进行语音输入，停顿结束输入后，将自动识别，并显示 ASR 结果。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1131/module_llm_stt_cores3_demo_02.jpg" width="70%">
