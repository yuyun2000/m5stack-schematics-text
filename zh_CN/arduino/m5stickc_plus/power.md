# StickC-Plus Power 电源管理 - AXP192

#>M5StickC Plus使用AXP192电源管理方案, 参考以下API与案例程序能够实现基本的电源输入输出相关数据读取。


## 案例程序

```cpp line-num
#include <M5StickCPlus.h>

void setup() {
    M5.begin();
    M5.Lcd.begin();
    M5.Lcd.setRotation(3);
}

void loop() {
    M5.Lcd.fillScreen(BLACK);
    M5.Lcd.setCursor(0, 0, 1);
    M5.Lcd.printf("AXP Temp: %.1fC \r\n", M5.Axp.GetTempInAXP192());
    M5.Lcd.printf("Bat:\r\n  V: %.3fv  I: %.3fma\r\n", M5.Axp.GetBatVoltage(), M5.Axp.GetBatCurrent());
    M5.Lcd.printf("USB:\r\n  V: %.3fv  I: %.3fma\r\n", M5.Axp.GetVBusVoltage(), M5.Axp.GetVBusCurrent());
    M5.Lcd.printf("5V-In:\r\n  V: %.3fv  I: %.3fma\r\n", M5.Axp.GetVinVoltage(), M5.Axp.GetVinCurrent());
    M5.Lcd.printf("Bat power %.3fmw", M5.Axp.GetBatPower());
    M5.update();
    delay(100);
}
```

## begin

**函数原型:**

```cpp
void begin(void);
```

**功能说明:**

- 初始化AXP192芯片, 使用M5.begin()将在内部自动调用Axp.begin()进行初始化。

**传入参数:**

- null

**返回值:**

- null

**案例程序:**

```cpp line-num
#include <M5StickCPlus.h>

void setup() {
  M5.begin();
}
void loop() {}
```


## PowerOff

**函数原型:**

```cpp
void PowerOff();
```

**功能说明:**

- 关闭电源

**传入参数:**

- null

**返回值:**

- null


**案例程序:**

```cpp line-num
#include <M5StickCPlus.h>

void setup() {
    M5.begin();
    M5.lcd.fillScreen(GREEN);
    delay(3000);
    M5.Axp.PowerOff();
}

void loop() {
}
```

## ScreenBreath

**函数原型:**

```cpp
void ScreenBreath(uint8_t brightness);
```

**功能说明:**

- 改变 AXP192 芯片的LDO3输出电压, 进而调整屏幕背光亮度。

**传入参数:**

- uint8_t brightness:
  - 输入范围0-100

**返回值:**

- null


**案例程序:**

```cpp line-num
#include <M5StickCPlus.h>

uint8_t i = 0;

void setup() {
    M5.begin();  // By default, "M5.begin()" will initialize AXP192 chip
    M5.Lcd.printf("Hello, M5Stack!!");
}
void loop() {
    M5.Axp.ScreenBreath(i++);
    if (i > 100) i = 0;
    delay(10);
}
```


## ScreenSwitch

**函数原型:**

```cpp
void ScreenSwitch(bool state);
```

**功能说明:**

- 屏幕背光开关

**传入参数:**

- bool state:
  - true:开启屏幕背光
  - false:关闭屏幕背光

**返回值:**

- null

**案例程序:**

```cpp line-num
#include <M5StickCPlus.h>

uint8_t i = 0;

void setup() {
    M5.begin();
    M5.Lcd.fillScreen(BLUE);
}
void loop() {
    M5.Axp.ScreenSwitch(true);
    delay(1000);
    M5.Axp.ScreenSwitch(false);
    delay(1000);
}
```


## GetBatState

**函数原型:**

```cpp
bool GetBatState();
```

**功能说明:**

- 读取电池连接状态

**传入参数:**

- null

**返回值:**

- bool:
  - true:电池已连接
  - false:电池未连接


## GetBatVoltage

**函数原型:**

```cpp
float GetBatVoltage();
```

**功能说明:**

- 读取电池电压

**传入参数:**

- null

**返回值:**

- float:
  - 电池电压(V)


## GetBatCurrent

**函数原型:**

```cpp
float GetBatCurrent();
```

**功能说明:**

- 读取电池电流

**传入参数:**

- null

**返回值:**

- float:
  - 电池电流(mA)


## GetVinVoltage

**函数原型:**

```cpp
float GetVinVoltage();
```

**功能说明:**

- 读取VIN输入电压

**传入参数:**

- null

**返回值:**

- float:
  - VIN输入电压(V)


## GetVinCurrent

**函数原型:**

```cpp
float GetVinCurrent();
```

**功能说明:**

- 读取VIN输入电流

**传入参数:**

- null

**返回值:**

- float:
  - VIN输入电流(mA)


## GetVBusVoltage

**函数原型:**

```cpp
float GetVBusVoltage();
```

**功能说明:**

- 读取USB输入电压


**传入参数:**

- null

**返回值:**

- float:
  - USB输入电压(V)

## GetVBusCurrent

**函数原型:**

```cpp
float GetVBusCurrent();
```

**功能说明:**

- 读取USB输入电流


**传入参数:**

- null

**返回值:**

- float:
  - USB输入电流(mA)

## GetTempInAXP192

**函数原型:**

```cpp
float GetTempInAXP192();
```

**功能说明:**

- 读取AXP192内部温度传感器数值

**传入参数:**

- null

**返回值:**

- float:
  - 温度值(deg C)


## GetBatPower

**函数原型:**

```cpp
float GetBatPower();
```

**功能说明:**

- 读取电池当前功率mW

**传入参数:**

- null

**返回值:**

- float:
  - 电池功率(mW)


