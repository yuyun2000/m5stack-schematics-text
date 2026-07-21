# Faces Calculator

<span class="product-sku">SKU:A005</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/faces_calculator/faces_calculator_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/faces_calculator/faces_calculator_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/faces_calculator/faces_calculator_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/faces_calculator/faces_calculator_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/faces_calculator/faces_calculator_05.webp">
</PictureViewer>

## 描述

**Faces Calculator** 是适配 FACE_BOTTOM 的全功能计算器面板，可用于数学计算或自定义按键功能。面板采用 4 \* 5 按键布局设计，涵盖数学计算所需的基本功能按键，您也可以通过修改固件将其重新映射为自定义的功能按键。面板内部集成 **MEGA328** 处理器，通过 I2C 通信协议 (0x08) 工作在从机模式下。

## 产品特性

- I2C 通讯 (0x08)
- 数字键盘输入
- 开发平台 [UiFlow](http://flow.m5stack.com), [MicroPython](http://micropython.org/), [Arduino](http://www.arduino.cc)

## 包装内容

- 1 x Faces Calculator

## 应用场景

- 数据录入
- 计算器
- 人机交互

## 规格参数

| 规格     | 参数                 |
| -------- | -------------------- |
| 通信接口 | I2C 通信 @ 0x08      |
| 按键布局 | 20 按键              |
| 外壳材质 | Plastic （PC）       |
| 产品尺寸 | 58.2 x 54.2 x 10.4mm |
| 产品重量 | 20.0g                |
| 包装尺寸 | 95.0 x 65.0 x 25.0mm |
| 毛重     | 40.0g                |

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/module/faces_calculator/faces_calculator_sch_01.webp" width="70%">

## 管脚映射

### Mega328 ISP 下载接口 Pin 脚定义

<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-cardkb/mega328_isp_sch_01.webp" width="30%">

### Faces Pannel Bus

::m5-bus-table
| PIN | LEFT | RIGHT | PIN |
| --- | ---- | ----- | --- |
| GND | 1    | 2     |     |
|     | 3    | 4     | 3V3 |
|     | 5    | 6     |     |
|     | 7    | 8     |     |
|     | 9    | 10    |     |
|     | 11   | 12    |     |
|     | 13   | 14    |     |
|     | 15   | 16    | SDA |
|     | 17   | 18    | SCL |
|     | 19   | 20    |     |
|     | 21   | 22    | INT |
::

## 软件开发

### Arduino

- [Faces Calculator 测试程序](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/Module/CALCULATOR)

### UiFlow1

- [Faces Calculator UiFlow1 文档](/zh_CN/uiflow/blockly/module/face_calculator)

### 内置固件

- [Faces Calculator 内置固件](https://github.com/m5stack/FACES-Firmware/blob/master/Calculator.ino)

### Easyloader

| Easyloader                                      | 下载链接                                                                                                          | 备注 |
| ----------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ---- |
| Faces Calculator Example Easyloader with M5Core | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/CORE/EasyLoader_FACES_FactoryTest.exe) | /    |

## 相关视频

<video id="example_video" controls>
  <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Core/FACES.mp4">
</video>
