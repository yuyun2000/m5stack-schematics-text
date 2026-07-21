# Unit UHF-RFID Arduino 使用教程

## 1. 准备工作

- 环境配置： 参考 [Arduino IDE 上手教程](/zh_CN/arduino/arduino_ide)完成 IDE 安装，并根据实际使用的开发板安装对应的板管理，与需要的驱动库。
- 使用到的驱动库：
  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5GFX](https://github.com/m5stack/M5GFX)
  - [M5Unit-UHF-RFID](https://github.com/m5stack/M5Unit-UHF-RFID/tree/master)

\#> 注意 | 需要在 GitHub 上下载最新的库版本，库地址: [M5Unit-UHF-RFID - M5Stack GitHub](https://github.com/m5stack/M5Unit-UHF-RFID/tree/master)，请勿在 Arduino Library 中下载。（如有疑问，请参考[此教程](/zh_CN/arduino/arduino_library#git%E6%89%8B%E5%8A%A8%E5%AE%89%E8%A3%85)）

- 使用到的硬件产品：
  - [CoreS3](https://shop.m5stack.com/products/m5stack-cores3-esp32s3-lotdevelopment-kit)
  - [Unit UHF-RFID](https://shop.m5stack.com/products/uhf-rfid-unit-jrd-4035)

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/CoreS3/img-2f6b5728-af80-4934-854f-4771a7fe859e.webp" width="20%"/> <img src="https://static-cdn.m5stack.com/resource/docs/products/unit/uhf_rfid/uhf_rfid_05.webp" width="20%"/>

## 2. 注意事项

\#> 标签识别 | 包装盒内放有一个 RFID 标签以供测试。若需使用其他标签，您只需要找到具有 EPCglobal UHF Class 1 Gen 2 或 ISO 18000-6C 协议的标签即可。

\#> 引脚兼容性 | 由于每款主机的引脚配置不同，使用前请参考产品文档中的[引脚兼容表](/zh_CN/unit/uhf_rfid)，并根据实际引脚连接情况修改案例程序。

<ProductCompatible sku="U107" type="UNIT"></ProductCompatible>

## 3. 案例程序

- 本教程中使用的主控设备为 CoreS3 ，搭配 Unit UHF-RFID。本射频读写模块采用串口的方式通讯，根据实际的电路连接修改程序中的引脚定义，设备连接后对应的串口 IO 为 `G1 (RX)`，`G2 (TX)`。

```cpp line-num
/*
 * SPDX-FileCopyrightText: 2025 M5Stack Technology CO LTD
 *
 * SPDX-License-Identifier: MIT
 */

#include <M5Unified.h>
#include <M5GFX.h>
#include "UNIT_UHF_RFID.h"

M5GFX display;
Unit_UHF_RFID uhf;
String info = "";

void setup() {
    M5.begin();
    Serial.begin(115200);
    uhf.begin(&Serial2, 115200, 1, 2, false);
    while (1) {
        info = uhf.getVersion();
        if (info != "ERROR") {
            Serial.println(info);
            break;
        }
    }
    uhf.setTxPower(2600);
    M5.Display.fillRect(0, 0, 320, 240, WHITE);
    M5.Display.setTextColor(BLACK);
    M5.Display.setFont(&fonts::FreeMonoBold9pt7b);
    M5.Display.setCursor(0, 0);
    M5.Display.println("Unit RFID UHF init...");
}

uint8_t write_buffer[]  = {0xab, 0xcd, 0xef, 0xdd};
uint8_t reade_buffer[4] = {0};

void log(String info) {
    Serial.println(info);
    M5.Display.println(info);
}

void loop() {
        log("polling once");
        uint8_t result = uhf.pollingOnce();
        // result = pollingMultiple(uint16_t polling_count);  Can be scanned repeatedly multiple times.
        Serial.printf("scan result: %d\r\n", result);
        if (result > 0) {
            for (uint8_t i = 0; i < result; i++) {
                log("pc: " + uhf.cards[i].pc_str);
                log("rssi: " + uhf.cards[i].rssi_str);
                log("epc: " + uhf.cards[i].epc_str);
                log("-----------------");
                delay(10);
            }
        }
        delay(2000);
        M5.Display.fillScreen(WHITE);
        M5.Display.setCursor(0, 0);

        if (uhf.select(uhf.cards[0].epc)) {
            log("Select OK");
        } else {
            log("Select ERROR");
        }
        log("Current Select EPC:");
        log(uhf.selectInfo());
        delay(2000);
        M5.Display.fillScreen(WHITE);
        M5.Display.setCursor(0, 0);

        log("Write Data...");
        if (uhf.writeCard(write_buffer, sizeof(write_buffer), 0x04, 0, 0x00000000)) {
            log("Write OK");
        } else {
            log("Write ERROR");
        }
        delay(1000);
        log("Read Data...");
        if (uhf.readCard(reade_buffer, sizeof(reade_buffer), 0x04, 0, 0x00000000)) {
            log("Read OK");
            log("Data Content");
            for (uint8_t i = 0; i < sizeof(reade_buffer); i++) {
                Serial.printf("%x", reade_buffer[i]);
                M5.Display.printf("%x", reade_buffer[i]);
            }
        } else {
            log("Read ERROR");
        }
        delay(2000);
        M5.Display.fillScreen(WHITE);
        M5.Display.setCursor(0, 0);
}
```

## 4. 编译上传

- 下载模式：不同设备进行程序烧录前需要进入下载模式，不同的主控设备该步骤可能有所不同。详情可参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)页面底部的设备程序下载教程列表，查看具体的操作方式。

- CoreS3 长按复位按键 (大约 2 秒) 直到内部绿色 LED 灯亮起，便可松开，此时设备已进入下载模式，等待烧录。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5CORES3%20SE/cores3%20(2).gif" width="30%">

- 选中设备端口，点击 Arduino IDE 左上角编译上传按钮，等待程序完成编译并上传至设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1125/module_fan_v1.1_arduino_example_01.jpg" width="70%">

## 5. 标签识别

- 程序起始阶段是扫描阶段，若扫描成功会有 RFID 标签的协议控制字，表示接收到的 RFID 标签信号强度指示以及 RFID 标签的电子产品代码显示在屏幕上。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/842/Unit_RFID_UHF_1.jpg" width="70%">

- 当有多个标签时，RFID 模块支持选择功能，当选择成功后会显示出该标签的电子代码。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/842/Unit_RFID_UHF_2.jpg" width="70%">

- 可以用 RFID 模块直接对标签的存储区域进行读写，写入成功会显示 "Write OK" , 读取成功会显示 "Read OK" 并且输出刚刚写入的数据。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/842/Unit_RFID_UHF_3.jpg" width="70%">
