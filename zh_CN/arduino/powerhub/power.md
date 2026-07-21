# PowerHub Power 电源管理

PowerHub Power 电源管理相关 API 与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.3
- 开发板选项 = M5PowerHub
- M5Unified 库版本 >= 0.2.11

```cpp line-num
#include <M5Unified.h>

void setup() {
  M5.begin();
  Serial.begin(115200);

  M5.Power.setBatteryCharge(true);  // battery charge

  M5.Power.setExtOutput(1, m5::ext_USB);  // USB-A + USB-C together
  M5.Power.setExtOutput(0, m5::ext_PA);   // PORT.I2C  red
  M5.Power.setExtOutput(0, m5::ext_PC1);  // PORT.UART blue

  // CAN + RS485 together
  m5::ext_port_bus_t port_cfg;
  port_cfg.enable = 1;          // 0 = disable, 1 = enable
  port_cfg.direction = 1;       // 0 = input,   1 = output
  port_cfg.voltage = 12000;     // mV
  port_cfg.currentLimit = 300;  // mA
  M5.Power.setExtPortBusConfig(port_cfg);

  // 5V OUT in the backside 2*8 pin
  pinMode(14, OUTPUT);
  digitalWrite(14, LOW);  // LOW = disable, HIGH = enable
}

void loop() {
  M5.update();

  Serial.printf("ExtOutput: %s", M5.Power.getExtOutput() ? "ON\n" : "OFF\n");  // 0 = all OFF, 1 = some or all ON

  Serial.printf("Battery: %s charging", M5.Power.isCharging() ? "IS" : "NOT");
  Serial.printf(", %d %%", M5.Power.getBatteryLevel());      // 0 ~ 100 %
  Serial.printf(", %d mV", M5.Power.getBatteryVoltage());    // mV
  Serial.printf(", %d mA\n", M5.Power.getBatteryCurrent());  // mA, >0 = charge, <0 = discharge

  Serial.printf("  USB A+C: %d mV", M5.Power.getExtVoltage(m5::ext_USB));     // mV
  Serial.printf(", %d mA\n", M5.Power.getExtCurrent(m5::ext_USB));            // mA
  Serial.printf(" PORT.I2C: %d mV", M5.Power.getExtVoltage(m5::ext_PA));      // mV
  Serial.printf(", %d mA\n", M5.Power.getExtCurrent(m5::ext_PA));             // mA
  Serial.printf("PORT.UART: %d mV", M5.Power.getExtVoltage(m5::ext_PC1));     // mV
  Serial.printf(", %d mA\n", M5.Power.getExtCurrent(m5::ext_PC1));            // mA
  Serial.printf("      CAN: %d mV", M5.Power.getExtVoltage(m5::ext_PWRCAN));  // mV
  Serial.printf(", %d mA\n", M5.Power.getExtCurrent(m5::ext_PWRCAN));         // mA
  Serial.printf("    RS485: %d mV", M5.Power.getExtVoltage(m5::ext_PWR485));  // mV
  Serial.printf(", %d mA\n", M5.Power.getExtCurrent(m5::ext_PWR485));         // mA

  Serial.println();
  delay(2000);

  // M5.Power.powerOff();
}
```

该程序将设置各电源接口的通断，并检测电池充电状态、电量百分比、电压、电流，以及各电源接口的电压、电流。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1183/Arduino_power.png" width="90%">

## API

PowerHub Power 电源管理部分驱动使用了`M5Unified`库中的`Power_Class`，更多相关的 API 可以参考下方文档：

- [M5Unified - Power Class](/zh_CN/arduino/m5unified/power_class)