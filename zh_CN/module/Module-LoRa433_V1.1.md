# Module LoRa433 v1.1

<span class="product-sku">SKU:M005-V11</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Module-LoRa433_V1.1/img-dac09b0a-7367-4ed9-9374-b604f646ec3b.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Module-LoRa433_V1.1/img-874ae828-f842-4a8d-8892-70ca5648398d.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Module-LoRa433_V1.1/img-17d64524-16d8-4999-ba74-34a0af7e92f8.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Module-LoRa433_V1.1/img-df7edfb7-0825-4dac-b4f7-e891bd1fb2cd.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Module-LoRa433_V1.1/img-6d4a69c2-0eaf-4938-bc8e-9dacddef0686.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Module-LoRa433_V1.1/img-e511537d-4657-4816-a8ee-d84385c4fe48.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Module-LoRa433_V1.1/img-d64e3825-3d1c-4c43-9888-b93854d75662.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Module-LoRa433_V1.1/img-566f39c2-4eb1-4bd3-91d0-2139978b2918.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Module-LoRa433_V1.1/img-976688b9-0be6-4911-bc9e-f06457fcf5c8.webp">
</PictureViewer>

## 描述

**Module LoRa433 v1.1** 是 M5Stack 堆叠模块系列中的一款 LoRa 通信模块 （工作频率为 433MHz） ，采用 **Ra-02 模组** （芯片 SX1278） 方案。该模块默认搭载 **外置 SMA 天线**，并额外预留了两个贴片 MCX 焊盘接口，使用户能够根据需求自由切换不同类型的天线。此外，模块上还预留了 **拨码开关**，以便用户能够灵活切换不同的通讯引脚，**可进行多个堆叠同时使用**，提供更多自定义的可能性和灵活性。适用于远程监控、智能城市、家庭和工业自动化、物联网 （IoT） 设备等领域。

## 产品特性

- 串行通信协议: SPI
- 工作频率: 410MHz~525MHz
- 支持 FSK,GFSK,MSK,GMSK,LoRa™ 和 OOK 调制模式
- 接收灵敏度：低至 - 140 dBm
- 可编程比特率高达 300Kbps
- 外部天线接口
- 内置拨码开关切换引脚
- 开发平台: Arduino, Micropython, UiFlow (Blockly)

## 包装内容

- 1 x Module LoRa433 v1.1
- 1 x 外置 SMA 天线

## 应用场景

- 远程监控
- 智能城市
- 家庭和工业自动化
- 物联网 (IoT) 设备

## 规格参数

| 规格         | 参数                                 |
| ------------ | ------------------------------------ |
| 频谱范围     | 410MHz~525MHz                        |
| 通讯接口     | SPI                                  |
| 可编程比特率 | 最高可达 300kbps                     |
| 天线         | 胶棒天线 @2.5dBi 总长 110mm SMA 内针 |
| 工作温度     | 0-40°C                               |
| 产品尺寸     | 54.0 x 54.0 x 13.1mm                 |
| 产品重量     | 23.1g                                |
| 包装尺寸     | 95.0 x 66.0 x 26.0mm                 |
| 毛重         | 42.7g                                |

## 操作说明

### 拨码操作

Module LoRa433 v1.1 与不同的 Core 搭配使用时，需要根据下图的说明切换对应管脚的拨码开关，否则无法正常使用。

<img alt="operate" width="100%" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Module-LoRa433_V1.1/switch pin_cn.png">

## 原理图

<img alt="schematics" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Module-LoRa433_V1.1/%E5%8E%9F%E7%90%86%E5%9B%BE1.png" width="100%" />

## 管脚映射

### M5-Bus

\#> DIP Switch | 下方 M5-Bus 中标记 `SW` 的引脚，可通过拨码开关进行切换，用于适配不同的主控设备。

::m5-bus-table
| PIN     | LEFT | RIGHT | PIN      |
| ------- | ---- | ----- | -------- |
| GND     | 1    | 2     | IRQ (SW) |
| GND     | 3    | 4     |          |
| GND     | 5    | 6     |          |
| MOSI    | 7    | 8     | RST (SW) |
| MISO    | 9    | 10    |          |
| SCK     | 11   | 12    |          |
|         | 13   | 14    |          |
|         | 15   | 16    |          |
|         | 17   | 18    |          |
|         | 19   | 20    | CS (SW)  |
| CS (SW) | 21   | 22    | RST (SW) |
| CS (SW) | 23   | 24    | CS (SW)  |
|         | 25   | 26    | IRQ (SW) |
|         | 27   | 28    | 5V       |
|         | 29   | 30    |          |
::

## 尺寸图

<img alt="module size" src="https://static-cdn.m5stack.com/resource/docs/products/module/Module-LoRa433_V1.1/img-cba38900-1914-4903-81e4-b5e49268d3f8.jpg" width="100%" />

## 数据手册

- [Ra-02_CH](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Module-LoRa433_V1.1/sx1278.pdf)
- [Ra-02_EN](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Module-LoRa433_V1.1/c048ps01a1_ra-02_product_specification_v1.1.pdf)
- [SX127X](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Module-LoRa433_V1.1/sx1278.pdf)

## 软件开发

### Arduino

- [Module LoRa433 v1.1 Arduino 驱动库](https://github.com/m5stack/M5-SX127x/blob/master/examples)
- [Module LoRa433 v1.1 Arduino Demo(LoRaSender)](https://github.com/m5stack/M5-SX127x/blob/master/examples/LoRaSender/LoRaSender.ino)
- [Module LoRa433 v1.1 Arduino Demo(LoRaReceiver)](https://github.com/m5stack/M5-SX127x/tree/master/examples/LoRaReceiver)
- [Module LoRa433 v1.1 Arduino Demo(LoRaSetSpread)](https://github.com/m5stack/M5-SX127x/blob/master/examples/LoRaSetSpread/LoRaSetSpread.ino)
- [Module LoRa433 v1.1 Arduino Demo(LoRaDuplex)](https://github.com/m5stack/M5-SX127x/blob/master/examples/LoRaDuplex/LoRaDuplex.ino)

### UiFlow1

- [Module LoRa433 v1.1 UiFlow1 文档](/zh_CN/uiflow/blockly/module/lora433)

## 版本变更

| 上市日期   | 产品变动                    | 备注                                                                                                          |
| ---------- | --------------------------- | ------------------------------------------------------------------------------------------------------------- |
| 2024.05.17 | LoRa868_V1.1 (SKU:M005_V11) | 相较上个版本添加了拨码开关，可以切换不同的通讯引脚，适合 Basic/Core2/CoreS3 主机，也可以进行多个堆叠使用      |
| /          | 首次发售 LoRa433 (SKU:M005) | /                                                                                                             |