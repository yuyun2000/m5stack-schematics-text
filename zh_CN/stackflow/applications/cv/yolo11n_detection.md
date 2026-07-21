# Module LLM - Yolo11n

该示例演示了如何在 Arduino 平台上利用 M5ModuleLLM 库调用 yolo11n 模型，以执行 YOLO 目标检测任务。

## 准备工作

1. 参考[Module LLM Arduino 快速上手](/zh_CN/stackflow/module_llm/arduino)，完成基础环境搭建与 M5ModuleLLM 驱动库的安装。

2. 参考[Module LLM 软件包更新教程](/zh_CN/stackflow/module_llm/software)，完成以下模型包的安装。

```shell
apt install llm-yolo
```

3. 以下示例使用到的硬件设备包含：

- [Module LLM Kit](https://shop.m5stack.com/products/m5stack-llm-large-language-model-module-kit-ax630c)
- [CoreS3](https://shop.m5stack.com/products/m5stack-cores3-esp32s3-lotdevelopment-kit)
- USB 摄像头

## Yolo11n CoreS3

```cpp
/*
 * SPDX-FileCopyrightText: 2024 M5Stack Technology CO LTD
 *
 * SPDX-License-Identifier: MIT
 */
#include <Arduino.h>
#include <M5Unified.h>
#include <M5ModuleLLM.h>
#include <M5GFX.h>

#include "M5CoreS3.h"

M5ModuleLLM module_llm;
String yolo_work_id;

struct DetectionResult {
    String class_name;
    float confidence;
    int x1;
    int y1;
    int x2;
    int y2;
};

M5Canvas canvas(&M5.Display);

void setup()
{
    M5.begin();
    M5.Display.setTextSize(2);
    M5.Display.setTextScroll(true);

    canvas.createSprite(M5.Display.width(), M5.Display.height());

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

    /* Set ModuleLLM baud rate */
    M5.Display.printf(">> ModuleLLM connected, set baud rate to 1500000\n");
    module_llm.setBaudRate(1500000);

    Serial2.begin(1500000, SERIAL_8N1, rxd, txd);
    module_llm.begin(&Serial2);

    /* Setup YOLO module and save returned work id */
    M5.Display.printf(">> Setup yolo..\n");
    yolo_work_id = module_llm.yolo.setup();
    canvas.setFont(&fonts::FreeSerifBold12pt7b);
}

DetectionResult parseDetection(String& jsonStr)
{
    DetectionResult detection;
    JsonDocument doc;
    deserializeJson(doc, jsonStr);
    JsonObject obj = doc.as<JsonObject>();
    if (obj["bbox"].is<JsonArray>() && obj["class"].is<const char*>() && obj["confidence"].is<const char*>()) {
        detection.class_name = obj["class"].as<const char*>();
        detection.confidence = atof(obj["confidence"].as<const char*>());
        JsonArray bbox       = obj["bbox"].as<JsonArray>();
        if (bbox.size() == 4) {
            detection.x1 = (int)atof(bbox[0].as<const char*>());
            detection.y1 = (int)atof(bbox[1].as<const char*>());
            detection.x2 = (int)atof(bbox[2].as<const char*>());
            detection.y2 = (int)atof(bbox[3].as<const char*>());
        }
    }
    return detection;
}

void loop()
{
    if (CoreS3.Camera.get()) {
        uint8_t* out_jpg   = NULL;
        size_t out_jpg_len = 0;
        frame2jpg(CoreS3.Camera.fb, 50, &out_jpg, &out_jpg_len);
        canvas.pushImage(0, 0, CoreS3.Display.width(), CoreS3.Display.height(), (uint16_t*)CoreS3.Camera.fb->buf);
        module_llm.yolo.inferenceAndWaitResult(
            yolo_work_id, out_jpg, out_jpg_len,
            [](String& result) {
                DetectionResult detection = parseDetection(result);
                int y1_pos                = detection.y1 - 40;
                if (y1_pos < 24) y1_pos = 24;
                String combinedResult = detection.class_name + " " + String(detection.confidence, 2);
                canvas.drawString(combinedResult, detection.x1, y1_pos);
                canvas.drawRect(detection.x1, detection.y1 - 40, detection.x2, detection.y2 - 40, ORANGE);
            },
            10);
        canvas.pushSprite(0, 0);
        free(out_jpg);
    }
    CoreS3.Camera.free();
}
```

1. 将代码上传到 CoreS3。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1131/module_llm_yolo11_cores3_demo_01.jpg" width="70%">

2. 等待初始化完成，进入检测模式，屏幕显示检测结果。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1131/module_llm_yolo11_cores3_demo_02.jpg" width="70%">

?> 注意事项 | 此 demo 会改变 Module LLM 串口通信的波特率。当 CoreS3 重启后，需要断电重启 Module LLM。

## Yolo11n USB 摄像头

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
String camera_work_id;
String yolo_work_id;

void clearDisplay()
{
    M5.Display.fillRect(40, 50, 270, 20, BLACK);
    M5.Display.fillRect(150, 80, 60, 20, BLACK);
    M5.Display.fillRect(40, 110, 40, 20, BLACK);
    M5.Display.fillRect(40, 140, 40, 20, BLACK);
    M5.Display.fillRect(40, 170, 40, 20, BLACK);
    M5.Display.fillRect(40, 200, 40, 20, BLACK);
}

void setup()
{
    M5.begin();
    M5.Display.setTextSize(2);
    M5.Display.setTextScroll(true);

    /* Init module serial port */
    int rxd = M5.getPin(m5::pin_name_t::port_c_rxd);
    int txd = M5.getPin(m5::pin_name_t::port_c_txd);
    Serial2.begin(115200, SERIAL_8N1, rxd, txd);

    /* Init module */
    module_llm.begin(&Serial2);

    /* Make sure module is connected */
    M5.Display.setTextColor(ORANGE, BLACK);
    M5.Display.setTextSize(2);
    M5.Display.setTextDatum(middle_center);
    M5.Display.drawString("Check ModuleLLM connection..", M5.Display.width() / 2, M5.Display.height() / 2);
    while (1) {
        if (module_llm.checkConnection()) {
            break;
        }
    }

    /* Reset ModuleLLM */
    M5.Display.fillRect(0, (M5.Display.height() / 2) - 10, 320, 25, BLACK);
    M5.Display.drawString("Reset ModuleLLM..", M5.Display.width() / 2, M5.Display.height() / 2);
    module_llm.sys.reset();

    /* Setup Camera module */
    M5.Display.fillRect(0, (M5.Display.height() / 2) - 10, 320, 25, BLACK);
    M5.Display.drawString("Setup camera..", M5.Display.width() / 2, M5.Display.height() / 2);
    camera_work_id = module_llm.camera.setup();

    /* Setup YOLO module and save returned work id */
    M5.Display.fillRect(0, (M5.Display.height() / 2) - 10, 320, 25, BLACK);
    M5.Display.drawString("Setup yolo..", M5.Display.width() / 2, M5.Display.height() / 2);
    m5_module_llm::ApiYoloSetupConfig_t yolo_config;
    yolo_config.input = {camera_work_id};
    yolo_work_id      = module_llm.yolo.setup(yolo_config, "yolo_setup");

    M5.Display.fillRect(0, (M5.Display.height() / 2) - 10, 320, 25, BLACK);

    M5.Display.setTextDatum(top_left);
    M5.Display.drawString("class", 10, 20);
    M5.Display.drawString("confidence", 10, 80);
    M5.Display.drawString("x1", 10, 110);
    M5.Display.drawString("y1", 10, 140);
    M5.Display.drawString("x2", 10, 170);
    M5.Display.drawString("y2", 10, 200);
}

void loop()
{
    /* Update ModuleLLM */
    module_llm.update();

    /* Handle module response messages */
    for (auto& msg : module_llm.msg.responseMsgList) {
        /* If YOLO module message */
        if (msg.work_id == yolo_work_id) {
            /* Check message object type */
            if (msg.object == "yolo.box.stream") {
                /* Parse message json and get YOLO result */
                JsonDocument doc;
                deserializeJson(doc, msg.raw_msg);
                JsonObject delta = doc["data"]["delta"].as<JsonObject>();

                if (delta.containsKey("bbox") && delta.containsKey("class") && delta.containsKey("confidence")) {
                    String class_name   = delta["class"].as<String>();
                    float confidence    = delta["confidence"].as<float>();
                    JsonArray bboxArray = delta["bbox"].as<JsonArray>();

                    if (bboxArray.size() == 4) {
                        int x1 = bboxArray[0].as<int>();
                        int y1 = bboxArray[1].as<int>();
                        int x2 = bboxArray[2].as<int>();
                        int y2 = bboxArray[3].as<int>();

                        clearDisplay();

                        M5.Display.drawString(class_name, 40, 50);
                        M5.Display.drawFloat(confidence, 2, 150, 80);
                        M5.Display.drawNumber(x1, 40, 110);
                        M5.Display.drawNumber(y1, 40, 140);
                        M5.Display.drawNumber(x2, 40, 170);
                        M5.Display.drawNumber(y2, 40, 200);
                    }
                } else {
                    clearDisplay();
                }
            }
        }
    }

    /* Clear handled messages */
    module_llm.msg.clearMsg("yolo_setup");
    module_llm.msg.responseMsgList.clear();
}
```

1. 将 USB 摄像头到 Module LLM，由于 Module LLM 并没有 USB-A 接口，连接的时候需要使用到一个 USB-A to USB-C 转接器。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1131/module_llm_yolo11_usb_demo_01.jpg" width="70%">

2. 将代码上传到 CoreS3。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1131/module_llm_yolo11_usb_demo_02.jpg" width="70%">

3. 等待初始化完成，进入检测模式，屏幕以文本显示检测结果。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1131/module_llm_yolo11_usb_demo_03.jpg" width="70%">
