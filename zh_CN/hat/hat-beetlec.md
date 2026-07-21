# BeetleC

<span class="product-sku">SKU:K030</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-beetlec/hat-beetlec_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-beetlec/hat-beetlec_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-beetlec/hat-beetlec_03.webp">
</PictureViewer>

## 描述

**BeetleC**是一款兼容 M5StickC 的可编程小车底座，底座主要部分由双电机驱动器、双路减速电机、控制芯片、7 个可编程 RGB LED 以及亚克力轮等部件组成。其极度简洁的外观设计与拓展性极强、具备网络通信能力的控制器方案，能够带给用户不一样的机器小车控制体验。

**BeetleC**底座需要结合 M5StickC 控制器使用。在底座上，配备了两个由 STM32F030 驱动的直流减速电机，电路连接至 M5StickC 的顶部插槽，最终实现控制。

车身外观是略微倾斜的，由于正面和背面的车轮尺寸不同，如图所示。此外，电源开关位于机身前部。

## 产品特性

- 可编程小车
- 远程控制
- 双电机驱动器
- 7xRGB LED
- 简洁的设计
- 内置电池：底座 (80ma).
- 平稳控制
- 前轮直径:⌀25mm
- 后轮直径:⌀14mm

## 包装内容

- 1 x BeetleC

## 应用场景

- 远程电机控制
- 无线小车控制

## 规格参数

| 规格     | 参数           |
| -------- | -------------- |
| MCU      | STM32F030F4P6  |
| 产品重量 | 27g            |
| 毛重     | 47g            |
| 产品尺寸 | 70 x 50 x 25mm |
| 包装尺寸 | 85 x 55 x 31mm |

## 操作说明

### 基本配置

- 通过顶部拓展端口将 M5StickC 连接到 beetlec 底座.
- 按复位按钮打开 M5StickC.
- 检查硬件反馈:
     - Base 的 7 个 LED 将依次点亮 3 次.
     - 按下按钮 A, 前轮将前后旋转 500ms.
- 使用手机或计算机进行 Wi-Fi 扫描，搜索并连接 ssid 名称 "beetle", 密码为 "12345678" 加上屏幕上显示的 mac 地址开头.
- 然后打开浏览器并输入`192.168.4.1 / ctl`. 加载页面后，控制页面如图显示.

### 控制页面

<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-beetlec/hat-beetlec_04.webp" width="40%">

- 向上推动控制杆以加速车轮，向下推动减速.
- 底部有四个颜色的螺栓。彩色块用于打开底部的所有 RGB LED 指定的颜色。黑色挡将关闭灯.

## 管脚映射

| M5StickC | G0  | G26 | 3.3V | GND | BAT |
| -------- | --- | --- | ---- | --- | --- |
| BeetleC  | SDA | SCL | 3.3V | GND | BAT |

## 软件开发

### Arduino

- [BeetleC Example](https://github.com/m5stack/M5StickC/tree/master/examples/Hat/BeetleC)

### UiFlow1

- [BeetleC UiFlow1 文档](/zh_CN/uiflow/blockly/hat/beetlec)

### Easyloader

| Easyloader         | 下载链接                                                                                               | 备注 |
| ------------------ | ------------------------------------------------------------------------------------------------------ | ---- |
| BeetleC Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/HAT/BeetleC/EasyLoader_BeetleC.exe) | /    |

## 相关视频

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/HAT/BeetleC_01.mp4" type="video/mp4">
</video>

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/HAT/BeetleC_02.mp4" type="video/mp4">
</video>
