# Air Quality

<span class="product-sku">SKU:K131</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/AirQ/4.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/AirQ/2.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/AirQ/6.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/AirQ/img-7286a3f4-b08e-4410-85e5-119b69532629.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/AirQ/img-b529336f-75dc-44a5-bf7a-55cbd37aa85d.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/AirQ/img-dbb19996-0e88-4c17-aeb6-bb05cfc68ff5.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/AirQ/img-d035f29f-b196-457c-b3a6-0a9670f5bc70.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/AirQ/img-050ef8e9-330b-4c9f-89c1-51ec2390c46b.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/AirQ/img-a1640cb6-2e5a-45c0-8943-e61c6fac0558.webp">
</PictureViewer>

## 描述

**Air Quality**是一款一体化低功耗空气质量监测装置。内置多功能空气质量传感器 **SEN55** 和 CO2 传感器 SCD40，能监测空气中的 PM1.0、PM2.5、PM4、PM10 颗粒物、温度、湿度、VOC 和 CO2 浓度。采用 StampS3 主控，8MB Flash，配备 1.54 寸墨水屏，分辨率为 200 x 200 ，掉电后也能显示最终画面。内置 600 mah 电池及 RTC 低功耗电源管理电路，能实现休眠及定时唤醒。出厂固件默认将数据上传至 M5 的 EZDATA 云平台，自动生成监控页面，为用户提供方便的远程云端访问方式。底部设有乐高安装孔、吸附磁铁和 4 个插拔式挂耳，支持多样的固定方式。适用于家庭、学校、工业、医院空气环境的长时间在线监测等领域。

## 教程 & 快速上手

learn>| ![Arduino IDE](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/arduino_banner_01.png) | [Arduino IDE](/zh_CN/arduino/m5air_quality/program) | 本教程将向你介绍，如何通过 Arduino IDE 编程控制 Air Quality 设备。 |

learn>| ![UiFlow2](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/uiflow2.0_banner_01.png) | [UiFlow2](/zh_CN/uiflow2/airq/program) | 本教程将向你介绍，如何通过 UiFlow2 图形化编程平台控制 Air Quality 设备。 |

## 产品特性

- SEN55 和 SCD40 传感器
- 1.54 寸墨水屏 (分辨率 200 x 200)
- 内置 600mAh 电池
- Grove 接口
- EZDATA 云平台访问
- RTC 定时唤醒
- 开发平台
  - UiFlow2
  - Arduino IDE
  - ESP-IDF
  - PlatformIO

## 包装内容

- 1 x Air Quality
- 1 x 操作说明书

## 应用场景

- 家庭环境监测
- 工业自动化
- 医疗场所
- 科研实验室
- 远程监测应用
- 空调系统优化
- 建筑工地

## 规格参数

| 规格         | 参数                                                        |
| ------------ | ----------------------------------------------------------- |
| 模组型号     | StampS3                                                     |
| SoC          | ESP32S3FN8@Xtensa LX7 双核，主频 240MHz                     |
| USB          | USB OTG, USB Serial/JTAG                                    |
| Flash        | 8MB                                                         |
| Wi-Fi        | 2.4 GHz Wi-Fi                                               |
| 分辨率       | 200 x 200px                                                 |
| SEN55        | I2C 地址：0x69                                              |
| SCD40        | I2C 地址：0x62                                              |
| 环境检测类型 | PM1.0、PM2.5、PM4、PM10 颗粒物、温度、湿度、VOC 和 CO2 浓度 |
| RTC          | RTC8563                                                     |
| 电池         | 600mAh@3.7V                                                 |
| 按键         | 按键 A (G0)，按键 B (G8)，开机按键，复位与关机              |
| Grove 接口   | HY2.0-4P                                                    |
| 蜂鸣器       | 板载无源蜂鸣器                                              |
| 固定结构     | 乐高安装孔、吸附磁铁和 4 个 M3 插拔式挂耳                   |
| 工作温度     | 0 ~ 40°C                                                    |
| 产品尺寸     | 72.0 x 56.0 x 24.1mm                                        |
| 产品重量     | 91.9g                                                       |
| 包装尺寸     | 100.8 x 74.3 x 30.5mm                                       |
| 毛重         | 120.0g                                                      |

## 操作说明

### 开关机操作

- 开机：可通过按 "WAKE" 按钮，以及 RTC 定时触发的 IRQ 信号进行唤醒启动，在完成触发唤醒信号后，在程序初始化中需要设置 hold (G46) 引脚为高电平 (1) 对电源进行维持，否则设备将重新进入休眠状态。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/467/01.jpg" width="40%" />

- 关机：在无 USB 外部供电时，按 RST 按键实现，或者无 USB 外部供电时，在程序运行中设置 HOLD (GPIO46)=0，即实现断电关机。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/467/02.jpg" width="40%" />

