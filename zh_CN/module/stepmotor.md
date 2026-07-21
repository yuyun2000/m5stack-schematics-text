# Module Stepmotor

<span class="product-sku">SKU:M012</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/stepmotor/stepmotor_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/stepmotor/stepmotor_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/stepmotor/stepmotor_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/stepmotor/stepmotor_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/stepmotor/stepmotor_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/stepmotor/stepmotor_06.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/stepmotor/stepmotor_07.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/stepmotor/stepmotor_08.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/stepmotor/stepmotor_09.webp">
</PictureViewer>

## 描述

**Module Stepmotor** 是 M5Stack 堆叠模块系列中的一款步进电机驱动模块。该模块能够通过 **GRBL** 库同时驱动 3 个步进电机。因此非常适合应用在运动控制项目。模块内置 MEGA328P ，并且搭载 **GRBL** 固件，通过 I2C (0x70) 与 M5Core 通信。
集成 3 片由 DRV8825 芯片组成的步进电机驱动板，一个简单但非常强大的电路板，可以控制一个双极步进电机，并允许微步进高达 1/32 步。

## 产品特性

- 电源输入：DC 9 ~ 24V
- 控制 3 路步进电机 **(X, Y, Z)**

## 包装内容

- 1 x Module Stepmotor

## 应用场景

- DIY 3D 打印机
- 搭建机械臂

## 规格参数

| 规格         | 参数                 |
| ------------ | -------------------- |
| DC 接口型号  | XT30                 |
| 通信接口     | I2C 通信 @ 0x70      |
| 电机接口规格 | HY2.0-4P             |
| 产品尺寸     | 54.2 x 54.2 x 12.8mm |
| 产品重量     | 24.0g                |
| 包装尺寸     | 60.0 x 57.0 x 17.0mm |
| 毛重         | 34.0g                |

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/module/stepmotor/stepmotor_sch_01.webp" width="80%">

## 管脚映射

### Mega328 ISP 下载接口 Pin 脚定义

<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-cardkb/mega328_isp_sch_01.webp" width="30%" height="30%">

### M5-Bus

::m5-bus-table
| PIN       | LEFT | RIGHT | PIN       |
| --------- | ---- | ----- | --------- |
| GND       | 1    | 2     |           |
| GND       | 3    | 4     |           |
| GND       | 5    | 6     |           |
|           | 7    | 8     | RS485_TX  |
|           | 9    | 10    |           |
|           | 11   | 12    | 3V3       |
|           | 13   | 14    |           |
| STEP_X    | 15   | 16    | DIR_X     |
| SDA       | 17   | 18    | SCL       |
|           | 19   | 20    |           |
| STEP_Y    | 21   | 22    | DIR_Y     |
| STEP_Z    | 23   | 24    | DIR_Z     |
| HPWR      | 25   | 26    | RS485_RX  |
| HPWR      | 27   | 28    | 5V        |
| HPWR      | 29   | 30    |           |
::

## 数据手册

- [DRV8825 Datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/DRV8825_en.pdf)

## 软件开发

### Arduino

- [Module Stepmotor Example with M5Core](https://github.com/m5stack/M5Stack/tree/master/examples/Modules/StepmotorGRBL_M012)

### UiFlow1

- [Module Stepmotor UiFlow1 文档](/zh_CN/uiflow/blockly/module/stepmotor)

### 内置固件

- [Module Stepmotor 内置固件](https://github.com/m5stack/stepmotor_module/tree/master/Firmware%20for%20stepmotor%20module/GRBL-Arduino-Library)

### Easyloader

| Easyloader                       | 下载链接                                                                                            | 备注 |
| -------------------------------- | --------------------------------------------------------------------------------------------------- | ---- |
| Module Stepmotor Test Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Module/EasyLoader_STEPMOTOR.exe) | /    |
