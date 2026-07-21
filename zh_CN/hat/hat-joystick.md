# Hat Joystick

<span class="product-sku">SKU:U073</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-joystick/hat-joystick_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-joystick/hat-joystick_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-joystick/hat-joystick_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-joystick/hat-joystick_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-joystick/hat-joystick_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-joystick/hat-joystick_06.webp">
</PictureViewer>

## 描述

**Hat Joystick** 是一款专为 M5StickC 设计的摇杆模块。内嵌 STM32F030F4 主控芯片，采用 I2C 通信协议与主机 M5StickC 进行数据传输。这个拥有迷你体积的遥杆模块支持进行全方位的角度偏移与中心按压，并输出角度偏移数据以及开关数字信号。采用 HAT 系列统一的插接式设计与 M5StickC 可靠连接，用最精简的方式，获得更多人机交互输入体验。

## 产品特性

- 内嵌 STM32F030F4
- 通信协议：I2C (地址：0x38)
- 支持全方位偏移 / 中心按键

## 包装内容

- 1 x Hat Joystick
- 1 x 双面胶

## 应用场景

- 游戏控制器
- 无线摇杆设备

## 规格参数

| 规格     | 参数                  |
| -------- | --------------------- |
| MCU      | STM32F030F4P6         |
| 通信接口 | I2C 通信 @ 0x38       |
| 产品尺寸 | 34.9 x 24.0 x 16.7mm  |
| 产品重量 | 8.5g                  |
| 包装尺寸 | 138.0 x 93.0 x 18.0mm |
| 毛重     | 10.8g                 |

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-joystick/hat-joystick_sch_01.webp" width="60%">

## 管脚映射

| M5StickC     | G0  | G26 | 3.3V | GND |
| ------------ | --- | --- | ---- | --- |
| Joystick HAT | SDA | SCL | 3.3V | GND |

## 尺寸图

[Hat Joystick 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/868/hatjoystick.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/868/hatjoystick_page_01.png" width="100%">

## 软件开发

### Arduino

- [Hat Joystick Example](https://github.com/m5stack/M5StickC/tree/master/examples/Hat/Joystick)

### UiFlow1

- [Hat Joystick UiFlow1 文档](/zh_CN/uiflow/blockly/hat/joystick)

### UiFlow2

- [Hat Joystick UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/hats/joystick.html)

### 通信协议

<mark>I2C 地址: 0x38</mark>

寄存器:

0x01 只读 4 bytes, 单轴数值 0 ~ 4096

`0: x轴原始数据低八位`

`1: x轴原始数据高八位`

`2: y轴原始数据低八位`

`3: y轴原始数据高八位`

0x02 只读 3 bytes

`0: x轴换算后数据 ( -127 ~ 127)`

`1: y轴换算后数据 (-127 ~ 127)`

`2: 0 or 1 (按键按下为0, 松开为1)`

0x03 只写 1 bytes

`0x00: 普通模式`

`0x01: 中心点校零`

`0x02: 最大值校准(需手动旋转摇杆获取最大值)`

`0x03: 保存中心点及最大值数据至flash, 保存后恢复至普通模式 `

> 摇杆校准方法：先 i2c 写寄存器 0x03 然后发送 0x02, 摇杆绕上下左右反复转圈几次，然后寄存器 0x03 写 0x03 保存.

### EasyLoader

| Easyloader              | 下载链接                                                                                                     | 备注 |
| ----------------------- | ------------------------------------------------------------------------------------------------------------ | ---- |
| Hat Joystick Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/HAT/Joystick/EasyLoader_Joystick_HAT.exe) | /    |

## 相关视频

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/HAT/Joystick_HAT.mp4" type="video/mp4">
</video>
