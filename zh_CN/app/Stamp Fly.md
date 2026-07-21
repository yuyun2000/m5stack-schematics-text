# StampFly

<span class="product-sku">SKU:K138</span>

<PictureViewer>
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/app/Stamp%20Fly/4.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/app/Stamp%20Fly/5.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/app/Stamp%20Fly/13.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/app/Stamp%20Fly/6.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/app/Stamp%20Fly/7.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/app/Stamp%20Fly/8.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/app/Stamp%20Fly/9.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/app/Stamp%20Fly/10.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/app/Stamp%20Fly/11.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1069/K138-weight.jpg">
</PictureViewer>

## 描述

**Stamp Fly**是一款可编程的开源四轴飞行器套件，以 Stamp-S3 为主控，集成了 BMI270 6 轴陀螺仪和 BMM150 3 轴磁罗盘提供姿态和方向检测，BMP280 气压传感器和两路 VL53L3 距离传感器，实现精准的定高和避障功能，蜂鸣器、复位按钮和 WS2812 RGB 灯珠用于互动和状态指示。配备 300mAh 高压动力电池和四个高速空心杯电机。PCB 板载 INA3221AIRGVR 实时监测电流 / 电压，预留的两个 Grove 接口方便扩展其他传感器和外设。出厂预装调试程序，搭配 Atom JoyStick 作为遥控，通过 ESP-NOW 协议通信，用户根据需要可选择自动或手动模式，轻松实现定点飞行和翻转等功能，固件源代码开源。该产品适用于教育，科研以及各类无人机开发等项目。

## 教程 & 快速上手

learn>| ![初次使用烧录固件教程](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/app/Stamp%20Fly/8313a0f7cc86ee549103b4ecc0991c8.png) | [StampFly & Atom Joystick 固件烧录，上手教程](/zh_CN/guide/hobby_kit/stampfly/stamply_firmware) | 本教程将向你介绍，如何通过 M5Burner 给 StampFly & Atom Joystick 烧录出厂固件，配对以及四轴飞行器的基本操作和指示 |

## 注意事项

\#> 充电注意事项 | 将电池插到 Atom Joystick 充电槽进行充电，数据线连接 Atom Joystick 即可进行充电。

?> 电池维护事项 | 1. 在负载下，切勿将电池放电至每节电池 3V 以下。<br/>2. 充满电的电池不要存放超过 3 天。长期存放时，请将电压保持在 3.8V 和 3.9V 之间。

## 产品特性

- Stamp-S3 作为主控
- BMP280 大气压力检测
- VL53L3 距离传感器定高和避障
- 6 轴姿态传感器
- 3 轴磁罗盘方向检测
- 蜂鸣器
- 300mAh 高压动力电池
- 电流电压检测
- Grove 口扩展

## 包装内容

- 1x Stamp Fly
- 1x 300mAh 高压锂电池
- 1x 拆桨器
- 2x 螺旋桨 (0.8mm 孔径)

## 应用场景

- 教育
- 科研
- 无人机开发
- DIY 项目

## 规格参数

| 规格                    | 参数                                  |
| ----------------------- | ------------------------------------- |
| 模组型号                | Stamp-S3                              |
| SoC                     | ESP32-S3@Xtensa LX7 双核，主频 240MHz |
| USB                     | USB OTG, USB Serial/JTAG              |
| Flash                   | 8MB                                   |
| Wi-Fi                   | 2.4 GHz Wi-Fi                         |
| 电机                    | 716-17600kv                           |
| 距离传感器              | VL53L3C 0x29 (7-bits) 最大 3 米       |
| 大气压力传感器          | BMP280 (0x76)@300-1100hPa             |
| 3 轴磁传感器            | BMM150 (0x10)                         |
| 6 轴姿态传感器          | BMI270                                |
| Grove                   | I2C+UART                              |
| 电池                    | 300mAh 高压锂电池                     |
| 电池输出电压            | 4.35V                                 |
| 续航                    | 约 4 分钟                             |
| 充电时间（Input:5V@1A） | 55min                                 |
| 电流 / 电压检测         | INA3221AIRGVR (0x40)                  |
| 蜂鸣器                  | 无源板载蜂鸣器 @5020                  |
| 工作温度                | 0 ~ 40°C                              |
| 产品重量                | 27.7g                                 |
| 产品尺寸                | 81.5 x 81.5 x 31mm                    |
| 包装尺寸                | 162 x 99 x 36mm                       |
| 毛重                    | 70.7g                                 |

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

| StampFly (Stamp-S3) | G3      | G4      |
| ------------------- | ------- | ------- |
| INA3221AIRGVG       | INA_SDA | INA_SCL |
| BMM150              | INA_SDA | INA_SCL |
| BMP280              | INA_SDA | INA_SCL |
| VL53L3              | INA_SDA | INA_SCL |

### SPI 接口

| StampFly (Stamp-S3) | G14  | G44 | G43  | G46 | G12 |
| ------------------- | ---- | --- | ---- | --- | --- |
| BMI270              | MOSI | SCK | MISO | CS  |     |
| PMW3901MB-TXQT      | MOSI | SCK | MISO |     | CS2 |

### Grove 接口

| StampFly (Stamp-S3) | G13 | G15 | G1      | G2      |
| ------------------- | --- | --- | ------- | ------- |
| Grove (RED)         | SDA | SCL |         |         |
| Grove (BLACK)       |     |     | GROVE I | GROVE O |

### 蜂鸣器和 RGB 灯珠

| StampFly (Stamp-S3) | G40  | G39 |
| ------------------- | ---- | --- |
| BEEP                | BEEP |     |
| WS2812              |      | RGB |

## 尺寸图

<img alt="module size" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/app/Stamp%20Fly/%E5%B0%BA%E5%AF%B8%E5%9B%BE.jpg" width="100%" />

## 结构文件

- [StampFly 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/K138_StampFly/Structures)

## 数据手册

- [VL53L3(ToF)](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/app/Stamp%20Fly/VL53L3.PDF)
- [PMW3901MB-TXQT(Optical Flow Sensor Chip)](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/app/Stamp%20Fly/PMW3901MB-TXQT.PDF)
- [BMP280(Pressure Sensor Chip)](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/app/Stamp%20Fly/BMP280.PDF)
- [BMM150(3D Magnetometer Compass)](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/app/Stamp%20Fly/BMM150.PDF)
- [BMI270(6-axis Inertial Measurement Unit (IMU) Sensor)](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/app/Stamp%20Fly/BMI270.PDF)

## 软件开发

### Arduino

- [StampFly Firmware](https://github.com/m5stack/M5StampFly)

### Easyloader

| Easyloader                   | 下载链接                                                                                                                   | 备注 |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ---- |
| StampFly Firmware Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/app/Stamp%20Fly/Stamp%20Fly%20Firmware.exe) | /    |

## 相关视频

- Atom JoyStick 搭配 Stamp Fly 四轴飞行器基本功能演示

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/app/Stamp%20Fly/StampFly%E3%80%81AtomJoyStick%20video.mp4" type="video/mp4"></video>
