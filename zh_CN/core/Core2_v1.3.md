# Core2 v1.3

<span class="product-sku">SKU:K010-V13</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1231/K010-V13-Core2-v1.3-main-pictures_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1231/K010-V13-Core2-v1.3-main-pictures_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1231/K010-V13-Core2-v1.3-main-pictures_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1231/K010-V13-Core2-v1.3-main-pictures_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1231/K010-V13-Core2-v1.3-main-pictures_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1231/K010-V13-Core2-v1.3-main-pictures_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1231/K010-V13-Core2-v1.3-main-pictures_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1231/K010-V13-Core2-v1.3-main-pictures_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1231/K010-V13-Core2-v1.3-main-pictures_09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1231/K010-V13-Core2-v1.3-main-pictures_10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1231/K010-V13-Core2-v1.3-main-pictures_11.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1231/K010-V13-Core2-v1.3-main-pictures_12.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1231/K010-V13-Core2-v1.3-main-pictures_13.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1231/K010-V13-Core2-v1.3-main-pictures_14.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1231/K010-V13-weight.jpg">
</PictureViewer>

## 描述

Core2 v1.3 是一款面向物联网应用的高集成度主控。内部集成 ESP32-D0WDQ6-V3 核心主控， 搭载 Xtensa 双核 32 位 LX6 处理器，主频 240 MHz。
板载 16MB Flash、8MB PSRAM，并支持 2.4 GHz Wi-Fi。 该版本基于 Core2 v1.0 迭代，沿用 AXP192 电源管理芯片，在保持整机架构与兼容性的前提下，将背部扩展小板上的 6 轴 IMU 升级为 BMI270，以提升姿态检测精度与综合性能。人机交互方面，设备采用 2.0" 彩色电容触控屏幕；屏幕正面三处圆点为触摸热区，可编程映射为 3 颗虚拟按键。内置震动马达，便于触觉反馈。存储与音频方面，板载 microSD 卡槽与扬声器，音频经 I2S 数字接口与 NS4168 功放输出，有利于降低失真、改善听感。设备内置 RTC 实时时钟芯片，500mAh 锂电池。 背部扩展小板集成 BMI270 六轴 IMU 与麦克风，可实现姿态感知与音频采集功能。本产品适用于物联网终端、人机交互设备、姿态检测及嵌入式多功能开发等场景。

## 教程 & 快速上手

learn>| ![UiFlow](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/uiflow1.0_banner_01.png) | [UiFlow](/zh_CN/uiflow/m5core2/program) | 本教程介绍如何通过 UiFlow 图形化编程平台控制 Core2 设备。 |

learn>| ![UiFlow2](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/uiflow2.0_banner_01.png) | [UiFlow2](/zh_CN/uiflow2/m5core2/program) | 本教程介绍如何通过 UiFlow2 图形化编程平台控制 Core2 设备。 |

learn>| ![Arduino IDE](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/arduino_banner_01.png) | [Arduino IDE](/zh_CN/arduino/m5core2/program) | 本教程介绍如何通过 Arduino IDE 编程控制 Core2 设备。 |

### 注意事项

