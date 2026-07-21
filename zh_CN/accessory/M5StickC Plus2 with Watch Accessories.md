# StickC-Plus2 Watch Kit

<span class="product-sku">SKU:K016-H2</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/accessory/M5StickC Plus2 with Watch Accessories/img-cca2ed45-bd1a-4954-b9dc-581467d0192a.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/accessory/M5StickC Plus2 with Watch Accessories/img-e33d7612-5e1d-4b11-bb31-9a10940ccc58.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/accessory/M5StickC Plus2 with Watch Accessories/img-ffb23ba0-4c32-475a-b26f-2e690e86d5b7.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/accessory/M5StickC Plus2 with Watch Accessories/img-ad370bf9-0434-410f-a2b3-7529f70f3b09.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/accessory/M5StickC Plus2 with Watch Accessories/img-882abfaf-5728-4290-aed7-d863ed3dbdc4.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/accessory/M5StickC Plus2 with Watch Accessories/img-ee87c0e5-0403-42d6-bfea-5a1c7cd742ad.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1113/K016-H2-02.jpg">

</PictureViewer>

## 描述

**StickC-Plus2 Watch Kit** 是一款包含 M5StickC Plus2 物联网开发板和一系列表带配件的手表套装，基于 StickC-Plus2 自身强大的硬件资源与拓展性，除了能够用于时间显示，还可以实现运动状态监控，智能家居控制等应用。 搭配 M5Stack HAT 硬件周边体系进行二次开发，能够赋予智能穿戴更多的应用可能。

## 产品特性

- 个性化支持自定义显示屏
- 200mAh 电池
- 轻巧便携

## 包装内容

- 1 x StickC-Plus2
- 1 x LEGO 适配件
- 1 x Wall/1515
- 1 x 表带
- 1 x Type-C USB(50cm)

## 应用场景

- 智能手表

## 规格参数

| 规格           | 参数                                            |
| -------------- | ----------------------------------------------- |
| SoC            | ESP32-PICO-V3-02@双核处理器，主频 240MHz        |
| Flash          | 8MB                                             |
| PSRAM          | 2MB                                             |
| Wi-Fi          | 2.4 GHz Wi-Fi                                   |
| 输入电压       | 5V@500mA                                        |
| 接口           | USB Type-C x 1, GROVE (I2C+I/O+UART) x 1        |
| LCD 屏幕       | 1.14 inch, 135 x 240 Colorful TFT LCD, ST7789v2 |
| 麦克风         | SPM1423                                         |
| 按键           | 自定义按键 x 3                                  |
| 电源指示 LED   | 绿色 LED x 1 (不可编程)                         |
| RTC            | BM8563                                          |
| 蜂鸣器         | 板载蜂鸣器                                      |
| MEMS           | MPU6886                                         |
| 天线           | 2.4G 3D 天线                                    |
| 外接引脚       | G0, G25/G26, G36, G32, G33                      |
| 电池           | 200mAh@3.7V, inside                             |
| 工作温度       | 0~40°C                                          |
| 表带尺寸及重量 | 230 x 22 x 6mm / 12.3g                          |
| 产品尺寸       | 38.0 x 26.7 x 10.6mm                            |
| 产品重量       | 28.8g                                           |
| 包装尺寸       | 125.0 x 65.0 x 23.0mm                           |
| 毛重           | 72.0g                                           |

## 操作说明

### 开关机

\#> 开关机 | 开机：<br/>可通过按 “BUTTON C“按钮超过 2 秒，或者 RTC 定时触发的 IRQ 信号进行唤醒启动，在完成触发唤醒信号后，在程序初始化中需要设置 hold (G4) 引脚为高电平 (1) 对电源进行维持，否则设备将重新进入关机状态。<br/>关机：<br/>在无 USB 外部供电时，按 “BUTTON C“按键超过 6 秒。或者无 USB 外部供电时，在程序运行中设置 HOLD (GPIO4)=0，即实现断电关机。连接着 USB 时，按 “BUTTON C“按键超过 6 秒，关断屏幕进入休眠状态，但不是断电关机。

## 原理图

- [StickC-Plus2原理图PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/512/Sch_M5StickC_Plus2_v0.5.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/512/Sch_M5StickC_Plus2_v0.5_page_01.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/512/Sch_M5StickC_Plus2_v0.5_page_02.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/512/Sch_M5StickC_Plus2_v0.5_page_03.png">
</SchViewer>

## 尺寸图

<SchViewer>
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5StickC%20PLUS2/148c931a782264fa73700b89a6060bb.jpg">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5StickC%20PLUS2/e537f92bdea6ec347037fd8ee014b84.jpg">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5StickC%20PLUS2/f1243c84791dc7551d58d683edb6aab.jpg">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/m5stickc_plus/%E5%B0%BA%E5%AF%B8%E5%9B%BE.jpg">
</SchViewer>

## 数据手册

- [ESP32-PICO-V3-02](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/669/esp32-pico_series_datasheet_cn.pdf)
- [ST7789v2](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/ST7789V.pdf)
- [BM8563](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/BM8563_V1.1_cn.pdf)
- [MPU6886](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/MPU-6886-000193%2Bv1.1_GHIC_en.pdf)
- [SPM1423](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/SPM1423HM4H-B_datasheet_en.pdf)

## 软件开发

### Arduino

- [StickC-Plus2 Arduino 驱动库](https://github.com/m5stack/M5StickCPlus2)
- [StickC-Plus2 Factory Test](https://github.com/m5stack/M5StickCPlus2-UserDemo)

### USB 驱动

\#> 点击下方连接下载匹配操作系统的驱动程序。CP34X (适用于**CH9102**) 驱动程序压缩包。在解压压缩包后，选择对应操作系统位数的安装包进行安装。 在使用时，若出现无法正常下载程序 (提示超时或者是 Failed to write to target RAM) 的情况，可尝试重新安装设备驱动。

| 驱动名称                  | 适用驱动芯片 | 下载链接                                                                                             |
| ------------------------- | ------------ | ---------------------------------------------------------------------------------------------------- |
| CH9102_VCP_SER_Windows    | CH9102       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CH9102_VCP_SER_Windows.exe) |
| CH9102_VCP_SER_MacOS v1.7 | CH9102       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CH9102_VCP_MacOS_v1.7.zip)  |

### EasyLoader

| Easyloader                           | Download                                                                                                                             | Note |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ---- |
| StickC-Plus2 Factory Test Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5StickC%20PLUS2/PLUS2%20Factory%20Firmware.exe) | /    |

## 相关视频

- StickC-Plus2 Watch Kit 功能介绍

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5StickC%20PLUS2/StackC%20Plus2%20%E8%A7%86%E9%A2%91.mp4" type="video/mp4"></video>
