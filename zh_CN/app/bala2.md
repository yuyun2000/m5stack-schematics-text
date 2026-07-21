# Bala2

<span class="product-sku">SKU:K014-C</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/bala2/bala2_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/bala2/bala2_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/bala2/bala2_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/bala2/bala2_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/bala2/bala2_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/bala2/bala2_06.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/bala2/bala2_07.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/bala2/bala2_08.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/bala2/bala2_09.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/bala2/bala2_10.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/bala2/bala2_11.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/bala2/bala2_12.webp">
</PictureViewer>

## 描述

**Bala2** 是一款平衡车应用。该产品是由[M5Stack Gray](/zh_CN/core/gray) 与 BALA2 电机底座组合而成的一款自平衡机器人，底座采用 STM32F030C8T6 作为主控，由两路 N20 编码减速电机提供动力，内置 1200mAh 电池，其 "BALA" 名称的由来出自 "Balance" 一词的缩写，目前为第二代产品。BALA2 底座包含了丰富的接口，除了常规的 PortB、PortC 外还支持 8 路舵机，其中 4 路接口可直接连接，其余 4 路需从底座内部引出。您可以通过编程控制它自由行走，也可以结合 WiFi 开发遥控功能。即使您从来没有接触过平衡车程序，您也可以通过 UiFlow 快速完成编程对它进行控制。出厂默认预装平衡车应用程序，在运行时使用 PID 闭环算法保持垂直平衡，利用加速度计与陀螺仪姿态数据来校正其方向和位置。

## 教程 & 快速上手

learn>| ![BALA2](https://static-cdn.m5stack.com/resource/docs/products/app/bala2/bala2_09.webp) | [Usage and Sensor calibration](/zh_CN/guide/hobby_kit/bala2/bala2_quick_start) | 出厂时 BALA2 已经进行校准，开机即可自动保持平衡，如需手动进行校准请参考该教程 |

## 产品特性

- 9 轴姿态传感器
- 双轮驱动，PID 控制平衡
- Grove 扩展接口 (PORTB/PORTC)
- 8 路舵机驱动，4 路外接，4 路内置
- 支持 WiFi, 可编程
- 内置扬声器
- 支持 microSD 拓展
- 兼容 LEGO
- I2C 通信：0x3A
- 开发平台
  - MicroPython
  - UiFlow
  - Arduino

## 包装内容

- 1 x Gray
- 1 x Bala2 Base
- 2 x HY2.0-4P 连接线 (20cm)
- 4 x 轮毂连接器
- 2 x 乐高臂
- 1 x 内六角扳手
- 1 x USB Type-C 连接线 (1m)

## 应用场景

- Balancing car

## 规格参数

| 规格      | 参数                                                              |
| --------- | ----------------------------------------------------------------- |
| MCU       | STM32F030C8T6                                                     |
| ESP32     | 240MHz 双核，600 DMIPS，520KB SRAM，Wi-Fi，                       |
| Flash/RAM | 16MB Flash                                                        |
| LCD       | 2 英寸，320x240 彩色 TFT LCD, ILI9342C                            |
| 扬声器    | 1W-0928                                                           |
| MEMS      | BMM150+MPU6886                                                    |
| 电机驱动  | HR8833                                                            |
| 底座主控  | STM32F030                                                         |
| 接口      | GROVE I2C x 1/UART x 1/GPIO x 1/SERVO x 4 (+4 Extendable Channel) |
| 电池容量  | 1200mAh                                                           |
| 外壳材质  | Plastic                                                           |
| 产品尺寸  | 54.0 x 54.0 x 65.0mm                                              |
| 产品重量  | 157.0g                                                            |
| 包装尺寸  | 100.0 x 100.0 x 100.0mm                                           |
| 毛重      | 337.0g                                                            |

## 操作说明

?> BMM150 磁场干扰 | 带有磁铁的产品可能对 BMM150 磁场传感器造成干扰，导致读数异常。当搭配含有磁铁的 M5 主控设备时，需拆除磁铁，同时避免 BMM150 传感器放置在强磁场附近。

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/app/bala2/bala2_sch_01.webp" width="70%">

## 管脚映射

### HY2.0-4P

| Fire   | G22 | G21 | G26 | G36 | G16 | G17 |
| ------ | --- | --- | --- | --- | --- | --- |
| PORT A | SCL | SDA |     |     |     |     |
| PORT B |     |     | DAC | ADC |     |     |
| PORT C |     |     |     |     | RX  | TX  |

## 软件开发

### Arduino

- [Bala2 Balancing Example](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/Application/Bala2)

### Easyloader

| Easyloader                     | 下载链接                                                                                                                | 备注 |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------- | ---- |
| Bala2 Test Firmware Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/APPLICATION/EasyLoader_BALA2_APPICATION.exe) | /    |

## 相关视频

- 开机运行，按住 ButtonB + 左侧开机键进入校准模式，A/C 调整，B 键保存

<video id="example_video" controls>
   <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/App/BALA2.mp4" type="video/mp4">
</video>
