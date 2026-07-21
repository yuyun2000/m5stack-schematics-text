# Base BTC

<span class="product-sku">SKU:A011/A011-B</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/btc_base/btc_base_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/btc_base/btc_base_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1000/A011-B-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/btc_base/btc_base_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/btc_base/btc_base_06.webp">
</PictureViewer>

## 描述

**Base BTC** 是一款环境数据检测底座，内置 SHT30 温湿度传感器，可精准测量温湿度数据。采用排母插接设计，通过 Base Bottom 排针与核心主控连接并通信，适用于构建个人桌面环境数据检测显示系统。

## 产品特性

- 内置 SHT30 温湿度传感器
- 高测量精度
- I2C 通信接口

## 包装内容

- 1 x Base BTC
- 1 x USB Type-C 连接线 (1m)
- 2 x M3 \* 16 螺丝
- 1 x 内六角扳手 L 形 2.5mm (适配 M3 螺丝)

## 应用场景

- 室内环境监测系统
- 智能家居联动设备
- 教学实验平台
- 小型气象站

## 规格参数

| 规格                | 参数                   |
| ------------------- | ---------------------- |
| 最大温度测量范围    | -40 ~ 120 ℃            |
| 最高测量精度        | 0 ~ 60 ℃/±0.2℃         |
| 湿度测量范围 / 误差 | 10 ~ 90 % RH / ±2%     |
| 产品尺寸            | 55.0 x 47.0 x 23.0mm   |
| 产品重量            | 9.2g                   |
| 包装尺寸            | 170.0 x 120.0 x 21.0mm |
| 毛重                | 60.0g                  |

## 操作说明

### 充电说明

当搭配 Basic 等 Core 一代主控机型使用时：

- Base BTC 底座的 USB 接口仅为主控设备供电。
- 如需为 Base Bottom 内置锂电池充电，请连接主控设备上的 USB 接口。

### I2C 地址冲突

- 请勿在 I2C 总线额外扩展包含 SHT30 相同 I2C 地址（0x44）的传感器，否则将因地址冲突导致设备无法正常工作。

## 原理图

- [Base BTC 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1000/A011-Sch_BTC_v2.1.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1000/A011-Sch_BTC_v2.1_page_01.png">
</SchViewer>

## 管脚映射

### SHT30

| Basic | G22 | G21 | 3V3 | GND |
| ----- | --- | --- | --- | --- |
| SHT30 | SCL | SDA | 3V3 | GND |

### M5-Bus

::m5-bus-table
| PIN     | LEFT | RIGHT | PIN     |
| ------- | ---- | ----- | ------- |
| NC      | 1    | 2     | NC      |
| NC      | 3    | 4     | NC      |
| NC      | 5    | 6     | NC      |
| NC      | 7    | 8     | NC      |
| NC      | 9    | 10    | NC      |
| NC      | 11   | 12    | NC      |
| NC      | 13   | 14    | NC      |
| NC      | 15   | 16    | NC      |
| I2C_SDA | 17   | 18    | I2C_SCL |
| NC      | 19   | 20    | NC      |
| NC      | 21   | 22    | NC      |
| NC      | 23   | 24    | NC      |
| NC      | 25   | 26    | NC      |
| NC      | 27   | 28    | 5V      |
| NC      | 29   | 30    | BAT     |
::

## 尺寸图

- [Base BTC 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1000/A011-B-BASE-BTC.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1000/A011-B-BASE-BTC_page_01.png" width="100%">

## 数据手册

- [DHT12 datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/hat/DHT12_en.pdf)
- [SHT30 datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/SHT3x_Datasheet_digital.pdf)

## 软件开发

### Arduino

- [Base BTC SHT30 案例程序](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/Base/BTC/Arduino/BTC2.1)
- [Base BTC DHT12 案例程序](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/Base/BTC/Arduino/BTC)

## 版本变更

| 上市日期 | 产品变动           |
| -------- | ------------------ |
| 2020.5   | DHT12 修改为 SHT30 |
| 2017.7   | 首次发售           |
