# Base15

<span class="product-sku">SKU:K025</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/base15/base15_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/base15/base15_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/base15/base15_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/base15/base15_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/base15/base15_05.webp">
</PictureViewer>

## 描述

**Base15** 是 M5 体系中一款支持高度定制化的工业底座。与 PLC Base 有着类似，却有着更高级别定制化能力。套件内提供了 Protoboard（万能板）允许您添加自己的电路设计，并预留了两个 Grove 接口焊盘，方便您进行线路的拓展。提供 M 型防水接头组件，允许用户将其安装在底座的侧面或是底部。

**Base15** 中 “15” 代号来源于底座的高度 15cm，底座上每一侧都是可以自由拆卸、切割、定制成不同的接口，以满足不同需求。关于底座的定制，我们提供了大量的结构组件替代方案，并将其完全开源，你可以基于这些设计去制作 3D 打印文件或是二次设计。不但如此，该底座完全兼容 M5 堆叠模块与硬件拓展体系。在产品的底部，我们提供了 2 种不同的装配方式：导轨固定，悬挂固定。

底座覆盖工业级外壳，自由拼接的组件能够为您提供无限的组合方式，为您创造出功能强大且可靠的工业应用。对于面向工业场景，要求一定的防护水准且希望项目高度定制化的开发者用户来说，**Base15** 是一个很好的解决方案。

## 产品特性

- 支持高度定制化
- 可替换部件
- M5-Bus 拓展
- 板载 DC-DC 转换 (9 ~ 24V -> 5V)
- 2 种底座固定方式

## 包装内容

- 1 x Base15 Proto Board
- 1 x Base15 底座外壳
- 2 x HY2.0-4P 端子
- 1 x 1.5mm 六角扳手
- 1 x 2.0mm 六角扳手
- 1 x 2.5mm 六角扳手
- 1 x 35mm 银色金属导轨
- 1 x 35mm 黑色导轨卡扣
- 2 x M3\*8mm 螺丝 (沉头，机械牙)
- 2 x M3\*22mm 螺丝 (杯头，机械牙)
- 4 x M2\*5mm 螺丝 (杯头，自攻牙)
- 2 x M3 螺母 (带防滑胶圈)
- 1 x 产品贴纸

## 规格参数

| 规格     | 参数                  |
| -------- | --------------------- |
| 产品尺寸 | 54.0 x 54.0 x 15.0mm  |
| 产品重量 | 21.0g                 |
| 包装尺寸 | 125.0 x 67.0 x 23.0mm |
| 毛重     | 116.0g                |

## 原理图

- [Base15 原理图PDF](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/schematic/Bases/BASE15.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1002/K025-BASE15_page_01.png" width="100%">

## 管脚映射

### M5-Bus

::m5-bus-table
| PIN  | LEFT | RIGHT | PIN |
| ---- | ---- | ----- | --- |
| GND  | 1    | 2     | NC  |
| GND  | 3    | 4     | NC  |
| GND  | 5    | 6     | EN  |
| NC   | 7    | 8     | NC  |
| NC   | 9    | 10    | NC  |
| NC   | 11   | 12    | 3V3 |
| NC   | 13   | 14    | NC  |
| NC   | 15   | 16    | NC  |
| SDA  | 17   | 18    | SCL |
| NC   | 19   | 20    | NC  |
| NC   | 21   | 22    | NC  |
| NC   | 23   | 24    | NC  |
| HPWR | 25   | 26    | NC  |
| HPWR | 27   | 28    | 5V  |
| HPWR | 29   | 30    | BAT |
::

## 尺寸图

- [Base15 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1002/K025-model-base15.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1002/K025-model-base15_page_01.png" width="100%">

## 结构文件

- [Base15 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/K025_Base15/Structures)
