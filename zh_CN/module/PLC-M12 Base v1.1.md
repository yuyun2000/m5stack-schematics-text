# Base PLC-M12 v1.1

<span class="product-sku">SKU:K011-B-V11</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/PLC-M12 Base v1.1/img-6694a5a7-ab13-44e2-ba3c-b319e6169c7a.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/PLC-M12 Base v1.1/img-ad1a2863-1e78-4db5-958c-1e652efe991b.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/PLC-M12 Base v1.1/img-31e1e0bd-6741-42d6-9229-cccaa8fe9348.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/PLC-M12 Base v1.1/img-7b0ce76b-6371-4fa6-9bf7-dfab071ccd24.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/PLC-M12 Base v1.1/img-2bdcec81-6c23-41f3-9da2-aa2e423d06dd.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/PLC-M12 Base v1.1/img-445ccf47-842f-483d-b005-8f83f35ac8ee.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/PLC-M12 Base v1.1/img-b103cd10-29cd-4ee6-9d43-77e54e1df4bf.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/PLC-M12 Base v1.1/img-e1a0b283-747c-49c0-b63e-67ed3d7248a5.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/PLC-M12 Base v1.1/img-8571ee57-6c37-4d88-92e4-e28e86923274.webp">
</PictureViewer>

## 描述

**Base PLC-M12 v1.1** 是一款工业控制底座。覆盖工业级外壳，专为工控领域设计，与典型工控 PLC (可编程逻辑控制器) 有所不同。有着更加紧凑的外观设计，在实现基础工控功能的同时，维持控制器低功耗。基于 M5 开发体系，你可以根据需求添加任意数量的继电器开关，并且支持 TTL-RS485 通信。支持功能模块堆叠拓展，如堆叠 LoRa 模块，使 PLC 成为一个 LoRa 通信节点。提供 PLC-Proto 板，方便进行后续电路拓展设计。通过不同的硬件堆叠与拓展设计，满足工业级应用场景的各种定制化需求。**Base PLC-M12 v1.1** 底座会是工控项目的完美解决方案。

## 产品特性

- 电压输入范围：DC 9 ~ 24V

## 包装内容

- 1 x PLC Proto Board
- 1 x PLC 底座外壳
- 1 x RS485-To-TTL 转接板
- 1 x HT3.96-4P 端子
- 2 x HT3.96-3P 端子
- 1 x 1.5mm 六角扳手
- 1 x 2.0mm 六角扳手
- 1 x 2.5mm 六角扳手
- 10 x 2mm 冷压端子
- 1 x 磁铁 (中间带孔，直径 15mm，3mm 厚)
- 1 x 35mm 银色金属导轨
- 1 x 35mm 黑色导轨卡扣
- 2 x M3\*28mm 螺丝 (杯头，机械牙)
- 4 x M2\*5mm 螺丝 (杯头，自攻牙)
- 1 x 电缆接头 (M12)
- 1 x 2.54mm-20P 直插排针 (总高 5.32mm)
- 1 x 产品贴纸

## 规格参数

| 规格     | 参数            |
| -------- | --------------- |
| 产品尺寸 | 54 x 54 x 28mm  |
| 包装尺寸 | 105 x 65 x 40mm |
| 产品重量 | 25g             |
| 毛重     | 133g            |

## 操作说明

### RS485 拓展板安装

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1001/K011-B-Operate_01.jpg" width="80%">

## 原理图

<SchViewer>
<img alt="schematics" src="https://static-cdn.m5stack.com/resource/docs/products/module/PLC-M12 Base v1.1/img-ebfb57a0-ba41-414a-a0b7-231f89daae07.webp"/>
<img alt="schematics" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/PLC-M12%20Base%20v1.1/rs485%E5%8E%9F%E7%90%86%E5%9B%BE.png"/>
</SchViewer>

## 管脚映射

### RS485 管脚映射

| M5Core | RXD(G16)  | TXD(G17)  | 5V  | GND |
| ------ | --------- | --------- | --- | --- |
| RS485  | RS485 RXD | RS485 TXD | 5V  | GND |

### M5-Bus

::m5-bus-table
| PIN      | LEFT | RIGHT | PIN      |
| -------- | ---- | ----- | -------- |
| GND      | 1    | 2     | NC       |
| GND      | 3    | 4     | NC       |
| GND      | 5    | 6     | NC       |
| NC       | 7    | 8     | NC       |
| NC       | 9    | 10    | NC       |
| NC       | 11   | 12    | 3V3      |
| NC       | 13   | 14    | NC       |
| RS485_TX | 15   | 16    | RS485_RX |
| NC       | 17   | 18    | NC       |
| NC       | 19   | 20    | NC       |
| NC       | 21   | 22    | NC       |
| NC       | 23   | 24    | NC       |
| HPWR     | 25   | 26    | NC       |
| HPWR     | 27   | 28    | 5V       |
| HPWR     | 29   | 30    | BAT      |
::

## 版本变更

| 上市日期 | 产品变动       | 备注     |
| -------- | -------------- | -------- |
| 2023     | 升级至版本 1.1 | 增删配件 |
| /        | 首次发售       | /        |
