# Fire Battery 电池

Fire 电池状态读取相关 API 与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.2
- 开发板选项 = M5Fire
- M5Unified 库版本 >= 0.2.8
- M5GFX 库版本 >= 0.2.11

```cpp line-num
#include "M5Unified.h"

void setup() {
  M5.begin();
  M5.Display.setFont(&fonts::FreeMonoBold12pt7b);

  M5.Display.clear();
  M5.Display.setCursor(0, 0);
  M5.Display.print("Fire Battery Status");
}

void loop() {
  M5.update();
  bool isCharging = M5.Power.isCharging();
  int batteryLevel = M5.Power.getBatteryLevel();  // 0 - 100 %

  M5.Display.setCursor(0, 50);
  M5.Display.printf("  isCharging: %-3s", isCharging ? "Yes" : "No");

  M5.Display.setCursor(0, 100);
  M5.Display.printf("batteryLevel: %3d %%", batteryLevel);

  delay(1000);
}
```

该程序将在屏幕上显示电池是否正在充电、电量百分比，每秒刷新一次。

由于硬件限制，Fire 无法读取电池电压、电流信息，读取的电量百分比只有五档（0%、25%、50%、75%、100%，百分比与电压的对应关系见 [产品页面](/zh_CN/core/fire_v2.7)）。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/658/Arduino_battery.jpg" width="50%">

## API

Fire 电池部分使用了`M5Unified`库中的`Power_Class`，更多相关的 API 可以参考下方文档：

- [M5Unified - Power Class](/zh_CN/arduino/m5unified/power_class)