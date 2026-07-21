# TimerCamera

<span class="product-sku">SKU:U082</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/timercam/timercam_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/timercam/timercam_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/timercam/timercam_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/timercam/timercam_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/timercam/timercam_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/timercam/timercam_06.webp">
</PictureViewer>

## 描述

**TimerCamera** 是一款基于 ESP32-D0WDQ6-V3 的摄像头模块，板载 8M PSRAM，采用 3MP 的摄像头 (OV3660)，DFOV 66.5°，最高可实现拍摄 2048x1536 分辨率的照片。带有状态指示灯与 RESET 按键，主打超低功耗设计，通过 RTC ( BM8563 ) 可实现定时休眠与唤醒，休眠电流可低至 2μA。板上预留电池接口，用户可自行接入电池供电。模块支持 WiFi 图像传输和 USB 端口调试，底部 HY2.0-4P 端口输出，可连接其他外设。通过 M5Burner 烧录固件，可直接使用 Camera-Tool 对 **TimerCamera** 进行设置，也可在 UiFlow 中对 **TimerCamera** 数据进行处理。

## 产品特性

- 基于 ESP32 设计
- WIFI 图像传输
- 定时休眠唤醒
- 状态指示灯
- 超低功耗设计
- 编程平台：ESP-IDF/Arduino/UiFlow

## 包装内容

- 1 x TimerCamera

## 应用场景

- 定时拍照
- 远程监控

## 规格参数

| 规格         | 参数                                              |
| ------------ | ------------------------------------------------- |
| PSRAM        | 8MB Quad                                          |
| Flash        | 4M                                                |
| 图像传感器   | OV3660                                            |
| 最大分辨率   | 3MP                                               |
| 输出格式     | 8-/10-Bit RAW，RGB and YCbCr output，compression. |
| DFOV         | 66.5°                                             |
| 电池接口规格 | SH1.0-2P                                          |
| 产品尺寸     | 45 x 20 x 12mm                                    |
| 产品重量     | 6g                                                |
| 包装尺寸     | 60 x 60 x 15mm                                    |
| 毛重         | 17g                                               |

## 操作说明

> Timer Camera 系列采用的低功耗电源管理方案与 CORE 与 StickC 设备有所不同，使用时，PWR 按键作为开机按键使用 (长按 2s)，如需要使设备关机，则需要通过软件 API 或是按下 PCB 板上的复位按键。当使用外部供电时，设备将保持开机状态。

## 原理图

