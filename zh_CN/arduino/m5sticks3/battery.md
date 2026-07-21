# StickS3 Battery 电池

StickS3 电池状态读取相关 API 与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.5
- 开发板选项 = M5StickS3
- M5Unified 库版本 >= 0.2.12
- M5GFX 库版本 >= 0.2.18

```cpp line-num
#include "M5Unified.h"

void setup()
{
    M5.begin();
    Serial.begin(115200);
    M5.Lcd.setTextDatum(middle_center);
    M5.Lcd.setTextFont(&fonts::FreeMonoBold9pt7b);
    M5.Lcd.setTextSize(1);
    M5.Lcd.setRotation(1);
}

void loop()
{
    M5.Lcd.clear();
    
    bool isCharging = M5.Power.isCharging();
    int vol_per = M5.Power.getBatteryLevel();
    int vol = M5.Power.getBatteryVoltage();

    M5.Lcd.setCursor(0, 30);
    M5.Lcd.printf("Charging: %s \n\n", isCharging ? "Yes" : "No");
    M5.Lcd.setCursor(0, 60);
    M5.Lcd.printf("Bat_level: %d%%", vol_per);
    M5.Lcd.setCursor(0, 90);
    M5.Lcd.printf("Bat_voltage: %d%mV", vol);
    delay(2000);
}                           
```

该程序将在屏幕上显示电池是否正在充电、电量百分比、电池电压信息，每 2 秒刷新一次。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/StickS3_Arduino_battery.jpg" width="40%">

## API

StickS3 电源部分使用了 `M5Unified` 库中的 `Power_Class` , 更多相关的API可以参考下方文档:

- [M5Unified - Power Class](/zh_CN/arduino/m5unified/power_class)
