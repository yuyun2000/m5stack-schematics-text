# M5GFX 库相关数据定义

## 颜色编码

M5GFX 会通过使用的颜色数据类型，自动检测RGB888，RGB565，RGB332。

### 编码类型

| 类型     | 颜色   |
| -------- | ------ |
| uint8_t  | RGB332 |
| uint16_t | RGB565 |
| uint32_t | RGB888 |

### 常用颜色列表

| 颜色            | 十六进制值(Hex) | 红(R) | 绿(G) | 蓝(B) |
| --------------- | --------------- | ----- | ----- | ----- |
| TFT_BLACK       | 0x0000          | 0     | 0     | 0     |
| TFT_NAVY        | 0x000F          | 0     | 0     | 128   |
| TFT_DARKGREEN   | 0x03E0          | 0     | 128   | 0     |
| TFT_DARKCYAN    | 0x03EF          | 0     | 128   | 128   |
| TFT_MAROON      | 0x7800          | 128   | 0     | 0     |
| TFT_PURPLE      | 0x780F          | 128   | 0     | 128   |
| TFT_OLIVE       | 0x7BE0          | 128   | 128   | 0     |
| TFT_LIGHTGREY   | 0xD69A          | 211   | 211   | 211   |
| TFT_LIGHTGRAY   | 0xD69A          | 211   | 211   | 211   |
| TFT_DARKGREY    | 0x7BEF          | 128   | 128   | 128   |
| TFT_DARKGRAY    | 0x7BEF          | 128   | 128   | 128   |
| TFT_BLUE        | 0x001F          | 0     | 0     | 255   |
| TFT_GREEN       | 0x07E0          | 0     | 255   | 0     |
| TFT_CYAN        | 0x07FF          | 0     | 255   | 255   |
| TFT_RED         | 0xF800          | 255   | 0     | 0     |
| TFT_MAGENTA     | 0xF81F          | 255   | 0     | 255   |
| TFT_YELLOW      | 0xFFE0          | 255   | 255   | 0     |
| TFT_WHITE       | 0xFFFF          | 255   | 255   | 255   |
| TFT_ORANGE      | 0xFDA0          | 255   | 180   | 0     |
| TFT_GREENYELLOW | 0xB7E0          | 180   | 255   | 0     |
| TFT_PINK        | 0xFE19          | 255   | 192   | 203   |
| TFT_BROWN       | 0x9A60          | 150   | 75    | 0     |
| TFT_GOLD        | 0xFEA0          | 255   | 215   | 0     |
| TFT_SILVER      | 0xC618          | 192   | 192   | 192   |
| TFT_SKYBLUE     | 0x867D          | 135   | 206   | 235   |
| TFT_VIOLET      | 0x915C          | 180   | 46    | 226   |
| TFT_TRANSPARENT | 0x0120          |       |       |       |

## 颜色深度

| 值  | 比特   | 颜色数量   |
| --- | ------ | ---------- |
| 1   | 1 bit  | 2          |
| 2   | 2 bit  | 4          |
| 4   | 4 bit  | 16         |
| 8   | 8 bit  | 256        |
| 16  | 16 bit | 65,536     |
| 24  | 24 bit | 16,777,216 |
 
## enum epd_mode_t
 
| 类型        | 描述                     |
| ----------- | ------------------------ |
| epd_quality | 精细渲染,速度较慢        |
| epd_text    | ↑                        |
| epd_fast    | ↓                        |
| epd_fastest | 渲染速度更快，但质量较差 |

## enum textdatum_t

指定显示文本的基准坐标

| 左对齐        | 居中对齐        | 右对齐         |
| ------------- | --------------- | -------------- |
| top_left      | top_center      | top_right      |
| middle_left   | middle_center   | middle_right   |
| bottom_left   | bottom_center   | bottom_right   |
| baseline_left | baseline_center | baseline_right |

## struct TextStyle

| 参数        | 类型        | 描述       |
| ----------- | ----------- | ---------- |
| fore_rgb888 | uint32_t    | 字体颜色   |
| back_rgb888 | uint32_t    | 背景颜色   |
| size_x      | float       | 文本x坐标  |
| size_y      | float       | 文本y坐标  |
| datum       | textdatum_t | 文本基准   |
| padding_x   | int32_t     | 填充 X     |
| utf8        | bool        | UTF8  编码 |
| cp437       | bool        | cp437 编码 |

## struct touch_point_t

