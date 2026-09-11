# StamPLC IO

<span class="product-sku">SKU:A176</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1257/A176_StamPLC_IO_main_pictures_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1257/A176_StamPLC_IO_main_pictures_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1257/A176_StamPLC_IO_main_pictures_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1257/A176_StamPLC_IO_main_pictures_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1257/A176_StamPLC_IO_main_pictures_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1257/A176_StamPLC_IO_main_pictures_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1257/A176_StamPLC_IO_main_pictures_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1257/A176_StamPLC_IO_main_pictures_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1257/A176_StamPLC_IO_main_pictures_09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1257/A176_StamPLC_IO_main_pictures_10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1257/A176_StamPLC_IO_main_pictures_11.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1257/A176_StamPLC_IO_main_pictures_12.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1257/A176_StamPLC_IO_main_pictures_weight.jpg">
</PictureViewer>

## 描述

StamPLC IO 为配套 StamPLC 主机设计的电气隔离型 IO 扩展模块，专为工业现场强弱电混合场景开发。模块搭载 2 路有源模拟量采集通道、2 路固态继电器输出、1 路机械继电器输出，支持工业有源电压 / 电流型传感器信号采集，同时实现各类负载回路通断控制。板载 STM32G030F6P6 主控芯片，统一管理外部输入输出、继电器驱动、地址分配与隔离通道 I2C 总线通信；配套硬件拨码开关完成 I2C 地址自定义，支持多模块并联级联，灵活扩展系统 IO 点位。

模块搭载 CA-IS3020S 数字隔离器与 B0505M-2WR3 隔离电源，实现通信总线与供电回路完全电气隔离，有效抑制传感器、现场负载带来的共模干扰、浪涌冲击，大幅提升整套系统运行稳定性。适用于电源支路监测、低压执行器驱动、传感器供电管控等工业自动化场景。

## 产品特性

- STM32G030F6P6 核心主控
- I2C 通信接口
- 板载 4 位拨码开关，可配置设备 I2C 地址
- 2 路有源模拟信号检测通道
  - 支持接入 DC 0 ~ 10V 电压型传感器
  - 支持接入 0 ~ 20mA 电流型传感器
- 2 路固态继电器控制
  - 支持 DC 0 ~ 60V MAX 2.5A 线路通断
- 1 路机械式继电器控制
  - 支持 AC 250V@5A / DC 28V@5A 线路通断
- 内置 CA-IS3020S I2C 隔离器
- 内置 B0505M-2WR3 隔离电源模块
- 板载继电器输出状态指示 LED
- 输入与输出通道带保护电路
- DIN 导轨安装 / 挂孔安装

## 包装内容

- 1 x StamPLC IO
- 2 x 固定连接件

## 应用场景

- 通用模拟量信号采集
- 外部执行器开关控制
- 继电器干接点远程控制
- 多模块隔离 IO 扩展

## 规格参数

| 规格            | 参数                                                                                         |
| --------------- | -------------------------------------------------------------------------------------------- |
| MCU             | STM32G030F6P6                                                                                |
| 通信方式        | I2C @ 0x20                                                                                   |
| I2C 隔离器      | CA-IS3020S                                                                                   |
| 隔离电源        | B0505M-2WR3                                                                                  |
| 电源转换        | TPAP7343D-33FS4                                                                              |
| 电压 / 电流检测 | INA226AIDGSR                                                                                 |
| 检测通道        | 2 路模拟信号检测通道（兼容 0 ~ 20mA 和 0 ~ 10V 模拟量采集）                                  |
| MOS 开关输出    | 2 路固态继电器 MOS1 / MOS2，公共端 COM，支持 DC 0 ~ 60V  MAX 2.5A 线路通断                   |
| 继电器输出      | 1 路 SRD-5VDC-SL-C 机械式继电器，端子 N.C / COM / N.O ，支持 AC 250V@5A / DC 28V@5A 线路通断 |
| 地址配置        | 4 位拨码开关，可配置 I2C 地址范围：0x20 ~ 0x2F                                               |
| 控制接口类型    | 2 x 3P 开关输出 / 继电器接线端子，1 x 6P 输入端子                                            |
| 安装方式        | DIN 导轨安装 / 挂孔                                                                          |
| 产品尺寸        | 51.4 x 80.0 x 27.1mm                                                                         |
| 产品重量        | 62.1g                                                                                        |
| 包装尺寸        | 84.0 x 56.0 x 29.0mm                                                                         |
| 毛重            | 69.2g                                                                                        |

