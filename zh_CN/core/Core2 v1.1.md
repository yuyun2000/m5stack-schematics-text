# Core2 v1.1

<span class="product-sku">SKU:K010-V11</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/Core2 v1.1/img-1a949091-da2c-4fbb-bf4f-bce108cb43ec.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/Core2 v1.1/img-1ee68d74-996c-430b-acdf-45591a31e3e9.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/Core2 v1.1/img-f43dd27e-347d-49f6-a4ce-c28d2a7e013b.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/Core2 v1.1/img-a2f506a3-abd1-466c-8a05-6b79eff967c3.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/Core2 v1.1/img-4ff57e17-84db-4386-bc77-040a792972cb.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/Core2 v1.1/img-e2847063-4866-4a02-b08a-0fd991c757d4.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/Core2 v1.1/img-e68e1a0a-e0bc-4a80-a25a-d6e749d296a0.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/Core2 v1.1/img-6bd39535-26f9-4360-a88b-3537bd73b607.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/Core2 v1.1/img-0c2e243c-4e58-43ce-8c35-3dd2dbda427e.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/486/K010-V11-weight.jpg">
</PictureViewer>

## 描述

**Core2 v1.1** 是 M5Stack 开发套件系列中第二代主机的迭代版本，在原有一代主机基础上对功能进一步加强，迭代为电源管理芯片为 AXP2101+INA3221 的方案，硬件功能更加齐全，添加了 RTC 电池，满足低功耗应用需求，和精准计时功能需求。其核心主控配备了 ESP32-D0WDQ6-V3，具有两个可以单独控制的 Xtensa® 32-bit LX6 处理器，主频高达 240Mhz，支持 Wi-Fi 功能，板载 16MB Flash 与 8MB PSRAM，可通过 TYPE-C 接口下载程序，强劲的配置满足复杂应用的资源开销。正面搭载一块 2.0 寸一体化电容式触摸屏，为用户带来更流畅的人机交互体验。

机身内置震动马达，可提供触觉回馈和震动提醒功能。内建的 RTC 模块和专为 RTC 供电的电池，可提供精准计时功能。电源部分搭载 AXP2101 电源管理芯片可有效控制机身功耗，内置蓝色电源指示灯。同时机身内配备了 TF-card (microSD) 卡槽与扬声器，为了保证获得更高质量的声音效果，采用 I2S 数字音频接口的功放芯片，能有效防止信号失真。在机身的左侧和底部配有独立的电源按键与重启 (RST) 按键，屏幕正面的 3 个圆点属于触摸屏的一部分，可通过编写程序设置热区映射为 3 个虚拟按键。机身背部的扩展小板集成 6 轴 IMU 传感器与麦克风。

## 教程 & 快速上手

learn>| ![UiFlow](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/uiflow1.0_banner_01.png) | [UiFlow](/zh_CN/uiflow/m5core2/program) | 本教程介绍如何通过 UiFlow 图形化编程平台控制 Core2 v1.1 设备。 |

learn>| ![UiFlow2](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/uiflow2.0_banner_01.png) | [UiFlow2](/zh_CN/uiflow2/m5core2/program) | 本教程介绍如何通过 UiFlow2 图形化编程平台控制 Core2 v1.1 设备。 |

learn>| ![Arduino IDE](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/arduino_banner_01.png) | [Arduino IDE](/zh_CN/arduino/m5core2/program) | 本教程介绍如何通过 Arduino IDE 编程控制 Core2 v1.1 设备。 |

## 注意事项

- Core2 V1.1 与 M5 模块进行堆叠的时候，您需要拆卸 Core2 V1.1 的电池底部，如果需要保持底座的 I2S 麦克风，IMU 和电池功能并同时堆叠其他模块，则建议使用[M5GO Bottom2](/zh_CN/base/m5go_bottom2)。Core2 V1.1 的 PCB 板上预留了 CH910F 芯片的接口，与锂电池接口。

- Core2 V1.1 自带的震动马达与 M5 Base 系列底座在结构上存在干涉，为防止损坏设备，请勿将 Core2 V1.1 与 M5 Base 系列功能底座堆叠使用。

