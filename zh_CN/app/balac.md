# BalaC

<span class="product-sku">SKU:K038</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/balac/balac_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/balac/balac_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/balac/balac_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/balac/balac_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/balac/balac_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/balac/balac_06.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/balac/balac_07.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/balac/balac_08.webp">
</PictureViewer>

## 描述

**BalaC** 是一款可以 DIY 的双轮平衡车，其底座采用 STM32 系列主控，板载 2 颗舵机驱动接口，带有电源指示灯，配备可更换的充电电池。轻巧的设计以及 采用 360° 舵机作为动力执行机构，让你可以利用 UiFlow 图形界面就能写出平衡程序。套装内含有 StickC, 借助内置的 MPU6886 进行姿态解算，通过计算偏移值控制舵机实时补偿，达到平衡的目的。兼容乐高的设计可以让你更换不同的轮胎，如果你想学习 PID 相关内容，或者需要一款有趣的编程玩具产品，那么 BalaC 也许是不错的选择。

## 产品特性

- 基于 ESP32+STM32
- 个性 DIY
- 可拆卸设计
- 双轮舵机控制
- 可更换电池
- 开发平台:
  - [UiFlow](http://flow.m5stack.com)
  - [MicroPython](http://micropython.org/)
  - [Arduino](http://www.arduino.cc)

## 包装内容

- 1 x StickC
- 1 x BalaC Base
- 2 x 轮胎
- 2 x 轮胎适配器
- 2 x 9G 舵机
- 2 x 橡皮筋
- 2 x 螺丝
- 1 x 内六角扳手
- 1 x 16340 700mAh 电池
- 1 x USB Type-C 连接线 (20cm)

## 应用场景

- PID 控制教学
- 创客 DIY 项目
- 机器人入门学习

## 规格参数

| 规格          | 参数                                               |
| ------------- | -------------------------------------------------- |
| ESP32-Pico-D4 | 240MHz dual core, 600 DMIPS, 520KB SRAM, Wi-Fi     |
| MCU           | STM32F030F4P6                                      |
| 舵机          | 旋转角度：360°, 无负载速度：0.12 秒 / 60 度 (4.8V) |
| 驱动器        | L9110S                                             |
| 通讯下位机    | STM32F030F4P6                                      |
| 通讯协议      | I2C: 0x38                                          |
| 电池          | 16340，700mAh 可充电锂电池                         |
| 产品重量      | 162.0g                                             |
| 毛重          | 206.0g                                             |
| 产品尺寸      | 30 x 100 x 105mm                                   |
| 包装尺寸      | 148 x 118 x 42mm                                   |

## 操作说明

<img src="https://static-cdn.m5stack.com/resource/docs/products/app/balac/balac_09.webp" width="100%">
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/balac/balac_10.webp" width="100%">

## 软件开发

### Arduino

- [BalaC Balancing Example](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/App/BalaC/Arduino/Balac)

### UiFlow1

- [Hat Balac 测试程序](/zh_CN/uiflow/blockly/hat/balac)

### Easyloader

| Easyloader            | 下载链接                                                                                                                 | 备注 |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------ | ---- |
| BalaC Test Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/APPLICATION/EasyLoader_BalaC_APPLICATION.exe) | /    |

## 相关视频

- 开机后短按电源键进行校准，此时 LED 闪烁，校准成功即可自动保持平衡。

<video id="example_video" controls>
   <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/App/BalaC.mp4" type="video/mp4">
</video>
