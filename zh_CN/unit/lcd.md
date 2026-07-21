# Unit LCD

<span class="product-sku">SKU:U120</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/lcd/lcd_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/lcd/lcd_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/lcd/lcd_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/lcd/lcd_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/lcd/lcd_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/lcd/lcd_06.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/lcd/lcd_07.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/lcd/lcd_08.webp">
</PictureViewer>

## 描述

**Unit LCD** 是一款 1.14 英寸的彩色 LCD 拓展屏幕单元。采用 ST7789V2 驱动方案，分辨率为 135 x 240，支持 RGB666 显示 (262,144 色)。内部集成 ESP32-PICO 控制核心 (内置固件，显示开发更加便捷)，支持通过 I2C (addr: 0x3E) 通信接口进行控制与固件升级。屏幕背部集成了磁吸设计，能够轻松吸附金属表面进行固定。该 LCD 屏幕拓展适合嵌入到各种需要显示简单内容的仪器仪表或是控制设备中作为显示面板。

## 产品特性

- 1.14 inch 彩色 LCD 显示面板
- I2C 通信接口
- 可视角：全视角
- 背部磁吸设计
- 支持 I2C 固件升级

## 包装内容

- 1 x Unit LCD
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 信息显示屏

## 规格参数

| 规格        | 参数                       |
| ----------- | -------------------------- |
| 屏幕驱动 IC | ST7789V2                   |
| 工作电流    | 45.7mA                     |
| 通信接口    | I2C 通信 @ 0x3E            |
| 显示尺寸    | 1.14 inch                  |
| 像素间距    | 0.1101 (H) x 0.1038 (V) mm |
| 分辨率      | 135 x 240                  |
| 可视角      | 全视角                     |
| 工作温度    | 0 ~ 60°C                   |
| 外壳材质    | Plastic (PC)               |
| 产品尺寸    | 48.0 x 24.0 x 8.0mm        |
| 产品重量    | 8.6g                       |
| 包装尺寸    | 68.0 x 57.0 x 17.0mm       |
| 毛重        | 21.3g                      |

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/lcd/lcd_sch_01.webp" width="80%">

## 管脚映射

### Unit LCD

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 尺寸图

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/lcd/%E5%B0%BA%E5%AF%B8%E5%9B%BE.jpg" width="80%">

## 数据手册

- [ST7789V2](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/lcd/ST7789V2_SPEC_V1.0.pdf)

## 软件开发

### Arduino

