# Unit Mini CAN

<span class="product-sku">SKU:U179</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-Mini CAN/img-027ca92c-9862-4be2-96d3-e88ca7d4ea77.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-Mini CAN/img-3b5e0bff-109f-4fd3-8c8b-1369a284f25f.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-Mini CAN/img-4e99b8e5-9b67-4381-8232-939f4d15514a.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-Mini CAN/img-2c2855ee-66df-4e53-bd5a-2c4f9f24364a.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-Mini CAN/img-f9c7e55d-aa74-4c6f-95e2-00eae24db786.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-Mini CAN/img-d8296edf-2e0f-4459-aa69-df57db939b39.webp">
</PictureViewer>

## 描述

**Unit Mini CAN** 是一款小型 CAN 总线通讯单元，采用 TJA1051T 芯片，具备卓越的高速数据传输能力，并配备电磁兼容性 (EMC) 和静电放电 (ESD) 保护机制。内部集成 DC-DC 电源芯片，拥有宽电压输入范围，为用户提供了稳定高效的 CAN 通信解决方案。该产品适用于汽车电子、工业自动化和通信系统等领域，为用户提供可靠且灵活的 CAN 通信解决方案。

## 产品特性

- 采用 TJA1051T/3 芯片
- 高速数据传输能力
- 电磁兼容性 (EMC) 和静电放电 (ESD) 保护机制
- HT3.96 端子宽电压输入范围 (9-24v)

## 包装内容

- 1 x Unit Mini CAN
- 1 x HY2.0-4P Grove 连接线 (20cm)
- 1 x HT3.96-4P

## 应用场景

- 汽车电子
- 工业自动化

## 规格参数

| 规格       | 参数                                                     |
| ---------- | -------------------------------------------------------- |
| 传输速率   | 高达 1Mbit/s                                             |
| 协议标准   | 符合 ISO 11898-2:2016 和 SAE J2284-1 至 SAE J2284-5 标准 |
| 宽电压输入 | HT3.96 端子：9-24V<br/>Grove:5V                          |
| 带载能力   | DC 5V/Max:700mA                                          |
| 工作电流   | Avg:DC 5V/4.02mA<br/>Avg:DC 24V/2mA                      |
| 待机电流   | Avg:DC 5V/3.09mA                                         |
| 工作温度   | 0 ~ 40°C                                                 |
| 产品尺寸   | 32.0 x 24.0 x 10.2mm                                     |
| 产品重量   | 8.0g                                                     |
| 包装尺寸   | 138.0 x 93.0 x 11.2mm                                    |
| 毛重       | 13.3g                                                    |

## 原理图

- [Unit Mini CAN 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/631/SCH_UNIT_Mini_CAN_V1.0.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/631/SCH_UNIT_Mini_CAN_V1.0_sch_01.png">
</SchViewer>

## 管脚映射

### Unit Mini CAN

::grove-table
| HY2.0-4P | Black | Red | Yellow | White  |
| -------- | ----- | --- | ------ | ------ |
| PORT.C   | GND   | 5V  | CAN_TX | CAN_RX |
::

## 尺寸图

<img alt="module size" src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-Mini CAN/img-098a4216-2c39-44ba-836c-5565299c05d7.jpg" width="100%" />

## 数据手册

- [TJA1051T](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-Mini%20CAN/TJA1051T.pdf)

## 软件开发

### Arduino

- [Unit Mini CAN Test Example with M5CoreS3](https://github.com/m5stack/M5CoreS3/tree/main/examples/Unit/MiniCAN_TJA1051T)
- [Unit Mini CAN Test Example with M5AtomS3](https://github.com/m5stack/M5AtomS3/tree/main/examples/Unit/MiniCAN_TJA1051T)
- [Unit Mini CAN Test Example with M5Core](https://github.com/m5stack/M5Stack/tree/master/examples/Unit/CAN)

### UiFlow1

- [Unit Mini CAN UiFlow1 文档](/zh_CN/uiflow/blockly/unit/mini_can)

### UiFlow2

- [Unit Mini CAN UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/can.html)

## 产品对比

::compare-table
| 产品对比表   | [Unit Mini CAN](/zh_CN/unit/Unit-Mini%20CAN) ![Unit Mini CAN](https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-Mini%20CAN/img-fde85c7a-655d-497c-8ece-3f3e81e2dfc4.webp) | [Unit CAN](/zh_CN/unit/can) ![Unit CAN](https://static-cdn.m5stack.com/resource/docs/products/unit/can/can_cover_01.webp) |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| CAN 收发器   | TJA1051T/3                                                                                                                                                                              | CA-IS3050G                                                                                                                |
| 是否电源隔离 | 不带隔离                                                                                                                                                                                | 带隔离                                                                                                                    |
| 速率         | 1Mbps                                                                                                                                                                                   | 1Mbps                                                                                                                     |
| 输入电源     | HY2.0-4P 接口 DC 5V 供电 <br/> HT3.96-4P 接口 DC 9 ~ 24V 供电                                                                                                                           | HY2.0-4P 接口 DC 5V 供电                                                                                                  |
::
