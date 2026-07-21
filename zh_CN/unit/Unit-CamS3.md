# Unit CamS3

<span class="product-sku">SKU:U174</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-CamS3/img-01d9c694-5514-4e0e-ae3e-7d965bba9125.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-CamS3/img-e2756f48-fc8a-4238-9635-c0c4a40d53c6.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-CamS3/img-1d83a5c3-42a7-4a05-a84f-d0cec95ff443.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-CamS3/img-4a3f8a65-3bda-4983-92c3-b2a05d0ecbc7.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-CamS3/img-ba8a8801-9034-49f2-b13a-98b460ffb887.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-CamS3/img-5bfb04b9-982a-4abd-9a48-fa813bc5e1e5.webp">
</PictureViewer>

## 描述

**Unit CamS3** 是一款基于 **ESP32S3** 模组的精简摄像头单元，支持 **WiFi 云端** 传输图像。它搭载了 8M PSRAM 和 16M Flash 内存，搭配 2MP 的摄像头 (OV2640)，拥有 DFOV 66.5° 的视角，能够以最高分辨率拍摄 1600x1200 的照片。内置 microSD 卡槽可用于存储图像及其他信息。内置 PDM 麦克风，能够录制声音。底部的 HY2.0-4P 端口引出 S3 内部 D+/D - 引脚，支持通过连接 M5Grove2USB-C 模块进行固件更新或 USB 串口通信。板载 2 个 1x3 排母引出了 ESP32S3 的程序下载口。原厂出厂固件提供了完整的拍摄上传 EZData 的功能，用户可以通过简单配置，便能实现远程免费的图像监控功能。本产品适用于远程监控、延时摄影、工业自动化等多个领域应用。

## 教程 & 快速上手

learn>| ![Unit CamS3](https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-CamS3/img-e2756f48-fc8a-4238-9635-c0c4a40d53c6.webp) | [Unit CamS3上手教程](/zh_CN/guide/wifi_camera/m5unitcams3/m5unitcams3) | 本教程将向你介绍，如何通过 Burner 向 M5CAMS3 设备烧录固件以及功能介绍 |

## 产品特性

- 基于模组 ESP32-S3-WROOM-1-N16R8，支持 WIFI
- WiFi 云端 EZDATA 或串口传输图像数据
- 搭载 2MP 摄像头 (OV2640)
- 内置 microSD 卡槽
- 内置 PDM 麦克风，支持声音录制功能
- 内置可编程指示灯

## 包装内容

- 1 x Unit CamS3
- 1 x Grove2USB-C
- 2 x 公对公面包线
- 1 x HY2.0-4P Grove 连接线 (20cm)
- 1 x LEGO 适配件

## 应用场景

- 远程监控
- 延时摄影
- 工业自动化

## 规格参数

| 规格                   | 参数                                                                     |
| ---------------------- | ------------------------------------------------------------------------ |
| ESP32-S3-WROOM-1-N16R8 | 双核 240 MHz@ 支持 WiFi，模块板载天线                                    |
| PSRAM                  | 8M PSRAM                                                                 |
| Flash                  | 16M Flash                                                                |
| 摄像头                 | 2MP 像素 @OV2640                                                         |
| OV2640 支持输出格式    | YUV (422/420) / YCbCr422，8 位压缩数据，RGB565/555，8/10 位 Raw RGB 数据 |
| DFOV                   | 66.5°                                                                    |
| MIC                    | PDM 麦克风 @MSM1261D4030HCPM                                             |
| 内存卡                 | microSD 卡                                                               |
| 工作温度               | 0 ~ 40°C                                                                 |
| 外壳材质               | 塑料                                                                     |
| 产品尺寸               | 40.0 x 24.0 x 11.0mm                                                     |
| 产品重量               | 8.3g                                                                     |
| 包装尺寸               | 138.0 x 93.0 x 12.0mm                                                    |
| 毛重                   | 13.7g                                                                    |

## 操作说明

\#> 下载程序：| 使用产品包装配备的[Grove2USB-C](/zh_CN/accessory/Grove2USB-C)进行下载时，通电之前，将配备的公对公面包线短接排母的 G0 和 GND 引脚进入下载模式，方可使用 Grove2USB-C 连接进行下载。

