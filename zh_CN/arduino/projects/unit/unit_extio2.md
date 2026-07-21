# Unit EXT.IO2 Arduino 使用教程

## 1. 准备工作

- 环境配置： 参考 [Arduino IDE 上手教程](/zh_CN/arduino/arduino_ide)完成 IDE 安装，并根据实际使用的开发板安装对应的板管理，与需要的驱动库。
- 使用到的驱动库：
  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5GFX](https://github.com/m5stack/M5GFX)
  - [M5Unit-EXTIO2](https://github.com/m5stack/M5Unit-EXTIO2/tree/main)

\#> 注意 | 需要在 GitHub 上下载最新的库版本，库地址: [M5Unit-EXTIO2 - M5Stack GitHub](https://github.com/m5stack/M5Unit-EXTIO2/tree/main)，请勿在 Arduino Library 中下载。（如有疑问，请参考[此教程](/zh_CN/arduino/arduino_library#git%E6%89%8B%E5%8A%A8%E5%AE%89%E8%A3%85)）

- 使用到的硬件产品：
  - [CoreS3](https://shop.m5stack.com/products/m5stack-cores3-esp32s3-lotdevelopment-kit)
  - [Unit EXT.IO2](https://shop.m5stack.com/products/extend-i-o-unit-2-stm32f0)

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/CoreS3/img-2f6b5728-af80-4934-854f-4771a7fe859e.webp" width="20%"/> <img src="https://static-cdn.m5stack.com/resource/docs/products/unit/extio2/extio2_cover_01.webp" width="20%"/>

## 2. 注意事项

\#> 引脚兼容性 | 由于每款主机的引脚配置不同，使用前请参考产品文档中的[引脚兼容表](/zh_CN/unit/extio2#兼容性)，并根据实际引脚连接情况修改案例程序。

<ProductCompatible sku="U011-B" type="UNIT"></ProductCompatible>

## 3. 案例程序

- 本教程中使用的主控设备为 CoreS3 ，搭配 Unit EXT.IO2。本 IO 拓展单元采用 I2C 的方式通讯，根据实际的电路连接修改程序中的引脚定义，设备连接后对应的通信 IO 为 `G1 (SDA)`，`G2 (SCL)`。

- 引脚模拟量 ADC 输入

```cpp line-num
#include <M5Unified.h>
#include "M5_EXTIO2.h"

M5_EXTIO2 extio;

void setup() {
    M5.begin();
    Serial.begin(115200);
    M5.Display.fillScreen(WHITE);
    M5.Display.setTextColor(BLACK);
    M5.Display.setTextFont(&fonts::FreeMonoBold9pt7b);
    M5.Display.setCursor(0, 0);
    while (!extio.begin(&Wire, 2, 1,
                        0x45)) {
        Serial.println("extio Connect Error");
        M5.Display.println("extio Connect Error");
        delay(100);
    }
    extio.setAllPinMode(ADC_INPUT_MODE);  // Set all pins to ADC input mode.
}

char info[50];

void loop() {
    M5.Display.fillScreen(WHITE);
    M5.Display.setCursor(0, 0);
    M5.Display.println("ADC INPUT MODE");
    M5.Display.println("FW VERSION: " + String(extio.getVersion()));
    for (uint8_t i = 0; i < 8; i++) {
        uint16_t adc =
            extio.getAnalogInput(i, _12bit);  // Get ADC value. 获取ADC值
        Serial.printf("CH:%d ADC: %d", i, adc);
        M5.Display.fillRect(0, i * 20 + 40, 200, 15, WHITE);
        M5.Display.setCursor(0, i * 20 + 40);
        M5.Display.printf("CH:%d ADC: %d", i, adc);
    }
    vTaskDelay(1000);
}
```

- 引脚数字输出

```cpp line-num
#include <M5Unified.h>
#include "M5_EXTIO2.h"

M5_EXTIO2 extio;

extio_io_mode_t mode = DIGITAL_OUTPUT_MODE;

void btnTask(void *pvParameters) {
    while (1) {
        if (M5.BtnA.wasPressed()) {
            if (mode == DIGITAL_INPUT_MODE) {
                mode = DIGITAL_OUTPUT_MODE;
            } else {
                mode = DIGITAL_INPUT_MODE;
            }
        }
        M5.update();
        vTaskDelay(80);
    }
}

void setup() {
    M5.begin();
    Serial.begin(115200);
    M5.Display.fillScreen(WHITE);
    M5.Display.setTextColor(BLACK);
    M5.Display.setTextFont(&fonts::FreeMonoBold9pt7b);
    M5.Display.setCursor(0, 0);
    while (!extio.begin(&Wire, 2, 1, 0x45)) {
        Serial.println("extio Connect Error");
        M5.Display.println("extio Connect Error");
        delay(100);
    }
    extio.setAllPinMode(
        DIGITAL_OUTPUT_MODE);
    xTaskCreatePinnedToCore(btnTask, "btnTask",
                            4096,
                            NULL,
                            1 ,
                            NULL, 0);
}

char info[50];

void loop() {
    if (mode == DIGITAL_INPUT_MODE) {
        M5.Display.fillScreen(WHITE);
        M5.Display.setCursor(0, 0);
        M5.Display.println("DIGITAL INPUT MODE");
        M5.Display.println("FW VERSION: " + String(extio.getVersion()));
        for (uint8_t i = 0; i < 8; i++) {
            if (extio.getDigitalInput(i)) {
                M5.Display.fillRect(i * 30 + 30, 145, 28, 30, WHITE);
            } else {
                M5.Display.fillRect(i * 30 + 30, 145, 28, 30, WHITE);
            }
        }
    } else if (mode == DIGITAL_OUTPUT_MODE) {
        M5.Display.fillScreen(WHITE);
        M5.Display.setCursor(0, 0);
        M5.Display.println("DIGITAL OUTPUT MODE");
        M5.Display.printf("FW VERSION: %s",String(extio.getVersion()));
        for (uint8_t i = 0; i < 8; i++) {
            extio.setDigitalOutput(i, HIGH);
            M5.Display.fillRect(i * 30 + 30, 145, 28, 30, BLACK);
            M5.Display.setCursor(i * 30 + 30, 145);
            vTaskDelay(100);
        }
        for (uint8_t i = 0; i < 8; i++) {
            extio.setDigitalOutput(i, LOW);
            M5.Display.fillRect(i * 30 + 30, 145, 28, 30, BLACK);
            M5.Display.setCursor(i * 30 + 30, 145);
            vTaskDelay(100);
        }
    }
    extio.setAllPinMode(mode);
    vTaskDelay(100);
}
```

- 引脚数字输入

```cpp line-num
#include <M5Unified.h>
#include "M5_EXTIO2.h"

M5_EXTIO2 extio;

extio_io_mode_t mode = DIGITAL_OUTPUT_MODE;

void btnTask(void *pvParameters) {
    while (1) {
        if (M5.BtnA.wasPressed()) {
            if (mode == DIGITAL_INPUT_MODE) {
                mode = DIGITAL_OUTPUT_MODE;
            } else {
                mode = DIGITAL_INPUT_MODE;
            }
        }
        M5.update();
        vTaskDelay(80);
    }
}

void setup() {
    M5.begin();
    Serial.begin(115200);
    M5.Display.fillScreen(WHITE);
    M5.Display.setTextColor(BLACK);
    M5.Display.setTextFont(&fonts::FreeMonoBold9pt7b);
    M5.Display.setCursor(0, 0);
    while (!extio.begin(&Wire, 2, 1, 0x45)) {
        Serial.println("extio Connect Error");
        M5.Display.println("extio Connect Error");
        delay(100);
    }
    extio.setAllPinMode(
        DIGITAL_OUTPUT_MODE);
    xTaskCreatePinnedToCore(btnTask, "btnTask",
                            4096,
                            NULL,
                            1 ,
                            NULL, 0);
}

char info[50];

void loop() {
        M5.Display.fillScreen(WHITE);
        M5.Display.setCursor(0, 0);
        M5.Display.println("DIGITAL INPUT MODE");
        M5.Display.println("FW VERSION: " + String(extio.getVersion()));
        extio.setDigitalOutput(0, HIGH);
        M5.Display.println("Set Pin_0 level to high");
        M5.Display.printf("Pin_1 level is %s",(String)extio.getDigitalInput(1));
        extio.setAllPinMode(mode);
        vTaskDelay(100);
}
```

- SERVO 控制

```cpp line-num
#include <M5Unified.h>
#include "M5_EXTIO2.h"

M5_EXTIO2 extio;

void setup() {
    M5.begin();
    Serial.begin(115200);
    M5.Display.fillScreen(WHITE);
    M5.Display.setTextColor(BLACK);
    M5.Display.setTextFont(&fonts::FreeMonoBold9pt7b);
    M5.Display.setCursor(0, 0);
    while (!extio.begin(&Wire, 2, 1, 0x45)) {
        Serial.println("extio Connect Error");
        M5.Display.println("extio Connect Error");
        delay(100);
    }
    extio.setAllPinMode(SERVO_CTL_MODE);
}

char info[50];

void loop() {
    M5.Display.fillScreen(WHITE);
    M5.Display.setCursor(0, 0);
    M5.Display.println("SERVO CTL MODE");
    M5.Display.printf("FW VERSION: %s", String(extio.getVersion()));
    for (uint8_t deg = 0; deg <= 180; deg += 45) {
        for (uint8_t i = 0; i < 8; i++) {
            extio.setServoAngle(i, deg);
            Serial.printf("CH:%d DEG: %d", i, deg);
            M5.Display.fillRect(0, i * 20, 200, i * 20 + 20, WHITE);
            M5.Display.setCursor(0, i * 20);
            M5.Display.printf("CH:%d DEG: %d", i, deg);
        }
        vTaskDelay(500);
    }
    for (int pulse = 500; pulse <= 2500; pulse += 100) {
        for (uint8_t i = 0; i < 8; i++) {
            extio.setServoPulse(i, pulse);
            Serial.printf("CH:%d P: %d", i, pulse);
            M5.Display.fillRect(0, i * 20, 200, i * 20 + 20, WHITE);
            M5.Display.setCursor(0, i * 20);
            M5.Display.printf("CH:%d P: %d", i, pulse);
        }
        vTaskDelay(500);
    }
    delay(100);
}
```

## 4. 编译上传

- 下载模式：不同设备进行程序烧录前需要进入下载模式，不同的主控设备该步骤可能有所不同。详情可参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)页面底部的设备程序下载教程列表，查看具体的操作方式。

- CoreS3 长按复位按键 (大约 2 秒) 直到内部绿色 LED 灯亮起，便可松开，此时设备已进入下载模式，等待烧录。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5CORES3%20SE/cores3%20(2).gif" width="30%">

- 选中设备端口，点击 Arduino IDE 左上角编译上传按钮，等待程序完成编译并上传至设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1125/module_fan_v1.1_arduino_example_01.jpg" width="70%">

## 5. 拓展效果

- 在 ADC_INPUT 模式下，可以读取到各个通道的模拟值。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/789/Unit_EXTIO2_2.jpg" width="70%">

- 在数字输出模式下，接入一个 LED 灯来可视化该引脚的电平变化。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/789/Unit_EXTIO2_5.jpg" width="70%">

- 在数字输入模式下，一个引脚输出高电平并用另一引脚读取，可以判断其电平状态。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/789/Unit_EXTIO2_1.jpg" width="70%">

- 在 SERVO 模式下，该引脚可以输出一个 PWM 信号以驱动舵机。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/789/Unit_EXTIO2_4.jpg" width="70%">

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/789/Unit_EXTIO2_3.jpg" width="70%">
