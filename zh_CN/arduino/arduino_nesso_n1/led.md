# Arduino Nesso N1 LED 指示灯

Arduino Nesso N1 LED 指示灯相关API与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.5
- 开发板选项 = ArduinoNessoN1
- M5GFX 库版本 >= 0.2.17
- M5Unified 库版本 >= 0.2.11

```cpp line-num
#include "M5Unified.h"

void setup() {
  auto cfg = M5.config();
  M5.begin(cfg);
}

void loop() {

  // LED_BUILTIN at E1.P7
  auto& ioe = M5.getIOExpander(1);
  ioe.digitalWrite(7, false);
  delay(1000);
  ioe.digitalWrite(7, true);
  delay(1000);
}
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1198/arduino_nesso_n1_led_example_01.jpg" width="50%" />