## 原理图

<img alt="schematics" src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-CamS3/img-e3213db4-1167-4f95-b6b5-9ff7a42d0111.png" width="100%" />

## 管脚映射

### Camera

| Interface            | Camera Pin | ESP32-S3 |
| -------------------- | ---------- | -------- |
| SCCB Clock           | SIOC       | G41      |
| SCCB Data            | SIOD       | G17      |
| System Clock         | XCLK       | G11      |
| Vertical Sync        | VSYNC      | G42      |
| Horizontal Reference | HREF       | G18      |
| Pixel Clock          | PCLK       | G12      |
| Pixel Data Bit 0     | D2         | G6       |
| Pixel Data Bit 1     | D3         | G15      |
| Pixel Data Bit 2     | D4         | G16      |
| Pixel Data Bit 3     | D5         | G7       |
| Pixel Data Bit 4     | D6         | G5       |
| Pixel Data Bit 5     | D7         | G10      |
| Pixel Data Bit 6     | D8         | G4       |
| Pixel Data Bit 7     | D9         | G13      |
| Camera Reset         | RESET      | G21      |
| Camera Power Down    | PWDN       | GND      |
| Power Supply 3.3V    | 3V3        | 3V3      |
| Ground               | GND        | GND      |

| CAMS3 Unit       | TX/D+ | RX/D- | CS  | MOSI | CLK | MISO | LED | MIC_CLK | MIC_DATA |
| ---------------- | ----- | ----- | --- | ---- | --- | ---- | --- | ------- | -------- |
| GROVE            | G20   | G19   |     |      |     |      |     |         |          |
| SD Card Socket   |       |       | G9  | G38  | G39 | G40  |     |         |          |
| Programmable LED |       |       |     |      |     |      | G14 |         |          |
| MIC              |       |       |     |      |     |      |     | G47     | G48      |

## 尺寸图

<img alt="module size" src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-CamS3/img-f1d342e1-5b43-40d6-bab8-438134d98477.jpg" width="100%" />

## 数据手册

- [OV2640](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/OV2640DS_en.pdf)
- [ESP32-S3-WROOM-1-N16R8](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-CamS3/ESP32-S3-WROOM-1-N16R8.pdf)
- [MSM1261D4030HCPM](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-CamS3/MSM1261D4030HCPM.pdf)

## 软件开发

### Arduino

- [Unit CamS3 User Demo](https://github.com/m5stack/UnitCamS3-UserDemo)

### EasyLoader

| Easyloader                     | 下载链接                                                                                                                    | 备注 |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------- | ---- |
| Unit CamS3 Firmware Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-CamS3/CamS3%20Unit%20Firmware.exe) | /    |

\#> 烧录固件之后，电脑或手机连接 “UnitCAMS3-WiFi” 的热点，在浏览器输入 192.168.4.1，点击 “Steam” 即可查看图像。内置 EZData 云端远程查看，录音，SD 卡存储等实用功能。

## 相关视频

- Unit CAMS3 图像远程查看以及延时摄影

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-CamS3/3c1447b3398128884d7bcbc0dce78fce.mp4" type="video/mp4"></video>

## 产品对比

|            | SoC                    | Memory                         | Camera     | MIC              | Download Mode                                                                                 |
| ---------- | ---------------------- | ------------------------------ | ---------- | ---------------- | --------------------------------------------------------------------------------------------- |
| CAM Unit   | ESP32-WROOM-32E        | 520 KB SRAM and 4 MB SPI flash | OV2640 2MP | /                | [ESP32-Downloader](/zh_CN/tool/usb_downloader)                                                |
| CAMS3 Unit | ESP32-S3-WROOM-1-N16R8 | 8M PSRAM and 16M Flash         | OV2640 2MP | MSM1261D4030HCPM | [ESP32-Downloader](/zh_CN/tool/usb_downloader) or [Grove2USB-C](/zh_CN/accessory/Grove2USB-C) |

如需对比 Unit CAM 系列产品信息，可访问[产品选型表](/zh_CN/products_selector/unit_cam_compare?select=U174)，勾选目标产品即可获取对比结果。选型表涵盖核心参数、功能特性等关键信息，支持多产品同步比对。
