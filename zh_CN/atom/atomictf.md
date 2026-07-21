# Atom TFCard

<span class="product-sku">SKU:K044</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomictf/atomictf_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomictf/atomictf_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomictf/atomictf_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomictf/atomictf_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomictf/atomictf_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomictf/atomictf_06.webp">
</PictureViewer>

## 描述

**Atom TFCard** 是一款基于 Atomic 的 TF (microSD) 卡读写模块，自弹式卡槽设计，可支持 16G 容量的 microSD，您可以将程序中重要的配置文件和用户数据保存至 microSD 内，也可以在程序运行过程中随时调用这些文件。使用 microSD 读写模块可以大大减少外部资源文件对宝贵 Flash 空间的占用。

## 产品特性

- 最高支持 16G
- FAT/FAT32 格式
- 自弹式卡槽

## 包装内容

- 1 x Atom-Lite
- 1 x Atomic TFCard Base
- 1 x M2 内六角扳手
- 1 x M2\*8mm 杯头机械牙螺丝
- 1 x 18cm TYPE-C 数据线

## 应用场景

- 数据保存
- 文件读写
- 日志记录

## 规格参数

| 规格     | 参数                  |
| -------- | --------------------- |
| 支持类型 | 16G FAT/FAT32 microSD |
| 产品尺寸 | 24.0 x 48.0 x 18.0mm  |
| 产品重量 | 23.0g                 |
| 包装尺寸 | 54.0 x 54.0 x 20.0mm  |
| 毛重     | 33.0g                 |

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomictf/atomictf_sch_01.webp" width="80%">

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

| Atom         | G19  | G23 | G33  |
| ------------ | ---- | --- | ---- |
| Atom TF-CARD | MOSI | CLK | MISO |

## 尺寸图

- [Atom TFCard模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/909/K044-atom-tfcard.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/909/K044-atom-tfcard_page_01.png" width="100%">

## 软件开发

### Arduino

- [Atom TFCard 测试程序](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/AtomBase/AtomicTF)

### UiFlow1

- [Atom TFCard UiFlow1 文档](/zh_CN/uiflow/blockly/atomic_base/tf_card)

### EasyLoader

| Easyloader                  | 下载链接                                                                                                       | 备注 |
| --------------------------- | -------------------------------------------------------------------------------------------------------------- | ---- |
| Atom TFCard Test Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/ATOM_BASE/EasyLoader_Atomic_TF.exe) | /    |

## 相关视频

- SD 卡读写文件测试，串口输出查看

<video id="example_video" controls>
   <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/AtomBase/AtomicTF.mp4" type="video/mp4">
</video>
