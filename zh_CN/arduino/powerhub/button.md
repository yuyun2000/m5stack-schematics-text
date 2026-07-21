# PowerHub Button 按键

PowerHub Button 按键相关 API 与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.3
- 开发板选项 = M5PowerHub
- M5Unified 库版本 >= 0.2.11

```cpp line-num
#include "M5Unified.h"

void setup() {
  M5.begin();
  Serial.begin(115200);
}

void loop() {
  M5.update();

  if (M5.BtnA.wasPressed()) {
    Serial.println("BtnA was pressed");
  }
  if (M5.BtnA.wasReleased()) {
    Serial.println("BtnA was released");
  }
  if (M5.BtnA.wasSingleClicked()) {
    Serial.println("BtnA was single clicked");
  }
  if (M5.BtnA.wasDoubleClicked()) {
    Serial.println("BtnA was double clicked");
  }
  if (M5.BtnA.wasHold()) {
    Serial.println("BtnA was held");
  }
  if (M5.BtnA.wasReleaseFor(5000)) {  // ms
    Serial.println("BtnA was released after being held for 5000 ms");
  }

  if (M5.BtnB.wasPressed()) {
    Serial.println("BtnB was pressed");
  }
  if (M5.BtnB.wasReleased()) {
    Serial.println("BtnB was released");
  }
  if (M5.BtnB.wasSingleClicked()) {
    Serial.println("BtnB was single clicked");
  }
  if (M5.BtnB.wasDoubleClicked()) {
    Serial.println("BtnB was double clicked");
  }
  if (M5.BtnB.wasHold()) {
    Serial.println("BtnB was held");
  }
  if (M5.BtnB.wasReleaseFor(5000)) {  // ms
    Serial.println("BtnB was released after being held for 5000 ms");
  }

  delay(10);
}
```

该程序将检测设备上两个按键（黄色圆形按键为 BtnA，矩形半透明按键为 BtnB）的状态（包括按下、松开、短按一次、短按两次、长按、长按 5000 毫秒后松开等），并在串口监视器打印消息：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1183/Arduino_BtnAB.png" width="50%">

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1183/Arduino_button.png" width="90%">

## API

PowerHub Button 按键部分驱动使用了`M5Unified`库中的`Button_Class`，更多相关的 API 可以参考下方文档：

- [M5Unified - Button Class](/zh_CN/arduino/m5unified/button_class)