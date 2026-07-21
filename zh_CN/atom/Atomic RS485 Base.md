# Atomic RS485 Base

<span class="product-sku">SKU:A131</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/922/Atomic_RS485_Base_main_pictures_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/922/Atomic_RS485_Base_main_pictures_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/922/A131-package.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/922/Atomic_RS485_Base_main_pictures_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/922/Atomic_RS485_Base_main_pictures_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/922/Atomic_RS485_Base_main_pictures_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/922/Atomic_RS485_Base_main_pictures_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/922/Atomic_RS485_Base_main_pictures_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/922/A131-weight.jpg">
</PictureViewer>

## 描述

**Atomic RS485 Base** 是一款基于 Atomic 设计的 TTL-RS485 转换器，用于 TTL 电平与 RS485 电平转换。RS485 是工业领域应用广泛的一种电气规范，具有更强的抗干扰能力与更远的传输距离。其内部集成有 DC/DC 降压稳压芯片，可以直接将 RS485 的 12V 电压转为 5V 为 ATOM 供电，免去了单独供电的烦恼，当多台设备需要通信控制时，使用 Atomic RS485 进行接口类型转接会是一个不错的选择。

## 产品特性

- 多点通讯
- SP3485EE
- 内置 DC-DC

## 包装内容

- 1 x Atomic RS485 Base
- 1 x HT3.96-4P 端子
- 1 x I/O 贴纸

## 应用场景

- RS485 多点通讯
- 工业控制节点

## 规格参数

| 规格        | 参数                  |
| ----------- | --------------------- |
| 外接端口    | VH-3.96 4P            |
| 电平转换 IC | SP3485EE              |
| DC-DC       | A0Z1282CI             |
| 外壳材质    | Plastic (PC)          |
| 产品尺寸    | 24.0 x 48.0 x 18.0mm  |
| 产品重量    | 9.9g                  |
| 包装尺寸    | 136.0 x 92.0 x 13.0mm |
| 毛重        | 14.5g                 |

## 原理图

<img alt="schematics" src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic RS485 Base/img-1f833240-7458-4d92-8120-c60a936e1c04.webp" width="100%" />

## 管脚映射

::m5-bus-table
| PIN | LEFT | RIGHT | PIN      |
| --- | ---- | ----- | -------  |
|     |      | 1     | 3V3      |
|     | 2    | 3     | RS485_RX |
|     | 4    | 5     | RS485_TX |
| 5V  | 6    | 7     |          |
| GND | 8    | 9     |          |
::

## 尺寸图

- [Atomic RS485 Base模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/931/A092-atom-pwm.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/931/A092-atom-pwm_page_01.png" width="100%">

## 数据手册

- [SP485EEN](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/hat/SP485EEN_en.pdf)
- [AOZ1282CI](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/atombase/tail485/AOZ1282CI-datasheet.pdf)

## 软件开发

### Arduino

- [Atomic RS485 Base Arduino 快速上手](/zh_CN/arduino/projects/atomic/atomic_rs485_232_base)

### UiFlow1

- [Atomic RS485 Base UiFlow1 测试程序](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/AtomBase/AtomicRS485/UIFlow)

<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic RS485 Base/uiflowCase-1690959488958atomic485_uiflow_01.png" width="100%"/>

### UiFlow2

- [Atomic RS485 Base UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/base/rs485.html)

### EasyLoader

| Easyloader                        | 下载链接                                                                                                                                       | 备注 |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---- |
| Atomic RS485 Base Test Easyloader | [download](https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic%20RS485%20Base/ezLoader-34f76c77-d882-458d-9c0e-dd603a1cd137.exe) | /    |

## 相关视频

- MQTT & RS485 控制继电器

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/Atomic%20RS485%20Base/A131.mp4" type="video/mp4"></video>
