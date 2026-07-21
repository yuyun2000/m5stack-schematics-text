# Atomic Motion Base

<span class="product-sku">SKU:A090</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic Motion Base/img-40a0d2ba-04b3-4aa3-8417-0624762b3cc3.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic Motion Base/img-b1a0c4d1-5cb2-4acd-a293-42bc81301898.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic Motion Base/img-cfe1a4d4-3dba-4f65-bc11-226e85513e1d.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic Motion Base/img-c7505238-4375-49db-a3a3-76728e532c7c.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic Motion Base/img-356c9358-e01b-4974-929e-31d3df17ab03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic Motion Base/img-22e24391-066f-4725-863f-d641e209337e.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic Motion Base/img-7bbb5a49-e7f3-4b02-bb58-3c8fff5a2000.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic Motion Base/img-3a669496-7ee3-41b1-9d69-1dfe834cd610.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic Motion Base/img-89a360be-6ad0-493e-9ba4-902f690e37c3.webp">
</PictureViewer>

## 描述

**Atomic Motion Base** 是适配 ATOM 主控系列的舵机 & DC 电机驱动方案，内部集成 STM32 控制芯片，采用 I2C 通信控制方式。提供 4 通道舵机，2 通道 DC 电机接口。集成规格 16340/18350 锂电池 (容量 700mAh) 。两路 HY2.0-4P 接口拓展，对 4 个 PIN 脚进行了引出，能够用于外接一些传感器与拓展设备。适用于多舵机 / 电机控制场景，如多轴舵机机械臂控制或是小车电机驱动。

## 产品特性

- 适用于 AtomS3/AtomS3-Lite/Atom-Lite/Atom-Matrix
- 4 通道舵机控制
- 2 通道直流电机控制
- 可拆卸锂电池
- 背面磁吸设计
- 独立电源开关
- 2 路 HY2.0-4P 拓展接口

## 包装内容

- 1 x Atomic Motion Base
- 1 x 16340 规格 700mAh 电池

## 应用场景

- 直流电机小车控制
- 舵机机械臂控制

## 规格参数

| 规格                   | 参数                            |
| ---------------------- | ------------------------------- |
| MCU                    | STM32F030F4P6                   |
| 通信接口               | I2C 通信 @ 0x38                 |
| 可拆卸锂电池           | 规格：16340/18350 (容量 700mAh) |
| 电机接口 PIN 间距      | 2.54mm                          |
| 满负荷转向电流         | 3A                              |
| 单通道电机工作峰值电流 | 1A                              |
| 单通道舵机工作峰值电流 | 0.4A                            |
| 产品尺寸               | 74 x 24 x 20.7mm                |
| 包装尺寸               | 136 x 92 x 13mm                 |
| 产品重量               | 35g                             |
| 毛重                   | 37g                             |

## 原理图

<img alt="schematics" src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic Motion Base/img-e3e37376-655b-4193-aa31-b44c116df5ff.webp" width="100%" />

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

- I2C Interface

| Atom               | G21 | G25 |
| ------------------ | --- | --- |
| Atomic Motion Base | SCL | SDA |
| PORT（White）      | SCL | SDA |

- HY2.0-4P

| Atom               | G23、G33        | G22、G19       |
| ------------------ | --------------- | -------------- |
| Atomic Motion Base | PORT.B（Black） | PORT.C（Blue） |

## 尺寸图

<img alt="module size" src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic Motion Base/img-724e1d6d-a17d-43b3-b987-364bbf109ae1.jpg" width="100%" />

## 数据手册

- [RZ7899 Datashhet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/atombase/atom_motion/C92373_RZ7899_2017-02-13.PDF)

## 软件开发

### Arduino

- [Atomic Motion Base 测试程序](https://github.com/m5stack/M5AtomS3/blob/main/examples/AtomicBase/AtomicMotion/AtomicMotion.ino)

### UiFlow1

- [Atomic Motion Base 测试程序](/zh_CN/uiflow/blockly/atomic_base/motion)

### UiFlow2

- [Atomic Motion Base UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/base/motion.html)

### 通信协议

- 协议类型 I2C
- I2C Address: **0x38**

| Function     | Reg Address            | Lenght    | Data Range      | R/W |
| ------------ | ---------------------- | --------- | --------------- | --- |
| Servo（1~4） | 0x00~0x03              | 1Byte MSB | angle: 0-180    | R/W |
| Servo（1~4） | 0x10、0x12、0x14、0x16 | 2Byte MSB | pulse: 500-2500 | R/W |
| Motor（1~2） | 0x20~0x21              | 1Byte MSB | speed: -127-127 | R/W |

## 相关视频

- 控制 4 路舵机与 2 路 DC 电机转动，按下 ATOM 中心按键可切换 DC 电机旋转方向

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/AtomBase/ATOM_MOTION.mp4" type="video/mp4"></video>

- Atom Motion Base UiFlow 例子 (乐高小车的搭建)

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/atom_motion/Atom%20Motion%20uiflow.mp4" type="video/mp4"></video>
