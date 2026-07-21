# Arduino Nesso N1 Power 电源管理

Arduino Nesso N1 Power 电源管理相关 API 与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.5
- 开发板选项 = ArduinoNessoN1
- M5GFX 库版本 >= 0.2.17
- M5Unified 库版本 >= 0.2.11 (develop branch)

### 电池状态

启用电池充电，并显示当前电池电压和容量状态。

```cpp line-num
#include "M5Unified.h"

void setup()
{
    auto cfg = M5.config();
    M5.begin(cfg);
    M5.Display.setRotation(1);
    M5.Display.setTextColor(GREEN);
    M5.Display.setTextDatum(middle_center);
    M5.Display.setTextFont(&fonts::FreeSerifBoldItalic18pt7b);
    M5.Display.setTextSize(1);

    M5.Power.setBatteryCharge(true);
    M5.Power.setChargeCurrent(100);
    M5.Power.setChargeVoltage(4200);
}

void loop()
{
    M5.Display.clear();
    int vol = M5.Power.getBatteryVoltage();
    M5.Display.setCursor(10, 30);
    M5.Display.printf("Bat: %dmv", vol);
    int level = M5.Power.getBatteryLevel();
    M5.Display.setCursor(10, 65);
    M5.Display.printf("Level: %d%%", level);
    M5.Display.setCursor(10, 100);
    m5::Power_Class::is_charging_t status = M5.Power.isCharging();
    M5.Display.printf("Charging: %s", status == m5::Power_Class::is_charging_t::is_charging ? "YES" : "NO");
    delay(1000);
}
```


<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1198/arduino_nesso_n1_power_example_01.jpg" width="50%" />


### Grove 接口供电

开关 Grove 接口供电。

```cpp line-num
#include "M5Unified.h"

void setup() {
  auto cfg = M5.config();
  M5.begin(cfg);
  M5.Display.setRotation(1);
  M5.Display.setTextColor(GREEN);
  M5.Display.setTextDatum(middle_center);
  M5.Display.setTextFont(&fonts::FreeSerifBoldItalic18pt7b);
  M5.Display.setTextSize(1);

  M5.Power.setBatteryCharge(true);
  M5.Power.setChargeCurrent(100);
  M5.Power.setChargeVoltage(4200);
}

bool power_status = true;

void loop() {
  M5.Display.clear();
  M5.Display.setCursor(10, 30);
  M5.Display.println("Grove Power:");
  M5.Power.setExtOutput(power_status);
  M5.Display.setCursor(10, 65);
  M5.Display.printf("%s", power_status ? "ON" : "OFF");
  power_status = !power_status;
  delay(1000);
}
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1198/arduino_nesso_n1_power_example_02.jpg" width="50%" />
