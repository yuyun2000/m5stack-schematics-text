# CardputerZero

?> Work in progress | 本产品包装及软件研发尚未完成，最终功能及资料可能有变，敬请理解。

<span class="product-sku">SKU:C154</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1243/C154-CardputerZero-main-pictures_01.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1243/C154-CardputerZero-main-pictures_02.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1243/C154-CardputerZero-main-pictures_03.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1243/C154-CardputerZero-main-pictures_04.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1243/C154-CardputerZero-main-pictures_05.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1243/C154-CardputerZero-main-pictures_06.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1243/C154-CardputerZero-main-pictures_07.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1243/C154-CardputerZero-main-pictures_08.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1243/C154-CardputerZero-main-pictures_09.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1243/C154-CardputerZero-main-pictures_10.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1243/C154-CardputerZero-main-pictures_11.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1243/C154-CardputerZero-main-pictures_12.png">
</PictureViewer>

## 描述

**CardputerZero** 是一款面向极客与开发者的口袋 **Linux** 个人电脑，基于 **Raspberry Pi CM0** 平台，集成四核 Cortex-A53 处理器、1.9 英寸显示屏、46 键矩阵键盘、8MP 摄像头、IMU 与 RTC，在掌上体积中提供接近完整开发终端的交互体验。它同时具备 Wi-Fi、蓝牙、以太网、microSD、可切换 Host/Slave 的 USB 体系，以及 I2C/UART/SPI/GPIO 等模块化扩展能力，配合音视频编解码与电池供电设计，可实现随身开发、边缘采集与多媒体交互的一体化。典型应用场景包括：移动渗透与运维终端、物联网设备调试与现场部署、便携式 AI / 视觉原型验证、创客项目开发，以及户外数据采集与快速人机交互控制。

## 产品特性

- 核心性能:
  - Raspberry Pi Compute Module 0 (CM0)
  - RP3A0 (BCM2837)，四核 Cortex-A53 @ 1 GHz
  - 512 MB LPDDR2
- 人机交互:
  - 1.9" LCD 屏幕，分辨率 320 x 170
  - 46 键矩阵键盘
  - IMX219 8MP 摄像头
  - BMI270 IMU + BMM150 磁力计
  - 红外发射 + 接收
- 网络通信:
  - 2.4 GHz Wi-Fi 802.11 b/g/n
  - 10/100M 以太网
- USB 扩展:
  - 支持 Host / Slave 模式切换
  - 1x USB-A 2.0
  - 2x USB Type-C 2.0，其中右侧接口支持 USB OTG
- 外部扩展:
  - 1x microSD 卡槽
  - 1x HY2.0-4P 接口，支持 I2C / UART 切换
  - EXT 2.54-14P 扩展总线，支持 SPI、UART、I2C、USB 和 GPIO
- 音视频:
  - ES8389 音频编解码
  - 1x MEMS 麦克风
  - 1W @ 8Ω 扬声器
  - 3.5mm TRRS 音频输入/输出接口
  - 支持 1080P 30fps 视频输出与编解码
- 电源管理:
  - 内置 DC 3.7V@1750mAh 锂电池，集成 NTC
  - BQ27220YZFR 电池计量
  - RX8130CE RTC

## 包装内容

#> 产品提示 | CardputerZero 标准版标配 32GB microSD 卡，CardputerZero-Lite 不含 microSD 卡，需另行购置。

### CardputerZero (SKU:C154)

- 1 x CardputerZero
- 1 x 32GB microSD

### CardputerZero-Lite (SKU:C155)

- 1 x CardputerZero-Lite

## 应用场景

- 运维终端
- 物联网设备调试
- 便携式 AI / 视觉原型验证
- 创客项目开发

## 规格参数

