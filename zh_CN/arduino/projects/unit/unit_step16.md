# Unit Step16 Arduino 使用教程

## 1. 准备工作

- 环境配置： 参考 [Arduino IDE 上手教程](/zh_CN/arduino/arduino_ide)完成 IDE 安装，并根据实际使用的开发板安装对应的板管理，与需要的驱动库。
- 使用到的驱动库：
  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5GFX](https://github.com/m5stack/M5GFX)
  - [M5Unit-Step16](https://github.com/m5stack/M5Unit-Step16)

\#> 注意 | 需要在 GitHub 上下载最新的库版本，库地址: [M5Unit-Step16 - M5Stack GitHub](https://github.com/m5stack/M5Unit-Step16)，请勿在 Arduino Library 中下载。（如有疑问，请参考[此教程](/zh_CN/arduino/arduino_library#git%E6%89%8B%E5%8A%A8%E5%AE%89%E8%A3%85)）

- 使用到的硬件产品：
  - [CoreS3](https://shop.m5stack.com/products/m5stack-cores3-esp32s3-lotdevelopment-kit)
  - [Unit Step16](https://shop.m5stack.com/products/step16-unit-with-16-bit-rotary-encoder-gsmr-16)

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/CoreS3/img-2f6b5728-af80-4934-854f-4771a7fe859e.webp" width="20%"/> <img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1160/Unit_Step16_product.jpg" width="20%"/>

## 2. 注意事项

\#> 引脚兼容性 | 由于每款主机的引脚配置不同，为了让用户更方便地使用，M5Stack 官方提供了[引脚兼容性表](/zh_CN/unit/Unit_Step16#%E5%85%BC%E5%AE%B9%E6%80%A7)，方便用户查看，请根据实际引脚连接情况修改案例程序。

<ProductCompatible sku="U198" type="UNIT"></ProductCompatible>

## 3. 案例程序

- 本教程中使用的主控设备为 CoreS3 ，搭配 Unit Step16。本 16 定位旋转编码器模块采用 I2C 的方式通讯，根据实际的电路连接修改程序中的引脚定义，设备连接后对应的 I2C 引脚为 `G1 (SCL)`，`G2 (SDA)`。

```cpp line-num
/*
 * SPDX-FileCopyrightText: 2025 M5Stack Technology CO LTD
 *
 * SPDX-License-Identifier: MIT
 */
/*
 * @Hardwares: M5Stack PortA device + Unit Step16
 * @Dependent Library:
 * M5Unit-Step16:https://github.com/m5stack/M5Unit-Step16
 * @description: When the knob is rotated, only 0-8 is displayed,
 *              when raw value reaches 9-F, rotation direction is automatically reversed,
 *              LED brightness follows display value, never zero (minimum 10%),
 *              RGB color follows the 0-8 pattern
 */
#include <M5Unified.h>
#include <M5UnitStep16.h>

#define I2C_SDA_PIN     (2)
#define I2C_SCL_PIN     (1)
#define NUM_DIGITS      (9)
#define MAX_DIGIT       (8)
#define MIN_DIGIT       (0)
#define MIN_BRIGHTNESS  (10)
#define MAX_BRIGHTNESS  (100)
#define BRIGHTNESS_STEP (10)
#define RGB_BRIGHTNESS  (70)
#define LED_ALWAYS_ON   (0xFF)

UnitStep16 step16;
uint8_t currentDigit = 0;
uint8_t lastRawValue = 0;
bool isFirstRead     = true;

const uint8_t digitBrightness[NUM_DIGITS] = {
    MIN_BRIGHTNESS,                        // 0 - 10%
    MIN_BRIGHTNESS + BRIGHTNESS_STEP,      // 1 - 20%
    MIN_BRIGHTNESS + BRIGHTNESS_STEP * 2,  // 2 - 30%
    MIN_BRIGHTNESS + BRIGHTNESS_STEP * 3,  // 3 - 40%
    MIN_BRIGHTNESS + BRIGHTNESS_STEP * 4,  // 4 - 50%
    MIN_BRIGHTNESS + BRIGHTNESS_STEP * 5,  // 5 - 60%
    MIN_BRIGHTNESS + BRIGHTNESS_STEP * 6,  // 6 - 70%
    MIN_BRIGHTNESS + BRIGHTNESS_STEP * 7,  // 7 - 80%
    MIN_BRIGHTNESS + BRIGHTNESS_STEP * 8   // 8 - 90%
};

struct MyRGBColor {
    uint8_t r, g, b;
    const char* name;
};

const MyRGBColor digitColors[NUM_DIGITS] = {
    {0, 0, 128, "Deep Blue"},       // 0 - cold color
    {0, 64, 192, "Blue"},           // 1
    {0, 128, 255, "Light Blue"},    // 2
    {0, 192, 192, "Cyan"},          // 3
    {0, 255, 128, "Cyan Green"},    // 4
    {128, 255, 0, "Yellow Green"},  // 5
    {192, 192, 0, "Yellow"},        // 6
    {255, 128, 0, "Orange"},        // 7
    {255, 64, 0, "Orange Red"}      // 8 - warm color
};

uint8_t mapRawValueToDigit(uint8_t rawValue);
void updateDisplay(uint8_t digit);
uint8_t mapRawValueToDigit(uint8_t rawValue);
void updateDisplay(uint8_t digit);
void handleValueChange(uint8_t oldVal, uint8_t newVal);

void setup()
{
    M5.begin();
    Serial.begin(115200);
    Wire.begin(I2C_SDA_PIN, I2C_SCL_PIN);
    while(!step16.begin()){
        delay(1000);
        Serial.println("M5Unit-Step16 not found!");
    }
    M5.Display.fillRect(0, 0, 320, 240, WHITE);
    M5.Display.setTextColor(BLACK);
    M5.Display.setFont(&fonts::FreeMonoBold18pt7b);
    M5.Display.setCursor(0, 0);
    M5.Display.printf("M5Unit-Step16\n");
    step16.setRgbConfig(1);
    step16.setRgbBrightness(RGB_BRIGHTNESS);
    lastRawValue = step16.getValue();
    currentDigit = mapRawValueToDigit(lastRawValue);
    updateDisplay(currentDigit);
}

void loop()
{
    uint8_t rawValue = step16.getValue();
    if (rawValue != lastRawValue && !isFirstRead) {
        handleValueChange(lastRawValue, rawValue);
        lastRawValue = rawValue;
        M5.Display.fillRect(0, 0, 320, 240, WHITE);
        M5.Display.setCursor(0, 0);
        M5.Display.printf("Raw Value: %d\n", rawValue);
    }
    if (isFirstRead)    isFirstRead = false;
    delay(50);
}

/**
 * @brief Handle value change
 * @param oldVal Old raw value
 * @param newVal New raw value
 */
void handleValueChange(uint8_t oldVal, uint8_t newVal)
{
    if (newVal >= 9 && newVal <= 15) {
        uint8_t currentDirection = step16.getSwitchState();
        step16.setSwitchState(currentDirection == 0 ? 1 : 0);
    }
    uint8_t newDigit = mapRawValueToDigit(newVal);
    if (newDigit != currentDigit) {
        currentDigit = newDigit;
        updateDisplay(currentDigit);
    }
}

/**
 * @brief Map raw value to digit 0-8
 * @param rawValue Raw value (0-15)
 * @return Mapped digit (0-8)
 */
uint8_t mapRawValueToDigit(uint8_t rawValue)
{
    if (rawValue <= 8) {
        return rawValue;
    } else {
        return 17 - rawValue;
    }
}

/**
 * @brief Update display
 * @param digit Digit to display (0-8)
 */
void updateDisplay(uint8_t digit)
{
    if (digit > MAX_DIGIT) return;
    step16.setLedBrightness(digitBrightness[digit]);
    step16.setRgb(digitColors[digit].r, digitColors[digit].g, digitColors[digit].b);
    step16.setLedConfig(LED_ALWAYS_ON);
}
```

## 4. 编译上传

- 下载模式：设备进行程序烧录前需要进入下载模式，不同的主控设备该步骤可能有所不同。详情可参考 [Arduino IDE 上手教程](/zh_CN/arduino/arduino_ide)页面底部的设备程序下载教程列表，查看具体的操作方式。

- CoreS3 长按复位按键 (大约 2 秒) 直到内部绿色 LED 灯亮起，便可松开，此时设备已进入下载模式，等待烧录。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5CORES3%20SE/cores3%20(2).gif" width="30%">

- 选中设备端口，点击 Arduino IDE 左上角编译上传按钮，等待程序完成编译并上传至设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1125/module_fan_v1.1_arduino_example_01.jpg" width="70%">

## 5. 数码管显示

- 程序初始状态晶体管显示为 0 ，当转动旋钮后，晶体管的数字会随着旋转而改变，RGB 灯的颜色也会随之变换。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1160/Unit_Step16_1.jpg" width="60%"><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1160/Unit_Step16_2.jpg" width="60%"><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1160/Unit_Step16_3.jpg" width="60%">
