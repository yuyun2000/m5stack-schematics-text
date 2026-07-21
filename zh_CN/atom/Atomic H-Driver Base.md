# Atomic HDriver Base

<span class="product-sku">SKU:A092</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic H-Driver Base/img-ee0353ff-f8a5-40c0-929e-455844999d21.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic H-Driver Base/img-7c41b561-a56b-43a4-81df-f9efe19f621b.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic H-Driver Base/img-df14a956-fb2a-48a7-8e8d-a2548959790b.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic H-Driver Base/img-ebeef97e-04e8-4132-b819-3e98c93a6f3e.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic H-Driver Base/img-49031532-62ee-4567-a043-95bc7d60bc2f.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic H-Driver Base/img-bd3a8d78-376b-4077-93a9-295bb2a23414.webp">
</PictureViewer>

## 描述

**Atomic HDriver Base** 是一款适配 ATOM 系列控制器的 H 桥电机驱动器。内置 DRV8876 电机驱动芯片，支持 DC 9 ~ 24V 电源输入 (内嵌 DC/DC 电路为整机设备供电，ADC 引脚 G33 直连分压电路可随时监测电源输入情况) ，输出电流可达 1.5A ，峰值 2A ，能够用于直流电机调速与正反转控制。驱动内部集成了 N 沟道 H 桥、充电泵稳压器、电流检测和调节、电流比例输出和保护电路 (保护功能集成：电源欠压锁定 (UVLO)、充电泵欠压 (CPUV)、输出过流 (OCP) 和器件超温 (TSD) ，故障情况并通过 FAULT 引脚指示) 。

## 产品特性

- N 沟道 H 桥电机驱动器
- 高输出电流能力
- 3.3V 逻辑输入
- 扩频时钟可降低电磁干扰
- 集成保护功能

## 包装内容

- 1 x Atomic HDriver Base
- 1 x HT3.96-4P 端子

## 应用场景

- 直流电机控制

## 规格参数

| 规格     | 参数                   |
| -------- | ---------------------- |
| 输入电压 | DC 9 ~ 24V             |
| 输出电流 | 实际输出 1.5A, 峰值 2A |
| 产品尺寸 | 48 x 24 x 17.5mm       |
| 包装尺寸 | 136 x 92 x 13.7mm      |
| 产品重量 | 15.7g                  |
| 毛重     | 20.8g                  |

## 原理图

<img alt="schematics" src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic H-Driver Base/img-640b15c1-b24d-4e9a-b936-2ec3e5a0e8e6.png" width="100%" />

## 管脚映射

::m5-bus-table
| PIN | LEFT | RIGHT | PIN      |
| --- | ---- | ----- | -------- |
|     |      | 1     | 3V3      |
|     | 2    | 3     | FAULT    |
|     | 4    | 5     | IN1      |
| 5V  | 6    | 7     | IN2      |
| GND | 8    | 9     | VIN-1/10 |
::

## 尺寸图

- [Atomic HDriver Base模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/931/A092-atom-pwm.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/931/A092-atom-pwm_page_01.png" width="100%">

## 数据手册

- [DRV8876PWPR Datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/atombase/atom_hdriver/C575551_DRV8876PWPR_2020-06-01.PDF)

## 软件开发

### Arduino

- [Atomic HDriver Base Arduino 快速上手](/zh_CN/arduino/projects/atomic/atomic_hdriver_base)
- [Atomic HDriver Base Example - with Atom](https://github.com/m5stack/M5Atom/tree/master/examples/ATOM_BASE/ATOM_Hdriver)
- [Atomic HDriver Base Example - with AtomS3](https://github.com/m5stack/M5AtomS3/blob/main/examples/AtomicBase/AtomicHDriver/AtomicHDriver.ino)

### UiFlow1

- [Atomic HDriver Base UiFlow1 文档](/zh_CN/uiflow/blockly/atomic_base/h_driver)

### UiFlow2

- [Atomic HDriver Base UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/base/hdriver.html)

## 相关视频

- Atomic H-Driver Base 功能介绍

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/AtomBase/ATOM_HDRIVER.mp4" type="video/mp4"></video>
