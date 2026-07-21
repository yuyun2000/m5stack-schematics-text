# Faces RFID

<span class="product-sku">SKU:A067</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/faces_rfid/faces_rfid_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/faces_rfid/faces_rfid_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/faces_rfid/faces_rfid_03.webp">
</PictureViewer>

## 描述

**Faces RFID** 是一款兼容 FACE 套件的无线射频识别面板 。内置**MFRC522**芯片，工作频率为 13.56 MHz 。支持读卡、写卡、识别、记录、对 RF 卡进行编码和授权等多个功能。利用磁场感应技术，能够实现非接触式双向信息交互、读取感应卡的信息并验证。

## 产品特性

- FACES 套件兼容
- I2C 通讯协议 (0x28)
- MFRC522

## 包装内容

- 1 x Faces RFID
- 1 x RFID 卡
- 1 x Fudan S50 卡

## 应用场景

- 智能家居门禁系统
- 车辆管理
- 智能交通
- 智能书架

## 规格参数

| 规格         | 参数                                                |
| ------------ | --------------------------------------------------- |
| 通信接口     | I2C 通信 @ 0x28                                     |
| 工作频率     | 13.56MHz                                            |
| I2C 速率     | 快速模式：最高 400Kbit/s/ 高速模式：最高 3400Kbit/s |
| 支持协议     | ISO14443A, MIFARE and NTAG                          |
| 数据保存时间 | > 10 年                                             |
| 读写距离     | < 20mm                                              |
| 材质         | Plastic (PC)                                        |
| 产品尺寸     | 58.2 x 54.2 x 10.0mm                                |
| 产品重量     | 18.4g                                               |
| 包装尺寸     | 95.0 x 65.0 x 25.0mm                                |
| 毛重         | 52.0g                                               |

## 原理图

- [Faces RFID 原理图 PDF](https://github.com/m5stack/M5-Schematic/blob/master/Modules/FACE_RFID.pdf)

<img src="https://static-cdn.m5stack.com/resource/docs/products/module/faces_rfid/faces_rfid_sch_01.webp" width="80%">

## 管脚映射

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

## 数据手册

- [MFRC522](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/MFRC522_en.pdf)

## 软件开发

### Arduino

- [Faces RFID Example with M5Core](https://github.com/m5stack/M5Stack/tree/master/examples/Face/RFID)

### UiFlow1

- [Faces RFID UiFlow1 文档](/zh_CN/uiflow/blockly/module/face_rfid)

### Easyloader

| Easyloader                                | 下载链接                                                                                             | 备注 |
| ----------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---- |
| Faces RFID Example Easyloader with M5Core | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Module/EasyLoader_FACES_RFID.exe) | /    |

## 相关视频

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/FACES-RFID.mp4" type="video/mp4">
</video>
