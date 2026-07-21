# Module COMX GPS

<span class="product-sku">SKU:M031-G</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_gps/comx_gps_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_gps/comx_gps_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_gps/comx_gps_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_gps/comx_gps_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_gps/comx_gps_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_gps/comx_gps_06.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_gps/comx_gps_07.webp">
</PictureViewer>

## 描述

**Module COMX GPS** 是 M5Stack 堆叠模块系列中的一款卫星定位模块。基于 NEO-M8N 模组开发，配备有源天线。NEO-M8N 具备 -167dBm 高接收灵敏度，并且保持系统低功耗。NEO-M8N 集成了 72 通道的 [u-blox](https://www.u-blox.com) M8 GNSS 引擎，支持多个 GNSS 系统 (北斗、Galileo、GLONASS、GPS / QZSS) ，允许同时接收 3 个 GNSS 系统的数据。模组内部集成了可编程 FLASH ，可对固件进行升级。该模块具有较小的静态漂移，低功耗和紧凑的尺寸非常适合于车辆，PDA 等手持设备，车辆监控，移动电话，相机和其他移动定位系统中的应用。M5Core 与 Module COMX GPS 模块之间使用 UART 通信协议，通过模块内的拨码开关可设置 UART 通讯引脚。

## 注意事项

?> 兼容性 | 搭配 Fire 主控使用时候，由于 PSRAM 引脚（G16/G17）冲突，使用时候请将模块底座拨码开关引脚切换至 TX (G0/G13),RX (G5/G15)。

## 产品特性

- 天线类型：外置有源天线
- 外部天线端口：SMA
- 可以同时从 3 个 GNSS 系统接收数据
- 水平位置精度：最小 2.5m
- GPS 模组 (NEO-M8N) 内置闪存，通过[u-center-just-for-Windows](https://www.u-blox.com/en/product/u-center-windows)升级固件
- 支持协议: NMEA, UBX, RTCM
- 行业领先的 -167dBm 灵敏度
- 与 NEO‑7 和 NEO‑6 系列向后兼容
- UART 通信接口:
  - 默认波特率：9600bps
  - 数据位：8 位
  - 起始位：1 位
  - 停止位：1 位
  - 校验位：无

## 包装内容

- 1 x Module COMX GPS
- 1 x 外置天线 (长度: 1 m)

## 应用场景

- 基于 GPS 的物流跟踪管理
- 无人驾驶汽车定位

## 规格参数

| 规格        | 参数                                                                  |
| ----------- | --------------------------------------------------------------------- |
| 接收类型    | GPS:L1C/A SBAS:L1C/A QZSS:L1C/A GLONASS:L1OF BediDou:B1 Galileo:E1B/C |
| 定位时间    | Cold start:26S Hot start:1.5S                                         |
| 灵敏度      | -167 dBm                                                              |
| 刷新率      | Separate GNSS 10Hz，Parallel GNSS 5Hz                                 |
| 速率精度    | 0.05m/s                                                               |
| 最大速度    | 500m/s                                                                |
| 工作温度    | -40 ~ 80°C                                                            |
| DC 接口规格 | 5.5mm                                                                 |
| 产品重量    | 28g                                                                   |
| 毛重        | 99g                                                                   |
| 产品尺寸    | 54 x 54 x 13mm                                                        |
| 包装尺寸    | 165 x 60 x 36mm                                                       |

## 操作说明

\#> 信号质量 | 为了使 GPS 模块获得良好信号，请在使用时将模块放置在室外。

\#> 供电切换 | 模块底座带有 DC 电源输入接口，使用该接口接入电源请严格按照输入范围 (5-12V) 防止模块损坏。内部电源拨码开关可调节内部的端子 VIN 的电压水平，用于适配不同模块。

<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_lte/comx_lte_dc_power.webp" width="70%">

如果你想要更改串口波特率，请点击 ( [u-center-just-for-Windows](https://www.u-blox.com/en/product/u-center-windows) ) 查看。

## 原理图

### Module COMX 模块插接底板原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_gps/comx_gps_sch_01.webp" width="80%">

## 管脚映射

### M5-Bus

\#> Switch | 下方 M5-Bus 中标记 `SW` 的引脚，可通过拨码开关进行切换，用于适配不同的主控设备。

::m5-bus-table
| PIN       | LEFT | RIGHT | PIN       |
| --------- | ---- | ----- | --------- |
| GND       | 1    | 2     |           |
| GND       | 3    | 4     |           |
| GND       | 5    | 6     |           |
|           | 7    | 8     |           |
|           | 9    | 10    |           |
|           | 11   | 12    | 3V3       |
|           | 13   | 14    |           |
| TXD (SW)  | 15   | 16    | RXD (SW)  |
|           | 17   | 18    |           |
|           | 19   | 20    | TXD (SW)  |
|           | 21   | 22    | RXD (SW)  |
| TXD (SW)  | 23   | 24    | RXD (SW)  |
|           | 25   | 26    |           |
|           | 27   | 28    | 5V        |
|           | 29   | 30    |           |
::

## 尺寸图

- [Module COMX GPS 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/935/MODLUE-COMX.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/935/MODLUE-COMX_page_01.png" width="100%">

## 数据手册

- [NEO-M8N](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/NEO-M8-FW3_DataSheet_en.pdf)

- [GPS Info](https://www.u-blox.com/zh/product/neo-m8-series) (GPS)

- [TinyGPS++ Library](http://arduiniana.org/libraries/tinygpsplus/)

- [U-Blox Protocol Manual](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/u-blox8-M8_ReceiverDescrProtSpec_en.pdf)

- [u-blox Protocol Manual](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/u-blox8-M8_ReceiverDescrProtSpec_en.pdf)

## 软件开发

### Arduino

- [Module COMX GPS Example with M5Core](https://github.com/m5stack/M5Stack/tree/master/examples/Modules/GPS_NEO_M8N)

### 通信协议

- [u-blox 8 / u-blox M8 Receiver Description - Manual](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/954/spx-15106.pdf)

### Easyloader

| Easyloader                                     | 下载链接                                                                                                  | 备注 |
| ---------------------------------------------- | --------------------------------------------------------------------------------------------------------- | ---- |
| Module COMX GPS Example Easyloader with M5Core | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/MODULE/EasyLoader_COM_GPS.exe) | /    |

### 相关视频

<video id="example_video" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Module/COM.GPS.mp4" type="video/mp4"></video>
