# StickS3

<span class="product-sku">SKU:K150</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/K150-stickS3_main-products_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/K150-stickS3_main-products_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/K150-stickS3_main-products_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/K150-stickS3_main-products_13.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/K150-stickS3_main-products_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/K150-stickS3_main-products_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/K150-stickS3_main-products_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/K150-stickS3_main-products_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/K150-stickS3_main-products_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/K150-stickS3_main-products_09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/K150-stickS3_main-products_10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/K150-stickS3_main-products_11.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/K150-stickS3_main-products_12.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/K150-weight.jpg">
</PictureViewer>

## 描述

StickS3 是一款紧凑且高性能的可编程控制器，专为远程控制，物联网应用设计。核心搭载 ESP32-S3-PICO-1-N8R8 主控芯片，支持 2.4 GHz Wi-Fi 无线通信，内置 8MB Flash 与 8MB PSRAM，满足多样化应用开发需求，提供出色的性能与扩展性。人机交互方面配备 1.14" LCD 显示屏、 6 轴 IMU 传感器、可编程按钮。音频系统采用 ES8311 单声道编解码器，结合高灵敏 MEMS 麦克风 与 AW8737 功率放大器，实现清晰拾音与高保真音频输出，赋能语音识别与交互体验。同时集成 IR 发送和接收管，250mAh 锂电池，适合智能家居控制，AI 语音助手，IoT 项目开发等应用场景。

## 教程 & 快速上手

learn>| ![Arduino IDE](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/arduino_banner_01.png) | [Arduino IDE](/zh_CN/arduino/m5sticks3/program) | 本教程将向你介绍，如何通过 Arduino IDE 编程控制 StickS3 设备。 |

learn>| ![UiFlow2](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/uiflow2.0_banner_01.png) | [UiFlow2](/zh_CN/uiflow2/sticks3/program) | 本教程将向你介绍，如何通过 UiFlow2 图形化编程平台控制 StickS3 设备。 |

learn>| ![StickS3 小智语音助手](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/sticks3_xiaozhi_cover.jpg) | [StickS3 小智语音助手](/zh_CN/guide/realtime/xiaozhi/sticks3) | 本教程将向你介绍使用 StickS3 设备，通过 M5Burner 烧录小智语音助手固件，构建个人语音助手应用。 |

learn>| ![StickS3 ESP-Claw 固件烧录](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/StickS3-ESP-Claw-cover.jpg) | [StickS3 ESP-Claw 固件烧录](/zh_CN/guide/agent/esp_claw/sticks3) | 本教程介绍如何在 StickS3 上烧录 ESP-Claw 固件，帮助用户快速将 StickS3 设备配置为支持 AI 交互、硬件编程与自动化控制的智能终端。 |

## 注意事项

!> EXT_5V_EN 输入供电注意 | 设备 5V 供电接口可配置为 DC 5V 输出 / 输入模式。接口默认为输入模式，此时可通过 Grove 接口，顶部 Hat2-Bus 的 EXT_5V， 5VIN 接口输入 DC 5V 供电。 当配置为输出模式时，仅允许通过 USB 或 顶部 Hat2-Bus 的 5VIN 进行输入，请勿从其他输出接口进行供电输入，否则设备存在短路损坏风险。

!> 红外接收注意事项 | 1. StickS3 红外接收解码**必须使用 ESP32 RMT 外设**，不支持通过 GPIO 方式进行接收解码。<br>2. 使用红外接收功能时，需要关闭扬声器功放，否则无法正常接收。操作方法可参考[教程](/zh_CN/arduino/m5sticks3/m5pm1?id=spk%20amp)。<br>3. 确保发射端与接收端尽量正对，且两者距离不小于 30cm；若距离过近，可能导致接收异常。

!> 扬声器音量注意 | 使用电池供电（未连接 USB）时，建议将扬声器音量保持在 75% 以下，以免因功率过大导致设备意外重启。

?> 设备异响 | 首发批次的 StickS3 启动后可能存在轻微异响，不影响功能使用。

?> 使用注意事项 | 请勿私自拆解产品外壳，拆解可能造成天线 PFC 电路损坏，影响设备正常工作。

## 产品特性

- 集成 ESP32-S3-PICO-1-N8R8 主控
- 8MB Flash 和 8MB PSRAM
- ES8311 单声道音频编解码芯片
- MEMS 麦克风 + 扬声器
- 集成红外发射管 + 红外接收管
- 背面磁吸设计
- 拓展接口:
  - 可扩展 Hat2 总线 (2.54-16P)
  - HY2.0-4P 接口
