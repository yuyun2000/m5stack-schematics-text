# Faces Gamepad

<span class="product-sku">SKU:A004</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/faces_gameboy/faces_gameboy_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/faces_gameboy/faces_gameboy_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/faces_gameboy/faces_gameboy_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/faces_gameboy/faces_gameboy_04.webp">
</PictureViewer>

## 描述

**Faces Gamepad** 是适配 FACE_BOTTOM 的游戏手柄面板。包含常用的上 / 下 / 左 / 右、A/B 按键和开始 / 暂停，8 个按键，适配 FC、GAMEBOY 等经典游戏主机的手柄布局，您可通过烧录游戏模拟器固件自由加载游戏，或自行编写游戏。面板内部集成**MEGA328**处理器，通过 I2C 通信协议 (0x08) 工作在从机模式下。

## 产品特性

- I2C 通讯 (0x08)
- 适配 FACE 底座
- 开发平台 [UiFlow](http://flow.m5stack.com), [MicroPython](http://micropython.org/), [Arduino](http://www.arduino.cc)

## 包装内容

- 1 x Faces Gamepad

## 应用场景

- 游戏手柄
- 人机交互

## 规格参数

| 规格     | 参数                                    |
| -------- | --------------------------------------- |
| 通信接口 | I2C 通信 @ 0x08                         |
| 按键布局 | 上 / 下 / 左 / 右 / A / B / 开始 / 暂停 |
| 外壳材质 | Plastic (PC)                            |
| 产品尺寸 | 58.2 x 54.2 x 10.4mm                    |
| 产品重量 | 18.0g                                   |
| 包装尺寸 | 95.0 x 65.0 x 25.0mm                    |
| 毛重     | 38.0g                                   |

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/module/faces_gameboy/faces_gameboy_sch_01.webp" width="70%">

## 管脚映射

### Mega328 ISP 下载接口 Pin 脚定义

<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-cardkb/mega328_isp_sch_01.webp" width="30%" height="30%">

### Faces Pannel Bus

::m5-bus-table
| PIN      | LEFT | RIGHT | PIN      |
| -------- | ---- | ----- | -------- |
| GND      | 1    | 2     |          |
|          | 3    | 4     | 3V3      |
|          | 5    | 6     |          |
|          | 7    | 8     |          |
|          | 9    | 10    |          |
|          | 11   | 12    | RXD      |
|          | 13   | 14    | TXD      |
|          | 15   | 16    | SDA      |
|          | 17   | 18    | SCL      |
|          | 19   | 20    |          |
|          | 21   | 22    | INT      |
::

## 软件开发

### 快速上手

- [GameBoy游戏烧录教程](/zh_CN/guide/hobby_kit/faces/gameboy_burn_a_nes_game)

### Arduino

- [Faces Gamepad Snake_Gameboy Example with M5Core](https://github.com/m5stack/M5Stack/tree/master/examples/Face/Snake_Gameboy)

### UiFlow1

- [Faces Gamepad UiFlow1 文档](/zh_CN/uiflow/blockly/module/face_gameboy)

### 内置固件

- [Faces Gamepad 内置固件](https://github.com/m5stack/FACES-Firmware/blob/master/GameBoy.ino)

### Easyloader

| Easyloader                                       | 下载链接                                                                                                           | 备注 |
| ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ---- |
| Faces GameBoy BladeBuster Easyloader with M5Core | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/M5Core/Faces_kit/Faces_GameBoy_BladeBuster.exe) | /    |
| Faces Factory Test with M5Core                   | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/CORE/EasyLoader_FACES_FactoryTest.exe)  | /    |

## 相关视频

<video id="example_video" controls>
  <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Core/FACES.mp4">
</video>
