# Hat Mini JoyC Arduino 使用教程

## 1. 准备工作

- 环境配置： 参考 [Arduino IDE 上手教程](/zh_CN/arduino/arduino_ide)完成 IDE 安装，并根据实际使用的开发板安装对应的板管理，与需要的驱动库。

- 使用到的驱动库：
  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5GFX](https://github.com/m5stack/M5GFX)
  - [M5Hat-Mini-JoyC](https://github.com/m5stack/M5Hat-Mini-JoyC)

- 使用到的硬件产品：
  - [StickC Plus](https://shop.m5stack.com/products/m5stickc-plus-esp32-pico-mini-iot-development-kit)
  - [Hat Mini JoyC](https://shop.m5stack.com/products/m5stickc-mini-joyc-hat-stm32f030)

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc_plus/m5stickc_plus_cover_01.webp" width="20%"/> <img src="https://static-cdn.m5stack.com/resource/docs/products/hat/MiniJoyC/img-08befb22-8188-417a-a35b-4e1b5d4f269c.webp" width="20%"/>

## 2. 注意事项

\#> 引脚兼容性 | 由于每款主机的引脚配置不同，使用前请参考产品文档中的[引脚兼容表](/zh_CN/hat/MiniJoyC)，并根据实际引脚连接情况修改案例程序。

<ProductCompatible sku="U156" type="HAT"></ProductCompatible> 

## 3. 案例程序

- 本教程中使用的主控设备为 StickC Plus，搭配 Hat Mini JoyC 模块。本摇杆模块采用 I2C 方式通讯，根据实际的电路连接修改程序中的引脚定义，设备堆叠后对应的 I2C IO 为 `G26 (SCL)`，`G0 (SDA)`。

```cpp line-num
#include "M5Unified.h"
#include "M5HatMiniJoyC.h"

// MiniJoyC I2C pins
#define MiniJoyC_SDA 0
#define MiniJoyC_SCL 26

M5HatMiniJoyC joyc;

// Wait until MiniJoyC is ready
static void waitMiniJoyCReady() {
  while (!joyc.begin(&Wire, MiniJoyC_ADDR, MiniJoyC_SDA, MiniJoyC_SCL, 100000UL)) {
    delay(100);
  }
}

void setup() {
  M5.begin();
  waitMiniJoyCReady();

  M5.Display.setRotation(0);
  M5.Display.setFont(&fonts::FreeMonoBold9pt7b);
  M5.Display.fillScreen(BLACK);
}

void loop() {
  M5.update();

  // Read raw ADC values (0~4095)
  int16_t adc_x = joyc.getADCValue(ADC_X);
  int16_t adc_y = joyc.getADCValue(ADC_Y);

  // Read normalized position (-128~127)
  int8_t pos_x = joyc.getPOSValue(POS_X, _8bit);
  int8_t pos_y = joyc.getPOSValue(POS_Y, _8bit);

  // Display values
  M5.Display.fillScreen(BLACK);
  M5.Display.setTextColor(WHITE, BLACK);

  M5.Display.setCursor(0, 20);
  M5.Display.printf("ADC X:%4d", adc_x);
  M5.Display.setCursor(0, 50);
  M5.Display.printf("ADC Y:%4d", adc_y);

  M5.Display.drawLine(0, 80, 135, 80, ORANGE);

  M5.Display.setCursor(0, 100);
  M5.Display.printf("POS X:%4d", pos_x);
  M5.Display.setCursor(0, 130);
  M5.Display.printf("POS Y:%4d", pos_y);

  M5.Display.drawLine(0, 160, 135, 160, ORANGE);

  M5.Display.setCursor(0, 180);
  M5.Display.printf("BtnVal: %d", joyc.getButtonStatus());

  // Map joystick to RGB888
  uint8_t r = constrain(map(-pos_y, -128, 127, 0, 255), 0, 255);
  uint8_t g = constrain(map( pos_y, -128, 127, 0, 255), 0, 255);
  uint8_t b = constrain(map( pos_x, -128, 127, 0, 255), 0, 255);

  // Center dead zone → white
  if (abs(pos_x) < 8 && abs(pos_y) < 8) {
    r = g = b = 255;
  }

  // Combine to RGB888 (0xRRGGBB)
  uint32_t rgb888 = (r << 16) | (g << 8) | b;

  // Set MiniJoyC LED color
  joyc.setLEDColor(rgb888);

  delay(30);
}
```

## 4. 控制效果

- 设备上电后，摇动摇杆可以改变屏幕上显示的数值，同时背后的 RGB LED 颜色也会随摇杆位置变化而变化，按下摇杆按钮可以切换按钮状态显示。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/610/Hat_Mini_JoyC_Arduino_pic.jpg" width="40%">
