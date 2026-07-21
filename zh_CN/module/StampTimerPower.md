# Stamp Timer Power

<span class="product-sku">SKU:S005</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/StampTimerPower/img-0031c82e-4b0a-4d4d-9649-077dd37b6f83.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/StampTimerPower/img-a9d7ea5a-5b01-4878-9538-05e6b16c9504.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/StampTimerPower/img-d49a08a2-2570-4cb0-9a21-81800f092fa6.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/StampTimerPower/img-8e89ac30-0ece-4977-866d-782da2f4f462.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/StampTimerPower/img-26497b3e-8e17-429b-97e8-1f644765880c.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/StampTimerPower/img-a56fae2e-6182-4ca5-8e34-28b0f3c8dd2c.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/StampTimerPower/img-434ee1c7-2ed8-41ca-a867-790557a33d95.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/StampTimerPower/img-aa26d3a9-4641-473d-aa5c-49f6732689f2.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/StampTimerPower/img-4c5877b1-7ddf-47d4-8b10-90e5d5430334.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1036/S005_Stamp_Timer_Power_weight.jpg">
</PictureViewer>

## 描述

**Stamp Timer Power** 是一款具有 **STAMP 系列封装** 的内置 **RTC 唤醒**的**低功耗电源控制模块**，内部具有**手动唤醒** + **手动休眠** + **RTC 定时唤醒** + **电池充电** + **5V 升压输出** + **3V3 电源输出**等功能，RTC 采用 **BM8563** ，能设定**溢出时间**从而唤醒模块供电。该模块采用 STAMP 封装，可采用 **SMD** 、**DIP** 以及飞线等使用方式，可用作**低功耗产品的电源部分**。

## 产品特性

- 多 IO 引出，支持多种应用形态 (SMT,DIP, 飞线)
- 手动或软件定时唤醒或休眠
- 锂电池充电和 5v 升压
- 3.3V 输出 的 DC-DC 电路

## 包装内容

- 1 x Stamp Timer Power
- 1 x 2.0mm 六角扳手
- 1 x HY2.0-4P 端子

## 应用场景

- 低功耗产品电源部分
- 低功耗定时摄像
- 电池门铃
- 可穿戴设备
- 智能家居

## 规格参数

| 规格             | 参数                                         |
| ---------------- | -------------------------------------------- |
| RTC              | BM8563                                       |
| 电池管理 IC      | TP4057                                       |
| RTC8563 通信接口 | 默认 I2C 通信 @ 0x51 / 0xA2 (写) / 0xA3 (读) |
| IO 接口间距      | 2.54mm                                       |
| 固定螺丝规格     | M2\*4 沉头内六角机械牙                       |
| 工作温度         | 0°C ~ 60°C                                   |
| 产品尺寸         | 20.0 x 20.0 x 5.0mm                          |
| 产品重量         | 2.6g                                         |
| 包装尺寸         | 136.0 x 92.0 x 13.0mm                        |
| 毛重             | 5.8g                                         |

## 原理图

- [Stamp Timer Power 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/571/Sch_StampTimerPower_v1.2.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/571/Sch_StampTimerPower_v1.2_sch_01.png">
</SchViewer>

## 尺寸图

- [Stamp Timer Power 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1036/S005-model-size-STAMP-Timerpower.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1036/S005-model-size-STAMP-Timerpower_page_01.png" width="100%">

## 数据手册

- [BM8563](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/Stamp/StampTimerPower/RTC8563.pdf)
- [TP4057](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/Stamp/StampTimerPower/tp4057.PDF)

## 软件开发

### Arduino

- [Stamp Timer Power Arduino Example](https://github.com/m5stack/M5Stamp-TimerPower)

### UiFlow1

<img src="https://static-cdn.m5stack.com/resource/docs/products/module/StampTimerPower/uiflowCase-1672829385864aa.png" width="100%"/>
