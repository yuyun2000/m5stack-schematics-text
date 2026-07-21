# Core2

<span class="product-sku">SKU:K010</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/644/core2_01.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/core2/core2_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/core2/core2_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/core2/core2_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/core2/core2_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/core2/core2_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/644/K010-weight.jpg">
</PictureViewer>

## 描述

**Core2** 是 M5Stack 开发套件系列中第二代主机，在原有一代主机基础上对功能进一步加强，硬件功能更加齐全。其核心主控**Core2**配备了 **ESP32-D0WDQ6-V3**，具有两个可以单独控制的 **Xtensa® 32-bit LX6** 处理器，主频高达 240 MHz ，支持 Wi-Fi 功能，板载 **16MB Flash** 与 **8MB PSRAM**，可通过 **USB Type-C** 接口下载程序，强劲的配置满足复杂应用的资源开销。正面搭载一块 2.0 寸一体化电容式触摸屏，为用户带来更流畅的人机交互体验。

机身内置 **震动马达**，可提供 **触觉回馈** 和震动提醒功能。内建的 RTC 模块可提供精准计时功能。电源部分搭载 **AXP192** 电源管理芯片可有效控制机身功耗，内置绿色电源指示灯。<br/>同时，机身内配备了 microSD 卡槽与扬声器，为了保证获得更高质量的声音效果，采用 **I2S** 数字音频接口的 **功放芯片**，能有效防止信号失真。<br/>在机身的左侧和底部配有独立的电源按键与重启 (RST) 按键，屏幕正面的 3 个圆点属于触摸屏的一部分，可通过编写程序设置热区映射为 3 个虚拟按键。机身背部的扩展小板集成 6 轴 IMU 传感器与麦克风。

## 教程 & 快速上手

learn>| ![UiFlow](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/uiflow1.0_banner_01.png) | [UiFlow](/zh_CN/uiflow/m5core2/program) | 本教程介绍如何通过 UiFlow 图形化编程平台控制 Core2 设备。 |

learn>| ![UiFlow2](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/uiflow2.0_banner_01.png) | [UiFlow2](/zh_CN/uiflow2/m5core2/program) | 本教程介绍如何通过 UiFlow2 图形化编程平台控制 Core2 设备。 |

learn>| ![Arduino IDE](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/arduino_banner_01.png) | [Arduino IDE](/zh_CN/arduino/m5core2/program) | 本教程介绍如何通过 Arduino IDE 编程控制 Core2 设备。 |

## 注意事项