- 开发平台
  - Arduino
  - UiFlow2
  - ESP-IDF
  - PlatformIO

## 包装内容

- 1 x StickS3

## 应用场景

- 智能家居控制
- AI 语音助手
- IoT 项目开发

## 规格参数

| 规格               | 参数                                                                                                                           |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| SoC                | ESP32-S3-PICO-1-N8R8 @双核 Xtensa LX7 处理器，主频高达 240MHz                                                                  |
| Flash              | 8MB                                                                                                                            |
| PSRAM              | 8MB Octal                                                                                                                      |
| IMU                | BMI270                                                                                                                         |
| Wi-Fi              | 2.4 GHz Wi-Fi                                                                                                                  |
| 屏幕               | 型号：ST7789P3<br>分辨率：135x240                                                                                              |
| 输入电源           | USB Type-C DC 5V                                                                                                               |
| 音频编解码器       | ES8311：24 位分辨率，采用 I2S 协议                                                                                             |
| 麦克风             | MEMS 麦克风，信噪比 (SNR)：65 dB                                                                                               |
| 扬声器             | AW8737 功放芯片 + 8Ω@1W 2011 型腔体喇叭                                                                                        |
| 工作温度           | 0 ~ 40°C                                                                                                                       |
| 电池容量           | 250mAh                                                                                                                         |
| Grove 接口带载能力 | 空载：5V<br>最大：4.88V@0.38A                                                                                                  |
| 功耗               | 关机状态：4.2V@14.02uA<br>L1 状态：4.2V@52.47uA<br>L2 状态：4.2V@102.40uA<br>L3A 状态：4.2V@36.69mA<br>满载状态：4.2V@519.02mA |
| 产品尺寸           | 48.0 x 24.0 x 15.0mm                                                                                                           |
| 产品重量           | 20.0g                                                                                                                          |
| 包装尺寸           | 65.0 x 25.0 x 15.0mm                                                                                                           |
| 毛重               | 22.4g                                                                                                                          |

## 操作说明

### 兼容性说明

**StickS3**在结构上不兼容以下 Hat 系列产品：Hat Mini JoyC（SKU:U156）、Hat Mini EncoderC（SKU:U157）和 Hat 18650C（SKU:U080）。

### 进入下载模式

设备连接 USB 线，长按机身侧边复位按键。当设备内部绿色 LED 闪烁时，表示设备已成功进入下载模式。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/stickS3_operate_01.gif" width="50%">

### 按键操作说明

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/K150-stickS3_main-products_13.jpg" width="50%">

- 长按：进入下载模式
- 双击：关机
- 单击：开机 / 复位

### EXT_5V_EN

M5Unified 默认初始化中将关闭 EXT_5V_EN，此操作将关闭 Grove、Hat EXT_5V 接口和 IR TX/RX 的供电，切换为输入模式。此时需要外部 5V 输入供电， IR TX/RX 才能正常工作。无外接供电的使用场景，则可以通过以下 API 重新打开 EXT_5V 输出模式，恢复 IR TX/RX 供电。

```cpp
M5.Power.setExtOutput(true); // EXT_5V OUTPUT
// M5.Power.setExtOutput(false); // EXT_5V INPUT
```

### IMU 三轴方向示意图

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/IMU-StickS3.jpg" width="70%">

## 原理图

