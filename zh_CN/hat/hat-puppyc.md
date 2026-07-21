# PuppyC

<span class="product-sku">SKU:K035</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-puppyc/hat-puppyc_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-puppyc/hat-puppyc_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-puppyc/hat-puppyc_03.webp">
</PictureViewer>

## 描述

**PuppyC**是一款兼容 M5StickC 的可编程四足机器人底座。它由控制芯片 STM32F030F4、四路 SG90 舵机、电池座和独立开关等部件组成，其移动行走较为平缓，易于控制。因为接触面积小且运动慢，所以使用时尽量选择摩擦力较大且柔软的表面。该底座需要结合 M5StickC 控制器使用，M5StickC 编程后通过 I2C 协议（0x38）与 PuppyC 进行通信，进而控制舵机运动。

## 产品特性

- 可编程机器人
- 舵机驱动控制器
- 四足行走
- 舵机角度：0-180°

## 包装内容

- 1 x PuppyC
- 1 x 16340 电池 (700mAh)
- 4 x SG90 舵机

## 应用场景

- 舵机驱动
- 机器人控制
- 智能玩具

## 规格参数

| 规格     | 参数            |
| -------- | --------------- |
| MCU      | STM32F030F4P6   |
| 通信协议 | I2C:0x38        |
| 产品重量 | 58g             |
| 毛重     | 108g            |
| 产品尺寸 | 52 x 60 x 35mm  |
| 包装尺寸 | 106 x 66 x 42mm |

## 软件开发

### Arduino

- [PuppyC Example](https://github.com/m5stack/M5StickC/tree/master/examples/Hat/PuppyC)

### UiFlow1

- [PuppyC UiFlow1 文档](/zh_CN/uiflow/blockly/hat/puppyc)

### Easyloader

| Easyloader        | 下载链接                                                                                             | 备注 |
| ----------------- | ---------------------------------------------------------------------------------------------------- | ---- |
| PuppyC Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/HAT/PuppyC/EasyLoader_PuppyC.exe) | /    |

## 相关视频

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/App/PuppyC/PuppyC.mp4" type="video/mp4">
</video>
