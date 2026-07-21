# StopWatch Power 电源管理

StopWatch 电源管理相关 API 与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.3.7
- 开发板选项 = M5StopWatch
- M5Unified 库版本 >= 0.2.15
- M5GFX 库版本 >= 0.2.21

```cpp line-num
#include <M5Unified.h>

void setup() {
    M5.begin();
    Serial.begin(115200);
    M5.Lcd.setRotation(0);
    M5.Lcd.setFont(&fonts::FreeMonoBold12pt7b);

    M5.Lcd.setTextDatum(middle_center);
    M5.Lcd.drawString("StopWatch Realtime", M5.Lcd.width() / 2, 50);
    M5.Lcd.drawString("Battery Status\n",  M5.Lcd.width() / 2, 80);
    M5.Lcd.setCursor(40, 170);
    M5.Lcd.print("Battery Charging:");
    M5.Lcd.setCursor(40, 210);
    M5.Lcd.print("Battery    Level:");
    M5.Lcd.setCursor(40, 250);
    M5.Lcd.print("Battery  Voltage:");
}

void loop() {
  M5.update();

  bool    isCharging     = M5.Power.isCharging();
  int32_t batteryLevel   = M5.Power.getBatteryLevel();    // 0 - 100 %
  int16_t batteryVoltage = M5.Power.getBatteryVoltage();  // unit: mV

  M5.Lcd.setCursor(290, 170);
  M5.Lcd.printf("%s \n", isCharging ? "Yes" : "No");

  M5.Lcd.setCursor(290, 210);
  M5.Lcd.printf("%d %%\n", batteryLevel);

  M5.Lcd.setCursor(290, 250);
  M5.Lcd.printf("%d mV\n", batteryVoltage);

  delay(2000);
}
```

该程序将在屏幕上显示电池是否正在充电、电量百分比、电池电压，每2秒刷新一次。由于硬件限制，StopWatch 无法读取电池电流。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1242/StopWatch_Arduino_battery.jpg" width="50%">

## API

StopWatch 电池状态部分使用了 `M5Unified` 库中的 `Power_Class`，更多相关的API可以参考下方文档：

- [M5Unified - Power Class](/zh_CN/arduino/m5unified/power_class)