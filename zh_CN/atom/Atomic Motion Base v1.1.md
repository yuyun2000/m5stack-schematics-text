# Atomic Motion Base v1.1

<span class="product-sku">SKU:A090-V11</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1124/A090-V11_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1124/A090-V11_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1124/A090-V11_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1124/A090-V11_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1124/A090-V11_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1124/A090-V11_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1124/A090-V11_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1124/A090-V11_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1124/A090-V11_09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1124/A090-V11_10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1124/A090-V11_11.webp">
</PictureViewer>

## 描述

**Atomic Motion Base v1.1** 是专为 ATOM 主控系列设计的舵机与 DC 电机驱动底座。产品提供 4 通道 **舵机** 接口和 2 通道 **直流电机** 接口，同时板载两路 **Grove** 接口，可方便外接各类传感器与扩展设备。通信方面，采用 **I2C** 通信方式，并配合 STM32 控制芯片，确保数据传输稳定。在供电方面，内置 18350 规格锂电池 (900mAh) ，搭载 **INA226** 电流 / 电压检测芯片，实时监控电池电压、电流及功率，保障系统供电安全稳定。同时，集成过载保护功能，有效防止设备因负载过大而损坏。产品还具备电池充电功能，确保电池可以便捷地充电以延长使用时间。板载独立电源开关设计，便于用户进行电源的开关操作。该产品适用于多舵机控制、机器人开发、智能设备原型设计以及自动化实验等领域。

## 产品特性

- 适用于 Atom 系列主控
- 4 通道舵机控制
- 2 通道直流电机控制
- 可拆卸锂电池
- 背面磁吸设计
- 独立电源开关
- 2 路 Grove 接口
- 可充电
- 电池电流 / 电压检测
- 开发平台
  - UiFlow1
  - UiFlow2
  - Arduino IDE

## 包装内容

- 1 x Atomic Motion Base v1.1
- 1 x 18350 规格 900mAh 电池

## 应用场景

- 直流电机小车控制
- 舵机机械臂控制

## 规格参数

| 规格                   | 参数                 |
| ---------------------- | -------------------- |
| MCU                    | STM32F030F4P6        |
| 通信接口               | I2C 通信 @ 0x38      |
| 直流电机驱动           | RZ7899               |
| 功率检测芯片           | INA226               |
| 充放电芯片             | ETA9740              |
| 过载保护               | 5V@5A                |
| 可拆卸锂电池           | 18350@900mAh         |
| 电机接口 PIN 间距      | 2.54mm               |
| 满负荷转向电流         | 3A                   |
| 单通道电机工作峰值电流 | 1A                   |
| 单通道舵机工作峰值电流 | 0.4A                 |
| 待机电流 (开关打开)    | DC4.2V@70.96uA       |
| 充电电流               | DC 5V@1.152A         |
| Grove 接口             | HY2.0-4P             |
| 工作温度               | 0 ~ 40°C             |
| 产品尺寸               | 74.0 x 24.0 x 20.7mm |
| 包装尺寸               | 77.0 x 30.0 x 26.0mm |
| 产品重量               | 41.1g                |
| 毛重                   | 44.8g                |

## 操作说明

\#> 电池充电 | 给 Atomic Motion Base v1.1 在充电前，请确保将开关拨至 ON 位置，然后通过连接数据线与 ATOM 系列主机，或通过 Grove 接口输入 5V 电压进行充电。

## 原理图

[Atomic Motion Base v1.1 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1124/A090-V11_schematic.pdf)

<SchViewer>
<img alt="schematics" src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1124/A090-V11_schematic_sch_01.png" width="100%" />
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

- STM32

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

## 软件开发

### 快速上手

- [Atomic Motion Base v1.1 Arduino Guide](/zh_CN/arduino/projects/atomic/atomic_motion_base)

### Arduino

- [Atomic Motion Base v1.1 Library](https://github.com/m5stack/M5Atomic-Motion)
- [Atomic Motion Base v1.1 测试程序](https://github.com/m5stack/M5AtomS3/blob/main/examples/AtomicBase/AtomicMotion/AtomicMotion.ino)

### UiFlow1

- [Atomic Motion Base v1.1 Docs](/zh_CN/uiflow/blockly/atomic_base/motion)
- [Atomic Motion Base v1.1 Example](https://flow.m5stack.com/?examples=atom_base_motion_demo)

### UiFlow2

- [Atomic Motion Base v1.1 Docs and example](https://uiflow-micropython.readthedocs.io/zh-cn/latest/base/motion.html)

### 通信协议

- 协议类型 I2C
- I2C Address: **0x38**

| Function     | Reg Address            | Lenght    | Data Range      | R/W |
| ------------ | ---------------------- | --------- | --------------- | --- |
| Servo（1~4） | 0x00~0x03              | 1Byte MSB | angle: 0-180    | R/W |
| Servo（1~4） | 0x10、0x12、0x14、0x16 | 2Byte MSB | pulse: 500-2500 | R/W |
| Motor（1~2） | 0x20~0x21              | 1Byte MSB | speed: -127-127 | R/W |

## 相关视频

- Atomic Motion Base v1.1 产品介绍以及示例展示

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1124/A090_V11_Atomi_Motion_Base_v1.1_video.mp4" type="video/mp4"></video>

- Atom Motion Base v1.1 UiFlow 例子 (乐高小车的搭建)

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/atom_motion/Atom%20Motion%20uiflow.mp4" type="video/mp4"></video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=114136910398966&bvid=BV13CRGYeEEN&p=1&autoplay=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/bHNaAJmHRxk?si=zyWVe1_EGoxvP6jU" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>

## 产品对比

::compare-table
| 产品对比表   | [Atomic Motion Base v1.1](/zh_CN/atom/Atomic%20Motion%20Base%20v1.1) ![Atomic Motion Base v1.1](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1124/A090-V11_09.webp) | [Atomic Motion Base](/zh_CN/atom/Atomic%20Motion%20Base) ![Atomic Motion Base](https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic%20Motion%20Base/img-7bbb5a49-e7f3-4b02-bb58-3c8fff5a2000.webp) |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 功率监控     | INA226 (电池电流 / 电压检测)                                                                                                                                            | 不包含                                                                                                                                                                                                          |
| 电池         | 18350@900mAh                                                                                                                                                            | 18350@900mAh                                                                                                                                                                                                    |
| 过载保护     | 具备                                                                                                                                                                    | 具备                                                                                                                                                                                                            |
| 驱动电机类型 | 4 舵机 + 2 直流电机                                                                                                                                                     | 4 舵机 + 2 直流电机                                                                                                                                                                                             |
| 直流电机驱动 | RZ7899                                                                                                                                                                  | RZ7899                                                                                                                                                                                                          |
| 充放电芯片   | ETA9740                                                                                                                                                                 | ETA9740                                                                                                                                                                                                         |
::
