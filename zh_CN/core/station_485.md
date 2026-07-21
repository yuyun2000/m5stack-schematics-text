# Station-485

<span class="product-sku">SKU:K123</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/station_485/station_485_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/station_485/station_485_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/station_485/station_485_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/station_485/station_485_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/station_485/station_485_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/station_485/station_485_06.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/station_485/station_485_07.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/station_485/station_485_08.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/station_485/station_485_09.webp">
</PictureViewer>

## 描述

**Station-485**是一款多用途**工业级**可编程嵌入式控制器。采用乐鑫 **ESP32** 主控芯片，集成了 **Wi-Fi** 方案，搭载双核低功耗 **Xtensa® 32-bit LX6** 微处理器，主频高达 **240MHz** 。板载 **16MB Flash** ，并集成了 **240 x 135 1.14 英寸全彩高清 IPS 显示面板** 、 **实体按键面板** 、 **丰富的外设** 以及 **两组六个拓展接口** ，还具备 **低功耗休眠 / 定时唤醒** 功能。

支持多种供电方式，包括 **USB Type-C，PWR485，内部可充电电池（板上预留电池插座）** 。板载集成了高功率密度的全集成升压 DC/DC 转换器 SCT12A0DHKR，即便处于复杂的应用场景中，也能够确保电气设备运行的 **稳定性** 。

该控制器适用于工业现场控制、智能楼宇、多路数据采集节点以及开发者原型设计等多种应用场景。

## 教程 & 快速上手

learn>| ![UiFlow](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/uiflow1.0_banner_01.png) | [UiFlow](/zh_CN/uiflow/m5station/program) | 本教程将向你介绍，如何通过 UiFlow 图形化编程平台控制 Station 设备 |

learn>| ![UiFlow2](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/uiflow2.0_banner_01.png) | [UiFlow2](/zh_CN/uiflow2/m5station/program) | 本教程将向你介绍，如何通过 UiFlow2 图形化编程平台控制 Station 设备 |

learn>| ![Arduino IDE](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/arduino_banner_01.png) | [Arduino IDE](/zh_CN/arduino/m5station/program) | 本教程将向你介绍，如何通过 Arduino IDE 编程控制 Station 设备。 |

## 产品特性

- **交互设计**:

  - 1.14 英寸 IPS 显示面板
  - 3 个物理可编程按键
  - 1 个开关按键
  - 7 个可编程 RGB LED 灯

- **电源设计**:

  - 输入部分：
    - 集成 9~24V->5V DC/DC **SY8303** 降压电路
    - **AXP192**电源管理芯片
  - 输出部分：
    - 每路接口（5 路 Grove，1 路 USB-A）均采用电子开关 **SGM2553D** 实现独立通断
    - 6 路 Grove 接口均采用 **INA3221** 作电压 / 电流采集，USB-A 采用 **INA199** 作电流采集
    - 集成高功率密度的全集成升压 DC/DC 转换器**SCT12A0DHKR**
  - 低功耗：
    - 集成 RTC **BM8563** 低功耗休眠 / 定时唤醒

- **端口设计**:

  - 6 路 Grove 拓展接口
    - Port A1/A2 共用供电及信号引脚
    - Port B1/B2/C1/C2 均为独立供电及信号引脚
  - **PWR485**接口（4 线 - HT3.96）
    - RS485
    - 9~24V 电源输入
  - USB type-A 仅作供电输出，无信号引脚

- **结构设计**:

  - **Din 导轨**
  - **磁吸**
  - **挂墙**
  - **螺丝**
  - **轧带**

- 开发平台
  - UiFlow1
  - UiFlow2
  - Arduino IDE
  - ESP-IDF
  - PlatformIO

## 包装内容

- 1 x Station-485
- 1 x USB Type-C 连接线 （100cm）
- 1 x 内六角扳手
- 1 x I/O 贴纸

## 应用场景

- 物联网控制器
- 多路数据采集
- 物联网产品原型设计
- DIY 作品

## 规格参数

