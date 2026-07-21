# AtomS3R-CAM

<span class="product-sku">SKU:C126-CAM</span>

<PictureViewer>
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3R%20Cam/4.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3R%20Cam/12.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3R%20Cam/15.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3R%20Cam/5.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3R%20Cam/7.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3R%20Cam/8.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3R%20Cam/10.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3R%20Cam/11.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3R%20Cam/13.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/681/C126-CAM-weight.jpg">
</PictureViewer>

## 描述

**AtomS3R-CAM** 是一款集成了摄像头的迷你物联网可编程控制器，内部集成了 **ESP32-S3-PICO-1-N8R8** 主控，集成 Wi-Fi 功能、8 MB 片上 **Flash** 和 8 MB **PSRAM**。它具有 5V 转 3.3V 的电源管理电路，并内置了三轴 **BMM150** 地磁传感器和六轴 **BMI270** 姿态传感器。此外，产品还搭载了 0.3MP 的 **GC0308** 摄像头，支持图像采集，并具有红外发射控制功能。摄像头前配备了保护玻璃，用于防尘并提高图像质量。与之前的产品相比，**AtomS3R-CAM** 的 **3D 天线** 经过增强，提供了更好的性能和更高的稳定性。该产品出厂配备了 **UVC** (USB Video Class) 功能固件，作为免驱 USB 摄像头使用，用户无需安装驱动即可通过 USB 接口直接使用摄像头。产品还包括 **USB Type-C** 接口用于供电和固件下载，并带有一个 **HY2.0-4P** 扩展端口。底部设计了六个 **GPIO** 和电源引脚，便于扩展。产品尺寸仅为 **24.0 x 24.0 x 13.5mm** ，适用于物联网设备监控、教育开发工具等嵌入式场景。

## 教程 & 快速上手

learn>| ![Arduino IDE](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/arduino_banner_01.png) | [Arduino IDE](/zh_CN/arduino/m5atoms3r-cam/program) | 本教程将向你介绍，如何通过 Arduino IDE 编程控制 AtomS3R-CAM 设备。 |

<!--
learn>| ![UiFlow2](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/uiflow2.0_banner_01.png) | [UiFlow2](/zh_CN/uiflow2/m5atoms3r-cam/program) | 本教程将向你介绍，如何通过 UiFlow2 图形化编程平台控制 AtomS3R-CAM 设备 |
-->

## 产品特性

- 集成 ESP32-S3-PICO-1-N8R8 主控
- 0.3MP GC0308 摄像头
- 九轴传感器系统（BMI270 六轴 + BMM150 三轴地磁传感器）
- 8MB Flash 和 8MB PSRAM
- 支持红外发射控制功能
- 可扩展的引脚与接口
- 开发平台
  - Arduino IDE
  - ESP-IDF
  - PlatformIO

## 包装内容

- 1 x AtomS3R-CAM

## 应用场景

- USB 免驱摄像头
- 运动检测方向感知
- 可穿戴设备
- 智能设备控制
- 物联网应用

## 规格参数

| 规格                      | 参数                                                                                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SoC                       | ESP32-S3-PICO-1-N8R8@双核 Xtensa LX7 处理器，主频高达 240MHz                                                                                                                    |
| USB                       | USB OTG, USB Serial/JTAG                                                                                                                                                        |
| Flash                     | 8MB                                                                                                                                                                             |
| PSRAM                     | 8MB Octal                                                                                                                                                                       |
| Wi-Fi                     | 2.4 GHz Wi-Fi                                                                                                                                                                   |
| 六轴姿态传感器 (BMI270)   | 精度：0.05% （加速度），0.05°/s （角速度） <br/>I2C 地址：0x68                                                                                                                  |
| 三轴地磁式传感器 (BMM150) | 精度：0.3 μT <br/>挂载在 BMI270 上，通过 BMI270 获取磁力计数据                                                                                                                  |
| 摄像头                    | GC0308<br/>最大帧率：30 帧 / 秒<br/>输出格式：YCbCr4:2:2，RGB565，Raw Bayer<br/>光圈值：F2.6<br/>分辨率：0.3MP<br/>传感器尺寸 (摄像头对角线长度)：1/6.5''<br/>视场角：FOV 57.6° |
| 摄像头面板材质            | 玻璃                                                                                                                                                                            |
| 红外 IR                   | ∠180° 时红外线发射距离：12.46m （无遮挡情况下）                                                                                                                                 |
| 休眠电流                  | GPIO-5V 供电：DC 5V@11.63 uA<br/>Grove-5V 供电：DC 5V@10.75 uA<br/>USB-5V 供电：DC 5V@92.50 uA (含 PD 电阻损耗)                                                                 |
| 底部预留 GPIO             | G5/G6/G7/G8/G38/G39                                                                                                                                                             |
| 工作温度                  | 0 ~ 40°C                                                                                                                                                                        |
| 产品尺寸                  | 24.0 x 24.0 x 13.5mm                                                                                                                                                            |
| 产品重量                  | 7.4g                                                                                                                                                                            |
| 包装尺寸                  | 85.0 x 65.0 x 14.3mm                                                                                                                                                            |
| 毛重                      | 13.6g                                                                                                                                                                           |