| 规格         | 参数                                                                                  |
| ------------ | ------------------------------------------------------------------------------------- |
| 核心主控     | Raspberry Pi Compute Module 0 (CM0)                                                   |
| CPU          | RP3A0 (BCM2837)，四核 Cortex-A53 @ 1 GHz, ARMv8-A (aarch64)                           |
| 内存         | 512 MB LPDDR2                                                                         |
| 存储         | microSD                                                                               |
| Wi-Fi        | 2.4GHz Wi-Fi 802.11 b/g/n                                                             |
| 以太网       | 10/100M 以太网接口，SR9900A USB 2.0 转以太网芯片                                      |
| 显示屏       | 1.9" LCD 屏幕 @ ST7789v3, 分辨率 320 x 170                                            |
| 摄像头       | IMX219 CSI 4-Lane 8MP (3280 x 2464)                                                   |
| IMU & 磁力计 | BMI270 + BMM150                                                                       |
| RTC          | RX8130CE                                                                              |
| 红外         | 红外发射 + 接收                                                                       |
| 键盘         | 46 键矩阵键盘                                                                         |
| 音频编解码   | ES8389                                                                                |
| 麦克风       | 1x MEMS 麦克风                                                                        |
| 扬声器       | AW8737A 扬声器功放 + 1W @ 8Ω 扬声器                                                   |
| 音频接口     | 3.5mm TRRS 音频输入/输出接口，推荐适配 35Ω 阻抗耳机                                   |
| 视频输出     | 1x 高清数字音视频输出接口，支持 1080P 30fps                                           |
| 视频编解码   | H.264 / MPEG-4 1080P 30fps 解码，H.264 1080P 30fps 编码                               |
| 扩展接口     | EXT 2.54-14P 扩展总线，1x HY2.0-4P 接口（I2C / UART 可切换，5V 输出最大电流 < 500mA） |
| USB 接口     | 1x USB-A 2.0，2x USB Type-C 2.0，支持 Host / Slave 切换及 USB OTG                     |
| USB 拓展芯片 | GL852G-OHY60 USB 2.0 Hub                                                              |
| 电池计量     | BQ27220YZFR                                                                           |
| 待机功耗     | 2.5W                                                                                  |
| 内置电池     | DC 3.7V@ 1750mAh 集成 NTC                                                             |
| 电源         | 供电 / 充电建议 5V @ 2A                                                               |
| 产品尺寸     | 84.0 x 54.0 x 23.1mm                                                                  |
| 产品重量     | Work in progress                                                                      |
| 包装尺寸     | Work in progress                                                                      |
| 毛重         | Work in progress                                                                      |

## 操作说明

### 设备供电

## 原理图

