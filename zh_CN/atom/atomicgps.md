# Atom GPS

<span class="product-sku">SKU:K043</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomicgps/atomicgps_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomicgps/atomicgps_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomicgps/atomicgps_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomicgps/atomicgps_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomicgps/atomicgps_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomicgps/atomicgps_06.webp">
</PictureViewer>

## 描述

**Atom GPS** 是一款基于 Atomic 的 GPS 定位模组，定位导航芯片为 M8030-KT, 内置 Flash 和纽扣电池，支持断电保存用户配置。采用 NMEA-0183 协议输出，支持 GPS、GLONASS、GALILEO、BDS、SBAS 和 QZSS 多种卫星系统，具备 72 搜索通道数，可用于地理坐标查看、公交车报站、车船导航、轨迹追踪等应用。此外在 GPS 模块下方内置有 TF (microSD) 卡槽，您可以读取 GPS 或其他文件数据，例如以特定的格式导出 GPS 数据在地图软件中查看运动轨迹，或作为普通读卡器实现文件读写。

## 产品特性

- 捕获灵敏度高
- 支持 BDS / GPS / GLONASS / GALILEO / SBAS / QZSS 多种卫星导航系统的单系统定位，或任意组合的多系统联合定位
- 内置自弹式 TF (microSD) 卡槽
- 低功耗设计
- UART 参数设置:
  - 波特率 (**9600bps**)
  - 起始位 (1 bit)
  - 停止位 (1 bit)
  - 校验位 (无)

## 包装内容

- 1 x Atom-Lite
- 1 × Atomic GPS Base
- 1 x M2 内六角扳手
- 1 x M2\*8mm 杯头机械牙螺丝
- 1 x M2\*3mm 杯头自攻螺丝
- 1 x USB Type-C 连接线 (20cm)

## 应用场景

- 车载、船载定位与导航
- 轨迹记录
- 文件读写

## 规格参数

| 规格               | 参数                                                            |
| ------------------ | --------------------------------------------------------------- |
| 精频率度           | GPS L1, GLONASS L1, BDS B1, GALILEO E1, SBAS L1, QZSS L1        |
| 精度               | 水平：2 米，速度：0.1m/s，时间：1us                             |
| 通道数             | 72 搜索通道                                                     |
| 更新频率           | 1-10Hz                                                          |
| 最大速度           | 515 米 / 秒                                                     |
| 工作最大加速度温度 | < 4g                                                            |
| 灵敏度             | 跟踪: -167dBm，捕捉: -160dBm，冷启动: -148dBm，热启动: -156dBm  |
| 启动时间           | 冷启动: 26 seconds，温启动: 25 seconds，热启动: 1 second        |
| 波特率             | 9600bps                                                         |
| 输出协议           | NMEA-0183                                                       |
| NMEA 语句          | RMC, VTG, GGA, GSA, GSV, GLL                                    |
| 指示灯             | TX: 上电蓝灯闪烁，表示有数据输出，PPS:3D 定位后闪烁，未定位不亮 |
| 工作温度           | 0 ~ 40°C                                                        |
| 产品重量           | 28g                                                             |
| 毛重               | 38g                                                             |
| 产品尺寸           | 24 x 48 x 18mm                                                  |
| 包装尺寸           | 54 x 54 x 20mm                                                  |

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomicgps/atomicgps_sch_01.webp" width="80%">

## 管脚映射

::m5-bus-table
| PIN      | LEFT | RIGHT | PIN |
| -------- | ---- | ----- | --- |
| 3V3      |      | 1     |     |
| UART_TX  | 2    | 3     |     |
| SPI_MOSI | 4    | 5     | 5V  |
| SPI_CLK  | 6    | 7     | GND |
| SPI_MISO | 8    | 9     |     |
::

## 数据手册

- [CASIC 多模卫星导航接收机协议规范](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/950/Multimode_satellite_navigation_receiver_cn.pdf)
- [ATOMGPS 更改导航系统的方法](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/atomicgps/AtomGPSKit%E6%9B%B4%E6%94%B9%E5%AF%BC%E8%88%AA%E7%B3%BB%E7%BB%9F%E6%96%B9%E6%B3%95.pdf)

## 软件开发

### Arduino

- [Atom GPS 测试程序](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/AtomBase/AtomicGPS)

### UiFlow1

- [Atom GPS UiFlow1 文档](/zh_CN/uiflow/blockly/atomic_base/gps)

### EasyLoader

| Easyloader          | 下载链接                                                                                                        | 备注 |
| ------------------- | --------------------------------------------------------------------------------------------------------------- | ---- |
| Atom GPS Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/ATOM_BASE/EasyLoader_Atomic_GPS.exe) | /    |

## 相关视频

<video id="example_video" controls>
  <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/AtomBase/AtomGPS.mp4" type="video/mp4">
</video>
