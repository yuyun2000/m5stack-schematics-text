# Atomic Motion Base v1.2

<span class="product-sku">SKU:A090-V12</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1151/A090-V12_Atomic_Motion_Base_v1.2_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1151/A090-V12_Atomic_Motion_Base_v1.2_11.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1151/A090-V12_Atomic_Motion_Base_v1.2_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1151/A090-V12_Atomic_Motion_Base_v1.2_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1151/A090-V12_Atomic_Motion_Base_v1.2_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1151/A090-V12_Atomic_Motion_Base_v1.2_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1151/A090-V12_Atomic_Motion_Base_v1.2_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1151/A090-V12_Atomic_Motion_Base_v1.2_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1151/A090-V12_Atomic_Motion_Base_v1.2_09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1151/A090-V12_Atomic_Motion_Base_v1.2_10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1151/A090-V12_Atomic_Motion_Base_v1.2_14.webp">

</PictureViewer>

## 描述

**Atomic Motion Base v1.2**是专为 Atom 主控系列打造的高性能舵机与 DC 电机驱动底座，深度融合动力控制、智能扩展与安全防护功能，为多领域开发提供一站式解决方案。产品配备 4 通道舵机接口与 2 通道直流电机接口，可精准驱动多种执行机构；两路 HY2.0-4P 接口支持快速接入温湿度、光线等各类传感器，轻松实现设备功能拓展。通信层面，采用稳定的 I2C 通信协议，搭配 STM32+RZ7899 控制芯片，确保驱动稳定、数据传输高效、低延迟。​
供电系统方面，内置 18350 规格 900mAh 可充电锂电池，搭载 DW01-A 高精度单节锂电池保护芯片与 INA226 电流 / 电压检测芯片，构建双重安全防护体系。DW01-A 芯片具备过充电、过放电及短路保护功能，全方位守护电池安全；INA226 芯片则实时监控电池电压、电流及功率，为系统稳定运行提供数据支撑。此外，产品集成过载保护、便捷充电功能，搭配独立电源开关与可拆卸电池设计，使用灵活且安全无忧。​
**Atomic Motion Base v1.2** 具备高度集成化与双重防护设计，尤其适合需兼顾安全性、可扩展性与便携性的应用领域。

## 产品特性

- 适用于 Atom 系列主控
- STM32+RZ7899 控制芯片
- DW01-A 高精度单节锂电池保护芯片
- INA226 电流 / 电压检测芯片
- 集成过载保护功能
- 4 通道舵机控制
- 2 通道直流电机控制
- 2 路 HY2.0-4P 接口
- 可充电锂电池
- 独立电源开关
- 背面磁吸设计
- 独立电源开关
- 开发平台
  - UiFlow1
  - UiFlow2
  - Arduino IDE

## 包装内容

- 1 x Atomic Motion Base v1.2
- 1 x 18350 规格 900mAh 电池

## 应用场景

- 直流电机小车控制
- 舵机机械臂控制

## 规格参数

| 规格                   | 参数                                   |
| ---------------------- | -------------------------------------- |
| MCU                    | STM32F030F4P6                          |
| 通信接口               | I2C 通信 @ 0x38                        |
| 直流电机驱动           | RZ7899                                 |
| 功率检测芯片           | INA226                                 |
| 充放电芯片             | ETA9740                                |
| 电池保护芯片           | DW01-A                                 |
| 充放电保护截止电压     | 充电截止电压 4.14V / 放电截止电压 2.5V |
| 过载保护               | 5V@5A                                  |
| 可拆卸锂电池           | 18350@900mAh                           |
| 电机接口 PIN 间距      | 2.54mm                                 |
| 满负荷转向电流         | 3A                                     |
| 单通道电机工作峰值电流 | 1A                                     |
| 单通道舵机工作峰值电流 | 0.4A                                   |
| 待机电流（开关打开）   | DC4.04V@40.97uA                        |
| 充电电流               | DC 5V@1.18A                            |
| 工作温度               | 0 ~ 40°C                               |
| 产品尺寸               | 75.4 x 24.0 x 20.7mm                   |
| 产品重量               | 41.0g（含电池）                        |
| 包装尺寸               | 79.0 x 31.0 x 26.0mm                   |
| 毛重                   | 45.3g                                  |

## 操作说明

\#> 电池充电 | 给 Atomic Motion Base v1.2 进行充电前，请确保将开关拨至 ON 位置，然后通过连接数据线与 Atom 系列主机，或通过 HY2.0-4P 接口输入 5V 电压进行充电。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1151/A090-V12_Atomic_Motion_Base_v1.2_13.webp" width="50%" >

## 原理图

[Atomic Motion Base v1.2 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1151/A090-V12_schematic.pdf)

<SchViewer>
<img alt="schematics" src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1151/A090-V12_schematic_page_01.png" width="100%" />
</SchViewer>

## 管脚映射

::m5-bus-table
| PIN     | LEFT | RIGHT | PIN    |
| ------- | ---- | ----- | ------ |
|         |      | 1     | 3V3    |
| I2C_SCL | 2    | 3     | PORT.C |
| I2C_SDA | 4    | 5     | PORT.C |
| 5V      | 6    | 7     | PORT.B |
| GND     | 8    | 9     | PORT.B |
::