- Core2 v1.3 自带的震动马达与 Base 系列底座在结构上存在干涉，为防止损坏设备，请勿将 Core2 v1.3 与 Base 系列功能底座堆叠使用。
- Core2 v1.3 与 M5 模块进行堆叠的时候，您需要拆卸 Core2 v1.3 的电池底部，如果需要保持底座的 I2S 麦克风，IMU 和电池功能并同时堆叠其他模块，则建议使用[M5GO Bottom2](/zh_CN/base/m5go_bottom2)。
- 部分屏幕边缘会存在触摸非线性的问题，可尝试使用[M5Tool](https://github.com/m5stack/M5Tools) 来升级屏幕固件解决此问题。

## 产品特性

- ESP32-D0WDQ6-V3 核心主控:
  - 16MB Flash
  - 8MB PSRAM
  - 2.4 GHz Wi-Fi
- 人机交互
  - 2.0" 彩色电容触控屏幕
  - 内置扬声器
  - 震动马达
- 独立外设拓展小板
  - BMI270, 6 轴 IMU
  - PDM 麦克风
- AXP192 电源管理
- RTC 时钟
- 内置 500mAh 锂电池
- HY2.0-4P 拓展接口
- microSD 插槽
- 开发平台
  - UiFlow1
  - UiFlow2
  - Arduino IDE
  - ESP-IDF
  - PlatformIO

## 包装内容

- 1 x Core2 v1.3
- 1 x USB Type-C 连接线 (20cm)
- 1 x 内六角扳手 L 形 2.0mm (适配 M2.5 螺丝)

## 应用场景

- 物联网控制器
- DIY 作品
- 智能家居设备

## 规格参数

| 规格                | 参数                                                                     |
| ------------------- | ------------------------------------------------------------------------ |
| SoC                 | ESP32-D0WDQ6-V3@双核处理器，主频 240MHz                                  |
| Flash               | 16MB                                                                     |
| PSRAM               | 8MB                                                                      |
| Wi-Fi               | 2.4 GHz Wi-Fi                                                            |
| 输入电压            | 5V @ 500mA                                                               |
| 主机接口            | USB Type-C x 1，GROVE (I2C+I/O+UART) x 1                                 |
| LED                 | 绿色电源指示灯                                                           |
| 按键                | 电源键、RST 键、屏幕虚拟按键 x 3                                         |
| 震动提醒            | 震动马达                                                                 |
| IPS LCD 屏幕        | 2.0"@320 x 240 ILI9342C                                                  |
| 电容式触摸屏 IC     | FT6336U                                                                  |
| 麦克风              | SPM1423                                                                  |
| I2S 功放            | NS4168                                                                   |
| IMU                 | BMI270                                                                   |
| RTC                 | BM8563                                                                   |
| PMU                 | AXP192                                                                   |
| USB-TTL             | CH9102F                                                                  |
| 锂电池              | 3.7V @ 500mAh                                                            |
| RTC 电池            | MS412FE 3V 1.0mAh 可充电微型锂电池                                       |
| 充电参数            | 充电电流：0.219A<br/>充满后电流（关机）:0.055A<br/>充满电（开机）:0.147A |
| 天线                | 2.4G 3D 天线                                                             |
| 工作温度            | 0 ~ 60°C                                                                 |
| 底座螺丝规格        | 内六角沉头 M3                                                            |
| 内部 PCB 板预留接口 | 电池接口（规格：1.25mm-2P）USB 线路接口（规格：1.25mm-4P）               |
| 产品尺寸            | 54.0 x 54.0 x 16.5mm                                                     |
| 产品重量            | 58.8g                                                                    |
| 包装尺寸            | 80.0 x 59.9 x 21.6mm                                                     |
| 毛重                | 88.2g                                                                    |

## 操作说明

### 开关机

- 开机：单击左侧电源键
- 关机：长按左侧电源键
- 复位：单击底侧 RST 按键

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1231/Core2_v1.3_operate.gif" width="40%">

### 板载预留接口

Core2 v1.3 的 PCB 板上预留了 USB-TTL 芯片接口以及锂电池接口。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1231/ext-port-pin.png" width="40%">

### IMU 三轴方向示意图

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1231/IMU-Core2-v1.3.jpg" width="70%">

## 认证信息

- CE/MIC/FCC/RCM
- IEC62133

## 原理图

- [Core2 v1.3-核心部分 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/644/CORE2_V1.0_SCH.pdf)
- [Core2 v1.3-拓展板部分 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/486/core2_v1.3_SCH_2025_11_14_09_40_33.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/644/CORE2_V1.0_SCH_page_01.png" width="80%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/486/core2_v1.3_SCH_2025_11_14_09_40_33_page_01.png" width="80%">
</SchViewer>

## 管脚映射

### LCD

| ESP32-D0WDQ6-V3 | G38  | G23  | G18 | G5  | G15 |
| --------------- | ---- | ---- | --- | --- | --- |
| ILI9342C        | MISO | MOSI | SCK | CS  | DC  |

| AXP192   | AXP_IO4 | AXP_DC3 | AXP_LDO2 |
| -------- | ------- | ------- | -------- |
| ILI9342C | RST     | BL      | PWR      |

### microSD

| ESP32-D0WDQ6-V3 | G38  | G23  | G18 | G4  |
| --------------- | ---- | ---- | --- | --- |
| microSD         | MISO | MOSI | SCK | CS  |

### Touch

| ESP32-D0WDQ6-V3 | G21 | G22 | G39 |
| --------------- | --- | --- | --- |
| FT6336U (0x38)  | SDA | SCL | INT |

| AXP192  | AXP_IO4 |
| ------- | ------- |
| FT6336U | RST     |

### Audio

| ESP32-D0WDQ6-V3 | G12  | G0   | G2   | G34  |
| --------------- | ---- | ---- | ---- | ---- |
| NS4168          | BCLK | LRCK | DATA |      |
| SPM1423         |      | CLK  |      | DATA |

| AXP192 | AXP_IO2 |
| ------ | ------- |
| NS4168 | SPK_EN  |

### AXP 电源指示灯 & 震动马达

| AXP192          | AXP_IO1 | AXP_LDO3 |
| --------------- | ------- | -------- |
| Green LED       | VCC     |
| Vibration Motor |         | VCC      |

### RTC

| ESP32-D0WDQ6-V3 | G21 | G22 |
| --------------- | --- | --- |
| BM8563 (0x51)   | SDA | SCL |

| AXP192 | AXP_PWR |
| ------ | ------- |
| BM8563 | INT     |

### IMU（3 轴陀螺仪 + 3 轴加速计）

| ESP32-D0WDQ6-V3 | G21 | G22 |
| --------------- | --- | --- |
| BMI270 (0x68)   | SDA | SCL |

### 内部 I2C 连接

| ESP32-D0WDQ6-V3 | G21 | G22 |
| --------------- | --- | --- |
| BMI270 (0x68)   | SDA | SCL |
| AXP192 (0x34)   | SDA | SCL |
| BM8563 (0x51)   | SDA | SCL |
| FT6336U (0x38)  | SDA | SCL |

### HY2.0-4P

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | G32    | G33   |
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

## 尺寸图

- [Core2 v1.3 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1231/K010-V13_Core2_v1.3_model-size.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1231/K010-V13_Core2_v1.3_model-size_page_01.png" width="100%">

## 结构文件

- [Core2 v1.3 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/K010_Core2/Structures)

## 数据手册

- [ESP32](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/644/esp32_datasheet_cn.pdf)
- [FT6336U](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/Ft6336GU_Firmware%20%E5%A4%96%E9%83%A8%E5%AF%84%E5%AD%98%E5%99%A8_20151112.xlsx)
- [NS4168](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/NS4168_CN_datasheet.pdf)
- [BMI270](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/K128%20CoreS3/BMI270.PDF)
- [ILI9342C](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/ILI9342C-ILITEK.pdf)
- [SPM1423](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/SPM1423HM4H-B_datasheet_en.pdf)
- [BM8563](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1231/BM8563_V1.1_cn.pdf)
- [SY7088](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1231/SY7088-Silergy.pdf)
- [AXP192 datasheet](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1231/AXP192_datasheet_cn.pdf) <!--注意中英文链接不同-->
- [1027DC Motor](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/1027RFN01-33d.pdf)

## 软件开发

### Arduino

- [Core2 v1.3 Arduino 快速上手](/zh_CN/arduino/m5core2/program)
- [Core2 v1.3 Arduino 驱动库](https://github.com/m5stack/M5Core2)
- [Core2 v1.3 Arduino API](/zh_CN/arduino/m5core2/button)

### UiFlow1

- [Core2 v1.3 UiFlow1 快速上手](/zh_CN/uiflow/m5core2/program)

### UiFlow2

- [Core2 v1.3 UiFlow2 快速上手](/zh_CN/uiflow2/m5core2/program)

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

### ESP-IDF

- [Core2 v1.3 ESP-IDF BSP 使用教程](/zh_CN/esp_idf/m5core2/bsp)

### USB 驱动

请按所使用的操作系统，从下表下载并安装 **CH9102** USB 串口（VCP）驱动。安装 **CH9102_VCP_SER_MacOS v1.7** 时，安装程序可能提示报错，多为误报，驱动通常已正确安装，可忽略该提示并继续。 烧录或下载固件时出现失败、超时，或提示 `Failed to write to target RAM` 等异常时，可先尝试重新安装驱动、更换 USB 线或接口。

| 驱动名称                  | 适用驱动芯片 | 下载链接                                                                                             |
| ------------------------- | ------------ | ---------------------------------------------------------------------------------------------------- |
| CH9102_VCP_SER_Windows    | CH9102       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CH9102_VCP_SER_Windows.exe) |
| CH9102_VCP_SER_MacOS v1.7 | CH9102       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CH9102_VCP_MacOS_v1.7.zip)  |

### Easyloader

| Easyloader             | 下载链接                                                                                     | 备注 |
| ---------------------- | -------------------------------------------------------------------------------------------- | ---- |
| Core2 Factory FirmWare | [下载链接](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1231/Core2_Factory_FirmWare.exe) | /    |

### 其他

- [ESP32 formats and communication protocols](https://link.springer.com/book/10.1007/978-1-4842-9376-8)

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/core2/07c3be99c38835c886b7afc23c10083.jpg" width="80%">

> [《ESP32 formats and communication protocols》](https://link.springer.com/book/10.1007/978-1-4842-9376-8)一书分了几章介绍了 M5Stack Core2 模块。M5Stack Core2 模块集成了触摸 LCD 屏幕和 Wi-Fi 通信，麦克风和扬声器，以及加速度计和陀螺仪，使 M5Stack Core2 模块非常通用。本书使用通信协议构建项目，从将智能手表连接手机 (BLE) 到与地球上空环绕的卫星的远程通信 (LoRa) 以及设备之间的音频信号传输 (I2S)。QR 码用于通过互联网控制外部设备，而 ESP-MESH 和 ESP-NOW 协议可在没有互联网连接的情况下实现微控制器之间的通信。

## 相关视频

- Core2 v1.3 产品介绍以及功能展示

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1231/K010-V13-Core2-v1.3-video-ZH.mp4" type="video/mp4"></video>

## 产品对比

::compare-table
| Product Compare | [Core2 v1.3](/zh_CN/core/Core2_v1.3) ![Core2 v1.3](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1231/K010-V13-Core2-v1.3-main-pictures_02.webp) | [Core2 v1.1](/zh_CN/core/Core2%20v1.1) ![Core2 v1.1](https://static-cdn.m5stack.com/resource/docs/products/core/Core2%20v1.1/img-9eb726ec-5729-42c3-9cce-e06140856095.webp) | [Core2](/zh_CN/core/core2) ![Core2](https://static-cdn.m5stack.com/resource/docs/products/core/core2/core2_cover_01.webp) |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| IMU             | BMI270                                                                                                                                              | MPU6886                                                                                                                                                                     | MPU6886                                                                                                                   |
| PMIC            | AXP192                                                                                                                                              | AXP2101                                                                                                                                                                     | AXP192                                                                                                                    |
| USB-TTL         | CH9102                                                                                                                                              | CH9102                                                                                                                                                                      | CP2104/CH9102                                                                                                             |
| 电源指示灯颜色  | 绿色                                                                                                                                                | 蓝色                                                                                                                                                                        | 绿色                                                                                                                      |
::

如需对比控制器系列产品信息，可访问[产品选型表](/zh_CN/products_selector/m5core_compare?select=K010-V13)，勾选目标产品即可获取对比结果。选型表涵盖核心参数、功能特性等关键信息，支持多产品同步比对。
