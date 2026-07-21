# AtomS3-Lite

<span class="product-sku">SKU:C124</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/AtomS3 Lite/img-dc6432b6-fd9b-4066-9a4d-49786503d1a3.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/AtomS3 Lite/img-3db34239-aaae-4acf-ad5f-a8a00adec82b.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/471/C124_01.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/AtomS3 Lite/img-ceb227fb-89b5-4f0b-a53f-66ca2eb467e3.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/AtomS3 Lite/img-2ebc2ad4-4ba3-4352-8c55-d4bcacba092d.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/AtomS3 Lite/img-31be1561-8bc3-4396-b82c-62d6fc500d78.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/AtomS3 Lite/img-81e96bb1-716a-498d-aa6d-c1a2d959fe0d.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/AtomS3 Lite/img-e1ca2ebd-1ec1-4fec-b3cc-0f83e49b9cae.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/AtomS3 Lite/img-65ad4dde-eada-4edc-a442-8d31c61b1ccf.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/471/C124-weight.jpg">
</PictureViewer>

## 描述

**AtomS3-Lite** 是 M5Stack 开发套件系列中一款采用 **ESP32-S3** 作为主控的 **Atom 系列可编程控制器**，其大小只有 24.0 x 24.0 x 9.5mm 。主控采用 **ESP32-S3FN8** 方案，拥有 **8 MB** 的 SPI 闪存，集成 **Wi-Fi** 功能，内置 **3D 天线**、**5V 转 3.3V** 电源电路，提供 **红外发射灯**、**RGB 状态指示灯**、**按键** 以及**HY2.0 - 4P** 接口。产品底部设有电源以及 6 个 GPIO 排母引出，方便作扩展应用。板载 **USB Type-C** 接口可实现程序下载以及串口通信功能，背面提供一个 **M2 螺丝孔** 用于固定。适用于各种嵌入式的智能设备应用。

## 教程 & 快速上手

learn>| ![Arduino IDE](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/arduino_banner_01.png) | [Arduino IDE](/zh_CN/arduino/m5atoms3/program) | 本教程将向你介绍，如何通过 Arduino IDE 编程控制 AtomS3-Lite 设备。 |

learn>| ![UiFlow2](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/uiflow2.0_banner_01.png) | [UiFlow2](/zh_CN/uiflow2/atoms3lite/program) | 本教程将向你介绍，如何通过 UiFlow2 图形化编程平台控制 AtomS3-Lite 设备。 |

## 产品特性

- 基于 ESP32-S3FN8 开发
- 自带 USB 下载功能
- 可编程按键
- 红外发射功能
- 可扩展的引脚与接口
- 开发平台
  - UiFlow2
  - Arduino IDE
  - ESP-IDF
  - PlatformIO

## 包装内容

- 1 x AtomS3-Lite

## 应用场景

- 物联网节点
- 微型控制器

## 规格参数

| 规格       | 参数                 |
| ---------- | -------------------- |
| SoC        | ESP32-S3FN8          |
| Flash      | 8MB                  |
| RGB        | WS2812C-2020         |
| DC-DC      | SY8089               |
| 工作温度   | 0 ~ 40°C             |
| 供电电压   | 5V                   |
| 供电方式   | Type-C               |
| 输出电压   | 3.3V                 |
| IO 接口 ×6 | G5/G6/G7/G8/G38/G39  |
| 产品尺寸   | 24.0 x 24.0 x 9.5mm  |
| 产品重量   | 5.3g                 |
| 包装尺寸   | 85.0 x 65.0 x 12.2mm |
| 毛重       | 11.0g                |

## 操作说明

### 进入下载模式

如需烧录固件，请长按复位按键（大约 2 秒）直到内部绿色 LED 灯亮起，便可松开，此时设备已进入下载模式，等待烧录。

<img alt="schematics" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3%20Lite/download%20mode.gif" width="30%" />

## 原理图

- [AtomS3-Lite 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/471/Sch_M5_AtomS3_v1.0.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/471/Sch_M5_AtomS3_v1.0_sch_01.png">
</SchViewer>

## 管脚映射

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/471/C124_PinMap_01.jpg" width="100%">

### HY2.0-4P

::grove-table
| HY2.0-4P    | Black | Red | Yellow | White |
| ----------- | ----- | --- | ------ | ----- |
| PORT.CUSTOM | GND   | 5V  | G2     | G1    |
::

## 尺寸图

<img alt="module size" src="https://static-cdn.m5stack.com/resource/docs/products/core/AtomS3 Lite/img-1ff0758c-2ca5-4cb8-adb8-b52d55af34a8.png" width="100%" />

## 结构文件

- [AtomS3-Lite 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/C124_AtomS3-Lite/Structures)

## 数据手册

- [ESP32-S3](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/472/esp32-s3_datasheet_cn.pdf)
- [SY8089](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/atombase/ATOMS3/sy8089.pdf)

## 软件开发

### Arduino

- [AtomS3-Lite Arduino 快速上手](/zh_CN/arduino/m5atoms3/program)
- [AtomS3-Lite Arduino 驱动库](https://github.com/m5stack/M5AtomS3)

### UiFlow2

- [AtomS3-Lite UiFlow2 快速上手](/zh_CN/uiflow2/atoms3lite/program)

### PlatformIO

```bash
[env:m5stack-atoms3]
platform = espressif32
board = esp32-s3-devkitc-1
framework = arduino
upload_speed = 1500000
monitor_speed = 115200
build_flags =
    -DESP32S3
    -DCORE_DEBUG_LEVEL=5
    -DARDUINO_USB_CDC_ON_BOOT=1
	-DARDUINO_USB_MODE=1
lib_deps =
    M5Unified=https://github.com/m5stack/M5Unified
```

### Easyloader

| Easyloader                      | 下载链接                                                                                          | 备注 |
| ------------------------------- | ------------------------------------------------------------------------------------------------- | ---- |
| AtomS3-Lite 出厂固件 Easyloader | [download](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/471/AtomS3-Lite-Factory-Firmware.exe) | /    |

## 相关视频

AtomS3-Lite + Bluetooth LE PWM 控制 RGB 灯 (UiFlow)

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3/M5Stack%20AtomS3's%20%2B%20Bluetooth%20LE.mp4" type="video/mp4"></video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113083737508456&bvid=BV16PpuerEVB&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/CI_OCxpAp44?si=bV_ZOjbGNUfeFWMa" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>

## 产品对比

如需对比 Atom 系列产品信息，可访问[产品选型表](/zh_CN/products_selector/m5atom_compare?select=C124)，勾选目标产品即可获取对比结果。选型表涵盖核心参数、功能特性等关键信息，支持多产品同步比对。
