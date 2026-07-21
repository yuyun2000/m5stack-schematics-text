# Core2 Battery 电池

Core2 电池状态读取相关API与案例程序。

## 案例程序

```cpp line-num
#include "M5Unified.h"

void setup()
{
    auto cfg = M5.config();
    M5.begin(cfg);
    M5.Display.setTextDatum(middle_center);
    M5.Display.setTextColor(TFT_BLACK);
    M5.Display.setTextFont(&fonts::Orbitron_Light_24);
    M5.Display.setTextSize(1);
}

void loop()
{
    M5.Display.clear(TFT_WHITE);
    
    bool isCharging = M5.Power.isCharging();
    // Set LED based on charging status
    if (isCharging) {
        M5.Power.setLed(255); // Set LED to light when charging
    } else {
        M5.Power.setLed(0);
    }
    int vol_per = M5.Power.getBatteryLevel();
    int vol = M5.Power.getBatteryVoltage();
    int cur = M5.Power.getBatteryCurrent();

    M5.Display.setCursor(0, 30);
    M5.Display.printf("Charging: %s \n\n", isCharging ? "Yes" : "No");
    M5.Display.setCursor(0, 60);
    M5.Display.printf("Bat_level: %d%%", vol_per);
    M5.Display.setCursor(0, 90);
    M5.Display.printf("Bat_voltage: %d%mV", vol);
    M5.Display.setCursor(0, 120);
    M5.Display.printf("Bat_current: %d%mA", cur);
    delay(2000);
}                           
```

该程序将在屏幕上显示电池是否正在充电、电量百分比、电池电压、电流信息，每2秒刷新一次。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/644/core2_Arduino_battery.jpg" width="50%">

## API

Core2 电源部分使用了M5Unified库中的`Power_Class`, 更多相关的API可以参考下方文档:

- [M5Unified - Power Class](/zh_CN/arduino/m5unified/power_class)
