# Module ExtPort For Core2

<span class="product-sku">SKU:M123</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/extport_for_core2/extport_for_core2_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/extport_for_core2/extport_for_core2_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/976/M123-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/extport_for_core2/extport_for_core2_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/extport_for_core2/extport_for_core2_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/extport_for_core2/extport_for_core2_06.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/extport_for_core2/extport_for_core2_07.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/extport_for_core2/extport_for_core2_08.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/extport_for_core2/extport_for_core2_09.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/extport_for_core2/extport_for_core2_grove_01.webp" width="80%">
</PictureViewer>

## 描述

**Module ExtPort For Core2**是一款专门为 **M5Stack Core2** 转接 **Grove 接口**的堆叠扩展模块。它提供了 **PORT.B/PORT.C/PORT.D/PORT.E** 4 路 Grove 接口，其中 **PORT.D/PORT.E** 能通过内部拨码开关配置不同的 GPIO。

## 注意事项

\#>**注意:**<br/>1.**ExtPort For Core2**正面写有合作者签名。<br/>2. 在使用之前，请将拨码开关中对应的开关拨到 `ON`。其中所有拨码开关的 "1" 号位默认为 ON。切记每个拨码开关中只允许一位拨到 ON，若多位为 ON 时，设备有可能损坏。<br/>3. 如果你需要使用 Core2 的底盖，则需要把 PROTO 模块的四个支撑脚剪掉 (如下图)，以避免底盖的干涉，并为固定准备适合长度的 M3 螺丝。

<img src="https://static-cdn.m5stack.com/resource/docs/products/module/extport_for_core2/extport_for_core2_02.webp" width="40%"><img src="https://static-cdn.m5stack.com/resource/docs/products/module/extport_for_core2/extport_for_core2_default_setting.webp" width="25%"><img src="https://static-cdn.m5stack.com/resource/docs/products/module/extport_for_core2/extport_for_core2_case_modify.webp" width="30%">

## 产品特性

- 4 x Grove 接口 (PortB/C/D/E)
- 4 x 3 位拨码开关 (PortD/E)
- 1 x 5Pin@2.54mm 排针

## 包装内容

- 1 x Module ExtPort For Core2

## 应用场景

- 多传感器、多执行器扩展
- DIY 项目

## 规格参数

| 规格     | 参数                       |
| -------- | -------------------------- |
| 扩展接口 | PortB, PortC, PortD, PortE |
| 产品尺寸 | 54.0 x 54.0 x 13.0mm       |
| 产品重量 | 24.0g                      |
| 包装尺寸 | 132.0 x 95.0 x 16.0mm      |
| 毛重     | 58.0g                      |

## 原理图

Designed by [@akita](https://twitter.com/akita11)

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/typec2grove/@akita.webp" width="5%">

- [Module ExtPort For Core2 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/550/module_ext_port_for_core2_sch.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/550/module_ext_port_for_core2_sch_sch_01.png">
</SchViewer>

## 管脚映射

### HY2.0-4P

其中带 \* 标识的为默认引脚

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.B   | GND   | 5V  | G26    | G36   |
| PORT.C   | GND   | 5V  | G14    | G13   |
| PORT.D   | GND   | 5V  | G35\*  | G34\* |
| PORT.E   | GND   | 5V  | G19\*  | G27\* |
::

> 注意：端口 D/E 的引脚分配可由每个 3p 开关配置为下列分配之一
>
> - PortD-1 (白线) : 34 (默认) / 22 (内部 I2C-SCL) / 3 (RXD0)
> - PortD-2 (黄线) : 35 (默认) / 21 (内部 I2C-SDA) / 1 (TXD0)
> - PortE-1 (白线) : 27 (默认) / 2 (NS4168-DATA) / 0 (NS4168-LRCK)
> - PortE-2 (黄线) : 19 (默认) / 25 / 2 (NS4168-DATA)

<div class="product_pic">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/extport_for_core2/extport_for_core2_grove_01.webp" width="40%">
</div>

### M5-Bus

\#> Switch | 下方 M5-Bus 中标记 `SW` 的引脚，可通过拨码开关进行切换，用于适配不同的主控设备。

::m5-bus-table
| PIN         | LEFT | RIGHT | PIN         |
| ----------- | ---- | ----- | ----------- |
| GND         | 1    | 2     | PORT.D (SW) |
| GND         | 3    | 4     | PORT.B      |
| GND         | 5    | 6     |             |
|             | 7    | 8     | PORT.E (SW) |
|             | 9    | 10    | PORT.B      |
|             | 11   | 12    | 3V3         |
| PORT.D (SW) | 13   | 14    | PORT.D (SW) |
|             | 15   | 16    |             |
| PORT.D (SW) | 17   | 18    | PORT.D (SW) |
| PORT.A | 19 | 20 | PORT.A |\
| PORT.E (SW) | 21 | 22 | PORT.E (SW) |
| PORT.E (SW) | 23 | 24 | PORT.E (SW) |
|             | 25 | 26 | PORT.D (SW) |
|             | 27 | 28 | 5V          |
|             | 29 | 30 |             |
::

### 2.54-5P 排针

| 1       | 2          | 3   | 4   | 5   |
| ------- | ---------- | --- | --- | --- |
| 5V(+5V) | 3V3(+3.3V) | G36 | G26 | GND |

## 尺寸图

[Module ExtPort For Core2 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/976/extportforcore2.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/976/extportforcore2_page_01.png" width="100%">

## PCB

- [Module ExtPort For Core2 KiCad Project](https://github.com/m5stack/M5_Hardware/tree/master/KiCad/Projects/Module_ExtPort_For_Core2)

## 数据手册

- [M5Stackハンズオン資料 From Japanese](https://docs.google.com/presentation/d/11nBajGIhjv-naQnr_dzS9U8Bt7wMfS5UbUuWfKnAS3c/edit?usp=sharing)
