# Cardputer Battery 电池状态

Cardputer 电池状态相关 API 与案例程序，适用于 Cardputer 和 Cardputer-Adv。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.3
- 开发板选项 = M5Cardputer
- M5Cardputer 库版本 >= 1.1.1
- M5Unified 库版本 >= 0.2.10

```cpp line-num
#include <M5Cardputer.h>

void setup() {
  M5Cardputer.begin();
  M5Cardputer.Display.setFont(&fonts::FreeMonoBold9pt7b);
  M5Cardputer.Display.setCursor(0, 0);

  M5Cardputer.Display.print("   Cardputer (-Adv)\n");
  M5Cardputer.Display.print("    Battery Status\n\n");
  M5Cardputer.Display.print("  Percent:\n");
  M5Cardputer.Display.print("  Voltage:\n");
}

void loop() {
  M5Cardputer.update();

  bool isCharging = M5Cardputer.Power.isCharging();
  int batteryLevel = M5Cardputer.Power.getBatteryLevel();      // 0 - 100 %
  int batteryVoltage = M5Cardputer.Power.getBatteryVoltage();  // unit: mV

  M5Cardputer.Display.setCursor(120, 55);
  M5Cardputer.Display.printf("%3d %%", batteryLevel);
  M5Cardputer.Display.setCursor(120, 72);
  M5Cardputer.Display.printf("%4d mV", batteryVoltage);

  delay(1000);
}
```

该程序将在屏幕上显示电池电量百分比、电池电压，每秒刷新一次。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/Arduino_battery.jpg" width="70%">

?>|由于硬件限制，Cardputer 及 Cardputer-Adv 无法读取电池是否正在充电、电池电流信息。<br>
请注意，Cardputer 及 Cardputer-Adv 连接电脑或电源时，必须打开上侧面的开关才会充电，否则电池断开，设备使用外部电源供电。

## API

Cardputer Battery 电池状态部分驱动使用了`M5Unified`库中的`Power_Class`，更多相关的 API 可以参考下方文档：

- [M5Unified - Power Class](/zh_CN/arduino/m5unified/power_class)