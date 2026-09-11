# Atom JoyStick v1.1

<span class="product-sku">SKU:K137-V11</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/coming-soon.png">
</PictureViewer>

## 描述

**Atom JoyStick v1.1** 是 Atom JoyStick 的迭代升级版本，是一款多用途可编程双摇杆遥控器，主控由 AtomS3 升级为 [AtomS3R](/zh_CN/core/AtomS3R)。AtomS3R 集成 ESP32-S3-PICO-1-N8R8，配备 8MB Flash、8MB PSRAM 和 2.4 GHz Wi-Fi，并内置 BMI270 六轴姿态传感器与 BMM150 三轴地磁传感器。手柄底座采用 STM32F030F4P6 实现协处理功能，配备 2 个霍尔传感器五向摇杆、2 个功能按键、1 个拨动开关和 RGB 灯珠，并集成两路高压动力电池充电电路。产品出厂预烧录 StampFly 遥控固件，通过 ESP-NOW 协议与 StampFly 通信，固件源代码开源，适用于无人机操控、机器人控制、智能小车和各种 DIY 项目。

## 教程 & 快速上手

learn>| ![初次使用烧录固件教程](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/app/Atom%20JoyStick/c81e91d3b047ae3bee4895e69a7303b.png) | [StampFly & Atom JoyStick v1.1 固件烧录、上手教程](/zh_CN/guide/hobby_kit/stampfly/stamply_firmware) | 本教程将向你介绍，如何通过 M5Burner 给 StampFly 与 Atom JoyStick v1.1 烧录出厂固件，并完成设备配对、四轴飞行器基本操作及指示状态确认。 |

## 注意事项

?> 使用提醒 | 初次使用 Atom JoyStick v1.1 时，需要按照上述教程烧录遥控固件，完成后才可与 StampFly 配对飞行。

#> 充电提醒 | 接通数据线充电，对应的电池前面有电源指示灯，**红色**代表电池正在充电，未充满电；**绿色**代表充满电，已达到 4.35V 的电压。

?> 电池维护事项 | 1. 在负载下，切勿将电池放电至每节电池 3V 以下。<br/>2. 充满电的电池不要存放超过 3 天。长期存放时，请将电压保持在 3.8V 和 3.9V 之间。

<img alt="schematics" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/app/Atom%20JoyStick/%E5%85%85%E7%94%B5.png" width="50%" />

## 产品特性

- STM32F030F4P6
- 配备 AtomS3R
  - ESP32-S3-PICO-1-N8R8
  - 8MB Flash 和 8MB PSRAM
  - 0.85 寸 IPS 屏幕 (分辨率 128 x 128)
  - BMI270 六轴姿态传感器和 BMM150 三轴地磁传感器
  - 增强型 3D 天线
- 兼容 Atom 系列主控
- 双摇杆、双按键、拨动开关
- WS2812C RGB 灯珠
- 两路高压锂电池充电电路
- 电量检测

## 包装内容

- 1 x Atom JoyStick v1.1
- 1 x 300mAh 高压锂电池

## 应用场景

- 无人机操控
- 机器人控制
- 智能小车
- DIY 项目

## 规格参数

| 规格                       | 参数                                                             |
| -------------------------- | ---------------------------------------------------------------- |
| 主控                       | AtomS3R                                                          |
| SoC                        | ESP32-S3-PICO-1-N8R8 @ Xtensa® 32 位 LX7 双核处理器，主频 240MHz |
| Flash                      | 8MB                                                              |
| PSRAM                      | 8MB Octal                                                        |
| Wi-Fi                      | 2.4 GHz Wi-Fi                                                    |
| 显示屏                     | 0.85 寸 IPS 屏幕                                                 |
| 分辨率                     | 128 x 128                                                        |
| 六轴姿态传感器             | BMI270 (I2C 地址：0x68)                                          |
| 三轴地磁传感器             | BMM150 (通过 BMI270 Sensor Hub 接入)                             |
| 协处理器                   | STM32F030F4P6                                                    |
| 协处理器通信地址           | 0x59                                                             |
| RGB                        | WS2812C                                                          |
| 充电芯片                   | TP4067@4.35V                                                     |
| 电池电量                   | 300mAh@1S                                                        |
| 电池输出电压               | 4.35V                                                            |
| 充电电流                   | DC 5V/430mA                                                      |
| 电池充满时间 (Input:5V/1A) | 大约 55 分钟                                                     |
| 按键                       | 左 / 右按键                                                      |
| 蜂鸣器                     | 板载无源蜂鸣器 @5020                                             |
| 工作温度                   | 0 ~ 40°C                                                         |
| 产品尺寸                   | 84 x 60 x 31.5mm                                                 |
| 包装尺寸                   | xxxmm                                                            |
| 产品重量                   | xxxg                                                             |
| 毛重                       | xxxg                                                             |

