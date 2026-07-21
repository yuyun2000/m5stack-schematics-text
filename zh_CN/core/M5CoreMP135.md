# CoreMP135

<span class="product-sku">SKU:K135</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/M5CoreMP135/img-e1972b35-73c9-4a6c-a91f-adcd915b7771.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/M5CoreMP135/img-7865e70c-3235-4410-a2b3-37f68f92d3fa.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/M5CoreMP135/img-fe7a09c5-eb66-47bc-9246-b871bfff0bcf.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/497/K135_main_pictures_01.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/497/K135_main_pictures_03.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/497/K135_main_pictures_02.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/497/K135_main_pictures_04.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/M5CoreMP135/img-6bd0997d-2a48-4fba-b251-796ef88f22d9.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/M5CoreMP135/img-c5cc6409-17d3-40ee-9b15-ede6b129fb9d.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/M5CoreMP135/img-20181675-5898-4f24-a266-75513dd0b587.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/M5CoreMP135/img-9b07a582-f5c5-4e87-a643-a97786556991.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/497/K135_Weight.jpg">
</PictureViewer>

## 描述

**CoreMP135** 是一款基于 **STM32MP135DAE7** 芯片的一体化 **Linux** 工控主机。其集成了单核 ARM Cortex-A7 处理器，主频高达 1 GHz ，另配备 4Gbit DDR3L SDRAM 运行内存。
适用于高级工业自动化、智能家居和多媒体娱乐设备以及工业物联网边缘网关，机器人运动控制中枢等领域。

**CoreMP135** 提供多个功能丰富的接口：

- 2 路千兆网 GbE 接口
- 1 路高清视频输出接口
- 2 路 USB2.0-A 接口
- 1 路 USB-C 接口 (支持 OTG 及供电) ，microSD 卡槽
- 2 路 CAN FD 接口
- 1 路 PWR485 (9~24V 电源输入 + RS485) 接口
- 2 个 Grove (I2C & UART) 接口

在人机交互界面方面，CoreMP135 自带 2.0 英寸 IPS 电容触摸屏，并搭载 1W 扬声器（16 位 I2S 驱动）。整机采用低功耗设计，搭载 AXP2101 电源管理芯片，内置 BM8563 RTC，支持定时唤醒与休眠功能；支持可充电电池供电，同时配备 DC 电源接口，可外接 DC 12V@2A 直流电源供电。设备适配多种安装场景，底部配有 DIN 导轨底板，支持挂壁与螺丝固定安装。

## 教程 & 快速上手

learn>| ![UiFlow2](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/uiflow2.0_banner_01.png) | [UiFlow2](/zh_CN/guide/linux/coremp135/uiflow2) | 本教程将向你介绍，如何通过 UiFlow2 图形化编程平台控制 CoreMP135 设备。 |

## 产品特性

- STM32MP135DAE7@Arm Cortex-A7@1GHz
- Linux 标准平台
- 多种通讯方式，丰富的外设接口 (CANRS485 千兆网口等)
- 2.0 寸触摸屏幕
- 统一电源管理
- 内置扬声器
- microSD 以及 4Gbit DDR3L SDRAM 运行内存
- M5-Bus\&PORT A/C
- DIN Rail 导轨方便安装
- 开发平台
  - UiFlow2

## 包装内容

- 1 x CoreMP135
- 1 x M3 六角扳手
- 1 x HT3.96-4P
- 2 x 接线端子 2.54mm-2P (绿色)
- 1 x microSD 卡 (已经装于机器中)
- 1 x 说明书

## 应用场景

- 工业自动化
- 智能家居
- 工业物联网边缘网关
- 教育和开发
- 机器人运动中枢控制器

## 规格参数

