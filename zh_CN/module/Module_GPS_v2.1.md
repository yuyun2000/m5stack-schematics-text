# Module GPS v2.1

<span class="product-sku">SKU:M003-V21</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1173/Module_GPS_v2.1_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1173/Module_GPS_v2.1_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1173/Module_GPS_v2.1_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1173/Module_GPS_v2.1_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1173/Module_GPS_v2.1_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1173/Module_GPS_v2.1_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1173/Module_GPS_v2.1_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1173/Module_GPS_v2.1_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1173/Module_GPS_v2.1_09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1173/Module_GPS_v2.1_10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1173/Module_GPS_v2.1_11.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1173/Module_GPS_v2.1_13.webp.jpg">
</PictureViewer>

## 描述

**Module GPS v2.1** 是一款高性能的 GNSS 全球定位模块，集成高性能 AT6668 芯片，提供精确和可靠的卫星定位服务。该模块支持多频多模 GNSS 信号接收，兼容多个卫星导航系统，包括 GPS、BD2、BD3、GLONASS、GALILEO 和 QZSS 等，能够实现高精度、多系统联合定位或单系统独立定位，并具备优秀的抗干扰能力。在信号较弱的区域，能够快速获取更高精度的位置信息。
该模块默认搭载外置 **SMA 天线**，此外，模块上还预留了**拨码开关**，用户可以灵活切换 TX/RX 通讯引脚，并通过 PPS 信号输出实现精准时间同步，适用于车载定位与导航、物联网定位设备、远程监控、智能城市、家庭和工业自动化等高精度定位应用场景。相比之前的 Module GPS v2.0，本产品对接口进行了兼容优化，可以适配 CoreMP135，UART 引脚选择由四选一变为五选一。

## 产品特性

- 支持多种卫星导航系统 (GPS/QZSS/BD2/BD3/GAL/GLO)
- 多频点多系统接收
- 多通道
- 低功耗
- 精确时序支持
- 模块堆叠支持
- 开发平台
  - UiFlow1
  - UiFlow2
  - Arduino IDE

## 包装内容

- 1 x Module GPS v2.1
- 1 x 外置有源 GPS/BD 天线 (长度: 1m)

## 应用场景

- 车载定位与导航
- 物联网定位设备 (IoT)
- 工业自动化与机器人定位
- 高精度测绘与地理信息系统

## 规格参数

| 规格             | 参数                                                                 |
| ---------------- | -------------------------------------------------------------------- |
| SoC              | AT6668                                                               |
| 支持卫星导航系统 | GPS/QZSS/BD2/BD3/GAL/GLO                                             |
| 频点             | BDS：B1I+B1C <br/>GPS/QZSS/SBAS：L1 <br>GALILEO：E1 <br/>GLONASS：R1 |
| 通道             | 50 通道                                                              |
| 定位精度         | <1.5m (CEP50)                                                        |
| 定位更新率       | 最大 10Hz                                                            |
| 协议             | NMEA0183 4.1                                                         |
| 通信方式         | UART 115200bps @ 8N1                                                 |
| 灵敏度           | 跟踪: -162dBm<br>捕捉: -160dBm<br>冷启动: -148dBm<br>热启动：-156dBm |
| 启动时间         | 冷启动：23s<br>热启动：1s                                            |
| 功耗             | 待机电流：DC 5V/29.43uA <br>工作电流：DC 5V/28.35mA                  |
| 天线频率         | 1555MHz ~ 1580MHz                                                    |
| 超级电容         | 20000uF DC 3.3V                                                      |
| 产品尺寸         | 54.0 x 63.6 x 13.1mm                                                 |
| 产品重量         | 16.0g                                                                |
| 包装尺寸         | 123.0 x 65.0 x 22.0mm                                                |
| 毛重             | 78.3g                                                                |

## 原理图