## 原理图

- [Atom JoyStick 底座原理图 PDF](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/app/Atom%20JoyStick/Sch_AtomJoystick_v0.3.pdf)
- [AtomS3R 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/680/Sch_M5_AtomS3R_v0.4.1.pdf)

<img alt="schematics" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/app/Atom%20JoyStick/c0a25d850ef9122df3669baeab813e5.png" width="100%" />

## 管脚映射

### AtomS3R 与手柄底座

- I2C 通信 (0x59)

| Atom JoyStick v1.1 (AtomS3R)  | G39(SCL) | G38(SDA)  |
| ----------------------------- | -------- | --------- |
| STM32F030F4P6                 | PA9(SCL) | PA10(SDA) |

### 蜂鸣器和 RGB 灯珠

| Atom JoyStick v1.1 (AtomS3R)  | G5   | G6  |
| ----------------------------- | ---- | --- |
| BEEP                          | BEEP |     |
| WS2812C                       |      | RGB |

### 摇杆

| STM32F030F4P6  | PA1       | PA2       | PA3       | PA6        | PA5        | PA7        |
| -------------- | --------- | --------- | --------- | ---------- | ---------- | ---------- |
| JoyStick_LEFT  | LEFT-SW-X | LEFT-SW-Y | LEFT-SW-B |            |            |            |
| JoyStick_RIGHT |           |           |           | RIGHT-SW-X | RIGHT-SW-Y | RIGHT-SW-B |

### 按钮和电池检测

| STM32F030F4P6 | PF0      | PF1       | PA0      | PA1      |
| ------------- | -------- | --------- | -------- | -------- |
| Button_LEFT   | LEFT-BTN |           |          |          |
| Button_RIGHT  |          | RIGHT-BTN |          |          |
| BAT1-Detect   |          |           | BAT-ADC1 |          |
| BAT2-Detect   |          |           |          | BAT-ADC2 |

## 尺寸图

<img alt="module size" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/app/Atom%20JoyStick/%E5%B0%BA%E5%AF%B8%E5%9B%BE.jpg" width="100%" />

## 数据手册

- [TP4067(Battery Charge Chip)](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/app/Atom%20JoyStick/TP4067.PDF)

<!--待更新

## 软件开发

### Arduino

- [Atom JoyStick v1.1 StampFly Controller](https://github.com/m5stack/Atom-JoyStick/tree/main/examples/StampFlyController)

### 内置固件

- [Atom JoyStick v1.1 内置固件](https://github.com/m5stack/Atom-JoyStick-Internal-FW)

### Easyloader

| Easyloader                                   | 下载链接                                                                                                                           | 备注 |
| -------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---- |
| Atom JoyStick v1.1 Controller Firmware Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/app/Atom%20JoyStick/Atom%20JoyStick%20Firmware.exe) | /    |   -->

## 相关视频

- Atom JoyStick v1.1 搭配 StampFly 四轴飞行器基本功能演示

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/app/Stamp%20Fly/StampFly%E3%80%81AtomJoyStick%20video.mp4" type="video/mp4"></video>

## 产品对比

::compare-table
| 产品对比表 | [Atom JoyStick v1.1](/zh_CN/app/Atom_JoyStick_v1.1) ![Atom JoyStick v1.1](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/coming-soon.png)                          | [Atom JoyStick](/zh_CN/app/Atom%20JoyStick) ![Atom JoyStick](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/app/Atom%20JoyStick/4.webp)  |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 主控       | AtomS3R                                                                                                                                                                   | AtomS3                                                                                                                                                        |
| SoC        | ESP32-S3-PICO-1-N8R8                                                                                                                                                      | ESP32-S3FN8                                                                                                                                                   |
| 内存       | 8MB Flash + 8MB PSRAM                                                                                                                                                     | 8MB Flash                                                                                                                                                     |
| 姿态传感器 | BMI270 六轴姿态传感器                                                                                                                                                     | MPU6886 六轴姿态传感器                                                                                                                                        |
| 地磁传感器 | BMM150 三轴地磁传感器                                                                                                                                                     | /                                                                                                                                                             |
| 天线       | 增强型 3D 天线                                                                                                                                                            | 标准 3D 天线                                                                                                                                                  |
| 协处理器   | STM32F030F4P6                                                                                                                                                             | STM32F030F4P6                                                                                                                                                 |
::
