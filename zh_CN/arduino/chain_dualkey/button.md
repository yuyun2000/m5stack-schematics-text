# Chain DualKey Button 按键

Chain DualKey Button 按键相关 API 与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.4
- 开发板选项 = M5ChainDualKey
- M5Unified 库版本 >= 0.2.11

```cpp line-num
#include "M5Unified.h"

#define pin_Key1 0
#define pin_Key2 17

m5::Button_Class Key1;
m5::Button_Class Key2;

void setup() {
  pinMode(pin_Key1, INPUT);
  pinMode(pin_Key2, INPUT);

  Serial.begin(115200);
}

void loop() {
  uint32_t ms = millis();
  Key1.setRawState(ms, !digitalRead(pin_Key1));
  Key2.setRawState(ms, !digitalRead(pin_Key2));

  if (Key1.wasPressed()) {
    Serial.println("Key1 was pressed");
  }
  if (Key1.wasReleased()) {
    Serial.println("Key1 was released");
  }
  if (Key1.wasSingleClicked()) {
    Serial.println("Key1 was single clicked");
  }
  if (Key1.wasDoubleClicked()) {
    Serial.println("Key1 was double clicked");
  }
  if (Key1.wasHold()) {
    Serial.println("Key1 was held");
  }
  if (Key1.wasReleaseFor(5000)) {  // ms
    Serial.println("Key1 was released after being held for 5000 ms");
  }

  if (Key2.wasPressed()) {
    Serial.println("Key2 was pressed");
  }
  if (Key2.wasReleased()) {
    Serial.println("Key2 was released");
  }
  if (Key2.wasSingleClicked()) {
    Serial.println("Key2 was single clicked");
  }
  if (Key2.wasDoubleClicked()) {
    Serial.println("Key2 was double clicked");
  }
  if (Key2.wasHold()) {
    Serial.println("Key2 was held");
  }
  if (Key2.wasReleaseFor(5000)) {  // ms
    Serial.println("Key2 was released after being held for 5000 ms");
  }

  delay(10);
}
```

该程序将检测设备上两个按键（远离挂绳孔的为 Key1，靠近挂绳孔的为 Key2）的状态（包括按下、松开、短按一次、短按两次、长按、长按 5000 毫秒后松开等），并在串口监视器打印消息：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/Keys.jpg" width="30%">

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/Arduino_button.png" width="90%">

## API

Chain DualKey Button 按键部分驱动使用了`M5Unified`库中的`Button_Class`，更多相关的 API 可以参考下方文档：

- [M5Unified - Button Class](/zh_CN/arduino/m5unified/button_class)