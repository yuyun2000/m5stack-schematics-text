# LGFX_Button Class

- [LGFX_Button Class](#lgfx_button-class)
  - [initButton](#initbutton)
  - [initButtonUL](#initbuttonul)
  - [setLabelText](#setlabeltext)
  - [setLabelDatum](#setlabeldatum)
  - [setOutlineColor](#setoutlinecolor)
  - [setFillColor](#setfillcolor)
  - [setTextColor](#settextcolor)
  - [drawButton](#drawbutton)
  - [contains](#contains)
  - [press](#press)
  - [isPressed](#ispressed)
  - [justPressed](#justpressed)
  - [justReleased](#justreleased)
- [综合案例程序](#综合案例程序)


## initButton

**函数原型:**

```cpp  
void initButton( LovyanGFX *gfx, int16_t x, int16_t y, uint16_t w, uint16_t h, const T& outline, const T& fill, 
                 const T& textcolor, const char *label, float textsize_x = 1.0f, float textsize_y = 0.0f)
```

**功能说明:**

- 初始化按钮

**传入参数:**

- gfx: 指向 LGFX 类的指针
- x: 按钮的 x 坐标
- y: 按钮的 y 坐标
- w: 按钮的宽度
- h: 按钮的高度
- outline: 按钮的轮廓颜色
- fill: 按钮的填充颜色
- textcolor: 按钮的文本颜色
- label: 按钮的标签文本
- textsize_x: 按钮文本的 x 方向缩放比例
- textsize_y: 按钮文本的 y 方向缩放比例

**返回值:**

- null

**案例程序:**

```cpp line-num
#include <Arduino.h>
#include <M5GFX.h>
#include <M5Unified.h>

static int32_t w;
static int32_t h;

LGFX_Button button;

void setup(void) {
    auto cfg = M5.config();
    M5.begin(cfg);
    w = M5.Lcd.width();
    h = M5.Lcd.height();
    button.initButton(&M5.Lcd, w / 2, h / 2, 100, 50, TFT_RED, TFT_YELLOW, TFT_BLACK, "Btn", 2, 2);
    button.drawButton();
}

void loop(void) {
}
```

## initButtonUL

**函数原型:**

```cpp
void initButtonUL( LovyanGFX *gfx, int16_t x, int16_t y, uint16_t w, uint16_t h, const T& outline, const T& fill,
                   const T& textcolor, const char *label, float textsize_x = 1.0f, float textsize_y = 0.0f)
```

**功能说明:**

- 初始化按钮，该函数与 initButton 类似，但以左上角为基准点。

**传入参数:**

- gfx: 指向 LGFX 类的指针
- x: 按钮的 x 坐标
- y: 按钮的 y 坐标
- w: 按钮的宽度
- h: 按钮的高度
- outline: 按钮的轮廓颜色
- fill: 按钮的填充颜色
- textcolor: 按钮的文本颜色
- label: 按钮的标签文本
- textsize_x: 按钮文本的 x 方向缩放比例
- textsize_y: 按钮文本的 y 方向缩放比例

**返回值:**

- null

**案例程序:**

```cpp line-num
#include <Arduino.h>
#include <M5GFX.h>
#include <M5Unified.h>

static int32_t w;
static int32_t h;

LGFX_Button button;

void setup(void) {
    auto cfg = M5.config();
    M5.begin(cfg);
    w = M5.Lcd.width();
    h = M5.Lcd.height();
    button.initButtonUL(&M5.Lcd, w / 2, h / 2, 100, 50, TFT_RED, TFT_YELLOW, TFT_BLACK, "Btn", 2, 2);
    button.drawButton();
}

void loop(void) {
}
```

#>注意事项: | 上述两初始化按键函数中的 label 参数是一个指向字符串的指针, 该字符串必须在使用前被初始化, 否则会导致未定义行为，编译不通过。


## setLabelText

**函数原型:**

```cpp
void setLabelText(const char* label)
```

**功能说明:**

- 设置按钮的标签文本

**传入参数:**

- label: 按钮的标签文本

**返回值:**

- null

**案例程序:**

```cpp line-num
#include <Arduino.h>
#include <M5GFX.h>
#include <M5Unified.h>

static int32_t w;
static int32_t h;

LGFX_Button button;

void setup(void) {
    auto cfg = M5.config();
    M5.begin(cfg);
    w = M5.Lcd.width();
    h = M5.Lcd.height();
    button.initButton(&M5.Lcd, w / 2, h / 2, 100, 50, TFT_RED, TFT_YELLOW, TFT_BLACK, "null", 2, 2);
    button.setLabelText("BTN");
    button.drawButton();
}

void loop(void) {
}  
```

## setLabelDatum

**函数原型:**

```cpp
void setLabelDatum(int16_t x_delta, int16_t y_delta, textdatum_t datum = middle_center)
```

**功能说明:**

- 设置按钮的标签基准点

**传入参数:**

- x_delta: 标签的 x 坐标偏移量
- y_delta: 标签的 y 坐标偏移量
- datum: 标签的对齐方式 （关于 [textdatum_t](/zh_CN/arduino/m5gfx/m5gfx_appendix#enum%20textdatum_t)）

**返回值:**

- null

**案例程序:**

```cpp line-num
#include <Arduino.h>
#include <M5GFX.h>
#include <M5Unified.h>

static int32_t w;
static int32_t h;

LGFX_Button button;

void setup(void) {
    auto cfg = M5.config();
    M5.begin(cfg);
    w = M5.Lcd.width();
    h = M5.Lcd.height();
    button.initButtonUL(&M5.Lcd, 0, 0, 100, 50, TFT_RED, TFT_YELLOW, TFT_BLACK, "Btn", 2, 2);
    button.setLabelDatum(0,0,middle_left);
    button.drawButton();
}

void loop(void) {
}
```

## setOutlineColor

**函数原型:**

```cpp
void setOutlineColor(const T& clr)
```

**功能说明:**

- 设置按钮的轮廓颜色

**传入参数:**

- clr: 按钮的轮廓颜色 （关于[颜色编码](/zh_CN/arduino/m5gfx/m5gfx_appendix#%E9%A2%9C%E8%89%B2%E7%BC%96%E7%A0%81)）

**返回值:**

- null

## setFillColor

**函数原型:**

```cpp
void setFillColor(const T& clr)
```

**功能说明:**

- 设置按钮的填充颜色

**传入参数:**

- clr: 按钮的填充颜色

**返回值:**

- null

## setTextColor

**函数原型:**

```cpp
void setTextColor(const T& clr)
```

**功能说明:**

- 设置按钮的文本颜色

**传入参数:**

- clr: 按钮的文本颜色

**返回值:**

- null

## drawButton

**函数原型:**

```cpp
void drawButton(bool inverted = false, const char* long_name = nullptr)
```

**功能说明:**

- 绘制按钮

**传入参数:**

- inverted: 反转按钮的颜色标志
- long_name: 按钮的长名称

**返回值:**

- null

**案例程序:**

```cpp line-num
#include <Arduino.h>
#include <M5GFX.h>
#include <M5Unified.h>

static int32_t w;
static int32_t h;

LGFX_Button button;

void setup(void) {
    auto cfg = M5.config();
    M5.begin(cfg);
    w = M5.Lcd.width();
    h = M5.Lcd.height();
    button.initButton(&M5.Lcd, w / 2, h / 2, 100, 50, TFT_RED, TFT_YELLOW, TFT_BLACK, "BTN", 2, 2);
    
    button.setOutlineColor(TFT_WHITE);//set button outline color
    button.setFillColor(TFT_BLUE);//set button color
    button.setTextColor(TFT_DARKGRAY);//set button text color
    button.drawButton();//draw button
}

void loop(void) {
}
```

## contains

**函数原型:**

```cpp
bool contains(int16_t x, int16_t y)
``` 

**功能说明:**

- 判断指定的坐标是否在按钮范围内

**传入参数:**

- x: 坐标的 x 值
- y: 坐标的 y 值

**返回值:**

- bool
  - true: 坐标在按钮范围内
  - false: 坐标不在按钮范围内

**案例程序:**

```cpp line-num
#include <Arduino.h>
#include <M5GFX.h>
#include <M5Unified.h>

static int32_t w;
static int32_t h;

LGFX_Button button;

void setup(void) {
    auto cfg = M5.config();
    M5.begin(cfg);
    w = M5.Lcd.width();
    h = M5.Lcd.height();
    button.initButton(&M5.Lcd, w / 2, h / 2, 100, 50, TFT_RED, TFT_YELLOW, TFT_BLACK, "BTN", 2, 2);
    button.drawButton();

    M5.Display.setTextDatum(middle_center);
    M5.Display.setTextFont(&fonts::FreeSans12pt7b);
    M5.Display.setTextSize(1);
    M5.Display.drawString("Coordinate Contained ? : \n", M5.Display.width() / 2, M5.Display.height() - 50);
    const char *con_str = button.contains(w / 2, h / 2) ? "Yes" : "No";// coordinate: (w / 2, h / 2)
    M5.Display.drawString(con_str, M5.Display.width() / 2, M5.Display.height() - 20);
}

void loop(void) {
}
```

## press

**函数原型:**

```cpp
void press(bool p)
``` 

**功能说明:**

- 设置按钮的按下状态

**传入参数:**

- p: 按钮的按下状态

**返回值:**

- null

## isPressed

**函数原型:**

```cpp
bool isPressed(void)
```

**功能说明:**

- 判断按钮是否被按下

**传入参数:**

- null

**返回值:**

- bool
  - true: 按钮被按下
  - false: 按钮未被按下

## justPressed

**函数原型:**

```cpp
bool justPressed(void)
``` 

**功能说明:**

- 判断按钮是否刚刚被按下

**传入参数:**

- null

**返回值:**

- true: 按钮刚被按下
- false: 按钮不是刚被按下

## justReleased

**函数原型:**

```cpp
bool justReleased(void)
```

**功能说明:**

- 判断按钮是否刚被释放

**传入参数:**

- null

**返回值:**

- true: 按钮刚被释放
- false: 按钮不是刚被释放

#>注意事项: | 上述四按键状态函数作用仅为状态记录，没有检测实际按键操作。

## 综合案例程序

**案例程序:**

```cpp line-num
#include <Arduino.h>
#include <M5GFX.h>
#include <M5Unified.h>

static int32_t w;
static int32_t h;

LGFX_Button button;

void setup(void) {
    auto cfg = M5.config();
    M5.begin(cfg);
    w = M5.Lcd.width();
    h = M5.Lcd.height();
    button.initButton(&M5.Lcd, w / 2, h / 2, 100, 50, TFT_RED, TFT_YELLOW,
                      TFT_BLACK, "null", 2, 2);
    button.drawButton();
}

void loop(void) {
    M5.update();
    if (M5.BtnA.isPressed()) {
        button.press(true);
        button.drawButton(true, "BtnA");
        M5.Lcd.drawString("Button A Pressed ", 0, 0, &fonts::lgfxJapanGothic_16);
    } 
    else if (M5.BtnB.isPressed()) {
        button.press(true);
        button.drawButton(true, "BtnB");
        M5.Lcd.drawString("Button B Pressed ", 0, 0, &fonts::lgfxJapanGothic_16);
    }
    else if (M5.BtnC.isPressed()) {
        button.press(true);
        button.drawButton(true, "BtnC");
        M5.Lcd.drawString("Button C Pressed ", 0, 0, &fonts::lgfxJapanGothic_16);
    }
    else {
        button.press(false);
        button.drawButton(false, "Test");
        M5.Lcd.drawString("Button  Released", 0, 0, &fonts::lgfxJapanGothic_16);
    }
    delay(100);
}  
```

例程效果如下：

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/644/LGFX_button_comprehensive_example.mp4" type="video/mp4"></video>