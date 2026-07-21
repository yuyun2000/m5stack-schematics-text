# StampFly v1.1

<span class="product-sku">SKU:K138-V11</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1247/K138-V11_StampFly_v1.1_main_pictures_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1247/K138-V11_StampFly_v1.1_main_pictures_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1247/K138-V11_StampFly_v1.1_main_pictures_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1247/K138-V11_StampFly_v1.1_main_pictures_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1247/K138-V11_StampFly_v1.1_main_pictures_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1247/K138-V11_StampFly_v1.1_main_pictures_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1247/K138-V11_StampFly_v1.1_main_pictures_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1247/K138-V11_StampFly_v1.1_main_pictures_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1247/K138-V11_StampFly_v1.1_main_pictures_09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1247/K138-V11_StampFly_v1.1_main_pictures_10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1247/K138-V11_StampFly_v1.1_main_pictures_11.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1247/K138-V11_StampFly_v1.1_main_pictures_12.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1247/K138-V11-weight.jpg">
</PictureViewer>

## 描述

StampFly v1.1 是一款可编程的开源四轴飞行器套件，作为 StampFly 系列的迭代升级版本，其核心改进在于主控模组由 Stamp-S3 升级为性能更强的 Stamp-S3A，全新优化了天线结构设计，显著提升了无线信号接收性能，使遥控连接更加稳定。

整机集成 BMI270 六轴陀螺仪与 BMM150 三轴磁罗盘，精准完成姿态及方位检测；搭配 BMP280 气压传感器与两路 VL53L3 距离传感器，稳定实现精准定高与智能避障。板载蜂鸣器、复位按键及 WS2812 RGB 灯珠，用于人机交互与设备状态提示；标配 320mAh 高压动力电池与四组高速空心杯电机，动力输出充沛。

板载 INA3221AIRGVR 芯片可实时监测设备电流与电压，预留两路 Grove 拓展接口，可灵活外接各类传感器与外设。产品出厂预装调试程序，搭配 Atom Joystick 遥控器使用，基于 ESP-NOW 协议建立无线通信，支持手动、自动两种飞行模式，可轻松实现定点悬停、空中翻转等飞行效果，全套固件源代码开源，方便用户二次开发与功能自定义，适用于科创教育、科研实验、无人机项目开发、嵌入式学习实训等场景。

## 教程 & 快速上手

learn>| ![StampFly & Atom Joystick 使用教程](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/app/Stamp%20Fly/8313a0f7cc86ee549103b4ecc0991c8.png) | [StampFly & Atom Joystick 使用教程](/zh_CN/guide/hobby_kit/stampfly/stamply_firmware) | 本教程将向你介绍，如何通过 M5Burner 给 StampFly & Atom Joystick 烧录出厂固件，配对以及四轴飞行器的基本操作和指示。 |

## 注意事项

\#> 充电注意事项 | 将电池插到 Atom Joystick 充电槽，数据线连接 Atom Joystick 即可进行充电。

?> 电池维护事项 | 1. 在负载下，切勿将电池放电至每节电池 3V 以下。<br/>2. 充满电的电池不要存放超过 3 天。长期存放时，请将电压保持在 3.8V ~ 3.9V 之间。

## 产品特性

- Stamp-S3A 作为主控
- BMP280 大气压力检测
- VL53L3 距离传感器定高和避障
- 6 轴姿态传感器
- 3 轴磁罗盘方向检测
- 320mAh 高压动力电池
- 电流电压检测
- Grove 口扩展

## 包装内容

- 1x Stamp Fly v1.1
- 1x 320mAh 高压锂电池
- 1x 拆桨器
- 2x 螺旋桨 (0.8mm 孔径)

## 应用场景

- 科创教育
- 开源 DIY 创意制作
- 无人机研发开发
- 智能飞行算法验证

## 规格参数

| 规格           | 参数                                   |
| -------------- | -------------------------------------- |
| 模组型号       | Stamp-S3A                              |
| SoC            | ESP32-S3@Xtensa LX7 双核，主频 240MHz  |
| USB            | USB OTG, USB Serial/JTAG               |
| Flash          | 8MB                                    |
| Wi-Fi          | 2.4 GHz Wi-Fi                          |
| 驱动电机       | 716-17600kv                            |
| 距离传感器     | VL53L3C（7 位精度，最大检测距离 3 米） |
| 大气压力传感器 | BMP280（检测范围：300~1100hPa）        |
| 三轴磁传感器   | BMM150                                 |
| 六轴姿态传感器 | BMI270                                 |
| 接口类型       | I2C / UART                             |
| 电池规格       | 320mAh 高压锂电池                      |
| 电池输出电压   | 4.35V                                  |
| 续航时长       | 约 4 分钟                              |
| 充电参数       | 输入 5V@1A，充满时长约 55 分钟         |
| 检测模块       | INA3221AIRGVR 电压 / 电流检测芯片      |
| 蜂鸣器         | 板载 5020 无源蜂鸣器                   |
| 工作温度       | 0 ~ 40°C                               |
| 产品重量       | 27.6g                                  |
| 产品尺寸       | 73.6 x 73.6 x 32.0mm                   |
| 包装尺寸       | 126.0 x 99.0 x 30.0mm                  |
| 毛重           | 80.0g                                  |