- [StickS3 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/K150_Stick_S3_PRJ_V0.6_20251111_2025_11_17_16_10_24.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/K150_Stick_S3_PRJ_V0.6_20251111_2025_11_17_16_10_24_page_02.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/K150_Stick_S3_PRJ_V0.6_20251111_2025_11_17_16_10_24_page_03.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/K150_Stick_S3_PRJ_V0.6_20251111_2025_11_17_16_10_24_page_04.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/K150_Stick_S3_PRJ_V0.6_20251111_2025_11_17_16_10_24_page_05.png">
</SchViewer>

## 管脚映射

### LCD

| ESP32‑S3 | G39  | G40 | G45 | G41 | G21 | G38 |
| -------- | ---- | --- | --- | --- | --- | --- |
| ST7789P3 | MOSI | SCK | RS  | CS  | RST | BL  |

### IMU & M5PM1

| ESP32‑S3      | G48 | G47 |
| ------------- | --- | --- |
| BMI270 (0x68) | SCL | SDA |
| M5PM1 (0x6e)  | SCL | SDA |

### M5PM1

| M5PM1          | G0            | G1       | G2          | G3             | G4           |
| -------------- | ------------- | -------- | ----------- | -------------- | ------------ |
| Battery Charge | PYG0_CHG_STAT |          |             |                |              |
| ESP32-S3       |               | PYG1_IRQ |             |                |              |
| L3B Power      |               |          | PYG2_L3B_EN |                |              |
| Speaker        |               |          |             | PYG3_SPK_Pulse |              |
| IMU INT        |               |          |             |                | PYG4_IMU_INT |

### Audio

| ESP32‑S3      | G18  | G14  | G17  | G15  | G16 | G48 | G47 |
| ------------- | ---- | ---- | ---- | ---- | --- | --- | --- |
| ES8311 (0x18) | MCLK | DOUT | BCLK | LRCK | DIN | SCL | SDA |

### Button

| ESP32‑S3 | G11   | G12   |
| -------- | ----- | ----- |
| KEY1     | Input |       |
| KEY2     |       | Input |

### IR

| ESP32‑S3 | G46   | G42   |
| -------- | ----- | ----- |
| IR       | IR_TX | IR_RX |

### HY2.0-4P

- PORT.A

::grove-table
| HY2.0-4P    | Black | Red | Yellow | White |
| ----------- | ----- | --- | ------ | ----- |
| PORT.CUSTOM | GND   | 5V  | G9     | G10   |
::

### Hat2-Bus

::m5-bus-table
| PIN    | LEFT | RIGHT | PIN |
| ------ | ---- | ----- | --- |
| GND    | 1    | 2     | G5  |
| EXT_5V | 3    | 4     | G4  |
| Boot   | 5    | 6     | G6  |
| G1     | 7    | 8     | G7  |
| G8     | 9    | 10    | G43 |
| BAT    | 11   | 12    | G44 |
| 3V3_L2 | 13   | 14    | G2  |
| 5V_IN  | 15   | 16    | G3  |
::

## 尺寸图

- [StickS3 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/K150-sticks3.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/K150-sticks3_page_01.png" width="100%">

## 结构文件

- [StickS3 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/K150_StickS3/Structures)

## 数据手册

- [ESP32S3](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/477/esp32-s3_technical_reference_manual_cn.pdf)
- [ES8311](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/Atomic%20Echo%20Base/ES8311.pdf)
- [BMI270](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/K128%20CoreS3/BMI270.PDF)

## 软件开发

### 快速上手

- [StickS3 ESP-Claw 固件烧录](/zh_CN/guide/agent/esp_claw/sticks3)

### Arduino

- [StickS3 Arduino 快速上手](/zh_CN/arduino/m5sticks3/program)
- [StickS3 M5PM1 电源管理](/zh_CN/arduino/m5sticks3/m5pm1)
- [M5PM1 Arduino Library](https://github.com/m5stack/M5PM1)
- [StickS3 Arduino M5Unified 驱动库](https://github.com/m5stack/M5Unified)
- [StickS3 Arduino M5GFX 驱动库](https://github.com/m5stack/M5GFX)

### UiFlow2

- [StickS3 UiFlow2 快速上手](/zh_CN/uiflow2/sticks3/program)

### 通信协议

- [M5PM1 电源管理芯片](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/M5PM1_Datasheet_CN.pdf)

### 其他

- [StickS3 小智语音助手](/zh_CN/guide/realtime/xiaozhi/sticks3)

### PlatformIO

```bash
[env:m5stack-sticks3]
platform = espressif32@6.12.0
board = esp32-s3-devkitc-1
framework = arduino
board_build.arduino.partitions = default_8MB.csv
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
    M5PM1=https://github.com/m5stack/M5PM1
```

## 相关视频

- StickS3 产品介绍以及功能展示

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/K150-StickS3-video-ZH.mp4" type="video/mp4"></video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=115949470486273&bvid=BV1G3zCBGEdh&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/bBwT7dZOZl8?si=JIrlXGf4ra1oGdmf" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=116815778876283&bvid=BV1vD756jETQ&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/OOgfKi4Al-Q?si=0q8Ao4FFXRXfChP9" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>


## 产品对比

如需对比 Stick 系列产品信息，可访问[产品选型表](/zh_CN/products_selector/m5stick_compare?select=K150)，勾选目标产品即可获取对比结果。选型表涵盖核心参数、功能特性等关键信息，支持多产品同步比对。
