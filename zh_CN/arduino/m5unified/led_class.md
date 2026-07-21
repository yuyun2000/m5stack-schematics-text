# M5Unified LED Class

- [LED Class](#m5unified-led-class)
  - [setLedInstance](#setledinstance)
  - [getLedInstancePtr](#getledinstanceptr)
  - [begin](#begin)
  - [display](#display)
  - [setAutoDisplay](#setautodisplay)
  - [getCount](#getcount)
  - [getBuffer](#getbuffer)
  - [setBrightness](#setbrightness)
  - [setColor](#setcolor)
  - [setColors](#setcolors)
  - [setAllColor](#setallcolor)
  - [isEnabled](#isenabled)
  - [示例程序](#示例程序)

## setLedInstance

**函数原型:**

```cpp
void setLedInstance(std::shared_ptr<LED_Base> instance);
```

**功能说明:**

- 设置 LED 实例

**传入参数:**

- instance：
  - LED 实例指针

**返回值:**

- null

## getLedInstancePtr

**函数原型:**

```cpp
LED_Base* getLedInstancePtr(void);
```

**功能说明:**

- 获取 LED 实例指针

**传入参数:**

- null

**返回值:**

- LED_Base*:
  - LED 实例指针

## begin

**函数原型:**

```cpp
bool begin(void);
```

**功能说明:**

- 初始化 LED

**传入参数:**

- null

**返回值:**

- bool:
  - true: 初始化成功
  - false: 初始化失败

## display

**函数原型:**

```cpp
void display(void);
```

**功能说明:**

- 更新 LED 状态

**传入参数:**

- null

**返回值:**

- null

## setAutoDisplay

**函数原型:**

```cpp
void setAutoDisplay(bool enable);
```

**功能说明:**

- 设置自动更新 LED 状态（默认自动更新）

**传入参数:**

- enable：
  - true: 启用自动更新
  - false: 禁用自动更新

**返回值:**

- null

## getCount

**函数原型:**

```cpp
size_t getCount(void);
```

**功能说明:**

- 获取 LED 数量

**传入参数:**

- null

**返回值:**

- size_t:
  - LED 数量

## getBuffer

**函数原型:**

```cpp
RGBColor* getBuffer(void);
```

**功能说明:**

- 获取 LED 颜色数值缓冲区

**传入参数:**

- null

**返回值:**

- RGBColor*:
  - LED 颜色数值缓冲区指针

## setBrightness

**函数原型:**

```cpp
void setBrightness(uint8_t brightness);
```

**功能说明:**

- 设置 LED 亮度

**传入参数:**

- brightness：
  - 亮度数值 (0-255)

**返回值:**

- null

## setColor

**函数原型 1:**

```cpp
void setColor(size_t index, const RGBColor& color);
```

**函数原型 2:**

```cpp
void setColor(size_t index, uint8_t red, uint8_t green, uint8_t blue);
```

**函数原型 3:**

```cpp
void setColor(size_t index, T c);
```

**功能说明:**

- 设置指定 LED 颜色

**传入参数:**

- index：
  - LED 索引位置 (从 0 开始)
- color / red, green, blue / c：
  - 颜色数值 / RGB 颜色数值 / 泛型颜色数值

**返回值:**

- null

## setColors

**函数原型:**

```cpp
void setColors(const T* values, size_t index = 0, size_t length = INT32_MAX);
```

**功能说明:**

- 批量设置 LED 颜色

**传入参数:**

- values：
  - 颜色数值数组指针
- index：
  - 起始 LED 索引位置 (从 0 开始)
- length：
  - 颜色数值数组长度

**返回值:**

- null

## setAllColor

**函数原型:**

```cpp
void setAllColor(T c);
```

**功能说明:**

- 设置所有 LED 颜色

**传入参数:**

- c：
  - 颜色数值编码

**返回值:**

- null

## isEnabled

**函数原型:**

```cpp
bool isEnabled(void);
```

**功能说明:**

- 获取 LED 启用状态

**传入参数:**

- null

**返回值:**

- bool:
  - true: 已启用
  - false: 未启用

## 示例程序

```cpp line-num
#include "M5Unified.h"
#include "utility/led/LED_Strip_Class.hpp"
#include "utility/led/LED_Base.hpp"

RGBColor colors[10] = {
  { 255, 0, 0 },      // Red 
  { 0, 255, 0 },      // Green
  { 0, 0, 255 },      // Blue 
  { 255, 255, 0 },    // Yellow 
  { 0, 255, 255 },    // Cyan
  { 255, 0, 255 },    // Magenta
  { 128, 128, 128 },  // Gray
  { 255, 128, 0 },    // Orange
  { 0, 128, 255 },    // Sky Blue
  { 128, 0, 255 }     // Purple-Blue
};

void setup() {
  M5.begin();

  // Configure RMT bus for LED strip (data pin: GPIO26)
  auto busled = std::make_shared<m5::LedBus_RMT>();
  auto buscfg = busled->getConfig();
  buscfg.pin_data = 26;
  busled->setConfig(buscfg);

  // Configure LED strip (30 LEDs, 3 bytes/LED, GRB order)
  auto led_strip = std::make_shared<m5::LED_Strip_Class>();
  auto ledcfg = led_strip->getConfig();
  ledcfg.led_count = 30;
  ledcfg.byte_per_led = 3;
  ledcfg.color_order = m5::LED_Strip_Class::config_t::color_order_grb;
  led_strip->setConfig(ledcfg);

  led_strip->setBus(busled);  // Link bus to LED strip
  M5.Led.setLedInstance(led_strip);  // Register to M5 system
  M5.Led.begin();  // Initialize LED strip

  M5.Display.clear();
  M5.Display.setFont(&fonts::FreeMonoBoldOblique12pt7b);
  M5.Display.setCursor(20, 50);
  M5.Display.printf("LED Cnt: %d", M5.Led.getCount());
  M5.Display.setCursor(20, 70);
  M5.Display.printf("LED Status: %s", M5.Led.isEnabled() ? "Enabled" : "Disabled");
  M5.Led.setBrightness(100);
}

void loop() {
  static int offset = 0;  // Scrolling offset (persists between loops)
  RGBColor* buf = M5.Led.getBuffer();  // Get LED color buffer

  // Assign colors to each LED with offset (cyclic scrolling)
  for (int i = 0; i < 30; ++i) {
    buf[i] = colors[(i + offset) % 10];
  }

  M5.Led.setColors(buf, 0, 30);  // Update LED strip with buffer data
  offset = (offset + 1) % 10;    // Increment offset (cycle 0-9)
}
```

使用 M5GO 运行上述代码，在 PORT.B 接入 30 颗 RGB 灯珠灯带，效果如下所示：

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/661/m5go_Arduino_led_strip.mp4" type="video/mp4"></video>
