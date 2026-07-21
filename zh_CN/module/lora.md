# Module LoRa433

<span class="product-sku">SKU:M005</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/lora/lora_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/lora/lora_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/lora/lora_03.webp">
</PictureViewer>

learn>| ![TTN(The Things Network)](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/lora/lorawan/ttn_01.jpg) | [TTN(The Things Network)](/zh_CN/guide/lora/lora433/lorawan470_ttn) | 本教程将介绍如何通过 [Basic](/zh_CN/core/basic) 主机和 [Module LoRa433)](/zh_CN/module/lora) 实现 LoRaWAN470 网关和节点，并与 [TTN](https://www.thethingsnetwork.org) 进行通信 |

## 描述

**Module LoRa433** 是 M5Stack 堆叠模块系列中的一款 LoRa 通信模块（工作频率为 433MHz ）。模块上保留了一定的拓展空间，以便你进行更多的功能设计。无论是进行基本的无线通信或是有着更多定制化元素的项目，Module LoRa433 都会是合适的选择。

## 产品特性

- Module LoRa433 模块: Ra-02
- 串行通信协议: SPI
- 工作频率: 433 MHz
- 支持 FSK,GFSK,MSK,GMSK,LoRa™和 OOK 调制模式
- 接收灵敏度：低至 - 140 dBm
- 可编程比特率高达 300Kbps
- 内置 PCB 天线
- 外部天线接口
- 开发平台: Arduino, Micropython, UiFlow (Blockly)

## 包装内容

- 1 x Module LoRa433

## 应用场景

- 自动抄表系统
- 楼宇自动化
- 远程灌溉系统

## 规格参数

| 规格     | 参数                 |
| -------- | -------------------- |
| 产品重量 | 13g                  |
| 毛重     | 24g                  |
| 产品尺寸 | 54.2 x 54.2 x 12.8mm |
| 包装尺寸 | 60 x 57 x 17mm       |

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/module/lora/lora_sch_01.webp" width="80%">

## 管脚映射

### M5-Bus

::m5-bus-table
| PIN      | LEFT | RIGHT | PIN      |
| -------- | ---- | ----- | -------- |
| GND      | 1    | 2     |          |
| GND      | 3    | 4     | IRQ      |
| GND      | 5    | 6     |          |
| SPI_MOSI | 7    | 8     | RST      |
| SPI_MISO | 9    | 10    |          |
| SPI_CLK  | 11   | 12    |          |
|          | 13   | 14    |          |
|          | 15   | 16    |          |
|          | 17   | 18    |          |
|          | 19   | 20    | CS       |
|          | 21   | 22    |          |
|          | 23   | 24    |          |
|          | 25   | 26    |          |
|          | 27   | 28    | 5V       |
|          | 29   | 30    |          |
::

## 数据手册

- [Ra-02_CH](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Module-LoRa433_V1.1/sx1278.pdf)
- [Ra-02_EN](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Module-LoRa433_V1.1/c048ps01a1_ra-02_product_specification_v1.1.pdf)
- [SX127X](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Module-LoRa433_V1.1/sx1278.pdf)

## 软件开发

### Arduino

- [Module LoRa433 Arduino 驱动库](https://github.com/m5stack/M5-SX127x/blob/master/examples)
- [Module LoRa433 LoRaSender Example](https://github.com/m5stack/M5-SX127x/blob/master/examples/LoRaSender/LoRaSender.ino)
- [Module LoRa433 LoRaReceiver Example](https://github.com/m5stack/M5-SX127x/tree/master/examples/LoRaReceiver)
- [Module LoRa433 LoRaSetSpread Example](https://github.com/m5stack/M5-SX127x/blob/master/examples/LoRaSetSpread/LoRaSetSpread.ino)
- [Module LoRa433 LoRaDuplex Example](https://github.com/m5stack/M5-SX127x/blob/master/examples/LoRaDuplex/LoRaDuplex.ino)

### UiFlow1

- [Module LoRa433 UiFlow1 文档](/zh_CN/uiflow/blockly/module/lora433)

### Easyloader

| Easyloader                                               | 下载链接                                                                                              | 备注 |
| -------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ---- |
| Module LoRa433 LoRaDuplex Example Easyloader with M5Core | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Module/EasyLoader_LORA_Duplex.exe) | /    |
