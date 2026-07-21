# Base LAN v1.2

<span class="product-sku">SKU:K012-B-V12</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/lan_v12/lan_v12_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/lan_v12/lan_v12_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/999/K012-B-V12-weight.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/lan_v12/lan_v12_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/lan_v12/lan_v12_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/lan_v12/lan_v12_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/lan_v12/lan_v12_06.webp">
</PictureViewer>

## 描述

**Base LAN v1.2** 是一款以太网控制器底座，内置 **W5500** 全硬件 TCP/IP 嵌入式以太网控制器（SPI 通信接口），支持多种通信协议（TCP、UDP、IPv4、ICMP、ARP、IGMP 和 PPPoE 等）并集成储存缓存区便于以太网数据包处理。内部预留拓展焊盘可以用于拓展 RS485/RS232 通信转接模块或是添加自定义设计，标配固定导轨等配件，兼具性能与拓展灵活性的 **Base LAN v1.2** 能够为你提供更加简洁的嵌入式以太网连接方式。

## 产品特性

- 能够满足实际生产环境中的有线网络接入需求.
- 专为工业应用场景设计:
  - 提供金属滑轨便于安装固定
  - 配备 HT3.96 端子用作电气连接
  - 支持输入电源电压: 9-24V
- 标配 TTL-RS485 + TTL-RS232 两款转接板，适配不同通信接口.

## 包装内容

- 1 x Base LAN v1.2
- 1 x RS485-To-TTL 转接板
- 1 x RS232-To-TTL 转接板
- 1 x HT3.96-4P 端子
- 2 x HT3.96-3P 端子
- 1 x 1.5mm 六角扳手
- 1 x 2.0mm 六角扳手
- 1 x 2.5mm 六角扳手
- 10 x 2mm 冷压端子
- 1 x 磁铁 (中间带孔，直径 15mm，3mm 厚)
- 1 x 35mm 银色金属导轨
- 1 x 35mm 黑色导轨卡扣
- 1 x M3\*6mm 螺丝 (沉头，机械牙)
- 2 x M3\*28mm 螺丝 (杯头，机械牙)
- 4 x M2\*5mm 螺丝 (杯头，自攻牙)
- 1 x 2.54mm-20P 直插排针 (总高 5.32mm)
- 1 x 产品贴纸

## 应用场景

- M5Core + LAN 实现传输带控制器

<img src="https://static-cdn.m5stack.com/resource/docs/products/base/lan_base/lan_base_07.webp" width="70%" height="70%">

- PC 端与 Core 有线传输视频数据

<img src="https://static-cdn.m5stack.com/resource/docs/products/base/lan_base/lan_base_08.webp" width="70%" height="70%">

## 规格参数

| 规格         | 参数                     |
| ------------ | ------------------------ |
| 以太网控制器 | W5500                    |
| 网口         | RJ45 自适应 10/100M 网口 |
| 产品重量     | 32g                      |
| 毛重         | 132g                     |
| 产品尺寸     | 54 x 54 x 28mm           |
| 包装尺寸     | 105 x 65 x 40mm          |

## 操作说明

### 拓展板焊接位置

\#> 通信拓展板:|LAN BASE V12 标配了 TTL-RS485 + TTL-RS232 两款转接板，用于适配不同通信接口。焊接位置如下，实际链接 GPIO 请参考管脚映射表格。

- **RS232** 转接板焊接位 或 **RS485** 转接板焊接位

<img src="https://static-cdn.m5stack.com/resource/docs/products/base/lan_v12/lan_v12_07.webp" width="70%">
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/lan_v12/lan_v12_08.webp" width="70%">

## 原理图

- [Base LAN v1.2原理图PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/999/lan_base.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/999/lan_base_page_01.png" width="70%">

## 管脚映射

### W5500 以太网芯片

| W5500 | ESP32 Chip |
| ----- | ---------- |
| MOSI  | G23        |
| MISO  | G19        |
| CLK   | G18        |
| CS    | G26        |
| RST   | G13        |
| INTn  | G34        |

### RS485/RS232 转接板

| ESP32 Chip | RS485/RS232 |
| ---------- | ----------- |
| RX         | G5          |
| TX         | G15         |

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

## 数据手册

- [W5500](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/base/W5500_datasheet_v1.0.2_1_en.pdf)

## 软件开发

### Arduino

- [Base LAN PoE v1.2 Web Server Example](https://github.com/m5stack/M5Stack/blob/master/examples/Modules/Base_PoE/LAN_W5500/WebServer/WebServer.ino)
- [Base LAN PoE v1.2 RS485 Example](https://github.com/m5stack/M5Stack/blob/master/examples/Modules/Base_PoE/RS_485/RS_485.ino)

### UiFlow1

- [Base LAN PoE v1.2 UiFlow1 文档](/zh_CN/uiflow/blockly/base/lan_base)

### EasyLoader

| Easyloader               | Download                                                                                                 | Note |
| ------------------------ | -------------------------------------------------------------------------------------------------------- | ---- |
| Base LAN Test Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/BASE/EasyLoader_LAN_BASE.exe) | /    |

## 相关视频

**Base LAN 案例 - PC 使用 UDP 协议通过 LAN 底座实现有线传输视频给 Core**

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Blog/Twitch201904/M5StackLovyanlauncher.mp4" type="video/mp4">
</video>
