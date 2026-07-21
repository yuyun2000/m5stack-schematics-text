# Base M5GO Bottom

<span class="product-sku">SKU:A014</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/m5go_bottom/m5go_bottom_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/m5go_bottom/m5go_bottom_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1006/A014_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/m5go_bottom/m5go_bottom_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/m5go_bottom/m5go_bottom_04.webp">
</PictureViewer>

## 描述

**Base M5GO Bottom** 是一款 Core 增强型通用底座，兼容 Core 各型号主机。相比基础型 [Core Bottom](/zh_CN/base/core_bottom) 而言，增强型底座配备了更大容量的锂电池（500 mAh），内部集成麦克风、LED 灯条、红外 LED，并拓展出两个 HY2.0-4P 接口（PORT.B/PORT.C）等。其背面兼容乐高孔，同时引出 pogo pin 可用于连接支持的 I2C 设备（如 BALA）或磁吸式充电底座。

## 产品特性

- 兼容 Core
- 集成 Mic/LED 灯条 / HY2.0-4P 接口
- 兼容乐高积木
- 可配置磁吸充电底座
- 底座内置 10 个 RGB LED

## 包装内容

- 1 x Base M5GO Bottom
- 2 x M3x16 螺丝

## 规格参数

| 规格     | 参数                 |
| -------- | -------------------- |
| 产品尺寸 | 54.0 x 54.0 x 15.0mm |
| 产品重量 | 32.7g                |
| 包装尺寸 | 132 x 95 x 16mm      |
| 毛重     | 50.6g                |

## 原理图

[Base M5GO Bottom 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1006/A014_Sch_M5GO.pdf)

<SchViewer>
<img alt="schematics" src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1006/A014_Sch_M5GO_page_01.png" width="100%"/>
</SchViewer>

## 管脚映射

### Base M5GO Bottom

| Basic            | G13   | G15     | G34 | G22 | G21 |
| ---------------- | ----- | ------- | --- | --- | --- |
| Base M5GO Bottom | IR TX | LED Pin | MIC | SCL | SDA |

### HY2.0-4P

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.B   | GND   | 5V  | G26    | G36   |
| PORT.C   | GND   | 5V  | G17    | G16   |
::

### M5-Bus

::m5-bus-table
| PIN          | LEFT | RIGHT | PIN          |
| -------      | ---- | ----- | -------      |
| GND          | 1    | 2     | NC           |
| GND          | 3    | 4     | PORT.B       |
| GND          | 5    | 6     | NC           |
| NC           | 7    | 8     | NC           |
| NC           | 9    | 10    | PORT.B       |
| NC           | 11   | 12    | NC           |
| NC           | 13   | 14    | NC           |
| UART_RX      | 15   | 16    | UART_TX      |
| POGO_PIN_SDA | 17   | 18    | POGO_PIN_SCL |
| NC           | 19   | 20    | NC           |
| NC           | 21   | 22    | IR_TX        |
| RGB LED      | 23   | 24    | NC           |
| NC           | 25   | 26    | MIC          |
| NC           | 27   | 28    | 5V           |
| NC           | 29   | 30    | BAT          |
::

## 尺寸图

<img alt="module size" src="https://static-cdn.m5stack.com/resource/docs/products/module/M5GO3 Bottom/img-c2558938-5e94-482b-9c59-02df14bb3088.jpg" width="100%" />

## 产品对比

::compare-table
| 产品对比表 | [Base M5GO Bottom](/zh_CN/base/m5go_bottom) ![Base M5GO Bottom](https://static-cdn.m5stack.com/resource/docs/products/base/m5go_bottom/m5go_bottom_cover_01.webp) | [Base M5GO Bottom2](/zh_CN/base/m5go_bottom2) ![Base M5GO Bottom2](https://static-cdn.m5stack.com/resource/docs/products/base/m5go_bottom2/m5go_bottom2_cover_01.webp) | [Base M5GO Bottom3](/zh_CN/module/M5GO3%20Bottom) ![Base M5GO Bottom3](https://static-cdn.m5stack.com/resource/docs/products/module/M5GO3%20Bottom/img-911850a0-1162-493a-8e2f-fa6493b6a9af.webp) |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Core       | Basic (Core)                                                                                                                                                      | Core2                                                                                                                                                                  | CoreS3                                                                                                                                                                                            |
| RGB        | 10*SK6812                                                                                                                                                         | 10*SK6812                                                                                                                                                              | 10\*WS2812                                                                                                                                                                                        |
| IMU        | /                                                                                                                                                                 | MPU6886                                                                                                                                                                | /                                                                                                                                                                                                 |
| IR         | IR                                                                                                                                                                | /                                                                                                                                                                      | IR                                                                                                                                                                                                |
| BATTERY    | 500mAh                                                                                                                                                            | 500mAh                                                                                                                                                                 | 500mAh                                                                                                                                                                                            |
| MIC        | SPQ2410                                                                                                                                                           | SPM1423                                                                                                                                                                | /                                                                                                                                                                                                 |
::
