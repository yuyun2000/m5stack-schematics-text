# CardputerZero-Lite

?> Work in progress | 本产品包装及软件研发尚未完成，最终功能及资料可能有变，敬请理解。

<span class="product-sku">SKU:C155</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/coming-soon.png">
</PictureViewer>

## 描述

**CardputerZero-Lite** 是一款面向极客与开发者的口袋 **Linux** 个人电脑，基于 **Raspberry Pi CM0** 平台，集成四核 Cortex-A53 处理器、1.9 英寸显示屏、46 键矩阵键盘与 RTC，在掌上体积中提供接近完整开发终端的交互体验。它具备 Wi-Fi、蓝牙、以太网、microSD、可切换 Host/Slave 的 USB 体系，以及 I2C/UART/SPI/GPIO 等模块化扩展能力；配合音视频编解码与电池供电设计，可实现随身开发、边缘采集与多媒体交互的一体化。典型应用场景包括：移动渗透与运维终端、物联网设备调试与现场部署、便携式 AI / 视觉原型验证、创客项目开发，以及户外数据采集与快速人机交互控制。相较于标准版 CardputerZero，Lite 版本在保留核心计算与主要扩展能力的同时，移除了 **8MP 摄像头** 与 **IMU**，更聚焦于终端开发与控制交互场景。

## 产品特性

- Raspberry Pi CM0 核心主控:
  - RP3A0 (BCM2837)
  - CPU：四核 Cortex-A53 @ 1 GHz, ARMv8-A (aarch64)
  - 内存: 512 MB LPDDR2
- 人机交互:
  - 46 键矩阵键盘
  - 1.9" LCD 屏幕 @ ST7789v3, 分辨率 170x320
  - 红外发射 + 接收
- 无线通信:
  - 2.4GHz Wi-Fi 802.11 b/g/n
  - BT 4.2 标准，支持低功耗模式（BLE）
- 丰富接口:
  - 1× 高清数字音视频输出接口，支持 1080P 30fps
  - 1x 10/100M 以太网接口
  - 1x microSD 卡槽
  - 1x HY2.0-4P 拓展接口 (内置电子开关可切换 I2C / UART 接口)
  - Cap EXT 2.54-14P 拓展总线:
    - SPI, UART, I2C, USB, GPIO, 5VIN/OUT
- USB 拓展:
  - 独立 Host / Slave 切换开关:
  - Slave 模式：控制机身右侧 USB Type-C 接口
    - 1x USB Type-C 供电 / USB 2.0 + OTG
  - Host 模式：控制机身左侧 USB 接口
    - 1x USB-A 2.0 接口
    - 1x USB Type-C 2.0 接口
- 音频交互:
  - ES8389 音频编解码
  - MEMS 麦克风 x1
  - AW8737A 扬声器功放 + 1W @ 8Ω 扬声器
  - 3.5 音频输出接口 TRRS
- 视频编解码:
  - Decode: 1080P 30fps in H.264 or MPEG-4
  - Encode: 1080P 30fps in H.264
- 内置 3.7V@ 1500mAh 锂电池
- BQ27220YZFR 电池状态读取
- RTC RX8130CE

## 产品对比

::compare-table
| 产品对比项          | [CardputerZero](dummy) ![CardputerZero](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/coming-soon.png) | [CardputerZero-Lite](dummy) ![CardputerZero-Lite](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/coming-soon.png) |
| ------------------- | -------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| 核心                | Raspberry Pi CM0                                                                                               | Raspberry Pi CM0                                                                                                         |
| Wi-Fi & Bluetooth   | ✅                                                                                                              | ✅                                                                                                                        |
| 红外发射 + 接收     | ✅                                                                                                              | ✅                                                                                                                        |
| 8MP 摄像头          | ✅                                                                                                              | ❌                                                                                                                        |
| IMU BMI270 + BMM150 | ✅                                                                                                              | ❌                                                                                                                        |
| 标配 32GB microSD   | ✅                                                                                                              | ❌                                                                                                                        |
::