- 部分屏幕边缘会存在触摸非线性的问题，你可以尝试使用 [M5Tool](https://github.com/m5stack/M5Tools) 来升级屏幕固件解决此问题。

## 产品特性

- 基于 ESP32 开发，支持 Wi-Fi
- 16MB Flash，8MB PSRAM
- 内置扬声器，电源指示灯，震动马达，RTC，I2S 功放，电容式触摸屏幕，电源键，复位按键
- microSD 插槽
- 内置锂电池，配备电源管理芯片
- 独立小板内置 6 轴 IMU，PDM 麦克风
- M5-Bus 总线接口
- 开发平台
  - UiFlow1
  - UiFlow2
  - Arduino IDE
  - ESP-IDF
  - PlatformIO

## 包装内容

- 1 x Core2 V1.1
- 1 x USB Type-C 连接线 (20cm)
- 1 x 内六角扳手 L 形 2.0mm (适配 M2.5 螺丝)

## 应用场景

- 物联网控制器
- STEM 教育
- DIY 作品
- 智能家居设备

## 规格参数

| 规格                | 参数                                                       |
| ------------------- | ---------------------------------------------------------- |
| SoC                 | ESP32-D0WDQ6-V3@双核处理器，主频 240MHz                    |
| DMIPS               | 600                                                        |
| SRAM                | 520KB                                                      |
| Flash               | 16MB                                                       |
| PSRAM               | 8MB                                                        |
| Wi-Fi               | 2.4 GHz Wi-Fi                                              |
| 输入电压            | 5V@500mA                                                   |
| 主机接口            | USB Type-C x 1，GROVE (I2C+I/O+UART) x 1                   |
| LED                 | 蓝色电源指示灯                                             |
| 按键                | 电源键、RST 键、屏幕虚拟按键 \* 3                          |
| 震动提醒            | 震动马达                                                   |
| IPS LCD 屏幕        | 2.0"@320 x 240 ILI9342C                                    |
| 电容式触摸屏 IC     | FT6336U                                                    |
| 扬声器功放          | 1W (尺寸：0928)                                            |
| 麦克风              | SPM1423                                                    |
| I2S 功放            | NS4168                                                     |
| IMU                 | MPU6886                                                    |
| RTC                 | BM8563                                                     |
| PMU                 | AXP2101                                                    |
| 电流计              | INA3221                                                    |
| USB 芯片            | CH9102F                                                    |
| DC-DC 升压          | SY7088                                                     |
| 锂电池              | 500mAh @ 3.7V                                              |
| 天线                | 2.4G 3D 天线                                               |
| 工作温度            | 0 ~ 60°C                                                   |
| 底座螺丝规格        | 内六角沉头 M3                                              |
| 内部 PCB 板预留接口 | 电池接口（规格：1.25mm-2P）USB 线路接口（规格：1.25mm-4P） |
| 外壳材质            | Plastic ( PC )                                             |
| 产品尺寸            | 54.0 x 54.0 x 16.5mm                                       |
| 产品重量            | 45.1g                                                      |
| 包装尺寸            | 80.0 x 59.9 x 21.6mm                                       |
| 毛重                | 74.3g                                                      |

## 操作说明

### 开关机操作

- 开机：单击左侧电源键
- 关机：长按 4 秒左侧电源键
- 复位： 单击底侧 RST 按键

### IMU 三轴方向示意图

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/486/IMU-Core2-v1.1.jpg" width="70%">

## 原理图

- [Core2 v1.1 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/486/Sch_Core2_v1.1_2023-07-20.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/486/Sch_Core2_v1.1_2023-07-20_sch_01.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/486/Sch_Core2_v1.1_2023-07-20_sch_02.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/486/Sch_Core2_v1.1_2023-07-20_sch_03.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/486/Sch_Core2_v1.1_2023-07-20_sch_04.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/486/Sch_Core2_v1.1_2023-07-20_sch_05.png">
</SchViewer>

## 管脚映射

### LCD & microSD (LCD :320x240)

| ESP32-D0WDQ6-V3 | G38  | G23  | G18 | G5  | G15 |
| --------------- | ---- | ---- | --- | --- | --- |
| ILI9342C        | MISO | MOSI | SCK | CS  | DC  |

| AXP2101  | AXP_ALDO2 | AXP_BLDO1 | AXP_ALDO4 |
| -------- | --------- | --------- | --------- |
| ILI9342C | RST       | BL        | PWR       |

### microSD

| ESP32-D0WDQ6-V3 | G38  | G23  | G18 | G4  |
| --------------- | ---- | ---- | --- | --- |
| microSD         | MISO | MOSI | SCK | CS  |

### CAP.TOUCH (I2C Addr: 0x38)

| ESP32-D0WDQ6-V3 | G21 | G22 | G39 |
| --------------- | --- | --- | --- |
| FT6336U (0x38)  | SDA | SCL | INT |

| AXP2101 | AXP_ALDO2 |
| ------- | --------- |
| FT6336U | RST       |

### Mic & NS4168(Speaker)

| ESP32-D0WDQ6-V3 | G12  | G0   | G2   | G34  |
| --------------- | ---- | ---- | ---- | ---- |
| NS4168          | BCLK | LRCK | DATA |      |
| Mic             |      | CLK  |      | DATA |

| AXP2101 | AXP_ALDO3 |
| ------- | --------- |
| NS4168  | SPK_EN    |

### AXP Power Indicator Light

| AXP2101         | VRTC | DLDO1 |
| --------------- | ---- | ----- |
| Bule LED        | Vcc  |       |
| Vibration motor |      | Vcc   |

### RTC

| ESP32-D0WDQ6-V3 | G21 | G22 | \   |
| --------------- | --- | --- | --- |
| BM8563 (0x51)   | SDA | SCL |     |

| AXP2101 | AXP_IRQ |
| ------- | ------- |
| BM8563  | INT     |

### IMU(3-axis gyroscope & 3-axis accelerometer)

| ESP32-D0WDQ6-V3 | G21 | G22 |
| --------------- | --- | --- |
| MPU6886 (0x68)  | SDA | SCL |

### USB to serial chip

| ESP32-D0WDQ6-V3 | G1  | G3  |
| --------------- | --- | --- |
| CH9102F         | RXD | TXD |

### Internal I2C connection

| ESP32-D0WDQ6-V3 | G21 | G22 |
| --------------- | --- | --- |
| MPU6886         | SDA | SCL |
| AXP2101 (0x34)  | SDA | SCL |
| BM8563          | SDA | SCL |
| FT6336U         | SDA | SCL |
| INA3221 (0x40)  | SDA | SCL |

### HY2.0-4P

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | G32    | G33   |
| PORT.B   | GND   | 5V  | G26    | G36   |
| PORT.C   | GND   | 5V  | G14    | G13   |
::

### M5-Bus

::m5-bus-table
| FUNC       | PIN | LEFT | RIGHT | PIN | FUNC       |
| ---------- | --- | ---- | ----- | --- | ---------- |
|            | GND | 1    | 2     | G35 | ADC        |
|            | GND | 3    | 4     | G36 | ADC        |
|            | GND | 5    | 6     | RST | EN         |
| MOSI       | G23 | 7    | 8     | G25 | DAC        |
| MISO       | G38 | 9    | 10    | G26 | DAC        |
| SCK        | G18 | 11   | 12    | 3V3 |            |
| RXD0       | G3  | 13   | 14    | G1  | TXD0       |
| RXD2       | G13 | 15   | 16    | G14 | TXD2       |
| Int SDA    | G21 | 17   | 18    | G22 | Int SCL    |
| PORT.A SDA | G32 | 19   | 20    | G33 | PORT.A SCL |
| GPIO       | G27 | 21   | 22    | G19 | GPIO       |
| I2S_DOUT   | G2  | 23   | 24    | G0  | I2S_LRCK   |
|            | NC  | 25   | 26    | G34 | I2S_DATA   |
|            | NC  | 27   | 28    | 5V  |            |
|            | NC  | 29   | 30    | BAT |            |
::

### Core2 v1.1 BUS（与 M5Stack 对比）

<img class="png" src="https://www.gwendesign.com/kb/m5stack/img/M5StackM5Core2GPIO.png" width = "70%">

## 尺寸图

<img alt="module size" src="https://static-cdn.m5stack.com/resource/docs/products/core/Core2 v1.1/img-7deeba31-ce3d-4118-8351-e3f787147e97.jpg" width="100%" />

## 结构文件

- [Core2 v1.1 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/K010-V11_Core2_v1.1/Structures)

## 数据手册

- [ESP32](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/644/esp32_datasheet_cn.pdf)
- [FT6336U](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/Ft6336GU_Firmware%20%E5%A4%96%E9%83%A8%E5%AF%84%E5%AD%98%E5%99%A8_20151112.xlsx)
- [NS4168](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/NS4168_CN_datasheet.pdf)
- [MPU6886](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/MPU-6886-000193%2Bv1.1_GHIC_en.pdf)
- [ILI9342C](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/ILI9342C-ILITEK.pdf)
- [SPM1423](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/SPM1423HM4H-B_datasheet_en.pdf)
- [BM8563](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/BM8563_V1.1_cn.pdf)
- [SY7088](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/SY7088-Silergy.pdf)
- [AXP2101](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/Core2%20v1.1/axp2101.pdf)
- [1027DC Motor](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/1027RFN01-33d.pdf)
- [INA3221](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/Core2%20v1.1/ina3221.pdf)

## 软件开发

### Arduino

- [Core2 v1.1 Arduino 快速上手](/zh_CN/arduino/m5core2/program)
- [Core2 v1.1 Arduino 驱动库](https://github.com/m5stack/M5Core2)
- [Core2 v1.1 Arduino M5GFX 驱动库](https://github.com/m5stack/M5GFX)
- [Core2 v1.1 Arduino M5Unified 驱动库](https://github.com/m5stack/M5Unified)

### UiFlow1

- [Core2 v1.1 UiFlow1 快速上手](/zh_CN/uiflow/m5core2/program)

### UiFlow2

- [Core2 v1.1 UiFlow2 快速上手](/zh_CN/uiflow2/m5core2/program)

### PlatformIO

```
[env:m5stack-core2]
platform = espressif32@6.12.0
board = m5stack-core2
framework = arduino
upload_speed = 921600
monitor_speed = 115200
board_build.partitions = default_16MB.csv
build_type = debug
build_flags =
    -DBOARD_HAS_PSRAM
    -DCORE_DEBUG_LEVEL=5
lib_deps =
    M5Unified=https://github.com/m5stack/M5Unified
```

### PlatformIO

```bash
[env:m5stack-core2]
platform = espressif32@6.7.0
board = m5stack-core-esp32
framework = arduino
upload_speed = 1500000
monitor_speed = 115200
build_flags =
    -DBOARD_HAS_PSRAM
    -mfix-esp32-psram-cache-issue
    -DCORE_DEBUG_LEVEL=5
lib_deps =
    M5Unified=https://github.com/m5stack/M5Unified
```

### Easyloader

| Easyloader                         | 下载链接                                                                                                                         | 备注 |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | ---- |
| Core2 v1.1 Factory Test Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/Core2%20v1.1/Core2%20v1.1%20FactoryTest.exe) | /    |

### USB 驱动

点击下方连接下载匹配操作系统的驱动程序。目前存在两种驱动芯片版本，CP34X（适用于**CH9102**版本）驱动程序压缩包。在解压压缩包后，选择对应操作系统位数的安装包进行安装。(若您不确定您的设备所使用的 USB 芯片，可同时安装两种驱动。**CH9102_VCP_SER_MacOS v1.7**在安装过程中，可能出现报错，但实际上已经完成安装，忽略即可。) 在使用时，若出现无法正常下载程序 (提示超时或者 Failed to write to target RAM) 的情况，可尝试重新安装设备驱动。

| 驱动名称                  | 适用驱动芯片 | 下载链接                                                                                             |
| ------------------------- | ------------ | ---------------------------------------------------------------------------------------------------- |
| CH9102_VCP_SER_Windows    | CH9102       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CH9102_VCP_SER_Windows.exe) |
| CH9102_VCP_SER_MacOS v1.7 | CH9102       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CH9102_VCP_MacOS_v1.7.zip)  |

## 相关视频

本案例将执行硬件运行测试扬声器，Wi-Fi，按钮，加速度计，microSD，屏幕等。

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Core/CORE2%20.mp4" type="video/mp4"></video>

## 产品对比

如需对比控制器系列产品信息，可访问[产品选型表](/zh_CN/products_selector/m5core_compare?select=K010-V11)，勾选目标产品即可获取对比结果。选型表涵盖核心参数、功能特性等关键信息，支持多产品同步比对。

### AXP2101（Core2 v1.1）和 AXP192（Core2）参数对比

| 特性             | AXP2101（Core2 v1.1） | AXP192（Core2） |
| ---------------- | --------------------- | --------------- |
| 电池电压         | 0.7V ~ 4.2V           | 0.7V ~ 4.2V     |
| 电池充电电流     | 100mA                 | 500mA           |
| 电池充电效率     | 94%                   | 90%             |
| 电池充电终止电流 | 10mA                  | 50mA            |
| 电池放电效率     | 96%                   | 95%             |
| 电源输出电流     | 300mA                 | 500mA           |
| 电源输出效率     | 95%                   | 90%             |

### Core2 和 Core2 v1.1 的区别

| 对比项         | Core2                      | Core2 v1.1                          |
| -------------- | -------------------------- | ----------------------------------- |
| 电源管理方案   | 仅 AXP192 芯片             | AXP2101 + INA3221 组合方案          |
| 电源指示灯颜色 | 绿色                       | 蓝色                                |
| RTC 计时功能   | 无独立供电电池，断电后失准 | 配备 RTC 芯片供电电池，断电精准计时 |

\#>AXP192 和 AXP2101 的 ID 不同，程序以此作为区分版本的标志。

## 版本变更

| 上市日期 | 产品变动       | 备注                                                                               |
| -------- | -------------- | ---------------------------------------------------------------------------------- |
| 2023.11  | Core2 v1.1     | 更改 PMU 电源管理芯片为 AXP2101+INA3221、新增 RTC 供电电池、电源指示灯调整为蓝色   |
| /        | 首次发售 Core2 | /                                                                                  |