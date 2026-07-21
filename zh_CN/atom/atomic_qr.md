# Atom QRCode

<span class="product-sku">SKU:K041</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomic_qr/atomic_qr_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomic_qr/atomic_qr_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomic_qr/atomic_qr_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomic_qr/atomic_qr_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomic_qr/atomic_qr_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomic_qr/atomic_qr_06.webp">
</PictureViewer>

## 描述

**Atom QRCode** 是一款识别读取一维 / 二维码扫描模组套件，内含 Atom-Lite 主机，支持 6 类二维码和 19 类一维码，内置照明 LED，即使黑暗环境也能轻松识别，绿色 LED 方便对焦与瞄准，高分辨率 CMOS 成像有效识别精度达到 5mil，同时具备多种识读模式，您可以根据需要调整为自动连续触发或手动触发。模块自带蜂鸣器，在不同状态下有不同的提示音效。此外模块支持数据添加自定义前缀后缀，定义多国键盘、数据编辑等众多功能。该模块采用 TTL 进行通讯，可以方便的使用串口进行数据传输，无论使用 Arduino 还是 UiFlow 编程都能轻松上手，您可通过 Atom-Lite 内置的 ESP32 将扫描得到的数据以有线或无线的方式发送至接收端进行处理。

## 产品特性

- 基于 ESP32, 支持 WIFI
- 兼容 Atom-Matrix/Atom-Lite
- 支持 Arduino、UiFlow、Micropython
- 自带照明与对焦 LED
- UART/TTL 通讯
- 手动、自动扫描模式
- 灯光、声音提醒
- 多种输出格式
- 数据可预编辑和隐藏
- 丰富的自定义指令
- 支持原始数据 / GBK/Unicode 编码方式
- 二维码：QR Code,Mrico QR, Data Matrix, PDF417,Mrico PDF417,Aztec
- 一维码：EAN,UPC,Code 39,Code 93,Code 128,UCC/EAN 128, Codabar,Interleaved 2 of 5, ITF-6,ITF-14,ISBN,ISSN, MSI-Plessey,GS1 Databar,Code 11,Industrial 25,Standard 25,Plessey, Matrix 2 of 5

## 包装内容

- 1 x Atom-Lite
- 1 x Atomic QRCode Base
- 1 x M2 内六角扳手
- 1 x M2\*8 杯头机械牙螺丝
- 1 x USB Type-C 连接线 (20cm)

## 应用场景

- 收银扫描
- 条码录入
- 仓库盘点

## 规格参数

| 规格           | 参数                                                                                                                                                                                     |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 传感器         | 640x480 CMOS                                                                                                                                                                             |
| 照明           | 白光 LED                                                                                                                                                                                 |
| 对焦瞄准       | 绿光 LED                                                                                                                                                                                 |
| 识读二维码类型 | QR Code,Micro QR, Data Matrix, PDF417,Micro PDF417,Aztec                                                                                                                                 |
| 识读一维码类型 | EAN,UPC,Code 39,Code 93,Code 128,UCC/EAN 128, Codabar,Interleaved 2 of 5, ITF-6,ITF-14,ISBN,ISSN, MSI-Plessey, GS1 Databar,Code 11,Industrial 25, Standard 2 of 5,Plessey, Matrix 2 of 5 |
| 识别读取精度   | ≥5mil                                                                                                                                                                                    |
| 读取范围       | EAN-13: 50-200mm（13mil）, Code39: 40-90mm（5mil 10 字节）, QR Code: 25-240mm（20mil 16 字节）, Data Matrix: 50-90mm（10mil 20 字节）, PDF 417: 30-130mm（6.67mil 7 字节）               |
| 对比度         | ≥25%                                                                                                                                                                                     |
| 扫描角度       | 转角 360°, 仰角 ±55°, 偏角 ±55°                                                                                                                                                          |
| 视场角         | 水平 34°, 垂直 28°                                                                                                                                                                       |
| 通讯接口       | UART/TTL                                                                                                                                                                                 |
| 电压电流       | DC 3.3V/170mA, 待机 10mA                                                                                                                                                                 |
| 外壳材质       | Plastic （ PC ）                                                                                                                                                                         |
| 产品尺寸       | 48 x 24 x 18mm                                                                                                                                                                           |
| 产品重量       | 17g                                                                                                                                                                                      |
| 包装尺寸       | 55 x 55 x 20mm                                                                                                                                                                           |
| 毛重           | 37g                                                                                                                                                                                      |

## 操作说明

扫码模块在出厂时已经进行了配置，Atom-Lite 未内置程序，您需要在 Atom-Lite 中烧录以下示例程序。如果您需要更改配置，请参照用户手册扫描二维码进行配置，如果您恢复了出厂设置，请务必扫描确认您处于 TTL 通讯模式下，并且波特率设置正确。部分一维码和二维码的识读需要扫描二维码配置使能。

## 管脚映射

::m5-bus-table
| PIN     | LEFT | RIGHT | PIN |
| ------- | ---- | ----- | --- |
| 3V3     |      | 1     |     |
| UART_RX | 2    | 3     |     |
| UART_TX | 4    | 5     | 5V  |
| TRIG    | 6    | 7     | GND |
| DONE    | 8    | 9     |     |
::

## 数据手册

- [QR 模块串口控制指令表](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/atombase/AtomicQR/ATOM_QRCODE_CMD_CN.pdf)
- [用户手册 QR 模块二维码指令说明](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/atombase/AtomicQR/AtomicQR_Reader_CN.pdf)

## 软件开发

### Arduino

- [Atom QRCode Button Control Example](https://github.com/m5stack/M5Atom/tree/master/examples/ATOM_BASE/ATOM_QRCode/BTN_CONTROL)
- [Atom QRCode UART Control Example](https://github.com/m5stack/M5Atom/tree/master/examples/ATOM_BASE/ATOM_QRCode/UART_CMD_CONTROL)

### UiFlow1

- [Atom QRCode UiFlow1 文档](/zh_CN/uiflow/blockly/atomic_base/qrcode)

<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomic_qr/atomic_qr_uiflow_01.webp" width = "50%">

### EasyLoader

| Easyloader             | 下载链接                                                                                                              | 备注 |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------- | ---- |
| Atom QRCode Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/ATOM_BASE/EasyLoader_QRCODE_ATOM_BASE.exe) | /    |

## 相关视频

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/AtomBase/Atomic_QR.mp4" type="video/mp4" >
</video>
