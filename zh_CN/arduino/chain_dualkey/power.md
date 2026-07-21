# Chain DualKey Power 电源管理

Chain DualKey Power 电源管理相关 API 与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.4
- 开发板选项 = M5ChainDualKey

```cpp line-num
#define PIN_ADC_CHRG 9
#define PIN_ADC_BATT 10
#define PIN_ADC_VBUS 2

float chgVoltage;
float batVoltage;
float usbVoltage;

void setup() {
  pinMode(PIN_ADC_CHRG, INPUT);
  pinMode(PIN_ADC_BATT, INPUT);
  pinMode(PIN_ADC_VBUS, INPUT);

  Serial.begin(115200);
}

void loop() {
  chgVoltage = analogRead(PIN_ADC_CHRG) / 4095.0 * 3.3;
  batVoltage = analogRead(PIN_ADC_BATT) / 4095.0 * 3.3 * 1.51;
  usbVoltage = analogRead(PIN_ADC_VBUS) / 4095.0 * 3.3 * 1.51;

  if (chgVoltage >= 1.4 && chgVoltage <= 1.8) {
    Serial.println("Battery is charging");
  } else if (chgVoltage > 1.8 && chgVoltage <= 2.4) {
    Serial.println("Battery is full");
  } else if (chgVoltage > 3.0) {
    Serial.println("Battery is not charging");
  } else {
    Serial.println("Battery charging status is unknown");
  }

  Serial.printf("Battery voltage: %.4f V\n", batVoltage);  // Unit: V
  Serial.printf("    USB voltage: %.4f V\n", usbVoltage);  // Unit: V

  Serial.println();
  delay(1000);
}
```

该程序将检测电池充电状态、电池电压、USB 输入电压，每秒向串口输出一次：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/Arduino_power.png" width="90%">

#> 关于电池充电 | 只要连接外部电源，无论开关拨到什么位置，都会给电池充电。