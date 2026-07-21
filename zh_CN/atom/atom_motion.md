# Atom Motion

<span class="product-sku">SKU:K053</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_motion/atom_motion_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_motion/atom_motion_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_motion/atom_motion_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_motion/atom_motion_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_motion/atom_motion_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_motion/atom_motion_06.webp">
</PictureViewer>

## 描述

**Atom Motion** 是适配 ATOM 主控系列的舵机 & DC 电机驱动方案，内部集成 STM32 控制芯片，采用 I2C 通信控制方式。提供 4 通道舵机，2 通道 DC 电机接口。集成规格 16340/18350 锂电池 (容量 700mAh) 。两路 HY2.0-4P 接口拓展，对 4 个 PIN 脚进行了引出，能够用于外接一些传感器与拓展设备。适用于多舵机 / 电机控制场景，如多轴舵机机械臂控制或是小车电机驱动。

## 产品特性

- 4 通道舵机控制
- 2 通道直流电机控制
- 可拆卸锂电池
- 背面磁吸设计
- 独立电源开关
- 2 路 HY2.0-4P 拓展接口

## 包装内容

- 1 x Atom-Lite
- 1 x Atomic Motion Base
- 1 x M2 内六角扳手
- 1 x M2\*8 杯头机械牙螺丝
- 1 x USB Type-C 连接线 (20cm)

## 应用场景

- 直流电机小车控制
- 舵机机械臂控制

## 规格参数

| 规格                   | 参数                           |
| ---------------------- | ------------------------------ |
| MCU                    | STM32F030F4P6                  |
| 通信接口               | I2C 通信 @ 0x38                |
| 可拆卸锂电池           | 规格：16340/18350, 容量 700mAh |
| 电机接口 PIN 间距      | 2.54mm                         |
| 满负荷转向电流         | 3A                             |
| 单通道电机工作峰值电流 | 1A                             |
| 单通道舵机工作峰值电流 | 0.4A                           |
| 产品尺寸               | 24 x 72 x 21mm                 |
| 产品重量               | 40g                            |
| 包装尺寸               | 95 x 65 x 25mm                 |
| 毛重                   | 77.1g                          |

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_motion/atom_motion_sch_01.webp" width="80%">

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

## 数据手册

- [RZ7899 Datashhet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/atombase/atom_motion/C92373_RZ7899_2017-02-13.PDF)

## 软件开发

### Arduino

- [Atom Motion 测试程序](https://github.com/m5stack/M5Atom/tree/master/examples/ATOM_BASE/ATOM_Motion)

### UiFlow1

- [Atom Motion UiFlow1 文档](/zh_CN/uiflow/blockly/atomic_base/motion)

### 通信协议

- 协议类型 I2C
- I2C Address: **0x38**

| Function     | Reg Address            | Lenght    | Data Range      | R/W |
| ------------ | ---------------------- | --------- | --------------- | --- |
| Servo（1~4） | 0x00~0x03              | 1Byte MSB | angle: 0-180    | R/W |
| Servo（1~4） | 0x10、0x12、0x14、0x16 | 2Byte MSB | pulse: 500-2500 | R/W |
| Motor（1~2） | 0x20~0x21              | 1Byte MSB | speed: -127-127 | R/W |

### EasyLoader

| Easyloader                  | 下载链接                                                                                                         | 备注 |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---- |
| Atom Motion Test Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/ATOM_BASE/EasyLoader_Atom_Motion.exe) | /    |

## 相关视频

- 控制 4 路舵机与 2 路 DC 电机转动，按下 ATOM 中心按键可切换 DC 电机旋转方向

<video id="example_video" controls>
  <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/AtomBase/ATOM_MOTION.mp4" type="video/mp4">
</video>

- Atom Motion UiFlow 例子 (乐高小车的搭建)

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/atom_motion/Atom%20Motion%20uiflow.mp4" type="video/mp4"></video>
