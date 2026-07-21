# Base15 v1.1

<span class="product-sku">SKU:K025-B</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Base15 V1.1/img-b4dbf15a-b5d9-472f-9342-c398f7989a29.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Base15 V1.1/img-80c8327a-9767-4870-aa05-bf3c5a2506fd.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Base15 V1.1/img-454544e9-fa16-4f07-a999-0650f9531212.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Base15 V1.1/img-130d8088-23da-463a-a610-f9463a635576.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Base15 V1.1/img-c02ded07-e3d2-4cdb-a0d5-59187c371f67.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Base15 V1.1/img-a350663b-0dec-4946-84fa-dbc8a1514589.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Base15 V1.1/img-e194b82c-2def-401d-b485-03181b6308a3.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Base15 V1.1/img-cba52ce0-7b83-4286-a7d3-33301f191355.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Base15 V1.1/img-05b01a4d-573c-437b-8564-ee4920beec65.webp">
</PictureViewer>

## 描述

**Base15 v1.1** 是一款 “5 x 5cm 体系” 的通用型功能底座，产品厚度为 15 mm (不含母线排针部分)，内含 9 ~ 24V 转 5V 的 DC/DC 电路和 2 个自定义 Grove 扩展口，以及 PCB 中央 2.54mm 间距的洞洞板区域，用户可以自主添加电路功能。在结构上预留了多种固定方式，支持 DIN 导轨、挂墙、螺丝固定、底部 M12 接头固定。

## 产品特性

- 内置 9-24V 转 5V DC-DC 电路
- 导轨、挂墙、螺丝以及 M12 固定方式
- 2.54MM 洞洞板
- 包含 2 个 Grove 扩展口
- 自定义添加电路

## 包装内容

- 1 x Base15 V1.1 Proto Board
- 1 x Base15 V1.1 底座外壳
- 2 x HY2.0-4P 端子
- 1 x 1.5mm 六角扳手
- 1 x 2.0mm 六角扳手
- 1 x 2.5mm 六角扳手
- 1 x 35mm 银色金属导轨
- 1 x 35mm 黑色导轨卡扣
- 2 x M3\*8mm 螺丝 (沉头，机械牙)
- 2 x M3\*22mm 螺丝 (杯头，机械牙)
- 2 x M3\*25mm 螺丝 (杯头，机械牙)
- 2 x M3\*28mm 螺丝 (杯头，机械牙)
- 2 x M3\*30mm 螺丝 (杯头，机械牙)
- 4 x M2\*5mm 螺丝 (杯头，自攻牙)
- 2 x M3 螺母 (带防滑胶圈)
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
| 产品重量       | 27.1g           |
| 毛重           | 133.7g          |

## 原理图

- [Base15 v1.1 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/539/Sch_BASE_v1.1.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/539/Sch_BASE_v1.1_sch_01.png">
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
