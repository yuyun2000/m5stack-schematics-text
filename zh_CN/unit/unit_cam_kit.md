# Unit Camera DIY Kit

<span class="product-sku">SKU:U109-X</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/unit_cam_kit/unit_cam_kit_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/unit_cam_kit/unit_cam_kit_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/unit_cam_kit/unit_cam_kit_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/unit_cam_kit/unit_cam_kit_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/unit_cam_kit/unit_cam_kit_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/unit_cam_kit/unit_cam_kit_06.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/unit_cam_kit/unit_cam_kit_07.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/unit_cam_kit/unit_cam_kit_08.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/unit_cam_kit/unit_cam_kit_09.webp">
</PictureViewer>

## 描述

**Unit Camera DIY Kit** 是一款可 "自行拼装" 的 ESP32 WiFi 摄像头套件，套件内标配广角鱼眼 + 常规视角两个镜头模组，均采用 OV2640 图像传感器，最大支持输出 2MP 图像。支持 WiFi 或串口传图。DIY 外壳设计，开箱后你将获得一个功能强大的摄像头与一份动手拼接模型的乐趣。整机体积紧凑，具备高分辨率与调焦功能的它适合用于各种 IoT 图像拍摄应用。

- 高灵活性:

  - 支持镜头调焦
  - GROVE 拓展接口、可编程 RGB 灯

- 即插即用:
  - 出厂自带图像传输固件，支持 UART/WIFI 图片传输
  - 集成图像参数 API 接口 (白平衡，曝光，增益，尺寸等)
  - 配套 PC 端上位机调试工具
  - 支持 UiFlow 图形化编程平台一键调用，云端传输
  - 全面兼容 Arduino、ESP32-IDF 等主流开发平台

## 产品特性

- 即插即用
- 丰富的图像处理 API 接口
- 趣味 DIY 结构模型壳
- 内置 ESP32 MCU

## 包装内容

- 1 x Unit CAM 核心板
- 1 x OV2640 摄像头 (FOV:66.5°)
- 1 x OV2640 摄像头 (FOV:160°)
- 1 x 模型外壳配件
- 1 x 摄像头背夹 (兼容 LEGO)
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 远程监控
- 定时拍照

## 规格参数

| 规格                   | 参数                                                                                                           |
| ---------------------- | -------------------------------------------------------------------------------------------------------------- |
| ESP32-WROOM-32E        | 240MHz dual core，600 DMIPS，520KB SRAM，Wi-Fi                                                                 |
| Flash                  | 4MB                                                                                                            |
| 广角鱼眼镜头           | 焦距 1.0±5% mm<br/>光圈 2.2±5%<br/>镜头类型 1/4inch<br/>视场角 160°<br/>2MP<br/>畸变 -135%<br/>感光芯片 OV2640 |
| 常规视角镜头           | 焦距 4.8±5% mm<br/>光圈 2.4±5%<br/>镜头类型 1/4inch<br/>视场角 65°<br/>2MP<br/>畸变 <1%<br/>感光芯片 OV2640    |
| 固件默认通信方式       | UART: 115200bps 8N1                                                                                            |
| 摄像头固件默认输出图像 | QVGA@28fps、VGA@13fps、支持调节 (UXGA、SXGA、XGA 等更大尺寸图像输出)                                           |
| 传感器支持输出格式     | YUV (422/420) /YCbCr422，8 位压缩数据，RGB565/555，8-/10 位 Raw RGB 数据                                       |
| 产品重量               | 21.8g                                                                                                          |
| 毛重                   | 49.1g                                                                                                          |
| 模型板                 | 11 x 66 x 181mm                                                                                                |
| 鱼眼摄像头拼装整机尺寸 | 40 x 24 x 17.2mm                                                                                               |
| 常规摄像头拼装整机尺寸 | 40 x 24 x 11mm                                                                                                 |
| 包装尺寸               | 25 x 73 x 220mm                                                                                                |

## 操作说明

> Unit CAM 并不包含程序下载电路，用户需要下载为 ESP32 更新程序时，可以通过外部连接 USB-TTL 下载器进行程序烧录。[点击此处购买ESP32下载板](https://shop.m5stack.com/products/esp32-downloader-kit)

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/unit_cam/unit_cam_04.webp">

<img src="https://static-cdn.m5stack.com/resource/docs/products/accessory/esp32_downloader_kit/esp32_downloader_kit_08.webp" width="50%">

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/unit_cam/unit_cam_sch_01.webp" width="80%">

## 管脚映射

### Camera

| 接口                 | Camera Pin | Unit CAM |
| -------------------- | ---------- | -------- |
| SCCB Clock           | SIOC       | G23      |
| SCCB Data            | SIOD       | G25      |
| System Clock         | XCLK       | G27      |
| Vertical Sync        | VSYNC      | G22      |
| Horizontal Reference | HREF       | G26      |
| Pixel Clock          | PCLK       | G21      |
| Pixel Data Bit 0     | D0         | G32      |
| Pixel Data Bit 1     | D1         | G35      |
| Pixel Data Bit 2     | D2         | G34      |
| Pixel Data Bit 3     | D3         | G5       |
| Pixel Data Bit 4     | D4         | G39      |
| Pixel Data Bit 5     | D5         | G18      |
| Pixel Data Bit 6     | D6         | G36      |
| Pixel Data Bit 7     | D7         | G19      |
| Camera Reset         | RESET      | G15      |
| Camera Power Down    | PWDN       | -1       |
| Power Supply 3.3V    | 3V3        | 3V3      |
| Ground               | GND        | GND      |

### HY2.0-4P 接口

| HY2.0-4P | Unit CAM |
| -------- | -------- |
| RX       | G16      |
| TX       | G17      |
| 5V       | 5V       |
| GND      | GND      |

### LED (blue)

| LED | Unit CAM |
| --- | -------- |
| D1  | G4       |

## 数据手册

- [ESP32-WROOM-32E](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/unit_cam/ESP32-WROOM-32E-EN.pdf)
- [OV2640](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/OV2640DS_en.pdf)

## 软件开发

### 快速上手

- [Camera-Tool](/zh_CN/guide/wifi_camera/timer_cam/cameratool)
- [UART 传输 / Timer 定时拍摄](/zh_CN/guide/wifi_camera/timer_cam/uiflow)

### Arduino

?> 使用说明:| 该案例程序适用于 M5Core，用于通过 UART 接收来自 Unit Camera 的图像，请勿烧录至 Unit Camera。

- [Camera UART to Core](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/Unit/UNIT_CAM/CAM2CORE)

### ESP IDF

- [AWS-S3-PUT](https://github.com/m5stack/M5_Camera_Examples/tree/main/idf/AWS-S3-PUT)
- [Ali-OSS-PUT](https://github.com/m5stack/M5_Camera_Examples/tree/main/idf/Ali-OSS)
- [SMB-OSS-PUT](https://github.com/m5stack/M5_Camera_Examples/tree/main/idf/SMB-PUT)
- [Timer Wakeup](https://github.com/m5stack/M5_Camera_Examples/tree/main/idf/Wake-up)
- [HTTP Stream](https://github.com/m5stack/M5_Camera_Examples/tree/main/idf/http-stream)
- [Wireless-send](https://github.com/m5stack/M5_Camera_Examples/tree/main/idf/wireless-send)

## 相关视频

- 开箱手动拼装

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Unit/UnitCAM_XF.mp4" type="video/mp4">
</video>
