# Unit Finger Arduino 使用教程

## 1. 准备工作

- 环境配置： 参考 [Arduino IDE 上手教程](/zh_CN/arduino/arduino_ide)完成 IDE 安装，并根据实际使用的开发板安装对应的板管理，与需要的驱动库。
- 使用到的驱动库：
  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5GFX](https://github.com/m5stack/M5GFX)
  - [M5-FPC1020A](https://github.com/m5stack/M5-FPC1020A)

\#> 注意 | 需要在 GitHub 上下载最新的库版本，库地址: [M5-FPC1020A - M5Stack GitHub](https://github.com/m5stack/M5-FPC1020A)，请勿在 Arduino Library 中下载。（如有疑问，请参考[此教程](/zh_CN/arduino/arduino_library#git%E6%89%8B%E5%8A%A8%E5%AE%89%E8%A3%85)）

- 使用到的硬件产品：
  - [CoreS3](https://shop.m5stack.com/products/m5stack-cores3-esp32s3-lotdevelopment-kit)
  - [Unit Finger](https://shop.m5stack.com/products/finger-sensor-unit)

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/CoreS3/img-2f6b5728-af80-4934-854f-4771a7fe859e.webp" width="20%"/> <img src="https://static-cdn.m5stack.com/resource/docs/products/unit/finger/finger_cover_01.webp" width="20%"/>

## 2. 注意事项

\#> 引脚兼容性 | 由于每款主机的引脚配置不同，使用前请参考产品文档中的[引脚兼容表](/zh_CN/unit/finger)，并根据实际引脚连接情况修改案例程序。

<ProductCompatible sku="U008" type="UNIT"></ProductCompatible>

## 3. 案例程序

- 本教程中使用的主控设备为 CoreS3 ，搭配 Unit Finger。本指纹识别模块采用串口的方式通讯，根据实际的电路连接修改程序中的引脚定义，设备连接后对应的串口 IO 为 `G1 (RX)`，`G2 (TX)`。

```cpp line-num
/**
 * @file Unit_Finger_M5CoreS3.ino
 * @author Zovey (liangzhuowei@m5stack.com)
 * @brief
 * @version 0.1
 * @date 2025-07-04
 *
 *
 * @Hardwares: M5CoreS3 + Unit Finger
 * @Dependent Library:
 * M5_FPC1020A: https://github.com/m5stack/M5-FPC1020A
 */

#include "M5Unified.h"
#include "M5_FPC1020A.h"

M5_FPC1020A finger;

bool add_user_process(uint8_t id, uint8_t permission);
bool id_input = 1, id_Verification = 1, id_delete = 1;

void setup() {
    M5.begin();
    Serial.begin(115200);
    M5.Display.fillRect(0, 0, 320, 240, WHITE);
    M5.Display.setTextColor(BLACK);
    M5.Display.setFont(&fonts::FreeMonoBold9pt7b);
    M5.Display.setCursor(0, 0);
    M5.Display.println("Finger Unit init...");
    if (!finger.begin(&Serial2, 1, 2, 19200)) {
        Serial.println("FPC1020A not found");
        while (1) delay(1);
    }
    M5.Display.fillRect(0, 0, 320, 240, WHITE);
    M5.Display.println("Finger Unit TEST");
    finger.delAllFinger();
    M5.Display.println("All ID have been deleted");
}

void loop() {
    while(id_input){
        M5.Display.fillScreen(WHITE);
        M5.Display.println("Please logic your finger");
        if(add_user_process(1, 1)){
            Serial.println("add user success");
            M5.Display.println("add user success");
            id_input = 0;
        }
    }
    delay(2000);
    while(id_Verification){
        M5.Display.fillScreen(WHITE);
        M5.Display.setCursor(0, 0);
        M5.Display.printf("User ID Verification:\r\n");
        uint8_t res = finger.available();
        if (res == ACK_SUCCESS){
            M5.Display.print("Success \r");
            Serial.println("Success");
            M5.Display.print("User ID: ");
            Serial.print("User ID: ");
            M5.Display.println(finger.getFingerID());
            Serial.println(finger.getFingerID());
            id_Verification = 0;
        }
        delay(2000);
    }
    while(id_delete){
        uint8_t res2 = finger.available();
        M5.Display.printf("Put your finger on the sensor again can delete all id\n");
        if (res2 == ACK_SUCCESS){
            finger.delAllFinger();
            M5.Display.println("All ID have been deleted");
            Serial.println("All ID have been deleted");
            id_delete = 0;
        }
        delay(2000);
    }
}

bool add_user_process(uint8_t id, uint8_t permission) {
    M5.Display.fillRect(0, 0, 320, 240, WHITE);
    M5.Display.setCursor(0, 0);
    M5.Display.println("add finger process:");
    M5.Display.println("put your finger on the sensor");
    for (uint8_t i = 0; i < 6; i++) {
        while (!finger.addFinger(id, permission, i)) {
            Serial.printf("Finger ID: %d Finger Record:%d error\r\n", id, i);
            Serial.println("Retry...");
            delay(1000);
        };
        M5.Display.printf("add finger count : %d/6\r\n", i + 1);
        Serial.printf("Finger ID: %d Finger Record:%d ok\r\n", id, i);
    }
    return true;
}
```

## 4. 编译上传

- 下载模式：不同设备进行程序烧录前需要进入下载模式，不同的主控设备该步骤可能有所不同。详情可参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)页面底部的设备程序下载教程列表，查看具体的操作方式。

- CoreS3 长按复位按键 (大约 2 秒) 直到内部绿色 LED 灯亮起，便可松开，此时设备已进入下载模式，等待烧录。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5CORES3%20SE/cores3%20(2).gif" width="30%">

- 选中设备端口，点击 Arduino IDE 左上角编译上传按钮，等待程序完成编译并上传至设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1125/module_fan_v1.1_arduino_example_01.jpg" width="70%">

## 5. 指纹识别

- 程序初始阶段是录入指纹，录入成功后会显示 `add user success` 等字样。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/717/Unit_Finger_Test_1.jpg" width="30%"> <img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/717/Unit_Finger_Test_2.jpg" width="30%">

- 成功录入后等待两秒会进入识别模式，再次把录入的指纹放在传感器上，屏幕显示 `Success User ID: 1` 等字样即是识别成功。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/717/Unit_Finger_Test_3.jpg" width="30%"> <img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/717/Unit_Finger_Test_4.jpg" width="30%">

- 最后会进入删除模式，把已录入的指纹放在传感器上即可进行删除，删除成功后会显示 `All ID have been deleted` 等字样。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/717/Unit_Finger_Test_5.jpg" width="30%"> <img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/717/Unit_Finger_Test_6.jpg" width="30%">
