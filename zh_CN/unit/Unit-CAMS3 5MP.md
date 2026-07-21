# Unit CamS3-5MP

<span class="product-sku">SKU:U174-B</span>

<PictureViewer>
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-CAMS3%205MP/4.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-CAMS3%205MP/6.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1050/U174-B-package.jpg">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-CAMS3%205MP/3.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-CAMS3%205MP/5.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-CAMS3%205MP/7.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-CAMS3%205MP/8.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-CAMS3%205MP/9.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-CAMS3%205MP/11.webp">
</PictureViewer>

## 描述

**Unit CamS3-5MP** 是一款基于 ESP32S3 模组的精简摄像头单元，支持 WiFi 云端传输图像。它搭载了 8M PSRAM 内存和 16M Flash 闪存，搭配定制的 **5MP** 摄像头 PY260，拥有 88° DFoV 的视角，能够以最高分辨率拍摄 2592 x 1944 的照片。内置 microSD 卡槽可用于存储图像及其他信息。内置 PDM 麦克风，能够录制声音。底部的 HY2.0-4P 端口引出 ESP32-S3 内部 D+/D- 引脚，支持通过连接 [Grove to USBC](/zh_CN/accessory/Grove2USB-C) 模块进行固件更新或 USB 串口通信。板载 2 个 1x3 排母引出了 ESP32-S3 的程序下载口。出厂固件提供了完整的拍摄上传 **EzData** 的功能，用户只需简单配置，便能实现免费的远程图像监控功能。本产品适用于远程监控、延时摄影、工业自动化等多个领域的应用。

## 教程 & 快速上手

learn> | ![Arduino IDE](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/arduino_banner_01.png) | [Arduino IDE上手教程](/zh_CN/arduino/m5unitcams3_5mp/program) | 本教程将向你介绍，如何通过 Arduino IDE 编程控制 Unit CAMS3 5MP 设备。 |

learn>| ![Home Assistant](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/hhome_assistant_cover_02.jpg) | [Home Assistant](/zh_CN/homeassistant/camera/unit_cams3_5mp) | 本教程介绍如何将 Unit CamS3-5MP 摄像头模块接入 Home Assistant。 |

learn> | ![Unit CamS3-5MP](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-CAMS3%205MP/6.webp) | [Unit CamS3-5MP 恢复出厂固件教程](/zh_CN/guide/wifi_camera/m5unitcams3/m5unitcams3) | 本教程将向你介绍，如何通过 M5Burner 向 Unit CAMS3 5MP 设备烧录固件。 |

## 产品特性

- 基于模组 ESP32-S3-WROOM-1-N16R8，支持 Wi-Fi
- WiFi 云端 EzData 或串口传输图像数据
- 搭载 5MP 摄像头 PY260
- 内置 microSD 卡槽
- 内置 PDM 麦克风，支持声音录制功能
- 内置可编程指示灯

## 包装内容

- 1 x Unit CamS3-5MP
- 1 x Grove2USB-C
- 2 x 公对公面包线
- 1 x HY2.0-4P Grove 连接线 (20cm)
- 1 x LEGO 适配件

## 应用场景

- 远程监控
- 延时摄影
- 工业自动化

## 规格参数

| 规格                   | 参数                                  |
| ---------------------- | ------------------------------------- |
| ESP32-S3-WROOM-1-N16R8 | 双核 240 MHz 支持 Wi-Fi，模块板载天线 |
| PSRAM                  | 8M PSRAM                              |
| Flash                  | 16M Flash                             |
| 摄像头                 | 5MP PY260                             |
| 固定焦距               | 0.6m                                  |
| 支持输出格式           | JPEG                                  |
| DFoV                   | 88°                                   |
| MIC                    | PDM 麦克风 MSM1261D4030HCPM           |
| 支持内存卡类型         | microSD 卡                            |
| 工作温度               | 0 ~ 40°C                              |
| 产品尺寸               | 40.0 x 24.0 x 11.0mm                  |
| 产品重量               | 11.1g                                 |
| 包装尺寸               | 138.0 x 93.0 x 12.0mm                 |
| 毛重                   | 19.2g                                 |

## 操作说明

\#> 下载程序 | 使用产品配备的 [Grove2USB-C](/zh_CN/accessory/Grove2USB-C) 进行下载时，要在上电之前用配备的公对公面包线短接排母的 G0 和 GND 引脚，使设备进入下载模式。

## 原理图

