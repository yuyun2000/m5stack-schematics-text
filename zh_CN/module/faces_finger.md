# Faces Finger

<span class="product-sku">SKU:A066</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/faces_finger/faces_finger_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/faces_finger/faces_finger_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/faces_finger/faces_finger_02.webp">
</PictureViewer>

## 描述

**Faces Finger** 是一款兼容 FACE 套件的指纹识别面板。内部集成 FPC1020A 电容式指纹识别模组，具备多指纹录入、图像处理、特征值提取、指纹比对、搜索等功能。支持设定不同安全级别，能够为您的项目提供稳定可靠的指纹添加、验证、管理机制 。

## 产品特性

- FACES 套件兼容
- 串口通讯：UART2 (16/17)
- 电容式识别
- 指纹搜索、比对

## 包装内容

- 1 x Faces Finger

## 应用场景

- 指纹考勤机
- 指纹储物柜

## 规格参数

| 规格         | 参数               |
| ------------ | ------------------ |
| 感应阵列尺寸 | 160 x 160 像素     |
| 像素分辨率   | 256 灰度级 (8 位)  |
| 安全等级     | 0-9 级，默认等级 5 |
| 解析度       | 508DPI             |
| 产品重量     | 20g                |
| 毛重         | 43g                |
| 产品尺寸     | 58.2 x 54.2 x 10mm |
| 包装尺寸     | 95 x 65 x 25mm     |
| 材质         | Plastic ( PC )     |

## 原理图

- [Faces Finger 原理图 PDF](https://github.com/m5stack/M5-Schematic/blob/master/Modules/FACE_FINGER.pdf)

<SchViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/faces_finger/faces_finger_sch_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/faces_finger/faces_finger_sch_02.webp">
</SchViewer>

## 管脚映射

### Faces Pannel Bus

::m5-bus-table
| PIN      | LEFT | RIGHT | PIN      |
| -------- | ---- | ----- | -------- |
| GND      | 1    | 2     |          |
|          | 3    | 4     | 3V3      |
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

## 数据手册

- [FPC1020A](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/hat/1020A_datasheet_cn.pdf)

## 软件开发

### Arduino

- [Faces Finger with M5Core](https://github.com/m5stack/M5-FPC1020A/blob/master/examples/Module_Finger_M5Core/Module_Finger_M5Core.ino)

### UiFlow1

- [Faces Finger UiFlow1 文档](/zh_CN/uiflow/blockly/module/face_finger)

### 通信协议

- [Faces Finger 串口通信协议](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/biovo_fingerprint_Protocol.pdf)

### Easyloader

| Easyloader                                  | 下载链接                                                                                               | 备注 |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------------ | ---- |
| Faces Finger Example Easyloader with M5Core | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Module/EasyLoader_FACES_FINGER.exe) | /    |

## 相关视频

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/FACES-Finger.mp4" type="video/mp4">
</video>