## 操作说明

### 电压型传感器检测接法说明

- 测试电压时，使用输入检测通道的 IN+、ISO GND 端子接入有源被测设备，接线示意图如下：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1257/A176_StamPLC_IO_connect_pictures_01_CN.png" width="60%">

### 电流型传感器检测接法说明

- 测试电流时，使用输入检测通道的 IN+、IN- 端子接入有源被测设备，接线示意图如下：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1257/A176_StamPLC_IO_connect_pictures_02_CN.png" width="60%">

### 继电器开关接法说明

- 机械式继电器输出端子提供 N.C / COM / N.O 三个端子，固态继电器输出端子提供 MOS1 / MOS2 / COM 三个端子，接线示意图如下：

!> 安全警告 | 机械式继电器端子接入 220V 交流电时，请务必确保操作安全，避免触电风险。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1257/A176_StamPLC_IO_connect_pictures_04_CN.png" width="60%">

### StamPLC 与 StamPLC IO 连接示意图

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1257/StamPLC_IO_connect.png" width="70%">

## 原理图

- [StamPLC IO 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1257/SCH_StamPLC_IO_SCH_V0.5_20260430_2026_07_02_18_04_04.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1257/SCH_StamPLC_IO_SCH_V0.5_20260430_2026_07_02_18_04_04_page_01.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1257/SCH_StamPLC_IO_SCH_V0.5_20260430_2026_07_02_18_04_04_page_02.png">
</SchViewer>

## 管脚映射

| StamPLC    | G15 | G13 |
| ---------- | --- | --- |
| StamPLC IO | SCL | SDA |

### StamPLC-Bus

::m5-bus-table
| PIN      | LEFT | RIGHT | PIN      |
| -------- | ---- | ----- | -------- |
| IO_1     | 1    | 2     | IO_2     |
| IO_3     | 3    | 4     | IO_4     |
| IO_5     | 5    | 6     | IO_6     |
| IO_7     | 7    | 8     | IO_8     |
| USER_SDA | 9    | 10    | USER_SCL |
| EXT_5V   | 11   | 12    | GND      |
| GND      | 13   | 14    | GND      |
| GND      | 15   | 16    | HV_IN    |
::

## 尺寸图

- [StamPLC IO 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1257/A176_StamPLC_IO_model_size.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1257/A176_StamPLC_IO_model_size_page_01.png" width="100%">

## 数据手册

- [STM32G030F6P6](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/U162%20AIN4-20mA%20Unit/STM32G030F6%20datasheet.PDF)
- [INA226AIDGSR](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/INA226AIDGSR.pdf)
- [CA-IS3020S](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/CA-IS3020S.pdf)
- [TPAP7343D](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1158/LDO_TPAP7343D-33FS4_datasheet.pdf)

## 软件开发

### Arduino

- [StamPLC IO Arduino 快速上手](/zh_CN/arduino/projects/stamplc/stamplc_io)
- [StamPLC IO Arduino 案例程序](https://github.com/m5stack/M5StamPLC/tree/main/examples/Modules/StamPLC_IO)

### 内置固件

- [StamPLC IO 内置固件](https://github.com/m5stack/M5StamPLC-IO-Internal-FW)

### 通信协议


- [StamPLC IO I2C 通信协议 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1257/StamPLC_IO-I2C-Protocol-CN-V1.0.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1257/StamPLC_IO-I2C-Protocol-CN-V1.0_page_01.png" width="100%">

<!-- 英文版：
https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1257/StamPLC_IO-I2C-Protocol-EN-V1.0.pdf
https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1257/StamPLC_IO-I2C-Protocol-EN-V1.0_page_01.png -->

## 相关视频

- StamPLC IO 产品介绍以及功能展示

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1257/A176_StamPLC_IO-video_CN.mp4" type="video/mp4"></video>   <!--英文视频链接：https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1257/A176_StamPLC_IO-video_EN.mp4>