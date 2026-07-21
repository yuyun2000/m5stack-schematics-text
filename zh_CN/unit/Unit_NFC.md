# Unit NFC

<span class="product-sku">SKU:U216</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1229/U216_Unit-NFC-main-pictures_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1229/U216_Unit-NFC-main-pictures_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1229/U216_Unit-NFC-main-pictures_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1229/U216_Unit-NFC-main-pictures_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1229/U216_Unit-NFC-main-pictures_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1229/U216_Unit-NFC-main-pictures_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1229/U216_Unit-NFC-main-pictures_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1229/U216_Unit-NFC-main-pictures_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1229/U216_Unit-NFC-main-pictures_09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1229/U216_Unit-NFC-main-pictures_10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1229/U216_Unit-NFC-main-pictures_11.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1229/U216_Unit-NFC-main-pictures_12.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1229/U216-weight.jpg">
</PictureViewer>

## 描述

**Unit NFC**是一款基于 13.56MHz 频段的近场通信读写单元。模块内置 ST25R3916 高性能 NFC 前端芯片，支持 ISO14443A、ISO14443B、FeliCa™和 ISO15693 主流协议，可对各类 NFC/RFID 标签与卡片进行稳定读写和数据交互。芯片支持读卡器模式、卡模拟模式及自定义协议，具备自动天线调谐、高灵敏接收与完备的协议处理能力。
该单元采用 I2C 接口与主控设备通信，数据传输可靠稳定。产品采用 LEGO 兼容孔设计，便于结构集成与螺丝固定安装，适用于门禁系统、身份认证、智能交通等各类近场通信与信息核验场景。

## 产品特性

- 13.56MHz 高频近场通信
- 搭载 ST25R3916 高性能芯片
- 支持 ISO14443A、ISO14443B、FeliCa™和 ISO15693 协议
- 支持三种模式：读写器 / 卡模拟 / 自定义协议
- I2C 通信接口
- LEGO 兼容孔设计
- 开发平台
  - UiFlow2
  - Arduino IDE

## 包装内容

- 1 x Unit NFC
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 门禁系统
- 身份识别
- 智能交通

## 规格参数

| 规格     | 参数                                                                                                                |
| -------- | ------------------------------------------------------------------------------------------------------------------- |
| IC 类型  | ST25R3916-AQWT                                                                                                      |
| 工作频率 | 13.56MHz                                                                                                            |
| 通信接口 | I2C 通信 @ 0x50 （100K / 400K）                                                                                     |
| 支持协议 | **读写器模式**：NFC-A/B（兼容 ISO14443A/B）、NFC-F（FeliCa™）、NFC-V（ISO15693 ）<br>**卡模拟模式**：NFC-A / NFC-F  |
| 读写距离 | ≤ 40mm                                                                                                              |
| 功耗     | 休眠：5V @ 19.33uA<br>上电未设置：5V @ 19.79uA<br>连续读卡：5V @ 67.65mA<br>间断读卡：5V @ 66.48mA                  |
| 产品尺寸 | 48.0 x 24.0x 8.0mm                                                                                                  |
| 产品重量 | 5.9g                                                                                                                |
| 包装尺寸 | 138.0 x 93.0 x 9.0mm                                                                                                |
| 毛重     | 11.5g                                                                                                               |

## 认证信息

- CE/FCC/RoHS/WEEE/MIC

## 原理图

- [Unit NFC 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1229/SCH_Unit_NFC_V0.1_2025_11_28_12_15_35.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1229/SCH_Unit_NFC_V0.1_2025_11_28_12_15_35_page_01.png">
</SchViewer>

## 尺寸图

- [Unit NFC 模型尺寸 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1229/u216unitnfc-model-size.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1229/u216unitnfc-model-size_page_01.png">
</SchViewer>

## 管脚映射

### Unit NFC

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 软件开发

### Arduino

- [Unit NFC Arduino 驱动库](https://github.com/m5stack/M5Unit-NFC)
- [Unit NFC Arduino 快速上手](/zh_CN/arduino/projects/unit/unit_nfc)

## 数据手册

- [ST25R3916](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1229/st25r3916_datasheet.pdf)

## 相关视频

- Unit NFC 产品介绍以及功能展示

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1229/U216-Unit-NFC-video-ZH.mp4" type="video/mp4"></video>
