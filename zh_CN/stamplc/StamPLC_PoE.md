# StamPLC PoE

<span class="product-sku">SKU:A165</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1202/A165_main-pictures_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1202/A165_main-pictures_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1202/A165_main-pictures_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1202/A165_main-pictures_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1202/A165_main-pictures_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1202/A165_main-pictures_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1202/A165_main-pictures_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1202/A165_main-pictures_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1202/A165_main-pictures_09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1202/A165_main-pictures_10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1202/A165_main-pictures_11.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1202/A165_main-pictures_12.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1202/A165_main-pictures_13.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1202/A165-weight.jpg">
</PictureViewer>

## 描述

StamPLC PoE 是一款适配 StamPLC 主机的以太网控制模块，支持 PoE（有源以太网）技术，可通过网线同时实现数据传输与供电。该模块内置 W5500 嵌入式以太网控制器，集成 TCP/IP 协议栈，具备 8 路独立硬件 Socket、10/100M 以太网数据链路层（MAC）及物理层（PHY），支持 UDP、TCP 等主流网络通信方式。模块通过 RJ45 以太网接口接入网络，通过 SPI 接口与 StamPLC 主机进行通信，适用于对网络稳定性和实时性要求较高的场景，如工业自动化产线、楼宇集中控制系统、能源与配电监控、机房与通信设备管理等有线网络接入应用场景。

## 教程 & 快速上手

learn>| ![Arduino IDE](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/arduino_banner_01.png) | [Arduino IDE](/zh_CN/arduino/projects/stamplc/stamplc_poe) | 本教程介绍如何通过 Arduino IDE 编程控制 StamPLC PoE。|

## 产品特性

- W5500 嵌入式以太网控制器
- SPI 协议控制
- 支持 PoE（有源以太网）供电，通过单根网线同时实现数据与供电
- 支持通过 UDP 实现以太网唤醒功能
- 集成 TCP/IP 协议栈，支持 TCP / UDP / ICMP / IPv4 / ARP / IGMP / PPPoE 协议
- 支持最多 8 路独立硬件 Socket 并发通信
- 集成 10/100M 以太网 MAC 与 PHY，支持全双工 / 半双工工作模式
- 支持网速自适应
- 板载 RJ45 以太网接口
- DIN 导轨安装 / 挂孔安装
- 开发平台
  - Arduino
  - UiFlow2

## 包装内容

- 1 x StamPLC PoE
- 2 x 固定连接件

## 应用场景

- 自动化产线
- 楼宇集中控制系统
- 能源与配电监控
- 机房与通信设备管理

## 规格参数

| 规格             | 参数                                               |
| ---------------- | -------------------------------------------------- |
| 通信方式         | SPI 通信                                           |
| 以太网控制器     | W5500                                              |
| 以太网速率       | 10/100M 自适应                                     |
| 供电方式         | PoE / DC 12V / DC 5V                               |
| 硬件 Socket 数量 | 8 路独立硬件 Socket                                |
| 支持协议         | TCP / UDP / ICMP / IPv4 / ARP / IGMP / PPPoE       |
| PoE 特性         | 符合 IEEE802.3af 标准，支持 DC 37 ~ 57V 宽电压输入 |
| PoE 功率         | 最大 13W                                           |
| 接口类型         | 2 × 8P 2.54mm 排针 / 排母，RJ45 以太网接口         |
| MAC/PHY          | 集成 10/100M MAC & PHY                             |
| 安装方式         | DIN 导轨安装 / 挂孔                                |
| 产品尺寸         | 77.0 x 38.0 x 27.1mm                               |
| 产品重量         | 46.0g                                              |
| 包装尺寸         | 80.0 x 47.0 x 30.0mm                               |
| 毛重             | 52.0g                                              |

## 原理图