- [Unit CamS3-5MP 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1050/SCH_UNIT_CAMS3_V1.0.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1050/SCH_UNIT_CAMS3_V1.0_page_01.png">
</SchViewer>

## 管脚映射

### HY2.0-4P

::grove-table
| HY2.0-4P  | Black | Red | Yellow | White |
| --------- | ----- | --- | ------ | ----- |
| UART PORT | GND   | 5V  | G20    | G19   |
::

### Camera

| Interface            | Camera Pin   | ESP32-S3 |
| -------------------- | ------------ | -------- |
| SCCB Clock           | SIO_C        | G41      |
| SCCB Data            | SIO_D        | G17      |
| System Clock         | XCLK         | G11      |
| Vertical Sync        | VSYNC        | G42      |
| Horizontal Reference | HREF         | G18      |
| Pixel Clock          | PCLK         | G12      |
| Pixel Data Bit 0     | Y2           | G6       |
| Pixel Data Bit 1     | Y3           | G15      |
| Pixel Data Bit 2     | Y4           | G16      |
| Pixel Data Bit 3     | Y5           | G7       |
| Pixel Data Bit 4     | Y6           | G5       |
| Pixel Data Bit 5     | Y7           | G10      |
| Pixel Data Bit 6     | Y8           | G4       |
| Pixel Data Bit 7     | Y9           | G13      |
| Camera Reset         | RESET        | G21      |
| Camera Power Down    | PWDN         | GND      |
| Power Supply         | AVDD / DOVDD | 2.8V     |
| Power Supply         | DVDD         | 1.2V     |
| Ground               | GND          | GND      |

| Unit CAMS3 5MP   | G19   | G20   | G9  | G38  | G39 | G40  | G14 | G47 | G48  |
| ---------------- | ----- | ----- | --- | ---- | --- | ---- | --- | --- | ---- |
| Grove            | RX/D- | TX/D+ |     |      |     |      |     |     |      |
| SD Card Socket   |       |       | CS  | MOSI | CLK | MISO |     |     |      |
| Programmable LED |       |       |     |      |     |      | LED |     |      |
| Mic              |       |       |     |      |     |      |     | CLK | DATA |

## 尺寸图

<img alt="module size" src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-CAMS3 5MP/img-92a0b5bb-a0c6-4604-8e2b-ca7856313280.jpg" width="100%" />

## 数据手册

- [ESP32-S3-WROOM-1-N16R8](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-CamS3/ESP32-S3-WROOM-1-N16R8.pdf)
- [MSM1261D4030HCPM (PDM Mic)](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-CamS3/MSM1261D4030HCPM.pdf)

## 软件开发

### Home Assistant

- [Home Assistant 集成](/zh_CN/homeassistant/camera/unit_cams3_5mp)

### ESP-IDF

- [Unit CamS3-5MP 出厂固件](https://github.com/m5stack/UnitCamS3-UserDemo/tree/unitcams3-5mp)

?> 兼容性 | Unit CamS3-5MP 摄像头不兼容 Unit CamS3 的程序。

## EasyLoader

| Easyloader                         | 下载链接                                                                                                                                | 备注 |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | ---- |
| Unit CamS3-5MP Firmware Easyloader | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-CAMS3%205MP/CAMS3%205MP%20Unit%20Firmware.exe) | /    |

\#> 烧录固件之后，电脑或手机连接名为 `UnitCAMS3-WiFi` 的热点，在浏览器输入 192.168.4.1，点击 `Stream` 即可查看图像。内置 EzData 云端远程查看、录音、SD 卡存储等实用功能。

## 相关视频

- Unit CamS3-5MP 基本功能介绍以及配置教程

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-CAMS3%205MP/9b258811e7e5a229195bc3b521f3f1c2.mp4" type="video/mp4"></video>

## 产品对比

| 产品                    | SoC                    | 内存和闪存                | 摄像头     | 麦克风           | 下载工具                                       | 下载方式 |
| ----------------------- | ---------------------- | ------------------------- | ---------- | ---------------- | ---------------------------------------------- | -------- |
| Unit CAM (U109)         | ESP32-WROOM-32E        | 520KB SRAM, 4MB SPI flash | OV2640 2MP | /                | [ESP32-Downloader](/zh_CN/tool/usb_downloader) | USB-TTL  |
| Unit CAMS3 (U174)       | ESP32-S3-WROOM-1-N16R8 | 8MB PSRAM, 16MB Flash     | OV2640 2MP | MSM1261D4030HCPM | [Grove2USB-C](/zh_CN/accessory/Grove2USB-C)    | CDC      |
| Unit CAMS3 5MP (U174-B) | ESP32-S3-WROOM-1-N16R8 | 8MB PSRAM, 16MB Flash     | PY260 5MP  | MSM1261D4030HCPM | [Grove2USB-C](/zh_CN/accessory/Grove2USB-C)    | CDC      |

如需对比 Unit CAM 系列产品信息，可访问[产品选型表](/zh_CN/products_selector/unit_cam_compare?select=U174-B)，勾选目标产品即可获取对比结果。选型表涵盖核心参数、功能特性等关键信息，支持多产品同步比对。
