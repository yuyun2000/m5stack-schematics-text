# BugC

<span class="product-sku">SKU:K033</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-bugc/hat-bugc_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-bugc/hat-bugc_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-bugc/hat-bugc_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-bugc/hat-bugc_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-bugc/hat-bugc_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-bugc/hat-bugc_06.webp">
</PictureViewer>

## 描述

**BugC** 是一款兼容 M5StickC 的可编程机器人底座，底座主要部分由四路电机驱动器、四路直流电机、控制芯片为 STM32F030F4、2 个可编程 RGB LED 以及电池座和独立开关等部件组成，外观小巧运动灵活.
Bugc 底座需要结合 M5StickC 控制器使用。在底座上，配备了四个由 STM32F030 驱动的直流减速电机，电路连接至 M5StickC 的顶部插槽，通过 I2C 协议 (0x38) 通信，最终实现控制.

## 产品特性

- 可编程机器人
- 远程控制
- 四路电机驱动器
- 2xRGB LED
- 简洁的设计
- 配备电池底座
- 运动灵活
- 输出轴:⌀0.81mm
- 电机参数:
  - 额定电压: 3.7V DC
  - 额定转速: 15000-2000rpm
  - 额定电流: 50mA
  - 堵转电流: 70mA
  - 绝缘电阻: 10MΩ

## 包装内容

- 1 x BugC
- 1 x 16340 电池 (750mAh)

## 应用场景

- 远程电机控制
- 机器人控制
- 智能玩具

## 规格参数

| 规格     | 参数           |
| -------- | -------------- |
| MCU      | STM32F030F4P6  |
| 通信协议 | I2C:0x38       |
| 产品重量 | 34g            |
| 毛重     | 46g            |
| 产品尺寸 | 55 x 40 x 25mm |
| 包装尺寸 | 74 x 46 x 9mm  |

## 管脚映射

| M5StickC | G0  | G26 | 3.3V | GND | BAT |
| -------- | --- | --- | ---- | --- | --- |
| BugC     | SDA | SCL | 3.3V | GND | BAT |

## 软件开发

### Arduino

- [BugC Example](https://github.com/m5stack/M5StickC/tree/master/examples/Hat/BUGC)

### UiFlow1

- [BugC UiFlow1 文档](/zh_CN/uiflow/blockly/hat/bugc)

### 通信协议

<img style="width:100%" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/hat/hat-bugc/7a07be6bc58d81c503ccbfec3a91f24.png" alt="detail" />

### Easyloader

| Easyloader                                   | 下载链接                                                                                                           | 备注 |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | ---- |
| BugC Example Easyloader - with M5StickC      | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/HAT/BugC/EasyLoader_BugC.exe)                   | /    |
| BugC Example Easyloader - with M5StickC-Plus | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/HAT/BugC/EasyLoader_BugC_for_M5StickC_Plus.exe) | /    |

## 相关视频

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/HAT/bugC.mp4" type="video/mp4">
</video>
