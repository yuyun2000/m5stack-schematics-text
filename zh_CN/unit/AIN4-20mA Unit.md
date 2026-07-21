# Unit AIN4-20mA

<span class="product-sku">SKU:U162</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/AIN4-20mA Unit/img-a7fb07ad-7fd6-47f8-b333-2f55250f73a7.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/AIN4-20mA Unit/img-3edfd1af-26f2-41e4-82cd-2050ac7e1177.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/743/U162-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/AIN4-20mA Unit/img-4aeda38e-39f1-4992-9895-db4f28c456c5.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/AIN4-20mA Unit/img-9556cbf3-2c0d-4237-a79a-54fd747a713c.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/AIN4-20mA Unit/img-af108373-8241-4541-97eb-cb1f73619a1c.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/AIN4-20mA Unit/img-840cdc66-58ee-43e9-87b2-2c8f06dd8072.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/AIN4-20mA Unit/img-8361c9d7-92a9-4e99-a327-fba36ad5991a.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/AIN4-20mA Unit/img-323b3160-5967-4853-b3ec-a4b5676381b3.webp">
</PictureViewer>

## 描述

**Unit AIN4-20mA**是一款**单通道**4~20mA 电流模拟量测量单元。它采用了**STM32G030F6**主控芯片，与 M5 主机通过**I2C**进行通讯。支持通过跳线帽切换为由内部或外部供电的接线方式。板载电源隔离芯片和内置运放电路，能准确地测量外部电流传感器，确保信号的准确性和系统的安全性。适用于电力系统设备监测、电机控制、能源管理以及自动化和工业过程控制等领域。

## 产品特性

- STM32
- I2C 通讯
- 支持 2 或 4 线制传感器，跳线帽切换
- 内置电气隔离芯片
- 支持 Arduino、UiFlow 等编程平台

## 包装内容

- 1 x Unit AIN4-20mA
- 1 x HT3.96-4P 端子
- 1 x HY2.0-4P Grove 连接线 (20cm)
- 3 x 跳线帽

## 应用场景

- 电力系统设备监测
- 电机控制
- 能源管理
- 自动化和工业过程控制

## 规格参数

| 规格                        | 参数                  |
| --------------------------- | --------------------- |
| MCU                         | STM32G030F6P6         |
| 信号隔离芯片                | HCNR200               |
| 运放芯片                    | SGM321YC5/TR          |
| 通信接口                    | I2C 通信 @ 0x55       |
| IN + 与 IN - 输入阻抗典型值 | 200Ω                  |
| 工作温度                    | 0 ~ 40°C              |
| 产品尺寸                    | 56.0 x 24.0 x 11.3mm  |
| 产品重量                    | 8.8g                  |
| 包装尺寸                    | 138.0 x 93.0 x 12.3mm |
| 毛重                        | 17.1g                 |

## 操作说明

### 跳线帽的接法与说明

- 使用**无源电流型传感器**时，请连接 DC 24V 供电输入，传感器信号接入 IN+, IN- ， 并将跳线帽调整为下图所示：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/743/unit_ain4_20ma_passive_sensor_connect_01.png" width="80%">

- 使用**有源电流型传感器**时，传感器信号接入 IN+, IN- ，并将跳线帽调整为下图所示：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/743/unit_ain4_20ma_active_sensor_connect_01.png" width="80%">

## 原理图

- [Unit AIN4-20mA 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/617/SCH_UNIT_AIN4-20mA_V1.01.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/617/SCH_UNIT_AIN4-20mA_V1.01_sch_01.png">
</SchViewer>

## 管脚映射

### Unit AIN4-20mA

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 尺寸图

<img alt="module size" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/AIN4-20mA%20Unit/%E5%B0%BA%E5%AF%B8%E5%9B%BE.png" width="100%" />

## 数据手册

- [STM32G030F6 Datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/U162%20AIN4-20mA%20Unit/STM32G030F6%20datasheet.PDF)
- [HCNR200 Datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/U162%20AIN4-20mA%20Unit/HCNR200%20datasheet.PDF)
- [SGM321YC5 Datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/U162%20AIN4-20mA%20Unit/SGM321YC5%20datasheet.PDF)

## 软件开发

### Arduino

- [Unit AIN4-20mA Arduino 驱动库](https://github.com/m5stack/M5Module-4-20mA)

### UiFlow1

- [Unit AIN4-20mA UiFlow1 文档](/zh_CN/uiflow/blockly/unit/ain4_20ma)
- [Unit AIN4-20mA UiFlow1 Example](https://flow.m5stack.com/?examples=unit_ain420ma_demo)

### UiFlow2

- [Unit AIN4-20mA UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/ain4.html)

### 内置固件

- [Unit AIN4-20mA 内置固件](https://github.com/m5stack/M5Module-4-20mA-Internal-FW)

### 通信协议

<img alt="module size" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/AIN4-20mA%20Unit/55f6b58f664b1b2f5eb6de0ac4a771f.png" width="100%" />
