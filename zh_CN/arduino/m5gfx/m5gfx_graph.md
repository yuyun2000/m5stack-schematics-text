# 图形绘制

- [线条图形](#线条图形)
  - [drawArc](#drawarc)
  - [drawBezier](#drawbezier)
  - [drawCircle](#drawcircle)
  - [drawEllipse](#drawellipse)
  - [drawEllipseArc](#drawellipsearc)
  - [drawFastHLine](#drawfasthline)
  - [drawFastVLine](#drawfastvline)
  - [drawLine](#drawline)
  - [drawGradientHLine](#drawgradienthline)
  - [drawGradientLine](#drawgradientline)
  - [drawGradientVLine](#drawgradientvline)
  - [drawPixel](#drawpixel)
  - [drawTriangle](#drawtriangle)
- [填充图形](#填充图形)
  - [fillAffine](#fillaffine)
  - [fillArc](#fillarc)
  - [fillCircle](#fillcircle)
  - [fillEllipse](#fillellipse)
  - [fillEllipseArc](#fillellipsearc)
  - [fillRect](#fillrect)
  - [fillRectAlpha](#fillrectalpha)
  - [fillRoundRect](#fillroundrect)
  - [fillTriangle](#filltriangle)
  - [floodFill](#floodfill)
  - [paint](#paint)
  - [copyRect](#copyrect)
- [特殊图形](#特殊图形)
  - [progressBar](#progressbar)
  - [qrcode](#qrcode)
- [write and read](#write-and-read)
  - [getStartCount](#getstartcount)
  - [readPixel](#readpixel)
  - [readPixelRGB](#readpixelrgb)
  - [readRect](#readrect)
  - [readRectRGB](#readrectrgb)
  - [startWrite](#startwrite)
  - [endWrite](#endwrite)
  - [pushBlock](#pushblock)
  - [pushPixels](#pushpixels)
  - [pushPixelsDMA](#pushpixelsdma)
  - [writeColor](#writecolor)
  - [writeFastHLine](#writefasthline)
  - [writeFastVLine](#writefastvline)
  - [writeFillRect](#writefillrect)
  - [writeFillRectPreclipped](#writefillrectpreclipped)
  - [writeIndexedPixels](#writeindexedpixels)
  - [writePixel](#writepixel)
  - [writePixels](#writepixels)
  - [writePixelsDMA](#writepixelsdma)

## 线条图形

### drawArc

**函数原型 1：** 

```cpp
void drawArc(int32_t x, int32_t y, int32_t r0, int32_t r1, float angle0, float angle1)
```

**函数原型 2：**
```cpp
void drawArc(int32_t x, int32_t y, int32_t r0, int32_t r1, float angle0, float angle1, const T &color)
```

**功能说明：**

- 绘制圆弧，r0、r1 不同将绘制粗圆弧。

**传入参数:**

- x：圆弧中心点 x 坐标
- y：圆弧中心点 y 坐标
- r0：内圆半径
- r1：外圆半径
- angle0：圆弧起始角度
- angle1：圆弧终点角度
- color：圆弧颜色 （关于[颜色编码](/zh_CN/arduino/m5gfx/m5gfx_appendix#颜色编码)）

**返回值：**

- null

### drawBezier

**函数原型 1：** 

```cpp
void drawBezier( int32_t x0, int32_t y0, int32_t x1, int32_t y1, int32_t x2, int32_t y2, const T& color)
```

**函数原型 2：**

```cpp
void drawBezier( int32_t x0, int32_t y0, int32_t x1, int32_t y1, int32_t x2, int32_t y2)
```

**函数原型 3：**

```cpp
void drawBezier( int32_t x0, int32_t y0, int32_t x1, int32_t y1, int32_t x2, int32_t y2, int32_t x3, int32_t y3, const T& color)
```

**函数原型 4：**

```cpp
void drawBezier( int32_t x0, int32_t y0, int32_t x1, int32_t y1, int32_t x2, int32_t y2, int32_t x3, int32_t y3, const T& color)
```

**功能说明：**

- 绘制贝塞尔曲线，有两种类型可供选择：3 点型和 4 点型。

**传入参数:**

- xN: 绘制点 x 坐标
- yN：绘制点 y 坐标
- color：曲线颜色 （关于[颜色编码](/zh_CN/arduino/m5gfx/m5gfx_appendix#颜色编码)）

**返回值：**

- null

### drawCircle

**函数原型 1：**

```cpp
void drawCircle( int32_t x, int32_t y, int32_t r)
```

**函数原型 2：** 

```cpp
void drawCircle( int32_t x, int32_t y, int32_t r, const T& color)
```

**功能说明：**

- 绘制圆

**传入参数:**

- x：圆心 x 坐标
- y：圆心 y 坐标
- r：圆半径
- color：圆颜色 （关于[颜色编码](/zh_CN/arduino/m5gfx/m5gfx_appendix#颜色编码)）

**返回值：** 

- null

### drawEllipse

**函数原型 1：**

```cpp
void drawEllipse( int32_t x, int32_t y, int32_t rx, int32_t ry)
```

**函数原型 2：** 

```cpp
void drawEllipse( int32_t x, int32_t y, int32_t rx, int32_t ry, const T& color)
```

**功能说明：**

- 绘制椭圆

**传入参数:**

### drawGradientVLine
- x：绘制圆心 x 坐标
- y：绘制圆心 y 坐标
- rx：椭圆长半轴
- ry：椭圆短半轴
- color：椭圆颜色  （关于[颜色编码](/zh_CN/arduino/m5gfx/m5gfx_appendix#颜色编码)）

**返回值：**

- null

### drawEllipseArc

**函数原型 1：**

```cpp
void drawEllipseArc( int32_t x, int32_t y, int32_t r0x, int32_t r1x, int32_t r0y, int32_t r1y, float angle0, float angle1)
```

**函数原型 2：**

```cpp
void drawEllipseArc( int32_t x, int32_t y, int32_t r0x, int32_t r1x, int32_t r0y, int32_t r1y, float angle0, float angle1, const T& color)
```

**功能说明：**

- 绘制椭圆弧，r0、r1 不同将绘制粗椭圆弧。

**传入参数:**

- x：椭圆弧中心 x 坐标
- y：椭圆弧中心 y 坐标
- r0x：内椭圆 x 半径
- r1x：内椭圆 y 半径
- r0y：外椭圆 x 半径
- r1y：外椭圆 y 半径
- angle0：起始角度
- angle1：结束角度
- color：椭圆弧颜色  关于[颜色编码](/zh_CN/arduino/m5gfx/m5gfx_appendix#颜色编码)）

**返回值：**

- null

### drawFastHLine

**函数原型 1：**

```cpp
void drawFastHLine( int32_t x, int32_t y, int32_t w)
```

**函数原型 2：**

```cpp
void drawFastHLine( int32_t x, int32_t y, int32_t w, const T& color)
```

**功能说明：**

- 绘制水平线

**传入参数:**

- x：起点 x 坐标
- y：起点 y 坐标
- w：线长度
- color：线颜色 （关于[颜色编码](/zh_CN/arduino/m5gfx/m5gfx_appendix#颜色编码)） 

**返回值：**

- null

### drawFastVLine

**函数原型 1：**

```cpp
void drawFastVLine( int32_t x, int32_t y, int32_t w)
```

**函数原型 2：**

```cpp
void drawFastVLine( int32_t x, int32_t y, int32_t w, const T& color)
```

**功能说明：**

- 绘制垂直线

**传入参数:**

- x：起点 x 坐标
- y：起点 y 坐标
- w：线长度
- color：线颜色 （关于[颜色编码](/zh_CN/arduino/m5gfx/m5gfx_appendix#颜色编码)）

**返回值：**

- null

### drawLine

**函数原型 1：**

```cpp
void drawLine( int32_t x0, int32_t y0, int32_t x1, int32_t y1)
```

**函数原型 2：**

```cpp
void drawLine( int32_t x0, int32_t y0, int32_t x1, int32_t y1, const T& color)
```

**功能说明：**

- 绘制一条直线

**传入参数:**

- x0：起点 x 坐标
- y0：起点 y 坐标
- x1：终点 x 坐标
- y1：终点 y 坐标
- color：线颜色 （关于[颜色编码](/zh_CN/arduino/m5gfx/m5gfx_appendix#颜色编码)）

**返回值：**

- null

### drawGradientHLine

**函数原型：**

```cpp
void drawGradientHLine( int32_t x, int32_t y, int32_t w, const T& colorstart, const T& colorend) 
```

**功能说明：**

- 绘制水平渐变线

**传入参数:**

- x：起点 x 坐标
- y：起点 y 坐标
- w：线宽度
- colorstart：起始颜色
- colorend：结束颜色 

**返回值：**

- null

### drawGradientLine

**函数原型：**

```cpp
void drawGradientLine ( int32_t x0, int32_t y0, int32_t x1, int32_t y1, const T& colorstart, const T& colorend )
```

**功能说明：**

- 绘制由两点确定的渐变线

**传入参数:**

- x0：起点 x 坐标
- y0：起点 y 坐标
- x1：终点 x 坐标
- y1：终点 y 坐标
- colorstart：起始颜色
- colorend：结束颜色 

**返回值：**

- null

### drawGradientVLine

**函数原型：**

```cpp
void drawGradientVLine( int32_t x, int32_t y, int32_t h, const T& colorstart, const T& colorend) 
```

**功能说明：**

- 绘制垂直渐变线

**传入参数:**

- x：起点 x 坐标
- y：起点 y 坐标
- h：线高度
- colorstart：起始颜色
- colorend：结束颜色

**返回值：**

- null

### drawPixel

**函数原型 1：**

```cpp
void drawPixel( int32_t x, int32_t y)
```

**函数原型 2：**

```cpp
void drawPixel( int32_t x, int32_t y, const T& color)
```

**功能说明：**

- 绘制一个像素点

**传入参数:**

- x：x 坐标
- y：y 坐标
- color：像素颜色 （关于[颜色编码](/zh_CN/arduino/m5gfx/m5gfx_appendix#颜色编码)）

**返回值：**

- null

### drawTriangle

**函数原型 1：**

```cpp
void drawTriangle( int32_t x0, int32_t y0, int32_t x1, int32_t y1, int32_t x2, int32_t y2)
```

**函数原型 2：**

```cpp
void drawTriangle( int32_t x0, int32_t y0, int32_t x1, int32_t y1, int32_t x2, int32_t y2, const T& color)
```

**功能说明：**

- 绘制三角形

**传入参数:**

- xN：三角形顶点 x 坐标
- yN：三角形顶点 y 坐标
- color：三角形颜色 （关于[颜色编码](/zh_CN/arduino/m5gfx/m5gfx_appendix#颜色编码)）

**返回值：**

- null

## 填充图形

### fillAffine

**函数原型 1：**

```cpp
void fillAffine(const float matrix[6], int32_t w, int32_t h)
```

**函数原型 2：**

```cpp
void fillAffine(const float matrix[6], int32_t w, int32_t h, const T& color)
```

**功能说明：**

- 填充仿射变换区域

**传入参数:**

- matrix：仿射变换矩阵
- w：图像宽度
- h：图像高度
- color：填充颜色 （关于[颜色编码](/zh_CN/arduino/m5gfx/m5gfx_appendix#颜色编码)）

**返回值：**

- null

### fillArc

**函数原型 1：**

```cpp
void fillArc( int32_t x, int32_t y, int32_t r0, int32_t r1, float angle0, float angle1)
```

**函数原型 2：**

```cpp
void fillArc( int32_t x, int32_t y, int32_t r0, int32_t r1, float angle0, float angle1, const T& color)
```

**功能说明：**

- 填充弧形区域

**传入参数:**

- x：弧形区域中心 x 坐标
- y：弧形区域中心 y 坐标
- r0：内半径
- r1：外半径
- angle0：起始角度
- angle1：结束角度
- color：填充颜色 （关于[颜色编码](/zh_CN/arduino/m5gfx/m5gfx_appendix#颜色编码)）

**返回值：**

- null

### fillCircle

**函数原型 1：**

```cpp
void fillCircle( int32_t x, int32_t y, int32_t r)
```

**函数原型 2：**

```cpp
void fillCircle( int32_t x, int32_t y, int32_t r, const T& color)
```

**功能说明：**

- 绘制填充颜色的圆

**传入参数:**

- x：圆心 x 坐标
- y：圆心 y 坐标
- r：圆半径
- color：圆颜色 （关于[颜色编码](/zh_CN/arduino/m5gfx/m5gfx_appendix#颜色编码)）

**返回值：**

- null

### fillEllipse

**函数原型 1：**

```cpp
void fillEllipse( int32_t x, int32_t y, int32_t rx, int32_t ry)
```

**函数原型 2：**

```cpp
void fillEllipse( int32_t x, int32_t y, int32_t rx, int32_t ry, const T& color)
```

**功能说明：**

- 绘制填充颜色的椭圆

**传入参数:**

- x：绘制圆心 x 坐标
- y：绘制圆心 y 坐标
- rx：椭圆长半轴
- ry：椭圆短半轴
- color：椭圆颜色 （关于[颜色编码](/zh_CN/arduino/m5gfx/m5gfx_appendix#颜色编码)）

**返回值：**

- null

### fillEllipseArc

**函数原型 1：**

```cpp
void fillEllipseArc( int32_t x, int32_t y, int32_t r0x, int32_t r1x, int32_t r0y, int32_t r1y, float angle0, float angle1)
```

**函数原型 2：**

```cpp
void fillEllipseArc( int32_t x, int32_t y, int32_t r0x, int32_t r1x, int32_t r0y, int32_t r1y, float angle0, float angle1, const T& color)
```

**功能说明：**

- 绘制填充颜色的椭圆弧，r0、r1 不同将绘制粗椭圆弧。

**传入参数:**

- x：椭圆弧中心 x 坐标
- y：椭圆弧中心 y 坐标
- r0x：内椭圆 x 半径
- r1x：内椭圆 y 半径
- r0y：外椭圆 x 半径
- r1y：外椭圆 y 半径
- angle0：起始角度
- angle1：结束角度
- color：椭圆弧颜色 （关于[颜色编码](/zh_CN/arduino/m5gfx/m5gfx_appendix#颜色编码)）

**返回值：**

- null

### fillRect

**函数原型 1：**

```cpp
void fillRect( int32_t x, int32_t y, int32_t w, int32_t h)
```

**函数原型 2：**

```cpp
void fillRect( int32_t x, int32_t y, int32_t w, int32_t h, const T& color)
```

**功能说明：**

- 绘制填充颜色的矩形

**传入参数:**

- x：矩形起点 x 坐标
- y：矩形起点 y 坐标
- w：矩形宽度
- h：矩形高度
- color：矩形颜色 （关于[颜色编码](/zh_CN/arduino/m5gfx/m5gfx_appendix#颜色编码)）

**返回值：**

- null

### fillRectAlpha

**函数原型：**

```cpp
void fillRectAlpha(int32_t x, int32_t y, int32_t w, int32_t h, uint8_t alpha, const T& color)
```

**功能说明：**

- 绘制带透明度的填充矩形

**传入参数:**

- x：矩形起点 x 坐标
- y：矩形起点 y 坐标
- w：矩形宽度
- h：矩形高度
- alpha：透明度（0-255）
- color：矩形颜色 （关于[颜色编码](/zh_CN/arduino/m5gfx/m5gfx_appendix#颜色编码)）

**返回值：**

- null

### fillRoundRect

**函数原型 1：**

```cpp
void fillRoundRect( int32_t x, int32_t y, int32_t w, int32_t h, int32_t r)
```

**函数原型 2：**

```cpp
void fillRoundRect( int32_t x, int32_t y, int32_t w, int32_t h, int32_t r, const T& color)
```

**功能说明：**

- 绘制圆角填充矩形

**传入参数:**

- x：矩形起点 x 坐标
- y：矩形起点 y 坐标
- w：矩形宽度
- h：矩形高度
- r：圆角半径
- color：矩形颜色 （关于[颜色编码](/zh_CN/arduino/m5gfx/m5gfx_appendix#颜色编码)）

**返回值：**

- null

### fillTriangle

**函数原型 1：**

```cpp
void fillTriangle( int32_t x0, int32_t y0, int32_t x1, int32_t y1, int32_t x2, int32_t y2)
```

**函数原型 2：**

```cpp
void fillTriangle( int32_t x0, int32_t y0, int32_t x1, int32_t y1, int32_t x2, int32_t y2, const T& color)
```

**功能说明：**

- 绘制填充三角形

**传入参数:**

- xN：三角形顶点 x 坐标
- yN：三角形顶点 y 坐标
- color：三角形颜色 （关于[颜色编码](/zh_CN/arduino/m5gfx/m5gfx_appendix#颜色编码)）

**返回值：**

- null

### floodFill

**函数原型 1：**

```cpp
void floodFill( int32_t x, int32_t y)
```

**函数原型 2：**

```cpp
void floodFill( int32_t x, int32_t y, const T& color)
```

**功能说明：**

- 填充指定坐标所对应的大致色域范围

**传入参数:**

- x：指定点 x 坐标
- y：指定点 y 坐标
- color：填充颜色  （关于[颜色编码](/zh_CN/arduino/m5gfx/m5gfx_appendix#颜色编码)）

**返回值：**

- null

### paint

**函数原型 1：**

```cpp
void paint( int32_t x, int32_t y)
```

**函数原型 2：**

```cpp
void paint( int32_t x, int32_t y, const T& color)
```

**功能说明：**

- 绘制指定位置的颜色，与 [floodFill](#floodfill) 功能相同。

**传入参数:**

- x：指定位置的 x 坐标
- y：指定位置的 y 坐标
- color：指定位置的颜色 （关于[颜色编码](/zh_CN/arduino/m5gfx/m5gfx_appendix#颜色编码)）

**返回值：**

- null

### copyRect

**函数原型：** 

```cpp
void copyRect(uint32_t dst_x, uint32_t dst_y, uint32_t w, uint32_t h, uint32_t src_x, uint32_t src_y)
```

**功能说明：**

- 拷贝矩形范围

**传入参数：**

- dst_x：拷贝目的地 x 坐标
- dst_y：拷贝目的地 y 坐标
- w：矩形宽度
- h：矩形高度
- src_x：拷贝目标 x 坐标
- src_y：拷贝目标 y 坐标

**返回值：**

- null

## 特殊图形

### progressBar

**函数原型：**

```cpp
void progressBar(int x, int y, int w, int h, uint8_t val)
```

**功能说明：**

- 显示蓝色进度条

**传入参数:**

- x：进度条的起始 x 坐标
- y：进度条的起始 y 坐标
- w：进度条的宽度
- h：进度条的高度
- val：进度值（0 - 100）

**返回值：**

- null

### qrcode

**函数原型：**

```cpp
void qrcode(const char *string, uint16_t x = 50, uint16_t y = 10, uint8_t width = 220, uint8_t version = 6)
void qrcode(const String &string, uint16_t x = 50, uint16_t y = 10, uint8_t width = 220, uint8_t version = 6)
```

**功能说明：**

- 根据指定字符串信息生成二维码

**传入参数:**

- string：要生成二维码的字符串
- x：二维码的起始 x 坐标
- y：二维码的起始 y 坐标
- width：二维码的宽度
- version：二维码的版本（默认为 6）

**返回值：**

- null

**案例程序：**

```cpp line-num
#include <Arduino.h>
#include <M5GFX.h>
#include <M5Unified.h>

M5GFX display;

void setup() {
    display.begin();
    display.setRotation(3);
    display.clear(TFT_WHITE);
    delay(1000);
    uint16_t x = display.width() / 2;
    uint16_t y = display.height() / 2;

    display.drawArc(x, y, 100, 200, 0, 90, TFT_BLACK);
    display.drawBezier(0, 0, x/2, 0, x/2, y/2, TFT_VIOLET);
    display.drawBezier(0, 0, x/2, 0, x/2, y, 0, y, TFT_DARKGREEN);
    display.drawCircle(x, y, 200, TFT_BLACK);
    display.drawEllipse(x, y, 300, 200);
    display.drawEllipseArc(x, y, 100, 200, 200, 300, 180, 270);
    display.drawFastHLine(0, y/2, x);
    display.drawFastVLine(x/2, 0, y);
    display.drawLine(0, 0, x, y);
    display.drawGradientHLine(x, y/2*3, x, TFT_BLUE, TFT_RED);
    display.drawGradientVLine(x/2*3, y, y, TFT_BLUE, TFT_RED);
    display.drawGradientLine(x, y, x*2, y*2, TFT_BLUE, TFT_RED);
    display.drawTriangle(x/2, 0, x/4, y/2, x/2, y);

    static float Affine_mat[9] = {1, 0, 0,
                                  0, 1, y,
                                  0, 0, 1  };
    display.fillAffine(Affine_mat, x/4, y/4, TFT_RED);

    display.fillArc(x, y, 100, 200, 90, 180, TFT_ORANGE);
    display.fillCircle(x, y, 100, TFT_YELLOW);
    display.fillEllipse(x, y, 100, 50, TFT_BLACK);
    display.fillEllipseArc(x, y, 100, 200, 200, 300, 270, 360, TFT_SKYBLUE);
    display.fillRect(x/4, y, x/4, y/4, TFT_PINK);
    display.fillRectAlpha(x/4, y/4*5, x/4, y/4, 85, TFT_PINK);
    display.fillRoundRect(0, y/4*5, x/4, y/4, 30, TFT_GREEN);
    display.fillTriangle(0, 0, x/4, y/2, 0, y, TFT_BLUE);

    display.progressBar(x, 0, x, 40, 66);
    display.qrcode("Hello! This is M5Stack.", x/2*3, y/4, y/4*3);

    delay(2000);
    display.floodFill(x/4, y/2+10, TFT_MAGENTA);
    display.paint(x/4, y/2-10, TFT_CYAN);
}

void loop() {
}
```

## write and read

### getStartCount

**函数原型：**

```cpp
uint32_t getStartCount(void)
```

**功能说明：**

- 获取面板调用 [startWrite](#startwrite) 的次数

**传入参数:**

- null 

**返回值：**

- uint32_t：调用次数

### readPixel

**函数原型：**

```cpp
uint16_t readPixel(int32_t x, int32_t y)
```

**功能说明：**

- 读取指定坐标的颜色编码，颜色编码格式为 RGB565

**传入参数:**

- x：指定的 x 坐标
- y：指定的 y 坐标

**返回值：**

- uint16_t：读取到的颜色编码

### readPixelRGB

**函数原型：**

```cpp
RGBColor readPixelRGB(int32_t x, int32_t y)
```

**功能说明：**

- 读取指定坐标的颜色编码，颜色编码格式为 RGB888

**传入参数:**

- x：指定的 x 坐标
- y：指定的 y 坐标

**返回值：**

- RGBColor：读取到的颜色编码

### readRect

**函数原型：**

```cpp
void readRect( int32_t x, int32_t y, int32_t w, int32_t h, T* data)
```

**功能说明：**

- 读取指定矩形区域的颜色数据

**传入参数:**

- x：指定的 x 坐标
- y：指定的 y 坐标
- w：指定的宽度
- h：指定的高度
- data：存储读取到的颜色数据的缓冲区

**返回值：**

- null

### readRectRGB

**函数原型：**

```cpp
void readRectRGB( int32_t x, int32_t y, int32_t w, int32_t h, RGBColor* data)
```

**功能说明：**

- 读取指定矩形区域的颜色数据，颜色编码格式为 RGB888

**传入参数:**

- x：指定的 x 坐标
- y：指定的 y 坐标
- w：指定的宽度
- h：指定的高度
- data：存储读取到的颜色数据的缓冲区

**返回值：**

- null

### startWrite

**函数原型：**

```cpp
void startWrite(bool transaction = true)
```

**功能说明：** 

- 在 SPI 总线上声明 CS（片选信号）。它与 [endWrite](#endwrite) 配合使用。声明 `startWrite` 可使 M5GFX 有效地利用 DMA 缓冲区。

#>注意事项:| 不能与 SD 卡访问功能同时使用。当存在多个绘图任务时，需进行单独控制。

**传入参数:**

- transaction：是否开启事务标志，默认为 true（开启）。

**返回值：**

- null

### endWrite

**函数原型：**

```cpp
void endWrite(void)
```

**功能说明**

- 在 SPI 总线上关闭 CS（片选信号），与 [startWrite](#startwrite) 配套使用。

**传入参数：**

- null

**返回值:**

- null

#>注意事项: |下列函数需要与 [startWrite](#startwrite) 和 [endWrite](#endwrite) 配合使用。

### pushBlock

#>注意事项：| 请在 M5GFX 库相关数据定义查看 [draw/push 和 write 函数之间的不同](/zh_CN/arduino/m5gfx/m5gfx_appendix#draw/push-和-write-函数之间的不同)

**函数原型：**

```cpp
void pushBlock( const T& color, uint32_t length)
```

**功能说明：**

- 在由 [setWindow](/zh_CN/arduino/m5gfx/m5gfx_sprite#setwindow) 或 [setAddrWindow](/zh_CN/arduino/m5gfx/m5gfx_sprite#setaddrwindow) 指定的矩形区域内绘制色块

**传入参数:**

- color：线条颜色
- length：线条长度

**返回值：**

- null

### pushPixels

**函数原型 1：**

```cpp
void pushPixels(T* data, int32_t len )
```

**函数原型 2：**

```cpp
void pushPixels(const uint16_t* data, int32_t len, bool swap)
void pushPixels(const void*     data, int32_t len, bool swap)
```

**功能说明：**

- 在由 [setWindow](/zh_CN/arduino/m5gfx/m5gfx_sprite#setwindow) 或 [setAddrWindow](/zh_CN/arduino/m5gfx/m5gfx_sprite#setaddrwindow) 指定的矩形区域内绘制像素点

**传入参数:**

- data：像素数据
- len：数据长度
- swap：是否交换字节（可选）

**返回值：**

- null

### pushPixelsDMA

**函数原型 1：**

```cpp
void pushPixelsDMA(T* data, int32_t len )
```

**函数原型 2：**

```cpp
void pushPixelsDMA(const uint16_t* data, int32_t len, bool swap)
void pushPixelsDMA(const void*     data, int32_t len, bool swap)
```

**功能说明：**

- 在由 [setWindow](/zh_CN/arduino/m5gfx/m5gfx_sprite#setwindow) 或 [setAddrWindow](/zh_CN/arduino/m5gfx/m5gfx_sprite#setaddrwindow) 指定的矩形区域内使用 DMA 绘制像素点

**传入参数:**

- data：像素数据
- len：数据长度
- swap：是否交换字节（可选）

**返回值：**

- null

### writeColor

**函数原型：**

```cpp
void writeColor( const T& color, uint32_t length)
```

**功能说明：**

- 在由 [setWindow](/zh_CN/arduino/m5gfx/m5gfx_sprite#setwindow) 或 [setAddrWindow](/zh_CN/arduino/m5gfx/m5gfx_sprite#setaddrwindow) 指定的矩形区域内绘制线条

#>注意事项：|此函数需要与 [startWrite](#startwrite) 和 [endWrite](#endwrite) 配合使用。

**传入参数:**

- color：绘制的颜色
- length：绘制的像素长度

**返回值：**

- null

### writeFastHLine

**函数原型 1：**

```cpp
void writeFastHLine( int32_t x, int32_t y, int32_t w)
```

**函数原型 2：**

```cpp
void writeFastHLine( int32_t x, int32_t y, int32_t w, const T& color)
```

**功能说明：**

- 绘制水平线

**传入参数:**

- x：起点 x 坐标
- y：起点 y 坐标
- w：线宽度
- color：线颜色 

**返回值：**

- null

### writeFastVLine

**函数原型 1：**

```cpp
void writeFastVLine( int32_t x, int32_t y, int32_t w)
```

**函数原型 2：**

```cpp
void writeFastVLine( int32_t x, int32_t y, int32_t w, const T& color)
```

**功能说明：**

- 绘制垂直线

**传入参数:**

- x：起点 x 坐标
- y：起点 y 坐标
- w：线宽度
- color：线颜色

**返回值：**

- null

### writeFillRect

**函数原型 1：**

```cpp
void writeFillRect( int32_t x, int32_t y, int32_t w, int32_t h)
```

**函数原型 2：**

```cpp
void writeFillRect( int32_t x, int32_t y, int32_t w, int32_t h, const T& color)
```

**功能说明：**

- 绘制填充颜色的矩形

**传入参数:**

- x：矩形起点 x 坐标
- y：矩形起点 y 坐标
- w：矩形宽度
- h：矩形高度
- color：矩形颜色

**返回值：**

- null

### writeFillRectPreclipped

**函数原型 1：**

```cpp
void writeFillRectPreclipped( int32_t x, int32_t y, int32_t w, int32_t h)
```

**函数原型 2：**

```cpp
void writeFillRectPreclipped( int32_t x, int32_t y, int32_t w, int32_t h, const T& color)
```

**功能说明：**

- 绘制预填充颜色的矩形

**传入参数:**

- x：矩形起点 x 坐标
- y：矩形起点 y 坐标
- w：矩形宽度
- h：矩形高度
- color：矩形颜色

**返回值：**

- null

### writeIndexedPixels

**函数原型：**

```cpp
void writeIndexedPixels(const uint8_t* data, T* palette, int32_t len, uint8_t depth = 8)
```

**功能说明：**

- 使用调色板颜色绘制图像数据

**传入参数:**

- data：图像数据
- paltte：调色板指针
- len：图像数据长度
- depth：颜色深度

**返回值：**

- null

### writePixel

**函数原型 1：**

```cpp
void writePixel(int32_t x, int32_t y)
```

**函数原型 2：**

```cpp
void writePixel(int32_t x, int32_t y, const T& color)
```

**功能说明：**

- 在裁剪区域内绘制一个像素点

**传入参数:**

- x：像素点 x 坐标
- y：像素点 y 坐标
- color：像素点颜色

**返回值：**

- null

### writePixels

**函数原型 1：**

```cpp
void writePixels(const T* data, int32_t len)
```

**函数原型 2：**

```cpp
void writePixels(const uint16_t* data, int32_t len, bool swap)
void writePixels(const void*     data, int32_t len, bool swap)
```

**功能说明：**

- 在裁剪区域内绘制像素点，数据会逐行绘制，从左上角开始。

**传入参数:**

- data：图像数据
- len：图像数据长度
- color：像素点颜色
- swap：字节交换标志

**返回值：**

- null

### writePixelsDMA

**函数原型 1：**

```cpp
void writePixelsDMA(const T* data, int32_t len)
```

**函数原型 2：**
```cpp
void writePixelsDMA(const uint16_t* data, int32_t len, bool swap)
void writePixelsDMA(const void*     data, int32_t len, bool swap)
```

**功能说明：**

- 在裁剪区域内使用 DMA 绘制像素点，数据会逐行绘制，从左上角开始。

**传入参数:**

- data：图像数据
- len：图像数据长度
- color：像素点颜色
- swap：字节交换标志

**返回值：**

- null

**案例程序：**
```cpp line-num
#include <Arduino.h>
#include <M5GFX.h>
#include <M5Unified.h>

M5GFX display;
const size_t data_len = 1320;
static uint16_t r_data;
RGBColor rgb_data;

void setup() {
    display.begin();
    display.setColorDepth(16);
    display.setRotation(1);
    display.clear(TFT_WHITE);
    display.setTextFont(&fonts::FreeSansOblique12pt7b);
    display.setTextColor(TFT_BLACK);
    delay(500);
    uint16_t x = display.width() / 2;
    uint16_t y = display.height() / 2;

    uint16_t w_data[data_len];
    for(int i=0; i<data_len; i++)
    {
        w_data[i] = 0;//BLACK
    }

    display.drawCenterString("Write Read Test", x, y);
    delay(1000);
    display.startWrite(true);
    display.writeFillRect(21, 21, 280, 10, TFT_RED);
    display.writeFillRectPreclipped(31, 31, 260, 10, TFT_BLUE);
    display.writeFastHLine(51, 51, 220, TFT_GREEN);
    display.writeFastHLine(51, 190, 220, TFT_GREEN);
    display.writeFastVLine(51, 51, 140, TFT_GREEN);
    display.writeFastVLine(270, 51, 140, TFT_GREEN);
    delay(500);
    for(int i=41; i<=280; i++)
    {
        for(int j=41; j<=50; j++)
        {
            display.writePixel(i, j, TFT_GREEN);
        }        
    }
    display.setWindow(51, 51, 270, 190);
    // By choosing to use the following code, you can clearly see the differences between setWindow and setAddrWindow.
    // display.setAddrWindow(51,51,270,190);
    display.pushBlock(TFT_ORANGE, data_len);
    display.writePixels(w_data, data_len, 0);//Has the same effect as the following code
    // display.pushPixels(w_data, data_len, 0);
    // display.writePixelsDMA(w_data, data_len, 0);
    delay(500);
    display.writeColor(TFT_DARKGREEN, data_len);//660 indicates that three rows of pixels have been drawn within the specified rectangular area.
    display.endWrite();

    auto color_565 = display.readPixel(21, 21);
    auto color_RGB = display.readPixelRGB(21, 21);
    display.setTextFont(&fonts::Font0);
    display.setCursor(21, 200);
    display.printf("565code: %#X, R:%d, G:%d, B:%d\n", color_565, color_RGB.r, color_RGB.g, color_RGB.b);

    display.readRect(25, 25, 1, 1, &r_data);
    display.readRectRGB(25, 25, 1, 1, &rgb_data);
    display.setCursor(21, 215);
    display.printf("888code: %#X\n", &r_data);
    display.setCursor(75, 230);
    display.printf("R:%d, G:%d, B:%d", &rgb_data.r, &rgb_data.g, &rgb_data.b);
}

void loop() {
}
```
