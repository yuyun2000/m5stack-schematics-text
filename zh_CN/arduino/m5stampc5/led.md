# Stamp-C5 Blue LED 灯

Stamp-C5 Blue LED 灯相关 API 与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.3.8
- 开发板选项 = M5StampC5

```cpp line-num
#define BLUE_LED_PIN 28

bool blue_ledState = false;

void setup() {
  pinMode(BLUE_LED_PIN, OUTPUT);
}

void loop() {
  blue_ledState = !blue_ledState;
  digitalWrite(BLUE_LED_PIN, blue_ledState);
  delay(1000);
}
```

该程序将控制设备上的蓝色 LED 灯以 1 秒间隔闪烁，可用于状态指示或调试：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1258/Stamp-C5_Arduino_tutorial_LED_01.jpg" width="50%">
