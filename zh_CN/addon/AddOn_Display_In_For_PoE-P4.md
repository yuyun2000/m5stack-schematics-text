# AddOn Display In For PoE-P4

<span class="product-sku">SKU:U220</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1265/U220_AddOn_Display_In_For_PoE-P4_main_pictures_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1265/U220_AddOn_Display_In_For_PoE-P4_main_pictures_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1265/U220_AddOn_Display_In_For_PoE-P4_main_pictures_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1265/U220_AddOn_Display_In_For_PoE-P4_main_pictures_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1265/U220_AddOn_Display_In_For_PoE-P4_main_pictures_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1265/U220_AddOn_Display_In_For_PoE-P4_main_pictures_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1265/U220_AddOn_Display_In_For_PoE-P4_main_pictures_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1265/U220_AddOn_Display_In_For_PoE-P4_main_pictures_09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1265/U220_AddOn_Display_In_For_PoE-P4_main_pictures_10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1265/U220_AddOn_Display_In_For_PoE-P4_main_pictures_11.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1265/U220_AddOn_Display_In_For_PoE-P4_main_pictures_12.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1265/U220_AddOn_Display_In_For_PoE-P4_weight.png">
</PictureViewer>

## 描述

**AddOn Display In For PoE-P4** 是一款适配 [Unit PoE-P4](/zh_CN/unit/Unit_PoE-P4) 的 HDMI 视频输入扩展模组。模块基于 `LT6911D` 芯片，可将外部设备输入的 `HDMI` 视频信号转换为 `2-Lane MIPI CSI` 信号并传输至 Unit PoE-P4，便于主控对视频画面进行采集、处理与分析。

除视频输入外，模块还集成了外设连接与本地存储相关扩展能力。板载 microSD 插槽接入主控 `SDIO` 总线，可用于存储采集的视频、图像及相关数据；板载 `USB Type-A` 接口可用于连接鼠标、键盘等外设。视频、控制、存储与 USB 信号均通过 24P FPC 接口连接至 Unit PoE-P4，适用于 HDMI 视频采集、图像处理与分析、机器视觉、视频监控与嵌入式多媒体终端等应用场景。

## 产品特性

- 适配 Unit PoE-P4 的 HDMI 视频输入扩展模组
- 基于 `LT6911D` 实现 `HDMI` 转 `MIPI CSI` 视频输入
- 标准 `HDMI Type-A` 输入接口，便于快速接入外部 HDMI 视频源
- 板载 microSD 插槽接入主控 `SDIO` 总线，支持本地存储采集的视频、图像及相关数据
- 板载 `USB Type-A` 接口，支持鼠标、键盘等外设接入
- 支持构建视频采集、图像处理、外设连接与本地存储联动的一体化应用方案
- 支持 `1280 x 720 @ 60Hz` 和 `1920 x 1080 @ 30Hz`输入分辨率

## 包装内容

- 1 x AddOn Display In For PoE-P4
- 1 x 24P FPC 排线 (0.5mm 间距)

## 应用场景

- HDMI 视频采集
- 图像处理与分析
- 机器视觉
- 视频监控
- 嵌入式多媒体终端

## 规格参数

| 规格          | 参数                                                  |
| ------------- | ----------------------------------------------------- |
| 转换芯片      | LT6911D                                               |
| I2C 地址      | 0x56                                                  |
| 主连接接口    | 24P FPC (0.5mm 间距)                                  |
| 输出信号      | 2-Lane MIPI CSI / INTIO                               |
| 输入信号      | SYS_SDA / SYS_SCL / USB1_DP / USB1_DN / SDIO / TF_DET |
| HDMI 输入接口 | 1 x HDMI Type-A                                       |
| USB 扩展接口  | 1 x USB Type-A                                        |
| USB 带载能力  | 5V@0.5A                                               |
| 存储扩展      | 1 x microSD 插槽                                      |
| 电源输入      | DC 5V (由 Unit PoE-P4 扩展接口供电)                   |
| HDMI 输入时序 | 1280 x 720 @ 60Hz / 1920 x 1080 @ 30Hz                |
| 待机功耗      | DC 5V@30.75mA （整机，不包括 DSI 接口屏幕）           |
| 工作功耗      | DC 5V@388.13mA （整机，包括 DSI 接口屏幕）            |
| 产品尺寸      | 63.1 x 20.3 x 15.5mm                                  |
| 产品重量      | 7.9g                                                  |
| 包装尺寸      | 138.0 x 93.0 x 16.5mm                                 |
| 毛重          | 11.0g                                                 |

## 操作说明

?> 注意事项 | 由于 Windows 与 macOS 默认启用了 GPU 缩放功能，`实际输出分辨率信号可能与系统中设置的分辨率不一致`，从而导致程序无法正常工作：<br>- Windows：需在显卡驱动中设置，才能正常输出目标分辨率信号显示。<br>- macOS：需借助第三方工具强制输出对应分辨率后，才能正常显示。

## 原理图

- [AddOn Display In For PoE-P4 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1265/SCH_UnitPoEP4_display_in_V0.3_SCH_PDF_20260326_2026_03_26_16_04_18.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1265/SCH_UnitPoEP4_display_in_V0.3_SCH_PDF_20260326_2026_03_26_16_04_18_page_01.png">
</SchViewer>

## 管脚映射

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1265/U220_AddOn_Display_In_For_PoE-P4_pinmap.jpg">

### 24P FPC CSI 接口

| 信号组      | 对应信号                                        |
| ----------- | ----------------------------------------------- |
| I2C         | SYS_SCL、SYS_SDA                                |
| MIPI CSI    | MIPI1_CLK_P/N、MIPI1_lane0_P/N、MIPI1_lane1_P/N |
| 控制 / 电源 | RST_1V8、1V8、GND                               |

### SDIO & USB & POWER

::m5-bus-table
| PIN      | LEFT | RIGHT | PIN    |
| -------- | ---- | ----- | ------ |
| SDIO_CMD | 1    | 1     | GND    |
| SDIO_CK  | 2    | 2     |        |
| SDIO_D3  | 3    | 3     |        |
| SDIO_D2  | 4    | 4     | INTIO  |
| SDIO_D1  | 5    | 5     | TF_DET |
| SDIO_D0  | 6    | 6     | 3V3    |
| USB1_DP  | 7    |       |        |
| USB1_DN  | 8    |       |        |
| 5V       | 9    |       |        |
::

## 尺寸图

- [AddOn Display In For PoE-P4 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1265/U220-AddOn_Display_In_For_PoE-P4_model_size.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1265/U220-AddOn_Display_In_For_PoE-P4_model_size_page_01.png" width="100%">

## 软件开发

### UiFlow2

- [AddOn Display In For PoE-P4 UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/addon/display_in.html)  <!--英文链接：https://uiflow-micropython.readthedocs.io/en/latest/addon/display_in.html> -->

### ESP-IDF

- [AddOn Display In For PoE-P4 ESP-IDF 示例程序使用教程](/zh_CN/esp_idf/unit_poe_p4/addon_display_in_for_poe-p4)

## 相关视频

<VideoGallery>
  <VideoItem title="AddOn Display In For PoE-P4 产品介绍以及功能展示" url="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1265/U220_AddOn_Display_In_For_PoE-P4_video_CN.mp4" />
</VideoGallery>
