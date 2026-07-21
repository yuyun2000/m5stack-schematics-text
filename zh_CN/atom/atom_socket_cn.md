# Atom Socket-CN

<span class="product-sku">SKU:K055-CN</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_socket_cn/atom_socket_cn_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_socket_cn/atom_socket_cn_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/916/K055-CN-zheng-package.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/916/K055-CN-fan-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_socket_cn/atom_socket_cn_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_socket_cn/atom_socket_cn_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_socket_cn/atom_socket_cn_05.webp">
</PictureViewer>

## 描述

**Atom Socket-CN** 是一款适配 ATOM 主控的智能电源插座。内嵌 HLW8032 高精度电能计量 IC，通过串口通信能够读取插座进电的相关电气参数 (线电压，电流，有功功率，视在功率和功率因数) 。外部插孔采用中国标准规格，内部集成单路继电器 (AC 220V@10A) 用于控制插座电源通断，搭配集成 WIFI 模块的 ATOM 主控，该电源插座能够轻松接入网络，实现远程控制与电能计量。额外插座集成 HY2.0-4P 接口，能够与外部设备进行交互 (继电器信号输入，按键信号输出) 。

## 产品特性

- 单路继电器控制插座电源通断 (AC:220V@10A)
- HLW8032 高精度电能计量 IC
- 支持电压电流检测功率计算，1000:1 的动态范围内:
  - 有功功率的测量误差达到 0.2%
  - 有效电流的测量误差达到 0.5%
  - 有效电压的测量误差达到 0.5%
- UART 通讯 (baud:4800)
- ∑-Δ 型 ADC，高精度的电能计量内核
- 中国标准插孔
- HY2.0-4P 外部控制接口

## 包装内容

- 1 x Atom-Lite
- 1 x Atom Socket CN

## 应用场景

- 计量插座
- 智能 WIFI 插座
- 智能家电控制

## 规格参数

| 规格                   | 参数                     |
| ---------------------- | ------------------------ |
| HLW8032 串口通信波特率 | 4800                     |
| 建议负载功率           | <=1000W                  |
| 继电器参数             | AC:220V@10A / DC:28V@10A |
| 产品尺寸               | 90 x 42 x 55mm           |
| 产品重量               | 104.0g                   |
| 包装尺寸               | 93.0 x 62.0 x 42.0mm     |
| 毛重                   | 116.6g                   |

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

### EasyLoader

| Easyloader             | 下载链接                                                                                                         | 备注 |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------- | ---- |
| Atom Socket Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/ATOM_BASE/EasyLoader_Atom_Socket.exe) | /    |

## 相关视频

- 远程控制 ATOM Socket 通断电源，并且监测电源状态

<video id="example_video" controls>
  <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/AtomBase/ATOM_SOCKET_CN.mp4" type="video/mp4">
</video>