- Core2 自带的震动马达与 Base 系列底座在结构上存在干涉，为防止损坏设备，请勿将 Core2 与 Base 系列功能底座堆叠使用。
- Core2 与 M5 模块进行堆叠的时候，您需要拆卸 Core2 的电池底部，如果需要保持底座的 I2S 麦克风，IMU 和电池功能并同时堆叠其他模块，则建议使用[M5GO Bottom2](/zh_CN/base/m5go_bottom2)。CORE2 的 PCB 板上预留了 CP2104 芯片的接口，与锂电池接口。
- 部分屏幕边缘会存在触摸非线性的问题，你可以尝试使用[M5Tool](https://github.com/m5stack/M5Tools) 来升级屏幕固件解决此问题。

## 产品特性

- 基于 ESP32 开发，支持 Wi-Fi
- 16MB Flash，8MB PSRAM
- 内置扬声器，电源指示灯，震动马达，RTC，I2S 功放，电容式触摸屏幕，电源键，复位按键
- microSD 插槽
- 内置锂电池，配备电源管理芯片
- 独立小板内置 6 轴 IMU，PDM 麦克风
- M5-Bus bus socket
- 开发平台
  - UiFlow1
  - UiFlow2
  - Arduino IDE
  - ESP-IDF
  - PlatformIO

## 包装内容

- 1 x Core2
- 1 x USB Type-C 连接线 (20cm)
- 1 x 内六角扳手

## 应用场景

- 物联网控制器
- STEM 教育
- DIY 作品
- 智能家居设备

## 规格参数

| 规格                | 参数                                                                     |
| ------------------- | ------------------------------------------------------------------------ |
| SoC                 | ESP32-D0WDQ6-V3@双核处理器，主频 240MHz                                  |
| DMIPS               | 600                                                                      |
| SRAM                | 520KB                                                                    |
| Flash               | 16MB                                                                     |
| PSRAM               | 8MB Quad                                                                 |
| Wi-Fi               | 2.4 GHz Wi-Fi                                                            |
| 输入电压            | 5V@500mA                                                                 |
| 主机接口            | USB Type-C x 1，GROVE (I2C+I/O+UART) x 1                                 |
| LED                 | 绿色电源指示灯                                                           |
| 按键                | 电源键、RST 键、屏幕虚拟按键 x 3                                         |
| 震动提醒            | 震动马达                                                                 |
| IPS LCD 屏幕        | 2.0"@320 x 240 ILI9342C                                                  |
| 电容式触摸屏 IC     | FT6336U                                                                  |
| 扬声器功放          | NS4168                                                                   |
| 麦克风              | SPM1423                                                                  |
| I2S 功放            | NS4168                                                                   |
| IMU                 | MPU6886                                                                  |
| RTC                 | BM8563                                                                   |
| PMU                 | AXP192                                                                   |
| USB 芯片            | CP2104/CH9102F (两个芯片版本，功能与使用上并无差异)                      |
| DC-DC 升压          | SY7088                                                                   |
| 锂电池              | 500mAh@3.7V                                                              |
| 充电参数            | 充电电流：0.219A<br/>充满后电流（关机）:0.055A<br/>充满电（开机）:0.147A |
| 天线                | 2.4G 3D 天线                                                             |
| 工作温度            | 0 ~ 60°C                                                                 |
| 底座螺丝规格        | 内六角沉头 M3                                                            |
| 内部 PCB 板预留接口 | 电池接口（规格：1.25mm-2P）USB 线路接口（规格：1.25mm-4P）               |
| 产品尺寸            | 54.0 x 54.0 x 16.5mm                                                     |
| 产品重量            | 54.9g                                                                    |
| 包装尺寸            | 80.0 x 59.9 x 21.6mm                                                     |
| 毛重                | 100.8g                                                                   |

## 操作说明

### 开关机

- 开机：单击左侧电源键
- 关机：长按 6 秒左侧电源键
- 复位： 单击底侧 RST 按键

### IMU 三轴方向示意图

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/644/IMU-Core2.jpg" width="70%">

## 认证信息

- CE/MIC/FCC/RCM
- IEC62133

## 原理图

- [Core2-核心部分 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/644/CORE2_V1.0_SCH.pdf)
- [Core2-拓展板部分 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/644/CORE2_EXT_Board.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/644/CORE2_V1.0_SCH_page_01.png" width="80%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/644/CORE2_EXT_Board_page_01.png" width="80%">
</SchViewer>

## 管脚映射

### LCD 屏幕 & TF Card

LCD 像素：320x240

| ESP32-D0WDQ6-V3 | G38  | G23  | G18 | G5  | G15 |
| --------------- | ---- | ---- | --- | --- | --- |
| ILI9342C        | MISO | MOSI | SCK | CS  | DC  |

| AXP192   | AXP_IO4 | AXP_DC3 | AXP_LDO2 |
| -------- | ------- | ------- | -------- |
| ILI9342C | RST     | BL      | PWR      |

### microSD

| ESP32-D0WDQ6-V3 | G38  | G23  | G18 | G4  |
| --------------- | ---- | ---- | --- | --- |
| TF Card         | MISO | MOSI | SCK | CS  |

### CAP.TOUCH

| ESP32-D0WDQ6-V3 | G21 | G22 | G39 |
| --------------- | --- | --- | --- |
| FT6336U (0x38)  | SDA | SCL | INT |

| AXP192  | AXP_IO4 |
| ------- | ------- |
| FT6336U | RST     |

### 麦克风 & NS4168 功放

| ESP32-D0WDQ6-V3 | G12  | G0   | G2   | G34  |
| --------------- | ---- | ---- | ---- | ---- |
| NS4168          | BCLK | LRCK | DATA |      |
| Mic             |      | CLK  |      | DATA |

| AXP192 | AXP_IO2 |
| ------ | ------- |
| NS4168 | SPK_EN  |

### AXP 电源指示灯 & 震动马达

| AXP192          | AXP_IO1 | AXP_LDO3 |
| --------------- | ------- | -------- |
| Green LED       | Vcc     |
| Vibration motor |         | Vcc      |

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
| MPU6886 (0x68)  | SDA | SCL |

### USB 转串口下载

| ESP32-D0WDQ6-V3 | G1  | G3  |
| --------------- | --- | --- |
| CP2104/CH9102F  | RXD | TXD |

### 内部 I2C 连接

| ESP32-D0WDQ6-V3 | G21 | G22 |
| --------------- | --- | --- |
| MPU6886         | SDA | SCL |
| AXP192 (0x34)   | SDA | SCL |
| BM8563          | SDA | SCL |
| FT6336U         | SDA | SCL |

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

### Core2 BUS（与 M5Stack 对比）

<img class="png" src="https://www.gwendesign.com/kb/m5stack/img/M5StackM5Core2GPIO.png" width = "70%">

### Core2 端口说明

| PORT          | PIN    | 备注：  |
| ------------- | ------ | ------- |
| PORT-A (红色) | G32/33 | I2C     |
| PORT-B (黑色) | G26/36 | DAC/ADC |
| PORT-C (蓝色) | G13/14 | UART    |

## 尺寸图

<img alt="module size" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/core2/%E5%B0%BA%E5%AF%B8%E5%9B%BE.jpg" width="100%" />

## 结构文件

- [Core2 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/K010_Core2/Structures)

## 数据手册

- [ESP32](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/644/esp32_datasheet_cn.pdf)
- [FT6336U](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/Ft6336GU_Firmware%20%E5%A4%96%E9%83%A8%E5%AF%84%E5%AD%98%E5%99%A8_20151112.xlsx)
- [NS4168](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/NS4168_CN_datasheet.pdf)
- [MPU6886](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/MPU-6886-000193%2Bv1.1_GHIC_en.pdf)
- [ILI9342C](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/ILI9342C-ILITEK.pdf)
- [SPM1423](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/SPM1423HM4H-B_datasheet_en.pdf)
- [BM8563](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/BM8563_V1.1_cn.pdf)
- [SY7088](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/SY7088-Silergy.pdf)
- [AXP192 datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/AXP192_datasheet_en.pdf)
- [AXP192 register](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/AXP192_datasheet_cn.pdf)
- [1027DC Motor](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/1027RFN01-33d.pdf)

## 软件开发

### Arduino

- [Core2 Arduino 快速上手](/zh_CN/arduino/m5core2/program)
- [Core2 Arduino 驱动库](https://github.com/m5stack/M5Core2)
- [Core2 Arduino API](/zh_CN/arduino/m5core2/button)

### UiFlow1

- [Core2 UiFlow1 快速上手](/zh_CN/uiflow/m5core2/program)

### UiFlow2

- [Core2 UiFlow2 快速上手](/zh_CN/uiflow2/m5core2/program)

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

- [Core2 ESP-IDF BSP 使用教程](/zh_CN/esp_idf/m5core2/bsp)

### USB 驱动

点击下方连接下载匹配操作系统的驱动程序。目前存在两种驱动芯片版本，CP210X（适用于**CP2104**版本）/CP34X（适用于**CH9102**版本）驱动程序压缩包。在解压压缩包后，选择对应操作系统位数的安装包进行安装。(若您不确定您的设备所使用的 USB 芯片，可同时安装两种驱动。**CH9102_VCP_SER_MacOS v1.7**在安装过程中，可能出现报错，但实际上已经完成安装，忽略即可。) 在使用时，若出现无法正常下载程序（提示超时或者 Failed to write to target RAM）的情况，可尝试重新安装设备驱动。

| 驱动名称                  | 适用驱动芯片 | 下载链接                                                                                             |
| ------------------------- | ------------ | ---------------------------------------------------------------------------------------------------- |
| CP210x_VCP_Windows        | CP2104       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CP210x_VCP_Windows.zip)     |
| CP210x_VCP_MacOS          | CP2104       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CP210x_VCP_MacOS.zip)       |
| CP210x_VCP_Linux          | CP2104       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CP210x_VCP_Linux.zip)       |
| CH9102_VCP_SER_Windows    | CH9102       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CH9102_VCP_SER_Windows.exe) |
| CH9102_VCP_SER_MacOS v1.7 | CH9102       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CH9102_VCP_MacOS_v1.7.zip)  |

