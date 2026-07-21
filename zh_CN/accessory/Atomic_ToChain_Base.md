# Atomic ToChain Base

<span class="product-sku">SKU:A163</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1193/A163_main-picture-01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1193/A163_main-picture-02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1193/A163_main-picture-03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1193/A163_main-picture-04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1193/A163_main-picture-05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1193/A163_main-picture-06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1193/A163_main-picture-07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1193/A163_main-picture-08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1193/A163_main-picture-09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1193/A163_main-picture-10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1193/A163-weight.jpg">
</PictureViewer>

## 描述

Atomic ToChain Base 是一款专为 Atom 系列主控设计的 Chain 接口转接板，能够便捷地将 Atom 主控底部的扩展 I/O 转换为公头 HY2.0-4P 连接器，轻松接入 M5Stack Chain 系列设备。转接板内部预留焊盘设计，支持灵活配置 Atom 主控底部 I/O 的接入方式。借助该转接板，用户可实现 Atom 系列与 Chain 系列设备之间的无缝扩展连接，拓展更多应用场景。

## 产品特性

- Atom 主控拓展 Chain 设备
- 内部预留焊盘，灵活切换 IO 引脚连接

## 包装内容

- 1 x Atomic ToChain Base
- 1 x 内六角扳手 L 形 1.5mm (适配 M2 螺丝)
- 1 x M2 \* 6mm 螺丝 (杯头，机械牙)

## 应用场景

- Atom 系列主控 Chain 接口转接板

## 规格参数

| 规格     | 参数                  |
| -------- | --------------------- |
| 产品尺寸 | 31.0 x 24.0 x 11.8mm  |
| 产品重量 | 4.3g                  |
| 包装尺寸 | 138.0 x 93.0 x 13.0mm |
| 毛重     | 7.7g                  |

## 操作说明

### 设备连接示意图

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1193/A163_operate_01.jpg">

## 原理图

- [Atomic ToChain Base 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1193/A163-Atom-Chain_SCH_Main_V1.0_20250902.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1193/A163-Atom-Chain_SCH_Main_V1.0_20250902_page_01.png">
</SchViewer>

## 管脚映射

::m5-bus-table
| PIN | LEFT | RIGHT | PIN |
| --- | ---- | ----- | --- |
|     |      | 1     | 3V3 |
|     | 2    | 3     | IO1 |
|     | 4    | 5     | IO2 |
| 5V  | 6    | 7     |     |
| GND | 8    | 9     |     |
::

### HY2.0-4P

转接板内部预留焊盘，用于灵活切换 Atom 主控底部的 IO 接入，以下为默认的引脚连接关系。

::grove-table
| Host         | GND | VCC | IO1 | IO2 |
| ------------ | --- | --- | --- | --- |
| AtomS3 / S3R | GND | 5V  | G5  | G6  |
| Atom         | GND | 5V  | G22 | G19 |
::

## 尺寸图

- [Atomic ToChain Base 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1193/A163-ATOMCHAIN.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1193/A163-ATOMCHAIN_page_01.png" width="100%">

## 相关视频

- Atomic ToChain Base 产品介绍与功能演示

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1193/A163-Atomic-ToChain-Base-video-ZH.mp4" type="video/mp4"></video>
