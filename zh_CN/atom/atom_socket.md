# Atom Socket

<span class="product-sku">SKU:K055</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/915/K055_product_pictures_01.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/915/K055_product_pictures_04.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_socket/atom_socket_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/915/K055_product_pictures_03.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/915/K055_product_pictures_02.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_socket/atom_socket_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/915/K055_Atom_Socket_weight.jpg">
</PictureViewer>

## 描述

**Atom Socket** 是一款适配 ATOM 主控的智能电源插座。内嵌 HLW8032 高精度电能计量 IC，通过串口通信能够读取插座进电的相关电气参数 (线电压，电流，有功功率，视在功率和功率因数) 。外部插孔采用日标规格，内部集成单路继电器 (AC 100 ~ 120V@10A) 用于控制插座电源通断，搭配集成 WIFI 模块的 ATOM 主控，该电源插座能够轻松接入网络，实现远程控制与电能计量。额外插座集成 HY2.0-4P 接口，能够与外部设备进行交互 (继电器信号输入，按键信号输出) 。

## 教程 & 快速上手

learn>| ![Home Assistant](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/hhome_assistant_cover_02.jpg) | [Home Assistant](/zh_CN/homeassistant/switch/atom_socket) | 本教程将介绍如何使用 Atom Socket 智能插座集成至 Home Assistant。 |

## 产品特性

- 单路继电器控制插座电源通断 (AC:100~120V@10A)
- HLW8032 高精度电能计量 IC
- 支持电压电流检测功率计算，1000:1 的动态范围内:
  - 有功功率的测量误差达到 0.2%
  - 有效电流的测量误差达到 0.5%
  - 有效电压的测量误差达到 0.5%
- UART 通讯 (baud:4800)
- ∑-Δ 型 ADC，高精度的电能计量内核
- 日标 / 美标插孔 - PSE 标准
- HY2.0-4P 外部控制接口

## 包装内容

- 1 x Atom-Lite
- 1 x Atom Socket

## 应用场景

- 计量插座
- 智能 WIFI 插座
- 智能家电控制

## 规格参数

| 规格                   | 参数                           |
| ---------------------- | ------------------------------ |
| HLW8032 串口通信波特率 | 4800bps 8E1                    |
| 建议负载功率           | <=1000W                        |
| 继电器参数             | AC 100 ~ 120V@10A / DC 28V@10A |
| 产品尺寸               | 90.0 x 42.0 x 55.0mm           |
| 产品重量               | 104.0g                         |
| 包装尺寸               | 92.0 x 62.0 x 42.0mm           |
| 毛重                   | 117.6g                         |

## 原理图

<SchViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_socket/atom_socket_sch_01.webp" width="80%">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_socket/atom_socket_sch_02.webp" width="80%">
</SchViewer>

## 管脚映射

| Atom        | G22 | G23   |
| ----------- | --- | ----- |
| Atom Socket | RX  | Relay |

## 尺寸图

- [Atom Socket模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/915/K055-atom-socket_asm.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/915/K055-atom-socket_asm_page_01.png" width="100%">

## 数据手册

- [HLW8032](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/atombase/atom_socket/DS_HLW8032_CN.pdf)

## 软件开发

### Arduino

- [Atom Socket 测试程序](https://github.com/m5stack/M5Atom/tree/master/examples/ATOM_BASE/ATOM_Socket)

### UiFlow1

- [Atom Socket UiFlow1 文档](/zh_CN/uiflow/blockly/atomic_base/socket)

### UiFlow2

- [Atom Socket Base UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/base/atom_socket.html)

### Home Assistant

- [Home Assistant 集成](/zh_CN/atom/atom_socket)

### EasyLoader

| Easyloader             | 下载链接                                                                                                         | 备注 |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------- | ---- |
| Atom Socket Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/ATOM_BASE/EasyLoader_Atom_Socket.exe) | /    |

## 相关视频

- 远程控制 Atom Socket 通断电源，并且监测电源状态

<video id="example_video" controls>
  <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/AtomBase/ATOM_Socket.mp4" type="video/mp4">
</video>
