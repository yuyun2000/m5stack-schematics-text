# Module LoRa868 v1.1

<span class="product-sku">SKU:M029-V11</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Module-LoRa868_V1.1/img-b1174978-3e89-4d80-ac30-85f881dd22d6.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Module-LoRa868_V1.1/img-5af343fc-b5bc-43ca-88a8-be60dcb486e2.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Module-LoRa868_V1.1/img-ee5bc5a1-3903-4c09-87de-3c03f16feda4.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Module-LoRa868_V1.1/img-c292de1f-1068-41db-94bb-43cf007eedbb.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Module-LoRa868_V1.1/img-14ddbbb0-72a2-42f4-a452-6ab73e2756fe.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Module-LoRa868_V1.1/img-ed360156-1ad0-4069-8739-3a8ab1b641a2.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Module-LoRa868_V1.1/img-fb5cb25e-182f-4e12-94f3-815b3bae8efc.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Module-LoRa868_V1.1/img-220498ab-e9aa-4411-8e6b-7dfe788b8b3f.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Module-LoRa868_V1.1/img-e7ce60e6-b3b7-4cb9-9dd7-7283cc25af4c.webp">
</PictureViewer>

## 描述

**Module LoRa868 v1.1** 是 M5Stack 堆叠模块系列中的一款 LoRa 通信模块（工作频率为 868MHz），采用 **Ra-01H 模组**（芯片 SX1276）方案。该模块默认搭载 **外置 SMA 天线**，并额外预留了两个贴片 MCX 天线焊盘接口，使用户能够根据需求自由切换不同类型的天线。此外，模块上还预留了 **拨码开关**，以便用户能够灵活切换不同的通讯引脚，**可进行多个堆叠同时使用**，提供更多自定义的可能性和灵活性。适用于远程监控、智能城市、家庭和工业自动化、物联网 （IoT） 设备等领域。

## 产品特性

- 串行通信协议: SPI
- Ra-01H 模组
- 拨码开关切换 IO
- 可多个堆叠使用
- 工作频率: 803~930 MHz
- 支持 FSK,GFSK,MSK,GMSK,LoRa™ 和 OOK 调制模式
- 接收灵敏度：低至 - 140 dBm
- 可编程比特率高达 300Kbps
- 外部天线接口
- 内置拨码开关切换引脚
- 开发平台: Arduino, Micropython, UiFlow (Blockly)

## 包装内容

- 1 x Module LoRa868 v1.1
- 1 x 外置 SMA 天线

## 应用场景

- 远程监控
- 智能城市
- 家庭和工业自动化
- 物联网 (IoT) 设备

## 规格参数

| 规格         | 参数                 |
| ------------ | -------------------- |
| 频谱范围     | 803~930MHz           |
| 通讯接口     | SPI                  |
| 可编程比特率 | 最高可达 300kbps     |
| 天线         | 胶棒天线 @2.5dBi     |
| 待机电流     | DC 5V@1.74mA         |
| 工作电流     | DC 5V@19.98mA        |
| 工作温度     | 0 ~ 40°C             |
| 产品尺寸     | 54.0 x 54.0 x 13.1mm |
| 产品重量     | 22.8g                |
| 包装尺寸     | 95.0 x 66.0 x 26.0mm |
| 毛重         | 41.9g                |

## 原理图

- [Module LoRa868 v1.1 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/545/SCH_Module_LoRa868_V1.1.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/545/SCH_Module_LoRa868_V1.1_sch_01.png">
</SchViewer>

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

<img alt="module size" src="https://static-cdn.m5stack.com/resource/docs/products/module/Module-LoRa868_V1.1/img-c773ae13-4072-4862-a412-5a211b44b05e.jpg" width="100%" />

## 数据手册

- [RA-01H](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Module-LoRa868_V1.1/ra-01h_product_specification_en.pdf)
- [SX127X](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Module-LoRa433_V1.1/sx1278.pdf)

## 软件开发

### Arduino

- [Module LoRa868 v1.1 Arduino 驱动库](https://github.com/m5stack/M5-SX127x/blob/master/examples)
- [Module LoRa868 v1.1 Arduino Demo(LoRaSender)](https://github.com/m5stack/M5-SX127x/blob/master/examples/LoRaSender/LoRaSender.ino)
- [Module LoRa868 v1.1 Arduino Demo(LoRaReceiver)](https://github.com/m5stack/M5-SX127x/tree/master/examples/LoRaReceiver)
- [Module LoRa868 v1.1 Arduino Demo(LoRaSetSpread)](https://github.com/m5stack/M5-SX127x/blob/master/examples/LoRaSetSpread/LoRaSetSpread.ino)
- [Module LoRa868 v1.1 Arduino Demo(LoRaDuplex)](https://github.com/m5stack/M5-SX127x/blob/master/examples/LoRaDuplex/LoRaDuplex.ino)

### UiFlow1

- [Module LoRa868 v1.1 UiFlow1 文档](/zh_CN/uiflow/blockly/module/lora868)

## 相关视频

- Module LoRa868 v1.1 产品介绍以及功能 demo 展示

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Module-LoRa868_V1.1/M029-V11%20LoRa868%20V1.1%20Module%20%E8%A7%86%E9%A2%91.mp4" type="video/mp4"></video>

## 版本变更

| 上市日期   | 产品变动                    | 备注                                                                                                          |
| ---------- | --------------------------- | ------------------------------------------------------------------------------------------------------------- |
| /          | 首次发售 LoRa868 (SKU:M029) | /                                                                                                             |
| 2024.04.19 | LoRa868_V1.1 (SKU:M029_V11) | 相较上个版本添加了拨码开关，可以切换不同的通讯引脚，适合 Basic/Core2/CoreS3 主机，也可以进行多个堆叠使用      |