- [CardputerZero 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1243/C154-CardputerZERO_SCH_V0.6.1_20260702.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1243/C154-CardputerZERO_SCH_V0.6.1_20260702_page_01.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1243/C154-CardputerZERO_SCH_V0.6.1_20260702_page_02.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1243/C154-CardputerZERO_SCH_V0.6.1_20260702_page_03.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1243/C154-CardputerZERO_SCH_V0.6.1_20260702_page_04.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1243/C154-CardputerZERO_SCH_V0.6.1_20260702_page_05.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1243/C154-CardputerZERO_SCH_V0.6.1_20260702_page_06.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1243/C154-CardputerZERO_SCH_V0.6.1_20260702_page_07.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1243/C154-CardputerZERO_SCH_V0.6.1_20260702_page_08.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1243/C154-CardputerZERO_SCH_V0.6.1_20260702_page_09.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1243/C154-CardputerZERO_SCH_V0.6.1_20260702_page_10.png">
</SchViewer>

## 管脚映射

### Display

| CM0      | G10  | G11  | G25 | G8  | G5  |
| -------- | ---- | ---- | --- | --- | --- |
| ST7789v3 | MOSI | SCLK | DC  | CS  | TE  |

| ST7789v3 | LCD_RST       | BL           |
| -------- | ------------- | ------------ |
| M5IOE1   | PYG12_LCD_RST | PYG10_BL_PWM |

通过 `M5IOE1` 拓展芯片的 `PYG12_LCD_RST` 控制屏幕复位, `PYG10_BL_PWM` 控制屏幕背光。

### Audio

| CM0          | G20_I2S_DIN | G19_I2S_LRCK | G18_I2S_BLCK | G21_I2S_DOUT | G2_I2C1_SDA | G3_I2C1_SCL |
| ------------ | ----------- | ------------ | ------------ | ------------ | ----------- | ----------- |
| ES8389(0x10) | DOUT        | LRCK         | BCLK         | MCLK/DIN     | SDA         | SCL         |

| CM0     | G24 |
| ------- | --- |
| AW8737A | EN  |

| CM0             | G17    |
| --------------- | ------ |
| 3.5mm Headphone | HP_DET |

3.5mm 音频输入/输出接口具备插入检测功能。当 `HP_DET` 检测到耳机插头接入时，系统自动切换输出线路；未插入耳机时，将启用 **AW8737A** 扬声器功放。功放使能信号可由 **CM0 的 G24 引脚** 进行控制。

### USB 2.0

CardputerZero 将 CM0 内部的 USB 接口资源，通过 USB Hub 集线器的方式进行了拓展。实现了多路 USB 接口，以太网接口功能。

机身左侧提供了一个 Host / Slave 物理切换开关。使用 Slave 模式时候将断开 USB Hub 芯片连接， 此时，左侧的 USB-A , USB Type-C 接口，以及顶部 EXT 2.54-14P 拓展总线的 HAT-P0/P1 USB 接口，以太网接口将无法使用。

- Slave 模式：
  - CM0 USB 连接至机身右侧 USB Type-C 接口
- Host 模式：
  - CM0 USB 连接至内部 USB Hub, 经过 USB Hub 进一步拓展出 4 路 USB 接口。
  - USB Hub 拓展出的 USB1 经过 USB-ETH 芯片拓展出以太网接口功能。
  - USB Hub 拓展出的 USB2 ~ 4 分别用于，USB-A , USB Type-C 接口，以及顶部 EXT 2.54-14P 拓展总线的 HAT-P0/P1 USB 接口。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1243/cardputerzero_usb_sch_01.png" width="70%">

### HMI

| CM0                           | G2_I2C1_SDA | G3_I2C1_SCL | G27    |
| ----------------------------- | ----------- | ----------- | ------ |
| Keyboard - TCA8418RTWR (0x34) | SDA         | SCL         | KB_INT |
| IMU - BMI270 (0x68)           | SDA         | SCL         |        |
| RTC - RX8130CE (0x32)         | SDA         | SCL         |        |

| BMI270        | BMI_SDA | BMI_SCL |
| ------------- | ------- | ------- |
| BMM150 (0x10) | SDA     | SCL     |

### Power Control

| CM0           | G4          |
| ------------- | ----------- |
| GROVE_FUNC_SW | I2C/UART_SW |

| CM0    | G6     |
| ------ | ------ |
| SWITCH | SW_DET |

`G6_SW_DET` 用于读取开关检测信号。

### M5IOE1

| CM0           | G2_I2C1_SDA | G3_I2C1_SCL | G16  |
| ------------- | ----------- | ----------- | ---- |
| M5IOE1 (0x4F) | SDA         | SCL         | NRST |

- 电源状态

| M5IOE1 | PYG2   | PYG4     | PYG5    | PYG14  |
| ------ | ------ | -------- | ------- | ------ |
| POWER  | HW_DET | GROVE_EN | PWR_DET | PWR_EN |

- 外设复位

| M5IOE1             | PYG3       | PYG6   |
| ------------------ | ---------- | ------ |
| KEYBOARD & USB_HUB | KB_HUB_RST |        |
| MIC                |            | MIC_SW |

`PYG3_KB_HUB_RST` 为键盘控制器 `TCA8418RTWR` 与 USB Hub `GL852G-OHY60` 的共用复位控制信号。

`PYG6_MIC_SW` 用于 3.5mm TRRS 接口的麦克风通道切换，可在 `CTIA / OMTP` 标准间切换。

| PYG6_MIC_SW | Standard |
| ----------- | -------- |
| LOW         | CTIA     |
| HIGH        | OMTP     |

- HAT P0/P1 功能切换

| M5IOE1 | PYG1        |
| ------ | ----------- |
| SW     | PYG1_HAT_SW |

| M5IOE1 | PYG13        |
| ------ | ------------ |
| HAT_EN | PYG13_HAT_EN |

`PYG13_HAT_EN` 用于 HAT 接口使能控制。

| PYG13_HAT_EN | HAT PORT POWER |
| ------------ | -------------- |
| LOW          | OFF            |
| HIGH         | ON             |

- CAPS LOCKS 指示灯

| M5IOE1   | PYG8      | PYG9   | PYG11   |
| -------- | --------- | ------ | ------- |
| KEY_LED1 | SHIFT_LED |        |         |
| KEY_LED2 |           | FN_LED |         |
| KEY_LED3 |           |        | SYM_LED |

### IR TX & RX

| CM0 | G12   | G13   |
| --- | ----- | ----- |
| IR  | IR_TX | IR_RX |

### HY2.0-4P

::grove-table
| HY2.0-4P   | Black | Red | Yellow                     | White                      |
| ---------- | ----- | --- | -------------------------- | -------------------------- |
| UART / I2C | GND   | 5V  | G14_UART_TXD / G2_I2C1_SDA | G15_UART_RXD / G3_I2C1_SCL |
::

通过 `CM0` 的 `G4_I2C/UART_SW` 控制电子开关切换 HY2.0-4P 接口功能。默认功能为 `UART`。

| G4_I2C/UART_SW | GROVE FUNC |
| -------------- | ---------- |
| LOW            | UART       |
| HIGH           | I2C1       |

通过 `M5IOE1` 的 `PYG4_GROVE_EN` 使能控制接口 5V 输出。 (最大供电电流 < 500mA)

### EXT 2.54-14P

::m5-bus-table
| FUNC           | PIN    | LEFT | RIGHT | PIN   | FUNC     |
| -------------- | ------ | ---- | ----- | ----- | -------- |
| USB4_D_P / G26 | HAT_P0 | 1    | 2     | 5VIN  |          |
| USB4_D_N / G23 | HAT_P1 | 3    | 4     | GND   |          |
|                | G22    | 5    | 6     | 5VOUT |          |
| SPI0_CLK       | G11    | 7    | 8     | G2    | I2C1_SDA |
| SPI0_MOSI      | G10    | 9    | 10    | G3    | I2C1_SCL |
| SPI0_MISO      | G9     | 11   | 12    | G15   | UART_RXD |
| SPI0_CS1       | G7     | 13   | 14    | G14   | UART_TXD |
::

通过 `M5IOE1` 拓展芯片的 `PYG1_HAT_SW` 可控制 `HAT_P0，HAT_P1` 引脚切换 `USB / GPIO` 功能。默认功能为 `GPIO`。

| PYG1_HAT_SW | EXT HAT_P0/P1 FUNC |
| ----------- | ------------------ |
| LOW         | GPIO26 / GPIO23    |
| HIGH        | USB Hub - USB4     |

## 外观贴纸

- [CardputerZero 贴纸设计文件 CDR](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1243/CardputerZero_Labels.zip)

## 软件开发

### 快速上手

- [CardputerZero 镜像烧录](/zh_CN/guide/linux/cardputerzero/image)
- [CardputerZero ADB 连接调试](/zh_CN/guide/linux/cardputerzero/adb)
- [CardputerZero 应用开发模板](https://github.com/CardputerZero/Template)

### SDK

coming soon...

### Kernel

coming soon...

## 产品对比

::compare-table
| 产品对比项          | [CardputerZero](/zh_CN/CardputerZero) ![CardputerZero](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1243/C154-CardputerZero-main-pictures_04.jpg) | [CardputerZero-Lite](#todo) ![CardputerZero-Lite](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/coming-soon.png) |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| 核心                | Raspberry Pi CM0                                                                                                                                      | Raspberry Pi CM0                                                                                                         |
| Wi-Fi & BT          | ✅                                                                                                                                                     | ✅                                                                                                                        |
| 红外发射 + 接收     | ✅                                                                                                                                                     | ✅                                                                                                                        |
| 8MP 摄像头          | ✅                                                                                                                                                     | ❌                                                                                                                        |
| IMU BMI270 + BMM150 | ✅                                                                                                                                                     | ❌                                                                                                                        |
| 标配 32GB microSD   | ✅                                                                                                                                                     | ❌                                                                                                                        |
::