- [StamPLC PoE 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1202/SCH_StamPLC_PoE_SCH_MAIN_V1.0_20251104_2025_12_02_17_25_33.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1202/SCH_StamPLC_PoE_SCH_MAIN_V1.0_20251104_2025_12_02_17_25_33_page_01.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1202/SCH_StamPLC_PoE_SCH_MAIN_V1.0_20251104_2025_12_02_17_25_33_page_02.png">
</SchViewer>

## 管脚映射

| StamPLC     | G8   | G9   | G7  | G11 | G3  | G14 |
| ----------- | ---- | ---- | --- | --- | --- | --- |
| StamPLC PoE | MOSI | MISO | SCK | CS  | RST | INT |

### StamPLC-Bus

::m5-bus-table
| PIN      | LEFT | RIGHT | PIN     |
| -------- | ---- | ----- | ------- |
| VIN      | 1    | 2     | GND     |
| GND      | 3    | 4     | GND     |
| GND      | 5    | 6     | EXT_5V  |
| SCL      | 7    | 8     | SDA     |
| RST      | 9    | 10    | INT     |
| SPI_MISO | 11   | 12    | SPI_SCK |
| SPI_MOSI | 13   | 14    | SPI_CS  |
|          | 15   | 16    |         |
::

## 尺寸图

- [StamPLC PoE 尺寸图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1202/A165-model-size-stamplc-poe.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1202/A165-model-size-stamplc-poe_page_01.png">

## 数据手册

- [W5500](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/base/W5500_datasheet_v1.0.2_1_en.pdf)

## 软件开发

### Arduino

- [StamPLC PoE Arduino 快速上手](/zh_CN/arduino/projects/stamplc/stamplc_poe)

### UiFlow2

- [StamPLC PoE UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/stamplc/poe.html)

### ESP-IDF

- [W5500 ESP-IDF 组件](https://github.com/espressif/esp-idf/tree/v5.5.2/examples/ethernet)

### 软件注意事项

StamPLC 在搭配 StamPLC PoE 扩展模块时，需要注意以下事项:

1. `StamPLC LCD` 屏幕的 RST，内部 IO 扩展芯片(`PI4IOE`) 的 RST，外部的 `StamPLC PoE` 扩展模块的 RST 互相连接。
2. 部分驱动库在初始化 StamPLC PoE 以太网模块 (W5500) 时候，会控制 RST 引脚，操作引脚复位。该操作将导致已经初始化的屏幕也一同复位，建议在以太网的驱动程序初始化时，将 RST 引脚配置为空(-1)。
3. 内部 IO 扩展芯片(PI4IOE) 的 INT 引脚连接到了，外部 StamPLC PoE 扩展模块的中断信号。当扩展模块的中断信号产生时，会导致 IO 扩展芯片(PI4IOE) 中断总线异常占用，为避免该状态产生，需对 IO 扩展芯片 进行以下配置:

将 PI4IOE 的中断掩码寄存器配置为全部禁用

```cpp
#define PI4IO_REG_INT_MASK 0x11
#define PI4IO_REG_IRQ_STA  0x13
#define PI4IO_REG_CHIP_ID  0x01

static void prepare_shared_int_gpio(void)
{
#if CONFIG_ETHERNET_SPI_INT0_GPIO >= 0 && CONFIG_ETHERNET_SPI_POLLING0_MS == 0
    i2c_bus_device_handle_t pi4io = io_expander.get_device_handle();
    if (pi4io) {
        i2c_bus_write_byte(pi4io, PI4IO_REG_INT_MASK, 0xFF);
        uint8_t dummy = 0;
        i2c_bus_read_byte(pi4io, PI4IO_REG_IRQ_STA, &dummy);
        i2c_bus_read_byte(pi4io, PI4IO_REG_CHIP_ID, &dummy);
    }
    i2c_bus_handle_t bus = io_expander.get_bus_handle();
#endif
}
```

以下为 ESP-IDF 环境，处理上述冲突问题的示例工程:

- [ESP-IDF StamPLC PoE Demo](https://github.com/Ocean-lhy/Stamplc-poe-demo)

## 相关视频

- StamPLC PoE 产品介绍以及功能展示

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1202/A165_StamPLC_PoE_video_ZH.mp4" type="video/mp4"></video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=115925160429698&bvid=BV14ikVBsEM7&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/uiPqSBEjRs4?si=KG66nB_FRz8Vt_QB" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
