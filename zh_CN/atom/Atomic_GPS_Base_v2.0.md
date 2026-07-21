# Atomic GPS Base v2.0

<span class="product-sku">SKU:A134-V2</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1158/A134-V2-01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1158/A134-V2-02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1158/A134-V2-03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1158/A134-V2-04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1158/A134-V2-05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1158/A134-V2-06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1158/A134-V2-07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1158/A134-V2-08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1158/A134-V2-09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1158/A134-V2-10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1158/A134-V2-11.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1158/A134-V2-weight.jpg">
</PictureViewer>

## 描述

**Atomic GPS Base V2.0** 是一款基于 Atom 系列主机的 GPS 定位模组，集成高性能 AT6668 芯片，内置 MAX2659 低噪放、陶瓷天线，提供精确和可靠的卫星定位服务。采用 NMEA0183 4.1 协议输出，支持多频多模 GNSS 信号接收，可接收 GPS、BD2、BD3、GLONASS、GALILEO 和 QZSS 等多个卫星导航系统的信号，可用于高精度的多系统联合定位和单系统独立定位等应用，具备较强的抗干扰能力和较高的定位精度，适用于车载定位与导航、物联网定位设备、工业自动化与机器人定位、无人机定位等应用场景。

## 产品特性

- 支持多种卫星导航系统（GPS/QZSS/BD2/BD3/GAL/GLO）的单系统定位，或任意组合的多系统联合定位
- 多频点多系统接收
- 多通道
- 低功耗
- 最大定位更新率 10Hz
- 开发平台：
  - Arduino IDE
  - UiFlow1
  - UiFlow2

## 包装内容

- 1 x Atomic GPS Base v2.0

## 应用场景

- 车载定位与导航
- 物联网定位设备 (IoT)
- 户外定位设备
- 无人机定位

## 规格参数

| 规格     | 参数                                                             |
| -------- | ---------------------------------------------------------------- |
| SoC      | ATGM336H-6N-74 模组 @AT6668                                      |
| 卫星频点 | BDS：B1、B1C<br/>GPS/QZSS：L1<br/>GALILEO：E1<br/>GLONASS：L1    |
| 定位精度 | <1.5m (CEP50)                                                    |
| 通道数   | 50                                                               |
| 输出频率 | 1Hz（最大 10Hz）                                                 |
| 启动时间 | 冷启动：23s；热启动：1s；重捕捉：1s                              |
| 捕捉时间 | 1s                                                               |
| 波特率   | 115200bps@8N1                                                    |
| 数据格式 | NMEA0183                                                         |
| 灵敏度   | 跟踪：-167dBm；重捕捉：-160dBm；冷启动：-148dBm；热启动：-156dBm |
| 功耗     | 待机电流：DC 5.01V@4.95mA；工作电流：DC 5.02V@35.07mA            |
| 产品尺寸 | 48.0 x 24.0 x 17.5 mm                                            |
| 产品重量 | 13.2g                                                            |
| 包装尺寸 | 138.0 x 93.0 x 19.0mm                                            |
| 毛重     | 15.5g                                                            |

## 原理图

- [Atomic GPS Base v2.0 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1158/SCH-A134-V2.pdf)

<img alt="schematics" src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1158/SCH-A134-V2.png" width="100%" />

## 管脚映射

::m5-bus-table
| PIN | LEFT | RIGHT | PIN     |
| --- | ---- | ----- | ------- |
|     |      | 1     | NC      |
| NC  | 2    | 3     | UART_TX |
| NC  | 4    | 5     | UART_RX |
| 5V  | 6    | 7     | RST     |
| GND | 8    | 9     | NC      |
::

## 尺寸图

[Atomic GPS Base v2.0模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1158/ATOMGPS-V2.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1158/ATOMGPS-V2_page_01.png" width="100%">

## 数据手册

- [ATGM336H-6N](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1158/ATGM336H-6N.pdf)
- [AT2659](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1158/AT2659_cn_datasheet.pdf)
- [TPAP7343D](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1158/LDO_TPAP7343D-33FS4_datasheet.pdf)
- [CASIC 多模卫星导航接收机协议规范](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1173/CASIC_Multi-mode_Satellite_Navigation_Receiver_Protocol_Specification.pdf)

## 软件开发

### 快速上手

- [Atomic GPS Base v2.0 Arduino 快速上手](/zh_CN/arduino/projects/atomic/atomic_gps_base_v2.0)

### Arduino

- [Atomic GPS Base v2.0 Arduino 驱动库](https://github.com/m5stack/TinyGPSPlus/blob/master/examples/UnitGPSExample/UnitGPSExample.ino)

### UiFlow2

- [Atomic GPS Base v2.0 UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/base/gpsv2.html)

## 相关视频

Atomic GPS Base v2.0 产品介绍以及案例展示

<video class="video-container" controls><source src="
https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1158/A134-V2-Atomic-GPS-Base-v2.0_video.mp4" type="video/mp4"></video>

## 产品对比

::compare-table
| 产品对比表     | [Atomic GPS Base v2.0](/zh_CN/atom/Atomic_GPS_Base_v2.0) ![Atomic GPS Base v2.0](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1158/A134-V2-02.webp) | [Atomic GPS Base](/zh_CN/atom/Atomic%20GPS%20Base) ![Atomic GPS Base v2.0](https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic%20GPS%20Base/img-fbbc6c4a-cb73-417b-b855-449d387daf38.webp) |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 定位精度       | <1.5m                                                                                                                                                   | 2m                                                                                                                                                                                                       |
| microSD 卡槽   | 无                                                                                                                                                      | 有                                                                                                                                                                                                       |
| 模组型号       | AT6668                                                                                                                                                  | M8030-KT                                                                                                                                                                                                 |
| 支持的卫星种类 | GPS / QZSS / BD2 / BD3 / GAL / GLO                                                                                                                      | BDS / GPS / GLO / GAL / SBAS / QZSS                                                                                                                                                                      |
::
