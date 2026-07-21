# Unit ChainBus

<span class="product-sku">SKU:U212</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1201/U212_main_pictures_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1201/U212_main_pictures_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1201/U212_main_pictures_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1201/U212_main_pictures_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1201/U212_main_pictures_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1201/U212_main_pictures_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1201/U212_main_pictures_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1201/U212_main_pictures_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1201/U212_main_pictures_09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1201/U212_main_pictures_10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1201/U212_main_pictures_11.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1201/U212-weight.jpg">
</PictureViewer>

## 描述

Unit ChainBus 是一款 Chain 系列通信协议转换单元，设备内部集成 STM32G031G8U6 芯片，采用 UART 串口级联通信协议实现多设备**链式连接**，支持多种协议接口转换，同一总线可拓展连接多种外设，并集成了硬件控制与数据交互能力。本单元左右两侧 UART 接口用于连接 Chain 系列设备，支持设备 UID 查询、版本查询、链路设备枚举、心跳包通信等功能；顶部多功能拓展接口可用于拓展 Unit 系列设备，支持 I2C 通信控制、GPIO 管理（输入、输出）、ADC 采集，NVIC 中断管理，适用于工业控制、物联网、智能家居等领域，为多设备统一管控与数据交互提供了有效方案。

## 产品特性

- STM32G031G8U6 核心主控
- 采用 UART 串口级联通信协议，支持 Chain 系列单 / 多设备链式连接
- 1 x RGB LED，可作为状态指示灯使用
- 1 x HY2.0-4P 多功能拓展接口，可拓展 Unit 系列设备
- 2 x HY2.0-4P UART 接口，可拓展 Chain 系列设备
- 开发平台
  - UiFlow2
  - Arduino

## 包装内容

- 1 x Unit ChainBus
- 2 x HY2.0-4P Grove 连接线 (5cm)

## 应用场景

- Chain 总线设备拓展
- 工业控制
- 物联网
- 智能家居

## 规格参数

| 规格         | 参数                                                                     |
| ------------ | ------------------------------------------------------------------------ |
| MCU          | STM32G031G8U6                                                            |
| 接口         | 2 x HY2.0-4P UART 接口、1 x HY2.0-4P 多功能拓展接口                      |
| RGB LED      | 1 x WS2812                                                               |
| 通信接口     | UART 115200bps @ 8N1                                                     |
| 级联协议     | Chain Bus UART 串口级联通信协议                                          |
| 级联功能     | 设备 UID 查询、版本查询、链路设备枚举、心跳包通信等                      |
| 拓展接口功能 | I2C 通信控制、GPIO 管理（含中断配置与状态查询）、ADC 采集、NVIC 中断管理 |
| 工作功耗     | RGB 白光最大亮度 3.3V@17.72mA                                            |
| 产品尺寸     | 29.8 x 24.0 x 8.0mm                                                      |
| 产品重量     | 3.9g                                                                     |
| 包装尺寸     | 138.0 x 93.0 x 10.0 mm                                                   |
| 毛重         | 8.7g                                                                     |

## 操作说明

Unit ChainBus 左右两侧的 HY2.0-4P 接口分别用于 Chain Bus 总线输入与输出，顶部拓展连接头可用于连接 Unit 系列设备。<br>
Unit ChainBus 采用与 Chain 系列其他拓展设备（如 Chain Angle、Chain Encoder 等）一样的 UART 的级联协议，可作为自定义的功能节点，接入到 Chain Bus 总线中。同一总线可拓展连接多个 Unit ChainBus， 通过接口功能配置，同一总线也能集成不同类型的硬件外设控制。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1201/U212_operate_01.jpg" width="70%">

## 原理图

- [Unit ChainBus 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1201/SCH_ChainBus_SCH_Main_V1.0_20250704_2025_11_28_11_09_00.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1201/SCH_ChainBus_SCH_Main_V1.0_20250704_2025_11_28_11_09_00_page_01.png">
</SchViewer>

## 管脚映射

### RGB LED

| STM32G031G8U6 | PA8 |
| ------------- | --- |
| WS2812C       | RGB |

### UART

| STM32G031G8U6 | PA2  | PA3  | PB6  | PB7  |
| ------------- | ---- | ---- | ---- | ---- |
| UART1         |      |      | TXD1 | RXD1 |
| UART2         | TXD2 | RXD2 |      |      |

### 外部连接

- 顶部 HY2.0-4P Grove 接口 - 拓展接口

::grove-table
| HY2.0-4P | Black | Red | Yellow     | White      |
| -------- | ----- | --- | ---------- | ---------- |
| PORT     | GND   | 5V  | SDA/IO/ADC | SCL/IO/ADC |
::

- 左侧 HY2.0-4P Grove 接口 - IN

::grove-table
| HY2.0-4P | Black | Red | Yellow   | White    |
| -------- | ----- | --- | -------- | -------- |
| PORT.IN  | GND   | 5V  | UART1_RX | UART1_TX |
::

- 右侧 HY2.0-4P Grove 接口 - OUT

::grove-table
| HY2.0-4P | Black | Red | Yellow   | White    |
| -------- | ----- | --- | -------- | -------- |
| PORT.OUT | GND   | 5V  | UART2_TX | UART2_RX |
::

## 尺寸图

- [Unit ChainBus 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1201/U212-model-size-unit-chainbus.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1201/U212-model-size-unit-chainbus_page_01.png" width="100%">

## 软件开发

### Arduino

- [Unit ChainBus Arduino 驱动库](https://github.com/m5stack/M5Chain)
- [Unit ChainBus Arduino 快速上手](/zh_CN/arduino/projects/unit/unit_chainbus)

### UiFlow2

- [Unit Chain Bus UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/chain/unit_bus.html)

### 内置固件

- [Unit ChainBus 内置固件](https://github.com/m5stack/M5Chain-Series-Internal-FW/tree/main/Unit-ChainBus)

### 通信协议

\#> 说明 | 协议中蓝色部分为顶部 Grove 接口控制功能，粉色部分为左右侧 Grove 接口的 UART 串口通信功能。

- [Unit ChainBus 通信协议](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1201/M5Stack-Unit-ChainBus-Protocol-CN.pdf)

<!-- 英文版链接： https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1201/M5Stack-Unit-ChainBus-Protocol-EN.pdf -->

## 相关视频

- Unit ChainBus 产品介绍以及功能展示

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1201/U212-Unit-ChainBus-video-ZH.mp4" type="video/mp4"></video>

<!-- 中英文视频链接不一样 -->

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=115926452146057&bvid=BV1MRk5BcEtb&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/QAva4d3ro_Y?si=6FePd0d1MxKJygMo" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
