# 文本绘制

- [文本显示](#文本显示)
  - [drawCenterString](#drawcenterstring)
  - [drawChar](#drawchar)
  - [drawFloat](#drawfloat)
  - [drawNumber](#drawnumber)
  - [drawString](#drawstring)
  - [print](#print)
  - [printf](#printf)
  - [println](#println)
- [文本属性](#文本属性)
  - [setFont](#setfont)
  - [getFont](#getfont)
  - [showFont](#showfont)
  - [fontHeight](#fontheight)
  - [fontWidth](#fontwidth)
  - [loadFont](#loadfont)
  - [unloadFont](#unloadfont)
  - [setTextColor](#settextcolor)
  - [setTextSize](#settextsize)
  - [getTextSizeX](#gettextsizex)
  - [getTextSizeY](#gettextsizey)
  - [setTextStyle](#settextstyle)
  - [getTextStyle](#gettextstyle)
  - [textLength](#textlength)
  - [textWidth](#textwidth)
- [文本对齐及边距](#文本对齐及边距)
  - [setTextDatum](#settextdatum)
  - [getTextDatum](#gettextdatum)
  - [setTextPadding](#settextpadding)
  - [getTextPadding](#gettextpadding)
- [自动换行](#自动换行)
  - [setTextWrap](#settextwrap)

## 文本显示

### drawCenterString

**函数原型1：**

```cpp
void drawCenterString(const char *string, int32_t x, int32_t y, const IFont* font)
```

**函数原型2：**

```cpp
void drawCenterString(const char *string, int32_t x, int32_t y)
```

**功能说明：**

- 在中心位置书写文本 

**传入参数:**

- string：文本字符串
- x：绘制起点 x 坐标
- y：绘制起点 y 坐标

**返回值：**

- null

### drawChar

**函数原型1：**

```cpp
size_t drawChar(int32_t x, int32_t y, uint16_t uniCode, T color, T bg, float size_x, float size_y)
```

**函数原型2：**

```cpp
size_t drawChar(int32_t x, int32_t y, uint16_t uniCode, T color, T bg, float size)
```

**函数原型3：**

```cpp
size_t drawChar(uint16_t uniCode, int32_t x, int32_t y, uint8_t font)
``` 

**函数原型4：**

```cpp
size_t drawChar(uint16_t uniCode, int32_t x, int32_t y)
```

**功能说明：**

- 绘制单个字符

**传入参数:**

- x：绘制起点 x 坐标
- y：绘制起点 y 坐标
- uniCode：字符 UniCode 编码
- color：字符颜色
- bg：字符背景颜色
- size(_N)：文本缩放比例 
- font：文本字体格式

**返回值：**

- size_t：
  - 字符在 x 方向占用的总像素宽度

### drawFloat

**函数原型1：**

```cpp
size_t drawFloat(float floatNumber, uint8_t dp, int32_t poX, int32_t poY)
```

**函数原型2：**

```cpp
size_t drawFloat(float floatNumber, uint8_t dp, int32_t poX, int32_t poY, uint8_t font)
```

**功能说明：**

- 绘制浮点数

**传入参数:**
 
- floatNumber：浮点数
- dp：小数点后位数
- poX：起点 x 坐标
- poY：起点 y 坐标
- font：文本字体格式

**返回值：**

- size_t：字符串绘制的总水平像素宽度

### drawNumber

**函数原型1：**

```cpp
size_t drawNumber(long long_num, int32_t poX, int32_t poY)
```

**函数原型2：**

```cpp
size_t drawNumber(long long_num, int32_t poX, int32_t poY, uint8_t font)
```

**功能说明：**

- 绘制一个长整型数字

**传入参数:**

- long_num：长整型数字
- poX：x 坐标
- poY：y 坐标
- font：文本字体格式

**返回值：**

- size_t：字符串绘制的总水平像素宽度

### drawString

**函数原型1：**

```cpp
size_t drawString( const char *string, int32_t x, int32_t y)
```

**函数原型2：**

```cpp
size_t drawString( const char *string, int32_t x, int32_t y, const IFont* font)
```

**功能说明：**

- 绘制字符串

**传入参数:**

- string：要绘制的字符串
- x：绘制起点 x 坐标
- y：绘制起点 y 坐标
- font：文本字体格式

**返回值：**

- size_t：字符串绘制的总水平像素宽度

### print

**函数原型1：**

```cpp
size_t print(char c)
size_t print(const char str[])
```

**函数原型2：**

```cpp
size_t print(int  n, int base = 10)
size_t print(long n, int base = 10)
size_t print(unsigned char n, int base = 10)
size_t print(unsigned int  n, int base = 10)
size_t print(unsigned long n, int base = 10)
size_t print(double        n, int digits= 2)
```

**功能说明：**

- 输出文本到光标位置，兼容 Arduino 头文件 `Print.h` 。

**传入参数:**

- c：字符
- str：字符串
- n：整数或浮点数
- base：进制（默认为 10）
- digits：小数点后保留的位数（默认为 2）

**返回值：**

- size_t：输出的字符数

### printf

**函数原型：**

```cpp
size_t printf(const char* format, ...)
```

**功能说明：**

- 输出文本到光标位置，兼容 Arduino 头文件 `LibPrint.h` 。

**传入参数:**

- format：格式化字符串
- ...：可变参数

**返回值：**

- size_t: 输出的字符数

### println

**函数原型：**

```cpp
size_t println(void)
size_t println(char c)
size_t println(const char c[])
```

**函数原型：**

```cpp
size_t println(int  n, int base = 10) 
size_t println(long n, int base = 10)
size_t println(unsigned char n, int base = 10)
size_t println(unsigned int  n, int base = 10)
size_t println(unsigned long n, int base = 10)
size_t println(double        n, int digits= 2)
```

**功能说明：**

- 输出文本到光标位置，兼容 Arduino 头文件 `Print.h` 。

**传入参数:**

- c：字符/字符串
- n：整数或浮点数
- base：进制（默认为 10）
- digits：小数点后保留的位数（默认为 2）

**返回值：**

- size_t：输出的字符数

## 文本属性

### setFont

**函数原型：**

```cpp
void setFont(const IFont* font)
```

**功能说明：**

- 设置文本字体

**传入参数:**

- font：文本字体格式

**返回值：**

- null

### getFont

**函数原型：**

```cpp
const IFont* getFont (void)
```

**功能说明：**

- 获取由 [setFont](#setfont) 设置的当前使用的字体
 
**传入参数:**

- null

**返回值：**

- const IFont*：当前使用的字体对象指针 （关于[Font](/zh_CN/arduino/m5gfx/m5gfx_appendix#字体列表)）

### showFont

**函数原型：**

```cpp
void showFont(uint32_t td = 2000)
```

**功能说明：**

- 按照指定时间显示文本

**传入参数:**

- td：显示时间，单位为毫秒

**返回值：**

- null

### fontHeight

**函数原型：**

```cpp
int32_t fontHeight(const IFont* font)
```

**功能说明：**

- 获取指定字体的高度

**传入参数:**

- font：文本字体格式

**返回值：**

- int32_t：字体高度

### fontWidth

**函数原型：**

```cpp
int32_t fontWidth(const IFont* font)
```

**功能说明：**

- 获取指定字体的宽度

**传入参数:**

- font：文本字体格式

**返回值：**

- int32_t：字体宽度

### loadFont

**函数原型1：**

```cpp
bool loadFont(const uint8_t* array)
```

**函数原型2：**

```cpp
bool loadFont(T &fs, const char *path)
```

**函数原型3：**

```cpp
bool loadFont(const char *path)
```

**函数原型4：**

```cpp
bool loadFont(DataWrapper* data)
```

**功能说明：**

- 加载字体数据

\*此函数使用可参考[此处](../../guide/develop_tools/vlw_font_creator#2.使用vlw字体)

**传入参数:**

- array：指向字体数据的指针
- fs：字体数据对象
  - SPIFFS
  - SD
    etc
- path：字体文件路径
- data：指向字体数据对象的指针

**返回值：**

- bool：加载是否成功
  - true：成功
  - false：失败

### unloadFont

**函数原型：**

```cpp
void unloadFont(void)
```

**功能说明：**

- 将由 [setFont](#setfont) 设置的字体恢复为默认字体 `&fonts:：Font0` 。

**传入参数:**

- null

**返回值：**

- null

### setTextColor

**函数原型1：**

```cpp
void setTextColor(T color)
```

**函数原型2：**

```cpp
void setTextColor(T1 fgcolor, T2 bgcolor)
```

**功能说明：**

- 设置文本颜色

**传入参数:**

- color：文本颜色
- fgcolor：文本前景色
- bgcolor：文本背景色

**返回值：**

- null

### setTextSize

**函数原型1：**

```cpp
void setTextSize(float size)
```

**函数原型2：**

```cpp
void setTextSize(float sx, float sy)
```

**功能说明：**

- 设置文本大小

**传入参数:**

- size：文本缩放比例
- sx：文本 x 轴向缩放比例
- sy：文本 y 轴向缩放比例

**返回值：**

- null

### getTextSizeX

**函数原型：**

```cpp
float getTextSizeX(void)
``` 

**功能说明：**

- 获取由 [setTextSize](#settextsize) 设置的文本宽度

**传入参数:**

- null 

**返回值：**

- float：文本宽度

### getTextSizeY

**函数原型：**

```cpp
float getTextSizeY(void)
```

**功能说明：**

- 获取由 [setTextSize](#settextsize) 设置的文本高度

**传入参数:**

- null

**返回值：**

- float：文本高度

### setTextStyle

**函数原型：**

```cpp
void setTextStyle(const TextStyle& text_style)
```

**功能说明：**

- 设置文本样式

**传入参数:**

- text_style：文本样式对象 （关于[TextStyle](/zh_CN/arduino/m5gfx/m5gfx_appendix#struct-textstyle)）

**返回值：**

- null

### getTextStyle

**函数原型：**

```cpp
TextStyle& getTextStyle(void)
```

**功能说明：**

- 获取由 [setTextStyle](#settextstyle) 设置的文本样式信息

**传入参数:**

- null

**返回值：** 

- TextStyle&：文本样式信息的引用

### textLength

**函数原型：**

```cpp
int32_t textLength(const char *string, int32_t width)
```

**功能说明：**

- 获取在指定范围内能显示的字符个数

**传入参数:**

- string：需要显示的字符串指针
- width：指定范围的像素宽度

**返回值：**

- int32_t：能显示的字节个数

?>特别提醒：|返回值为字节个数而非字符个数，如中文字符为多字节字符，返回的字节个数大于字符个数

### textWidth

**函数原型：**

```cpp
int32_t textWidth(const char *string, const IFont* font)
```

**功能说明：**

- 返回屏幕上显示的字符串的宽度。若未指定字体，则会使用默认字体或通过 [setFont](#setfont) 方法设置的字体来计算。

**传入参数:**

- string：屏幕上显示的字符串指针
- font：文本字体格式

**返回值：**

- int32_t：显示的字符串像素宽度

## 文本对齐及边距

### setTextDatum

**函数原型：**

```cpp
void setTextDatum(textdatum_t datum)
```

**功能说明：**

- 设置的文本基准信息

**传入参数:**

- datum：文本对齐方式

#>说明：|此对齐方式指的是指定坐标点相对于文本内容的位置，具体对齐方式请见 [`textdatum_t`](/zh_CN/arduino/m5gfx/m5gfx_appendix#enum-textdatum_t)。

**返回值：**

- null

### getTextDatum

**函数原型：**
 
```cpp
textdatum_t getTextDatum(void)
```

**功能说明：**

- 获取由 [setTextDatum](#settextdatum) 设置的文本基准信息

**传入参数:**
 
- null
 
**返回值：**

- textdatum_t：文本对齐方式

### setTextPadding

**函数原型：**

```cpp
void setTextPadding(uint32_t padding_x)
```

**功能说明：**

- 设置文本填充值

**传入参数:**

- padding_x：文本填充值，单位为像素

**返回值：**

- null

### getTextPadding

**函数原型：**

```cpp
uint32_t getTextPadding(void)
```

**功能说明：** 

- 获取由 [setTextPadding](#settextpadding) 设置的文本填充值

**传入参数:**

- null

**返回值：** 

- uint32_t：文本填充值

## 自动换行

### setTextWrap

**函数原型：**

```cpp
void setTextWrap( bool wrapX, bool wrapY = false)
```

**功能说明：**

- 设置文本自动换行

**传入参数:**

- wrapX：文本 x 轴向自动换行标志
- wrapY：文本 y 轴向自动换行标志（默认为不换行）

**返回值：**

- null

#>说明：|不使用此函数系统默认开启x轴向自动换行。

**案例程序：**

```cpp line-num
#include <Arduino.h>
#include <M5GFX.h>

M5GFX display;

void setup() {
    display.begin();

    display.setRotation(3);
    if(display.isEPD())
    {
        display.setColorDepth(8);//The ink screen product supports a maximum bit depth of 8 bits.
        display.setEpdMode(epd_fastest);
    }
    else
    {
        display.setColorDepth(16);
    }
    
    display.clear(TFT_WHITE);
    display.setFont(&fonts::FreeMonoBoldOblique24pt7b);
    display.setTextColor(TFT_BLACK);
    display.setTextWrap(true);
    display.setCursor(0, 0);
    display.setTextSize(1,2);
    uint16_t x = display.getTextSizeX();
    uint16_t y = display.getTextSizeY();
    display.printf("Text SizeX:%d SizeY:%d", x, y);
    display.setTextSize(1,1);
    display.setTextDatum(top_left);//This alignment method refers to the position of the specified coordinate points relative to the text content.
    x = display.fontWidth(&fonts::Font0);
    y = display.fontHeight(&fonts::Font0);
    display.printf(" Font0 W:%d H:%d", x, y);
    display.setTextPadding(10);
    x = display.width() / 2;
    y = display.height() / 2;

    display.drawCenterString("This is CenterString", x, y);
    display.drawChar(0x004D, 0, y/4*7-24);//M
    display.drawChar(0x0035, 30, y/4*7-24);//5
    display.drawChar(0x0053, 30*2, y/4*7-24);//S
    display.drawChar(0x0074, 30*3, y/4*7-24);//t
    display.drawChar(0x0061, 30*4, y/4*7-24);//a
    display.drawChar(0x0063, 30*5, y/4*7-24);//c
    display.drawChar(0x006B, 30*6, y/4*7-24);//k
    display.drawFloat(127.45678, 5, 0, y/4*7);
    display.drawNumber(1234567890, 0, y*2-40);
    display.drawString("This is drawString", x/2, y/4*7);
}

void loop() {
}
```