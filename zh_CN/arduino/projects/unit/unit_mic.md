# Unit MIC Arduino 使用教程

## 1. 准备工作

- 环境配置： 参考 [Arduino IDE 上手教程](/zh_CN/arduino/arduino_ide)完成 IDE 安装，并根据实际使用的开发板安装对应的板管理，与需要的驱动库。

- 使用到的驱动库：
  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5GFX](https://github.com/m5stack/M5GFX)

- 使用到的硬件产品：
  - [Core2 v1.1](https://shop.m5stack.com/products/m5stack-core2-esp32-iot-development-kit)
  - [Unit MIC](https://shop.m5stack.com/products/microphone-unit-lm393)

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/Core2%20v1.1/img-9eb726ec-5729-42c3-9cce-e06140856095.webp" width="20%"><img src="https://static-cdn.m5stack.com/resource/docs/products/unit/mic/mic_cover_01.webp" width="20%">

## 2. 注意事项

\#> 引脚兼容性 | 由于每款主机的引脚配置不同，为了让用户更方便地使用，M5Stack 官方提供了引脚兼容性表，方便用户查看，请根据实际引脚连接情况修改案例程序。

<ProductCompatible sku="U096" type="UNIT"></ProductCompatible>

## 3. 案例程序

本教程中使用的主控设备为 Core2 v1.1 ，搭配 Unit MIC。请根据实际的电路连接修改程序中的引脚定义，设备连接后对应的引脚为 `G33 (AIN)`，`G32 (DIN)`。

```cpp line-num
#include <M5Unified.h>
#include <M5GFX.h>

// Input pins
#define AIN_PIN 33      // Analog input pin
#define DIN_PIN 32      // Digital input pin (ADC)
#define LCD_W 320
#define LCD_H 240
#define MAX_LEN LCD_W   // Buffer length (matches screen width)
#define X_OFFSET 0

#define Y_AIN_OFFSET 60   // Vertical offset for AIN waveform
#define Y_DIN_OFFSET 150  // Vertical offset for DIN waveform
#define X_SCALE 1         // Amplitude scaling factor

// Draw real-time waveforms and values for AIN and DIN channels
static void draw_waveform_dual() {
  static int16_t ain_buf[MAX_LEN] = {0};  // Buffer for AIN samples
  static int16_t din_buf[MAX_LEN] = {0};  // Buffer for DIN samples
  static int16_t pt = MAX_LEN - 1;        // Circular buffer pointer

  int ainValue = analogRead(AIN_PIN);     // Read AIN ADC value
  int dinValue = analogRead(DIN_PIN);     // Read DIN ADC value

  // Map AIN: higher ADC values produce higher positions
  ain_buf[pt] = map((int16_t)(ainValue * X_SCALE), 1800, 4095, 0, 80);

  // Map DIN: ADC=0 at waveform bottom, ADC=4095 at waveform top
  din_buf[pt] = map((int16_t)(dinValue * X_SCALE), 0, 4095, 80, 0);

  if (--pt < 0) pt = MAX_LEN - 1;         // Circular buffer wrap-around

  for (int i = 1; i < MAX_LEN; i++) {
    uint16_t now_pt = (pt + i) % MAX_LEN;

    // Erase previous AIN waveform points
    M5.Lcd.drawLine(
      i + X_OFFSET,
      ain_buf[(now_pt + 1) % MAX_LEN] + Y_AIN_OFFSET,
      i + 1 + X_OFFSET,
      ain_buf[(now_pt + 2) % MAX_LEN] + Y_AIN_OFFSET,
      TFT_BLACK);

    // Erase previous DIN waveform points
    M5.Lcd.drawLine(
      i + X_OFFSET,
      din_buf[(now_pt + 1) % MAX_LEN] + Y_DIN_OFFSET,
      i + 1 + X_OFFSET,
      din_buf[(now_pt + 2) % MAX_LEN] + Y_DIN_OFFSET,
      TFT_BLACK);

    if (i < MAX_LEN - 1) {
      // Draw current AIN waveform in green
      M5.Lcd.drawLine(
        i + X_OFFSET,
        ain_buf[now_pt] + Y_AIN_OFFSET,
        i + 1 + X_OFFSET,
        ain_buf[(now_pt + 1) % MAX_LEN] + Y_AIN_OFFSET,
        TFT_GREEN);

      // Draw current DIN waveform in cyan
      M5.Lcd.drawLine(
        i + X_OFFSET,
        din_buf[now_pt] + Y_DIN_OFFSET,
        i + 1 + X_OFFSET,
        din_buf[(now_pt + 1) % MAX_LEN] + Y_DIN_OFFSET,
        TFT_CYAN);
    }
  }

  // Display current AIN ADC value (upper area)
  M5.Lcd.fillRect(10, Y_AIN_OFFSET - 25, 100, 20, TFT_BLACK);
  M5.Lcd.setTextColor(TFT_GREEN, TFT_BLACK);
  M5.Lcd.setTextFont(&fonts::FreeMonoBold9pt7b);
  M5.Lcd.setTextDatum(TL_DATUM);
  M5.Lcd.drawString("AIN: " + String(ainValue), 10, Y_AIN_OFFSET - 24);

  // Display current DIN ADC value (lower area)
  M5.Lcd.fillRect(10, Y_DIN_OFFSET + 80 - 25, 100, 20, TFT_BLACK);
  M5.Lcd.setTextColor(TFT_CYAN, TFT_BLACK);
  M5.Lcd.drawString("DIN: " + String(dinValue), 10, Y_DIN_OFFSET + 80 - 24);
}

void setup() {
  M5.begin();
  M5.Lcd.setTextFont(&fonts::FreeMonoBold9pt7b);
  M5.Lcd.setTextDatum(top_center);

  // AIN waveform label
  M5.Lcd.setTextColor(TFT_GREEN, TFT_BLACK);
  M5.Lcd.setTextDatum(top_center);
  M5.Lcd.drawString("AIN Wave", 220, Y_AIN_OFFSET - 24);

  // DIN waveform label (near bottom)
  M5.Lcd.setTextColor(TFT_CYAN, TFT_BLACK);
  M5.Lcd.drawString("DIN Wave", 220, Y_DIN_OFFSET + 80 - 24);
}

void loop() {
  draw_waveform_dual();
}
```

## 4. 编译上传

- 选中设备端口（详情请参考 [程序编译与烧录](/zh_CN/arduino/m5core2/program)），点击 Arduino IDE 左上角编译上传按钮，等待程序完成编译并上传至设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/733/Unit_MIC_arduino_example.png" width="70%">

## 5. 麦克风功能效果展示

- 该例程效果为实时绘制音频波形和采集到的 ADC 值，主控设备显示如下图所示。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/733/Unit_MIC_wav_example.jpg" width="35%">



