# Atomic QRCode2 Base

<span class="product-sku">SKU:A133-B</span>

<PictureViewer>
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/Atomic%20QRCode2%20Base/4.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic QRCode2 Base/img-40c2a72e-205c-408d-b076-94c8bf1cada1.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic QRCode2 Base/img-a99f683a-1f76-4601-aca6-9c3286395abe.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic QRCode2 Base/img-8176ad63-ccb6-464e-a1df-81a24eb907f1.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic QRCode2 Base/img-b16ed71a-af7c-42c6-9f3f-b5922fe1c595.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic QRCode2 Base/img-3260dfb9-2fb5-48ab-a76c-089e8350aed5.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic QRCode2 Base/img-e4815a55-3f44-472a-87a5-e3e45a72a16d.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic QRCode2 Base/img-7c9d8c0d-6969-4b34-b3ce-78e3cb5d417f.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic QRCode2 Base/img-4fa8a3c1-a87c-432c-882b-3da0b78a004f.webp">
</PictureViewer>

## 描述

**Atomic QRCode2 Base** 是专为 ATOM 系列主机设计的一款一维 / 二维码扫描底座，支持市场上主流的 3 类二维码和 14 类一维码。该底座内置蜂鸣器和补光 LED，可在不同状态下提供音效提示，并通过红色 LED 辅助对焦与瞄准。模块采用 TTL 进行通讯，可以方便地使用串口进行数据传输。您可通过 M5Atom 主机内置的 ESP32，将扫描数据以有线或无线方式传输至接收端进行处理。底座背部配有磁铁、M3 螺丝孔和乐高兼容孔，提供多种安装选项。适用于物流、零售、制造等领域。

## 产品特性

- 支持 3 类二维码和 14 类一维码
- 内置蜂鸣器音效提示
- 内置照明 LED
- 高分辨率成像
- 对焦与瞄准功能

## 包装内容

- 1 x Atomic QRCode2 Base

## 应用场景

- 物流
- 零售
- 制造

## 规格参数

| 规格           | 参数                                                                                                                                      |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| 传感器         | 640x480 CMOS@M14 模组                                                                                                                     |
| 照明           | 白光 LED                                                                                                                                  |
| 对焦瞄准       | 红光 LED                                                                                                                                  |
| 识读二维码类型 | PDF417，QR Code，Data Matrix                                                                                                              |
| 识读一维码类型 | Code11, Code39, Code93, Code128, EAN-13, EAN-8, UPC-A, UPC-E, <br>Codabar, Interleaved 2 of 5, Matrix 2 of 5, Industrial 2 of 5, MSI, GS1 |
| 识别读取精度   | ≥5mil                                                                                                                                     |
| 打印对比度     | ≥ 20%                                                                                                                                     |
| 扫描角度       | 转角 360°，仰角 ± 55°，偏角 ± 55°                                                                                                         |
| 视场角         | 水平 34°，垂直 28°                                                                                                                        |
| 通讯接口       | UART@115200                                                                                                                               |
| 功耗测试       | 待机电流 (未加 ATOM 主机):DC 5V/116.57mA <br/>工作电流 (加上 Atom-Lite):DC 5V/174.18mA                                                    |
| 工作温度       | 0 ~ 40°C                                                                                                                                  |
| 外壳材质       | Plastic ( PC )                                                                                                                            |
| 产品尺寸       | 48 x 24 x 17.5mm                                                                                                                          |
| 包装尺寸       | 136 x 92 x 18mm                                                                                                                           |
| 产品重量       | 12g                                                                                                                                       |
| 毛重           | 14.2g                                                                                                                                     |

## 操作说明

- 二维码扫描测试用例

<img alt="schematics" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/Atomic%20QRCode2%20Base/78bbee031d4adb98bdc49035bd25add.png" width="50%" />

## 原理图

- [Atomic QRCode2 Base 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/536/SCH_AtomicQRCode_V2.0pdf.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/536/SCH_AtomicQRCode_V2.0pdf_sch_01.png">
</SchViewer>

## 管脚映射

::m5-bus-table
| PIN | LEFT | RIGHT | PIN     |
| --- | ---- | ----- | ------- |
|     |      | 1     | 3V3     |
|     | 2    | 3     | UART_RX |
|     | 4    | 5     | UART_TX |
| 5V  | 6    | 7     | TRIG    |
| GND | 8    | 9     |         |
::

## 尺寸图

<img alt="module size" src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic QRCode2 Base/img-2c572f0f-1ddb-4f41-931d-2c816f3e484b.png" width="100%" />

## 数据手册

- [QRCODE 模块数据手册](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-QRCode/M14%E5%AE%89%E8%A3%85%E4%BD%BF%E7%94%A8%E6%8C%87%E5%8D%97.pdf)

## 软件开发

### Arduino

- [Atomic QRCode2 Base Arduino 驱动库](https://github.com/m5stack/M5Unit-QRCode/blob/main/example/uart_mode/uart_mode.ino)
- [Atomic QRCode2 Base Arduino 快速上手](/zh_CN/arduino/projects/atomic/atomic_qrcode2_base)

### UiFlow1

- [Atomic QRCode2 Base UiFlow1 文档](/zh_CN/uiflow/blockly/atomic_base/qrcode2)

### UiFlow2

- [Atomic QRCode2 Base UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/base/qrcode2.html)

### 通信协议

- [AT指令手册](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/536/Atomic-QRCode2-Base-Protocol-CN.pdf)
- [条码读取范围表示例](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/Atomic%20QRCode2%20Base/Barcode_Reading_Range_Table_EN.pdf)
- [识别设备用户手册](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/536/A133-B_Atomic_QRCode2_Base_Reader_User_Manual-2.5_CN.pdf)
- [识读模块通讯编程](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/536/Barcode_Reader_Module_Command_Protocol_Programming_CN.pdf)

## 相关视频

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/Atomic%20QRCode2%20Base/A133-B%20QR%20CODE2%20BASE%20%E8%A7%86%E9%A2%91.mp4" type="video/mp4" >
</video>

## 产品对比

### 版本对比

| 产品                               | SKU    | 外壳           | QRCode                   | 通讯方式    |
| ---------------------------------- | ------ | -------------- | ------------------------ | ----------- |
| Atomic QRCode2 Base                | A133-B | Plastic (PC)   | 3 类二维码和 14 类一维码 | UART        |
| Atom QR-CODE_v1.1 (Excluding Atom) | A133   | Plastic ( PC ) | 6 类二维码和 19 类一维码 | UART        |
| Atom QR-CODE Kit                   | K041   | Nylon          | 6 类二维码和 19 类一维码 | UART        |
| Atom QR-CODE Kit V1.1              | K041-B | Plastic ( PC ) | 6 类二维码和 19 类一维码 | UART        |
| Unit-QRCode                        | U173   | Plastic ( PC ) | 3 类二维码和 14 类一维码 | I2C or UART |