| 参数 | 类型     | 描述   |
| ---- | -------- | ------ |
| x    | int16_t  | X 坐标 |
| y    | int16_t  | Y 坐标 |
| size | uint16_t | 点大小 |
| id   | uint8_t  | 点 ID  |

## draw/push 和 write 函数之间的不同

与 draw/push 函数不同，write 函数没有通过 [startWrite](./m5gfx_graph#startwrite), [endWrite](./m5gfx_graph#endwrite) 定义。draw/push 等函数在其内部自动执行 startWrite 和 endWrite，这使得在连续进行多次绘图时，处理速度稍慢。在这种情况下，可以通过在 startWrite 和 endWrite 之间一起执行所有的 draw/push 等函数来提高速度。

### draw/push 和 write functions 表

| write(read)    | draw or push (etc) |
| -------------- | ------------------ |
| writePixel     | drawPixel          |
| writePixels    | pushPixels         |
| writePixelsDMA | pushPixelsDMA      |
| writeFastHLine | drawFastHLine      |
| writeFastVLine | drawFastVLine      |
| writeFillRect  | fillRect           |
| writeColor     |                    |
| pushBlock      |                    |

#> 说明：| `pushBlock` 因考虑库版本兼容性，未以 writeBlock 命名。

## 字体列表

### Latin 字体

- EN

```cpp line-num
&fonts::Font0
&fonts::Font2
&fonts::Font4
&fonts::Font6
&fonts::Font7
&fonts::Font8
&fonts::Font8x8C64
&fonts::AsciiFont8x16
&fonts::AsciiFont24x48
&fonts::TomThumb
&fonts::FreeMono9pt7b
&fonts::FreeMono12pt7b
&fonts::FreeMono18pt7b
&fonts::FreeMono24pt7b
&fonts::FreeMonoBold9pt7b
&fonts::FreeMonoBold12pt7b
&fonts::FreeMonoBold18pt7b
&fonts::FreeMonoBold24pt7b
&fonts::FreeMonoOblique9pt7b
&fonts::FreeMonoOblique12pt7b
&fonts::FreeMonoOblique18pt7b
&fonts::FreeMonoOblique24pt7b
&fonts::FreeMonoBoldOblique9pt7b
&fonts::FreeMonoBoldOblique12pt7b
&fonts::FreeMonoBoldOblique18pt7b
&fonts::FreeMonoBoldOblique24pt7b
&fonts::FreeSans9pt7b
&fonts::FreeSans12pt7b
&fonts::FreeSans18pt7b
&fonts::FreeSans24pt7b
&fonts::FreeSansBold9pt7b
&fonts::FreeSansBold12pt7b
&fonts::FreeSansBold18pt7b
&fonts::FreeSansBold24pt7b
&fonts::FreeSansOblique9pt7b
&fonts::FreeSansOblique12pt7b
&fonts::FreeSansOblique18pt7b
&fonts::FreeSansOblique24pt7b
&fonts::FreeSansBoldOblique9pt7b
&fonts::FreeSansBoldOblique12pt7b
&fonts::FreeSansBoldOblique18pt7b
&fonts::FreeSansBoldOblique24pt7b
&fonts::FreeSerif9pt7b
&fonts::FreeSerif12pt7b
&fonts::FreeSerif18pt7b
&fonts::FreeSerif24pt7b
&fonts::FreeSerifItalic9pt7b
&fonts::FreeSerifItalic12pt7b
&fonts::FreeSerifItalic18pt7b
&fonts::FreeSerifItalic24pt7b
&fonts::FreeSerifBold9pt7b
&fonts::FreeSerifBold12pt7b
&fonts::FreeSerifBold18pt7b
&fonts::FreeSerifBold24pt7b
&fonts::FreeSerifBoldItalic9pt7b
&fonts::FreeSerifBoldItalic12pt7b
&fonts::FreeSerifBoldItalic18pt7b
&fonts::FreeSerifBoldItalic24pt7b
&fonts::Orbitron_Light_24
&fonts::Orbitron_Light_32
&fonts::Roboto_Thin_24
&fonts::Satisfy_24
&fonts::Yellowtail_32
&fonts::DejaVu12
&fonts::DejaVu18
&fonts::DejaVu24
&fonts::DejaVu40
&fonts::DejaVu56
&fonts::DejaVu72
&fonts::DejaVu9
```

### Unicode 字体

- JA

```cpp line-num
&fonts::lgfxJapanMincho_8
&fonts::lgfxJapanMincho_12
&fonts::lgfxJapanMincho_16
&fonts::lgfxJapanMincho_20
&fonts::lgfxJapanMincho_24
&fonts::lgfxJapanMincho_28
&fonts::lgfxJapanMincho_32
&fonts::lgfxJapanMincho_36
&fonts::lgfxJapanMincho_40
&fonts::lgfxJapanMinchoP_8
&fonts::lgfxJapanMinchoP_12
&fonts::lgfxJapanMinchoP_16
&fonts::lgfxJapanMinchoP_20
&fonts::lgfxJapanMinchoP_24
&fonts::lgfxJapanMinchoP_28
&fonts::lgfxJapanMinchoP_32
&fonts::lgfxJapanMinchoP_36
&fonts::lgfxJapanMinchoP_40
&fonts::lgfxJapanGothic_8
&fonts::lgfxJapanGothic_12
&fonts::lgfxJapanGothic_16
&fonts::lgfxJapanGothic_20
&fonts::lgfxJapanGothic_24
&fonts::lgfxJapanGothic_28
&fonts::lgfxJapanGothic_32
&fonts::lgfxJapanGothic_36
&fonts::lgfxJapanGothic_40
&fonts::lgfxJapanGothicP_8
&fonts::lgfxJapanGothicP_12
&fonts::lgfxJapanGothicP_16
&fonts::lgfxJapanGothicP_20
&fonts::lgfxJapanGothicP_24
&fonts::lgfxJapanGothicP_28
&fonts::lgfxJapanGothicP_32
&fonts::lgfxJapanGothicP_36
&fonts::lgfxJapanGothicP_40
&fonts::efontJA_10
&fonts::efontJA_10_b
&fonts::efontJA_10_bi
&fonts::efontJA_10_i
&fonts::efontJA_12
&fonts::efontJA_12_b
&fonts::efontJA_12_bi
&fonts::efontJA_12_i
&fonts::efontJA_14
&fonts::efontJA_14_b
&fonts::efontJA_14_bi
&fonts::efontJA_14_i
&fonts::efontJA_16
&fonts::efontJA_16_b
&fonts::efontJA_16_bi
&fonts::efontJA_16_i
&fonts::efontJA_24
&fonts::efontJA_24_b
&fonts::efontJA_24_bi
&fonts::efontJA_24_i
```

- zh-CN

```cpp line-num
&fonts::efontCN_10
&fonts::efontCN_10_b
&fonts::efontCN_10_bi
&fonts::efontCN_10_i
&fonts::efontCN_12
&fonts::efontCN_12_b
&fonts::efontCN_12_bi
&fonts::efontCN_12_i
&fonts::efontCN_14
&fonts::efontCN_14_b
&fonts::efontCN_14_bi
&fonts::efontCN_14_i
&fonts::efontCN_16
&fonts::efontCN_16_b
&fonts::efontCN_16_bi
&fonts::efontCN_16_i
&fonts::efontCN_24
&fonts::efontCN_24_b
&fonts::efontCN_24_bi
&fonts::efontCN_24_i
```

- zh-TW

```cpp line-num
&fonts::efontTW_10
&fonts::efontTW_10_b
&fonts::efontTW_10_bi
&fonts::efontTW_10_i
&fonts::efontTW_12
&fonts::efontTW_12_b
&fonts::efontTW_12_bi
&fonts::efontTW_12_i
&fonts::efontTW_14
&fonts::efontTW_14_b
&fonts::efontTW_14_bi
&fonts::efontTW_14_i
&fonts::efontTW_16
&fonts::efontTW_16_b
&fonts::efontTW_16_bi
&fonts::efontTW_16_i
&fonts::efontTW_24
&fonts::efontTW_24_b
&fonts::efontTW_24_bi
&fonts::efontTW_24_i
```

- KR

```cpp line-num
&fonts::efontKR_10
&fonts::efontKR_10_b
&fonts::efontKR_10_bi
&fonts::efontKR_10_i
&fonts::efontKR_12
&fonts::efontKR_12_b
&fonts::efontKR_12_bi
&fonts::efontKR_12_i
&fonts::efontKR_14
&fonts::efontKR_14_b
&fonts::efontKR_14_bi
&fonts::efontKR_14_i
&fonts::efontKR_16
&fonts::efontKR_16_b
&fonts::efontKR_16_bi
&fonts::efontKR_16_i
&fonts::efontKR_24
&fonts::efontKR_24_b
&fonts::efontKR_24_bi
&fonts::efontKR_24_i
```

