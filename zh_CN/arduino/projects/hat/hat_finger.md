# Hat Finger Arduino 使用教程

## 1. 准备工作

- 环境配置： 参考 [Arduino IDE 上手教程](/zh_CN/arduino/arduino_ide)完成 IDE 安装，并根据实际使用的开发板安装对应的板管理，与需要的驱动库。
- 使用到的驱动库：
  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5GFX](https://github.com/m5stack/M5GFX)
  - [M5-FPC1020A](https://github.com/m5stack/M5-FPC1020A)

\#> 注意 | 需要在 GitHub 上下载最新的库版本，库地址: [M5-FPC1020A - M5Stack GitHub](https://github.com/m5stack/M5-FPC1020A)，请勿在 Arduino Library 中下载。（如有疑问，请参考[此教程](/zh_CN/arduino/arduino_library#git%E6%89%8B%E5%8A%A8%E5%AE%89%E8%A3%85)）

- 使用到的硬件产品：
  - [StickC-Plus2](https://shop.m5stack.com/products/m5stickc-plus2-esp32-mini-iot-development-kit)
  - [Hat Finger](https://shop.m5stack.com/products/m5stickc-fingerprint-hatf1020sc)

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/M5StickC%20PLUS2/3.webp" width="20%"/> <img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-finger/hat-finger_02.webp" width="20%"/>

## 2. 注意事项

\#> 引脚兼容性 | 由于每款主机的引脚配置不同，使用前请参考产品文档中的[引脚兼容表](/zh_CN/hat/hat-finger)，并根据实际引脚连接情况修改案例程序。

<ProductCompatible sku="U074" type="HAT"></ProductCompatible>

## 3. 案例程序

- 本教程中使用的主控设备为 StickC-Plus2 ，搭配 Hat Finger 模块。本指纹识别模块采用串口的方式通讯，根据实际的电路连接修改程序中的引脚定义，设备堆叠后对应的串口 IO 为 `G26 (RX)`，`G0 (TX)`。

```cpp line-num
/**
 * @file Unit_Finger_M5StickCPlus.ino
 * @author Zovey (liangzhuowei@m5stack.com)
 * @brief
 * @version 0.1
 * @date 2025-07-04
 *
 * @Hardwares: StickC-Plus2 + Hat Finger
 * @Dependent Library:
 * M5_FPC1020A: https://github.com/m5stack/M5-FPC1020A
 */

#include <M5Unified.h>
#include "M5_FPC1020A.h"

M5_FPC1020A finger;
uint8_t user_id = 0;

bool add_user_process(uint8_t id, uint8_t permission) ;
bool user_check(void);

void setup() {
    M5.begin();
    Serial.begin(115200);
    M5.Display.setRotation(1);
    M5.Display.setTextColor(BLACK);
    M5.Display.setTextSize(1);
    M5.Display.setFont(&fonts::FreeMonoBold9pt7b);
    M5.Display.setCursor(0, 0);
    M5.Display.println("Finger Unit init...");
    if (!finger.begin(&Serial2, 26, 0, 19200)) {
        Serial.println("FPC1020A not found");
        while (1) delay(1);
    }
    M5.Display.fillRect(0, 0, 240, 135, WHITE);
    M5.Display.setCursor(0, 0);
    M5.Display.println("Finger Unit TEST");

    uint8_t userNum = finger.getUserCount();
    Serial.print("userNum:");
    Serial.println(userNum);

    finger.delAllFinger();
    M5.Display.println("All User Deleted");

    M5.Display.println("Btn.A add a user");
    M5.Display.println("Btn.B verify user");
}

uint8_t new_user_id = 1;

void loop() {
    M5.update();
    if (M5.BtnA.wasPressed()) {
        // user id: 1 ~ 0xfff
        if (add_user_process(new_user_id, 1)) {
            Serial.println("add user success");
            M5.Display.println("add user success");
            new_user_id++;
        }
    }

    if (M5.BtnB.wasPressed()) {
        M5.Display.fillRect(0, 0, 240, 135, WHITE);
        M5.Display.setCursor(0, 0);
        if(new_user_id == 1)    M5.Display.printf("There is no id. Please add the user first!\r\n");
        user_check();
    }
}

bool add_user_process(uint8_t id, uint8_t permission) {
    uint8_t a = 40;
    M5.Display.fillRect(0, 0, 240, 135, WHITE);
    M5.Display.setCursor(0, 0);
    M5.Display.println("add finger process:");
    M5.Display.println("put your finger on the sensor");
    for (uint8_t i = 0; i < 6; i++) {
        while (!finger.addFinger(id, permission, i)) {
            Serial.printf("Finger ID: %d Finger Record:%d error\r\n", id, i);
            Serial.println("Retry...");
            delay(1000);
        };
        a += 9;
        M5.Display.scroll(0, -9);
        M5.Display.fillRect(0, a, 240, 135, WHITE);
        M5.Display.setCursor(0, a);
        M5.Display.printf("add finger count:%d/6\r\n", i + 1);
        Serial.printf("Finger ID: %d Finger Record:%d ok\r\n", id, i);
    }
    M5.Display.printf("Finger ID: %d added\r\n", id);
    return true;
}

bool user_check(void){
    while((new_user_id > 1)){
        uint8_t res = finger.available();
        if (res == ACK_SUCCESS) {
            M5.Display.println("Success");
            Serial.println("Success");
            M5.Display.print("User ID: ");
            Serial.print("User ID: ");
            M5.Display.println(finger.getFingerID());
            Serial.println(finger.getFingerID());
            M5.Display.print("User Permission: ");
            Serial.print("User Permission: ");
            M5.Display.println(finger.getFingerPermission());
            Serial.println(finger.getFingerPermission());
            return true;
        } else {
            M5.Display.fillRect(0, 0, 240, 135, WHITE);
            M5.Display.setCursor(0, 0);
            Serial.println("Please put your ID Finger on the sensor");
            M5.Display.println("Please put your ID Finger on the sensor");
            delay(1000);
        }
    }
    return false;
}
```

## 4. 指纹识别

- 在初始页展示了该例程的功能，按下 `Btn.A` 按键进入指纹录入页面，按下 `Btn.B` 按键进入指纹识别页面。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/869/Finger_Unit_Test_1.jpg" width="30%">

- 进入指纹录入页面后，把需要录入指纹的手指放在传感器上，并等待录入完成。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/869/Finger_Unit_Test_2.jpg" width="30%">

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/869/Finger_Unit_Test_3.jpg" width="30%">

- 随后可以进行指纹识别测试，按下 `Btn.B` 按钮，将手指放在传感器上，并等待识别完成。当出现 `Success` 等字样时，表示识别成功（此界面需识别成功才可切换）。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/869/Finger_Unit_Test_4.jpg" width="30%">

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/869/Finger_Unit_Test_5.jpg" width="30%">
