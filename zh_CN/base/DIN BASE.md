# Base DIN

<span class="product-sku">SKU:M132</span>

<PictureViewer>
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/base/DinBase/DinBase_01.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/base/DinBase/DinBase_02.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/base/DinBase/DinBase_03.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/base/DinBase/DinBase_04.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/base/DinBase/DinBase_05.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/base/DinBase/DinBase_06.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/base/DinBase/DinBase_07.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/base/DinBase/DinBase_08.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/base/DinBase/DinBase_09.webp">
</PictureViewer>

## 描述

**Base DIN** 是专为 “DinRail” 导轨固定而设的一种 “5X5cm” 系列底座。适用于 **M5Core 主机**，内置 500 mAh 锂电池，可外部输入 DC 电源（支持 9 ~ 24V），板载电源物理开关，可以彻底关断外部电源和电池。预留 PORT.B、PORT.C 接口。下侧方设有乐高安装孔方便固定，底部支持标准 35 mm Din 导轨，另外提供了 4 个插拔式挂耳，支持多样固定方式。**Base DIN** 内部 PCB 上预留了多处 proto 焊盘，方便用户 DIY。

## 产品特性

- 1X12P 2.54 接口
- Port.B、Port.C 接口
- 供电方式：
  - DC 电源 (9 ~ 24V)
  - 500mAh 锂电池
- 电源开关
- 多种固定方式:
  - DinRail
  - 挂耳
  - 底部内嵌两个铜螺母
  - 侧面预留三个乐高固定孔

## 包装内容

- 1 x Base DIN
- 4 x 挂耳
- 1 x 卡扣
- 1 x 内六角扳手 L 形 2.5mm (适配 M3 螺丝)
- 2 x M3 * 20mm 螺丝 (杯头，机械牙)
- 2 x M3 * 22mm 螺丝 (杯头，机械牙)
- 2 x M3 * 25mm 螺丝 (杯头，机械牙)

## 应用场景

- DIY 制作
- Core 等主机单独供电场景

## 规格参数

| 规格           | 参数                 |
| -------------- | -------------------- |
| DC-DC 降压芯片 | SY8303AIC            |
| 锂电池充电芯片 | TP4057               |
| DC 外接电源    | DC 9 ~ 24V           |
| 锂电池容量     | 500mAh               |
| 产品尺寸       | 54.0 x 54.0 x 22.5mm |
| 产品重量       | 32.4g                |
| 包装尺寸       | 95.0 x 66.0 x 26.0mm |
| 毛重           | 64.5g                |

## 原理图

- [Base DIN 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/559/SCH_DinBase_V1.1.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/559/SCH_DinBase_V1.1_sch_01.png">
</SchViewer>

## 管脚映射

### HY2.0-4P with Core

::grove-table
| HY2.0-4P | Black | Red | Yellow        | White         |
| -------- | ----- | --- | ------------- | ------------- |
| PORT.B   | GND   | 5V  | G26           | G36           |
| PORT.C   | GND   | 5V  | UART_TX / G17 | UART_RX / G16 |
::

### HY2.0-4P with Core2

::grove-table
| HY2.0-4P | Black | Red | Yellow        | White         |
| -------- | ----- | --- | ------------- | ------------- |
| PORT.B   | GND   | 5V  | G26           | G36           |
| PORT.C   | GND   | 5V  | UART_TX / G14 | UART_RX / G13 |
::

### HY2.0-4P with CoreS3

::grove-table
| HY2.0-4P | Black | Red | Yellow        | White         |
| -------- | ----- | --- | ------------- | ------------- |
| PORT.B   | GND   | 5V  | G9            | G8            |
| PORT.C   | GND   | 5V  | UART_TX / G17 | UART_RX / G18 |
::

### M5-Bus

::m5-bus-table
| PIN    | LEFT | RIGHT | PIN    |
| ------ | ---- | ----- | ------ |
| GND    | 1    | 2     | NC     |
| GND    | 3    | 4     | PORT.B |
| GND    | 5    | 6     | NC     |
| NC     | 7    | 8     | NC     |
| NC     | 9    | 10    | PORT.B |
| NC     | 11   | 12    | NC     |
| NC     | 13   | 14    | NC     |
| PORT.C | 15   | 16    | PORT.C |
| NC     | 17   | 18    | NC     |
| NC     | 19   | 20    | NC     |
| NC     | 21   | 22    | NC     |
| NC     | 23   | 24    | NC     |
| HPWR   | 25   | 26    | NC     |
| HPWR   | 27   | 28    | 5V     |
| HPWR   | 29   | 30    | BAT    |
::

## 尺寸图

<img  src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/base/DinBase/%E5%B0%BA%E5%AF%B8%E5%9B%BE.png" width="100%" />

## 结构文件

- [Base DIN 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/M132_Base_DIN/Structures)

## 数据手册

- [Power Manager TP4057](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/base/DinBase/TP4057.PDF)
- [SY8303AIC](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/base/DinBase/SY8303AIC.PDF)
