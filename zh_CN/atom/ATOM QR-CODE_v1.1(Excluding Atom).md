# Atomic QRCode v1.1 Base

<span class="product-sku">SKU:A133</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/ATOM QR-CODE_v1.1(Excluding Atom)/img-3fe4e63e-ae76-4a9b-b3fc-948adb3c274d.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/ATOM QR-CODE_v1.1(Excluding Atom)/img-4da4eb9c-8f22-47b2-b97c-91dc62ecadd7.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/ATOM QR-CODE_v1.1(Excluding Atom)/img-c895862b-473f-4484-8dbe-03a4e957b6f2.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/ATOM QR-CODE_v1.1(Excluding Atom)/img-783b401d-f6c2-4651-b4bc-740e705cccc4.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/ATOM QR-CODE_v1.1(Excluding Atom)/img-f6bfd552-5d75-4b92-97bc-60aaeb4d24d8.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/ATOM QR-CODE_v1.1(Excluding Atom)/img-20615e1b-f27d-4cf3-a7b2-983f2406b113.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/ATOM QR-CODE_v1.1(Excluding Atom)/img-bbe08b70-add8-4eba-916a-9676c715b7e9.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/ATOM QR-CODE_v1.1(Excluding Atom)/img-da8b7f56-dfa5-443c-88f1-78d69d67afaf.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/ATOM QR-CODE_v1.1(Excluding Atom)/img-8ba7b8c5-dca9-4a89-948d-98fe0f9e0cda.jpg">
</PictureViewer>

## 描述

**Atomic QRCode v1.1 Base** 是一款识别读取一维 / 二维码扫描底座，支持 6 类二维码和 19 类一维码。内置照明 LED，即便处于黑暗环境也能轻松实现识别，绿色 LED 有助于对焦与瞄准。凭借高分辨率 CMOS 成像，有效识别精度达到 5mil ，同时具备多种识读模式，您能够依据需求将其调整为自动连续触发或者手动触发模式。模块自身带有蜂鸣器，在不同状态下会发出不同的提示音效。此外，该模块支持为数据添加自定义前缀后缀，还能定义多国键盘、进行数据编辑等诸多功能。此模块采用 TTL 进行通讯，可便捷地利用串口进行数据传输，不管是运用 Arduino 还是 UiFlow 编程，都易于上手操作。您可以通过 M5Atom 主机内置的 ESP32 ，把扫描获取到的数据以有线或者无线的方式发送至接收端来进行处理。

\#> 扫码注意事项 | 如果要启用特殊的码类别扫描要在手册里先扫描对应二维码的 Enable 启用二维码

## 产品特性

- 兼容 Atom-Matrix/Atom-Lite/Atom S3/AtomS3-Lite
- 自带照明与对焦 LED
- UART/TTL 通讯
- 手动、自动扫描模式
- 灯光、声音提醒
- 多种输出格式
- 数据可预编辑和隐藏
- 丰富的自定义指令
- 支持原始数据 / GBK/Unicode 编码方式
- 支持 Arduino/UiFlow

## 包装内容

- 1 x Atomic QRCode v1.1 Base

## 应用场景

- 收银扫描
- 条码录入
- 仓库盘点

## 规格参数

| 规格           | 参数                                                                                                                                                                                     |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 识读二维码类型 | QR Code,Micro QR, Data Matrix, PDF417,Micro PDF417,Aztec                                                                                                                                 |
| 识读一维码类型 | EAN,UPC,Code 39,Code 93,Code 128,UCC/EAN 128, Codabar,Interleaved 2 of 5, ITF-6,ITF-14,ISBN,ISSN, MSI-Plessey, GS1 Databar,Code 11,Industrial 25, Standard 2 of 5,Plessey, Matrix 2 of 5 |
| 识别读取精度   | ≥5mil                                                                                                                                                                                    |
| 读取范围       | EAN-13: 50-200mm (13mil), Code39: 40-90mm (5mil 10 字节), QR Code: 25-240mm (20mil 16 字节), Data Matrix: 50-90mm (10mil 20 字节), PDF 417: 30-130mm (6.67mil 7 字节)                    |
| 对比度         | ≥25%                                                                                                                                                                                     |
| 扫描角度       | 转角 360°, 仰角 ±55°, 偏角 ±55°                                                                                                                                                          |
| 视场角         | 水平 34°, 垂直 28°                                                                                                                                                                       |
| 通讯接口       | UART/TTL                                                                                                                                                                                 |
| 电压电流       | DC 3.3V/170mA, 待机 10mA                                                                                                                                                                 |
| 外壳材质       | Plastic ( PC )                                                                                                                                                                           |
| 产品尺寸       | 48 × 24 × 18mm                                                                                                                                                                           |
| 产品重量       | 12.0g                                                                                                                                                                                    |
| 包装尺寸       | 136 × 92 × 13mm                                                                                                                                                                          |
| 毛重           | 25.0g                                                                                                                                                                                    |

## 管脚映射

::m5-bus-table
| PIN     | LEFT | RIGHT | PIN |
| ------- | ---- | ----- | --- |
|         |      | 1     | 3V3 |
| UART_RX | 2    | 3     |     |
| UART_TX | 4    | 5     | 5V  |
| TRIG    | 6    | 7     | GND |
| DONE    | 8    | 9     |     |
::

## 数据手册

- [QR module serial control command list](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/atombase/AtomicQR/ATOM_QRCODE_CMD_EN.pdf)
- [User manual of QR code command](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/atombase/AtomicQR/AtomicQR_Reader_EN.pdf)

## 软件开发

### Arduino

- [Atom QRCode Button Control Example](https://github.com/m5stack/M5Atom/tree/master/examples/ATOM_BASE/ATOM_QRCode/BTN_CONTROL)
- [Atom QRCode UART Control Example](https://github.com/m5stack/M5Atom/tree/master/examples/ATOM_BASE/ATOM_QRCode/UART_CMD_CONTROL)

### UiFlow1

- [Atom QRCode UART Control Example](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/AtomBase/AtomicQR/UIFlow)

- [Atom QRCode Button Control Example](https://flow.m5stack.com/?examples=atom_base_qrcode_demo)

- [Atom QRCode 测试程序](/zh_CN/uiflow/blockly/atomic_base/qrcode)

### UiFlow2

- [Atomic QRCode Base UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/base/qrcode.html)

### EasyLoader

| Easyloader             | 下载链接                                                                                                              | 备注 |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------- | ---- |
| Atom QRCode Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/ATOM_BASE/EasyLoader_QRCODE_ATOM_BASE.exe) | /    |

## 相关视频

- 扫描各种不同的码

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/AtomBase/Atomic_QR.mp4" type="video/mp4"></video>

## 版本变更

| 上市日期 | 产品变动                       |
| -------- | ------------------------------ |
| 2023.7   | 不搭配主机 Atom-Lite, 优化电路 |
| -------  | 首次发售                       |
