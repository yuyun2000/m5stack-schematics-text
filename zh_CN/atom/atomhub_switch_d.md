# Atom Switch-D

<span class="product-sku">SKU:K042-D</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomhub_switch_d/atomhub_switch_d_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomhub_switch_d/atomhub_switch_d_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/900/K042-D-zheng-package.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/900/K042-D-fan-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomhub_switch_d/atomhub_switch_d_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomhub_switch_d/atomhub_switch_d_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomhub_switch_d/atomhub_switch_d_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomhub_switch_d/atomhub_switch_d_06.webp">
</PictureViewer>

## 描述

**Atom Switch-D** 是一款专为 ATOM 主控适配的双路继电器电源控制开关，其中 D 表示着 Directly (直接), 在设计上 Switch D 采用了电源输入直连继电器的方案。交流电源直接流向两路继电器的 NO (常开) 触点，由 ATOM 进行通断控制。使用时，用户只需要将用电负载接入继电器既可，无需另外连接电源线路。与以往的继电器控制方案相比，这一款模块在控制用电负载上，会更加的简洁高效。

输入电源除了用于继电器负载供电，同时还将经过内置降压模块可为 ATOM 提供 5V/1A 的直流电源，为了保障使用安全，该电源输入电路具备过热与短路保护功能，当电流过大或发生短路时能有效断开电路，防止元器件损坏。内置 SP485EE 电平转换芯片，提供 RS485 通信接口支持多设备挂载通信，集成 9-24V 降压 5V 电路适应工业场景上的取电需求，拓展供电能力。引出了一组 HY2.0-4P 接口用于连接 I2C 外设或通用 I/O 设备。结合 ATOM 自带与 WIFI 功能，**Atom Switch-D** 可以快速搭建远程设备开关应用。

## 产品特性

- 内置 AC-DC 电路供电
- 2 路继电器
- 内置 RS485 电平转换，支持 Modbus
- HY2.0-4P 扩展接口
- 短路过热保护
- 可通过 WIFI、RS485 进行控制

## 包装内容

- 1 x Atom-Lite
- 1 x Atom Switch-D
- 4 x 强力磁铁
- 1 x 双面胶
- 1 x 轨道夹具
- 1 x HT3.96-4P 端子
- 3 x 3.96 x 2P 公头
- 1 x M4 内六角扳手
- 1 x M2 内六角扳手
- 2 x M4\*10mm 内六角沉头螺丝
- 1 x M2\*20mm 内六角杯头机械牙螺丝

## 应用场景

- 智能开关

## 规格参数

| 规格                 | 参数                                                                                              |
| -------------------- | ------------------------------------------------------------------------------------------------- |
| 继电器参数           | AC 250V/5A                                                                                        |
| Switch 电源（AC-DC） | AC 110 ~ 250V -> DC 5V                                                                            |
| RS485 供电电压       | DC 9 ~ 24V                                                                                        |
| 接口                 | 1 x HY2.0-4P（PORT.A）, 1 x HT3.96-4P（RS485）, 2 x HT3.96-2P（Relay）, 1 x HT3.96-2P（AC/DC IN） |
| 外壳材质             | Plastic （ PC ）                                                                                  |
| 产品尺寸             | 72 x 40 x 30mm                                                                                    |
| 产品重量             | 134g                                                                                              |
| 包装尺寸             | 102.0 x 78.0 x 35.0mm                                                                             |
| 毛重                 | 158g                                                                                              |

## 操作说明

\#> 套件配套导轨固件夹具，具体安装方式请参考下图:

<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomhub_switch_d/atomhub_switch_d_08.webp" width="60%">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomhub_switch_d/atomhub_switch_d_09.webp" width="60%">

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomhub_switch_d/atomhub_switch_d_sch_01.webp" width="80%">

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

- [Atom Switch-D 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/900/K042-D-atom-swtich-D.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/900/K042-D-atom-swtich-D_page_01.png" width="100%">

## 数据手册

- [SP485EE](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/hat/SP485EEN_en.pdf)

## 软件开发

### Arduino

- [Atom Switch-D 测试程序](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/AtomBase/AtomHubSwitch/AtomHubSwitch)

### UiFlow1

- [Atom Switch-D 测试程序](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/AtomBase/AtomHubSwitch/UIFlow)

<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomhub_switch_d/atomhub_switch_d_uiflow_01.webp" width="65%">

### EasyLoader

| Easyloader               | 下载链接                                                                                                           | 备注 |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------ | ---- |
| Atom Switch-D Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/ATOM_BASE/EasyLoader_AtomHubSwitch.exe) | /    |

## 相关视频

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/AtomBase/ATOM_SWITCH_D.mp4" type="video/mp4">
</video>

## 产品对比

### Switch & Switch-D 对比

| /            | Switch           | Switch-D                                                 |
| ------------ | ---------------- | -------------------------------------------------------- |
| 继电器电流   | AC 250V/10A      | AC 250V/5A                                               |
| 电源输入接口 | HT3.96R 2P       | HT3.96R 3P                                               |
| 继电器接口   | （NO,NC,COM） x2 | （NO（直连 AC 电源 L 线）, COM（直连 AC 电源 N 线）） x2 |

<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomhub_switch_d/atomhub_switch_d_07.webp">
