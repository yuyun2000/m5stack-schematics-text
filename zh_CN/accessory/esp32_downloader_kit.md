# ESP32 Downloader Kit

<span class="product-sku">SKU:A105</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/accessory/esp32_downloader_kit/esp32_downloader_kit_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/accessory/esp32_downloader_kit/esp32_downloader_kit_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1106/A105-weight.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/accessory/esp32_downloader_kit/esp32_downloader_kit_03.webp">
</PictureViewer>

## 描述

**ESP32 Downloader Kit**是一款适用 ESP32/ESP8266 的 USB-TTL 转接板，使用芯片 CP2104/CH9102, 支持一键下载程序，无需手动复位芯片与管脚拉低操作。配套的插接板与排针零件，能够非常方便的为 ESP32/ESP8266 系列开发板或 M5Stack 系列产品进行程序烧录或是串口调试。

## 注意事项

\#>CP2104/CH9102F | 实际发货有 CP2104/CH9102F 两个芯片版本，功能与使用上并无差异。

## 产品特性

- Type-C 接口
- ESP32/ESP8266 程序下载器
- 匹配 M5Stack 多款产品 IO 顺序，直插烧录，无需接线 (UNIT CAM/STAMP 系列等)
- 接收 / 发送缓存区
- 符合 USB2.0 规范

## 包装内容

- 1 x ESP32 Downloader
- 1 x ESP32 CAM 引脚插接板
- 1 x 2.54-6P 排母座
- 2 x 2.54-3P 排针
- 1 x 杜邦线

## 规格参数

| 规格           | 参数                                                                                          |
| -------------- | --------------------------------------------------------------------------------------------- |
| USB-TTL IC     | CP2104/CH9102F                                                                                |
| USB 接口类型   | Type-C                                                                                        |
| 波特率         | 300bps to 2Mbps                                                                               |
| 支持的数据格式 | 数据位：5、6、7 和 8<br/>停止位：1、1.5 和 2<br/>奇偶校验：奇数，偶数，标记，空格，无奇偶校验 |
| 缓冲区         | 576 字节的接收缓冲区，576 字节发送缓冲区                                                      |
| 产品尺寸       | 33.0 x 16.0 x 3.0mm                                                                           |
| 产品重量       | 10.0g                                                                                         |
| 包装尺寸       | 138.0 x 93.0 x 6.0mm                                                                          |
| 毛重           | 11.0g                                                                                         |

## 操作说明

**使用示意:**

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/unit_cam/unit_cam_04.webp" width="70%">
<img src="https://static-cdn.m5stack.com/resource/docs/products/accessory/esp32_downloader_kit/esp32_downloader_kit_04.webp" width="70%">
<img src="https://static-cdn.m5stack.com/resource/docs/products/accessory/esp32_downloader_kit/esp32_downloader_kit_05.webp" width="70%">

<div class="product_pic">
<img src="https://static-cdn.m5stack.com/resource/docs/products/accessory/esp32_downloader_kit/esp32_downloader_kit_07.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/accessory/esp32_downloader_kit/esp32_downloader_kit_08.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/accessory/esp32_downloader_kit/esp32_downloader_kit_09.webp">
</div>

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/accessory/esp32_downloader_kit/esp32_downloader_kit_sch_01.webp" width="80%">

## 软件开发

### USB 驱动

\#> 点击下方连接下载匹配操作系统的驱动程序。 USB-TTL 烧录板目前存在两种驱动芯片版本，CP210X（适用于**CP2104**版本）/CP34X（适用于**CH9102**版本）驱动程序压缩包。在解压压缩包后，选择对应操作系统位数的安装包进行安装。(若您不确定您的设备所使用的 USB 芯片，可同时安装两种驱动。**CH9102_VCP_SER_MacOS v1.7**在安装过程中，可能出现报错，但实际上已经完成安装，忽略即可。) 在使用时，若出现无法正常下载程序 (提示超时或者是 Failed to write to target RAM) 的情况，可尝试重新安装设备驱动。

| 驱动名称                  | 适用驱动芯片 | 下载链接                                                                                             |
| ------------------------- | ------------ | ---------------------------------------------------------------------------------------------------- |
| CP210x_VCP_Windows        | CP2104       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CP210x_VCP_Windows.zip)     |
| CP210x_VCP_MacOS          | CP2104       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CP210x_VCP_MacOS.zip)       |
| CP210x_VCP_Linux          | CP2104       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CP210x_VCP_Linux.zip)       |
| CH9102_VCP_SER_Windows    | CH9102       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CH9102_VCP_SER_Windows.exe) |
| CH9102_VCP_SER_MacOS v1.7 | CH9102       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CH9102_VCP_MacOS_v1.7.zip)  |
