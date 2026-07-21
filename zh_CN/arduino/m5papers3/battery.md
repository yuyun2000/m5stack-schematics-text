# PaperS3 Battery 电池状态

PaperS3 电池状态相关API与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 2.1.4
- 开发板选项 = M5PaperS3
- M5Unified 库版本 >= 0.2.5
- M5GFX 库版本 >= 0.2.7

```cpp line-num
#include <M5Unified.h>
#include <M5GFX.h>

void setup() {
  M5.begin();
  M5.Display.setRotation(0);
  M5.Display.setFont(&fonts::FreeMonoBold18pt7b);

  M5.Display.setCursor(0, 200);

  M5.Display.print("    PaperS3 Realtime\n");
  M5.Display.print("     Battery Status\n\n\n");
  M5.Display.print(" Battery Charging:\n\n");
  M5.Display.print(" Battery    Level:\n\n");
  M5.Display.print(" Battery  Voltage:\n\n");
}

void loop() {
  M5.update();

  bool    isCharging     = M5.Power.isCharging();
  int32_t batteryLevel   = M5.Power.getBatteryLevel();    // 0 - 100 %
  int16_t batteryVoltage = M5.Power.getBatteryVoltage();  // unit: mV

  M5.Display.setCursor(380, 340);
  M5.Display.printf("%s \n\n", isCharging ? "Yes" : "No");

  M5.Display.setCursor(380, 410);
  M5.Display.printf("%d %%  \n\n", batteryLevel);

  M5.Display.setCursor(380, 480);
  M5.Display.printf("%d mV   \n\n", batteryVoltage);

  delay(2000);
}
```

该程序将在屏幕上显示电池是否正在充电、电量百分比、电池电压，每2秒刷新一次。由于硬件限制，PaperS3无法读取电池电流。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/517/PaperS3_Arduino_battery.jpeg" width="50%">

## API

PaperS3 电池状态部分使用了 `M5Unified` 库中的 `Power_Class`，更多相关的API可以参考下方文档：

- [M5Unified - Power Class](/zh_CN/arduino/m5unified/power_class)