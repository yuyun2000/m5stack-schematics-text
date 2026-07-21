# Atomic RS232 Base

<span class="product-sku">SKU:A136</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/923/Atomic_RS232_Base_main_pictures_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/923/Atomic_RS232_Base_main_pictures_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/923/Atomic_RS232_Base_main_pictures_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/923/Atomic_RS232_Base_main_pictures_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/923/Atomic_RS232_Base_main_pictures_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/923/Atomic_RS232_Base_main_pictures_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/923/Atomic_RS232_Base_main_pictures_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/923/Atomic_RS232_Base_main_pictures_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/923/Atomic_RS232_Base_main_pictures_09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/923/A136_Atomic_RS232_Base_weight.jpg">
</PictureViewer>

## 描述

**Atomic RS232 Base** 是一款适用于适配 Atom 系列主机的 TTL-RS232 电平转换器。RS-232 是一种用于计算机和外围设备之间串行通信的标准，定义了电气特性和数据传输协议。模块采用 MAX232 芯片，支持 TTL 电平与 RS232 电平的双向转换，同时内置 DC-DC 降压稳压芯片，可以支持外部 12V 电平为 ATOM 供电。

## 产品特性

- 全双工通讯
- 内置 DC-DC

## 包装内容

- 1 × Atomic RS232 Base
- 1 × HT3.96-4P

## 应用场景

- RS232 通讯
- 工业控制节点

## 规格参数

| 规格         | 参数                  |
| ------------ | --------------------- |
| 外接端口     | VH-3.96 4P            |
| 电平转换芯片 | MAX232                |
| DC-DC        | A0Z1282CI             |
| 外壳材质     | Plastic (PC)          |
| 产品尺寸     | 24.0 x 48.0 x 18.0mm  |
| 产品重量     | 9.4g                  |
| 包装尺寸     | 136.0 x 92.0 x 13.0mm |
| 毛重         | 14.5g                 |

## 原理图

<img alt="schematics" src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic RS232 Base/img-0b5ff32c-a49e-4f05-a4e7-9ef94207bc70.webp" width="100%" />

## 管脚映射

::m5-bus-table
| PIN | LEFT | RIGHT | PIN     |
| --- | ---- | ----- | ------- |
|     |      | 1     | 3V3     |
|     | 2    | 3     | UART_TX |
|     | 4    | 5     | UART_RX |
| 5V  | 6    | 7     |         |
| GND | 8    | 9     |         |
::

## 尺寸图

- [Atomic RS232 Base模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/931/A092-atom-pwm.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/931/A092-atom-pwm_page_01.png" width="100%">

## 数据手册

- [MAX232](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/atombase/AtomicRS232/MAX232.pdf)
- [AOZ1282CI](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/atombase/tail485/AOZ1282CI-datasheet.pdf)

## 软件开发

### Arduino

- [Atomic RS232 Base Arduino 快速上手](/zh_CN/arduino/projects/atomic/atomic_rs485_232_base)

### UiFlow1

- [Atomic RS232 Base 测试程序](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/AtomBase/AtomicRS232/UIFlow)

<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic RS232 Base/uiflowCase-1691568007701atomic232_uiflow_01.png" width="100%"/>

### UiFlow2

- [Atomic RS232 Base UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/base/rs232.html)

### EasyLoader

| Easyloader                        | 下载链接                                                                                                                                       | 备注 |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---- |
| Atomic RS232 Base Test Easyloader | [download](https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic%20RS232%20Base/ezLoader-d540109d-17b5-403d-b519-3f1610ac920e.exe) | /    |

## 相关视频

- AtomicRS232 Base 示例用法

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/AtomBase/AtomicRS232.mp4" type="video/mp4"></video>

- AtomicRS232 Base 和 ATOM Printer 通讯

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/Atomic%20RS232%20Base/A136%20Atomic%20RS232%20Base.mp4" type="video/mp4"></video>