### STM32

| STM32F030F4P6 | PA10 | PA9 | PA4 | PB1 | PA6 | PA7 | PA0    | PA1    | PA2    | PA3    |
| ------------- | ---- | --- | --- | --- | --- | --- | ------ | ------ | ------ | ------ |
| I2C           | SDA  | SCL |     |     |     |     |        |        |        |        |
| DC Motor      |      |     | M1F | M1R | M2F | M2R |        |        |        |        |
| Servo         |      |     |     |     |     |     | Servo3 | Servo1 | Servo4 | Servo2 |

## 尺寸图

<img alt="module size" src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic Motion Base/img-724e1d6d-a17d-43b3-b987-364bbf109ae1.jpg" width="100%" />

## 数据手册

- [RZ7899](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/atombase/atom_motion/C92373_RZ7899_2017-02-13.PDF)
- [INA226](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1124/A090-V11_INA226.pdf)
- [ETA9740](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1124/A090-V11_ETA9740.pdf)
- [DW01-A](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1151/DW01-A-datasheet.pdf)

## 软件开发

### 快速上手

- [Atomic Motion Base v1.2 Arduino 快速上手](/zh_CN/arduino/projects/atomic/atomic_motion_base)

### Arduino

- [Atomic Motion Base v1.2 Arduino 驱动库](https://github.com/m5stack/M5Atomic-Motion)
- [Atomic Motion Base v1.2 测试程序](https://github.com/m5stack/M5AtomS3/blob/main/examples/AtomicBase/AtomicMotion/AtomicMotion.ino)

### UiFlow1

- [Atomic Motion Base v1.2 UiFlow1 文档](/zh_CN/uiflow/blockly/atomic_base/motion)
- [Atomic Motion Base v1.2 UiFlow1 测试程序](https://flow.m5stack.com/?examples=atom_base_motion_demo)

### UiFlow2

- [Atomic Motion Base v1.2 UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/base/motion.html)

### 通信协议

- 协议类型 I2C
- I2C Address: **0x38**

| 功能说明                            | 寄存器地址             | 数据格式  | 数据范围          | R/W |
| ----------------------------------- | ---------------------- | --------- | ----------------- | --- |
| Servo 角度控制通道 （ch:1 ~ 4）     | 0x00 ~ 0x03            | 1Byte MSB | angle: 0 ~ 180    | R/W |
| Servo PWM 脉冲宽度控制 （ch:1 ~ 4） | 0x10、0x12、0x14、0x16 | 2Byte MSB | pulse: 500 ~ 2500 | R/W |
| Motor 转速控制（ch:1 ~ 2）          | 0x20 ~ 0x21            | 1Byte MSB | speed: -127 ~ 127 | R/W |

## 相关视频

Atomic Motion Base v1.2 产品介绍以及示例展示

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1151/A090-V12_Atomic_Motion_Base_v1.2_video.mp4" type="video/mp4"></video>

## 产品对比

::compare-table
| 产品对比表   | [Atomic Motion Base v1.2](/zh_CN/atom/Atomic_Motion_Base_v1.2) ![Atomic Motion Base v1.2](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1151/A090-V12_Atomic_Motion_Base_v1.2_08.webp) | [Atomic Motion Base v1.1](/zh_CN/atom/Atomic%20Motion%20Base%20v1.1) ![Atomic Motion Base v1.1](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1124/A090-V11_09.webp) | [Atomic Motion Base](/zh_CN/atom/Atomic%20Motion%20Base) ![Atomic Motion Base](https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic%20Motion%20Base/img-7bbb5a49-e7f3-4b02-bb58-3c8fff5a2000.webp) |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 电池保护 IC  | DW01-A                                                                                                                                                                                    | 不具备                                                                                                                                                                  | 不具备                                                                                                                                                                                                          |
| 直流电机驱动 | RZ7899                                                                                                                                                                                    | RZ7899                                                                                                                                                                  | RZ7899                                                                                                                                                                                                          |
| 驱动电机类型 | 4 舵机 + 2 直流电机                                                                                                                                                                       | 4 舵机 + 2 直流电机                                                                                                                                                     | 4 舵机 + 2 直流电机                                                                                                                                                                                             |
| 过载保护     | 具备                                                                                                                                                                                      | 具备                                                                                                                                                                    | 具备                                                                                                                                                                                                            |
| 功率监控     | INA226 (电池电流 / 电压检测)                                                                                                                                                              | INA226 (电池电流 / 电压检测)                                                                                                                                            | 不包含                                                                                                                                                                                                          |
| 电池         | 18350@900mAh                                                                                                                                                                              | 18350@900mAh                                                                                                                                                            | 18350@900mAh                                                                                                                                                                                                    |
| 充放电芯片   | ETA9740                                                                                                                                                                                   | ETA9740                                                                                                                                                                 | ETA9740                                                                                                                                                                                                         |
::
