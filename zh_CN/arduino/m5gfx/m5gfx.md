# M5GFX Setup

M5GFX 是一个为 M5Stack 产品操作显示设备的库，用户可以调用该库中的 API 实现不同的显示效果及触摸效果等。

- [包括头文件和显示定义](#包括头文件和显示定义)
- [M5GFX.h](#m5gfxh)
  - [构造函数](#构造函数)
- [M5UnitLCD.h](#m5unitlcdh)
  - [构造函数](#Con-1)
  - [函数](#函数)
    - [init](#init)
    - [setup](#setup)
- [M5UnitOLED.h](#m5unitoledh)
  - [构造函数](#Con-2)
  - [函数](#Fun-1)
    - [init](#init-1)
    - [setup](#setup-1)
- [M5AtomDisplay.h](#m5atomdisplayh)
  - [构造函数](#Con-3)
  - [函数](#Fun-2)
    - [setResolution](#setresolution)
- [依赖额外头文件的 API 列表](#依赖额外头文件的-api-列表)

## 包括头文件和显示定义

每个设备的包含文件都不同，M5Stack 设备主要使用的头文件是 `M5GFX.h`；其他设备如 Unit LCD 需要使用的头文件为 `M5UnitLCD.h`，Unit OLED、Atom Display 同理。

## M5GFX.h

**支持的设备：**

M5Stack [核心控制器](/zh_CN/products?id=核心控制器-core)，如 M5Fire、M5Core2、M5Tough、M5StickC、M5Paper、M5Tab 等。

### 构造函数

**构造函数原型：**

```cpp
M5GFX(void)
```

**功能说明：**

- 创建 M5GFX 对象，默认指向当前设备

**案例程序：**

```cpp line-num
#include <M5GFX.h>

M5GFX display;

void setup() {
    display.begin();
    uint16_t x = display.width() / 2;
    uint16_t y = display.height() / 2;

    display.drawCenterString("M5Stack", x, y);
}

void loop() {
}
```

## M5UnitLCD.h

**支持的设备：**

M5Stack [Unit LCD](/zh_CN/unit/lcd)

<h3 id="Con-1">构造函数</h3>

**构造函数原型：**

```cpp
M5UnitLCD( uint8_t pin_sda = M5UNITLCD_SDA, uint8_t pin_scl = M5UNITLCD_SCL, uint32_t i2c_freq = M5UNITLCD_FREQ, 
           int8_t i2c_port = -1, uint8_t i2c_addr = 0x3E )
```

**功能说明：**

- 创建 M5UnitLCD 对象并设置 I2C 参数

**传入参数：**

- pin_sda：设备 LCD 的 SDA 引脚号
- pin_scl：设备 LCD 的 SCL 引脚号
- i2c_freq：I2C 通信频率
- i2c_port：I2C 端口（通常不使用）
- i2c_addr：I2C 地址（通常不使用）

#> 说明 | 对于 M5StickC/Plus/Atom 主控设备，`i2c_port` 和 `i2c_addr` 即使不传入参数，也会自动配置为 PORT.A 和 0x3E。

### 函数

#### init

**函数原型：**

```cpp
void init( uint8_t pin_sda, uint8_t pin_scl, uint32_t i2c_freq = M5UNITLCD_FREQ, int8_t i2c_port = -1, uint8_t i2c_addr = 0x3E )
```

**功能说明：**

- 初始化设置

**传入参数：**

- pin_sda：设备 LCD 的 SDA 引脚号
- pin_scl：设备 LCD 的 SCL 引脚号
- i2c_freq：I2C 通信频率
- i2c_port：I2C 端口（通常不使用）
- i2c_addr：I2C 地址（通常不使用）

#### setup

**函数原型：**

```cpp
setup(uint8_t pin_sda = M5UNITLCD_SDA, uint8_t pin_scl = M5UNITLCD_SCL, uint32_t i2c_freq = M5UNITLCD_FREQ, 
      int8_t i2c_port = -1, uint8_t i2c_addr = 0x3E)
``` 

**功能说明：**

- 改变初始设置

**传入参数：**

- pin_sda：设备 LCD 的 SDA 引脚号
- pin_scl：设备 LCD 的 SCL 引脚号
- i2c_freq：I2C 通信频率
- i2c_port：I2C 端口（通常不使用）
- i2c_addr：I2C 地址（通常不使用）

**案例程序：**

```cpp line-num
#include <M5UnitLCD.h>
M5UnitLCD display;

void setup() {
    display.init( 21, 22, 400000 );
    display.setup( 21, 22, 400000 );
    uint16_t x = display.width() / 2;
    uint16_t y = display.height() / 2;

    display.drawCenterString("M5Stack", x, y);
}

void loop() {
}
```

## M5UnitOLED.h

**支持的设备：**

M5Stack [Unit OLED](/zh_CN/unit/oled)

<h3 id="Con-2">构造函数</h3>

**构造函数原型：**

```cpp
M5UnitOLED( uint8_t pin_sda = M5UNITOLED_SDA, uint8_t pin_scl = M5UNITOLED_SCL, uint32_t i2c_freq = M5UNITOLED_FREQ, 
            int8_t i2c_port = -1, uint8_t i2c_addr = 0x3C)
```

**功能说明：**

- 创建 M5UnitOLED 对象并设置 I2C 参数

**传入参数：**

- pin_sda：设备 LCD 的 SDA 引脚号
- pin_scl：设备 LCD 的 SCL 引脚号
- i2c_freq：I2C 通信频率
- i2c_port：I2C 端口（通常不使用）
- i2c_addr：I2C 地址（通常不使用）

#> 说明 | 对于 M5StickC/Plus/Atom 主控设备，`i2c_port` 和 `i2c_addr` 即使不传入参数，也会自动配置为 PORT.A 和 0x3C。

<h3 id="Fun-1">函数</h3>

<h4 id="init-1">init</h4>

**函数原型：**

```cpp
void init( uint8_t pin_sda, uint8_t pin_scl, uint32_t i2c_freq = M5UNITOLED_FREQ, int8_t i2c_port = -1, uint8_t i2c_addr = 0x3C )
```

**功能说明：**

- 初始化设置

**传入参数：**

- pin_sda：设备 LCD 的 SDA 引脚号
- pin_scl：设备 LCD 的 SCL 引脚号
- i2c_freq：I2C 通信频率
- i2c_port：I2C 端口（通常不使用）
- i2c_addr：I2C 地址（通常不使用）

<h4 id="setup-1">setup</h4>

**函数原型：**

```cpp
setup(uint8_t pin_sda = M5UNITLCD_SDA, uint8_t pin_scl = M5UNITLCD_SCL, uint32_t i2c_freq = M5UNITLCD_FREQ, 
      int8_t i2c_port = -1, uint8_t i2c_addr = 0x3C)
``` 

**功能说明：**

- 改变初始设置

**传入参数：**

- pin_sda：设备 LCD 的 SDA 引脚号
- pin_scl：设备 LCD 的 SCL 引脚号
- i2c_freq：I2C 通信频率
- i2c_port：I2C 端口（通常不使用）
- i2c_addr：I2C 地址（通常不使用）

**案例程序：**

```cpp line-num
#include <M5UnitOLED.h>
M5UnitOLED display;

void setup() {
    display.init( 21, 22, 400000 );
    display.setup( 21, 22, 400000 );
    uint16_t x = display.width() / 2;
    uint16_t y = display.height() / 2;

    display.drawCenterString("M5Stack", x, y);
}

void loop() {
}
```

## M5AtomDisplay.h

**支持的设备：**

M5Stack [Atom Display](/zh_CN/atom/atom_display)、[AtomDisplayLite](/zh_CN/atom/atom_display_lite)

<h3 id="Con-3">构造函数</h3>

**构造函数原型：**

```cpp
M5AtomDisplay( unit16_t logical_width = 1280, uint16_t logical_height = 720, float refresh_rate = 0.0f, uint16_t output_width = 0, uint16_t output_height = 0, 
               uint_fast8_t scale_w = 0, uint_fast8_t scale_h = 0, uint32_t pixel_clock = 74250000)
```

**功能说明：**

- 创建 M5AtomDisplay 对象并设置 I2C 参数

**传入参数：**

- logical_width：程序处理的逻辑屏幕宽度
- logical_height：程序处理的逻辑屏幕高度
- refresh_rate：屏幕刷新速率
- output_width：实际输出屏幕宽度
- output_height：实际输出屏幕高度
- scale_w：逻辑宽度的放大率
- scale_h：逻辑高度的放大率

#> 说明 | 1. 最大分辨率取决于可用的内存  
2.可指定的刷新率取决于所使用的显示器  
  **分辨率使用示例：**  
  1280 x 720  x 60Hz  
  1920 x 1080 x 24Hz  
  320 x 240 x 240Hz

<h3 id="Fun-2">函数</h3>

#### setResolution

**函数原型：**

```cpp
bool setResolution(uint16_t logical_width = 0, uint16_t logical_height = 0, float refresh_rate = 0.0f, uint16_t output_width = 0, uint16_t output_height = 0, 
                   uint_fast8_t scale_w = 0, uint_fast8_t scale_h = 0, uint32_t pixel_clock = 74250000)
```

**功能说明：**

- 改变初始分辨率设置

**传入参数：**

- logical_width：程序处理的逻辑屏幕宽度
- logical_height：程序处理的逻辑屏幕高度
- refresh_rate：屏幕刷新速率
- output_width：实际输出屏幕宽度
- output_height：实际输出屏幕高度
- scale_w：逻辑宽度的放大率
- scale_h：逻辑高度的放大率
- pixel_clock：像素时钟频率

**案例程序：**

```cpp line-num
#include <M5AtomDisplay.h>
M5AtomDisplay display( 640, 480, 60 );

void setup() {
    display.setResolution( 320, 240, 60 );
    uint16_t x = display.width() / 2;
    uint16_t y = display.height() / 2;

    display.drawCenterString("M5Stack", x, y);
}

void loop() {
}
```

## 依赖额外头文件的 API 列表

M5GFX 一些 API 的使用除 M5GFX.h（或 M5UnitLCD.h，M5UnitOLED.h，M5AtomDisplay.h）外还`必须`包含其他对应的头文件，否则无法成功被调用。  
相关 API 及头文件如下表：

| API                                                         | 必需的头文件         |
| ----------------------------------------------------------- | -------------------- |
| [drawBmpFile](/zh_CN/arduino/m5gfx/m5gfx_image#drawbmpfile) | SD.h  or  SPIFFS.h   |
| [drawJpgFile](/zh_CN/arduino/m5gfx/m5gfx_image#drawjpgfile) | SD.h  or  SPIFFS.h   |
| [drawPngFile](/zh_CN/arduino/m5gfx/m5gfx_image#drawpngfile) | SD.h  or  SPIFFS.h   |
| [drawQoiFile](/zh_CN/arduino/m5gfx/m5gfx_image#drawqoifile) | SD.h  or  SPIFFS.h   |
| [drawBmpUrl](/zh_CN/arduino/m5gfx/m5gfx_image#drawbmpurl)   | HTTPClient.h         |
| [drawJpgUrl](/zh_CN/arduino/m5gfx/m5gfx_image#drawjpgurl)   | HTTPClient.h         |
| [drawPngUrl](/zh_CN/arduino/m5gfx/m5gfx_image#drawpngurl)   | HTTPClient.h         |
| [drawQoiUrl](/zh_CN/arduino/m5gfx/m5gfx_image#drawqoiurl)   | HTTPClient.h         |

#> 说明 | 1.请在 M5GFX.h（或 M5UnitLCD.h，M5UnitOLED.h，M5AtomDisplay.h）之前包含对应头文件。  
2.使用头文件 `SD.h` 还是 `SPIFFS.h` 需根据图像数据所在位置为外部存储卡还是主控内存选用。
