# Base LAN PoE v1.2

<span class="product-sku">SKU:K012-C-V12</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/lan_poe_v12/lan_poe_v12_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/lan_poe_v12/lan_poe_v12_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/997/K012-C-V12-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/lan_poe_v12/lan_poe_v12_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/lan_poe_v12/lan_poe_v12_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/lan_poe_v12/lan_poe_v12_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/lan_poe_v12/lan_poe_v12_06.webp">
</PictureViewer>

## 描述

**Base LAN PoE v1.2** 是一款集成 **PoE**（Power Over Ethernet）功能的 **以太网控制模组**。采用 **W5500** 全硬件 TCP/IP 嵌入式以太网控制器（SPI 通信接口）方案，支持多种通信协议（TCP、UDP、IPv4、ICMP、ARP、IGMP 和 PPPoE 等）并集成储存缓存区便于以太网数据包处理。

内部预留拓展焊盘可以用于拓展 **RS485**/**RS232**/**CAN** 通信转接模块或是添加自定义设计，支持 PoE 供电且标配导轨固定配件，无需额外供电导线与结构设计即可轻松将其部署工业现场。兼具性能与拓展灵活性的 **Base LAN PoE v1.2** 能够为你提供更加简洁的嵌入式以太网连接方案。

## 产品特性

- W5500:
  - 支持 8 路独立硬件 Socket 同时通信
  - 支持 TCP、UDP、ICMP、IPv4、ARP、IGMP、PPPoE 协议
  - 集成 10BaseT / 100Base-T 以太网 PHY
- 有线以太网接入
  - RJ45 自适应 10/100M 网口
- 电源输入方式：
  - 支持 PoE IEEE802.3 AF / 供电电压 DC 37-57V
  - 支持输入电源电压: 9-24V
  - 支持 M5-Bus 5V 供电 (搭配 M5CORE 使用情况下)
- 滑轨或磁吸固定
- RS485/RS232/CAN 通信拓展板

## 包装内容

- 1 x Base LAN PoE v1.2
- 1 x RS485-To-TTL 转接板
- 1 x RS232-To-TTL 转接板
- 1 x CAN-To-TTL 转接板
- 1 x HT3.96-4P 端子
- 2 x HT3.96-3P 端子
- 1 x 内六角扳手 L 形 1.5mm (适配 M2 螺丝)
- 1 x 内六角扳手 L 形 2.0mm (适配 M2 螺丝)
- 1 x 内六角扳手 L 形 2.5mm (适配 M2 螺丝)
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
- PC 端与 Core 有线传输视频数据

<img src="https://static-cdn.m5stack.com/resource/docs/products/base/lan_base/lan_base_07.webp" width="40%" height="70%">
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/lan_base/lan_base_08.webp" width="40%" height="70%">

## 规格参数

| 规格               | 参数                                                                                                                                                               |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| W5500 以太网控制器 | 支持 TCP/IP 协议族 : TCP, UDP, ICMP, IPv4, ARP, IGMP, PPPoE<br/>支持 8 路独立硬件 Socket 同时通信<br/>支持高速 SPI (SPI MODE 0, 3)<br/>集成 32Kbytes TX/RX Buffers |
| RS485-To-TTL       | SP485EEN-L/TR                                                                                                                                                      |
| RS232-To-TTL       | MAX232ESE                                                                                                                                                          |
| CAN-To-TTL         | CA-IS3050G                                                                                                                                                         |
| 网口               | RJ45 自适应 10/100M 网口                                                                                                                                           |
| 产品尺寸           | 54.0 x 54.0 x 27.5mm                                                                                                                                               |
| 产品重量           | 41.3g                                                                                                                                                              |
| 包装尺寸           | 105.0 x 65.0 x 41.0mm                                                                                                                                              |
| 毛重               | 146.1g                                                                                                                                                             |

## 操作说明

### 拓展板焊接位置

> LAN BASE V12 标配了 TTL-RS485 + TTL-RS232 两款转接板，用于适配不同通信接口。焊接位置如下，实际链接 GPIO 请参考管脚映射表格。

- **RS232** 转接板焊接位 或 **RS485** 转接板焊接位

<img src="https://static-cdn.m5stack.com/resource/docs/products/base/lan_v12/lan_v12_07.webp" width="70%">
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/lan_v12/lan_v12_08.webp" width="70%">

## 原理图

<SchViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/lan_poe_v12/lan_poe_v12_sch_01.webp" width="70%">
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/lan_poe_v12/lan_poe_v12_sch_02.webp" width="70%">
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/lan_poe_v12/lan_poe_v12_sch_03.webp" width="70%">
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/lan_poe_v12/lan_poe_v12_sch_04.webp" width="70%">
</SchViewer>

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

### RS485/RS232/CAN 转接板

| ESP32 Chip | RS485/RS232 |
| ---------- | ----------- |
| RX         | G5          |
| TX         | G15         |

### M5-Bus

::m5-bus-table
| PIN               | LEFT | RIGHT | PIN               |
| ----------------- | ---- | ----- | ----------------- |
| GND               | 1    | 2     | NC                |
| GND               | 3    | 4     | NC                |
| GND               | 5    | 6     | NC                |
| SPI_MOSI          | 7    | 8     | NC                |
| SPI_MISO          | 9    | 10    | CS                |
| SPI_CLK           | 11   | 12    | NC                |
| NC                | 13   | 14    | NC                |
| NC                | 15   | 16    | NC                |
| NC                | 17   | 18    | NC                |
| NC                | 19   | 20    | RS232_TX/RS485_TX |
| NC                | 21   | 22    | RST               |
| RS232_RX/RS485_RX | 23   | 24    | NC                |
| HPWR              | 25   | 26    | INT               |
| HPWR              | 27   | 28    | 5V                |
| HPWR              | 29   | 30    | BAT               |
::

## 尺寸图

<img alt="module size" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/base/lan_poe_v12/%E5%B0%BA%E5%AF%B8%E5%9B%BE.jpg" width="100%" />

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
