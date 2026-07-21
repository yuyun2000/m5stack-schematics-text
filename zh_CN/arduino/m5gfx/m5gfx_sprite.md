# 画布管理

- [面板参数](#面板参数)
  - [isEPD](#isepd)
  - [height](#height)
  - [width](#width)
  - [popState](#popstate)
  - [pushState](#pushstate)
  - [setBrightness](#setbrightness)
  - [getBrightness](#getbrightness)
  - [setEpdMode](#setepdmode)
  - [getEpdMode](#getepdmode)
  - [setResolution](#setresolution)
  - [setRotation](#setrotation)
  - [getRotation](#getrotation)
- [颜色](#颜色)
  - [setBaseColor](#setbasecolor)
  - [getBaseColor](#getbasecolor)
  - [setColor](#setcolor)
  - [setRawColor](#setrawcolor)
  - [getRawColor](#getrawcolor)
  - [setColorDepth](#setcolordepth)
  - [getColorDepth](#getcolordepth)
  - [getPalette](#getpalette)
  - [getPaletteCount](#getpalettecount)
- [清屏](#清屏)
  - [clear](#clear)
  - [clearDisplay](#cleardisplay)
  - [fillScreen](#fillscreen)
- [坐标点设置](#坐标点设置)
  - [setCursor](#setcursor)
  - [getCursorX](#getcursorx)
  - [getCursorY](#getcursory)
  - [setPivot](#setpivot)
  - [getPivotX](#getpivotx)
  - [getPivotY](#getpivoty)
- [画布区域选择](#画布区域选择)
  - [setAddrWindow](#setaddrwindow)
  - [setWindow](#setwindow)
  - [setClipRect](#setcliprect)
  - [getClipRect](#getcliprect)
  - [clearClipRect](#clearcliprect)
- [画布滚动](#画布滚动)
  - [scroll](#scroll)
  - [setTextScroll](#settextscroll)
  - [setScrollRect](#setscrollrect)
  - [getScrollRect](#getscrollrect)
  - [clearScrollRect](#clearscrollrect)
- [自定义处理](#自定义处理)
  - [effect](#effect)

## 面板参数

### isEPD

**函数原型：**

```cpp
bool isEPD(void)
```

**功能说明：**

- 检查面板是否为 EPD

**返回值：**

- bool：EPD 状态
  - true：是 EPD
  - false：不是 EPD

### height

**函数原型：**

```cpp
int32_t height(void)
``` 

**功能说明：**

- 获取当前面板高度

**传入参数:**

- null 

**返回值：**

- int32_t：当前面板像素高度

### width

**函数原型：**

```cpp
int32_t width (void)
```

**功能说明：**

- 获取当前面板宽度

**传入参数:**

- null

**返回值：**

- int32_t：当前面板像素宽度

### popState

**函数原型：**

```cpp
void popState(void)
```

**功能说明：**

- 暂时保存显示属性信息，如文本字体、光标位置等，恢复操作通过 [pushState](#pushstate)来完成。

**传入参数:**

- null

**返回值：**

- null

### pushState

**函数原型：**

```cpp
void pushState(void)
```

**功能说明：**

- 恢复先前通过 [popState](#popstate) 暂存的显示属性信息

**传入参数:**

- null

**返回值：**

- null

### setBrightness

**函数原型：**

```cpp
void setBrightness(uint8_t brightness)
```

**功能说明：**

- 设置显示面板的亮度

**传入参数:**

- brightness：指定的亮度值（0-255）

**返回值：**

- null

### getBrightness

**函数原型：**

```cpp
uint8_t getBrightness(void)
``` 

**功能说明：**

- 获取由 [setBrightness](#setbrightness) 设置的亮度

**传入参数:**

- null

**返回值：**

- uint8_t：亮度值

### setEpdMode

**函数原型：**

```cpp
void setEpdMode(epd_mode_t epd_mode)
```

**功能说明：**

- 设置 EPD 模式

**传入参数:**

- epd_mode：指定的 EPD 模式

**返回值：**

- null

### getEpdMode

**函数原型：**

```cpp
epd_mode_t getEpdMode(void)
```

**功能说明：**

- 获取由 [setEpdMode](#setepdmode) 设置的 EPD 模式。(仅限电子纸屏产品)

**传入参数:**

- null

**返回值：**

- epd_mode_t：EPD 模式值 （关于[epd_mode_t](/zh_CN/arduino/m5gfx/m5gfx_appendix#enum-epd_mode_t)）

### setResolution

**函数原型 1：**

```cpp
bool setResolution(uint16_t logical_width = 0, uint16_t logical_height = 0, float refresh_rate = 0.0f, uint16_t output_width = 0, uint16_t output_height = 0, uint_fast8_t scale_w = 0, uint_fast8_t scale_h = 0, uint32_t pixel_clock = 74250000)
```

**函数原型 2：**

```cpp
bool setResolution( const config_resolution_t& cfg_resolution )
```

**功能说明：**

- 设置分辨率，仅适用于 `M5AtomDisplay` 。

**传入参数:**

- logical_width：逻辑宽度
- logical_height：逻辑高度
- refresh_rate：刷新率
- output_width：输出宽度
- output_height：输出高度
- scale_w：缩放因子宽度
- scale_h：缩放因子高度
- pixel_clock：像素时钟频率
- cfg_resolution：分辨率配置结构体

#>说明：|`cfg_resolution` 包含了如上所示的所有参数。

**返回值：**

- bool
  - true：设置分辨率成功
  - false：设置分辨率失败

### setRotation

**函数原型：**

```cpp
void setRotation(uint_fast8_t r)
```

**功能说明：**

- 设置显示旋转角度

**传入参数:**

- r：旋转角度（0-7）

**返回值：**

- null

#>说明：|1.旋转角度是 90° 的倍数。  
2.0 到 3 表示顺时针旋转，4 到 7 表示逆时针旋转（默认值为 1）。  
3.需要在显示之前设置旋转角度。

### getRotation

**函数原型：**

```cpp
uint8_t getRotation(void)
```

**功能说明：**

- 获取由 [setRotation](#setrotation) 设置的旋转值

**传入参数:**

- null

**返回值：** 

- uint8_t：当前旋转值
  - 0：0 度
  - 1：90 度
  - 2：180 度
  - 3：270 度
  - 4：-0 度
  - 5：-90 度
  - 6：-180 度
  - 7：-270 度

## 颜色

### setBaseColor

**函数原型：**

```cpp
void setBaseColor(T c)
```

**功能说明：**

- 设置基色，使用滚动功能时可以指定绘图区域外的颜色。

**传入参数:**

- c：指定的基色

**返回值：**

- null

#>说明：|1.基色通常用于滚动区域外的颜色填充。  
2.基色的值可以是 RGB 或其他颜色格式，具体取决于面板的颜色深度和配置。

### getBaseColor

**函数原型：**

```cpp
uint32_t getBaseColor(void)
```

**功能说明：**

- 获取由 [setBaseColor](#setbasecolor) 设置的基色

**传入参数:**

- null

**返回值：**

- uint32_t：基色值

### setColor

**函数原型 1：**

```cpp
void setColor(uint8_t r, uint8_t g, uint8_t b)
```

**函数原型 2：**

```cpp
void setColor(T color)
```

**功能说明：**

- 设置绘图填充颜色，如[fillCircle](/zh_CN/arduino/m5gfx/m5gfx_graph#fillcircle)等未设置颜色参数时，会采用此函数设置的颜色绘制填充圆形。

**传入参数:**

- r：红色分量（0-255）
- g：绿色分量（0-255）
- b：蓝色分量（0-255）
- color：颜色编码

**返回值：**

- null

### setRawColor

**函数原型：**

```cpp
void setRawColor(uint32_t c)
```

**功能说明：**

- 设置原始颜色值，适用于直接使用 RGB 颜色编码的场景。

**传入参数:**

- c：颜色编码

**返回值：**

- null

### getRawColor

**函数原型：**

```cpp
uint32_t getRawColor(void)
```

**功能说明：** 

- 获取由 [setRawColor](#setrawcolor) 设置的原始颜色值

**传入参数:**

- null

**返回值：** 

- uint32_t：原始颜色值

### setColorDepth

**函数原型 1:**

```cpp
void setColorDepth(uint8_t bpp)
```

**函数原型 2:**

```cpp
void* setColorDepth(color_depth_t depth)
```

**功能说明:**

- 设置颜色深度

**传入参数:**

- bpp: 每个像素的位数
  - 1: 1 位
  - 2: 2 位
  - 4: 4 位
  - 8: 8 位
  - 16: 16 位
  - 24: 24 位
  - 32: 32 位
- depth: 颜色深度 （关于[color_depth_t](/zh_CN/arduino/m5gfx/m5gfx_appendix#颜色深度)）

?>注意事项:| 如果使用调色板或电子纸屏产品，颜色深度最高为 8 位。 

### getColorDepth

**函数原型：**

```cpp
color_depth_t getColorDepth(void)
```

**功能说明：**

- 获取由 [setColorDepth](#setcolordepth) 设置的颜色深度

**传入参数:**

- null

**返回值：**

- color_depth_t：颜色深度值

### getPalette

**函数原型：**

```cpp
RGBColor* getPalette(void)
```

**功能说明：**

- 获取当前调色板信息 

**传入参数:**

- null

**返回值：**

- RGBColor*：指向 bgr888_t 结构体的指针，指向当前调色板中的第一个颜色

### getPaletteCount

**函数原型：**

```cpp
uint32_t getPaletteCount(void)
``` 

**功能说明：**

- 获取调色板颜色数量

**传入参数:**

- null

**返回值：**

- uint32_t：调色板颜色数量

## 清屏

### clear

**函数原型：**

```cpp
void clear(const T &color)
```

**功能说明**

- 清空显示，如果指定了一个颜色，就用该颜色初始化屏幕，效果与 [clearDisplay](#cleardisplay)、  [fillScreen](#fillscreen) 相同。

**传入参数：**

- color：清屏颜色 （关于[颜色编码](/zh_CN/arduino/m5gfx/m5gfx_appendix#颜色编码)）

**返回值:**

- null

### clearDisplay

**函数原型：**

```cpp
void clearDisplay(uint32_t color = 0)
```

**功能说明：**

- 清空显示，如果指定了一个颜色，就用该颜色初始化屏幕，否则使用默认颜色。效果与[fillScreen](#fillscreen) 、 [clear](#clear)相同。

**传入参数:**

- color：清屏颜色 （关于[颜色编码](/zh_CN/arduino/m5gfx/m5gfx_appendix#颜色编码)）

**返回值：**

- null

### fillScreen

**函数原型：**

```cpp
void fillScreen(const T &color)
```

**功能说明：**

- 清空显示，如果指定了一个颜色，就用该颜色初始化屏幕，效果与 [clear](#cleardisplay)、  [clearDisplay](#cleardisplay) 相同。

**传入参数:**

- color：填充颜色

**返回值：**

- null

## 坐标点设置

### setCursor

**函数原型 1：**

```cpp
void setCursor(int16_t x, int16_t y)
```

**函数原型 2：**

```cpp
void setCursor(int16_t x, int16_t y, uint8_t font)
void setCursor( int32_t x, int32_t y, const IFont* font)
```

**功能说明：**

- 设置光标位置

**传入参数:**

- x：光标 x 坐标
- y：光标 y 坐标
- font：文本字体格式

**返回值：**

- null

### getCursorX

**函数原型：**

```cpp
int32_t getCursorX(void)
```

**功能说明：**

- 获取当前光标的 x 坐标位置

**传入参数:**

- null

**返回值：**

- int32_t：当前光标的 x 坐标位置

### getCursorY

**函数原型：**

```cpp
int32_t getCursorY(void)
```

**功能说明：** 

- 获取当前光标的 y 坐标位置

**传入参数:**

- null

**返回值：** 

- int32_t：当前光标的 y 坐标位置

### setPivot

**函数原型：**

```cpp
void setPivot(float x, float y)
```

**功能说明：**

- 设置基准点坐标

**传入参数:**

- x：基准点 x 坐标
- y：基准点 y 坐标

**返回值：**

- null

### getPivotX

**函数原型：**

```cpp
float getPivotX(void)
```

**功能说明：**

- 获取 x 轴的中心点坐标

**传入参数:**

- null 

**返回值：**

- float：x 轴的中心点坐标

### getPivotY

**函数原型：**

```cpp
float getPivotY(void)
```

**功能说明：**

- 获取 y 轴的中心点坐标

**传入参数:**

- null

**返回值：**

- float：y 轴的中心点坐标 

## 画布区域选择

### setAddrWindow

**函数原型：**

```cpp
void setAddrWindow(int32_t x, int32_t y, int32_t w, int32_t h)
```

**功能说明：**

- 指定 [writePixels](/zh_CN/arduino/m5gfx/m5gfx_graph#writepixels) 、[pushPixels](/zh_CN/arduino/m5gfx/m5gfx_graph#pushpixels) 等操作绘制区域的矩形范围

#>注意事项：|与 [setWindow](#setwindow) 功能相同，但参数不同。 setAddrWindow 会检查屏幕外的溢出，而 setWindow 不检查。

**传入参数:**

- x：指定的 x 坐标
- y：指定的 y 坐标
- w：指定的宽度
- h：指定的高度

**返回值：**

- null

### setWindow

#>注意事项：|与 [setAddrWindow](#setaddrwindow) 功能相同，但参数不同。 setAddrWindow 会检查屏幕外的溢出，而 setWindow 不检查。

**函数原型：**

```cpp
void setWindow(uint_fast16_t xs, uint_fast16_t ys, uint_fast16_t xe, uint_fast16_t ye)
```

**功能说明：**

- 指定 [writePixels](/zh_CN/arduino/m5gfx/m5gfx_graph#writepixels) 、[pushPixels](/zh_CN/arduino/m5gfx/m5gfx_graph#pushpixels) 等操作绘制区域的矩形范围

**传入参数:**

- xs：起始点 x 坐标
- ys：起始点 y 坐标
- xe：结束点 x 坐标
- ye：结束点 y 坐标

**返回值：**

- null

### setAddrWindow

**函数原型：**

```cpp
void setAddrWindow(int32_t x, int32_t y, int32_t w, int32_t h)
```

**功能说明：**

- 指定 [writePixels](/zh_CN/arduino/m5gfx/m5gfx_graph#writepixels) 、[pushPixels](/zh_CN/arduino/m5gfx/m5gfx_graph#pushpixels) 等操作绘制区域的矩形范围

#>注意事项：|与 [setWindow](#setwindow) 功能相同，但参数不同。 setAddrWindow 会检查屏幕外的溢出，而 setWindow 不检查。

**传入参数:**

- x：指定的 x 坐标
- y：指定的 y 坐标
- w：指定的宽度
- h：指定的高度

**返回值：**

- null

### setWindow

#>注意事项：|与 [setAddrWindow](#setaddrwindow) 功能相同，但参数不同。 setAddrWindow 会检查屏幕外的溢出，而 setWindow 不检查。

**函数原型：**

```cpp
void setWindow(uint_fast16_t xs, uint_fast16_t ys, uint_fast16_t xe, uint_fast16_t ye)
```

**功能说明：**

- 指定 [writePixels](/zh_CN/arduino/m5gfx/m5gfx_graph#writepixels) 、[pushPixels](/zh_CN/arduino/m5gfx/m5gfx_graph#pushpixels) 等操作绘制区域的矩形范围

**传入参数:**

- xs：起始点 x 坐标
- ys：起始点 y 坐标
- xe：结束点 x 坐标
- ye：结束点 y 坐标

**返回值：**

- null

### setClipRect

**函数原型：**

```cpp
void setClipRect(int32_t x, int32_t y, int32_t w, int32_t h)
```

**功能说明：**

- 指定绘图区域的剪裁矩形

**传入参数:**

- x：指定的 x 坐标
- y：指定的 y 坐标
- w：指定的宽度
- h：指定的高度

**返回值：**

- null

### getClipRect

**函数原型：**

```cpp
void getClipRect(int32_t *x, int32_t *y, int32_t *w, int32_t *h)
```

**功能说明：**

- 获取由 [setClipRect](#setcliprect) 设置的裁剪区域

**传入参数:** 

- x：指向 x 坐标的指针
- y：指向 y 坐标的指针 
- w：指向宽度的指针
- h：指向高度的指针

**返回值：**

- null

### clearClipRect

**函数原型：**

```cpp
void clearClipRect(void)
```

**功能说明：**

- 清除由[setClipRect](#setcliprect)绘制的矩形

**传入参数：**

- null

**返回值：**

- null

## 画布滚动

### scroll

**函数原型：**

```cpp
void scroll(int_fast16_t dx, int_fast16_t dy)
```

**功能说明：**

- 滚动显示的屏幕

**传入参数:**

- dx：X 轴滚动的距离
- dy：Y 轴滚动的距离

**返回值：**

- null

**案例程序：**

```cpp line-num
#include <Arduino.h>
#include <M5GFX.h>

M5GFX display;
uint16_t x;
uint16_t y;
bool flag = false;

void setup()
{
    display.begin();
    display.drawString("        Scrolling...      ", 0, 0, &fonts::lgfxJapanGothic_24);
}

void loop()
{
    if(flag)
    {
        for (int i=-53; i<=53; i+=1) {
            display.scroll(0, -2);
            if(i>=53){ flag = false; }
        }
    }
    else
    {
       for (int i=-53; i<=53; i+=1) {
            display.scroll(0, 2);
            if(i>=53){ flag = true; }
        } 
    }
}
```

### setTextScroll

**函数原型：**

```cpp
void setTextScroll(bool scroll)
```

**功能说明：**

- 设置文本滚动

**传入参数:**

- scroll：文本滚动标志

**返回值：**

- null

### setScrollRect

#>注意事项：| 设置文本滚动范围必须使用 `setTextScroll(true)` 。

**函数原型：**

```cpp
void setScrollRect(int32_t x, int32_t y, int32_t w, int32_t h, const T& color)
```

**功能说明：**

- 设置文本滚动范围

**传入参数:**

- x：滚动范围起点 x 坐标
- y：滚动范围起点 y 坐标
- w：滚轴宽度
- h：滚轴高度
- color：滚轴颜色

**返回值：**

- null

### getScrollRect

**函数原型：**

```cpp
void getScrollRect(int32_t *x, int32_t *y, int32_t *w, int32_t *h)
``` 

**功能说明：**

- 获取由 [setScrollRect](#setscrollrect) 设置的滚动区域

**传入参数:**

- x：指向 x 坐标的指针
- y：指向 y 坐标的指针
- w：指向宽度的指针
- h：指向高度的指针 

**返回值：**

- null

### clearScrollRect

**函数原型：** 

```cpp
void clearScrollRect(void)
```

**功能说明：**

- 清除由[setScrollRect](#setscrollrect)绘制的滚屏矩形

**传入参数:**

- null

**返回值：**

- null

**案例程序 1 :**

```cpp line-num
#include <Arduino.h>
#include <M5GFX.h>

M5GFX display;
uint32_t count = 0;

void setup() {
    display.begin();
    display.setRotation(1);
    if(display.isEPD())
    {
        display.setColorDepth(8);//The ink screen product supports a maximum bit depth of 8 bits.
        display.setEpdMode(epd_fastest);
    }
    else
    {
        display.setColorDepth(16);
    }

    display.fillScreen(TFT_WHITE);
    display.setBaseColor(TFT_WHITE);
    display.setTextFont(&fonts::FreeMonoBoldOblique18pt7b);
    display.setTextColor(TFT_BLACK);
    display.setTextScroll(true);
    display.setScrollRect(0, 0, display.width(), display.height());
}

void loop() {
  display.printf("Scroll: %d\n", count);
  count++;
  delay(500);
}
```

- `通过对比以下两个案例程序最终实现，可以看出使用 Canvas 的优势。`

**案例程序 2 (Display)：**

```cpp line-num
#include <Arduino.h>
#include <M5GFX.h>

M5GFX display;
uint16_t w;
uint16_t h;
static constexpr char text[] = "Hello world ! This is M5Stack scroll test.";
static constexpr size_t textlen = sizeof(text) / sizeof(text[0]);
int textpos = 0;
int scrollstep = 2;

void setup()
{
  display.begin();
  display.setRotation(3);
  display.setBaseColor(TFT_WHITE);
  display.fillScreen(TFT_WHITE);
  display.setFont(&fonts::FreeMonoBoldOblique24pt7b);
  display.setTextColor(TFT_BLACK);
  w = display.width() / 2;
  h = display.height() / 2;
}

void loop()
{
  int32_t cursor_x = display.getCursorX() - scrollstep;
  if (cursor_x <= 0)
  {
    textpos = 0;
    cursor_x = 0;
  }

  display.setCursor(cursor_x, h-24);
  display.scroll(-scrollstep, 0);
  while (textpos < textlen && cursor_x <= display.width())
  {
    display.print(text[textpos++]);
    cursor_x = display.getCursorX();
  }
}
```

**案例程序 3 (Canvas)：**

```cpp line-num
#include <Arduino.h>
#include <M5GFX.h>

M5GFX display;
M5Canvas canvas(&display);
uint16_t w;
uint16_t h;
static constexpr char text[] = "Hello world ! This is M5Stack scroll test.";
static constexpr size_t textlen = sizeof(text) / sizeof(text[0]);
int textpos = 0;
int scrollstep = 2;

void setup()
{
  display.begin();
  display.setRotation(3);
  display.fillScreen(TFT_WHITE);

  canvas.createSprite(display.width() + 64, 108);
  canvas.fillSprite(TFT_WHITE);
  canvas.setBaseColor(TFT_WHITE);
  canvas.setFont(&fonts::FreeMonoBoldOblique24pt7b);
  canvas.setTextColor(TFT_BLACK);
  canvas.setTextSize(1.5);
}

void loop()
{
  int32_t cursor_x = canvas.getCursorX() - scrollstep;
  if (cursor_x <= 0)
  {
    textpos = 0;
    cursor_x = display.width();
  }

  canvas.setCursor(cursor_x, 0);
  canvas.scroll(-scrollstep, 0);
  while (textpos < textlen && cursor_x <= display.width())
  {
    canvas.setColor(TFT_BLACK);
    canvas.print(text[textpos++]);
    cursor_x = canvas.getCursorX();
  }

  int y = (display.height() - canvas.height()) >> 1;
  canvas.pushSprite(&display, 0, y);
}
```

## 自定义处理

### effect

**函数原型：**

```cpp
void effect(int32_t x, int32_t y, int32_t w, int32_t h, TFunc&& effector)
```

**功能说明：**

- 使用自定义的变换函数对指定的矩形范围进行效果处理

**传入参数:**

- x：矩形起点 x 坐标
- y：矩形起点 y 坐标
- w：矩形宽度
- h：矩形高度
- effector：变换函数，用户可自定义

**返回值：**

- null