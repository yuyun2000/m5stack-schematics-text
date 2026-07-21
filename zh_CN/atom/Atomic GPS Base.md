# Atomic GPS Base

<span class="product-sku">SKU:A134</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic GPS Base/img-3f6d1129-0dde-4b67-adc6-69535a8d1052.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic GPS Base/img-a1e870b7-34ce-45a2-9c94-7efd4af7a0fb.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic GPS Base/img-eacf8f4d-7f0f-4136-accd-6d9f626d7b49.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic GPS Base/img-9d033914-b7d4-4b27-8438-6764dc6fabad.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic GPS Base/img-b632c1a0-7f0b-4f3a-aa89-31f38ba8534e.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic GPS Base/img-b13eec29-9740-4370-8db9-46ffba7c35a5.webp">
</PictureViewer>

## 描述

**Atomic GPS Base** 是一款基于 Atom 系列主机的 GPS 定位模组，定位导航芯片为 M8030-KT，内置 Flash 和纽扣电池，支持断电保存用户配置。采用 NMEA-0183 协议输出，支持 GPS、GLONASS、GALILEO、BDS、SBAS 和 QZSS 多种卫星系统，具备 72 搜索通道数，可用于地理坐标查看、公交车报站、车船导航、轨迹追踪等应用。此外在 GPS 模块下方内置有 microSD 卡槽，您可以读取 GPS 或其他文件数据，例如以特定的格式导出 GPS 数据在地图软件中查看运动轨迹，或作为普通读卡器实现文件读写。

## 产品特性

- 适用于 Atom-Lite / Atom-Matrix / AtomS3 / AtomS3-Lite
- 捕获灵敏度高
- 支持 BDS / GPS / GLONASS / GALILEO / SBAS / QZSS 多种卫星导航系统的单系统定位，或任意组合的多系统联合定位
- 内置自弹式 microSD 卡槽
- 低功耗设计
- UART 参数设置:
  - 波特率 (9600bps)
  - 起始位 (1 bit)
  - 停止位 (1 bit)
  - 校验位 (无)

## 包装内容

- 1 x Atomic GPS Base

## 应用场景

- 车载、船载定位与导航
- 轨迹记录
- 文件读写

## 规格参数

| 规格               | 参数                                                             |
| ------------------ | ---------------------------------------------------------------- |
| 精频率度           | GPS L1, GLONASS L1, BDS B1, GALILEO E1, SBAS L1, QZSS L1         |
| 精度               | 水平：2 米，速度：0.1m/s，时间：1us                              |
| 通道数             | 72 搜索通道                                                      |
| 更新频率           | 1-10Hz                                                           |
| 最大速度           | 515 米 / 秒                                                      |
| 工作最大加速度温度 | < 4g                                                             |
| 灵敏度             | 跟踪：-167dBm，捕捉：-160dBm，冷启动： -148dBm，热启动： -156dBm |
| 启动时间           | 冷启动： 26 seconds，温启动：25 seconds，热启动： 1 second       |
| 波特率             | 9600bps                                                          |
| 输出协议           | NMEA-0183                                                        |
| NMEA 语句          | RMC, VTG, GGA, GSA, GSV, GLL                                     |
| 指示灯             | TX：上电蓝灯闪烁，表示有数据输出，PPS：3D 定位后闪烁，未定位不亮 |
| 工作温度           | 0°C - 40°C                                                       |
| 产品尺寸           | 48.0 x 24.0 x 17.5mm                                             |
| 包装尺寸           | 136 x 92 x 20mm                                                  |
| 产品重量           | 14.4g                                                            |
| 毛重               | 18.1g                                                            |

## 原理图

<img alt="schematics" src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic GPS Base/img-c6106d8c-5518-4355-a565-69c615bef0c8.webp" width="100%" />

## 管脚映射

::m5-bus-table
| PIN | LEFT | RIGHT | PIN      |
| --- | ---- | ----- | -------- |
|     |      | 1     | 3V3      |
|     | 2    | 3     | UART_TX  |
|     | 4    | 5     | SPI_MOSI |
| 5V  | 6    | 7     | SPI_CLK  |
| GND | 8    | 9     | SPI_MISO |
::

## 尺寸图

- [Atomic GPS Base模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/930/A134-atomic-gps.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/930/A134-atomic-gps_page_01.png" width="100%">

## 软件开发

### Arduino

- [Atomic GPS Base Arduino 快速上手](/zh_CN/arduino/projects/atomic/atomic_gps_base)
- [Atomic GPS Base microSD Example - with Atom](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/AtomBase/AtomicGPS)
- [Atomic GPS Base Location Example - with AtomS3](https://github.com/m5stack/M5AtomS3/tree/main/examples/AtomicBase/AtomicGPS/GPS)

### UiFlow1

- [Atomic GPS Base UiFlow1 文档](/zh_CN/uiflow/blockly/atomic_base/gps)

### UiFlow2

- [Atomic GPS Base UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/base/atom_gps.html)

### 通信协议

- [CASIC multi-mode satellite navigation receiver protocol specification](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/950/Multimode_satellite_navigation_receiver_cn.pdf)
- [ATOMGPS method of changing the navigation system](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/atomicgps/AtomGPSKit%E6%9B%B4%E6%94%B9%E5%AF%BC%E8%88%AA%E7%B3%BB%E7%BB%9F%E6%96%B9%E6%B3%95.pdf)

### EasyLoader

| Easyloader                                  | 下载链接                                                                                                                                     | 备注 |
| ------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ---- |
| Atomic GPS Base Location Example Easyloader | [download](https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic%20GPS%20Base/ezLoader-79d326f1-ce68-4d48-8761-c461ea7b3872.exe) | /    |

## 相关视频

- 连接手机无线串口工具查看 GPS 信息

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/AtomBase/AtomGPS.mp4" type="video/mp4"></video>
