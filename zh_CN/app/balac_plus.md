# BalaC-Plus

<span class="product-sku">SKU:K038-B</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/balac_plus/balac_plus_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/balac_plus/balac_plus_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/balac_plus/balac_plus_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/balac_plus/balac_plus_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/balac_plus/balac_plus_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/balac_plus/balac_plus_06.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/balac_plus/balac_plus_07.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/balac_plus/balac_plus_08.webp">
</PictureViewer>

## 描述

**BalaC PLUS** 是一款可以 DIY 的双轮平衡车，其底座采用 STM32 系列主控，板载 2 颗电机驱动 IC, 带有电源指示灯，配备可更换的充电电池。轻巧的设计以及 360° 舵机的驱动形式，让你可以利用 UiFlow 图形界面就能写出平衡程序。套装内含有 StickC PLUS, 借助内置的 MPU6886 进行姿态解算，通过计算偏移值控制舵机实时补偿，达到平衡的目的。兼容乐高的设计可以让你更换不同的轮胎，如果你想学习 PID 方面的相关内容，或者需要一款有趣的编程玩具产品，那么 BalaC PLUS 也许是不错的选择。

## 教程 & 快速上手

learn>| ![快速上手](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1074/BalaC-Plus_operate_01.jpg) | [快速上手](/zh_CN/guide/hobby_kit/balac_plus/balac_plus) | 本教程主要演示为 BalaC-Plus 烧录平衡车固件并进行校准的操作方法。 |

## 产品特性

- 基于 ESP32+STM32
- 个性 DIY
- 可拆卸设计
- 双轮电机驱动
- 可更换电池
- 开发平台：
  - [UiFlow](http://flow.m5stack.com)
  - [MicroPython](http://micropython.org/)
  - [Arduino](http://www.arduino.cc)

## 包装内容

- 1 x StickC-Plus
- 1 x BalaC Base
- 2 x 轮胎
- 2 x 轮胎适配器
- 2 x 9G 舵机
- 2 x 橡皮筋
- 2 x 螺丝
- 1 x 内六角扳手
- 1 x 16340 700mAh 电池
- 1 x USB Type-C 连接线 (20cm)
- 1 x 组装说明书

## 应用场景

- 平衡车

## 规格参数

| 规格          | 参数                                               |
| ------------- | -------------------------------------------------- |
| ESP32-PICO-D4 | 240MHz dual core, 600 DMIPS, 520KB SRAM, Wi-Fi     |
| MCU           | STM32F030F4P6                                      |
| 舵机          | 旋转角度：360°, 无负载速度：0.12 秒 / 60 度 (4.8V) |
| 驱动器        | L9110S                                             |
| 通讯下位机    | STM32F030F4P6                                      |
| 通讯协议      | I2C: 0x38                                          |
| 电池          | 16340，700mAh 可充电锂电池                         |
| 产品尺寸      | 30.0 x 100.0 x 105.0mm                             |
| 产品重量      | 120.0g                                             |
| 包装尺寸      | 148.0 x 118.0 x 42.0mm                             |
| 毛重          | 156.0g                                             |

## 操作说明

<img src="https://static-cdn.m5stack.com/resource/docs/products/app/balac_plus/balac_plus_09.webp" width="100%">
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/balac_plus/balac_plus_10.webp" width="100%">

## 软件开发

### 快速上手

- [BalaC-Plus 上手体验](/zh_CN/guide/hobby_kit/balac_plus/balac_plus)

### Arduino

- [BalaC-Plus Balancing Example](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/App/BalaC-Plus/Arduino/BalaCplus)

### UiFlow1

- [BalaC-Plus 测试程序](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/App/BalaC-Plus/UiFlow)

<img src="https://static-cdn.m5stack.com/resource/docs/products/app/balac_plus/balac_plus_uiflow_01.webp" width="50%">

### Easyloader

| Easyloader                         | 下载链接                                                                                                                      | 备注 |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ---- |
| BalaC-Plus Test Easyloader         | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/APPLICATION/EasyLoader_BalaC_Plus_APPLICATION.exe) | /    |
| BalaC-Plus Balance Demo Easyloader | [download](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1074/BalaC-Plus-Balance-Demo-Easyloader.exe)                      | /    |

## 相关视频

- 开机后短按电源键进行校准，此时 led 闪烁，校准成功即可自动保持平衡.

<video id="example_video" controls>
   <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/App/BalaC.mp4" type="video/mp4">
</video>
