# StickC Display 屏幕显示

## RGB565 Color

下方API使用RGB565颜色编码格式

```cpp line-num
#define BLACK       0x0000 /*   0,   0,   0 */
#define NAVY        0x000F /*   0,   0, 128 */
#define DARKGREEN   0x03E0 /*   0, 128,   0 */
#define DARKCYAN    0x03EF /*   0, 128, 128 */
#define MAROON      0x7800 /* 128,   0,   0 */
#define PURPLE      0x780F /* 128,   0, 128 */
#define OLIVE       0x7BE0 /* 128, 128,   0 */
#define LIGHTGREY   0xC618 /* 192, 192, 192 */
#define DARKGREY    0x7BEF /* 128, 128, 128 */
#define BLUE        0x001F /*   0,   0, 255 */
#define GREEN       0x07E0 /*   0, 255,   0 */
#define CYAN        0x07FF /*   0, 255, 255 */
#define RED         0xF800 /* 255,   0,   0 */
#define MAGENTA     0xF81F /* 255,   0, 255 */
#define YELLOW      0xFFE0 /* 255, 255,   0 */
#define WHITE       0xFFFF /* 255, 255, 255 */
#define ORANGE      0xFDA0 /* 255, 180,   0 */
#define GREENYELLOW 0xB7E0 /* 180, 255,   0 */
#define PINK        0xFC9F /* 255, 255,  16 */
```


## fillScreen

**函数原型:**

```cpp
void fillScreen(uint32_t color);
```

**功能说明:**

- 以指定的颜色填充整个屏幕


**传入参数:**

- uint32_t color:
  - 颜色值

**返回值:**

- null

**案例程序:**

```cpp line-num
#include <M5StickC.h>

void setup() {
  M5.begin();
  M5.Lcd.fillScreen(BLUE);
}
void loop() {}
```

## setTextColor


**函数原型:**

```cpp
void setTextColor(uint16_t color, uint16_t backgroundcolor);
```

**功能说明:**

- 设置显示文本的前景颜色和背景颜色。

**传入参数:**

- uint16_t color:
  - 文本的前景颜色
- uint16_t backgroundcolor:
  - 文本的背景颜色

**返回值:**

- null


**案例程序:**

```cpp line-num
#include <M5StickC.h>

void setup() {
  M5.begin();
  M5.Lcd.setTextColor(RED, WHITE);
  M5.Lcd.println("Hello, M5Stack world!!");
}
void loop() {
}
```


## print

**函数原型:**

```cpp
size_t print(const String &s);
```

**功能说明:**

在屏幕的当前光标位置开始打印文本


**传入参数:**

- const String &s:
  - 字符串

**返回值:**

- size_t:
  - 打印的文本长度


**案例程序:**

```cpp line-num
#include <M5StickC.h>

void setup() {
  M5.begin();
  M5.Lcd.print("print text");
}
void loop() {}
```

## setCursor

**函数原型:**

```cpp
void setCursor(int16_t x0, int16_t y0);
```

**功能说明:**

- 移动光标位置到(x0, y0)处。

**传入参数:**

- int16_t x0:
  - x坐标
- int16_t y0:
  - y坐标


**返回值:**

- null


**案例程序:**

```cpp line-num
#include <M5StickC.h>

void setup() {
  M5.begin();
  M5.Lcd.setCursor(7, 20);
  M5.Lcd.println("scan done");
  M5.Lcd.setCursor(5, 60);
  M5.Lcd.printf("50 AP");
}
void loop(){}
```


## drawPixel

**函数原型:**

```cpp
void drawPixel(int16_t x, int16_t y, uint16_t color);
```

**功能说明:**

- 在位置(x,y)绘制像素


**传入参数:**

- int16_t x:
  - x坐标
- int16_t y:
  - y坐标
- uint16_t color:
  - 颜色值

**返回值:**

- null


**案例程序:**

```cpp line-num
#include <M5StickC.h>

void setup() {
  M5.begin();
  M5.Lcd.drawPixel(22, 22, RED);
}
void loop() {}
```

## drawLine

**函数原型:**

```cpp
void drawLine(int16_t x0, int16_t y0, int16_t x1, int16_t y1, uint16_t color);
```

**功能说明:**

- 以指定的颜色从点(x0,y0)到点(x1,y1)画直线

**传入参数:**

- int16_t x0:
  - 直线起点x0坐标
- int16_t y0:
  - 直线起点y0坐标
- int16_t x1:
  - 直线终点x1坐标
- int16_t y1:
  - 直线终点y1坐标
- uint16_t color
  - 颜色值

**返回值:**

- null

**案例程序:**

