# Paper Battery 电池状态

Paper 电池状态相关API与案例程序。

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
  M5.Display.setFont(&fonts::FreeMonoBold18pt7b);
  M5.Display.setEpdMode(epd_text);  // epd_quality, epd_text, epd_fast, epd_fastest
  M5.Display.clear();

  M5.Display.setCursor(0, 200);
  M5.Display.println("     Paper Realtime");
  M5.Display.println("     Battery Status\n\n");
  M5.Display.println(" Battery   Level:\n");
  M5.Display.println(" Battery Voltage:\n");
}

void loop() {
  M5.update();

  int32_t batteryLevel = M5.Power.getBatteryLevel();      // 0 - 100 %
  int16_t batteryVoltage = M5.Power.getBatteryVoltage();  // unit: mV

  M5.Display.setCursor(360, 340);
  M5.Display.printf(" %3d %%", batteryLevel);
  M5.Display.setCursor(360, 410);
  M5.Display.printf("%4d mV", batteryVoltage);

  delay(2000);
}
```

该程序将在屏幕上显示电池电量百分比、电池电压，每2秒刷新一次。由于硬件限制，Paper 无法读取电池是否正在充电、电池电流。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/689/Paper_Arduino_battery.jpeg" width="50%">

## API

Paper 电池状态部分使用了 `M5Unified` 库中的 `Power_Class`，更多相关的API可以参考下方文档：

- [M5Unified - Power Class](/zh_CN/arduino/m5unified/power_class)