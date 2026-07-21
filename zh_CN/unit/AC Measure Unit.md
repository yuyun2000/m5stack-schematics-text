# Unit AC Measure

<span class="product-sku">SKU:U164</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/AC Measure Unit/img-28a2411d-d63c-4596-b474-2db9d9b6dcc5.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/AC Measure Unit/img-1f6bc1cb-ebd7-4c63-9403-6c7023ecc346.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/744/U164-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/AC Measure Unit/img-3f28e3b3-3d07-4827-8f1d-60c90d9e2ce8.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/AC Measure Unit/img-b85fd4e6-389e-4779-a83f-621c8f8facb1.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/AC Measure Unit/img-11424b2a-bb96-434f-88dd-bac95dcd0f32.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/AC Measure Unit/img-ef2918e9-33ec-4816-92fd-ba89fc7c5aa4.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/AC Measure Unit/img-a84a5e0d-736a-4fc3-a4b3-265109d418ab.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/AC Measure Unit/img-b5431cb2-ce5a-425e-b4b3-f18096b3c896.webp">
</PictureViewer>

## 描述

**Unit AC Measure**是一款带隔离的单相交流电测量单元，采用**STM32 + HLW8032**的方案，可实时监测高精度的电流、电压、功率等数据。它内置交流电隔离芯片 B0505ST16-W5，并通过 EL357 光耦隔离芯片与 STM32 通讯。用户可通过 I2C 通讯的方式读取测量的数据。本产品适用于供电信息采集、远程智能家电产品等领域。

## 注意事项

?> 输入电压 | 测量输入电压工作范围：必须是 AC 100~240V@10A，否则设备无法正常工作。

## 产品特性

- STM32G030@M0+ 32-bit MCU，64 KB Flash，8 KB RAM
- 单相交流电 100-240V/10A 测量
- I2C 通讯 (0x42)
- 编程平台：UiFlow、Arduino

## 包装内容

- 1 x Unit AC Measure
- 1 x HY2.0-4P Grove 线 (20cm)
- 1 x 3.96-4P 端子

## 应用场景

- 智能家电产品
- 计量插座
- 智能 WIFI 插座
- 电动车充电桩
- 路灯控制系统

## 规格参数

| 规格            | 参数                  |
| --------------- | --------------------- |
| MCU             | STM32G030F6P6         |
| 交流电采集芯片  | HLW8032               |
| 隔离芯片        | B0505ST16-W5          |
| 光耦通讯芯片    | EL357NB               |
| 通信接口        | I2C 通信 @ 0x42       |
| 测量电压 / 电流 | AC 100 ~ 240V@10A     |
| 产品尺寸        | 56.0 x 24.0 x 10.3mm  |
| 产品重量        | 8.4g                  |
| 包装尺寸        | 138.0 x 93.0 x 11.3mm |
| 毛重            | 16.9g                 |

## 原理图

- [Unit AC Measure 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/619/SCH_UNIT_AC_Measure_V1.01.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/619/SCH_UNIT_AC_Measure_V1.01_sch_01.png">
</SchViewer>

## 管脚映射

### Unit AC Measure

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

### AC 电源端子接线

::grove-table
| HT3.96-4P | L1       | N1          | L2       | N2          |
| --------- | -------- | ----------- | -------- | ----------- |
| 端子      | 线路 (L) | 接地 (PE)   | 线路 (L) | 零线 (N)    |
::

<img
src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/744/connector.png"
width="40%"
/>

## 尺寸图

<img alt="module size" src="https://static-cdn.m5stack.com/resource/docs/products/unit/AC Measure Unit/img-9b8c7dfb-082c-4136-8aa8-dd395c2f12fd.png" width="100%" />

## 数据手册

- [B0505ST16-W5](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/AC%20Measure%20Unit/B0505ST16-W5.PDF)
- [EL357NB](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/AC%20Measure%20Unit/EL357NB.PDF)
- [HLW8032](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/AC%20Measure%20Unit/HLW8032.PDF)
- [STM32G030](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/AC%20Measure%20Unit/STM32G030.PDF)
- [I2C protocol](https://github.com/m5stack/M5Unit-ACMeasure/blob/main/docs/Unit_ACMeasure_I2C_Protocol.pdf)

## 软件开发

### Arduino

- [Unit AC Measure 驱动库](https://github.com/m5stack/M5Unit-ACMeasure)

### UiFlow1

- [Unit AC Measure UiFlow1 文档](/zh_CN/uiflow/blockly/unit/ac_measure)
- [Unit AC Measure UiFlow1 测试程序](https://flow.m5stack.com/?examples=unit_acmeasure_demo)

### UiFlow2

- [Unit AC Measure UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/ac_measure.html)

### Home Assistant

- [Unit AC Measure Home Assistant 集成](/zh_CN/homeassistant/sensor/unit_ac_measure)

### 内置固件

- [Unit AC Measure 内置固件](https://github.com/m5stack/M5Unit-ACMeasure-Internal-FW)

### 通信协议

- [Unit AC Measure I2C 通信协议](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/744/UnitACMeasure.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/744/SCH_UNIT_AC_Measure_V1.01_sch_01.png" width="100%">

### EasyLoader

| Easyloader                 | 下载链接                                                                                                                                     | 备注 |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ---- |
| Unit AC Measure Easyloader | [download](https://static-cdn.m5stack.com/resource/docs/products/unit/AC%20Measure%20Unit/ezLoader-de7322a6-ce1b-4558-a0c5-879a134878da.exe) | /    |
