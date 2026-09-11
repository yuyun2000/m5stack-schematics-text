# PaperMono-Lite

<span class="product-sku">SKU:C153-Lite</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1268/C153-Lite_PaperMono-Lite_main_pictures_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1268/C153-Lite_PaperMono-Lite_main_pictures_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1268/C153-Lite_PaperMono-Lite_main_pictures_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1268/C153-Lite_PaperMono-Lite_main_pictures_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1268/C153-Lite_PaperMono-Lite_main_pictures_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1268/C153-Lite_PaperMono-Lite_main_pictures_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1268/C153-Lite_PaperMono-Lite_main_pictures_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1268/C153-Lite_PaperMono-Lite_main_pictures_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1268/C153-Lite_PaperMono-Lite_main_pictures_09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1268/C153-Lite_PaperMono-Lite_main_pictures_10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1268/C153-Lite_PaperMono-Lite_main_pictures_11.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1268/C153-Lite_PaperMono-Lite_main_pictures_12.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1268/C153-Lite-weight.jpg">
</PictureViewer>

## 描述

**PaperMono-Lite** 是 PaperMono 的精简版本，面向低功耗显示与便携交互应用，配备支持触控的 3.97 英寸 4 阶灰度黑白墨水屏，基于 SSD1677 驱动，分辨率为 480x800，并集成 FT6336G 触控芯片与前光照明系统，可在弱光环境下提供清晰稳定的阅读与交互体验。核心采用 ESP32-S3R8，搭配 16MB Flash、8MB PSRAM 与 2.4 GHz Wi-Fi，同时板载蜂鸣器、PDM 麦克风 (LMD4737T261-AC02)、RGB LED、BMI270 六轴 IMU、M5IOE1 IO 扩展、microSD 卡槽和 RX8130CE 实时时钟。相比 PaperMono，Lite 版本不搭载 NFC 与 LoRa 模块，保留电子纸交互与基础无线连接能力；配合 M5PM1 多级电源管理系统与 1150mAh 电池，适用于电子阅读器、电子标牌、信息显示终端和低功耗嵌入式应用。

## 教程 & 快速上手

learn>| ![UiFlow2](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/uiflow2.0_banner_01.png) | [UiFlow2](/zh_CN/uiflow2/papermono/program) | 本教程将向你介绍，如何通过 UiFlow2 图形化编程平台控制 PaperMono-Lite 设备。 |

learn>| ![Arduino IDE](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/arduino_banner_01.png) | [Arduino IDE](/zh_CN/arduino/papermono/program) | 本教程将向你介绍，如何通过 Arduino IDE 编程控制 PaperMono-Lite 设备。 |

