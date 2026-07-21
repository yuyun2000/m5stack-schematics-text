# Module LoRa868

<span class="product-sku">SKU:M029</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/lora868/lora868_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/lora868/lora868_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/948/M029-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/lora868/lora868_05.webp">
</PictureViewer>

## 描述

**Module LoRa868** 是 M5Stack 堆叠模块系列中的一款 LoRa 通信模块 （工作频率为 868MHz） 。模块上保留了一定的拓展空间，以便你进行更多的功能设计。无论是进行基本的无线通信或是有着更多定制化元素的项目，Module LoRa868 都会是合适的选择。

## 产品特性

- LoRa 模块: Ra-01H
- 串行通信协议: SPI
- 万能板
- 工作频率: 803~930 MHz
- 支持 FSK,GFSK,MSK,GMSK,LoRa™和 OOK 调制模式
- 接收灵敏度：低至 - 140 dBm
- 可编程比特率高达 300Kbps
- 内置柔性 PCB 天线
- 外部天线接口
- 开发平台: Arduino

## 包装内容

- 1 x Module LoRa868

## 应用场景

- 自动抄表系统
- 楼宇自动化
- 远程灌溉系统

## 规格参数

| 规格     | 参数                  |
| -------- | --------------------- |
| 产品尺寸 | 54.2 x 54.2 x 13.0mm  |
| 产品重量 | 14.0g                 |
| 包装尺寸 | 138.0 x 93.0 x 15.0mm |
| 毛重     | 26.8g                 |

## 原理图

- [Module LoRa868 原理图 PDF](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/schematic/Modules/module_lora_sch.pdf)

<img src="https://static-cdn.m5stack.com/resource/docs/products/module/lora/lora_sch_01.webp" width="80%">

## 管脚映射

### M5-Bus

::m5-bus-table
| PIN      | LEFT | RIGHT | PIN |
| -------- | ---- | ----- | --- |
| GND      | 1    | 2     |     |
| GND      | 3    | 4     | IRQ |
| GND      | 5    | 6     |     |
| SPI_MOSI | 7    | 8     | RST |
| SPI_MISO | 9    | 10    |     |
| SPI_CLK  | 11   | 12    |     |
|          | 13   | 14    |     |
|          | 15   | 16    |     |
|          | 17   | 18    |     |
|          | 19   | 20    | CS  |
|          | 21   | 22    |     |
|          | 23   | 24    |     |
|          | 25   | 26    |     |
|          | 27   | 28    | 5V  |
|          | 29   | 30    |     |
::

## 数据手册

- [RA-01H](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Module-LoRa868_V1.1/ra-01h_product_specification_en.pdf)
- [SX127X](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Module-LoRa433_V1.1/sx1278.pdf)

## 软件开发

### Arduino

- [Module LoRa868 Arduino 驱动库](https://github.com/m5stack/M5-SX127x/blob/master/examples)
- [Module LoRa868 Arduino Demo(LoRaSender)](https://github.com/m5stack/M5-SX127x/blob/master/examples/LoRaSender/LoRaSender.ino)
- [Module LoRa868 Arduino Demo(LoRaReceiver)](https://github.com/m5stack/M5-SX127x/tree/master/examples/LoRaReceiver)
- [Module LoRa868 Arduino Demo(LoRaSetSpread)](https://github.com/m5stack/M5-SX127x/blob/master/examples/LoRaSetSpread/LoRaSetSpread.ino)
- [Module LoRa868 Arduino Demo(LoRaDuplex)](https://github.com/m5stack/M5-SX127x/blob/master/examples/LoRaDuplex/LoRaDuplex.ino)

### UiFlow1

- [Module LoRa868 UiFlow1 文档](/zh_CN/uiflow/blockly/module/lora868)

### UiFlow2

- [Module LoRa868 UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/module/lora.html)

### Easyloader

| Easyloader                                               | 下载链接                                                                                                         | 备注 |
| -------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---- |
| Module LoRa868 LoRaDuplex Example Easyloader with M5Core | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/MODULE/EasyLoader_LoRa868_MODULE.exe) | /    |

## 相关视频

<video id="example_video" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Module/LoRa868.mp4" type="video/mp4"></video>
