# Base DMX

<span class="product-sku">SKU:M128</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/DMX_Base/img-3ff79a98-9198-428f-a4ea-f50c58d834d1.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/DMX_Base/img-165f2fab-f842-4869-8b96-48b4898f9293.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/DMX_Base/img-542912f9-405b-48ae-b40d-7bed89041cc4.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/DMX_Base/img-0fa443bf-2ec6-4fde-adcc-9d59a310a491.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/DMX_Base/img-7a2c8000-476c-4185-9944-c3aecf771a3d.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/DMX_Base/img-1edd72bb-2d06-481f-9e0e-10bb45a80822.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/DMX_Base/img-d836ad93-eae0-4e00-b707-3ffe1da94782.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/DMX_Base/img-5ede0323-fc17-49f1-9765-142ac82ba566.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/DMX_Base/img-feb5488e-f65b-44b2-86e9-39ce66f0750f.webp">
</PictureViewer>

## 描述

Base DMX 是一款专门为 DMX-512 数据传输场景设计的功能底座，与 M5 主机 通过串口 进行通讯和使能控制，配备 XLR-5 和 XLR-3 公母头接口，方便用户连接不同接口的 DMX 设备。此外，模块上留有 HT3.96 间距的 485 接口，方便连接扩展 485 设备。通信信号采用高速光耦隔离，电源采用专用隔离电源模块，提供 两路独立的 RS-485 电路实现收、发 DMX 数据，可通过内部双掷开关选择两路独立或并接运行。供电方面，DC-JACK 接口以及相应的 DC-DC 电路 ，可为整个设备提供电源。本产品适用舞台灯光控制、声音设备控制、景观照明控制和彩灯控制等场合。

## 产品特性

- 配备 XLR-5 和 XLR-3 公母头接口，方便用户连接 DMX 设备
- 支持与 M5 主机通过串口进行通讯和使能控制
- 内置两路双掷开关，方便用户控制连接方式和传输路径
- 采用电源 DC-DC 隔离方式，提高稳定性和一致性
- 开发平台：
  - Arduino
  - UiFlow

## 包装内容

- 1 x Base DMX
- 1 x 内六角扳手 L 形 2.0mm (适配 M2.5 螺丝)
- 1 x 3.96-4P 端子
- 1 x XLR-3 接口

## 应用场景

- 舞台灯光控制
- 声音设备控制
- 景观照明控制
- 彩灯控制

## 规格参数

| 规格             | 参数                    |
| ---------------- | ----------------------- |
| 485 通讯         | SP3488EN                |
| 光耦隔离高速传输 | EL0600EL0631            |
| DC-DC            | MP1584EN                |
| 电压隔离         | B0505LS-1WR2            |
| 电压输入         | DC 9 ~ 24V              |
| DMX 接口         | XLR-5、XLR-3 公母头接口 |
| 485 接口         | HT3.96 接口             |
| 电源输出         | DC 5V/3.3V              |
| 工作温度范围     | 0 ~ 40°C                |
| 支持 DMX 信号    | DMX512                  |
| 产品尺寸         | 54.0 x 54.0 x 27.0mm    |
| 产品重量         | 48.0g                   |
| 包装尺寸         | 147.0 x 90.0 x 40.0mm   |
| 毛重             | 88.2g                   |

## 操作说明

### 板载开关功能说明

- Switch1: 控制 Base DMX 输出接口是否接入 680Ω 偏置电阻。该电阻用于确保总线空闲状态下的稳定电平与改善信号质量。
- Switch2：控制 Base DMX 输入信号分离 (信号输入到主控) 或是旁通输出到输出接口。
- Switch3：控制 Base DMX 输入接口是否接入 120Ω 终端电阻，该电阻用于减少信号反射与改善信号质量。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1017/base_dmx_switch_define.png" width="80%">

## 原理图

- [Base DMX 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/555/SCH_DMX_Base_V1.0.pdf)
- [Base DMX Sub 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/555/Sch_DMX-sub_V1.0.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/555/SCH_DMX_Base_V1.0_sch_01.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/555/Sch_DMX-sub_V1.0_sch_01.png">
</SchViewer>

## 管脚映射

### M5-Bus

::m5-bus-table
| PIN      | LEFT | RIGHT | PIN     |
| -------- | ---- | ----- | ------- |
| GND      | 1    | 2     | UART_RX |
| GND      | 3    | 4     | NC      |
| GND      | 5    | 6     | NC      |
| NC       | 7    | 8     | NC      |
| NC       | 9    | 10    | NC      |
| NC       | 11   | 12    | 3V3     |
| NC       | 13   | 14    | NC      |
| NC       | 15   | 16    | NC      |
| NC       | 17   | 18    | NC      |
| NC       | 19   | 20    | NC      |
| RS485_EN | 21   | 22    | UART_TX |
| NC       | 23   | 24    | NC      |
| HPWR     | 25   | 26    | NC      |
| HPWR     | 27   | 28    | 5V      |
| HPWR     | 29   | 30    | BAT     |
::

## 尺寸图

- [Base DMX 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1017/M128-BASE-DMX.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1017/M128-BASE-DMX_page_01.png" width="100%">

## 数据手册

- [EL0660](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/M128%20DMX-Base/EL0600.PDF)
- [EL0631](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/M128%20DMX-Base/EL0631.PDF)
- [MP1584EN](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/M128%20DMX-Base/MP1584EN-LF-Z.pdf)
- [SP485EEN](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/M128%20DMX-Base/SP485EEN.pdf)
- [B0505LS-1WR2](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/M128%20DMX-Base/B0505LS-1WR2.PDF)

## 软件开发

### Arduino

- [Base DMX Arduino 驱动库](https://github.com/m5stack/M5Module-DMX512)
- [Base DMX Tools Demo](https://github.com/m5stack/M5Module-DMX512/tree/master/examples/DMX512Tools)

<video id="example_video" controls>
  <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/M128%20DMX_Base/DMX_Base.mp4" type="video/mp4">
</video>

### UiFlow1

- [Base DMX UiFlow1 文档](/zh_CN/uiflow/blockly/base/dmx)
