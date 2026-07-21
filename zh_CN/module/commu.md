# Module COMMU

<span class="product-sku">SKU:M011</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/commu/commu_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/commu/commu_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/953/M011-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/commu/commu_04.webp">
</PictureViewer>

## 描述

**Module COMMU** 是 M5Stack 堆叠模块系列中的一款 ，通信转换模块。其内部集成了 2 个**I2C**接口、1 个**TTL**接口、1 个**CAN**接口、1 个**RS485**接口，能够满足开发时遇到的各种通信转换需求。

## 注意事项

\#> 注意 | 在搭配 Core2 使用时需要将底座拆下才能正常烧录程序。

## 产品特性

- 支持 I2C,TTL,RS485,CAN 等多种通讯协议

## 包装内容

- 1 x Module COMMU

## 规格参数

| 规格         | 参数                             |
| ------------ | -------------------------------- |
| 接口         | I2C x2, CAN x1, RS485 x1, TTL x1 |
| CAN 控制器   | MCP2515-1/SO                     |
| RS485 收发器 | SP3485EN-L/TR                    |
| 材质         | Plastic (PC)                     |
| 产品重量     | 13.5g                            |
| 毛重         | 24g                              |
| 产品尺寸     | 54.2 x 54.2 x 13mm               |
| 包装尺寸     | 133 x 95 x 16mm                  |

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/module/commu/commu_sch_01.webp" width="80%">

## 管脚映射

### M5-Bus

::m5-bus-table
| PIN         | LEFT | RIGHT | PIN         |
| ----------- | ---- | ----- | ----------- |
| GND         | 1    | 2     |             |
| GND         | 3    | 4     |             |
| GND         | 5    | 6     |             |
| SPI_MOSI    | 7    | 8     |             |
| SPI_MISO    | 9    | 10    |             |
| SPI_CLK     | 11   | 12    |             |
| UART_TX0    | 13   | 14    | UART_RX0    |
| RS485_TX    | 15   | 16    | RS485_RX    |
| I2C_SDA     | 17   | 18    | I2C_SCL     |
|             | 19   | 20    |             |
| CAN_CS      | 21   | 22    |             |
| CAN_INT     | 23   | 24    |             |
|             | 25   | 26    |             |
|             | 27   | 28    | 5V          |
|             | 29   | 30    |             |
::

## 尺寸图

[Module COMMU 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/953/module-commu.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/953/module-commu_page_01.png" width="100%">

## 数据手册

- [SP3485](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/SP3485_en.pdf)
- [MCP2515](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/MCP2515_en.pdf)

## 软件开发

### Arduino

- [Module COMMU Arduino 快速上手](/zh_CN/arduino/projects/module/module_commu)
- [Module COMMU Example with M5Core](https://github.com/m5stack/M5Stack/tree/master/examples/Modules/COMMU)

### UiFlow1

- [Module COMMU UiFlow1 文档](/zh_CN/uiflow/blockly/module/commu)

### UiFlow2

- [Module Commu UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/module/commu.html)

### Easyloader

| Easyloader                                  | 下载链接                                                                                                       | 备注 |
| ------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | ---- |
| Module COMMU Example Easyloader with M5Core | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/MODULE/EasyLoader_COMMU_MODULE.exe) | /    |

## 相关视频

<video id="example_video" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Module/COMMU.mp4" type="video/mp4"></video>
