# NanoC6 Blue LED 灯

NanoC6 Blue LED 灯相关 API 与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.5
- 开发板选项 = M5NanoC6
- M5NanoC6 库版本 = 1.0.0

```cpp line-num
#include <M5NanoC6.h>
#define BLUE_LED_PIN 7
bool blue_ledState = false;

void setup() {
  NanoC6.begin();
  pinMode(BLUE_LED_PIN, OUTPUT);
}

void loop() {
  blue_ledState = !blue_ledState;
  digitalWrite(BLUE_LED_PIN, blue_ledState);
  delay(1000);
}
```

该程序将控制设备上的蓝色 LED 灯以 1 秒间隔闪烁，可用于状态指示或调试：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/505/NanoC6_Arduino_tutorial_LED_part_01.jpg" width="70%">
