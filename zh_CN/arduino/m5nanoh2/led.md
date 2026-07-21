# NanoH2 Blue LED 灯

NanoH2 Blue LED 灯相关 API 与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.5
- 开发板选项 = M5NanoH2

```cpp line-num
#define BLUE_LED_PIN 4

bool blue_ledState = false;

void setup() {
  Serial.begin(115200);
  pinMode(BLUE_LED_PIN, OUTPUT);
}

void loop() {
  blue_ledState = !blue_ledState;
  digitalWrite(BLUE_LED_PIN, blue_ledState);
  delay(1000);
}
```

该程序将控制设备上的蓝色 LED 灯以 1 秒间隔闪烁，可用于状态指示或调试：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1204/arduino_nanoh2_blue_led_example_01.jpg" width="70%" >
