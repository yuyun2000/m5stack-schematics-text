# StickC-Plus Watch Kit

<span class="product-sku">SKU:K016-H</span>

<PictureViewer>
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/accessory/M5StickC%20Plus%20with%20Watch%20Accessories/4.jpg">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/accessory/M5StickC%20Plus%20with%20Watch%20Accessories/8.jpg">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/accessory/M5StickC%20Plus%20with%20Watch%20Accessories/10.jpg">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/accessory/M5StickC%20Plus%20with%20Watch%20Accessories/5.jpg">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/accessory/M5StickC%20Plus%20with%20Watch%20Accessories/6.jpg">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/accessory/M5StickC%20Plus%20with%20Watch%20Accessories/9.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1114/K016-H_02.jpg">
</PictureViewer>

## 描述

**StickC-Plus Watch Kit**是一款 M5StickC Plus 手表套装，包含 M5StickC Plus 物联网开发板和一系列表带配件。基于 M5StickC Plus 自身强大的硬件资源与拓展性，除了能够用于时间显示，还可以实现运动状态监控，智能家居控制等应用。 搭配 M5Stack HAT 硬件周边体系进行二次开发，更是能够赋予智能穿戴更多的应用可能。

## 产品特性

- 个性化支持自定义显示屏
- 200mAh 电池
- 轻巧便携

## 包装内容

- 1 x StickC-Plus
- 1 x LEGO 适配件
- 1 x Wall/1515
- 1 x 表带
- 1 x Type-C USB(50cm)

## 应用场景

- 智能手表

## 规格参数

| 主控资源       | 参数                                            |
| -------------- | ----------------------------------------------- |
| ESP32          | 240MHz dual core, 600 DMIPS, 520KB SRAM, Wi-Fi  |
| Flash 闪存     | 4MB Flash                                       |
| 输入电压       | 5V @ 500mA                                      |
| 接口           | Type-C x 1, GROVE (I2C+I/O+UART) x 1            |
| LCD 屏幕       | 1.14 inch, 135 x 240 Colorful TFT LCD, ST7789v2 |
| 麦克风         | SPM1423                                         |
| 按键           | 自定义按键 x 2                                  |
| LED            | 红色 LED x 1                                    |
| RTC            | BM8563                                          |
| PMU            | AXP192                                          |
| 蜂鸣器         | 板载蜂鸣器                                      |
| IR             | Infrared transmission                           |
| MEMS           | MPU6886                                         |
| 天线           | 2.4G 3D 天线                                    |
| 外接引脚       | G0, G25/G26, G36, G32, G33                      |
| 电池           | 120 mAh @ 3.7V, inside vb                       |
| 表带尺寸及重量 | 230 x 22 x 6mm / 12.3g                          |
| 产品尺寸       | StickC-Plus: 48.0 x 24.0 x 13.5mm               |
| 产品重量       | 29.2g                                           |
| 包装尺寸       | 126.0 x 67.0 x 22.0mm                           |
| 毛重           | 72.5g                                           |

## 操作说明

### 开关机

\#> 开机：<br/>可通过按 “BUTTON C“按钮超过 2 秒，或者 RTC 定时触发的 IRQ 信号进行唤醒启动，在完成触发唤醒信号后，在程序初始化中需要设置 hold (G4) 引脚为高电平 (1) 对电源进行维持，否则设备将重新进入关机状态。<br/>关机：<br/>在无 USB 外部供电时，按 “BUTTON C“按键超过 6 秒。连接着 USB 时，按 “BUTTON C“按键超过 6 秒，关断屏幕进入休眠状态，但不是断电关机。

## 原理图

- [StickC-Plus原理图PDF](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5StickC%20PLUS2/%E5%8E%9F%E7%90%86%E5%9B%BE.pdf)

<img alt="schematics" src="https://static-cdn.m5stack.com/resource/docs/products/core/M5StickC PLUS2/img-7381263f-5e60-48c2-8275-924b46e698f3.png" width="100%" />

## 尺寸图

<SchViewer>
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5StickC%20PLUS2/148c931a782264fa73700b89a6060bb.jpg">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5StickC%20PLUS2/e537f92bdea6ec347037fd8ee014b84.jpg">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5StickC%20PLUS2/f1243c84791dc7551d58d683edb6aab.jpg">
</SchViewer>

## 数据手册

- [ESP32-PICO](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/669/esp32-pico_series_datasheet_cn.pdf)
- [ST7789v2](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/ST7789V.pdf)
- [BM8563](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/BM8563_V1.1_cn.pdf)
- [MPU6886](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/MPU-6886-000193%2Bv1.1_GHIC_en.pdf)
- [AXP192 datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/AXP192_datasheet_en.pdf)
- [AXP192 register](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/AXP192_datasheet_cn.pdf)
- [SPM1423](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/SPM1423HM4H-B_datasheet_en.pdf)

## 软件开发

### Arduino

- [StickC-Plus Arduino 驱动库](https://github.com/m5stack/M5StickC-Plus)

### USB 驱动

\#> 点击下方连接下载匹配操作系统的驱动程序。CP34X (适用于**CH9102**) 驱动程序压缩包。在解压压缩包后，选择对应操作系统位数的安装包进行安装。 在使用时，若出现无法正常下载程序 (提示超时或者是 Failed to write to target RAM) 的情况，可尝试重新安装设备驱动。

| 驱动名称                  | 适用驱动芯片 | 下载链接                                                                                             |
| ------------------------- | ------------ | ---------------------------------------------------------------------------------------------------- |
| CH9102_VCP_SER_Windows    | CH9102       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CH9102_VCP_SER_Windows.exe) |
| CH9102_VCP_SER_MacOS v1.7 | CH9102       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CH9102_VCP_MacOS_v1.7.zip)  |

### Easyloader

| Easyloader                          | Download                                                                                                                  | Note |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ---- |
| StickC-Plus Factory Test Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/CORE/EasyLoader_M5StickC_Plus_FactoryTest.exe) | /    |

## 相关视频

- 加速计，麦克风，LED,IR,RTC, 无线连接等硬件测试，单击 A 键或 B 键可切换测试项.

<video id="example_video" controls>
  <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Core/M5StickC%20Plus.mp4" type="video/mp4">
</video>
