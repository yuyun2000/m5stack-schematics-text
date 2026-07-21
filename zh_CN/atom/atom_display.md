# Atom Display

<span class="product-sku">SKU:K115</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_display/atom_display_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_display/atom_display_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_display/atom_display_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_display/atom_display_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_display/atom_display_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_display/atom_display_06.webp">
</PictureViewer>

## 描述

**Atom Display** 是一款低成本的显示器驱动，使用 FPGA 模拟传统 SPI TFT-LCD 数据输出，支持最大 720P (1280 x 720) 的图像输出，并通过专用 RGB 转高清多媒体信号芯片实现广泛兼容的显示输出。内嵌 ESP32 控制器，集成 2.4G Wi-Fi，搭配 8MB Flash + 2MB PSRAM 内存组合。**Atom Display** 能够替代传统显示面板的 PC 控制方案，提供一种更加性价比的选择。

## 产品特性

- FPGA 与驱动库所有代码开源
- 采用 FPGA (Gowin GW1NR-9C)
- 内置 LT8618SX RGB 转高清多媒体信号芯片 (支持 24bit 色深)
- SPI 接口 (FPGA) + I2C 接口 (LT8618SX)
- 最大 720P (1280x720) 的图像输出
- 多种输出模式，优化帧率可达 12 ~ 16FPS
- 内置 Atom PSRAM 主控 (ESP32-PICO-V3-02, 8MB Flash + 2MB PSRAM)
- 可编程 RGB 灯 x1, 复位按钮 x1, 按键 x1, 全功能 Grove 拓展接口 x1
- 开发平台：Arduino, ESP32-IDF, UiFlow

## 包装内容

- 1 x Atom-PSRAM
- 1 x Atomic Display Base

## 应用场景

- 显示器输入信号源
- 高清数据看板

## 规格参数

| 规格             | 参数                                      |
| ---------------- | ----------------------------------------- |
| FPGA             | Gowin GW1NR-9C                            |
| LT8618SX         | RGB 转高清多媒体信号芯片，支持 24bit 色深 |
| 最大图像输出尺寸 | 720P (1280x720)                           |
| 输出帧率         | 1280x720 60Hz                             |
| USB 驱动芯片     | CH9102                                    |
| 产品尺寸         | 64 x 24 x 29mm                            |
| 产品重量         | 21.0g                                     |
| 包装尺寸         | 76 x 46 x 29mm                            |
| 毛重             | 34.0g                                     |

## 操作说明

\#> 显示器兼容性 | Atom Display Lite 需搭配具备自适应分辨率缩放功能的显示器，在一些不支持自适应分辨率的显示器上可能会出现显示异常现象。

## 原理图

<SchViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_display/atom_display_sch_01.webp" width="80%">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_display/atom_display_sch_02.webp" width="80%">
</SchViewer>

- [完整 Atom Display 原理图](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/atom_display/Sch_AtomDisplay.pdf)

## 管脚映射

::m5-bus-table
| PIN      | LEFT | RIGHT | PIN |
| -------- | ---- | ----- | --- |
| 3V3      |      | 1     |     |
| SPI_CLK  | 2    | 3     |     |
| CS       | 4    | 5     | 5V  |
| SPI_MISO | 6    | 7     | GND |
| SPI_MOSI | 8    | 9     |     |
::

- BUTTON & RGB LED

| Atom    | G39    | G27    |
| ------- | ------ | ------ |
| BUTTON  | SIGNAL | /      |
| RGB LED | /      | SK_DIN |

- LT8618SX

| Atom     | G25     | G21     | 5V  | GND |
| -------- | ------- | ------- | --- | --- |
| LT8618SX | LT_CSDA | LT_CSCL | VIN | GND |

## 尺寸图

- [Atom Display 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/894/K115-atom-display.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/894/K115-atom-display_page_01.png" width="100%">

## 软件开发

### Arduino

- [M5GFX - Lib](https://github.com/m5stack/M5GFX)

\#> 编程注意事项 | M5GFX 库中的案例程序使用前，需要将引入的头文件更改为适配当前使用的设备。如下方案例所示引入`#include <M5AtomDisplay.h>`，并创建实例`M5AtomDisplay display;`

```cpp

#include <Arduino.h>
#include <vector>

#include <M5AtomDisplay.h>
M5AtomDisplay display;

void setup(void)
{
  display.begin();
}

void loop(void)
{
  display.fillScreen(RED);
  delay(1000);
  display.fillScreen(GREEN);
  delay(1000);
  display.fillScreen(BLUE);
  delay(1000);
}

```

## 相关视频

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/AtomBase/ATOM_DISPLAY_VIDEO.mp4" type="video/mp4">
</video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=114318859371678&bvid=BV1hBdUYqENt&p=1&autoplay=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/i2KUrW6XYik?si=JrmvBXSw41SBmPc3" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