- [Module GPS v2.1 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1173/SCH_Module_GPS_v2.1_2025_06_18_16_45_23.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1173/SCH_Module_GPS_v2.1_2025_06_18_16_45_23_page_01.png" width="100%">

## 管脚映射

?> 拨码开关引脚注意事项 | 由于 ESP32 的 G12 引脚为 Strapping，因此当搭配 Basic 主机使用时，请勿将 G12 对应的拨码开关拨至 ON 端，否则会导致设备无法正常开机。同时，由于 G25 引脚和扬声器引脚复用，因此只能二选一使用。<br/>搭配`Core2`使用时，`G2`引脚和扬声器引脚复用，只能二选一使用。

### M5-Bus

\#> Switch | 下方 M5-Bus 中标记 `SW` 的引脚，可通过拨码开关进行切换，用于适配不同的主控设备。

::m5-bus-table
| PIN         | LEFT | RIGHT | PIN              |
| ----------- | ---- | ----- | ---------------- |
| GND         | 1    | 2     | GNSS_TX/PPS (SW) |
| GND         | 3    | 4     | PPS(SW)          |
| GND         | 5    | 6     |                  |
|             | 7    | 8     | PPS(SW)          |
|             | 9    | 10    |                  |
|             | 11   | 12    |                  |
| GNSS_TX(SW) | 13   | 14    | GNSS_RX(SW)      |
| GNSS_TX(SW) | 15   | 16    | GNSS_RX(SW)      |
|             | 17   | 18    |                  |
|             | 19   | 20    |                  |
| GNSS_RX(SW) | 21   | 22    | GNSS_TX(SW)      |
| GNSS_RX(SW) | 23   | 24    | GNSS_RX(SW)      |
| HPWR        | 25   | 26    | GNSS_TX(SW)      |
| HPWR        | 27   | 28    | 5V               |
| HPWR        | 29   | 30    | BAT              |
::

## 尺寸图

- [Module GPS v2.1 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1173/M003-V21-drw0004.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1173/M003-V21-drw0004_page_01.png" width="100%">

## 数据手册

- [ATGM336H-6N](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-GPS%20v1.1/ATGM336H-6N.pdf)
- [VRH3301NLX](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/950/LDO_VRH3301NLX_datasheet.pdf)
- [CASIC 多模卫星导航接收机协议规范](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1173/CASIC_Multi-mode_Satellite_Navigation_Receiver_Protocol_Specification.pdf)

## 软件开发

### 快速上手

- [Module GPS v2.1 Arduino 使用教程](/zh_CN/arduino/projects/module/module_gps_v2.0)

### Arduino

- [Module GPS v2.1 Arduino 驱动库](https://github.com/m5stack/TinyGPSPlus)

## 相关视频

- Module GPS v2.1 产品介绍

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1173/M003-V21_GPS_Module_V2.1_video.mp4" type="video/mp4"></video>

## 产品对比

::compare-table
| 产品对比表       | [Module GPS v2.1](/zh_CN/module/Module_GPS_v2.1) ![Module GPS v2.1](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1173/Module_GPS_v2.1_06.webp) | [Module GPS v2.0](/zh_CN/module/Module%20GPS%20v2.0) ![Module GPS v2.0](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Module%20GPS%20v2.0/9.webp) | [Module GPS](/zh_CN/module/gps) ![Module GPS](https://static-cdn.m5stack.com/resource/docs/products/module/gps/gps_03.webp) |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------- |
| GPS 模组         | AT6668                                                                                                                                             | AT6668                                                                                                                                                                         | NEO-M8N                                                                                                                     |
| 支持卫星         | BD2/BD3/GPS/GLO/GAL/QZSS                                                                                                                           | BD2/BD3/GPS/GLO/GAL/QZSS                                                                                                                                                       | GPS/GLO/GAL/BeiDou                                                                                                          |
| 定位精度         | <1.5m (CEP50)                                                                                                                                      | 1.5m                                                                                                                                                                           | 2.5m                                                                                                                        |
| 灵敏度           | 跟踪: -162dBm<br>捕捉: -160dBm<br>冷启动: -148dBm<br>热启动：-156dBm                                                                               | 跟踪: -162dBm<br>捕捉: -160dBm<br>冷启动: -148dBm                                                                                                                              | 跟踪: -167dBm<br>捕捉: -160dBm<br>冷启动: -148dBm                                                                           |
| 拨码开关切换引脚 | 四组串口控制引脚供选择，兼容 CoreMP135，兼容性更强                                                                                                 | 四组串口控制引脚供选择，不兼容 CoreMP135                                                                                                                                       | 固定引脚，不包含拨码开关切换                                                                                                |

::