| 主控资源            | 参数                                                                               |
| ------------------- | ---------------------------------------------------------------------------------- |
| SoC                 | ESP32-D0WDQ6-V3@双核处理器，主频 240MHz                                            |
| DMIPS               | 600                                                                                |
| SRAM                | 520KB                                                                              |
| Flash               | 16MB                                                                               |
| Wi-Fi               | 2.4 GHz Wi-Fi                                                                      |
| USB 供电            | 5V@1A                                                                              |
| RS485 供电          | 9~24V@1A                                                                           |
| 主机接口            | USB Type-C x 1，HY2.0-4P (I2C+I/O+UART) x 6，Full-Size USB Type-A (OUTPUT)，PWR485 |
| LED                 | SK6812 x 7                                                                         |
| 按键                | 电源键、物理按键 \* 3                                                              |
| IPS LCD 屏幕        | 1.14"@240 x 135 ST7789V2                                                           |
| RTC                 | BM8563                                                                             |
| PMU                 | AXP192                                                                             |
| 电压 / 电流采集器   | INA3221 + INA199                                                                   |
| USB 芯片            | CH9102F                                                                            |
| TTL-RS485           | SP3485                                                                             |
| 降压芯片            | SY8303                                                                             |
| DC/DC 升压          | SCT12A0DHKR                                                                        |
| 电源分配开关        | SGM2553D                                                                           |
| 天线                | 2.4G 3D 天线                                                                       |
| 工作温度            | 0 ~ 60°C                                                                           |
| 底座螺丝规格        | 内六角杯头 M2 x 8 螺丝                                                             |
| 内部 PCB 板预留接口 | 电池接口（规格：1.25mm-4P）USB 线路接口（规格：1.25mm-4P）                         |
| 外壳材质            | ABS+PC                                                                             |
| 产品尺寸            | 88.0 x 65.0 x 35.0mm                                                               |
| 产品重量            | 63.6g                                                                              |
| 包装尺寸            | 104.0 x 73.0 x 54.5mm                                                              |
| 毛重                | 105.3g                                                                             |

## 操作说明

### 开关机操作

- 开机：单击中央电源键
- 关机：长按 4 秒中央电源键

## 原理图

