# Atom Switch

<span class="product-sku">SKU:K042</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomhub_switch/atomhub_switch_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomhub_switch/atomhub_switch_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/899/K042-zheng-package.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/899/K042-fan-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomhub_switch/atomhub_switch_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomhub_switch/atomhub_switch_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomhub_switch/atomhub_switch_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomhub_switch/atomhub_switch_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/899/K042_Atom_Switch_weight.jpg">
</PictureViewer>

## 描述

**Atom Switch** 是一款支持 ATOM 的双路控制可编程开关，可同时接入两路交流 / 直流电路进行通断控制。内置降压模块可为 ATOM 提供 5V/1A 的直流电源，板载继电器最高支持 250V/10A 市电 (16A 瞬时电流) ，为了保障使用安全，其直流电路具备过热与短路保护功能，当电流过大或发生短路时能有效断开电路。为了方便用户在工业场景中使用，我们内置了一颗 SP485EE 电平转换芯片，提供一组 RS485 接口供用户连接 RS485 设备，RS485 具备为 ATOM 供电的能力，支持电压为 9-24V。此外还提供了一组 HY2.0 接口用于连接 I2C 外设或通用 I/O 设备。借助于 ATOM 的 WIFI 功能，您可以轻松实现远程遥控开关设备，如果您有多个**Atom Switch** ，可以通过 RS485 接口进行并联。

## 产品特性

- 内置 AC-DC 电路供电
- 2 路继电器
- 内置 RS485 电平转换，支持 Modbus
- HY2.0 扩展
- 短路过热保护
- 可通过 WIFI、RS485 进行遥控

## 包装内容

- 1 x Atom-Lite
- 1 x Atom Switch
- 1 x 双面胶
- 1 x 轨道夹具
- 1 x HT3.96-4P 端子
- 3 x 3.96 x 3P 公头
- 1 x M4 内六角扳手
- 1 x M2 内六角扳手
- 2 x M4\*10mm 内六角沉头螺丝
- 1 x M2\*20mm 内六角杯头机械牙螺丝
- 1 x I/O 贴纸

## 应用场景

- 智能开关

## 规格参数

| 规格                 | 参数                                                                                              |
| -------------------- | ------------------------------------------------------------------------------------------------- |
| 继电器参数           | AC 250V@10A（瞬时 16A）                                                                           |
| Switch 电源（AC-DC） | AC 250V-DC 5V                                                                                     |
| RS485 供电电压       | DC 9 ~ 24V                                                                                        |
| 接口                 | 1 x HY2.0-4P（PORT.A）, 1 x HT3.96-4P（RS485）, 2 x HT3.96-2P（Relay）, 1 x HT3.96-2P（AC/DC IN） |
| 外壳材质             | Plastic （ PC ）                                                                                  |
| 产品尺寸             | 72.0 x 40.0 x 30.0mm                                                                              |
| 产品重量             | 80.0g                                                                                             |
| 包装尺寸             | 150.0 x 77.0 x 35.0mm                                                                             |
| 毛重                 | 168.4g                                                                                            |

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomhub_switch/atomhub_switch_sch_01.webp" width="80%">

## 管脚映射

::m5-bus-table
| PIN    | LEFT | RIGHT | PIN      |
| ------ | ---- | ----- | -------- |
|        |      | 1     | 3V3      |
| PORT.A | 2    | 3     | RELAY1   |
| PORT.A | 4    | 5     | RELAY2   |
| 5V     | 6    | 7     | RS485_RX |
| GND    | 8    | 9     | RS485_TX |
::

## 尺寸图

- [Atom Switch模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/899/K042-atom-swtich.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/899/K042-atom-swtich_page_01.png" width="100%">

## 数据手册

- [SP485EE](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/hat/SP485EEN_en.pdf)

## 软件开发

### Arduino

- [Atom Switch 测试程序](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/AtomBase/AtomHubSwitch/AtomHubSwitch)

### UiFlow1

- [Atom Switch 测试程序](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/AtomBase/AtomHubSwitch/UIFlow)

<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomhub_switch_d/atomhub_switch_d_uiflow_01.webp" width="65%">

### EasyLoader

| Easyloader             | 下载链接                                                                                                           | 备注 |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------ | ---- |
| Atom Switch Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/ATOM_BASE/EasyLoader_AtomHubSwitch.exe) | /    |

## 相关视频

<video id="example_video" controls>
  <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/AtomBase/AtomSwitch.mp4" type="video/mp4">
</video>

## 产品对比

| /            | Switch           | Switch-D                                                 |
| ------------ | ---------------- | -------------------------------------------------------- |
| 继电器电流   | AC 250V/10A      | AC 250V/5A                                               |
| 电源输入接口 | HT3.96R 2P       | HT3.96R 3P                                               |
| 继电器接口   | （NO,NC,COM） x2 | （NO（直连 AC 电源 L 线）, COM（直连 AC 电源 N 线）） x2 |

<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomhub_switch_d/atomhub_switch_d_07.webp">

## 操作说明

\#> 套件配套导轨固件夹具，具体安装方式请参考下图:

<div class="product_pic">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomhub_switch_d/atomhub_switch_d_08.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomhub_switch_d/atomhub_switch_d_09.webp">
</div>