### Easyloader

| Easyloader             | 下载链接 / Download                                                                                                 | 备注 |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------- | ---- |
| Core2 Factory FirmWare | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/CORE/EasyLoader_M5Core2_FactoryTest.exe) | /    |

### 其他

- [Core2 恢复出厂固件教程](/zh_CN/guide/restore_factory/m5core2)
- [ESP32 formats and communication protocols](https://link.springer.com/book/10.1007/978-1-4842-9376-8)

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/core2/07c3be99c38835c886b7afc23c10083.jpg" width="80%">

> [《ESP32 formats and communication protocols》](https://link.springer.com/book/10.1007/978-1-4842-9376-8)一书分了几章介绍了 M5Stack Core2 模块。M5Stack Core2 模块集成了触摸 LCD 屏幕和 Wi-Fi 通信，麦克风和扬声器，以及加速度计和陀螺仪，使 M5Stack Core2 模块非常通用。本书使用通信协议构建项目，从将智能手表连接手机 (BLE) 到与地球上空环绕的卫星的远程通信 (LoRa) 以及设备之间的音频信号传输 (I2S)。QR 码用于通过互联网控制外部设备，而 ESP-MESH 和 ESP-NOW 协议可在没有互联网连接的情况下实现微控制器之间的通信。

## 相关视频

<video id="example_video" controls>
  <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Core/CORE2%20.mp4" type="video/mp4">
</video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113009246602303&bvid=BV1bmWUeBEjG&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/k1MJw22YQqw?si=0gQKPUrGgng2vXEo" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>

## 产品对比

如需对比控制器系列产品信息，可访问[产品选型表](/zh_CN/products_selector/m5core_compare?select=K010)，勾选目标产品即可获取对比结果。选型表涵盖核心参数、功能特性等关键信息，支持多产品同步比对。

## 版本变更

| 上市日期 | 产品变动                          | 备注：                                                       |
| -------- | --------------------------------- | ------------------------------------------------------------ |
| 2023.10  | 锂电池容量由 390mAh 更改为 500mAh | /                                                            |
| 2023.2   | 取消 RTC 纽扣电池                 | 不影响定时功能                                               |
| 2021.7   | CP2104 替换为 CH9102F             | 实际发货有 CP2104/CH9102F 两个芯片版本，功能与使用上并无差异 |
| 2020.6   | 首次发售                          | /                                                            |
