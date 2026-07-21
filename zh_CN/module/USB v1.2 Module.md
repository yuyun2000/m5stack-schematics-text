# Module USB v1.2

<span class="product-sku">SKU:M020-V12</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/USB v1.2 Module/img-2b9ca068-4799-46ee-a4f1-e7abc5314e7a.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/USB v1.2 Module/img-6086d652-c1aa-4cd5-97b1-8179c665a0f8.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/544/M020-V12-package.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/544/M020-V12.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/USB v1.2 Module/img-8215b675-699d-4afb-8581-d74407d48b92.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/USB v1.2 Module/img-263475b3-8251-46e6-986d-b2c37f258cc9.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/USB v1.2 Module/img-c44ab4fa-7e2a-4a3c-a2f1-05f321f70726.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/USB v1.2 Module/img-ff0703be-8ba8-4c87-aaf9-782b13d6063c.webp">
</PictureViewer>

## 描述

**Module USB v1.2** 是 M5Stack 堆叠模块系列中的 USB 扩展模块，基于 MAX3421E 方案，提供标准 USB 2.0 接口并支持 USB 主机/外设功能。模块通过 SPI 与主控通信，板载拨码开关可切换通信引脚，便于适配不同 M5 主机平台。板上同时预留 GPIO 扩展能力（5 路输入、5 路输出），可用于外设控制与状态采集；并集成锂电池座，进一步提升部署灵活性。该模块适合用于 USB 外设接入、协议验证、嵌入式功能扩展及教学实验等开发场景。

## 产品特性

- MAX3421E USB 控制芯片方案
- 标准 USB 2.0 接口，支持 USB 主机/外设模式
- SPI 通信接口，便于与 M5 主控快速对接
- 双拨码开关设计，可切换引脚以适配不同主机
- GPIO 扩展能力（5 路输入、5 路输出）
- 板载锂电池座，提升移动部署与供电灵活性

## 包装内容

- 1 x Module USB v1.2

## 应用场景

- USB 主机/外设功能扩展
- USB 键盘、鼠标等 HID 设备接入
- USB 存储设备读写与数据交互
- 嵌入式系统 USB 协议学习与教学实验
- 工业设备 USB 通讯接口扩展

## 规格参数

| 规格         | 参数                   |
| ------------ | ---------------------- |
| 芯片型号     | MAX3421E               |
| USB 标准     | USB 2.0                |
| 通信接口     | SPI                    |
| 电池座子规格 | 1.25mm-2P              |
| 工作温度     | 0 ~ 40°C               |
| 产品重量     | 13.3 g                 |
| 产品尺寸     | 54.0 x 54.0 x 12.8 mm  |
| 包装尺寸     | 132.0 x 95.0 x 16.0 mm |
| 毛重         | 28.0 g                 |

## 原理图

- [Module USB v1.2 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/544/SCH_USBHost_V1.2.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/544/SCH_USBHost_V1.2_sch_01.png">
</SchViewer>

## 管脚映射

<img src="https://static-cdn.m5stack.com/resource/docs/products/module/USB v1.2 Module/pinMap-70b8e2ad-8325-4887-af33-44e3dae91520.png" width="100%">

### M5-Bus

#> Switch | 下方 M5-Bus 中标记 `SW` 的引脚，可通过拨码开关进行切换，用于适配不同的主控设备。

::m5-bus-table
| PIN      | LEFT | RIGHT | PIN         |
| -------- | ---- | ----- | ----------- |
| GND      | 1    | 2     | INT (SW)    |
| GND      | 3    | 4     |             |
| GND      | 5    | 6     | EN          |
| SPI_MOSI | 7    | 8     |             |
| SPI_MISO | 9    | 10    |             |
| SPI_SCLK | 11   | 12    | 3V3         |
|          | 13   | 14    |             |
|          | 15   | 16    |             |
|          | 17   | 18    |             |
|          | 19   | 20    | SPI_CS (SW) |
|          | 21   | 22    | SPI_CS (SW) |
|          | 23   | 24    | SPI_CS (SW) |
|          | 25   | 26    | INT (SW)    |
|          | 27   | 28    | 5V          |
|          | 29   | 30    | BAT         |
::

## 尺寸图

<img src="https://static-cdn.m5stack.com/resource/docs/products/module/USB v1.2 Module/img-76853f1e-17c5-4a94-9c66-74e1b150a27c.jpg" width="100%" />

## 数据手册

- [MAX3421E](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/MAX3421E_en.pdf)

## 软件开发

### Arduino

- [Module USB v1.2 Arduino 驱动库](https://github.com/m5stack/M5-Max3421E-USBShield/tree/master)
- [Module USB v1.2 Mouse Example](https://github.com/m5stack/M5-Max3421E-USBShield/blob/master/examples/M5USBMouse/M5USBMouse.ino)

### UiFlow1

- [Module USB v1.2 UiFlow1 文档](/zh_CN/uiflow/blockly/module/usb)

## 相关视频

- Module USB v1.2 功能介绍以及案例

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/USB%20v1.2%20Module/M020-V12%20USB%20V1.2%20MODULE%20%E8%A7%86%E9%A2%91.mp4" type="video/mp4"></video>

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Blog/Twitch201902/USB%20Interface.mp4" type="video/mp4"></video>

## 版本变更

| 上市日期 | 产品变动                                      | 备注      |
| -------- | --------------------------------------------- | --------- |
| 2024.3   | 添加拨码开关，适配 basic/Core2/CoreS3 主机    | 版本 V1.2 |
| 2023.1   | 驱动芯片型号由 MAX3421EEHJ+ 改为 MAX3421EETJ+ | 版本 V1.1 |
| -        | 首次发售                                      | /         |