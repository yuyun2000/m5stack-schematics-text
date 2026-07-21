# Unit Encoder

<span class="product-sku">SKU:U135</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/encoder/encoder_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/encoder/encoder_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/801/U135-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/encoder/encoder_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/encoder/encoder_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/encoder/encoder_06.webp">
</PictureViewer>

## 描述

**Unit Encoder** 是一款 I2C 通信接口的 **旋转编码器** 拓展单元。集成 30 位脉冲编码旋钮 （ 带按键输入 ） + 2x SK6812 可编程 RGB LED。内置的 STM32F030 主控集成编码器脉冲信号采集固件，用户可通过 I2C 读取操作直接获取编码数值，化繁为简。适用于刻度数值控制 / 音量调整等控制场景。

## 产品特性

- 30 位脉冲编码旋钮 (每旋转一周产生 30 个脉冲)
- 2 x SK6812 可编程 RGB LED
- 1 x 按键输入

## 包装内容

- 1 x Unit Encoder
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 人机交互
- 音量旋钮

## 规格参数

| 规格           | 参数                           |
| -------------- | ------------------------------ |
| MCU            | STM32F030F4P6                  |
| 通信接口       | I2C 通信 @ 0x40                |
| 脉冲编码旋钮   | 30 位脉冲编码旋钮 (带按键输入) |
| 可编程 RGB LED | 2 x SK6812                     |
| 工作电流       | 编码器工作 (DC 5V@17mA)        |
| 产品尺寸       | 32.0 x 24.0 x 25.4mm           |
| 产品重量       | 7.4g                           |
| 包装尺寸       | 138.0 x 93.0 x 25.0mm          |
| 毛重           | 12.3g                          |

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/encoder/encoder_sch_01.webp" width="80%">

## 管脚映射

### Unit Encoder

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 尺寸图

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/801/U135_Model_Size_page_01.png" width="100%">

## 软件开发

### Arduino

- [Unit Encoder Arduino 驱动库](https://github.com/m5stack/UNIT_ENCODER)
- [Unit Encoder Test Example with M5Core](https://github.com/m5stack/M5Unit-Encoder/blob/master/examples/Unit_Encoder_M5Core/Unit_Encoder_M5Core.ino)
- [Unit Encoder Test Example with M5Core2](https://github.com/m5stack/M5Unit-Encoder/blob/master/examples/Unit_Encoder_M5Core/Unit_Encoder_M5Core2.ino)

### UiFlow1

- [Unit Encoder UiFlow1 文档](/zh_CN/uiflow/blockly/unit/encoder)

### UiFlow2

- [Unit Encoder UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/encoder.html)

### 内置固件

- [Unit Encoder 内置固件](https://github.com/m5stack/M5UnitEncoder_Firmware)

### 通讯协议

- [Unit Encoder I2C 通信协议](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/801/Unit-Encoder_Protocol.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/801/Unit-Encoder_Protocol_page_01.png" width="70%">

## 相关视频

- 读取编码数值

<video id="example_video" controls>
  <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Unit/UNIT_ENCODER_VIDEO.mp4" type="video/mp4">
</video>
