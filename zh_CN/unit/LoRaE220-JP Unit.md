# Unit LoRaE220-920

<span class="product-sku">SKU:U170</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/LoRaE220-JP Unit/img-09091755-bb45-4d76-9800-2203cb8142ca.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/LoRaE220-JP Unit/img-6282c168-fa3a-433a-b90c-35f004c175bf.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/846/U170-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/LoRaE220-JP Unit/img-3f99fc53-4ed1-4fc7-a7ac-4554fc63c5cf.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/LoRaE220-JP Unit/img-dfeaa83e-4eb7-481e-bf3c-c575ec21bb11.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/LoRaE220-JP Unit/img-40f48a2f-39b7-42d6-a2f2-72ed0d1c02ba.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/LoRaE220-JP Unit/img-9f255b22-ef28-4625-b28d-00acdb82477b.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/LoRaE220-JP Unit/img-39769a82-00eb-4625-9412-deecad1c9fd5.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/LoRaE220-JP Unit/img-4f07b9cc-a8d8-41a6-a97d-b00e64eda51a.webp">
</PictureViewer>

## 描述

**Unit LoRaE220-920** 是 M5Stack 推出的适用于 920MHz 频段的 LoRa 通讯单元，采用便捷的 串口 通信方式。以点对点发射和广播模式支持 无线唤醒 、载波监控和通信密钥等功能，通过 板载拨码 开关切换四种不同的工作模式，实现数据的发送和接收功能配置，满足各种通信需求。适用于家庭安防报警、楼宇自动化、智能家居以及汽车行业等。

## 产品特性

- 通信功能丰富：支持 Wake on Radio (无线唤醒) 、载波监听、通信密钥等功能。
- 板载拨码开关：通过拨动开关配置工作模式，实现数据的发送和接收功能配置。
- 通信频段：支持 920MHz 频段 (920.6〜928.0MHz)。
- 高性能：采用新一代 LoRa 方案，具有更长的传输距离、更快的速度和更低的功耗。
- 串口通信：支持串口通信方式，为物联网应用提供高度的灵活性和可靠性。

## 包装内容

- 1 x Unit LoRaE220-920
- 1 x HY2.0-4P Grove 连接线 (20cm)
- 1 x 胶棒天线 (@2.5dBi 总长 110mm SMA 内针)

## 应用场景

- 智能城市、农业、工业自动化
- 家庭安防
- 智能家居和汽车行业

## 规格参数

| 规格         | 参数                                   |
| ------------ | -------------------------------------- |
| Lora 模块    | E220-900T22S (JP) @ Telec (001-P01730) |
| 模组芯片     | LLCC68                                 |
| 支持频段     | 920MHz (920.6〜928.0MHz)               |
| 最大发射功率 | 13dBm (约 20mW)                        |
| 通讯距离     | 通信距离可达 5 公里                    |
| 供电电压     | 5V                                     |
| 通讯方式     | 串口通信                               |
| 产品尺寸     | 71.4 x 24.0 x 8.0mm                    |
| 产品重量     | 19.2g                                  |
| 包装尺寸     | 138.0 x 93.0 x 9.0mm                   |
| 毛重         | 25.0g                                  |

## 操作说明

LoRaE220-JP 工作模式

| 工作模式 (0-3)      | M0，M1         | 模式说明                                               |
| ------------------- | -------------- | ------------------------------------------------------ |
| 0: 发送接收传输模式 | M0:OFF，M1:OFF | 正常数据包收发模式                                     |
| 1:WOR 发送模式      | M0:ON，M1:OFF  | 发送 WOR 数据包，该模式同时支持数据接收                |
| 2:WOR 接收模式      | M0:OFF，M1:ON  | 关闭数据发送，该模式仅支持 WOR 数据包接收              |
| 3: 参数配置模式     | M0:ON，M1:ON   | 切换至配置模式，用于配置模组发射功率，信道，地址等信息 |

<img alt="schematics" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/LoRaE220-JP%20Unit/3.jpg" width="100%" />

\#> 上表中所说的 "ON" 代表数据手册中指的 "0";"OFF" 代表数据手册中指的 "1".

## 原理图

- [Unit LoRaE220-920 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/623/SCH_UNIT_LoraE220.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/623/SCH_UNIT_LoraE220_sch_01.png">
</SchViewer>

## 管脚映射

### Unit LoRaE220-920

::grove-table
| HY2.0-4P | Black | Red | Yellow  | White   |
| -------- | ----- | --- | ------- | ------- |
| PORT.C   | GND   | 5V  | UART_RX | UART_TX |
::

## 尺寸图

<img alt="module size" src="https://static-cdn.m5stack.com/resource/docs/products/unit/LoRaE220-JP Unit/img-14d3d8e7-2987-4184-a5be-6cb1d492082d.jpg" width="100%" />

## 数据手册

- [LoRaE220 Datasheet](<https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/LoRaE220-JP%20Unit/data_sheet_E220--900T22S(JP)Rev1.4.pdf>)

## 软件开发

### Arduino

- [Unit LoRaE220-920 Arduino 驱动库](https://github.com/m5stack/M5-LoRa-E220-JP)

## UiFlow2

- [Unit LoRaE220-920 UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/lora_e220.html)

## 相关视频

- Unit LoRaE220-JP 案例以及介绍

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/LoRaE220-JP%20Unit/LoRa%20E220%20JP.mp4" type="video/mp4"></video>
