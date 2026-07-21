# USB Downloader

<span class="product-sku">SKU:A012</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/tool/usb_downloader/usb_downloader_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/tool/usb_downloader/usb_downloader_02.webp">
</PictureViewer>

## 描述

**USB Downloader** 是一款内置 CP2104 芯片的串口转 USB 烧录板， 集成自动下载电路，能够非常方便的为 ESP32 系列产品进行程序下载与程序调试。

## 产品特性

- USB-TTL
- Type-C 接口
- ESP32 程序下载器
- 波特率: 300bps to 2Mbps
- 支持的数据格式:
  - 数据位：5、6、7 和 8
  - 停止位：1、1.5 和 2
  - 奇偶校验：奇数，偶数，标记，空格，无奇偶校验
- 符合 USB2.0 规范
- 576 字节的接收缓冲区，576 字节发送缓冲区

## 包装内容

- 1 x USB Downloader

## 规格参数

| 规格     | 参数          |
| -------- | ------------- |
| 产品尺寸 | 40 x 30 x 5mm |
| 产品重量 | 3g            |
| 包装尺寸 | 80 x 50 x 3mm |
| 毛重     | 3g            |

## 操作说明

<img src="https://static-cdn.m5stack.com/resource/docs/products/tool/usb_downloader/usb_downloader_cover_01.webp">

<img src="https://static-cdn.m5stack.com/resource/docs/products/accessory/esp32_downloader_kit/esp32_downloader_kit_04.webp">

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/accessory/esp32_downloader_kit/esp32_downloader_kit_sch_01.webp" width="80%">

## 软件开发

### USB 驱动

\#> 点击下方连接下载匹配操作系统的驱动程序。 USB-TTL 烧录板目前存在两种驱动芯片版本，CP210X (适用于`CP2104`版本)/CP34X (适用于`CH9102`版本) 驱动程序压缩包。在解压压缩包后，选择对应操作系统位数的安装包进行安装。(若您不确定您的设备所使用的 USB 芯片，可同时安装两种驱动。`CH9102_VCP_SER_MacOS v1.7`在安装过程中，可能出现报错，但实际上已经完成安装，忽略即可。) 在使用时，若出现无法正常下载程序 (提示超时或者是 Failed to write to target RAM) 的情况，可尝试重新安装设备驱动。

| 驱动名称                  | 适用驱动芯片 | 下载链接                                                                                             |
| ------------------------- | ------------ | ---------------------------------------------------------------------------------------------------- |
| CP210x_VCP_Windows        | CP2104       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CP210x_VCP_Windows.zip)     |
| CP210x_VCP_MacOS          | CP2104       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CP210x_VCP_MacOS.zip)       |
| CP210x_VCP_Linux          | CP2104       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CP210x_VCP_Linux.zip)       |
| CH9102_VCP_SER_Windows    | CH9102       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CH9102_VCP_SER_Windows.exe) |
| CH9102_VCP_SER_MacOS v1.7 | CH9102       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CH9102_VCP_MacOS_v1.7.zip)  |
