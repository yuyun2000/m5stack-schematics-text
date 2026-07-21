# Atomic TFCard Base

<span class="product-sku">SKU:A135</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic TF-Card Reader/img-f481a189-c8a3-4b21-8bde-24a6a8b4131d.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic TF-Card Reader/img-8b04e754-8514-4f49-af8e-1434bd945357.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic TF-Card Reader/img-efbd002d-422a-4ab2-8df8-8309912a500f.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic TF-Card Reader/img-c9257a63-de04-4747-9b1b-1acd2732fc3c.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic TF-Card Reader/img-755f23c7-6872-4aa1-b7d8-661d83aa04c9.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic TF-Card Reader/img-95ad227e-738a-4cde-a34c-69ae50bb8f05.webp">
</PictureViewer>

## 描述

**Atomic TFCard Base** 是一款基于 Atom 系列主机的 TF (microSD) 卡读写模块，自弹式卡槽设计，可最大支持 16G 容量的 microSD，您可以将程序中重要的配置文件和用户数据保存至 microSD 内，也可以在程序运行过程中随时调用这些文件。使用 microSD 读写模块可以大大减少外部资源文件对宝贵 Flash 空间的占用。适用于嵌入式控制系统、工业自动化和物联网设备等领域。

## 产品特性

- 最高支持 16G
- FAT/FAT32 格式
- 自弹式卡槽

## 包装内容

- 1 x Atomic TF-Card Reader

## 应用场景

- 数据保存
- 文件读写
- 日志记录

## 规格参数

| 规格     | 参数                  |
| -------- | --------------------- |
| 支持类型 | 16G FAT/FAT32 microSD |
| 产品尺寸 | 48 x 24 x 18mm        |
| 产品重量 | 8.8g                  |
| 包装尺寸 | 136 x 92 x 20mm       |
| 毛重     | 10.9g                 |

## 原理图

<img alt="schematics" src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic TF-Card Reader/img-88bbd018-3961-4acb-b12e-83c16a1accb7.webp" width="100%" />

## 管脚映射

::m5-bus-table
| PIN | LEFT | RIGHT | PIN      |
| --- | ---- | ----- | -------- |
|     |      | 1     | 3V3      |
|     | 2    | 3     |          |
|     | 4    | 5     | SPI_MOSI |
| 5V  | 6    | 7     | SPI_CLK  |
| GND | 8    | 9     | SPI_MISO |
::

## 尺寸图

- [Atomic TFCard Base模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/912/A077-atomic.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/912/A077-atomic_page_01.png" width="100%">

## 软件开发

### Arduino

- [Atomic TFCard Base Arduino 快速上手](/zh_CN/arduino/projects/atomic/atomic_tfcard_base)

### UiFlow1

- [Atomic TFCard Base UiFlow1 文档](/zh_CN/uiflow/blockly/atomic_base/tf_card)

### UiFlow2

- [Atomic TFCard Base UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/base/tfcard.html)

### EasyLoader

| Easyloader                         | 下载链接                                                                                                                                           | 备注 |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ---- |
| Atomic TFCard Base Test Easyloader | [download](https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic%20TF-Card%20Reader/ezLoader-8bdd5993-bee9-4b0f-9ddc-eff4889733b7.exe) | /    |

## 相关视频

- Atomic TFCard Reader Web 文件管理案例

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/Atomic%20TF-Card%20Reader/WeChat_20231117140029.mp4" type="video/mp4"></video>

- SD 卡读写文件测试，串口输出查看

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/AtomBase/AtomicTF.mp4" type="video/mp4"></video>
