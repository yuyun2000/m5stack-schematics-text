# Paper Button 滚轮按键

Paper 滚轮按键相关API与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 2.1.4
- 开发板选项 = M5Paper
- M5Unified 库版本 >= 0.2.5
- M5GFX 库版本 >= 0.2.7

```cpp line-num
#include <M5Unified.h>
#include <M5GFX.h>

void setup() {
  M5.begin();
  M5.Display.setRotation(0);
  M5.Display.setFont(&fonts::FreeMonoBold24pt7b);
  M5.Display.setEpdMode(epd_fast);  // epd_quality, epd_text, epd_fast, epd_fastest
  Serial.begin(115200);

  M5.Display.clear();
  M5.Display.setCursor(20, 100);
  M5.Display.print("Rotary Button Test");
  Serial.println("Rotary Button Test");

  M5.Display.setCursor(40, 300);
  M5.Display.print("____ was pressed");
}

void loop() {
  M5.update();

  if (M5.BtnA.wasPressed()) {
    M5.Display.setCursor(40, 300);
    M5.Display.print("BtnA was pressed");
    Serial.println("BtnA was pressed");
  }
  if (M5.BtnB.wasPressed()) {
    M5.Display.setCursor(40, 300);
    M5.Display.print("BtnB was pressed");
    Serial.println("BtnB was pressed");
  }
  if (M5.BtnC.wasPressed()) {
    M5.Display.setCursor(40, 300);
    M5.Display.print("BtnC was pressed");
    Serial.println("BtnC was pressed");
  }
}
```

该程序将在屏幕上显示按钮状态，其中`BtnA`为滚轮向上（G37），`BtnB`为滚轮按压（G38），`BtnC`为滚轮向下（G39）。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/689/Paper_Arduino_button.jpeg" width="50%">

## API

Paper 按键部分使用了 `M5Unified` 库中的 `Button_Class`，更多相关的API可以参考下方文档：

- [M5Unified - Button Class](/zh_CN/arduino/m5unified/button_class)