learn>| ![CrossPoint E‑Reader](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1267/C153_PaperMono_e-reader-fw-cover.png) | [CrossPoint E‑Reader](https://burner.m5stack.com/firmware/2091144466157694978/) | 点击此处下载 PaperMono-Lite 的 CrossPoint E‑Reader 固件。 |

## 注意事项

### 墨水屏使用注意事项

1. 使用时尽量避免阳光直射/暴晒，高温或强 UV 会损伤面板。
2. 软件上使用 10 次左右局部快速刷新之后建议使用一次全屏刷新清屏，避免产生累积的严重残影。
3. 屏幕有内置 OTP 波形可以直接调用，使用自制的外部波形时候需要注意直流平衡，否则可能对面板造成不可逆的损伤。
4. 需要避免不间断的连续局部快速刷新，避免长时间直流不平衡对面板造成不可逆的损伤。

### 触摸有效区域

#> PaperMono-Lite 触摸有效区域 | 触摸 IC 固件层面对触摸边界进行内缩处理，返回的有效触控坐标范围限定为： **X 轴：5 ~ 475**（总宽 480px），**Y 轴：5 ~ 795**（总高 800px）。

## 产品特点

- ESP32-S3R8 核心主控
  - 16MB Flash
  - 8MB PSRAM
  - 2.4 GHz Wi-Fi
- 3.97 英寸 4 阶灰度黑白墨水屏，支持触控
  - SSD1677
  - 480x800 分辨率
  - 4 阶灰度显示
  - FT6336G 触控
- 集成前光照明系统
- 音频交互
  - PDM 麦克风 (LMD4737T261-AC02)
  - 内置蜂鸣器
- 板载外设
  - BMI270 六轴 IMU
  - M5IOE1 IO 扩展
  - microSD 卡槽
  - RX8130CE RTC
  - RGB LED
- M5PM1 多级电源管理
- 相比 PaperMono，不搭载 NFC 与 LoRa 模块
- 内置 1150mAh 电池

## 包装内容

- 1 x PaperMono-Lite

## 应用场景

- 电子阅读器
- 电子标牌
- 信息显示终端
- 便携控制面板
- 低功耗 IoT 节点

## 规格参数

| 规格     | 参数                                                   |
| -------- | ------------------------------------------------------ |
| SoC      | ESP32-S3R8 @ Xtensa® 32 位 LX7 双核处理器，主频 240MHz |
| Flash    | 16MB                                                   |
| PSRAM    | 8MB Octal                                              |
| Wi-Fi    | 2.4 GHz Wi-Fi                                          |
| 屏幕     | 3.97" E-Paper (Mono) SSD1677 @ 480x800，触控 FT6336G   |
| 屏幕灰度 | 4 阶灰度显示                                           |
| 前光     | 集成墨水屏前光照明                                     |
| 输入电源 | USB Type-C DC 5V                                       |
| 电池容量 | 1150mAh                                                |
| 麦克风   | PDM 麦克风 LMD4737T261-AC02                            |
| 蜂鸣器   | 内置蜂鸣器                                             |
| IMU      | BMI270                                                 |
| 电源管理 | M5PM1                                                  |
| IO 扩展  | M5IOE1                                                 |
| 扩展存储 | microSD                                                |
| RTC      | RX8130CE                                               |
| RGB LED  | 内置 RGB LED                                           |
| 用户按键 | 2x 用户按键 + 1x 电源按键 (ON / OFF / RESET / BOOT)    |
| 产品尺寸 | 62.0 x 101.0 x 8.0mm                                   |
| 产品重量 | 72.4g                                                  |
| 包装尺寸 | 113.2 x 69.6 x21.0mm                                   |
| 毛重     | 88.9g                                                  |

## 操作说明

### 开关机

- 开机 / 复位：短按一次电源按钮
- 关机：连续按两次电源按钮

<video style="width:50%;" muted playsinline preload="auto" controls>
    <source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1268/C153-Lite_PaperMono-Lite_poweron_CN.mp4" type="video/mp4">
</video>

<!--英文视频为：https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1268/C153-Lite_PaperMono-Lite_poweron_EN.mp4-->

### 下载模式

长按电源按键（大约 2 秒）直到红色 LED 灯闪烁，此时松开手，设备即进入下载模式，等待烧录。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1268/C153-Lite_PaperMono-Lite_download.gif" width="50%">

### M5GFX LUT 刷新速度

以下数据为 PaperMono 在 M5GFX 不同刷新模式下的实验室测试结果。实际刷新耗时可能因显示内容和运行环境而异，仅供参考。

| 刷新模式      | 单次刷新耗时 |
| ------------- | ------------ |
| `epd_quality` | 4.71 s       |
| `epd_text`    | 0.45 s       |
| `epd_fast`    | 0.34 s       |
| `epd_fastest` | 0.07 s       |

**刷新模式演示：**

<video style="width:100%;" muted playsinline preload="auto" controls>
    <source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1267/C153_C153-Lite_reflash_mode_demo.mp4" type="video/mp4">
</video>

## 原理图

- [PaperMono-Lite 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1268/PaperMono-Lite_PRJ_V0.6.2_20260522.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1268/PaperMono-Lite_PRJ_V0.6.2_20260522_page_02.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1268/PaperMono-Lite_PRJ_V0.6.2_20260522_page_03.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1268/PaperMono-Lite_PRJ_V0.6.2_20260522_page_04.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1268/PaperMono-Lite_PRJ_V0.6.2_20260522_page_05.png">
</SchViewer>

## 管脚映射

### E-Paper

| ESP32-S3R8 | G14_SPI2_MOSI | G15_SPI2_CLK | G16_EINK_CS | G17_EINK_DC | G18_EINK_BUSY |
| ---------- | ------------- | ------------ | ----------- | ----------- | ------------- |
| SSD1677    | MOSI          | SCLK         | CS          | DC          | BUSY          |

| M5IOE1  | PYG5_ADC3 | PYG3       |
| ------- | --------- | ---------- |
| SSD1677 | RST       | EPD_3V3_EN |

| M5PM1      | G3_WAKEin / IRQout / PWM |
| ---------- | ------------------------ |
| Frontlight | BL_FB                    |

通过 `M5IOE1` 的 `PYG5_ADC3` 控制电子纸复位，`PYG3` 控制电子纸 3.3V 供电；通过 `M5PM1` 的 `G3_WAKEin` 控制前光亮度。

### Touch

| ESP32-S3R8    | G47_SYS_SDA | G48_SYS_SCL | G4_TP_INT |
| ------------- | ----------- | ----------- | --------- |
| FT6336G(0x38) | SDA         | SCL         | INT       |

| M5IOE1  | PYG6   | PYG13     |
| ------- | ------ | --------- |
| FT6336G | TP_RST | TP_VDD_EN |

### microSD

| ESP32-S3R8 | G12 | G13 | G11  | G10  | G9   | G8   |
| ---------- | --- | --- | ---- | ---- | ---- | ---- |
| microSD    | CMD | CLK | DAT0 | DAT1 | DAT2 | DAT3 |

| M5IOE1  | PYG14 | PYG1 |
| ------- | ----- | ---- |
| microSD | EN    | DET  |

`DET` 由 microSD 供电域上拉，卡槽开关闭合时检测脚被拉低，用于识别 microSD 卡插入。

### HMI

| ESP32-S3R8           | G47_SYS_SDA | G48_SYS_SCL | G2_KEY1 | G3_KEY2 |
| -------------------- | ----------- | ----------- | ------- | ------- |
| RTC - RX8130CE(0x32) | SDA         | SCL         |         |         |
| IMU - BMI270(0x68)   | SDA         | SCL         |         |         |
| KEY                  |             |             | KEY1    | KEY2    |

| M5PM1 | G0_WAKEin | G4_WAKEin | LED_EN_PP |
| ----- | --------- | --------- | --------- |
| HMI   | RTC_INT   | IMU_INT   | LED_R     |

`PYG0_RTC_INT` 与 `PYG4_IMU_INT` 接入 `M5PM1`，可作为低功耗唤醒源。

| M5IOE1 | PYG8_PWM2 | PYG9_PWM1 |
| ------ | --------- | --------- |
| HMI    | LED_G     | LED_B     |

PaperMono 机身侧边的 RGB LED 指示灯，由三色灯珠组成，其中红灯连接至 M5PM1 的 `LED_EN_PP`，设备开启后将根据 M5PM1 的默认行为点亮。由于 `LED_EN_PP` 不支持配置 PWM 输出模式，因此该指示灯可调的颜色将受到限制。

### KEY

| ESP32-S3R8 | G2                   | G3                   |
| ---------- | -------------------- | -------------------- |
| KEY        | USER_KEY1 (Button A) | USER_KEY2 (Button B) |

### Audio

| ESP32-S3R8 | G46_PDM_DAT | G45_PDM_CLK | G42_BB_PWM |
| ---------- | ----------- | ----------- | ---------- |
| PDM MIC    | DAT         | CLK         |            |
| BUZZER     |             |             | BB_PWM     |

| M5IOE1 | PYG12      |
| ------ | ---------- |
| PDM    | PDM_VDD_EN |

### M5PM1

| ESP32-S3R8  | G47_SYS_SDA | G48_SYS_SCL | G1_PY_IRQ | G0_BOOT_OUT |
| ----------- | ----------- | ----------- | --------- | ----------- |
| M5PM1(0x6E) | SDA         | SCL         | IRQ       | BOOT_OUT    |

### M5IOE1

| ESP32-S3R8   | G47_SYS_SDA | G48_SYS_SCL | G7      |
| ------------ | ----------- | ----------- | ------- |
| M5IOE1(0x4F) | SDA         | SCL         | PYB_IRQ |

| M5IOE1                 | PYG11_PWM3  |
| ---------------------- | ----------- |
| Charger - IP2315(0x75) | PYB_CHG_IIC |

> 注意事项 | 充电芯片 `IP2315` 的 I2C 工作模式依赖 I2C 引脚上拉至 VBAT 电压。设备接入 USB 将触发模式检测，若 VBAT 电压偏低，IP2315 可能无法正常初始化至 I2C 模式，进而干扰同一条 I2C 总线上的其他器件。M5IOE1 通过 PYG11_PWM3 控制 IP2315 与系统 I2C 总线的连接：设备运行期间，禁止将 IP2315 长期挂载在 I2C 总线上，通信结束后需及时断开，避免降低总线通信稳定性。若发生 I2C 总线通信异常，可通过短按电源键复置设备，恢复总线正常工作。

## 尺寸图

- [PaperMono-Lite 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1268/C153-Lite_PaperMono-Lite_model_size.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1268/C153-Lite_PaperMono-Lite_model_size_page_01.png" width="100%">

## 数据手册

- [ESP32-S3](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/472/esp32-s3_datasheet_cn.pdf)
- [RX8130CE 寄存器手册](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/RX8130CE_cn-Register-Datasheet.pdf)
- [BMI270](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/app/Stamp%20Fly/BMI270.PDF)
- [SSD1677 屏幕驱动](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1267/SSD1677.pdf)
- [3.97 英寸触控屏](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1267/EPD_Module_User_Manual.pdf)

## 软件开发

?>墨水屏驱动说明|1. M5GFX 库针对 PaperMono 设备的电子纸驱动波形目前尚不稳定。推荐优先使用下方的电子纸原厂 OTP 示例程序完成刷新配置，可获得更优的面板使用寿命与刷新稳定性。<br>2. 软件使用建议：执行约 10 次局部快速刷新后，建议执行一次全屏刷新清屏，防止残影持续累积加重。<br>3. 长时间反复刷新后，面板可能出现黑色沉积像素，属于墨水颗粒物理特性导致；静置一段时间后，执行一次全屏刷新即可恢复。

### Arduino

- [PaperMono-Lite Arduino 快速上手](/zh_CN/arduino/papermono/program)
- [PaperMono-Lite M5PM1 & M5IOE1 电源管理](/zh_CN/arduino/papermono/m5pm1_m5ioe1)
- [M5PM1 Arduino Library](https://github.com/m5stack/M5PM1)
- [M5IOE1 Arduino Library](https://github.com/m5stack/M5IOE1)
- [M5Unified Arduino Library](https://github.com/m5stack/M5Unified)
- [M5GFX Arduino Library](https://github.com/m5stack/M5GFX)

### UiFlow2

- [PaperMono-Lite UiFlow2 快速上手](/zh_CN/uiflow2/papermono/program)

### 通信协议

- [M5PM1 电源管理芯片](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/M5PM1_Datasheet_CN.pdf)
- [M5IOE1 IO拓展管理芯片](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1210/IO_Expander_Datasheet_CN.pdf)

### ESP-IDF

- [PaperMono-Lite 出厂固件源码](https://github.com/m5stack/M5PaperMono-UserDemo)
- [PaperMono-Lite OTP 案例程序](https://github.com/m5stack/M5PaperMono-OTP-Demo)

### PlatformIO

```bash
[env:m5stack-papermono-lite]
platform = espressif32@6.12.0
board = esp32-s3-devkitm-1
framework = arduino
board_build.partitions = default_16MB.csv
board_upload.flash_size = 16MB
board_upload.maximum_size = 16777216
board_build.arduino.memory_type = qio_opi
build_flags =
    -DESP32S3
    -DBOARD_HAS_PSRAM
    -mfix-esp32-psram-cache-issue
    -DCORE_DEBUG_LEVEL=0
    -DARDUINO_USB_CDC_ON_BOOT=1
    -DARDUINO_USB_MODE=1
lib_deps =
    M5Unified = https://github.com/m5stack/M5Unified#develop
    M5PM1 = https://github.com/m5stack/M5PM1
    M5IOE1 = https://github.com/m5stack/M5IOE1
```

### Easyloader

| Easyloader               | 下载链接                                                                                           | 备注 |
| ------------------------ | -------------------------------------------------------------------------------------------------- | ---- |
| PaperMono-Lite User Demo | [download](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1267/C153-PaperMono-UserDemo_0x00.exe) | /    |

### 其他

- [PaperMono-Lite 恢复出厂固件](https://burner.m5stack.com/firmware/2089640807996628993/)
- [PaperMono-Lite CrossPoint E-Reader](https://burner.m5stack.com/firmware/2091144466157694978/)

## 相关视频

<VideoGallery>
  <VideoItem title="PaperMono / PaperMono-Lite 产品介绍以及功能展示" url="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1267/C153_and_C153-Lite_PaperMono_video_CN.mp4" />
</VideoGallery>

## 产品对比

::compare-table
| 产品对比项 | [PaperMono](/zh_CN/core/PaperMono) ![PaperMono](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1267/C153_PaperMono_main_pictures_02.webp) | [PaperMono-Lite](/zh_CN/core/PaperMono-Lite) ![PaperMono-Lite](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1268/C153-Lite_PaperMono-Lite_main_pictures_02.webp) |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 主控       | ESP32-S3R8                                                                                                                                  | ESP32-S3R8                                                                                                                                                           |
| 屏幕       | 3.97" 4 阶灰度黑白墨水屏，480x800                                                                                                           | 3.97" 4 阶灰度黑白墨水屏，480x800                                                                                                                                    |
| 触控       | FT6336G                                                                                                                                     | FT6336G                                                                                                                                                              |
| 前光       | 集成                                                                                                                                        | 集成                                                                                                                                                                 |
| Wi-Fi      | 2.4 GHz                                                                                                                                     | 2.4 GHz                                                                                                                                                              |
| NFC        | ST25R3916                                                                                                                                   | ❌                                                                                                                                                                    |
| LoRa       | Stamp LoRa-1262                                                                                                                             | ❌                                                                                                                                                                    |
| 扩展存储   | microSD                                                                                                                                     | microSD                                                                                                                                                              |
| IMU        | BMI270                                                                                                                                      | BMI270                                                                                                                                                               |
| RTC        | RX8130CE                                                                                                                                    | RX8130CE                                                                                                                                                             |
| 电池       | 1150mAh                                                                                                                                     | 1150mAh                                                                                                                                                              |
| 外壳颜色   | 灰色                                                                                                                                        | 白色                                                                                                                                                                 |
::
