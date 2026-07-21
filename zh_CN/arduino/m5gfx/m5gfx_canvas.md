# M5Canvas Class

## 关于 M5Canvas

M5Canvas 为 LGFX_Sprite 的派生类，使用方式基本上与 TFT_eSPI 的 Sprite 相同，我们之所以可以称它为 M5Canvas，是因为它是从内存上绘图的角度来看，称它为 "Canvas "是合适的, 而不是M5GFX中定义的 "Sprite"，但是为了与TFT_eSprite兼容，pushSprite等方法仍然保留。

有关下面未包含的更详细的API信息，请参阅[此处](./m5gfx_functions)。

### Canvas 的优势

- 它可以提前在内存中绘制，并一次性显示在面板上，以便快速显示。

- 对显示小字符等很有用。

- 可以使用透明的颜色来提供重叠。

- 在显示屏上绘图时，可以进行缩放、旋转和抗锯齿。

## 构造函数

1. `M5Canvas()`

- 没有参数。
- 如果没有指定参数，必须在推送或绘制时指定，否则会出现问题。

2. `M5Canvas(M5GFX&)`

- 针对 M5GFX。
- 如果M5GFX被指定为一个参数，它将默认绘制到M5GFX设备。

建议使用 `M5Canvas(M5GFX&)`构造函数来确保有正确的绘制目标。

## LGFX_Sprite Class

