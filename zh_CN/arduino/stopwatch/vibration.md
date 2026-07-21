# StopWatch Vibration 振动电机

StopWatch 振动电机相关 API 与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.3.7
- 开发板选项 = M5StopWatch
- M5Unified 库版本 >= 0.2.15
- M5GFX 库版本 >= 0.2.21

```cpp line-num
#include <M5Unified.h>

void setup(void) {
  auto cfg = M5.config();
  M5.begin(cfg);

  M5.Display.setTextDatum(middle_center);
  M5.Display.setTextFont(&fonts::FreeMonoBold12pt7b);
  M5.Display.setTextSize(1);
  M5.Display.drawString("Vibration Test", M5.Display.width() / 2, M5.Display.height() / 2);
}

void loop(void) {
  M5.Power.setVibration(10);
  delay(500);
  M5.Power.setVibration(40);
  delay(500);
  M5.Power.setVibration(70);
  delay(500);
  M5.Power.setVibration(100);
  delay(500);
  M5.Power.setVibration(130);
  delay(500);
  M5.Power.setVibration(160);
  delay(500);
  M5.Power.setVibration(190);
  delay(500);
  M5.Power.setVibration(210);
  delay(500);
  M5.Power.setVibration(240);
  delay(500);
}
```

StopWatch 振动电机以逐渐增强的强度循环振动，效果如下：

<video style="width:40vw;max-width:40%;height:auto;" controls>
  <source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1242/StopWatch_Arduino_vibration.mp4" type="video/mp4"></video>

## API

StopWatch 振动电机部分使用了 `M5Unified` 库中的 `Power_Class`，更多相关的API可以参考下方文档：

- [M5Unified - Power Class](/zh_CN/arduino/m5unified/power_class)