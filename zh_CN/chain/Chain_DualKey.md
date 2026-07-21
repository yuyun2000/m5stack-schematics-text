# Chain DualKey

<span class="product-sku">SKU:C147</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/C147_chain-dualkey-mainpicture_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/C147_chain-dualkey-mainpicture_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/C147_chain-dualkey-mainpicture_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/C147_chain-dualkey-mainpicture_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/C147_chain-dualkey-mainpicture_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/C147_chain-dualkey-mainpicture_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/C147_chain-dualkey-mainpicture_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/C147_chain-dualkey-mainpicture_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/C147_chain-dualkey-mainpicture_09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/C147_chain-dualkey-mainpicture_10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/C147_chain-dualkey-mainpicture_11.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/C147-weight.jpg">
</PictureViewer>

## 描述

**Chain DualKey** 是一款可编程双按键输入开发板，搭载 ESP32-S3FN8 主控芯片。正面集成 2 个支持热插拔的青轴机械键盘按键及 2 个可编程 RGB LED，交互反馈清晰；内置 350mAh 锂电池，结合低功耗设计，续航表现良好。出厂预置 Chain 宏键盘固件，支持 USB / BLE 连接，模拟 HID 输入设备。设备启动后，可连接设备 AP 热点，通过内置的 Web 页面，配置本机或拓展节点的 HID 功能映射，实现各种控制需求。
该开发板采用 M5Stack Chain 系列可拓展设计，配备两个 HY2.0-4P 拓展接口，支持横向拓展及连接其他传感器设备。基于 ESP32-S3 内置的 USB-OTG 功能，适用于智能家居、键盘外设、宏键盘等场景。

## 教程 & 快速上手

learn>| ![UiFlow2](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/uiflow2.0_banner_01.png) | [UiFlow2](/zh_CN/uiflow2/chain_dualKey/program) | 本教程将向你介绍，如何通过 UiFlow2 图形化编程平台控制 Chain DualKey 设备。 |

learn>| ![Arduino IDE](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/arduino_banner_01.png) | [Arduino IDE](/zh_CN/arduino/chain_dualkey/program) | 本教程介绍如何通过 Arduino IDE 编程控制 Chain DualKey。|

learn>| ![出厂固件使用教程](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/firmware.png) | [出厂固件使用教程](/zh_CN/guide/input_device/chain_dualkey) | 本教程将介绍 Chain DualKey 的出厂固件使用教程，包含按键功能设置、LED 灯色彩设置、电池状态、Chain Bus 设备的操作方法。|

## 产品特性

- ESP32-S3FN8 主控芯片
- 内置 350mAh 锂电池
- 2 个可编程 RGB LED
- 2 个支持热插拔的青轴按键
- M5Stack Chain 系列可拓展设计
- 背部 LEGO 兼容孔设计
- 挂绳设计

## 包装内容

- 1 x Chain DualKey
- 1 x 键帽贴纸

## 应用场景

- 智能家居控制
- 宏键盘
- 键盘外设

## 规格参数

| 规格     | 参数                                                                                                                |
| -------- | ------------------------------------------------------------------------------------------------------------------- |
| SoC      | ESP32-S3FN8 @双核 Xtensa LX7 处理器，主频高达 240MHz                                                                |
| Flash    | 8MB                                                                                                                 |
| Wi-Fi    | 2.4 GHz Wi-Fi                                                                                                       |
| 输入电源 | USB：DC 5V                                                                                                          |
| 电池     | 350mAh 锂电池                                                                                                       |
| RGB LED  | 2x WS2812B                                                                                                          |
| 工作温度 | 0 ~ 40°C                                                                                                            |
| 待机电流 | 关机模式（VBAT）：DC 4.2V@8.97uA<br>深度睡眠模式（VBAT）：DC 4.2V@107.64uA<br>USB 5V 供电（不带电池）：DC 5V@41.7mA |
| 产品尺寸 | 47.9 x 34.3 x 23.9mm                                                                                                |
| 产品重量 | 23.7g                                                                                                               |
| 包装尺寸 | 63.0 x 72.0 x 28.0mm                                                                                                |
| 毛重     | 39.3g                                                                                                               |

## 操作说明

### 充电

