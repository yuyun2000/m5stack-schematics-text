# Faces Joystick

<span class="product-sku">SKU:A007</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/joystick/joystick_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/joystick/joystick_02.webp">
</PictureViewer>

## 描述

**Faces Joystick** 是一款兼容 FACE 套件的摇杆控制面板。通过推动面板上的摇杆能够进行角度、方向等数据的输入。使用 I2C 协议通讯，能够获取摇杆的偏移数据 (X, Y 坐标) ，以及中间按钮的状态。在摇杆的周围嵌入了由 12 个 LED 组成的 LED bar ，你可以根据你的需求自定义 LED 灯的发光形式。

## 产品特性

- 4 RGB Led
- I2C 通讯 (0x5E)
- 简洁的 API 接口

## 包装内容

- 1 x Faces Joystick

## 规格参数

| 规格     | 参数                 |
| -------- | -------------------- |
| 通信接口 | I2C 通信 @ 0x5E      |
| 产品尺寸 | 58.0 x 54.0 x 10.0mm |
| 产品重量 | 22.0g                |
| 包装尺寸 | 95.0 x 65.0 x 25.0mm |
| 毛重     | 50.0g                |

## 管脚映射

### Mega328 ISP 下载接口 Pin 脚定义

<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-cardkb/mega328_isp_sch_01.webp" width="30%" height="30%">

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
|     | 21   | 22    |     |
::

## 软件开发

### Arduino

- [Faces Joystick Example with M5Core](https://github.com/m5stack/M5Stack/tree/master/examples/Face/JOYSTICK)

### UiFlow1

- [Faces Joystick UiFlow1 文档](/zh_CN/uiflow/blockly/module/face_joystick)

### 内置固件

- [Faces Joystick 内置固件](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/Module/JOYSTICK/firmware_328p/FaceJoystick328)

### Easyloader

| Easyloader                                    | 下载链接                                                                                                 | 备注 |
| --------------------------------------------- | -------------------------------------------------------------------------------------------------------- | ---- |
| Faces Joystick Example Easyloader with M5Core | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Module/EasyLoader_FACES_joystick.exe) | /    |