- [createSprite](#createsprite)
- [fillSprite](#fillsprite)
- [pushSprite](#pushsprite)
- [deleteSprite](#deletesprite)
- [createFromBmp](#createfrombmp)
- [createFromBmpFile](#createfrombmpfile)
- [setBitmapColor](#setbitmapcolor)
- [setColorDepth](#setcolordepth)
- [createPalette](#createpalette)
- [getPalette](#getpalette)
- [setPaletteGrayscale](#setpalettegrayscale)
- [setPaletteColor](#setpalettecolor)
- [getPaletteIndex](#getpaletteindex)
- [deletePalette](#deletepalette)
- [readPixelValue](#readpixelvalue)
- [setPsram](#setpsram)
- [setBuffer](#setbuffer)
- [pushRotated](#pushrotated)
- [pushRotatedWithAA](#pushrotatedwithaa)
- [pushRotateZoom](#pushrotatezoom)
- [pushRotateZoomWithAA](#pushrotatezoomwithaa)
- [pushAffine](#pushaffine)
- [pushAffineWithAA](#pushaffinewithaa)

?>**特别提醒:**| 如果使用调色板，所有涉及到颜色设置的函数`只能通过调色板颜色索引号达到设置颜色的目的`，获取到的颜色信息也是`颜色索引号`而非颜色数值。

### createSprite

**函数原型:**

```cpp
void* createSprite(int32_t w, int32_t h)
```

**功能说明:**

- 创建画布

**传入参数:**

- w: 画布宽度
- h: 画布高度

**返回值:**

- null

### fillSprite

**函数原型:**

```cpp
void fillSprite (const T& color)
```

**功能说明:**

- 填充画布

**传入参数:**

- color: 填充颜色

**返回值:**

- null

### pushSprite

**函数原型1:**

```cpp
void pushSprite(int32_t x, int32_t y, const T& transp)
```

**函数原型2:**

```cpp
void pushSprite(LovyanGFX* dst, int32_t x, int32_t y, const T& transp)
```

**函数原型3:**

```cpp
void pushSprite(int32_t x, int32_t y)
```

**函数原型4:**

```cpp
void pushSprite(LovyanGFX* dst, int32_t x, int32_t y)
```

**功能说明:**

- 以指定坐标为基准点推送画布，基准点位于画布左上角。

**传入参数:**

- dst: 目标 LovyanGFX 对象
- x: 画布基准点 x 坐标
- y: 画布基准点 y 坐标
- transp: 透明颜色

**返回值:**

- null

### deleteSprite

**函数原型:**

```cpp
void deleteSprite(void)
```

**功能说明:**

- 删除画布

**传入参数:**

- null

**返回值:**

- null

**案例程序**

1.简单运用
```cpp line-num
#include <M5GFX.h>
#include <M5Unified.h>

static int32_t Disw;
static int32_t Dish;

void setup() {
    M5.begin();
    Disw = M5.Lcd.width();
    Dish = M5.Lcd.height();

    M5.Lcd.fillScreen(TFT_WHITE);

    M5Canvas canvas(&M5.Lcd);
    canvas.createSprite(100, 100);//set sprite size
    canvas.fillSprite(TFT_PINK);//fill sprite with color XXX
    delay(1000);
    canvas.fillSprite(TFT_BLACK);//fill sprite with color XXX
    canvas.println("M5Canvas");
    canvas.pushSprite(&M5.Lcd, Disw / 2 - 50, Dish / 2 - 50, TFT_PINK);//"&M5.Lcd" is not necessary here
    canvas.deleteSprite();
    //In this example, PINK will not be displayed
}

void loop() {
}   
```

例程效果如下：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/658/fire_M5GFX_E1.jpg" width="40%">

2.合并多个 Canvas 进行绘制
```cpp line-num
#include <M5GFX.h>
#include <M5Unified.h>

static int32_t Disw;
static int32_t Dish;

void setup() {
    M5.begin();
    Disw = M5.Lcd.width();
    Dish = M5.Lcd.height();

    M5.Lcd.fillScreen(TFT_WHITE);

    M5Canvas canvas(&M5.Lcd);
    M5Canvas can1(&M5.Lcd);
    M5Canvas can2(&M5.Lcd);

    canvas.createSprite(100, 100);//set sprite size
    canvas.fillSprite(TFT_PINK);//fill sprite with color XXX
    canvas.println("M5Canvas");
    
    can1.createSprite(30, 30);
    can1.fillSprite(TFT_BLUE);
    can1.println("Can1");
    can1.fillCircle(15, 15, 5, TFT_YELLOW);

    can2.createSprite(30, 30);
    can2.fillSprite(TFT_GREEN);
    can2.println("Can2");
    can2.fillTriangle(15, 10, 0, 30, 30, 30, TFT_BLUE);

    canvas.pushSprite(Disw / 2 - 50, Dish / 2 - 50);
    can1.pushSprite(Disw / 2 - 30, Dish / 2 - 30);
    can2.pushSprite(Disw / 2, Dish / 2);

    canvas.deleteSprite();
    can1.deleteSprite();
    can2.deleteSprite();
}

void loop() {
}     
```

例程效果如下：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/658/fire_M5GFX_E2.jpg" width="40%">

### createFromBmp

**函数原型1:**

```cpp
bool createFromBmp(const uint8_t *bmp_data, uint32_t bmp_len = ~0u)
```

**功能说明:**

- 从 BMP 数据创建画布

**传入参数:**

- bmp_data: BMP 数据指针
- bmp_len: BMP 数据长度（默认为 ~0u）

**函数原型2:**

```cpp
bool createFromBmp(T &fs, const char *path)
```

**功能说明:**

- 从 BMP 文件创建画布

**传入参数:**

- fs: 文件系统对象
- SPIFFS
- SD    
etc
- path: BMP 文件路径
    
**返回值:**

- bool
- true: 创建成功
- false: 创建失败

### createFromBmpFile

**函数原型1:**

```cpp
bool createFromBmpFile(const char *path)
```

**函数原型2:**

```cpp
bool createFromBmpFile(T &fs, const char *path)
```

**功能说明:**

- 从 BMP 文件创建画布

**传入参数:**

- path: BMP 文件路径
- fs: 文件系统对象
- SPIFFS
- SD    
etc

**返回值:**

- bool
- true: 创建成功
- false: 创建失败

此示例程序需要准备一张 microSD 卡，格式化为 FAT32 格式，在其根目录放入两张 `PNG` 图片并命名为 `LGFX_Canavs_Test01.bmp`、`LGFX_Canavs_Test02.bmp`。示例程序以`M5Fire`为目标设备，图片的分辨率为 `320*240`，你可以直接下载 [示例图片1](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/658/LGFX_Canavs_Test01.bmp)、[示例图片2](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/658/LGFX_Canavs_Test02.bmp)。如果图片的分辨率不是 `320*240`，则程序会根据预设来决定显示方式，可能会有显示异常。

?>注意事项: | 下述代码中头文件`SD.h`必须放在`<M5Unified.h>`之前，否则会导致编译不通过。

**案例程序**

```cpp line-num
#include <Arduino.h>
#include <SD.h>//This header file must before M5Unified.h
#include <SPI.h>
#include <M5GFX.h>
#include <M5Unified.h>

#define SD_SPI_CS_PIN   4
#define SD_SPI_SCK_PIN  18
#define SD_SPI_MOSI_PIN 23
#define SD_SPI_MISO_PIN 19

static int32_t Disw;
static int32_t Dish;

void setup() {
    M5.begin();
    Disw = M5.Lcd.width();
    Dish = M5.Lcd.height();

    M5.Lcd.fillScreen(TFT_BLACK);

    M5.Display.setTextFont(&fonts::Orbitron_Light_24);
    M5.Display.setTextSize(1);
    // SD Card Initialization
    SPI.begin(SD_SPI_SCK_PIN, SD_SPI_MISO_PIN, SD_SPI_MOSI_PIN, SD_SPI_CS_PIN);
    if (!SD.begin(SD_SPI_CS_PIN, SPI, 25000000)) {
        // Print a message if SD card initialization failed or if the SD card does not exist.
        M5.Display.print("\n SD card not detected\n");
        while (1); ;
    } else {
        M5.Display.print("\n SD card detected\n");
    }
    delay(1000);

    M5.Display.print("\n SD card read test...\n");
    if (SD.open("/LGFX_Canavs_Test01.bmp", FILE_READ, false)) {
        M5.Display.print(" BMP file 01 detected\n");
    } else {
        M5.Display.print(" BMP file 01 not detected\n");
    }
    if (SD.open("/LGFX_Canavs_Test02.bmp", FILE_READ, false)) {
        M5.Display.print(" BMP file 01 detected\n");
    } else {
        M5.Display.print(" BMP file 01 not detected\n");
    }
    delay(2000);
}

void loop() {
    M5Canvas canvas(&M5.Lcd);
    if (canvas.createFromBmp(SD, "/LGFX_Canavs_Test01.bmp")) {
        canvas.pushSprite(0, 0);
    } else {
        M5.Display.print("\ncreateFromBmp failed\n");
    }
    delay(1000);
    if (canvas.createFromBmpFile(SD, "/LGFX_Canavs_Test02.bmp")) {
        canvas.pushSprite(0, 0);
    } else {
        M5.Display.print("\ncreateFromBmpFile failed\n");
    }
    delay(1000);
    canvas.deleteSprite();
}
```

示例程序效果为两张图片交替显示，第一张图片为 `LGFX_Canavs_Test01.bmp`，第二张图片为 `LGFX_Canavs_Test02.bmp`。

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/658/Fire_M5GFX_bmp.mp4" type="video/mp4"></video>

### setBitmapColor

**函数原型:**

```cpp
void setBitmapColor(uint16_t fgcolor, uint16_t bgcolor)
```

**功能说明:**

- 设置位图颜色，仅适用于 1 位。

**传入参数:**

- fgcolor: 前景色
- bgcolor: 背景色

**返回值:**

- null

### setColorDepth

**函数原型1:**

```cpp
void setColorDepth(uint8_t bpp)
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

**函数原型2:**

```cpp
void* setColorDepth(color_depth_t depth)
```

**功能说明:**

- 设置颜色深度

**传入参数:**

- depth: 颜色深度

?>注意事项:| 1.如果使用调色板，`bpp`、`depth` 只能是 1、2、4 、8 位。  
2.在调用 `createPalette` 之前必须先调用 `setColorDepth` 设置颜色深度，否则会导致创建调色板失败。  
3.如果使用 `setColorDepth` 设置颜色深度为 1 位，则只能使用 `createPalette()` 创建调色板，不能使用 `createPalette(const uint16_t* colors, uint32_t count)` 或 `createPalette(const uint32_t* colors, uint32_t count)`。  

**返回值:**

- null

### createPalette

**函数原型1:**

```cpp
bool createPalette(void)
```

**函数原型2:**

```cpp
bool createPalette(const uint16_t* colors, uint32_t count)
```

**函数原型3:**

```cpp
bool createPalette(const uint32_t* colors, uint32_t count)
```

**功能说明:**

- 创建调色板

**传入参数:**

- colors: 颜色数组指针
- uint16_t: RGB565 16 位颜色
- uint32_t: RGB888/ARGB8888 24 位颜色/32 位颜色
- count: 颜色数量

**返回值:**

- bool
- true: 创建成功
- false: 创建失败

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

### setPaletteGrayscale

**函数原型:**

```cpp
void setPaletteGrayscale(void)
```

**功能说明:**

- 设置调色板为灰度

**传入参数:**

- null

**返回值:**

- null

### setPaletteColor

**函数原型1:**

```cpp
void setPaletteColor(uint32_t index, uint32_t color)
```

**功能说明:**

- 设置调色板颜色

**传入参数:**

- index: 调色板索引
- color: 颜色

**函数原型2:**

```cpp
void setPaletteColor(size_t index, const bgr888_t& rgb)
```

**功能说明:**

- 设置调色板颜色

**传入参数:**

- index: 调色板索引
- rgb: RGB 颜色

**函数原型3:**

```cpp
void setPaletteColor(size_t index, uint8_t r, uint8_t g, uint8_t b)
```

**功能说明:**

- 设置调色板颜色

**传入参数:**

- index: 调色板索引
- r: 红色分量
- g: 绿色分量
- b: 蓝色分量

**返回值:**

- null

### getPaletteIndex

**函数原型:**

```cpp
int32_t getPaletteIndex(const T& color)
```

**功能说明:**

- 获取调色板索引

**传入参数:**

- color: 颜色

**返回值:**

- res: 颜色索引
- -1: 函数执行失败

### deletePalette

**函数原型:**

```cpp
void deletePalette(void)
```

**功能说明:**

- 删除调色板

**传入参数:**

- null

**返回值:**

- null

**案例程序**

```cpp line-num
#include <M5Unified.h>
#include <M5GFX.h>

#define ROYAL_BLUE 0X435C
#define LAVENDER_PURPLE 0xE73F
#define SADDLE_BROWN 0x8A22
#define INDIA_RED 0xCAEB
#define FOREST_GREEN 0x2444
#define SALMON_PINK 0xFC0E

static int32_t Disw;
static int32_t Dish;
static uint16_t pale[] = {WHITE, ROYAL_BLUE, LAVENDER_PURPLE, SADDLE_BROWN, BLUE, INDIA_RED,FOREST_GREEN, SALMON_PINK};
// static uint16_t pale[256];

M5Canvas canvas(&M5.Lcd);

void setup() {
    M5.begin();

    Disw = M5.Lcd.width();
    Dish = M5.Lcd.height();

    canvas.createSprite(Disw, Dish);

    canvas.setColorDepth(lgfx::v1::palette_8bit);//This must be cited before createPalette
    canvas.setTextDatum(top_center);
    canvas.drawString("M5Canvas Palette", Disw / 2, 0, &fonts::FreeMonoBold24pt7b);
    canvas.drawString("Palette Color 0", Disw / 2, 100, &fonts::FreeMonoBold24pt7b);
    canvas.drawString("is background color", Disw / 2, 150, &fonts::FreeMonoBold24pt7b);

    canvas.createPalette(pale, 256);

    // If you choose "static uint16_t pale[256];", following code must be used

    // canvas.setPaletteColor(0, WHITE);
    // canvas.setPaletteColor(1, ROYAL_BLUE);
    // canvas.setPaletteColor(2, LAVENDER_PURPLE);
    // canvas.setPaletteColor(3, SADDLE_BROWN);
    // canvas.setPaletteColor(4, INDIA_RED);    
    // canvas.setPaletteColor(5, FOREST_GREEN);
    // canvas.setPaletteColor(6, SALMON_PINK);

    canvas.setTextColor(canvas.getPaletteIndex(ROYAL_BLUE));
    canvas.drawString("Palette Color 1", Disw / 2, 300, &fonts::FreeMonoBold24pt7b);
    canvas.setTextColor(canvas.getPaletteIndex(LAVENDER_PURPLE));
    canvas.drawString("Palette Color 2", Disw / 2, 350, &fonts::FreeMonoBold24pt7b);
    canvas.setTextColor(canvas.getPaletteIndex(SADDLE_BROWN));
    canvas.drawString("Palette Color 3", Disw / 2, 400, &fonts::FreeMonoBold24pt7b);
    canvas.setTextColor(canvas.getPaletteIndex(INDIA_RED));
    canvas.drawString("Palette Color 4", Disw / 2, 450, &fonts::FreeMonoBold24pt7b);
    canvas.setTextColor(canvas.getPaletteIndex(FOREST_GREEN));
    canvas.drawString("Palette Color 5", Disw / 2, 500, &fonts::FreeMonoBold24pt7b);
    canvas.setTextColor(canvas.getPaletteIndex(SALMON_PINK));
    canvas.drawString("Palette Color 6", Disw / 2, 550, &fonts::FreeMonoBold24pt7b);

    canvas.pushSprite(0,0);
    canvas.deletePalette();//must behind pushSprite()
    canvas.deleteSprite();
}

void loop() {
}   
```

例程效果如下：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/Tab5_M5GFX_Palette.jpg" width="40%">

### readPixelValue

**函数原型:**

```cpp
uint32_t readPixelValue(int32_t x, int32_t y)
```

**功能说明:**

- 读取指定坐标的像素值。

**传入参数:**

- x: 像素 x 坐标
- y: 像素 y 坐标

**返回值:**

- uint32_t: 像素值
- 0-1 (1 bpp)
- 0-255 (8 bpp)
- 0-0xFFFF (RGB565-16 bpp)
- 0-0xFFFFFF (RGB888-24 bpp)

<!-- **案例程序**

```cpp line-num
#include <M5GFX.h>
#include <M5Unified.h>

static int32_t Disw;
static int32_t Dish;

void setup() {
    M5.begin();
    Disw = M5.Lcd.width();
    Dish = M5.Lcd.height();

    M5.Lcd.fillScreen(TFT_WHITE);

    M5Canvas canvas(&M5.Lcd);
    canvas.createSprite(100, 100);//set sprite size
    canvas.fillSprite(TFT_BLACK);//fill sprite with color XXX
    canvas.print(canvas.readPixelValue(Disw / 2, Dish / 2));
    canvas.pushSprite(Disw / 2 - 50, Dish / 2 - 50);
    canvas.deleteSprite();
}

void loop() {
} 
``` -->

### setPsram

**函数原型:**

```cpp
void setPsram( bool enabled )
```

**功能说明:**

- 设置是否使用 PSRAM。

**传入参数:**

- enabled: 是否使用 PSRAM 标志
- true: 使用 PSRAM
- false: 不使用 PSRAM

**返回值:**

- null

### setBuffer

**函数原型:**

```cpp
void setBuffer(void* buffer, int32_t w, int32_t h, uint8_t bpp = 0)
```

**功能说明:**

- 设置缓冲区

**传入参数:**

- buffer: 缓冲区指针
- w: 宽度
- h: 高度
- bpp: 每个像素的位数（默认为 0）
  - 0: 使用默认值
  - 1: 1 位
  - 2: 2 位
  - 4: 4 位
  - 8: 8 位
  - 16: 16 位
  - 24: 24 位
  - 32: 32 位

**返回值:**

- null

### pushRotated

**函数原型1:**

```cpp
void pushRotated(float angle, const T& transp)
```

**函数原型2:**

```cpp
void pushRotated(LovyanGFX* dst, float angle, const T& transp)
```

**函数原型3:**

```cpp
void pushRotated(float angle)
```

**函数原型4:**

```cpp
void pushRotated(LovyanGFX* dst, float angle)
```

**功能说明:**

- 以指定角度旋转画布

**传入参数:**

- dst: 目标 LovyanGFX 对象
- angle: 旋转角度
- transp: 透明颜色

**返回值:**

- null

### pushRotatedWithAA

**函数原型1:**

```cpp
void pushRotatedWithAA(float angle, const T& transp)
```

**函数原型2:**

```cpp
void pushRotatedWithAA(LovyanGFX* dst, float angle, const T& transp)
```

**函数原型3:**

```cpp
void pushRotatedWithAA(float angle)
```

**函数原型4:**

```cpp
void pushRotatedWithAA(LovyanGFX* dst, float angle)
```

**功能说明:**

- 以指定角度旋转画布，并使用抗锯齿

**传入参数:**

- dst: 目标 LovyanGFX 对象
- angle: 旋转角度
- transp: 透明颜色

**返回值:**

- null

### pushRotateZoom

**函数原型1:**

```cpp
void pushRotateZoom(float angle, float zoom_x, float zoom_y, const T& transp)
```

**函数原型2:**

```cpp
void pushRotateZoom(LovyanGFX* dst, float angle, float zoom_x, float zoom_y, const T& transp)
```

**函数原型3:**

```cpp
void pushRotateZoom(float dst_x, float dst_y, float angle, float zoom_x, float zoom_y, const T& transp)
```

**函数原型4:**

```cpp
void pushRotateZoom(LovyanGFX* dst, float dst_x, float dst_y, float angle, float zoom_x, float zoom_y, const T& transp)
```

**函数原型5:**

```cpp
void pushRotateZoom(float angle, float zoom_x, float zoom_y)
```

**函数原型6:**

```cpp
void pushRotateZoom(LovyanGFX* dst, float angle, float zoom_x, float zoom_y)
```

**函数原型7:**

```cpp
void pushRotateZoom(float dst_x, float dst_y, float angle, float zoom_x, float zoom_y)
``` 

**函数原型8:**

```cpp
void pushRotateZoom(LovyanGFX* dst, float dst_x, float dst_y, float angle, float zoom_x, float zoom_y)
```

**功能说明:**

- 以指定角度和缩放比例旋转画布

**传入参数:**

- dst: 目标 LovyanGFX 对象
- dst_x: 目标 x 坐标
- dst_y: 目标 y 坐标
- angle: 旋转角度
- zoom_x: x 轴缩放比例
- zoom_y: y 轴缩放比例
- transp: 透明颜色

**返回值:**

- null

### pushRotateZoomWithAA

**函数原型1:**

```cpp
void pushRotateZoomWithAA(float angle, float zoom_x, float zoom_y, const T& transp)
```

**函数原型2:**

```cpp
void pushRotateZoomWithAA(LovyanGFX* dst , float angle, float zoom_x, float zoom_y, const T& transp)
```

**函数原型3:**

```cpp
void pushRotateZoomWithAA(float dst_x, float dst_y, float angle, float zoom_x, float zoom_y, const T& transp)
```

**函数原型4:**

```cpp
void pushRotateZoomWithAA(LovyanGFX* dst, float dst_x, float dst_y, float angle, float zoom_x, float zoom_y, const T& transp)
```

**函数原型5:**

```cpp
void pushRotateZoomWithAA(float angle, float zoom_x, float zoom_y)
```

**函数原型6:**

```cpp
void pushRotateZoomWithAA(LovyanGFX* dst, float angle, float zoom_x, float zoom_y)
```

**函数原型7:**

```cpp
void pushRotateZoomWithAA(float dst_x, float dst_y, float angle, float zoom_x, float zoom_y)
```

**函数原型8:**

```cpp
void pushRotateZoomWithAA(LovyanGFX* dst, float dst_x, float dst_y, float angle, float zoom_x, float zoom_y)
```

**功能说明:**

- 以指定角度和缩放比例旋转画布，并使用抗锯齿

**传入参数:**

- dst: 目标 LovyanGFX 对象
- dst_x: 目标 x 坐标
- dst_y: 目标 y 坐标
- angle: 旋转角度
- zoom_x: x 轴缩放比例
- zoom_y: y 轴缩放比例
- transp: 透明颜色

**返回值:**

- null

### pushAffine

**函数原型1:**

```cpp
void pushAffine(const float matrix[6], const T& transp)
```

**函数原型2:**

```cpp
void pushAffine(LovyanGFX* dst, const float matrix[6], const T& transp)
```

**函数原型3:**

```cpp
void pushAffine(const float matrix[6])
```

**函数原型4:**

```cpp
void pushAffine(LovyanGFX* dst, const float matrix[6])
```

**功能说明:**

- 以指定矩阵进行仿射变换

**传入参数:**

- dst: 目标 LovyanGFX 对象
- matrix: 变换矩阵
- [a, c, e]
- [b, d, f]
- [0, 0, 1]
- transp: 透明颜色

**返回值:**

- null

### pushAffineWithAA

**函数原型1:**

```cpp
void pushAffineWithAA(const float matrix[6], const T& transp)
```

**函数原型2:**

```cpp
void pushAffineWithAA(LovyanGFX* dst, const float matrix[6], const T& transp)
```

**函数原型3:**

```cpp
void pushAffineWithAA(const float matrix[6])
```

**函数原型4:**

```cpp
void pushAffineWithAA(LovyanGFX* dst, const float matrix[6])
```

**功能说明:**

- 以指定矩阵进行仿射变换，并使用抗锯齿

**传入参数:**

- dst: 目标 LovyanGFX 对象
- matrix: 变换矩阵
- [a, c, e]
- [b, d, f]
- [0, 0, 1]
- transp: 透明颜色

**返回值:**

- null

**案例程序**

```cpp line-num
#include <M5GFX.h>
#include <M5Unified.h>

static int32_t Disw;
static int32_t Dish;
static float Affine_mat[9] = {1, 0, 60,
                              0, 1, 20,
                              0, 0, 1  };

void setup() {
    M5.begin();
    Disw = M5.Lcd.width();
    Dish = M5.Lcd.height();

    M5.Lcd.fillScreen(TFT_WHITE);

    M5Canvas canvas(&M5.Lcd);
    canvas.createSprite(100, 100);//set sprite size
    canvas.fillSprite(TFT_BLACK);//fill sprite with color XXX
    canvas.pushSprite(Disw / 2 - 50, Dish / 2 - 50);
    delay(1000);
    canvas.fillSprite(TFT_PINK);

    // Rotate 45°
    canvas.pushRotated(45);
    // canvas.pushRotatedWithAA(45);

    // Rotate 90° Reduce to 80%
    // canvas.pushRotateZoom(90, 0.8, 0.8);
    // canvas.pushRotateZoomWithAA(90, 0.8, 0.8);

    // Shift 10 units from the origin using the affine matrix
    // canvas.pushAffine(Affine_mat);
    // canvas.pushAffineWithAA(Affine_mat);

    canvas.deleteSprite();
}

void loop() {
} 
```

例程效果如下：

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/658/Fire_M5GFX_push.mp4" type="video/mp4"></video>



