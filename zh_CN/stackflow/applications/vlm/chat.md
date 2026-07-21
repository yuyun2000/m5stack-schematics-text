# Module LLM - 视觉语言模型

该示例演示了如何在 Arduino 平台上利用 M5ModuleLLM 库调用 VLM 执行视觉语言模型任务。

## 准备工作

1. 参考[Module LLM Arduino 快速上手](/zh_CN/stackflow/module_llm/arduino)，完成基础环境搭建与 M5ModuleLLM 驱动库的安装。

2. 参考[Module LLM 软件包更新教程](/zh_CN/stackflow/module_llm/software)，完成以下模型包的安装。

```shell
apt install llm-vlm
```

```shell
apt install llm-model-internvl2.5-1b-364-ax630c
```

3. 以下示例使用到的硬件设备包含：

- [Module LLM Kit](https://shop.m5stack.com/products/m5stack-llm-large-language-model-module-kit-ax630c)
- [CoreS3](https://shop.m5stack.com/products/m5stack-cores3-esp32s3-lotdevelopment-kit)

## VLM CoreS3

```cpp
/*
 * SPDX-FileCopyrightText: 2024 M5Stack Technology CO LTD
 *
 * SPDX-License-Identifier: MIT
 */
#include <Arduino.h>
#include <M5Unified.h>
#include <M5ModuleLLM.h>

#include "M5CoreS3.h"

M5ModuleLLM module_llm;
String vlm_work_id;

void setup()
{
    M5.begin();
    M5.Display.setTextSize(2);
    M5.Display.setTextScroll(true);

    /* Init M5CoreS3 Camera */
    CoreS3.Camera.begin();
    CoreS3.Camera.sensor->set_framesize(CoreS3.Camera.sensor, FRAMESIZE_QVGA);

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

    /* Setup VLM module and save returned work id */
    M5.Display.printf(">> Setup vlm..\n");
    vlm_work_id = module_llm.vlm.setup();
}

void loop()
{
    String question = "Describe the content of the image";

    M5.update();

    auto count = M5.Touch.getCount();

    static m5::touch_state_t prev_state;
    auto t = M5.Touch.getDetail();

    static int vlm_inference;

    if (t.wasClicked()) {
        static unsigned long lastClickTime = 0;
        unsigned long currentMillis        = millis();
        if (currentMillis - lastClickTime < 800) {
            vlm_inference = 2;
        }
        lastClickTime = currentMillis;
    }

    if (t.wasFlicked()) {
        vlm_inference--;
    }

    if (CoreS3.Camera.get()) {
        if (vlm_inference == 2) {
            uint8_t* out_jpg   = NULL;
            size_t out_jpg_len = 0;
            frame2jpg(CoreS3.Camera.fb, 50, &out_jpg, &out_jpg_len);
            module_llm.vlm.inference(vlm_work_id, out_jpg, out_jpg_len);
            free(out_jpg);
            delay(10);
            M5.Lcd.setCursor(0, 0);
            /* Push question to LLM module and wait inference result */
            module_llm.vlm.inferenceAndWaitResult(vlm_work_id, question.c_str(), [](String& result) {
                /* Show result on screen */
                M5.Display.printf("%s", result.c_str());
            });
            vlm_inference--;
        } else if (vlm_inference == 1) {
            delay(10);
        } else {
            CoreS3.Display.pushImage(0, 0, CoreS3.Display.width(), CoreS3.Display.height(),
                                     (uint16_t*)CoreS3.Camera.fb->buf);
        }
        CoreS3.Camera.free();
    }
}
```

1. 将代码上传到 CoreS3。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1131/module_llm_vlm_cores3_demo_01.jpg" width="70%">

2. 等待初始化完成，显示摄像头画面。双击屏幕拍照，等待大模型返回结果。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1131/module_llm_vlm_cores3_demo_02.jpg" width="70%">

3. 滑动屏幕可清除显示的文本。
