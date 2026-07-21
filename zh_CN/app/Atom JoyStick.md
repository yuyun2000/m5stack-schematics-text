# Atom JoyStick

<span class="product-sku">SKU:K137</span>

<PictureViewer>
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/app/Atom%20JoyStick/4.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/app/Atom%20JoyStick/5.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/app/Atom%20JoyStick/12.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/app/Atom%20JoyStick/6.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/app/Atom%20JoyStick/7.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/app/Atom%20JoyStick/8.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/app/Atom%20JoyStick/9.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/app/Atom%20JoyStick/10.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/app/Atom%20JoyStick/11.webp">
</PictureViewer>

## 描述

**Atom JoyStick** 是一款多用途可编程双摇杆遥控器，采用 AtomS3 作为主控，板上采用 STM32 实现协处理功能，配备 2 个霍尔传感器 5 方向摇杆，以及 2 个功能按键，内置 RGB 灯珠用于人机互动和状态提醒；配备两路高压动力电池充电电路。出厂预烧录 Stamp Fly 遥控固件，通过 ESP-NOW 协议与 Stamp Fly 通信，固件源代码开源。本产品适用于无人机操控、机器人控制、智能小车和各种 DIY 项目。

## 教程 & 快速上手

learn>| ![初次使用烧录固件教程](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/app/Atom%20JoyStick/c81e91d3b047ae3bee4895e69a7303b.png) | [StampFly & Atom Joystick 固件烧录，上手教程](/zh_CN/guide/hobby_kit/stampfly/stamply_firmware) | 本教程将向你介绍，如何通过 M5Burner 给 StampFly & Atom Joystick 烧录出厂固件，配对以及四轴飞行器的基本操作和指示 |

## 注意事项

?> 使用提醒 | 初次使用 Atom JoyStick 需要根据如下教程进行飞行固件烧录，才可以和 StampFly 进行配对飞行。

\#> 充电提醒 | 接通数据线充电，对应的电池前面有电源指示灯，**红色**代表电池正在充电，未充满电；**绿色**代表充满电，已达到 4.35V 的电压。

?> 电池维护事项 | 1. 在负载下，切勿将电池放电至每节电池 3V 以下。<br/>2. 充满电的电池不要存放超过 3 天。长期存放时，请将电压保持在 3.8V 和 3.9V 之间。

<img alt="schematics" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/app/Atom%20JoyStick/%E5%85%85%E7%94%B5.png" width="50%" />

## 产品特性

- STM32F030F4P6
- 配备 AtomS3
- 兼容 Atom 系列主控
- 双摇杆、双按键、拨动开关
- WS2812C RGB 灯珠
- 两路高压锂电池充电电路
- 电量检测

## 包装内容

- 1 x Atom JoyStick
- 1 x 300mAh 高压锂电池

## 应用场景

- 无人机操控
- 机器人控制
- 智能小车
- DIY 项目

## 规格参数

| 规格                       | 参数                 |
| -------------------------- | -------------------- |
| MCU                        | STM32F030F4P6        |
| MCU 通信地址               | 0x59                 |
| RGB                        | WS2812C              |
| 充电芯片                   | TP4067@4.35V         |
| 电池电量                   | 300mAh@1S            |
| 电池输出电压               | 4.35V                |
| 充电电流                   | DC 5V/430mA          |
| 电池充满时间 (Input:5V/1A) | 大约 55 分钟         |
| 电池输出电压               | 4.35V                |
| 按键                       | 左 / 右 按键         |
| 蜂鸣器                     | 板载无源蜂鸣器 @5020 |
| 工作温度                   | 0-40°C               |
| 产品尺寸                   | 84 x 60 x 31.5mm     |
| 包装尺寸                   | 162 x 99 x 36mm      |
| 产品重量                   | 63.5g                |
| 毛重                       | 96.7g                |

## 原理图

- [Atom JoyStick原理图 PDF](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/app/Atom%20JoyStick/Sch_AtomJoystick_v0.3.pdf)

<img alt="schematics" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/app/Atom%20JoyStick/c0a25d850ef9122df3669baeab813e5.png" width="100%" />

## 管脚映射

### AtomS3 与手柄底座

- I2C 通信 (0x59)

| Atom JoyStick (AtomS3) | G39(SCL) | G38(SDA)  |
| ---------------------- | -------- | --------- |
| STM32F030F4P6          | PA9(SCL) | PA10(SDA) |

### 蜂鸣器和 RGB 灯珠

| Atom JoyStick (AtomS3) | G5   | G6  |
| ---------------------- | ---- | --- |
| BEEP                   | BEEP |     |
| WS2812C                |      | RGB |

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

## 软件开发

### Arduino

- [Atom JoyStick StampFly Controller](https://github.com/m5stack/Atom-JoyStick/tree/main/examples/StampFlyController)

### 内置固件

- [Atom JoyStick 内置固件](https://github.com/m5stack/Atom-JoyStick-Internal-FW)

### Easyloader

| Easyloader                                   | 下载链接                                                                                                                           | 备注 |
| -------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---- |
| Atom JoyStick Controller Firmware Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/app/Atom%20JoyStick/Atom%20JoyStick%20Firmware.exe) | /    |

## 相关视频

- Atom JoyStick 搭配 Stamp Fly 四轴飞行器基本功能演示

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/app/Stamp%20Fly/StampFly%E3%80%81AtomJoyStick%20video.mp4" type="video/mp4"></video>