只要连接外部电源，无论开关拨到什么位置，都会给电池充电。

### 重启

Chain DualKey 没有 reset 按键。将开关拨至中间位置，断开 USB-C 数据线并重新连接（请勿按住 Key1），设备重启。

### 进入下载模式

将设备的开关拨到中间位置，按住 Key1（远离挂绳的按键）通过 USB-C 数据线连接至电脑，然后松开 Key1，设备进入下载模式。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/Download_mode.gif" width="50%">

### 连接说明

用 Chain Bridge 连接器连接主控 Chain DualKey 和各个 Chain 系列输入设备。连接时需要注意方向，三角箭头从主控 Chain DualKey 指向外侧，如图：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/Chain_connect.jpg" width="50%">

## 原理图

- [Chain DualKey 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/Chain_DualKey_SCH_V1.5_20250725_2025_07_25_16_06_51.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/Chain_DualKey_SCH_V1.5_20250725_2025_07_25_16_06_51_page_01.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/Chain_DualKey_SCH_V1.5_20250725_2025_07_25_16_06_51_page_02.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/Chain_DualKey_SCH_V1.5_20250725_2025_07_25_16_06_51_page_03.png">
</SchViewer>

## 管脚映射

### KEY

| Chain DualKey | G0    | G17   |
| ------------- | ----- | ----- |
| KEY_1         | INPUT |       |
| KEY_2         |       | INPUT |

### RGB LED

| Chain DualKey | G21   | G40    |
| ------------- | ----- | ------ |
| WS2812        | INPUT |        |
| WS2812_PWR    |       | PWR_EN |

### ADC

| Chain DualKey | G8    | G7    | G10     | G2       | G9         |
| ------------- | ----- | ----- | ------- | -------- | ---------- |
| SWITCH_1      | INPUT |       |         |          |            |
| SWITCH_2      |       | INPUT |         |          |            |
| ADC_BAT       |       |       | ADC_BAT |          |            |
| ADC_VBUS      |       |       |         | ADC_VBUS |            |
| ADC_CHARGE    |       |       |         |          | ADC_CHARGE |

?> 注意事项 | 使用时请勿配置 SWITCH_1，SWITCH_2 为高电平输出，否则将导致设备无法正常关断电源。

### USB

| Chain DualKey | G19    | G20    |
| ------------- | ------ | ------ |
| USB           | USB_DN | USB_DP |

### HY2.0-4P

| Chain DualKey | GND | VOUT | G48      | G47      |
| ------------- | --- | ---- | -------- | -------- |
| HY2.0-4P_1    | GND | 5V   | UART1_RX | UART1_TX |

| Chain DualKey | GND | VOUT | G5       | G6       |
| ------------- | --- | ---- | -------- | -------- |
| HY2.0-4P_2    | GND | 5V   | UART2_RX | UART2_TX |

## 尺寸图

- [Chain DualKey 模型尺寸 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/C147-chain-dualkey-model-size.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/C147-chain-dualkey-model-size_page_01.png" width="100%">

## 数据手册

- [ESP32-S3](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/472/esp32-s3_datasheet_cn.pdf) <!--注意，这个的中英文链接不一样的-->

## 软件开发

### 快速上手

- [Chain DualKey 出厂固件使用教程](/zh_CN/guide/input_device/chain_dualkey)

### Arduino

- [Chain DualKey Arduino 快速上手](/zh_CN/arduino/chain_dualkey/program)
- [Chain 系列产品 驱动库](https://github.com/m5stack/M5Chain)

### UiFlow2

- [Chain DualKey UiFlow2 快速上手](/zh_CN/uiflow2/chain_dualKey/program)

### Home Assistant

- [Home Assistant 集成](/zh_CN/homeassistant/input_device/chain_dualkey)

### ESP-IDF

- [Chain DualKey 出厂固件源码](https://github.com/m5stack/M5DualKey-UserDemo)

## 相关视频

- Chain DualKey 产品介绍以及功能展示

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/C147-Chain-Dualkey-video-CN.mp4" type="video/mp4"></video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=115570087298583&bvid=BV1ZSyGBkEAp&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
      <iframe width="560" height="315" src="https://www.youtube.com/embed/1sK4M91pU8E?si=t4T9GL6QtwBscn7v" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