- [M5GFX Arduino 驱动库](https://github.com/m5stack/M5GFX)

```cpp
#include <M5UnitLCD.h>

M5UnitLCD display;

M5Canvas canvas(&display);

static constexpr char text[] = "Hello world ! こんにちは世界！ this is long long string sample. 寿限無、寿限無、五劫の擦り切れ、海砂利水魚の、水行末・雲来末・風来末、喰う寝る処に住む処、藪ら柑子の藪柑子、パイポ・パイポ・パイポのシューリンガン、シューリンガンのグーリンダイ、グーリンダイのポンポコピーのポンポコナの、長久命の長助";
static constexpr size_t textlen = sizeof(text) / sizeof(text[0]);
int textpos = 0;
int scrollstep = 2;

void setup(void)
{
  display.init();
  display.setRotation(2);
  canvas.setColorDepth(1); // mono color
  canvas.setFont(&fonts::lgfxJapanMinchoP_32);
  canvas.setTextWrap(false);
  canvas.setTextSize(2);
  canvas.createSprite(display.width() + 64, 72);
}

void loop(void)
{
  int32_t cursor_x = canvas.getCursorX()-scrollstep;
  if (cursor_x <= 0)
  {
    textpos = 0;
    cursor_x = display.width();
  }

  canvas.setCursor(cursor_x, 0);
  canvas.scroll(-scrollstep, 0);
  while (textpos < textlen && cursor_x <= display.width())
  {
    canvas.print(text[textpos++]);
    cursor_x = canvas.getCursorX();
  }
  display.waitDisplay();
  canvas.pushSprite(&display, 0, (display.height()-canvas.height()) >> 1);
}

```

### 内置固件

- [Unit LCD 内置固件](https://github.com/m5stack/M5UnitLCD_FirmWare)

### 通信协议

#### 关于 Unit LCD

- Unit LCD 是带有 ESP32 和 ST7789V2 的 I2C 单元。
- 它有一个分辨率为 135 x 240 的 IPS 面板。
- 可显示的颜色数为 RGB666 的 262，144 色，这是 ST7789V2 的规格。
- ESP32 负责 I2C 通信，并根据接收到的内容在内存中绘制帧缓冲区。
- ESP32 内存中帧缓冲区的内容通过 SPI 通信的 DMA 传输反映在 ST7789V2 中。
- 它由帧缓冲区上的 RGB888 16，777，216 色表示。

#### 关于 I2C 通信

- 您可以使用 I2C 通信向单元 LCD 发送命令和接收数据。
- I2C 通信的最大通信速度为 400kHz。
- I2C 的 7 位地址的初始值为 0x3E。可以使用 CHANGE_ADDR 命令更改它。
- 发送所需的字节数取决于命令。有些命令在 1 字节内完成，而其他命令需要 7 字节。还有不定长度的命令直到通信停止才会结束。
- 如果在命令传输过程中发生 I2C 通信 STOP 或 RESTART，则不会处理中断的命令。必须在单个传输序列中不间断地传输到最后。
- 发送一个定长命令后，可以连续发送另一个命令。
- 发送不确定长度的命令后，必须停止 I2C 通信以指示命令结束。
- 如果发送 NOP 命令或未定义的命令，通信内容将被忽略，直到 I2C 通信停止。
- 由于 I2C 通信单元和绘图处理单元并行运行，因此即使在绘图处理期间也可以执行 I2C 通信。
- I2C 通信内容存储在 ESP32 内存的命令缓冲区中，绘图处理单元依次处理。
- 您应该使用 READ_BUFCOUNT 命令来检查缓冲区的剩余量，因为发送大量繁重的处理，例如广泛的填充或范围复制，可能会溢出缓冲区。

#### 关于绘图

- 您可以通过使用 FILLRECT 用单一颜色填充任何区域来绘制矩形。
- 如果只想绘制一个像素，可以使用 DRAWPIXEL 而不是 FILLRECT。
- 如果您使用省略前景色的命令，则使用最后使用的颜色。
- 您可以使用 CASET 和 RASET 指定绘图范围，并使用 WRITE_RAW 命令发送图像数据。
- 您可以使用 WRITE_RLE 而不是 WRITE_RAW 来发送运行长度压缩的图像数据。

#### 命令列表

※ 未定义的命令被视为空操作指令。

| hex  | len | command      | description                                                                            | send params                                                                                                                                                                                  |
| :--: | :-: | :----------- | :------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x00 | 1-∞ | NOP          | 在通信停止之前什么都不做                                                               | \[0] 0x00<br/>\[1-∞] Ignored value                                                                                                                                                           |
| 0x20 | 1   | INVOFF       | 禁用颜色反转                                                                           | \[0] 0x20                                                                                                                                                                                    |
| 0x21 | 1   | INVON        | 启用颜色反转                                                                           | \[0] 0x21                                                                                                                                                                                    |
| 0x22 | 2   | BRIGHTNESS   | 背光亮度设置<br/>0:Off-255:Full lights                                                 | \[0] 0x22<br/>\[1] Brightness (0-255)                                                                                                                                                        |
| 0x23 | 7   | COPYRECT     | 矩形范围复制                                                                           | \[0] 0x23<br/>\[1] Copy source X_Left<br/>\[2] Copy source Y_Top<br/>\[3] Copy source X_Right<br/>\[4] Copy source Y_Bottom<br/>\[5] Copy destination X_Left<br/>\[6] Copy destination Y_Top |
| 0x2A | 3   | CASET        | X 方向范围选择                                                                         | \[0] 0x2A<br/>\[1] X_Left<br/>\[2] X_Right                                                                                                                                                   |
| 0x2B | 3   | RASET        | Y 方向范围选择                                                                         | \[0] 0x2B<br/>\[1] Y_Top<br/>\[2] Y_Bottom                                                                                                                                                   |
| 0x36 | 2   | ROTATE       | 设置绘图方向<br/>0:Normal / 1:90° / 2:180° / 3:270°<br/>4-7:flips 0-3 upside down      | \[0] 0x36<br/>\[1] Setting value (0-7)                                                                                                                                                       |
| 0x38 | 2   | SET_POWER    | 运行速度设置<br/>(power consumption setting)<br/>0:Low speed / 1:Normal / 2:High speed | \[0] 0x38<br/>\[1] Setting value (0-2)                                                                                                                                                       |
| 0x39 | 2   | SET_SLEEP    | 液晶面板休眠设置<br/>0:wake up / 1:sleep                                               | \[0] 0x39<br/>\[1] Setting value (0-1)                                                                                                                                                       |
| 0x41 | 2-∞ | WRITE_RAW_8  | 写入 image RGB332                                                                      | \[0] 0x41<br/>\[1] RGB332<br/>until \[1] communication STOP.                                                                                                                                 |
| 0x42 | 3-∞ | WRITE_RAW_16 | 写入 image RGB565                                                                      | \[0] 0x42<br/>\[1-2] RGB565<br/>until \[1-2] communication STOP.                                                                                                                             |
| 0x43 | 4-∞ | WRITE_RAW_24 | 写入 image RGB888                                                                      | \[0] 0x43<br/>\[1-3] RGB888<br/>until \[1-3] communication STOP.                                                                                                                             |
| 0x44 | 5-∞ | WRITE_RAW_32 | 写入 image ARGB8888                                                                    | \[0] 0x44<br/>\[1-4] ARGB8888<br/>until \[1-4] communication STOP.                                                                                                                           |
| 0x45 | 2-∞ | WRITE_RAW_A  | 写入 image A8<br/>only alpha channel.<br/>Use the last used drawing color.             | \[0] 0x45<br/>\[1] A8<br/>until \[1] communication STOP.                                                                                                                                     |
| 0x49 | 3-∞ | WRITE_RLE_8  | 写入 RLE image RGB332                                                                  | \[0] 0x49<br/>\[1-∞] RLE Data                                                                                                                                                                |
| 0x4A | 4-∞ | WRITE_RLE_16 | 写入 RLE image RGB565                                                                  | \[0] 0x4A<br/>\[1-∞] RLE Data                                                                                                                                                                |
| 0x4B | 5-∞ | WRITE_RLE_24 | 写入 RLE image RGB888                                                                  | \[0] 0x4B<br/>\[1-∞] RLE Data                                                                                                                                                                |
| 0x4C | 6-∞ | WRITE_RLE_32 | 写入 RLE image ARGB8888                                                                | \[0] 0x4C<br/>\[1-∞] RLE Data                                                                                                                                                                |
| 0x4D | 3-∞ | WRITE_RLE_A  | draw RLE image A8<br/>only alpha channel.<br/>Use the last used drawing color.         | \[0] 0x4D<br/>\[1-∞] RLE Data                                                                                                                                                                |
| 0x50 | 1   | RAM_FILL     | 用上次使用的绘图颜色填充选区                                                           | \[0] 0x50                                                                                                                                                                                    |
| 0x51 | 2   | SET_COLOR_8  | 用 RGB332 指定绘图颜色                                                                 | \[0] 0x51<br/>\[1] RGB332                                                                                                                                                                    |
| 0x52 | 3   | SET_COLOR_16 | 用 RGB565 指定绘图颜色                                                                 | \[0] 0x52<br/>\[1-2] RGB565                                                                                                                                                                  |
| 0x53 | 4   | SET_COLOR_24 | 用 RGB888 指定绘图颜色                                                                 | \[0] 0x53<br/>\[1-3] RGB888                                                                                                                                                                  |
| 0x54 | 5   | SET_COLOR_32 | 用 ARGB8888 指定绘图颜色                                                               | \[0] 0x54<br/>\[1-4] ARGB8888                                                                                                                                                                |
| 0x60 | 3   | DRAWPIXEL    | 绘制单点<br/>使用存储的绘制颜色                                                        | \[0] 0x60<br/>\[1] X<br/>\[2] Y<br/>                                                                                                                                                         |
| 0x61 | 4   | DRAWPIXEL_8  | 绘制单点<br/>RGB332 1Byte 用于绘制颜色规范                                             | \[0] 0x61<br/>\[1] X<br/>\[2] Y<br/>\[3] RGB332                                                                                                                                              |
| 0x62 | 5   | DRAWPIXEL_16 | 绘制单点<br/>RGB565 2Byte 用于绘制颜色规范                                             | \[0] 0x62<br/>\[1] X<br/>\[2] Y<br/>\[3-4] RGB565                                                                                                                                            |
| 0x63 | 6   | DRAWPIXEL_24 | 绘制单点<br/>RGB888 3Byte 用于绘制颜色规范                                             | \[0] 0x63<br/>\[1] X<br/>\[2] Y<br/>\[3-5] RGB888                                                                                                                                            |
| 0x64 | 7   | DRAWPIXEL_32 | 绘制单点<br/>ARGB8888 4Byte 用于绘制颜色规范<br/>与现有绘制内容透明合成                | \[0] 0x64<br/>\[1] X<br/>\[2] Y<br/>\[3-6] ARGB8888                                                                                                                                          |
| 0x68 | 5   | FILLRECT     | 填充矩形<br/>使用存储的绘图颜色                                                        | \[0] 0x68<br/>\[1] X_Left<br/>\[2] Y_Top<br/>\[3] X_Right<br/>\[4] Y_Bottom                                                                                                                  |
| 0x69 | 6   | FILLRECT_8   | 填充矩形<br/>RGB332 1Byte 用于绘制颜色规范                                             | \[0] 0x69<br/>\[1] X_Left<br/>\[2] Y_Top<br/>\[3] X_Right<br/>\[4] Y_Bottom<br/>\[5] RGB332                                                                                                  |
| 0x6A | 7   | FILLRECT_16  | 填充矩形<br/>RGB565 2Byte 用于绘制颜色规范                                             | \[0] 0x6A<br/>\[1] X_Left<br/>\[2] Y_Top<br/>\[3] X_Right<br/>\[4] Y_Bottom<br/>\[5-6] RGB565                                                                                                |
| 0x6B | 8   | FILLRECT_24  | 填充矩形<br/>RGB888 3Byte 用于绘制颜色规范                                             | \[0] 0x6B<br/>\[1] X_Left<br/>\[2] Y_Top<br/>\[3] X_Right<br/>\[4] Y_Bottom<br/>\[5-7] RGB888                                                                                                |
| 0x6C | 9   | FILLRECT_32  | 填充矩形<br/>ARGB8888 4Byte 用于绘制颜色规范<br/>与现有绘制内容透明合成                | \[0] 0x6C<br/>\[1] X_Left<br/>\[2] Y_Top<br/>\[3] X_Right<br/>\[4] Y_Bottom<br/>\[5-8] ARGB8888                                                                                              |
| 0xA0 | 4   | CHANGE_ADDR  | I2C 地址更改<br/>使用时 \[2] 指定 \[1] 的位反转值。                                    | \[0] 0xA0<br/>\[1] new I2C address.<br/>\[2] Bit \[1] 反转<br/>\[3] 0xA0                                                                                                                     |

#### 命令列表 (可读命令)

| hex  | len | command       | description                                                      | return values                                                              |
| :--: | :-: | :------------ | :--------------------------------------------------------------- | :------------------------------------------------------------------------- |
| 0x04 | 1   | READ_ID       | ID 和固件版本。<br/>收到 4Byte                                   | \[0] 0x77<br/>\[1] 0x89<br/>\[2] Major version<br/>\[3] Minor version      |
| 0x09 | 1   | READ_BUFCOUNT | 获取剩余的命令缓冲区。<br/>值越大，空间越大。<br/>可以连续读出。 | \[0] remaining command buffer (0~255) <br/>Repeated reception is possible. |
| 0x81 | 1   | READ_RAW_8    | 读取 RGB332 image                                                | \[0] RGB332<br/>Repeat \[0] until communication STOP.                      |
| 0x82 | 1   | READ_RAW_16   | 读取 RGB565 image                                                | \[0-1] RGB565<br/>Repeat \[0-1] until communication STOP.                  |
| 0x83 | 1   | READ_RAW_24   | 读取 RGB888 image                                                | \[0-2] RGB888<br/>Repeat \[0-2] until communication STOP.                  |

#### 通信示例

> 使用示例：使用填充矩形命令 0x6A 用红色填充 X16-31 和 Y32-47 的矩形范围。

| index | hex  | description              |
| :---: | :--: | :----------------------- |
| 0     | 0x6A | 填充矩形 RGB565          |
| 1     | 0x10 | X 左                     |
| 2     | 0x20 | Y 顶部                   |
| 3     | 0x1F | X 右                     |
| 4     | 0x2F | Y 底部                   |
| 5     | 0xF8 | 颜色数据 RRRRRGGG (红色) |
| 6     | 0x00 | 颜色数据 GGGBBBBB (红色) |

命令 6Ah 一共是 7Byte 命令序列。
如果在传输过程中发生 I2C 通信 STOP 或 RESTART，则不会处理该命令。
必须在单个传输序列中不间断地传输直到结束。

任何矩形填充命令 68h 到 6Ch 均可用于矩形填充。
索引 1 到 4 是相同的，但索引 5 和以后的索引指定颜色的方法不同。

命令 68h 的 “记住颜色” 表示将重用最后指定的颜色。
换句话说，如果你想连续做几个相同颜色的矩形填充，你可以只为第一个矩形填充指定颜色，然后使用 68h 命令省略颜色指定。

命令 6Ch，ARGB8888，允许您指定 alpha 通道 (透明度)，它允许您将已绘制的内容与绘制颜色组合。

---

> 使用示例：使用范围指定命令 0x2A/0x2B 和图像传输命令，在 X 10 到 13 和 Y 14 到 17 的矩形范围内绘制图像。

| index | hex  | description           |
| :---: | :--: | :-------------------- |
| 0     | 0x2A | X 方向范围选择        |
| 1     | 0x0A | X 左 (10)             |
| 2     | 0x0D | X 右 (13)             |
| 3     | 0x2B | Y 方向范围选择        |
| 4     | 0x0E | Y 顶部 (14)           |
| 5     | 0x11 | Y 底部 (17)           |
| 6     | 0x43 | 绘制图像 RGB888       |
| 7-54  | ??   | 图像数据 (RGB888 ×16) |

---

> 使用示例：使用 WRITE_RLE 命令发送 RLE (运行长度编码) 图像。

- RLE 规范基于 BMP 文件的 RLE。
- 与用于 BMP 文件的 RLE 不同，它可以用于 RGB565 和 RGB888。
- 它首先发送相同颜色 (0-255) 的连续像素数，然后是颜色数据。
- 如果 0 被发送到一个连续的号码，它将在不使用 RLE 的情况下处于直接模式。
- 在直接模式下，首先发送像素数 (1-255)，然后是像素数的颜色数据。

| index | hex    | description                          |
| :---: | -----: | :----------------------------------- |
| 0     | 0x4A   | 绘制 RLE 图像 RGB565                 |
| 1     | 0x07   | 连续数 (7 个像素)                    |
| 2-3   | 0xF800 | 颜色数据 (红色)                      |
| 4     | 0x00   | 连续数字 (0 像素)<br/>切换到直接模式 |
| 5     | 0x03   | 直接模式的连续数量 (3pixel)          |
| 6-7   | 0x07E0 | 颜色数据 (绿色)                      |
| 8-9   | 0x001F | 颜色数据 (蓝色)                      |
| 10-11 | 0xF800 | 颜色数据 (红色)                      |
| 12    | 0x04   | 连续数 (4 个像素)                    |
| 13-14 | 0x001F | 颜色数据 (蓝色)                      |

上面的例子将按如下方式处理。

- index1-3 : 在 RLE 模式下绘制 7 个红色像素。
- index4-5 : 切换到直接模式并指示它绘制 3 个像素。
- index6-11: 在直接模式下发送 3 个像素的颜色并绘制绿色、蓝色和红色。
- 由于 3 个像素的直接模式由 index11 完成，我们将从 index12 返回到 RLE 模式。
- index12-14 : 在 RLE 模式下绘制 4 个蓝色像素。

#### 固件升级

- 方式 1. 使用 ESP32-Downloader 下载固件进行更新

\#>[前往资源页面下载M5Burner](/zh_CN/download)，拆开 Unit LCD 外壳，通过[USB Downloader](https://shop.m5stack.com/products/usb-ttl-uart-serial-adapter)为其更新程序。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/753/lcd_fw_01.png" width="60%">

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/lcd/lcd_fw_02.webp" width="30%"><img src="https://static-cdn.m5stack.com/resource/docs/products/unit/lcd/lcd_fw_03.webp" width="30%">

- 方式 2. 通过 I2C 通信进行更新

\#> 编译上方[Github源码](https://github.com/m5stack/M5UnitLCD_FirmWare/blob/master/examples/FirmwareUpdater/FirmwareUpdater.ino)或是[前往资源页面下载M5Burner](/zh_CN/download)，烧录**UNIT_LCD_FW**固件至 M5Core1/Core2/M5StickC/CPlus/ATOM/Paper 任意一款主控中。将 Unit LCD 通过导线连接至 I2C 端口将会自动开始更新。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/753/lcd_fw_01.png" width="80%">

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/lcd/lcd_fw_05.webp" width="16%"><img src="https://static-cdn.m5stack.com/resource/docs/products/unit/lcd/lcd_fw_06.webp" width="50%">

## UiFlow1

- [Unit LCD UiFlow1 文档](/zh_CN/uiflow/blockly/unit/lcd)

## UiFlow2

- [Unit LCD UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/lcd.html)

## 相关视频

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Unit/UNIT_LCD_VIDEO.mp4" type="video/mp4">
</video>

- UiFlow2 Unit LCD

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113026929789562&bvid=BV1TEsLeVEnH&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
      <iframe width="560" height="315" src="https://www.youtube.com/embed/W5-wh-VZUcI?si=z7e4Rm3mhrzT6Tv1" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