## 操作说明

?> BMM150 磁场干扰 | 带有磁铁的产品可能对 BMM150 磁场传感器造成干扰，导致读数异常。当搭配含有磁铁的 M5 主控设备时，需拆除磁铁，同时避免 BMM150 传感器放置在强磁场附近。

### 桨叶安装方向示意图

#>说明|可使用[StampFly维修套件](/zh_CN/accessory/Stamp%20Fly%20Accessory%20Kit)更换桨叶。安装时请注意桨叶的方向，避免安装错误导致设备无法正常使用。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1247/V138-V11-StampFly-v1.1_operate_01.jpg" width="70%">

## 原理图

- [StampS3_Fly_Hat 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1069/StampS3_Fly_Hat.pdf)
- [Stamp_Fly 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1069/Stamp_Fly_v1.0.pdf)
- [PMW3901MB 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1069/Sch_PMW3901MB_SPI.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1069/StampS3_Fly_Hat_page_01.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1069/Stamp_Fly_v1.0_page_01.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1069/Sch_PMW3901MB_SPI_page_01.png">
</SchViewer>

## 管脚映射

### I2C 接口

| StampFly v1.1 (Stamp-S3A) | G3      | G4      |
| ------------------------- | ------- | ------- |
| INA3221AIRGVG (0x40)      | INA_SDA | INA_SCL |
| BMM150 (0x10)             | INA_SDA | INA_SCL |
| BMP280 (0x76)             | INA_SDA | INA_SCL |
| VL53L3 (0x29)             | INA_SDA | INA_SCL |

### SPI 接口

| StampFly v1.1 (Stamp-S3A) | G14  | G44 | G43  | G46 | G12 |
| ------------------------- | ---- | --- | ---- | --- | --- |
| BMI270                    | MOSI | SCK | MISO | CS  |     |
| PMW3901MB-TXQT            | MOSI | SCK | MISO |     | CS2 |

### Grove 接口

| StampFly v1.1 (Stamp-S3A) | G13 | G15 | G1      | G2      |
| ------------------------- | --- | --- | ------- | ------- |
| Grove (RED)               | SDA | SCL |         |         |
| Grove (BLACK)             |     |     | GROVE I | GROVE O |

### 蜂鸣器和 RGB 灯珠

| StampFly v1.1 (Stamp-S3A) | G40  | G39 |
| ------------------------- | ---- | --- |
| BEEP                      | BEEP |     |
| WS2812                    |      | RGB |

## 尺寸图

- [StampFly v1.1 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1247/K138-V11_StampFly_v1.1_model_size.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1247/K138-V11_StampFly_v1.1_model_size_page_01.png" width="100%">

## 结构文件

- [StampFly v1.1 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/K138_StampFly/Structures)

## 数据手册

- [VL53L3(ToF)](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/app/Stamp%20Fly/VL53L3.PDF)
- [PMW3901MB-TXQT](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/app/Stamp%20Fly/PMW3901MB-TXQT.PDF)
- [BMP280](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/app/Stamp%20Fly/BMP280.PDF)
- [BMM150](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/app/Stamp%20Fly/BMM150.PDF)
- [BMI270](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/app/Stamp%20Fly/BMI270.PDF)

## 软件开发

### Arduino

- [StampFly v1.1 Firmware](https://github.com/m5stack/M5StampFly)

### Easyloader

| Easyloader                   | 下载链接                                                                                                   | 备注 |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------- | ---- |
| StampFly Firmware Easyloader | [download](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1247/K138-V11-StampFly-V1.1-user-demo_0x0.exe) | /    |

## 相关视频

- Atom JoyStick 搭配 Stamp Fly 四轴飞行器基本功能演示

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/app/Stamp%20Fly/StampFly%E3%80%81AtomJoyStick%20video.mp4" type="video/mp4"></video>

## 产品对比

::compare-table
| 产品对比项             | [StampFly v1.1](/zh_CN/app/StampFly_v1.1)![StampFly v1.1](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1247/K138-V11_StampFly_v1.1_main_pictures_02.webp) | [StampFly](/zh_CN/app/Stamp%20Fly)![StampFly](https://static-cdn.m5stack.com/resource/docs/products/app/Stamp%20Fly/3.webp) |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| 核心模组               | Stamp-S3A                                                                                                                                                     | StampS3                                                                                                                     |
| 天线设计               | 优化设计，信号更强                                                                                                                                            | 常规设计                                                                                                                    |
| StampS3 模组 Boot 按键 | 优化按键手感，按键采用 4.0 x 3.0 x 2.0mm 规格                                                                                                                 | 按键规格 2.6 x 1.6 x 0.55mm                                                                                                 |
| 功耗表现               | 经过优化，实现更低功耗                                                                                                                                        | 常规设计                                                                                                                    |
| 电池容量               | 320mAh                                                                                                                                                        | 300mAh                                                                                                                      |
::
