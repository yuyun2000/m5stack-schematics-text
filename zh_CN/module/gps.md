# Module GPS

<span class="product-sku">SKU:M003</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/gps/gps_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/gps/gps_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/gps/gps_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/gps/gps_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/gps/gps_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/gps/gps_06.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/gps/gps_07.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/gps/gps_08.webp">
</PictureViewer>

## 描述

**Module GPS** 是 M5Stack 堆叠模块系列中的一款，卫星定位模块。基于 NEO-M8N 模组开发，配备有源天线。NEO-M8 能够做到花费少量的时间，进行高灵敏度采集，并且保持系统低功耗。 NEO-M8N 集成了 72 通道的 [u-blox](https://www.u-blox.com) M8 GNSS 引擎，支持多个 GNSS 系统：北斗，Galileo，GLONASS，GPS/QZSS，允许同时接收 3 个 GNSS 系统的数据。

## 产品特性

- 工作温度:-40 ~ 80°C
- 天线类型：内置陶瓷天线和外置天线
- 外部天线端口：SMA
- 可以同时从 3 个 GNSS 系统接收数据
- 水平位置精度：最小 2.5m
- GPS 模组 (NEO-M8N) 内置闪存，通过[u-center-just-for-Windows](https://www.u-blox.com/en/product/u-center-windows)升级固件
- 支持协议: NMEA, UBX, RTCM
- 行业领先的 -167dBm 灵敏度
- 与 NEO‑7 和 NEO‑6 系列向后兼容
- UART 通信接口:
  - 波特率 (默认为 9600bps)
  - 数据位 (8 位)
  - 起始位 (1 位)
  - 停止位 (1 位)
  - 校验位 (无)

## 包装内容

- 1 x Module GPS
- 1 x 外置天线 (长度: 1 m)

## 应用场景

- 基于 GPS 的物流跟踪管理
- 无人驾驶汽车定位

## 规格参数

| 规格     | 参数            |
| -------- | --------------- |
| 产品重量 | 43g             |
| 毛重     | 73g             |
| 产品尺寸 | 54 x 54 x 13mm  |
| 包装尺寸 | 125 x 68 x 23mm |

## 操作说明

\#> 信号质量 | 为了使 GPS 模块获得良好信号，请在使用时将模块放置在室外。

\#> 引脚切换 | 主控 Fire 的引脚 G16 / G17 默认与 PSRAM 连接，这使得 GPS 模块的 TXD / RXD (G16,G17) 与其产生冲突。因此，当你使用 Fire 去驱动 GPS 模块时，你需要将 Module GPS 的 TXD 与 RXD 切断，然后通过飞线引至另一组 UART 引脚.

<img src="https://static-cdn.m5stack.com/resource/docs/products/module/gps/gps_note_01.webp" width="100%">

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/module/gps/gps_sch_01.webp" width="80%">

## 管脚映射

### M5-Bus

::m5-bus-table
| PIN      | LEFT | RIGHT | PIN      |
| -------- | ---- | ----- | -------- |
| GND      | 1    | 2     |          |
| GND      | 3    | 4     |          |
| GND      | 5    | 6     |          |
|          | 7    | 8     |          |
|          | 9    | 10    |          |
|          | 11   | 12    | 3V3      |
|          | 13   | 14    |          |
| NEO_TXD  | 15   | 16    | NEO_RXD  |
|          | 17   | 18    |          |
|          | 19   | 20    |          |
|          | 21   | 22    |          |
|          | 23   | 24    |          |
|          | 25   | 26    |          |
|          | 27   | 28    | 5V       |
|          | 29   | 30    |          |
::

## 数据手册

- [GPS Info](https://www.u-blox.com/zh/product/neo-m8-series)
- [NEO-M8N](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/NEO-M8-FW3_DataSheet_en.pdf)
- [u-blox Protocol Manual](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/u-blox8-M8_ReceiverDescrProtSpec_en.pdf)
- [更改导航系统的方法](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/gps/ModuleGPS%E6%9B%B4%E6%94%B9%E5%AF%BC%E8%88%AA%E7%B3%BB%E7%BB%9F%E6%96%B9%E6%B3%95.pdf)

## 软件开发

### Arduino

- [Module GPS Example with M5Core](https://github.com/m5stack/M5Stack/tree/master/examples/Modules/GPS_NEO_M8N)

<img src="https://static-cdn.m5stack.com/resource/docs/products/module/gps/gps_09.webp">

- [TinyGPS++ Arduino 驱动库](http://arduiniana.org/libraries/tinygpsplus/)

### UiFlow1

- [Module GPS UiFlow1 文档](/zh_CN/uiflow/blockly/module/gps)

### UiFlow2

- [Module GPS UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/module/gps.html)

### 通信协议

- [u-blox 8 / u-blox M8 Receiver Description - Manual](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/954/spx-15106.pdf)

### Easyloader

| Easyloader                                | 下载链接                                                                                          | 备注 |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------- | ---- |
| Module GPS Example Easyloader with M5Core | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Module/EasyLoader_GPS_Raw.exe) | /    |