## 操作说明

?> BMM150 磁场干扰 | 带有磁铁的产品可能对 BMM150 磁场传感器造成干扰，导致读数异常。当搭配含有磁铁的 M5 主控设备时，需拆除磁铁，同时避免 BMM150 传感器放置在强磁场附近。

### 使能摄像头

摄像头初始化前，需要将**GPIO18**置为低电平以使能供电，该操作将同时将点亮电源指示灯。

### 进入下载模式

如需烧录固件，请长按复位按键（大约 2 秒）直到内部绿色 LED 灯亮起，便可松开，此时设备已进入下载模式，等待烧录。

<img alt="schematics" src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/681/AtomS3R-CAM_download_mode.gif" width="30%" />

### IMU 三轴方向示意图

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/681/IMU-AtomS3R-CAM.jpg" width="70%">

## 原理图

- [AtomS3R-CAM main board 原理图PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/681/main_board_schematic.pdf)
- [AtomS3R-CAM ext board 原理图PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/681/ext_board_schematic.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/681/main_board_schematic_page_01.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/681/ext_board_schematic_page_01.png">
</SchViewer>

## 管脚映射

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/681/C126-CAM_PinMap_01.jpg" width="100%" />

### BMI270 & IR

| ESP32-S3-PICO-1-N8R8 | G0      | G45     | G47        |
| -------------------- | ------- | ------- | ---------- |
| BMI270 (0x68)        | SYS_SCL | SYS_SDA |            |
| IR                   |         |         | IR_LED_DRV |

### BMM150

| BMI270 | BMI270_ASDx | BMI270_ASCx |
| ------ | ----------- | ----------- |
| BMM150 | A_SDA       | A_SCL       |

\#> BMM150 挂载于 BMI270 | 通过 BMI270 的 Sensor Hub 辅助 I2C 接口接入 BMM150，实现统一的 9 轴传感数据采集。

### GC0308

| GC0308  | ESP32-S3-PICO-1-N8R8 |
| ------- | -------------------- |
| CAM_SDA | G12                  |
| CAM_SCL | G9                   |
| VSYNC   | G10                  |
| HREF    | G14                  |
| Y9      | G13                  |
| XCLK    | G21                  |
| Y8      | G11                  |
| Y7      | G17                  |
| PCLK    | G40                  |
| Y6      | G4                   |
| Y2      | G3                   |
| Y5      | G48                  |
| Y3      | G42                  |
| Y4      | G46                  |
| POWER_N | G18                  |

### HY2.0-4P

::grove-table
| HY2.0-4P    | Black | Red | Yellow | White |
| ----------- | ----- | --- | ------ | ----- |
| PORT.CUSTOM | GND   | 5V  | G2     | G1    |
::

## 尺寸图

<img alt="module size" src="https://static-cdn.m5stack.com/resource/docs/products/core/AtomS3R Cam/img-1f8b0888-c56b-424c-95d3-b67a45015569.png" width="100%" />

## 结构文件

- [AtomS3R-CAM 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/C126-CAM_AtomS3R-CAM/Structures)

## 数据手册

- [ESP32-S3-PICO-1-N8R8](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3R/esp32-s3-pico-1_datasheet_en.pdf)
- [GC0308](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/K128%20CoreS3/GC0308.PDF)
- [BMI270](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/K128%20CoreS3/BMI270.PDF)
- [BMM150](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/K128%20CoreS3/BMM150.PDF)

## 软件开发

### Arduino

- [AtomS3R-CAM Arduino 快速上手](/zh_CN/arduino/m5atoms3r-cam/program)
- [AtomS3R-CAM Arduino 网络摄像头示例](https://github.com/m5stack/M5AtomS3/blob/main/examples/Basics/camera/camera.ino)

### PlatformIO

```bash
[env:m5stack-atoms3r]
platform = espressif32@6.7.0
board = esp32-s3-devkitc-1
framework = arduino
board_build.arduino.memory_type = qio_opi
build_flags =
    -DESP32S3
    -DBOARD_HAS_PSRAM
    -mfix-esp32-psram-cache-issue
    -DCORE_DEBUG_LEVEL=5
    -DARDUINO_USB_CDC_ON_BOOT=1
    -DARDUINO_USB_MODE=1
lib_deps =
    M5Unified=https://github.com/m5stack/M5Unified
```

### ESP-IDF

- [AtomS3R-CAM 出厂固件](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/681/ATOMS3R-CAM-UserDemo-M5Stack-20240927.zip)

\#> 出厂固件功能说明 | 出厂固件提供了`UVC`功能和`Wi-Fi图传`两种功能。<br/>UVC 功能可通过 USB 直连电脑，打开 PC 摄像头应用即可预览图像。<br/>WiFi 图传功能需连接设备发出的 AP：AtomS3R-CAM-WiFi，然后浏览器输入 192.168.4.1 即可以进入图传预览页面。

### Easyloader

| Easyloader                       | 下载链接                                                                                                                     | 备注 |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---- |
| AtomS3R-CAM User Demo Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3R%20Cam/AtomS3R-CAM-Demo-V0.1.exe) | /    |

## 相关视频

- AtomS3R-CAM 产品介绍以及案例展示

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3R%20Cam/C126-CAM.mp4" type="video/mp4"></video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=114650796524811&bvid=BV1q1T8zUEHK&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/FdTOMUm6Y0I?si=teYWSW3CiTDN-Pr_" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>

## 产品对比

::compare-table
| 产品对比 | [AtomS3R-M12](/zh_CN/core/AtomS3R-M12) ![AtomS3R-M12](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3R-M12/12.webp)                                                                                               | [AtomS3R-Cam](/zh_CN/core/AtomS3R%20Cam) ![AtomS3R-Cam](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3R%20Cam/12.webp)                                                                                                          |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 摄像头   | **图像传感器**: OV3660<br/>**最大帧率**: 30 帧 / 秒 (fps)<br/>**输出格式**: RAW RGB，RGB565/555/444，CCIR656，YCbCr422，和 compression<br/>**光圈值**: F2.4<br/>**分辨率**: 3MP (300 万像素)<br/>**焦距**: 1.8 ± 5% mm<br/>**视场角 (FOV)**: 120° | **图像传感器**: GC0308 <br/>**最大帧率**: 30 帧 / 秒 (fps)<br/>**输出格式**: YCbCr4:2:2，RGB565，Raw Bayer<br/>**光圈**: F2.6<br/>**分辨率**: 0.3MP (30 万像素)<br/>**传感器尺寸** (摄像头对角线长度): 1/6.5'' <br/>**焦距**: 2.43mm<br/>**视场角 (FOV)**: 57.6° |
| 分辨率   | 3MP                                                                                                                                                                                                                                               | 0.3MP                                                                                                                                                                                                                                                            |
| 通讯方式 | 支持 UVC 以及 Wi-Fi 等通讯方式                                                                                                                                                                                                                    | 支持 UVC 以及 Wi-Fi 等通讯方式                                                                                                                                                                                                                                   |
| SoC      | ESP32-S3-PICO-1-N8R8                                                                                                                                                                                                                              | ESP32-S3-PICO-1-N8R8                                                                                                                                                                                                                                             |
| 内存     | 8MB Flash + 8MB PSRAM                                                                                                                                                                                                                             | 8MB Flash + 8MB PSRAM                                                                                                                                                                                                                                            |
| 传感器   | BMI270 + BMM150                                                                                                                                                                                                                                   | BMI270 + BMM150                                                                                                                                                                                                                                                  |
| 天线     | 增强的 3D 天线                                                                                                                                                                                                                                    | 增强的 3D 天线                                                                                                                                                                                                                                                   |
::

如需对比 Atom 系列产品信息，可访问[产品选型表](/zh_CN/products_selector/m5atom_compare?select=C126)，勾选目标产品即可获取对比结果。选型表涵盖核心参数、功能特性等关键信息，支持多产品同步比对。