```cpp line-num
#include <M5StickC.h>

void setup() {
  M5.begin();
  M5.Lcd.drawLine(0, 0, 12, 12, BLUE);
}
void loop() {}
```

## drawTriangle

**函数原型:**

```cpp
void drawTriangle(int16_t x0, int16_t y0, int16_t x1, int16_t y1, int16_t x2, int16_t y2, uint16_t color);
```

**功能说明:**

- 以指定颜色画三角形,顶点分别为(x0,y0),(x1,y1)和(x2,y2)

**传入参数:**

- int16_t x0:
  - 三角形顶点x0坐标
- int16_t y0:
  - 三角形顶点y0坐标
- int16_t x1:
  - 三角形顶点x1坐标
- int16_t y1:
  - 三角形顶点y1坐标
- int16_t x2:
  - 三角形顶点x2坐标
- int16_t y2:
  - 三角形顶点y2坐标
- uint16_t color
  - 颜色值

**返回值:**

- null


**案例程序:**

```cpp line-num
#include <M5StickC.h>

void setup() {
  M5.begin();
  M5.Lcd.drawTriangle(22, 22, 69, 98, 51, 22, RED);
}
void loop() {}
```


## fillTriangle


**函数原型:**

```cpp
void fillTriangle(int16_t x0, int16_t y0, int16_t x1, int16_t y1, int16_t x2, int16_t y2, uint16_t color);
```

**功能说明:**

- 以指定颜色绘制填充三角形,顶点分别为(x0,y0),(x1,y1)和(x2,y2)


**传入参数:**

- int16_t x0:
  - 三角形顶点x0坐标
- int16_t y0:
  - 三角形顶点y0坐标
- int16_t x1:
  - 三角形顶点x1坐标
- int16_t y1:
  - 三角形顶点y1坐标
- int16_t x2:
  - 三角形顶点x2坐标
- int16_t y2:
  - 三角形顶点y2坐标
- uint16_t color
  - 颜色值

**返回值:**

- null


**案例程序:**

```cpp line-num
#include <M5StickC.h>

void setup() {
  M5.begin();
  M5.Lcd.fillTriangle(22, 22, 69, 98, 51, 22, RED);
}
void loop() {}
```


## drawRect


**函数原型:**

```cpp
void drawRect(int16_t x, int16_t y, int16_t w, int16_t h, uint16_t color);
```

**功能说明:**

- 以指定颜色画矩形,其中矩形左上角坐标为(x,y),宽高分别为width和height

**传入参数:**

- int16_t x:
  - 矩形左上角x坐标
- int16_t y:
  - 矩形左上角y坐标
- int16_t w:
  - 矩形宽度(px)
- int16_t h:
  - 矩形高度(px)
- uint16_t color:
  - 颜色值

**返回值:**

- null

**案例程序:**

```cpp line-num
#include <M5StickC.h>

void setup() {
  M5.begin();
  M5.Lcd.drawRect(50, 100, 30, 10, BLUE);
}
void loop() {}
```


## fillRect


**功能说明:**

- 以指定颜色画`填充形式`的矩形,其左上角坐标为(x,y),宽高分别为 width和 height

**函数原型:**

```cpp
void fillRect(int16_t x, int16_t y, int16_t w, int16_t h, uint16_t color);
```

**传入参数:**

- int16_t x:
  - 矩形左上角x坐标
- int16_t y:
  - 矩形左上角y坐标
- int16_t w:
  - 矩形宽度(px)
- int16_t h:
  - 矩形高度(px)
- uint16_t color:
  - 颜色值

**返回值:**

- null

**案例程序:**

```cpp line-num
#include <M5StickC.h>

void setup() {
  M5.begin();
  M5.Lcd.fillRect(50, 100, 20, 10, BLUE);
}
void loop() {}
```

## drawRoundRect


**函数原型:**

```cpp
void drawRoundRect(int16_t x0, int16_t y0, int16_t w, int16_t h, int16_t radius, uint16_t color);
```

**功能说明:**

以指定颜色画`圆角`矩形,其中矩形左上角坐标为(x,y),宽高分别为width和height,圆角半径为radius


**传入参数:**

- int16_t x:
  - 矩形左上角x坐标
- int16_t y:
  - 矩形左上角y坐标
- int16_t w:
  - 矩形宽度(px)
- int16_t h:
  - 矩形高度(px)
- int16_t radius:
  - 圆角半径
- uint16_t color:
  - 颜色值

**返回值:**

- null

**案例程序:**

```cpp line-num
#include <M5StickC.h>

void setup() {
  M5.begin();
  M5.Lcd.fillRoundRect(40, 70, 20, 10, 4, BLUE);
}
void loop() {}
```

