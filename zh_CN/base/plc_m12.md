# Base PLC-M12

<span class="product-sku">SKU:K011-B</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/plc_m12/plc_m12_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/plc_m12/plc_m12_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/plc_m12/plc_m12_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/plc_m12/plc_m12_04.webp">
</PictureViewer>

## 描述

**Base PLC-M12** 是一款工业控制底座。它覆盖工业级外壳，专为工控领域设计，与典型工控 PLC（可编程逻辑控制器）有所不同，有着更加紧凑的外观设计。在实现基础工控功能的同时，能维持控制器低功耗。基于 M5 开发体系，用户可根据需求添加任意数量的继电器开关，并且该底座支持 TTL/RS485 通信。它还支持功能模块堆叠拓展，例如堆叠 LoRa 模块，可使 PLC 成为一个 LoRa 通信节点。此外，底座提供 PLC - Proto 板，方便进行后续电路拓展设计。通过不同的硬件堆叠与拓展设计，它能够满足工业级应用场景的各种定制化需求。因此，**Base PLC-M12** 底座会是工控项目的完美解决方案。

## 产品特性

- 电压输入范围：9 ~ 24V

## 包装内容

- 1 x PLC Proto Board
- 1 x PLC 底座外壳
- 1 x RS485-To-TTL 转接板
- 1 x HT3.96-7P 端子
- 1 x HT3.96-4P 端子
- 1 x 1.5mm 六角扳手
- 1 x 2.0mm 六角扳手
- 1 x 2.5mm 六角扳手
- 10 x 2mm 冷压端子
- 1 x 磁铁 (中间带孔，直径 15mm，3mm 厚)
- 1 x 35mm 银色金属导轨
- 1 x 35mm 黑色导轨卡扣
- 1 x M3\*6mm 螺丝 (沉头，机械牙)
- 2 x M3\*28mm 螺丝 (杯头，机械牙)
- 4 x M2\*5mm 螺丝 (杯头，自攻牙)
- 1 x 电缆接头 (M12)
- 1 x 2.54mm-20P 直插排针 (总高 5.32mm)
- 1 x 产品贴纸

## 规格参数

| 规格     | 参数            |
| -------- | --------------- |
| 产品重量 | 25g             |
| 毛重     | 133g            |
| 产品尺寸 | 54 x 54 x 28mm  |
| 包装尺寸 | 105 x 65 x 40mm |

## 操作说明

如果需要添加 RS485 通信接口，请将 TTL-RS485 转接板与配套排针焊接到主板上相应的引脚上。TTL-RS485 转接板的串口引脚将连接到 PLC 底座的 G16 和 G17。

### RS485 拓展板安装

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1001/K011-B-Operate_01.jpg" width="80%">

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/base/plc_m12/plc_m12_sch_01.webp" width="80%">

## 管脚映射

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

## 尺寸图

- [Base PLC-M12 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1001/K011-B-BASE-PLC-M12.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1001/K011-B-BASE-PLC-M12_page_01.png" width="100%">

## 相关视频

**RS485 通信**

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Blog/Twitch201901/RS485%20Application.mp4" type="video/mp4">
</video>

## 版本变更

| 上市日期 | 产品变动       | 备注     |
| -------- | -------------- | -------- |
| /        | 首次发售       | /        |
| 2023     | 升级至版本 1.1 | 增删配件 |
