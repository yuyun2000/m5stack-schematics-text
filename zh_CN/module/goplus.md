# Module GoPlus

<span class="product-sku">SKU:M025</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/goplus/goplus_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/goplus/goplus_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/goplus/goplus_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/goplus/goplus_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/goplus/goplus_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/goplus/goplus_06.webp">
</PictureViewer>

## 描述

**Module GoPlus** 是 M5Stack 堆叠模块系列中的一款，功能增强型模块。集成 **MEGA328P** 与 **LV8548MC** 电机驱动芯片，整合 Module、Units 功能 （SERVO，PbHUB，IR） 。配备 2 通道直流电机驱动、 4 通道舵机驱动接口、红外收发器、3 个扩展端口 B （GPIO 端口）。具备多种功能特性，能够帮助你快速搭建功能强大的电机应用。

### 产品特性

- 2 x 直流电机驱动通道
- 4 x 舵机驱动通道
- IR 发射 & 接收
- 3 x 拓展 PORT B
- MEGA328P
- LV8548MC
- 通信协议：I2C (0x61)

### 包装内容

- 1 x Module GoPlus

## 规格参数

| 规格     | 参数           |
| -------- | -------------- |
| 产品重量 | 28g            |
| 毛重     | 43g            |
| 产品尺寸 | 54 x 54 x 13mm |
| 包装尺寸 | 60 x 57 x 17mm |

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/module/goplus/goplus_sch_01.webp" width="80%">

## 管脚映射

### Mega328 ISP 下载接口 Pin 脚定义

<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-cardkb/mega328_isp_sch_01.webp" width="30%" height="30%">

### M5-Bus

::m5-bus-table
| PIN      | LEFT | RIGHT | PIN      |
| -------- | ---- | ----- | -------- |
| GND      | 1    | 2     | IR_R     |
| GND      | 3    | 4     |          |
| GND      | 5    | 6     |          |
|          | 7    | 8     |          |
|          | 9    | 10    |          |
|          | 11   | 12    | 3V3      |
|          | 13   | 14    |          |
|          | 15   | 16    |          |
| SDA      | 17   | 18    | SCL      |
|          | 19   | 20    |          |
|          | 21   | 22    | IR_S     |
|          | 23   | 24    |          |
|          | 25   | 26    |          |
|          | 27   | 28    | 5V       |
|          | 29   | 30    |          |
::

## 数据手册

- [LV8548MC](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/LV8548MC-D.PDF)

## 软件开发

### Arduino

- [Module GoPlus 测试程序](https://github.com/m5stack/GoPlus/tree/master/test)

### UiFlow1

- [Module GoPlus UiFlow1 Example](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/Module/GOPLUS/UIFLOW).

<img src="https://static-cdn.m5stack.com/resource/docs/products/module/goplus/goplus_uiflow_01.webp" width="65%">

### 通信协议

- [Module GoPlus I2C Protocol](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/GoPlus_I2C_Protocol%20operation%20instructions.pdf)

### Easyloader

| Easyloader                                   | 下载链接                                                                                         | 备注 |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------ | ---- |
| Module GoPlus Example Easyloader with M5Core | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Module/EasyLoader_GOPLUS.exe) | /    |