- [TimerCamera 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1042/Sch_M5TimerCAM.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1042/Sch_M5TimerCAM_page_01.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1042/Sch_M5TimerCAM_page_02.png">
</SchViewer>

## 管脚映射

### OV3660

| 接口                 | Camera Pin | TimerCamera |
| -------------------- | ---------- | ----------- |
| SCCB Clock           | SIOC       | G23         |
| SCCB Data            | SIOD       | G25         |
| System Clock         | XCLK       | G27         |
| Vertical Sync        | VSYNC      | G22         |
| Horizontal Reference | HREF       | G26         |
| Pixel Clock          | PCLK       | G21         |
| Pixel Data Bit 0     | D0         | G32         |
| Pixel Data Bit 1     | D1         | G35         |
| Pixel Data Bit 2     | D2         | G34         |
| Pixel Data Bit 3     | D3         | G5          |
| Pixel Data Bit 4     | D4         | G39         |
| Pixel Data Bit 5     | D5         | G18         |
| Pixel Data Bit 6     | D6         | G36         |
| Pixel Data Bit 7     | D7         | G19         |
| Camera Reset         | RESET      | G15         |
| Camera Power Down    | PWDN       | -1          |
| Power Supply 3.3V    | 3V3        | 3V3         |
| Ground               | GND        | GND         |

### HY2.0-4P

| HY2.0-4P | TimerCamera |
| -------- | ----------- |
| SCL      | G13         |
| SDA      | G4          |
| 5V       | 5V          |
| GND      | GND         |

### LED

| LED     | TimerCamera |
| ------- | ----------- |
| LED_Pin | G2          |

### BM8563

| BM8563 | TimerCamera |
| ------ | ----------- |
| SCL    | G14         |
| SDA    | G12         |

### BAT

| BAT          | TimerCamera |
| ------------ | ----------- |
| BAT_ADC_Pin  | G38         |
| BAT_HOLD_Pin | G33         |

## 数据手册

- [ESP32-D0WDQ6-V3](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/644/esp32_datasheet_cn.pdf)
- [OV3660](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1060/OV3660_datasheet.pdf)

## 软件开发

### 快速上手

- [Camera-Tool Guide](/zh_CN/guide/wifi_camera/timer_cam/cameratool)
- [UiFlow-Media Trans](/zh_CN/guide/wifi_camera/timer_cam/media_trans)
- [UiFlow-UART/TIMER](/zh_CN/guide/wifi_camera/timer_cam/uiflow)
- [Arduino Quick Start](/zh_CN/arduino/arduino_ide)
- [Timer Folder Pusher](/zh_CN/guide/wifi_camera/timer_cam/smb)
- [Timer Amazon S3 Folder Pusher](/zh_CN/guide/wifi_camera/timer_cam/amazon_s3)

### Arduino

- [TimerCamera-Arduino](https://github.com/m5stack/TimerCam-arduino)

### ESP-IDF

- [FactoryTest](https://github.com/m5stack/TimerCam-idf)
- [AWS-S3-PUT](https://github.com/m5stack/M5_Camera_Examples/tree/main/idf/AWS-S3-PUT)
- [Ali-OSS-PUT](https://github.com/m5stack/M5_Camera_Examples/tree/main/idf/Ali-OSS)
- [SMB-OSS-PUT](https://github.com/m5stack/M5_Camera_Examples/tree/main/idf/SMB-PUT)
- [Timer Wakeup](https://github.com/m5stack/M5_Camera_Examples/tree/main/idf/Wake-up)
- [HTTP Stream](https://github.com/m5stack/M5_Camera_Examples/tree/main/idf/http-stream)
- [Wireless-send](https://github.com/m5stack/M5_Camera_Examples/tree/main/idf/wireless-send)

### Home Assistant

- [TimerCamera 系列 Home Assistant 集成](/zh_CN/homeassistant/camera/timercamera)

### 欠压 / 掉电保护

\#> 设备欠压时，摄像头可能触发欠压保护导致复位。

#### ESP-IDF

ESP-IDF 可以在编译工程时在 menuconfig 中进行配置，将其禁用。

```cpp
idf.py menuconfig
```

**Component config**->**ESP32-specific**->**Hardware brownout detect & reset** (disable)

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/timercam/timercam_brownout_config_01.webp" width="40%">

#### Arduino

Arduino 平台可在初始化时通过以下示例代码进行禁用。

```cpp
#include "soc/soc.h"
#include "soc/rtc_cntl_reg.h"

void setup() {
  WRITE_PERI_REG(RTC_CNTL_BROWN_OUT_REG，0); //disable   detector
}
```

### USB 驱动

> TimerCAM 在部分系统中，可能无法免驱工作，用户可以通过手动安装 FTDI VCP 驱动修复该问题。以 win10 环境为例，下载匹配操作系统的驱动文件，并解压，通过设备管理器进行安装。(注：某些系统环境下，需要安装两次，驱动才会生效，未识别的设备名通常为**M5Stack**或**USB Serial**，Windows 推荐使用驱动文件在设备管理器直接进行安装 (自定义更新)，可执行文件安装方式可能无法正常工作)。

[FTDI VCP 驱动下载页面：](https://ftdichip.com/drivers/vcp-drivers/)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1040/U082-X-USB-note-02.png" width="100%">

**安装方法：**

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1040/U082-X-USB-note-01.png" width="100%">

### EasyLoader

| Easyloader                      | 下载链接                                                                                                          | 备注 |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ---- |
| TimerCamera Firmware Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/TIMECAM/EasyLoader_TimerCamera_AP.exe) | /    |

## 相关视频

- 连接 Unt TimerCAM 热点，密码 12345678，在浏览器中打开 192.168.4.1 即可查看图像，如需使用定时拍照功能，请参考快速上手指南

<video id="example_video" controls height="400px"><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Unit/timer_cameraX.mp4" type="video/mp4"> </video>

<video class="video-container" controls height="400px"><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Unit/TimerCAM.mp4" type="video/mp4"> </video>

- 焦距调节

<video controls height="400px"><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Unit/timercam_lens_adj.mp4" type="video/mp4"> </video>

## 产品对比

如需对比 TimerCamera 系列产品信息，可访问[产品选型表](/zh_CN/products_selector/timer_cam_compare?select=U082)，勾选目标产品即可获取对比结果。选型表涵盖核心参数、功能特性等关键信息，支持多产品同步比对。
