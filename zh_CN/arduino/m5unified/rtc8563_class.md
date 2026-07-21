# M5Unified RTC Class

- [M5Unified RTC Class](#m5unified-rtc-class)
  - [begin](#begin)
  - [getVoltLow](#getvoltlow)
  - [getTime](#gettime)
  - [getDate](#getdate)
  - [getDateTime](#getdatetime)
  - [setTime](#settime)
  - [setDate](#setdate)
  - [setDateTime](#setdatetime)
  - [setAlarmIRQ](#setalarmirq)
  - [setSystemTimeFromRtc](#setsystemtimefromrtc)
  - [getIRQstatus](#getirqstatus)
  - [clearIRQ](#clearirq)
  - [disableIRQ](#disableirq)

## begin

**函数原型:**

```cpp
bool begin(I2C_Class* i2c = nullptr);
```

**功能说明:**

- 初始化 RTC

**传入参数:**

- I2C_Class\* i2c:
  - I2C 总线实例指针

**返回值:**

- bool:
  - true: 初始化成功
  - false: 初始化失败

## getVoltLow

**函数原型:**

```cpp
bool getVoltLow(void);
```

**功能说明:**

- 判断 RTC 掉电检测器指示位状态

**传入参数:**

- null

**返回值:**

- bool:
  - true: 未掉电
  - false: 已掉电

## getTime

**函数原型:**

```cpp
bool getTime(rtc_time_t* time) const;
```

**功能说明:**

- 获取当前时间

**传入参数:**

- rtc_time_t\* time:
  - 接收时间信息结构体的指针

**返回值:**

- bool:
  - true: 读取成功
  - false: 读取失败

**函数原型:**

```cpp
rtc_time_t getTime(void) const
```

**功能说明:**

- 获取当前时间

**传入参数:**

- null

**返回值:**

- rtc_time_t time: 时间信息结构体

```cpp line-num
struct __attribute__((packed)) rtc_time_t
{
  std::int8_t hours;
  std::int8_t minutes;
  std::int8_t seconds;

  rtc_time_t(std::int8_t hours_ = -1, std::int8_t minutes_ = -1, std::int8_t seconds_ = -1)
  : hours   { hours_   }
  , minutes { minutes_ }
  , seconds { seconds_ }
  {}

  rtc_time_t(const tm& t)
  : hours   { (int8_t)t.tm_hour }
  , minutes { (int8_t)t.tm_min  }
  , seconds { (int8_t)t.tm_sec  }
  {}
};
```

## getDate

**函数原型:**

```cpp
bool getDate(rtc_date_t* date) const;
```

**功能说明:**

- 获取当前日期

**传入参数:**

- rtc_date_t\* date:
  - 接收日期信息结构体的指针

**返回值:**

- bool:
  - true: 读取成功
  - false: 读取失败

**函数原型:**

```cpp
rtc_date_t getDate(void) const;
```

**功能说明:**

- 获取当前日期

**传入参数:**

- null

**返回值:**

- rtc_date_t date: 日期信息结构体

```cpp line-num
struct __attribute__((packed)) rtc_date_t
{
  /// year 1900-2099
  std::int16_t year;

  /// month 1-12
  std::int8_t month;

  /// date 1-31
  std::int8_t date;

  /// weekDay 0:sun / 1:mon / 2:tue / 3:wed / 4:thu / 5:fri / 6:sat
  std::int8_t weekDay;

  rtc_date_t(std::int16_t year_ = 2000, std::int8_t month_ = 1, std::int8_t date_ = -1, std::int8_t weekDay_ = -1)
  : year    { year_    }
  , month   { month_   }
  , date    { date_    }
  , weekDay { weekDay_ }
  {}

  rtc_date_t(const tm& t)
  : year    { (int16_t)(t.tm_year + 1900) }
  , month   { (int8_t )(t.tm_mon  + 1   ) }
  , date    { (int8_t ) t.tm_mday         }
  , weekDay { (int8_t ) t.tm_wday         }
  {}
};
```

## getDateTime

**函数原型:**

```cpp
bool getDateTime(rtc_datetime_t* datetime) const;
```

**功能说明:**

- 获取当前时间和日期

**传入参数:**

- rtc_datetime_t\* datetime:
  - 接收时间日期信息结构体的指针

**返回值:**

- bool:
  - true: 读取成功
  - false: 读取失败

**函数原型:**

```cpp line-num
rtc_datetime_t getDateTime(void) const
{
    rtc_datetime_t res;
    getDateTime(&res);
    return res;
}
```

**功能说明:**

- 获取当前时间和日期

**传入参数:**

- null

**返回值:**

- rtc_datetime_t datetime: 时间日期信息结构体

```cpp line-num
struct __attribute__((packed)) rtc_datetime_t
{
  rtc_date_t date;
  rtc_time_t time;
  rtc_datetime_t() = default;
  rtc_datetime_t(const rtc_date_t& d, const rtc_time_t& t) : date { d }, time { t } {};
  rtc_datetime_t(const tm& t) : date { t }, time { t } {}
  tm get_tm(void) const;
  void set_tm(tm& time);
  void set_tm(tm* t) { if (t) set_tm(*t); }
};
```

## setTime

**函数原型:**

```cpp
void setTime(const rtc_time_t &time);
```

**功能说明:**

- 设置 RTC 时间

**传入参数:**

- rtc_time_t\* time:
  - 传入时间信息结构体引用

**返回值:**

- null

**函数原型:**

```cpp
void setTime(const rtc_time_t* const time);
```

**功能说明:**

- 设置 RTC 时间

**传入参数:**

- rtc_time_t\* time:
  - 传入时间信息结构体指针

**返回值:**

- null

## setDate

**函数原型:**

```cpp
void setDate(const rtc_date_t &date);
```

**功能说明:**

- 设置 RTC 日期

**传入参数:**

- rtc_time_t\* time:
  - 传入日期信息结构体引用

**返回值:**

- null

**函数原型:**

```cpp
void setDate(const rtc_date_t* const date);
```

**功能说明:**

- 设置 RTC 日期

**传入参数:**

- rtc_time_t\* time:
  - 传入日期信息结构体指针

**返回值:**

- null

## setDateTime

**函数原型:**

```cpp
void setDateTime(const rtc_datetime_t &datetime);
```

**功能说明:**

- 设置 RTC 时间日期

**传入参数:**

- rtc_time_t\* time:
  - 传入时间日期信息结构体引用

**返回值:**

- null

**函数原型:**

```cpp
void setDateTime(const rtc_datetime_t* const datetime);
```

**功能说明:**

- 设置 RTC 时间日期

**传入参数:**

- rtc_time_t\* time:
  - 传入时间日期信息结构体指针

**返回值:**

- null

**函数原型:**

```cpp
void setDateTime(const tm* const datetime);
```

**功能说明:**

- 使用标准 C/C++ 时间结构体，初始化 RTC 时间日期

**传入参数:**

- rtc_time_t\* time:
  - 传入标准时间结构体指针

**返回值:**

- null

## setAlarmIRQ

\#> 注意事项:|IRQ 实现定时中断信号，定时唤醒等操作时，需在触发信号后需执行 clearIRQ, disableIRQ 对中断标志位进行清除，然后才能再次设置。

**函数原型:**

```cpp
int setAlarmIRQ(int afterSeconds);
```

**功能说明:**

- 设置定时中断信号，基于时间信息

**传入参数:**

- int afterSeconds:the set number of seconds.
  - 1 - 15,300. If 256 or more, 1-minute cycle. (max 255 minute.)

**返回值:**

- int(bool):
  - true: 设置成功
  - false: 设置失败

**函数原型:**

```cpp
int setAlarmIRQ(const rtc_time_t &time);
```

**功能说明:**

- 设置定时中断信号，基于时间信息

**传入参数:**

- const rtc_time_t \&time:
  - 时间信息结构体引用

**返回值:**

- int(bool):
  - true: 设置成功
  - false: 设置失败

**函数原型:**

```cpp
int setAlarmIRQ(const rtc_date_t &date, const rtc_time_t &time);
```

**功能说明:**

- 设置定时中断信号，基于时间，日期信息

**传入参数:**

- const rtc_date_t \&date:
  - 日期信息结构体引用
- const rtc_time_t \&time:
  - 时间信息结构体引用

**返回值:**

- int(bool):
  - true: 设置成功
  - false: 设置失败

## setSystemTimeFromRtc

**函数原型:**

```cpp
void setSystemTimeFromRtc(struct timezone* tz = nullptr);
```

**功能说明:**

- 使用 RTC 时间信息初始化系统时间

**传入参数:**

- struct timezone\* tz:
  - 时区偏移信息

**返回值:**

- null

## getIRQstatus

**函数原型:**

```cpp
bool getIRQstatus(void);
```

**功能说明:**

- 获取定时中断信号状态

**传入参数:**

- null

**返回值:**

- bool:
  - true: 中断信号已产生
  - false: 中断信号未产生

## clearIRQ

**函数原型:**

```cpp
void clearIRQ(void);
```

**功能说明:**

- 清除定时中断信号状态

**传入参数:**

- null

**返回值:**

- null

## disableIRQ

**函数原型:**

```cpp
void disableIRQ(void);
```

**功能说明:**

- 禁用定时器中断

**传入参数:**

- null

**返回值:**

- null