- [Station-485 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/521/Sch_M5Station_v1.3.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/521/Sch_M5Station_v1.3_sch_01.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/521/Sch_M5Station_v1.3_sch_02.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/521/Sch_M5Station_v1.3_sch_03.png">
</SchViewer>

## 管脚映射

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/521/K124-BK123.jpg" width="70%">

### 按键 BUTTON A & 按键 BUTTON

| ESP32-D0WDQ6-V3 | G37      | G38      | G39      |
| --------------- | -------- | -------- | -------- |
| 按键            | BUTTON A | BUTTON B | BUTTON C |

### 彩色 TFT 屏幕

驱动芯片：ST7789v2
分辨率：135 x 240 @1.14"

| ESP32-D0WDQ6-V3 | G5              | G15   | G18       | G19              | G23  |
| --------------- | --------------- | ----- | --------- | ---------------- | ---- |
| AXP192 Chip     |                 |       |           |                  |      |
| LCD             | CS(Chip Select) | RESET | SCK(SCLK) | RS(Date/Command) | MOSI |

| AXP192 Chip | AXP_LDO3 |
| ----------- | -------- |
| LCD         | LCD_BL   |

### RTC

| ESP32-D0WDQ6-V3 | G21 | G22 |
| --------------- | --- | --- |
| BM8563          | SDA | SCL |
| AXP192          |     |     |

| AXP192 | AXP_PWR |
| ------ | ------- |
| BM8563 | INT     |

### 电流电压监视器

| ESP32-D0WDQ6-V3 | G21 | G22 | 控制通道                        |
| --------------- | --- | --- | ------------------------------- |
| INA3221 (0x40)  | SDA | SCL | AXP_GPIO0，AXP_GPIO1            |
| INA3221 (0x41)  | SDA | SCL | AXP_GPIO2，AXP_GPIO3，AXP_GPIO4 |

### 内部 I2C 连接

| ESP32-D0WDQ6-V3     | G21 | G22 |
| ------------------- | --- | --- |
| AXP192(0x34)        | SDA | SCL |
| BM8563(0x51)        | SDA | SCL |
| INA3221(0x40、0x41) | SDA | SCL |

### PWR485

| ESP32-D0WDQ6-V3 | G3  | G1  | G2                                    | (DC-DC 9~24->5V) | GND |
| --------------- | --- | --- | ------------------------------------- | ---------------- | --- |
| SP3485          | TXD | RXD | 发送 - 高电平有效 / 接收 - 低电平有效 |                  | GND |
| SY8303          |     |     |                                       | VIN_12V          |     |

### 电源管理芯片 (AXP192)

| RTC  | LCD BackLight | ESP32-3.3V SK6812，INA3221，CH902F |
| ---- | ------------- | ---------------------------------- |
| LDO1 | LDO3          | DC-DC1                             |

### USB 转串口

| ESP32-D0WDQ6-V3 | G3  | G1  |
| --------------- | --- | --- |
| CH9102F         | TXD | RXD |

### HY2.0-4P

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A1  | GND   | 5V  | G32    | G33   |
| PORT.A2  | GND   | 5V  | G32    | G33   |
| PORT.B1  | GND   | 5V  | G25    | G35   |
| PORT.B2  | GND   | 5V  | G26    | G36   |
| PORT.C1  | GND   | 5V  | G14    | G13   |
| PORT.C2  | GND   | 5V  | G17    | G16   |
::

### 功耗测试

| 工作电流 (LCD、LED、Wi-Fi 开启) | 待机电流 (LCD、LED 开启) |
| ------------------------------- | ------------------------ |
| 161mA                           | 105mA                    |

## 尺寸图

<img alt="module size" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/station_485/module%20size.jpg" width="100%" />

## 结构文件

- [Station-485 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/K123_Station-485/Structures)

## 数据手册

- [ESP32](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/644/esp32_datasheet_cn.pdf)
- [ST7789v2](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/ST7789V.pdf)
- [SY8303AIC](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/SY8303AIC.pdf)
- [SP3485](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/SP3485.pdf)
- [SCT12A0DHKR](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/SCT12A0DHKR.PDF)
- [INA3221_CN](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/INA3221_CN.pdf)
- [INA199_CN](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/INA199_CN.pdf)
- [SGM2553](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/SGM2553.pdf)
- [BM8563](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/BM8563_V1.1_cn.pdf)
- [AXP192 datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/AXP192_datasheet_en.pdf)
- [AXP192 register](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/AXP192_datasheet_cn.pdf)

## 软件开发

### Arduino

- [Station-485 Arduino 快速上手](/zh_CN/arduino/m5station/program)
- [Station-485 Arduino 驱动库](https://github.com/m5stack/M5Station)

### UiFlow1

- [Station UiFlow1 快速上手](/zh_CN/uiflow/m5station/program)

### UiFlow2

- [Station UiFlow2 快速上手](/zh_CN/uiflow2/m5station/program)

### USB 驱动

点击下方连接下载匹配操作系统的驱动程序。在解压压缩包后，选择对应操作系统位数的安装包进行安装。(**CH9102_VCP_SER_MacOS v1.7**在安装过程中，可能出现报错，但实际上已经完成安装，忽略即可。) 在使用时，若出现无法正常下载程序（提示超时或者是 Failed to write to target RAM）的情况，可尝试重新安装设备驱动。

| 驱动名称                  | 适用驱动芯片 | 下载链接                                                                                             |
| ------------------------- | ------------ | ---------------------------------------------------------------------------------------------------- |
| CH9102_VCP_SER_Windows    | CH9102       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CH9102_VCP_SER_Windows.exe) |
| CH9102_VCP_SER_MacOS v1.7 | CH9102       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CH9102_VCP_MacOS_v1.7.zip)  |

### Easyloader

| Easyloader                  | 下载链接                                                                                      | 备注 |
| --------------------------- | --------------------------------------------------------------------------------------------- | ---- |
| Station-485 Test Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/CORE/M5Staion.exe) | /    |

## 产品对比

| Station-485                     | Station-BAT                                 |
| ------------------------------- | ------------------------------------------- |
| 搭载 PWR485（RS485 + 电源输入） | 板载 MPU6886、可搭载两节 18650 电池（并联） |

如需对比 Station 系列产品信息，可访问[产品选型表](/zh_CN/products_selector/m5station_compare?select=K123)，勾选目标产品即可获取对比结果。选型表涵盖核心参数、功能特性等关键信息，支持多产品同步比对。
