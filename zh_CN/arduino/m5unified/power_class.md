# M5Unified Power Class

- [Power Class](#m5unified-power-class)
  - [begin](#begin)
  - [setExtOutput](#setextoutput)
  - [getExtOutput](#getextoutput)
  - [setUsbOutput](#setusboutput)
  - [getUsbOutput](#getusboutput)
  - [setLed](#setled)
  - [powerOff](#poweroff)
  - [timerSleep](#timersleep)
  - [timerSleep](#timersleep-1)
  - [timerSleep](#timersleep-2)
  - [deepSleep](#deepsleep)
  - [lightSleep](#lightsleep)
  - [getBatteryLevel](#getbatterylevel)
  - [setBatteryCharge](#setbatterycharge)
  - [setChargeCurrent](#setchargecurrent)
  - [setChargeVoltage](#setchargevoltage)
  - [isCharging](#ischarging)
  - [getBatteryVoltage](#getbatteryvoltage)
  - [getBatteryCurrent](#getbatterycurrent)
  - [getKeyState](#getkeystate)
  - [setVibration](#setvibration)
  - [getType](#gettype)

## begin

**函数原型:**

```cpp
bool begin(void);
```

**功能说明:**

- 初始化 PMIC

**传入参数:**

- null

**返回值:**

- bool:
  - true: 初始化成功
  - false: 初始化失败

## setExtOutput

**函数原型:**

```cpp
void setExtOutput(bool enable, ext_port_mask_t port_mask = (ext_port_mask_t)0xFF);
```

**功能说明:**

- 设置外部端口的电源输出

**传入参数:**

- bool enable：
  - 电源输出使能状态:
    - true:输出使能
    - false:输出禁用
- ext_port_mask_t port_mask:
  - 操作的输出端口 mask：
    - 对支持多个输出端口独立开关电源的设备有效(如:M5Station)

**返回值:**

- null

## getExtOutput

**函数原型:**

```cpp
bool getExtOutput(void);
```

**功能说明:**

- 读取外部端口的电源输出状态

**传入参数:**

- null

**返回值:**

- bool:
  - true: 输出使能
  - false: 输出禁用

## setUsbOutput

**函数原型:**

```cpp
void setUsbOutput(bool enable);
```

**功能说明:**

- 设置 USB 电源输出状态(for M5Stack CoreS3 main USB port. Not for M5Station external USB.)

**传入参数:**

- bool enable：
  - USB 电源输出使能状态:
    - true:输出使能
    - false:输出禁用

**返回值:**

- null

## getUsbOutput

**函数原型:**

```cpp
bool getUsbOutput(void);
```

**功能说明:**

- 读取 USB 电源输出状态(for M5Stack CoreS3 main USB port. Not for M5Station external USB.)

**传入参数:**

- bool enable：
  - USB 电源输出使能状态:

**返回值:**

- bool:
  - true:输出使能
  - false:输出禁用

## setLed

**函数原型:**

```cpp
void setLed(uint8_t brightness = 255);
```

**功能说明:**

- 设置电源 LED 灯状态

**传入参数:**

- uint8_t brightness：
  - 0=OFF
  - 1-255=ON

**返回值:**

- null

## powerOff

**函数原型:**

```cpp
void powerOff(void);
```

**功能说明:**

- 关闭所有电源

**传入参数:**

- null

**返回值:**

- null

## timerSleep

#>timerSleep 注意事项|一些没有集成 PMIC 的设备如 M5Paper, 在 USB 供电状态下, 无法关闭电源。需在电池供电条件下该功能才生效。

**函数原型:**

```cpp
void timerSleep(int seconds);
```

**功能说明:**

- 设备休眠, 经过指定时间后定时唤醒。

**传入参数:**

- int seconds:
  - 休眠时长 s

**返回值:**

- null

## timerSleep

**函数原型:**

```cpp
void timerSleep(const rtc_time_t& time);
```

**功能说明:**

- 设备休眠, 经过指定时间后定时唤醒。

**传入参数:**

- const rtc_time_t& time:
  - 唤醒时间(只能指定分钟和小时。忽略秒)

**返回值:**

- null

## timerSleep

**函数原型:**

```cpp
void timerSleep(const rtc_date_t& date, const rtc_time_t& time);
```

**功能说明:**

- 设备休眠, 经过指定时间后定时唤醒。

**传入参数:**

- int const rtc_date_t& date:
  - 唤醒日期(只能指定日期和星期。忽略年份和月份)
- const rtc_time_t& time:
  - 唤醒时间(只能指定分钟和小时。忽略秒)

**返回值:**

- null

## deepSleep

**函数原型:**

```cpp
void deepSleep(std::uint64_t micro_seconds = 0, bool touch_wakeup = true);
```

**功能说明:**

- 芯片进入深度休眠一段时间后唤醒

**传入参数:**

- uint64_t micro_seconds:
  - 休眠时长
- bool touch_wakeup:
  - 是否开启触屏唤醒

**返回值:**

- null

## lightSleep

**函数原型:**

```cpp
void lightSleep(std::uint64_t micro_seconds = 0, bool touch_wakeup = true);
```

**功能说明:**

- 芯片进入浅度休眠一段时间后唤醒

**传入参数:**

- uint64_t micro_seconds:
  - 休眠时长
- bool touch_wakeup:
  - 是否开启触屏唤醒

**返回值:**

- null

## getBatteryLevel

**函数原型:**

```cpp line-num
/// Get the remaining battery power.
/// @return 0-100 level
std::int32_t getBatteryLevel(void);
```

**功能说明:**

- 获取剩余电量参考值

**传入参数:**

- null

**返回值:**

- int32_t level:
  - 0-100

## setBatteryCharge

**函数原型:**

```cpp
void setBatteryCharge(bool enable);
```

**功能说明:**

- 设置电池充电使能

**传入参数:**

- bool enable:

**返回值:**

- bool:
  - true: 使能电池充电
  - false: 禁用电池充电

## setChargeCurrent

#>setCharge 注意事项|设置充电电压, 电流相关 API 仅一些集成了 PMIC 的设备上支持。

**函数原型:**

```cpp
void setChargeCurrent(std::uint16_t max_mA);
```

**功能说明:**

- 设置电池充电电流

**传入参数:**

- uint16_t max_mA:
  - 最大充电电流 mA

**返回值:**

- null

## setChargeVoltage

**函数原型:**

```cpp
void setChargeVoltage(std::uint16_t max_mV);
```

**功能说明:**

- 设置电池充电电压

**传入参数:**

- uint16_t max_mV:
  - 最大充电电压 mV

**返回值:**

- null

## isCharging

**函数原型:**

```cpp
is_charging_t isCharging(void);
```

**功能说明:**

- 判断当前是否处于充电状态

**传入参数:**

- null

**返回值:**

- bool:
  - true: 充电中
  - false: 未充电

## getBatteryVoltage

**函数原型:**

```cpp
int16_t getBatteryVoltage(void);
```

**功能说明:**

- 获取电池电压

**传入参数:**

- null

**返回值:**

- int16_t voltage:
  - 电池电压 mV

## getBatteryCurrent

**函数原型:**

```cpp
int32_t getBatteryCurrent(void);
```

**功能说明:**

- 获取电池电流

**传入参数:**

- null

**返回值:**

- int32_t current:
  - 电池电流 mA ( +=charge / -=discharge )

## getKeyState

**函数原型:**

```cpp line-num
/// Get Power Key Press condition.
/// @return 0=none / 1=long pressed / 2=short clicked / 3=both
/// @attention Only for models with AXP192 or AXP2101
/// @attention Once this function is called, the value is reset to 0, and the next time it is pressed on, the value changes.
uint8_t getKeyState(void);
```

**功能说明:**

- 获取 PMIC 按键输入信号状态(Only for models with AXP192 or AXP2101), 调用后状态将重置。

**传入参数:**

- null

**返回值:**

- uint8_t key:
  - none:0
  - long pressed:1
  - short clicked:2
  - both:3

## setVibration

**函数原型:**

```cpp
void setVibration(uint8_t level);
```

**功能说明:**

- 控制振动电机振动

**传入参数:**

- uint8_t level:
  - 振动级别: 0-255, 0=stop

**返回值:**

- null

## getType

**函数原型:**

```cpp
pmic_t getType(void) const { return _pmic; }
```

**功能说明:**

- 获取 PMIC 类型

**传入参数:**

- null

**返回值:**

- pmic_t:
  - PMIC 芯片类型

```cpp line-num
enum pmic_t
{ pmic_unknown
, pmic_adc
, pmic_axp192
, pmic_ip5306
, pmic_axp2101
};
```
