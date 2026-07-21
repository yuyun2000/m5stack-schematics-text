# Base LAN

<span class="product-sku">SKU:K012-B</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/lan_base/lan_base_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/lan_base/lan_base_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/lan_base/lan_base_03.webp">
</PictureViewer>

## 描述

**Base LAN** 是一款以太网控制器底座。内置 **W5500** 全硬件 TCP/IP 嵌入式以太网控制器，为嵌入式系统提供更加简易的互联网连接方案。专为工业应用场景设计，提供金属滑轨和磁盘便于安装固定，配备 HT3.96 端子用作电气连接。能够满足实际生产环境中的有线网络接入需求。

## 产品特性

- 输入电源电压: 9-24V
- HT3.96 端子
- 支持 RS485 通信
- 固定方式简单

## 包装内容

- 1 x Base LAN
- 1 x TTL-RS485 转接板
- 1 x 排针 20pin
- 1 x 金属导轨和磁盘
- 3 x HT3.96 端子
- 2 x 3pin
- 1 x 4pin
- 10 x 冷压接端子
- 3 x 内六角扳手
    - 1 x 1.5mm
    - 1 x 2mm
    - 1 x 2.5mm
- 2 x 内六角螺丝 M3x28
- 4 x 内六角自攻螺丝 KA2x4
- 1 x 沉头螺丝 M3x8

## 应用场景

- M5Core + LAN 实现传输带控制器

<img src="https://static-cdn.m5stack.com/resource/docs/products/base/lan_base/lan_base_07.webp" width="70%" height="70%">

- PC 端与 Core 有线传输视频数据

<img src="https://static-cdn.m5stack.com/resource/docs/products/base/lan_base/lan_base_08.webp" width="70%" height="70%">

## 规格参数

| 规格     | 参数            |
| -------- | --------------- |
| 产品重量 | 32g             |
| 毛重     | 132g            |
| 产品尺寸 | 54 x 54 x 28mm  |
| 包装尺寸 | 105 x 65 x 40mm |

## 操作说明

HT3.96 连接器的 6 个引脚默认悬空，你可以根据需求将其与 M5-Bus 的任意引脚进行连接.

**下图为 LAN 的内部构造**

如果需要添加 RS485 通信接口，请将 TTL-RS485 转接板与配套排针焊接到主板上相应的引脚上.

**TTL-RS485 转接板 与 LAN 底座**

<img src="https://static-cdn.m5stack.com/resource/docs/products/base/lan_base/lan_base_04.webp" width="60%">

**TTL-RS485 转接板 与 LAN 底座的连接图**

TTL-RS485 转接板的串口引脚将连接到 LAN 底座的 G16 和 G17.

<img src="https://static-cdn.m5stack.com/resource/docs/products/base/lan_base/lan_base_05.webp" width="50%" height="50%">

<img src="https://static-cdn.m5stack.com/resource/docs/products/base/lan_base/lan_base_06.webp" width="70%">

## 原理图

- [Base LAN 原理图 PDF](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/schematic/Bases/lan_base.pdf)

<img src="https://static-cdn.m5stack.com/resource/docs/products/base/lan_base/lan_base_sch_01.webp" width="70%">

## 管脚映射

### W5500 以太网芯片

| W5500 | ESP32 Chip |
| :---: | :--------: |
| MOSI  | G23        |
| MISO  | G19        |
| CLK   | G18        |
| CS    | G26        |
| RST   | G13        |
| INTn  | G34        |

### M5-Bus

\#> Switch | 下方 M5-Bus 中标记 `SW` 的引脚，可通过拨码开关进行切换，用于适配不同的主控设备。

::m5-bus-table
| PIN                    | LEFT | RIGHT | PIN                    |
| ---------------------- | ---- | ----- | ---------------------- |
| GND                    | 1    | 2     | NC                     |
| GND                    | 3    | 4     | NC                     |
| GND                    | 5    | 6     | NC                     |
| SPI_MOSI               | 7    | 8     | NC                     |
| SPI_MISO               | 9    | 10    | CS                     |
| SPI_CLK                | 11   | 12    | NC                     |
| NC                     | 13   | 14    | NC                     |
| NC                     | 15   | 16    | NC                     |
| NC                     | 17   | 18    | NC                     |
| NC                     | 19   | 20    | RS232_TX/RS485_TX (SW) |
| NC                     | 21   | 22    | RST                    |
| RS232_RX/RS485_RX (SW) | 23   | 24    | NC                     |
| HPWR                   | 25   | 26    | INT                    |
| HPWR                   | 27   | 28    | 5V                     |
| HPWR                   | 29   | 30    | BAT                    |
::

## 尺寸图

- [Base LAN 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/996/K012-C-K012-B-BASE-LAN.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/996/K012-C-K012-B-BASE-LAN_page_01.png" width="100%">

## 数据手册

- [W5500](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/base/W5500_datasheet_v1.0.2_1_en.pdf)

## 软件开发

### Arduino

- [Base LAN Web Server Example](https://github.com/m5stack/M5Stack/blob/master/examples/Modules/Base_PoE/LAN_W5500/WebServer/WebServer.ino)
- [Base LAN RS485 Example](https://github.com/m5stack/M5Stack/blob/master/examples/Modules/Base_PoE/RS_485/RS_485.ino)

### UiFlow1

- [Base LAN UiFlow1 文档](/zh_CN/uiflow/blockly/base/lan_base)

### EasyLoader

| Easyloader               | Download                                                                                                 | Note |
| ------------------------ | -------------------------------------------------------------------------------------------------------- | ---- |
| Base LAN Test Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/BASE/EasyLoader_LAN_BASE.exe) | /    |

## 相关视频

**Base LAN 案例 - PC 使用 UDP 协议通过 LAN 底座实现有线传输视频给 Core**

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Blog/Twitch201904/M5StackLovyanlauncher.mp4" type="video/mp4">
</video>
