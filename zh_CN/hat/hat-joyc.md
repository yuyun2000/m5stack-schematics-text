# Hat JoyC

<span class="product-sku">SKU:U079</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-joyc/hat-joyc_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-joyc/hat-joyc_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/877/U079-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-joyc/hat-joyc_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-joyc/hat-joyc_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-joyc/hat-joyc_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-joyc/hat-joyc_06.webp">
</PictureViewer>

## 描述

**Hat JoyC** 是一款专为 M5StickC 设计的摇杆模块，可进行双手操作。内嵌 STM32F030F4 主控芯片，采用 I2C 通信协议与主机 M5StickC 进行数据传输。摇杆的范围为 0 ~ 200，左右摇杆下方各有 12 颗 RGB LED，摇杆底部配有 16340/18350 电池底座，提供长时间续航。该摇杆支持进行全方位的角度偏移与中心按压，并输出角度偏移数据以及开关数字信号。

## 产品特性

- 内嵌 STM32F030F4
- 通信协议：I2C (地址：0x38)
- 支持全方位偏移 / 中心按键

## 包装内容

- 1 x Hat JoyC
- 1 x 16340/18350 电池 (700mAh)

## 应用场景

- 游戏控制器
- 无线摇杆设备

## 规格参数

| 规格     | 参数                  |
| -------- | --------------------- |
| MCU      | STM32F030F4P6         |
| 通信接口 | I2C 通信 @ 0x38       |
| 产品尺寸 | 100.0 x 55.0 x 50.0mm |
| 产品重量 | 81.0g                 |
| 包装尺寸 | 119.0 x 89.0 x 65.0mm |
| 毛重     | 117.0g                |

## 尺寸图

[Hat JoyC 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/877/hatjoyc.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/877/hatjoyc_U079.jpg" width="100%">

## 软件开发

### Arduino

- [Hat JoyC Example](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/Hat/JoyC/Arduino/JoyC)
- [Hat JoyC & RoverC-Pro Remote Control - with M5StickC](https://github.com/m5stack/M5-RoverC/tree/master/examples/RoverC_M5StickC/JoyC_%26_RoverC)

### UiFlow1

- [Hat JoyC UiFlow1 文档](/zh_CN/uiflow/blockly/hat/joyc)

### UiFlow2

- [Hat JoyC UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/hats/joyc.html)

### 通信协议

- 协议类型 I2C

- I2C Address: **0x38**

- [Hat JoyC I2C Protocol](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/protocol/U079/U079_I2C_PROTOCOL_CN.pdf)

### EasyLoader

| Easyloader                                   | 下载链接                                                                                                               | 备注 |
| -------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---- |
| Hat JoyC Easyloader                          | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/HAT/EasyLoader_JoyC_Test.exe)               | /    |
| Hat JoyC & RoverC Easyloader - with M5StickC | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/HAT/RoverC_Remote/RoverC%26JoyC_Remote.zip) | /    |

## 相关视频

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/HAT/JoyC.mp4" type="video/mp4">
</video>
