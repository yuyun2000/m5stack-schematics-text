# Faces Encoder

<span class="product-sku">SKU:A006</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/encoder/encoder_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/encoder/encoder_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/encoder/encoder_03.webp">
</PictureViewer>

## 描述

**Faces Encoder**是一款兼容 FACE 套件的旋钮控制面板。专为旋转编码控制而设计，其内部集成 Mega328 微处理器，在旋钮的周围嵌入了由 12 个 LED 组成的 LED 灯环。 M5Core 与 Faces Encoder 之间的串行通信协议是 I2C (地址：0x5E)。

## 产品特性

- RGB Led 显示
- I2C 通讯
- 简洁的 API 接口
- 内置 Mega328
- 编码器检测

## 包装内容

- 1 x Faces Encoder

## 规格参数

| 规格     | 参数                 |
| -------- | -------------------- |
| RGB LED  | x12                  |
| 通信接口 | I2C 通信 @ 0x5E      |
| 材质     | Plastic (PC)         |
| 产品尺寸 | 58.2 x 54.2 x 28.0mm |
| 产品重量 | 27.0g                |
| 包装尺寸 | 95.0 x 65.0 x 25.0mm |
| 毛重     | 47.0g                |

## 管脚映射

### Mega328 ISP 下载接口 Pin 脚定义

<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-cardkb/mega328_isp_sch_01.webp" width="30%" height="30%">

### Faces Pannel Bus

::m5-bus-table
| PIN | LEFT | RIGHT | PIN |
| --- | ---- | ----- | --- |
|     | 1    | 2     |     |
|     | 3    | 4     |     |
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

- [Faces Encoder Example with M5Core](https://github.com/m5stack/M5Stack/tree/master/examples/Face/ENCODER)

### UiFlow1

- [Faces Encoder UiFlow1 文档](/zh_CN/uiflow/blockly/module/face_encoder)

### 内置固件

- [Faces Encoder 内置固件](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/Module/ENCODER/firmware_328p/FacesEncoder328)

### Easyloader

| Easyloader                                   | 下载链接                                                                                                        | 备注 |
| -------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | ---- |
| Faces Encoder Example Easyloader with M5Core | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/MODULE/EasyLoader_FACES_Encoder.exe) | /    |

## 相关视频

<video id="example_video" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Module/FACES_ENCODER.mp4" type="video/mp4"></video>
