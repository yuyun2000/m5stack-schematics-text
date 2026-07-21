# Faces QWERTY

<span class="product-sku">SKU:A003</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/faces_keyboard/faces_keyboard_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/faces_keyboard/faces_keyboard_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/faces_keyboard/faces_keyboard_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/faces_keyboard/faces_keyboard_04.webp">
</PictureViewer>

## 描述

**Faces QWERTY** 是适配 FACE_BOTTOM 的全功能键盘面板，共有 35 个按键，每个按键都可通过组合键复用，输出不同字符。内部集成 **MEGA328** 处理器，通过 I2C 通信协议 (0x08) 工作在从机模式下。"sym" 与 "Fn" 功能键用于上档切换，"aA" 功能键用于大小写切换，单击相应功能键指示灯常亮激活单字符输入，双击指示灯闪烁，可激活连续输入，再次单击恢复。

## 产品特性

- I2C 通讯 (0X08)
- 多功能按键复用
- 输入状态指示灯
- 开发平台 [UiFlow](http://flow.m5stack.com), [MicroPython](http://micropython.org/), [Arduino](http://www.arduino.cc)

## 包装内容

- 1 x Faces QWERTY

## 应用场景

- 数据录入
- 人机交互

## 规格参数

| 规格           | 参数                 |
| -------------- | -------------------- |
| 通信接口       | I2C 通信 @ 0x08      |
| MCU            | MEGA838P             |
| 通讯方式       | I2C (0x08)           |
| 按键布局       | QWERTY 全键盘        |
| 输入状态指示灯 | 蓝色 LED x 2         |
| 外壳材质       | Plastic (PC)         |
| 产品尺寸       | 58.2 x 54.2 x 10.4mm |
| 产品重量       | 21.0g                |
| 包装尺寸       | 95.0 x 65.0 x 25.0mm |
| 毛重           | 41.0g                |

## 原理图

### Faces QWERTY

<img src="https://static-cdn.m5stack.com/resource/docs/products/module/faces_keyboard/faces_keyboard_sch_01.webp" width="70%">

## 管脚映射

### Mega328 ISP 下载接口 Pin 脚定义

<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-cardkb/mega328_isp_sch_01.webp" width="30%" height="30%">

### Faces Pannel Bus

::m5-bus-table
| PIN      | LEFT | RIGHT | PIN      |
| -------- | ---- | ----- | -------- |
|          | 1    | 2     |          |
|          | 3    | 4     |          |
|          | 5    | 6     |          |
|          | 7    | 8     |          |
|          | 9    | 10    |          |
|          | 11   | 12    |          |
|          | 13   | 14    |          |
|          | 15   | 16    | SDA      |
|          | 17   | 18    | SCL      |
|          | 19   | 20    |          |
|          | 21   | 22    | INT      |
::

## 软件开发

### Arduino

- [Faces QWERTY Example with M5Core](https://github.com/m5stack/M5Stack/tree/master/examples/Face/KEYBOARD)

### UiFlow1

- [Faces QWERTY UiFlow1 文档](/zh_CN/uiflow/blockly/module/face_keyboard)

### 内置固件

- [Faces QWERTY 内置固件](https://github.com/m5stack/FACES-Firmware/blob/master/KeyBoard.ino)

### Easyloader

| Easyloader                                       | 下载链接                                                                                                           | 备注 |
| ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ---- |
| Faces GameBoy BladeBuster Easyloader with M5Core | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/M5Core/Faces_kit/Faces_GameBoy_BladeBuster.exe) | /    |
| Faces Factory Test with M5Core                   | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/CORE/EasyLoader_FACES_FactoryTest.exe)  | /    |

### 相关视频

<video id="example_video" controls>
  <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Core/FACES.mp4">
</video>