| 规格             | 参数                                                                                 |
| ---------------- | ------------------------------------------------------------------------------------ |
| MCU              | STM32MP135DAE7@单核 Arm Cortex-A7 处理器，主频 1 GHz                                 |
| 电源管理芯片     | AXP2101                                                                              |
| 485 通讯         | MAX3485                                                                              |
| CAN 通讯         | 两路 SIT1051T/3 (高速 FDCAN)                                                         |
| USB 集线器接口   | GL852G (2x USB2.0)<br/>1x USBC (支持 OTG 及供电)                                     |
| 高清视频接口芯片 | LT8618SXB，支持最高 24 位的色深                                                      |
| DDR3L SDRAM      | 4Gbit                                                                                |
| 以太网           | RTL8211F（最高支持 1Gbps 的数据速率）<br/>2x RJ45                                    |
| RTC 时钟         | BM8563                                                                               |
| 屏幕             | ILI9342C (2.0 IPS LCD)<br/>分辨率：240 x 320px                                       |
| 屏幕触摸         | FT6336U                                                                              |
| 功放             | NS4168 (单声道 D 类功放)<br/>I2S 串行数字音频输入<br/>支持宽范围采样速率：8kHz~96kHz |
| 扬声器           | 2014 型腔体喇叭：1W@8Ω                                                               |
| 直流电源输入     | DC 12V@2A                                                                            |
| 工作温度         | 0 ~ 40°C                                                                             |
| 供电电源         | DC 12V@2A 或者 USB-C 5V@3A                                                           |
| 产品尺寸         | 81.9 x 54.0 x 39.5mm                                                                 |
| 产品重量         | 98.3g                                                                                |
| 包装尺寸         | 122.2 x 71.5 x 61.6mm                                                                |
| 毛重             | 154.7g                                                                               |

## 操作说明

### M5-Bus 电源

\#>CoreMP135 的 M5-Bus 电源总线输入输出控制： | 参考原理图将 BUS_OUT_EN 设置为低电平则总线 5V 为输入模式，高电平则总线 5V 为输出模式。可使用以下指令打开向下输出：

```bash
echo 131 > /sys/class/gpio/export && echo out > /sys/class/gpio/PI3/direction
echo 1 > /sys/class/gpio/PI3/value
# echo 0 > /sys/class/gpio/PI3/value
```

### CoreMP135 模块总线电源配置

CoreMP135 的总线电源默认处于关闭状态，在进行 I2C 地址扫描、模块初始化前，需先执行以下命令手动开启总线电源，否则会出现模块无法被识别、I2C 地址扫描不到的问题。

```bash
echo 131 > /sys/class/gpio/export && echo out > /sys/class/gpio/PI3/direction && echo 1 > /sys/class/gpio/PI3/value
```

## 原理图