### 进入下载模式

如果要进入下载模式，请在先关机，然后按住 StampS3 上的 BooT 按键或 Air Quality 上 G0 键的同时插入 USB，通电之后再松开。

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/AirQ/airq%20(2).gif" width="30%" />

### 使用手册

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/467/K131_AIR_Quality_user_manual_ch_sch_01.jpg" width="100%" />

## 原理图

- [Air Quality 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/467/Sch_AirQ_v1.0.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/467/Sch_AirQ_v1.0_sch_01.png">
</SchViewer>

## 管脚映射

### 电源控制

| ESP32-S3           | G10      | G46  | G42  | G14 |
| ------------------ | -------- | ---- | ---- | --- |
| SEN55 POWER SWITCH | AirPWREN |      |      |     |
| HOLD               |          | HOLD |      |     |
| WAKE               |          |      | WAKE |     |
| BATTERY DETECT     |          |      |      | G14 |

### 显示屏

| ESP32-S3    | G1   | G2  | G3  | G4  | G5  | G6   |
| ----------- | ---- | --- | --- | --- | --- | ---- |
| GDEY0154D67 | BUSY | RST | D/C | CS  | SCK | MOSI |

### 输入交互

| ESP32-S3 | G9   | G0     | G8     |
| -------- | ---- | ------ | ------ |
| BEEP     | beep |        |        |
| BUTTON A |      | USER_A |        |
| BUTTON B |      |        | USER_B |

### 传感器

| ESP32-S3 | G11 | G12 |
| -------- | --- | --- |
| SEN55    | SDA | SCL |
| SCD40    | SDA | SCL |
| RTC8563  | SDA | SCL |

### HY2.0-4P

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | G13    | G15   |
::

## 尺寸图

<img alt="module size" src="https://static-cdn.m5stack.com/resource/docs/products/core/AirQ/img-cb5c5066-ca41-40f2-943c-64ddc02de03b.jpg" width="100%" />

## 结构文件

- [Air Quality 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/K131_Air_Quality/Structures)

## 数据手册

- [SEN55 Datasheet](https://static-cdn.m5stack.com/resource/docs/products/core/AirQ/Sensirion_Datasheet_Environmental_Node_SEN5x.pdf-9e2861345ac4a2cd640cc28e0e2d2a07.pdf)
- [SCD40 Datasheet](https://static-cdn.m5stack.com/resource/docs/datasheet/unit/co2/SCD40.pdf)
- [GDEY0154D67 Datasheet](<https://static-cdn.m5stack.com/resource/docs/products/core/AirQ/GDEY0154D67(1).pdf>)

## 软件开发

### Arduino

- [Air Quality Arduino 快速上手](/zh_CN/arduino/m5air_quality/program)
- [Air Quality Arduino M5Unified 驱动库](https://github.com/m5stack/M5Unified)
- [Air Quality Arduino M5GFX 驱动库](https://github.com/m5stack/M5GFX)

### UiFlow2

- [Air Quality UiFlow2 快速上手](/zh_CN/uiflow2/airq/program)

### PlatformIO

- [Air Quality 出厂固件](https://github.com/m5stack/AirQUserDemo)

?> 恢复出厂固件 | 若 Air Quality 设备先前烧录了 UiFlow 固件并进行了用户绑定，请在重新烧录 Air Quality 出厂固件前，在 UiFlow2 设备列表中对设备进行解绑，否则出厂固件运行时，数据可能无法正常上传至 Ezdata。

```bash
[env:m5stack-stamp-s3]
platform = espressif32
board = esp32-s3-devkitc-1
framework = arduino
upload_speed = 1500000
build_flags =
    -DESP32S3
    -DCORE_DEBUG_LEVEL=5
    -DARDUINO_USB_CDC_ON_BOOT=1
	-DARDUINO_USB_MODE=1

lib_deps =
    M5Unified=https://github.com/m5stack/M5Unified
```

### Easyloader

| Easyloader            | 下载链接                                                                                                                      | 备注 |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ---- |
| Air Quality User Demo | [download](https://static-cdn.m5stack.com/resource/docs/products/core/AirQ/ezLoader-4d75c8e2-f671-4d2a-bb1d-9f8b7fea5da8.exe) | /    |

### 其他

- [Air Quality 恢复出厂固件](/zh_CN/guide/restore_factory/air_quality)

## 相关视频

- Air Quality 产品功能介绍

<video class="video-container" controls><source src="https://static-cdn.m5stack.com/resource/docs/products/core/AirQ/K131%20AirQ%20%E8%A7%86%E9%A2%91.mp4" type="video/mp4"></video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=1355860383&bvid=BV1mz421B7M9&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/DkgFmuna7PM?si=oedpEcYs8zJLHzbw" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
