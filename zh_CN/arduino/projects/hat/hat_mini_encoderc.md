# Hat Mini EncoderC Arduino 使用教程

## 1. 准备工作

- 环境配置： 参考 [Arduino IDE 上手教程](/zh_CN/arduino/arduino_ide)完成 IDE 安装，并根据实际使用的开发板安装对应的板管理，与需要的驱动库。
- 使用到的驱动库：
  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5GFX](https://github.com/m5stack/M5GFX)
  - [M5Hat-Mini-EncoderC](https://github.com/m5stack/M5Hat-Mini-EncoderC)

- 使用到的硬件产品：
  - [StickC Plus](https://shop.m5stack.com/products/m5stickc-plus-esp32-pico-mini-iot-development-kit)
  - [Hat Mini EncoderC](https://shop.m5stack.com/products/m5stickc-mini-encoder-hat-stm32f030)

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc_plus/m5stickc_plus_cover_01.webp" width="20%"/> <img src="https://static-cdn.m5stack.com/resource/docs/products/hat/MiniEncoderC%20Hat/img-b20cb190-1185-4a4a-8ba4-a71f08ed00f2.webp" width="20%"/>

## 2. 注意事项

\#> 引脚兼容性 | 由于每款主机的引脚配置不同，使用前请参考产品文档中的[引脚兼容表](/zh_CN/hat/MiniEncoderC%20Hat)，并根据实际引脚连接情况修改案例程序。

<ProductCompatible sku="U157" type="HAT"></ProductCompatible> 

## 3. 案例程序

- 本教程中使用的主控设备为 StickC Plus，搭配 Hat Mini EncoderC 模块。本旋钮模块采用 I2C 方式通讯，根据实际的电路连接修改程序中的引脚定义，设备堆叠后对应的 I2C IO 为 `G26 (SCL)`，`G0 (SDA)`。

```cpp line-num
#include "M5Unified.h"
#include "M5HatMiniEncoderC.h"

// MiniEncoderC I2C pins
#define MiniEncoderC_SDA 0
#define MiniEncoderC_SCL 26

M5HatMiniEncoderC encoder;

// Used to detect encoder value changes
int32_t lastEncoderValue = 0;
int32_t encoderIncValue = 0;

// Used to detect button state changes
bool lastEncoderBtnValue = 0;

// Wait until MiniEncoderC is ready
static void waitMiniEncoderCReady() {
    while (!encoder.begin(&Wire, MiniEncoderC_ADDR, MiniEncoderC_SDA, MiniEncoderC_SCL, 100000UL)) {
      delay(100);
    }
}

void setup() {
    M5.begin();
    M5.Display.setRotation(0);
    M5.Display.setFont(&fonts::FreeMonoBold9pt7b);
    M5.Display.fillScreen(BLACK);

    // Initialize MiniEncoderC
    waitMiniEncoderCReady();

    // Reset encoder value to 0
    encoder.setEncoderValue(0);
    delay(100);

    // Initial display
    M5.Display.setCursor(0, 20);
    M5.Display.printf("Val:%d", 0);

    M5.Display.setCursor(0, 50);
    M5.Display.printf("IncVal:%d", 0);

    M5.Display.drawLine(0, 80, 135, 80, ORANGE);

    M5.Display.setCursor(0, 90);
    M5.Display.printf("BtnVal:1");

    M5.Display.setCursor(0, 180);
    M5.Display.printf("BtnA:\n Reset Cntr");
}

void loop() {
    M5.update();

    // Read encoder value
    int32_t encoderValue = encoder.getEncoderValue();

    // Read encoder button state
    bool EncoderBtnValue = encoder.getButtonStatus();

    // Only read increment value when encoder value changes
    if (encoderValue != lastEncoderValue) {
      encoderIncValue = encoder.getIncrementValue();

      // Update encoder value display
      M5.Display.fillRect(0, 20, 135, 50, BLACK);
      M5.Display.setTextColor(WHITE, BLACK);

      M5.Display.setCursor(0, 20);
      M5.Display.printf("Val: %d", encoderValue);

      M5.Display.setCursor(0, 50);
      M5.Display.printf("IncVal: %d", encoderIncValue);

      M5.Display.drawLine(0, 80, 135, 80, ORANGE);

      // Set LED color based on encoder value
      uint8_t r = abs(encoderValue * 5) % 256;
      uint8_t g = abs(encoderValue * 3) % 256;
      uint8_t b = abs(encoderValue * 7) % 256;
      uint32_t rgb888 = (r << 16) | (g << 8) | b;
      encoder.setLEDColor(rgb888);

      lastEncoderValue = encoderValue;
    }

    // Update display only when button state changes
    if (EncoderBtnValue != lastEncoderBtnValue) {
      M5.Display.fillRect(0, 90, 135, 80, BLACK);
      M5.Display.setCursor(0, 90);
      M5.Display.printf("BtnVal: %d", EncoderBtnValue);
      lastEncoderBtnValue = EncoderBtnValue;
    }

    if (M5.BtnA.wasPressed()) {
      // Reset encoder value to 0 when BtnA is pressed
      encoder.resetCounter();
    }

    delay(30);
}
```

## 4. 控制效果

- 设备上电后，旋转旋钮可以改变屏幕上显示的数值，同时背后的 RGB LED 颜色也会随数值变化而变化，按下旋钮按钮可以切换按钮状态显示，按下 StickC Plus 按键 A 可以将旋钮数值重置为 0。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/611/Hat_Mini_EncoderC_Arduino_pic.jpg" width="40%">
