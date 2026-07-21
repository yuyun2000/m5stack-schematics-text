# Atomic ToUnit Base

<span class="product-sku">SKU:A161</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1195/A161_main-picture-01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1195/A161_main-picture-02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1195/A161_main-picture-03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1195/A161_main-picture-04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1195/A161_main-picture-05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1195/A161_main-picture-06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1195/A161_main-picture-07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1195/A161_main-picture-08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1195/A161_main-picture-09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1195/A161_main-picture-10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1195/A161-weight.jpg">
</PictureViewer>

## 描述

Atomic ToUnit Base 是一款专为 Atom 系列主控设计的 Unit 接口转接板。它能够便捷地将 Atom 主控底部的扩展 IO 转换为公头 HY2.0-4P 连接器，从而直接连接 M5Stack Unit 系列设备。转接板内置拨码开关，支持灵活配置 Atom 底部 IO 的接入方式。借助该转接板，用户可实现 Atom 系列与 Unit 系列设备之间的无缝扩展连接，拓展更多应用场景。

## 产品特性

- Atom 主控底部 IO 拓展 Unit 设备
- 集成拨码开关，灵活切换 IO 引脚连接

## 包装内容

- 1 x Atomic ToUnit Base
- 1 x 内六角扳手 L 形 1.5mm (适配 M2 螺丝)
- 1 x M2 \* 10mm 螺丝 (杯头，自攻牙)
- 1 x 拨码开关贴纸

## 应用场景

- Atom 系列主控 Unit 接口转接板

## 规格参数

| 规格     | 参数                  |
| -------- | --------------------- |
| 产品尺寸 | 30.2 x 24.0 x 13.1mm  |
| 产品重量 | 4.6g                  |
| 包装尺寸 | 138.0 x 93.0 x 13.0mm |
| 毛重     | 7.8g                  |

## 操作说明

### 设备连接示意图

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1195/A161_operate_01.jpg">

### DIP Switch 引脚说明

1. DIP Switch 引脚开关拨至下方为禁用状态，拨至上方为启用状态。
2. 同一引脚仅可开启一组，禁止在如 IO1 与 IO2 中重复启用相同引脚（示例：IO2 侧启用 G22 后，IO1 侧不可再启用 G22），否则设备将无法正常运行。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1195/A161_operate_01.png" width="40%">

## 原理图

- [Atomic ToUnit Base 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1195/A161-SCH_Atomic-ToUnit-Base_SCH_2025_08_28_11_06_42.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1195/A161-SCH_Atomic-ToUnit-Base_SCH_2025_08_28_11_06_42.png">
</SchViewer>

## 管脚映射

::m5-bus-table
| PIN | LEFT | RIGHT | PIN       |
| --- | ---- | ----- | --------- |
|     |      | 1     | 3V3       |
|     | 2    | 3     | IO1 / IO2 |
|     | 4    | 5     | IO1 / IO2 |
| 5V  | 6    | 7     | IO1 / IO2 |
| GND | 8    | 9     | IO1 / IO2 |
::

### 拓展接口

::grove-table
| HY2.0-4P           | Black | Red | Yellow | White |
| ------------------ | ----- | --- | ------ | ----- |
| Atomic ToUnit Base | GND   | 5V  | IO1    | IO2   |
::

## 尺寸图

- [Atomic ToUnit Base模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1195/A161-atom2unit.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1195/A161-atom2unit_page_01.png" width="100%">

## 相关视频

- Atomic ToUnit Base 产品介绍以及功能展示

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1195/A161-Atomic-ToUnit-Base-video-ZH.mp4" type="video/mp4"></video>
