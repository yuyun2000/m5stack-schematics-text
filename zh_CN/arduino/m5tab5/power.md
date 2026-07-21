# Tab5 Power 电源管理

Tab5 Power 电源管理相关 API 与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.2
- 开发板选项 = M5Tab5
- M5Unified 库版本 >= 0.2.17
- M5GFX 库版本 >= 0.2.22

```cpp line-num
#include "M5Unified.h"

void setup()
{
    auto cfg = M5.config();
    M5.begin(cfg);
    M5.Display.setRotation(3);
    M5.Display.setTextDatum(top_center);
    M5.Display.setFont(&fonts::FreeMonoBold24pt7b);
    M5.Display.clear(WHITE);
    M5.Display.drawString("Tab5 Power Manager", M5.Lcd.width() / 2, 0);
}

void loop()
{
    M5.Display.clear();
    bool bat_ischarging = M5.Power.isCharging();
    M5.Display.setCursor(0, 100);
    M5.Display.printf("Bat Charging: %s\n", bat_ischarging ? "Yes" : "No");
    int bat_vol = M5.Power.getBatteryVoltage();
    M5.Display.printf("Bat Voltage: %dmv\n", bat_vol);
    int bat_level = M5.Power.getBatteryLevel();
    M5.Display.printf("Bat Level: %d\n", bat_level);
    delay(1000);
}
```

## 电源输出控制

- M5-Bus, HY2.0-4P, 2.54-10P Bus, USB-A 的 5V 输出在 M5.begin () 中默认启用。用户可根据开发需求，参考以下 API 进行配置。

```cpp
M5.Power.setExtOutput(true);
// M5.Power.setExtOutput(false);
```

- 如果需要单独控制 USB-A 电源或扩展口电源，可使用以下 API：
  - ext_PA：控制 M5-Bus / HY2.0-4P / 2.54-10P Bus（共用开关，不支持独立控制）
  - ext_USB：仅控制 USB-A

```cpp
M5.Power.setExtOutput(false, m5::ext_port_mask_t::ext_PA);
M5.Power.setExtOutput(false, m5::ext_port_mask_t::ext_USB);
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/tab5_arduino_power_manager_demo_01.jpg" width="50%">

## API

Tab5 电源管理驱动使用了 M5Unified 库中的`Power_Class`, 更多相关的 API 可以参考下方文档:

- [M5Unified - Power Class](/zh_CN/arduino/m5unified/power_class)
