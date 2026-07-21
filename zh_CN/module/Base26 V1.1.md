# Base26 v1.1

<span class="product-sku">SKU:K026-B</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Base26 V1.1/img-1870d519-5c97-46de-8ff5-7b002d23019b.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Base26 V1.1/img-1d3c254d-46fe-4140-9993-e580f0ebb019.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Base26 V1.1/img-0d503cb5-78e0-4803-ae6e-7ae7f7feae1e.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Base26 V1.1/img-f5431338-3f32-4b2d-96d3-7ccf8bad8aad.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Base26 V1.1/img-5e5b1986-6a7a-4519-b61b-c6b379265afc.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Base26 V1.1/img-bce42194-2798-46ca-8d6c-f94574a98122.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Base26 V1.1/img-c2c76857-75ca-428c-8043-f53849e6353f.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Base26 V1.1/img-e7dd6595-0c34-49c8-9554-3e59b44ce899.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Base26 V1.1/img-895d84a6-9e0a-41fe-9f81-ca5175abe0aa.webp">
</PictureViewer>

## 描述

**Base26 v1.1** 是一款 “5 x 5cm 体系” 的通用型功能底座，产品厚度为 26mm (不含母线排针部分)，内含 9 ~ 24V 转 5V 的 DC-DC 电路、2 个自定义 Grove 扩展口、1 个 HT3.96-4P 的接口、1 个侧开的 M12 过孔、3 个侧开的 SMA 天线过孔，以及 PCB 中央 2.54mm 间距的洞洞板区域，用户可以自主添加电路功能。套件中附送 1 个 RS485 转 TTL 的转换板，用户可自行焊接，以此可通过 HT3.96-4P 实现 PWR485 的功能。在结构上预留了多种固定方式，支持 DIN 导轨、挂墙、螺丝固定、底部 M12 接头固定。

## 产品特性

- 内置 9-24V 转 5V DC-DC 电路
- 导轨、挂墙、螺丝以及 M12 固定方式
- 2.54MM 洞洞板
- 包含 2 个 Grove 扩展口
- 自定义添加电路
- PWR485 通讯

## 包装内容

- 1 x Base26 V1.1 Proto Board
- 1 x Base26 V1.1 底座外壳
- 1 x RS485-To-TTL 转接板
- 2 x HY2.0-4P 端子
- 1 x 1.5mm 六角扳手
- 1 x 2.0mm 六角扳手
- 1 x 2.5mm 六角扳手
- 1 x 35mm 银色金属导轨
- 1 x 35mm 黑色导轨卡扣
- 2 x M3\*8mm 螺丝 (沉头，机械牙)
- 2 x M3\*22mm 螺丝 (杯头，机械牙)
- 2 x M3\*35mm 螺丝 (杯头，机械牙)
- 2 x M3\*38mm 螺丝 (杯头，机械牙)
- 2 x M3\*40mm 螺丝 (杯头，机械牙)
- 4 x M2\*5mm 螺丝 (杯头，自攻牙)
- 1 x 电缆接头 (M12)
- 2 x M3 螺母 (带防滑胶圈)
- 1 x 2.54mm-20P 直插排针 (总高 5.32mm)
- 1 x HT3.96-4P 端子
- 1 x 产品贴纸

## 应用场景

- 功能原型开发

## 规格参数

| 规格           | 参数            |
| -------------- | --------------- |
| DC-DC 转换芯片 | MP1584          |
| 输入电压范围   | 9-24V           |
| 持续输出电流   | 2A              |
| 输出电压       | 5V              |
| 产品尺寸       | 54 × 54 × 28mm  |
| 包装尺寸       | 105 × 65 × 40mm |
| 产品重量       | 27.4g           |
| 毛重           | 106.3g          |

## 原理图

- [Base26 v1.1 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/540/Sch_BASE_v1.1.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/540/Sch_BASE_v1.1_sch_01.png">
</SchViewer>

## 管脚映射

### M5-Bus

::m5-bus-table
| PIN       | LEFT | RIGHT | PIN    |
| --------- | ---- | ----- | ------ |
| GND       | 1    | 2     |        |
| GND       | 3    | 4     |        |
| GND       | 5    | 6     | EN     |
|           | 7    | 8     |        |
|           | 9    | 10    |        |
|           | 11   | 12    | 3.3V   |
|           | 13   | 14    |        |
|           | 15   | 16    |        |
| SDA       | 17   | 18    | SCL    |
|           | 19   | 20    |        |
|           | 21   | 22    |        |
|           | 23   | 24    |        |
| HPWR(IN+) | 25   | 26    |        |
| HPWR(IN+) | 27   | 28    | 5V     |
| HPWR(IN+) | 29   | 30    | BAT    |
::

## 数据手册

- [MP1584](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/Base26-B/MP1584.pdf)
