# Hat NeoFlash

<span class="product-sku">SKU:U071</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-neoflash/hat-neoflash_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-neoflash/hat-neoflash_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-neoflash/hat-neoflash_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-neoflash/hat-neoflash_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-neoflash/hat-neoflash_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-neoflash/hat-neoflash_06.webp">
</PictureViewer>

## 描述

**Hat NeoFlash** 是一款专为 M5SticKC 设计的矩阵 RGB LED 灯板。这块尺寸面积仅有 58x23.5mm 的 PCB 板总共嵌入了 126 颗可编程 RGB LED 灯（WS2812），允许用户自由的设置它的颜色与亮度，除了实现炫酷的彩色灯光效果以外，采用 7x18 矩阵设计的它能够带来良好的数字显示体验。在使用灯板制作一些数据显示应用时，使用配套的黑茶色亚克力板，能够有效增强显示效果。结合配套 / 默认的两 90° 组弯曲排针，**Hat NeoFlash** 能够以两种角度安装到 M5StickC 上。如果你打算为你的项目添加一个精致小巧的 LED 矩阵屏幕的话，**Hat NeoFlash** 会是一个不错的选择。

## 产品特性

- 单像素点的三基色颜色:
  - 可实现 0 ~ 256 级亮度显示
  - 完成 16777216 种颜色的全真色彩显示
  - 24 位 RGB 控制数据：每种颜色 8 位
- RGB LED 数量: 126 个
- 孔间距: 0.1 in - (2.54 mm)
- 孔尺寸: 0.039" 1mm (CNC 工艺)
- 安装方式：紧贴背面 (默认)/ 水平拼接
- 单品尺寸：58 x 23.5 x 1mm
- 单品重量：2g

## 包装内容

- 1 x Hat NeoFlash
- 2 x 2.54@8P 弯曲排针 (90°)
- 1 x 2mm 黑茶色亚克力板
- 2 x 15cm 固定线 (#71、0.4mm)

## 应用场景

- LED 矩阵显示屏
- 数字时钟
- 彩色灯光展示

## 规格参数

| 规格     | 参数                |
| -------- | ------------------- |
| 产品尺寸 | 58.0 x 24.0 x 3.0mm |
| 产品重量 | 11.0g               |
| 包装尺寸 | 67.0 x 53.0 x 12vmm |
| 毛重     | 20.0g               |

## 操作说明

> 矩阵灯板 / 亚克力板穿线方式示意图

<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-neoflash/hat-neoflash_07.webp" height="70%">

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-neoflash/hat-neoflash_sch_01.webp" width="70%">

## 管脚映射

| M5StickC     | G26  | 5V  | GND |
| ------------ | ---- | --- | --- |
| Neoflash HAT | DATA | 5V  | GND |

## 软件开发

### Arduino

- [Hat NeoFlash Example](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/Hat/neoflash-hat/Arduino)

### UiFlow2

- [Hat NeoFlash UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/hats/neoflash.html)

### EasyLoader

| Easyloader              | 下载链接                                                                                                     | 备注 |
| ----------------------- | ------------------------------------------------------------------------------------------------------------ | ---- |
| Hat NeoFlash Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/HAT/Neoflash/EasyLoader_Neoflash_HAT.exe) | /    |

## 相关视频

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/HAT/Neoflash_HAT.mp4" type="video/mp4">
</video>