- [CoreMP135 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/497/Sch_M5_CoreMP135_2024-04-24.pdf)
- [CoreMP135 MidLayer 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/497/Sch_M5_CoreMP1_MidLayer_2024-04-24.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/497/Sch_M5_CoreMP135_2024-04-24_sch_01.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/497/Sch_M5_CoreMP135_2024-04-24_sch_02.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/497/Sch_M5_CoreMP135_2024-04-24_sch_03.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/497/Sch_M5_CoreMP135_2024-04-24_sch_04.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/497/Sch_M5_CoreMP135_2024-04-24_sch_05.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/497/Sch_M5_CoreMP135_2024-04-24_sch_06.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/497/Sch_M5_CoreMP135_2024-04-24_sch_07.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/497/Sch_M5_CoreMP135_2024-04-24_sch_08.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/497/Sch_M5_CoreMP135_2024-04-24_sch_09.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/497/Sch_M5_CoreMP135_2024-04-24_sch_10.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/497/Sch_M5_CoreMP135_2024-04-24_sch_11.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/497/Sch_M5_CoreMP135_2024-04-24_sch_12.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/497/Sch_M5_CoreMP1_MidLayer_2024-04-24_sch_01.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/497/Sch_M5_CoreMP1_MidLayer_2024-04-24_sch_02.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/497/Sch_M5_CoreMP1_MidLayer_2024-04-24_sch_03.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/497/Sch_M5_CoreMP1_MidLayer_2024-04-24_sch_04.png">
</SchViewer>

## 管脚映射

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/497/K135_pinmap_01.png" width="100%">

### M5-Bus

::m5-bus-table
| FUNC     | PIN       | LEFT | RIGHT | PIN        | FUNC     |
| -------- | --------- | ---- | ----- | ---------- | -------- |
|          | GND       | 1    | 2     | PA0        | GPIO     |
|          | GND       | 3    | 4     | PA3        | PB_IN    |
|          | GND       | 5    | 6     | AXP-PWR-OK |          |
| SPI4MO   | PE11      | 7    | 8     | PB13       | GPIO     |
| SPI4MI   | PE13      | 9    | 10    | PE9        | PB_OUT   |
| SPI4SCK  | PB4       | 11   | 12    | 3V3        |          |
| U2RX     | PH8       | 13   | 14    | PF11       | U2TX     |
|          | DS-USB1-N | 15   | 16    | DS-USB1-P  |          |
| I2C1-SDA | PG8       | 17   | 18    | PB8        | I2C1-SCL |
| I2C2-SDA | PG9       | 19   | 20    | PF2        | I2C2-SCL |
| GPIO     | PA6       | 21   | 22    | PB10       | GPIO     |
| GPIO     | PA5       | 23   | 24    | PC13       | GPIO     |
|          | NC        | 25   | 26    | PA1        | GPIO     |
|          | NC        | 27   | 28    | 5V         |          |
|          | NC        | 29   | 30    | BAT        |          |
::

| M5-Bus   | STM32MP135DAE7 |
| -------- | -------------- |
| U2RX     | PH8            |
| U2TX     | PF11           |
| I2C1-SDA | PE8            |
| I2C1-SCL | PB8            |
| I2C2-SDA | PG9            |
| I2C2-SCL | PF2            |

| 设备名称 | Linux 设备节点 |
| -------- | -------------- |
| USART2   | /dev/ttySTM2   |
| I2C1     | /dev/i2c-2     |
| I2C2     | /dev/i2c-3     |

### PORT.A

| PORT.A         | I2C5_SCL | I2C5_SDA |
| -------------- | -------- | -------- |
| STM32MP135DAE7 | PA11     | PF3      |

| 设备名称 | Linux 设备节点 |
| -------- | -------------- |
| UI2C5    | /dev/i2c-1     |

### PORT.C

| PORT.C         | USART6RX | USART6TX |
| -------------- | -------- | -------- |
| STM32MP135DAE7 | PC6      | PC7      |

| 设备名称 | Linux 设备节点 |
| -------- | -------------- |
| USART6   | /dev/ttySTM0   |

### RS485

| MAX3485EIM     | USART3RX | USART3TX | DE/RE |
| -------------- | -------- | -------- | ----- |
| STM32MP135DAE7 | PG4      | PD8      | PD12  |

| 设备名称 | Linux 设备节点 |
| -------- | -------------- |
| USART3   | /dev/ttySTM3   |

### CAN

| STM32MP135DAE7     | PE3       | PE10      | PG0       | PE0       |
| ------------------ | --------- | --------- | --------- | --------- |
| SIT1051T/3(FDCAN1) | FDCAN1_TX | FDCAN1_RX |           |           |
| SIT1051T/3(FDCAN2) |           |           | FDCAN2_TX | FDCAN2_RX |

### Display

| LT8618SXB      | MCLK | SCLK | SD0 | WS   | I2C3_SDA | I2C3_SCL |
| -------------- | ---- | ---- | --- | ---- | -------- | -------- |
| STM32MP135DAE7 | PF13 | PF8  | PA3 | PG10 | PH7      | PH12     |

| 设备名称 | Linux 设备节点 |
| -------- | -------------- |
| I2C3     | /dev/i2c-0     |

### RTC

| PORT.A         | I2C3_SCL | I2C3_SDA |
| -------------- | -------- | -------- |
| STM32MP135DAE7 | PH7      | PH12     |

| 设备名称 | Linux 设备节点 |
| -------- | -------------- |
| I2C3     | /dev/i2c-0     |

### microSD

| microSD        | SD_DAT0 | SD_DAT1 | SD_DAT2 | SD_DAT3 | SD_CMD | SD_CLK |
| -------------- | ------- | ------- | ------- | ------- | ------ | ------ |
| STM32MP135DAE7 | PC8     | PC9     | PC10    | PC11    | PD2    | PC12   |

### NS4168

| NS4168         | LRCLK | BCLK | SDATA | WS   | I2C3_SDA | I2C3_SCL |
| -------------- | ----- | ---- | ----- | ---- | -------- | -------- |
| STM32MP135DAE7 | PE4   | PA4  | PD6   | PG10 | PH7      | PH12     |

| 设备名称 | Linux 设备节点 |
| -------- | -------------- |
| I2C3     | /dev/i2c-0     |

### Screen\&Touch

| STM32MP135DAE7  | ILI9342C | FT6336U |
| --------------- | -------- | ------- |
| PI0             | RST      |         |
| PC0             | MOSI     |         |
| PC3             | SCK      |         |
| PH5             | CS       |         |
| PH4             | DC       |         |
| PH12 (I2C3_SCL) |          | TP_SCL  |
| PH7 (I2C3_SDA)  |          | TP_SDA  |

| AX2101   | DLDO1 |
| -------- | ----- |
| ILI9342C | BL    |

| 设备名称 | Linux 设备节点 |
| -------- | -------------- |
| I2C3     | /dev/i2c-0     |

## 尺寸图

<img alt="module size" src="https://static-cdn.m5stack.com/resource/docs/products/core/M5CoreMP135/img-505b3448-ea63-497b-85d9-07a7a4259edb.png" width="100%" />

## 结构文件

- [CoreMP135 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/K135_CoreMP135/Structures)

## 数据手册

- [STM32MP135DAF7](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5CoreMP135/STM32MP135DAF7_%E8%A7%84%E6%A0%BC%E4%B9%A6_%E8%A7%84%E6%A0%BC%E4%B9%A6WJ364699.PDF)
- [GL852G(USB Hub Chip)](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5CoreMP135/GL852G-HHG12.PDF)
- [LT8618SXB](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5CoreMP135/LT8616SX.pdf)
- [RTL8211F(Ethernet chip)](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5CoreMP135/RTL8211F.pdf)
- [FT6336U(Touch Screen Driver)](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/Ft6336GU_Firmware%20%E5%A4%96%E9%83%A8%E5%AF%84%E5%AD%98%E5%99%A8_20151112-%20EN.xlsx)
- [NS4168(amplifier chip)](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/NS4168_CN_datasheet.pdf)
- [BM8563(Clock Chip)](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/BM8563_V1.1_cn.pdf)
- [AXP2101(PMU)](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/Core2%20v1.1/axp2101.pdf)
- [SIT1051T/3(CAM Comunication)](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5CoreMP135/SIT1051T%E3%80%813.pdf)
- [ILI9342C(Screen Driver)](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/ILI9342C-ILITEK.pdf)

## 软件开发

### 快速上手

- [CoreMP135 镜像烧录与软件更新](/zh_CN/guide/linux/coremp135/image)
- [CoreMP135 应用开发框架](/zh_CN/guide/linux/coremp135/develop)
- [CoreMP135 根文件系统扩容](/zh_CN/guide/linux/coremp135/fdisk)
- [CoreMP135 网络配置](/zh_CN/guide/linux/coremp135/network)
- [CoreMP135 Buildroot 编译](/zh_CN/guide/linux/coremp135/buildroot)
- [CoreMP135 覆盖设备树](/zh_CN/guide/linux/coremp135/dtbo)

### UiFlow2

- [CoreMP135 UiFlow2 快速上手](/zh_CN/guide/linux/coremp135/uiflow2)

### SDK

- [M5Stack Linux Libs](https://github.com/m5stack/M5Stack_Linux_Libs)
- [CoreMP135 Buildroot](https://github.com/m5stack/CoreMP135_buildroot)

\#>Buildroot | Buildroot 是一个简单、高效、易用的嵌入式生成工具，该存储库是一个 Buildroot BR2_EXTERNAL 树，专门用于支持 STM32MP1 平台。

- [CoreMP135 Buildroot External ST](https://github.com/m5stack/CoreMP135_buildroot-external-st)

### 镜像文件

| 镜像版本                        | 内核版本 | 下载链接                                                                                                             |
| ------------------------------- | -------- | -------------------------------------------------------------------------------------------------------------------- |
| M5_CoreMP135_buildroot_20240515 | 5.15.118 | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/coremp135/M5_CoreMP135_buildroot_20240515.7z) |
| M5_CoreMP135_buildroot_20240628 | 5.15.118 | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/coremp135/M5_CoreMP135_buildroot_20240628.7z) |
| M5_CoreMP135_debian12_20240515  | 5.15.118 | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/coremp135/M5_CoreMP135_debian12_20240515.7z)  |
| M5_CoreMP135_debian12_20240628  | 5.15.118 | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/coremp135/M5_CoreMP135_debian12_20240628.7z)  |
| M5_CoreMP135_debian12_20240919  | 5.15.118 | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/coremp135/M5_CoreMP135_debian12_20240919.7z)  |

## 相关视频

- CoreMP135 简介

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5CoreMP135/K135%20CoreMP135%20%E8%A7%86%E9%A2%91.mp4" type="video/mp4"></video>

- CoreMP135 镜像烧录

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/linux/coremp135/coremp135_image.mp4" type="video/mp4"></video>

- 基于 M5Stack Linux 应用开发框架编程控制 CoreMP135 上的外设硬件

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/linux/coremp135/coremp135_develop.mp4" type="video/mp4"></video>

- CoreMP135 UiFlow2 快速上手

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/linux/coremp135/cmp135UIFlow2quickstart.mp4" type="video/mp4"></video>
