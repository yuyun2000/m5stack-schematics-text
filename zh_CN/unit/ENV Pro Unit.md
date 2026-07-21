# Unit ENV-Pro

<span class="product-sku">SKU:U169</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/ENV Pro Unit/img-2ba12134-9756-471a-b1a5-ba803a875e8f.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/ENV Pro Unit/img-0619fb0d-481f-4208-a862-461f0f5a4aeb.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/725/U169-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/ENV Pro Unit/img-f8fc52d8-90dc-451b-9d7b-0f6abc445920.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/ENV Pro Unit/img-d86edc21-2e66-4da3-b875-f974a9b12557.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/ENV Pro Unit/img-7d6d9630-f684-4f16-87ba-3e48b83ab90b.webp">
</PictureViewer>

## 描述

**Unit ENV-Pro** 传感器是一款高集成度的环境检测单元，内置 **BME688** 传感器方案，支持测量 VOC 等挥发性有机化合物、CO₂ 当量、室内空气质量 （ IAQ ）、温湿度和大气压等多种环境参数。传感器采用 I2C 通信接口 （ 0x77 ），适用于天气站、室内环境监测和空气质量检测等应用场景。

## 产品特性

- 高集成传感器
- I2C 通讯
- 高精度低功耗
- 实时监测
- 多平台编程 Arduino UiFlow

## 包装内容

- 1 x Unit ENV-Pro
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 室内外空气质量测量
- 探测泄漏或火灾
- 农业温湿度检测

## 规格参数

| 规格                 | 参数                                                                                                                                                  |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| 气体传感器关键参数   | 标准扫描速度：10.8 s                                                                                                                                  |
| 湿度传感关键参数     | 响应时间 (τ 0-63%) ：8 秒 <br/>精度：±3% R.H <br/>测量范围：0 ~ 100% R.H.                                                                             |
| 大气压力传感关键参数 | 平方根噪声值：0.12 Pa，约等于 1.7 厘米海拔高度 <br/>偏移温度系数： ±1.3 Pa/K，约等于 ±10.9 cm 海拔高度 (1°C 温度变化下) <br/>测量范围：300 ~ 1100 hPa |
| 温度传感关键参数     | 绝对精度： ±0.5 °C (0 ~ 65°C) <br/>测量范围：-40 ~ +85 °C                                                                                             |
| 通信接口             | I2C 通信 @ 0x77                                                                                                                                       |
| 产品尺寸             | 32.0 x 24.0 x 8.0mm                                                                                                                                   |
| 产品重量             | 3.9g                                                                                                                                                  |
| 包装尺寸             | 138.0 x 93.0 x 9.0mm                                                                                                                                  |
| 毛重                 | 9.2g                                                                                                                                                  |

## 原理图

- [Unit ENV-Pro 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/622/Sch_UNIT-ENV_Pro.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/622/Sch_UNIT-ENV_Pro_sch_01.png">
</SchViewer>

## 管脚映射

### Unit ENV-Pro

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 尺寸图

<img alt="module size" src="https://static-cdn.m5stack.com/resource/docs/products/unit/ENV Pro Unit/img-c3e64d4b-35aa-4a1c-9473-cc743ad0c5ef.jpg" width="100%" />

## 结构文件

- [Unit ENV-Pro 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/U169_Unit_ENV-Pro/Structures)

## 数据手册

- [BME688 Datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/ENV%20Pro%20Unit/bst-bme688-ds000.pdf)

## 软件开发

### Arduino

- [ENV PRO UNIT Arduino示例 (读取温湿度、气压和室内空气质量数值) ](https://github.com/m5stack/M5Unit-ENV/blob/master/examples/ENV_PRO/ENV_PRO.ino)
- [Bosch BME688官方库文件](https://github.com/boschsensortec/Bosch-BSEC2-Library)
- [Bosch BME688官方检测分析上位机工具](https://www.bosch-sensortec.com/software-tools/software/bme688-software/)

### UiFlow1

- [Unit ENV-Pro 测试程序](https://flow.m5stack.com/?examples=unit_env_pro_demo)

### UiFlow2

- [Unit ENV-Pro UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/envpro.html)

### Home Assistant

- [Unit ENV-Pro Home Assistant 集成](/zh_CN/homeassistant/sensor/unit_env_pro_sensor)

## 相关视频

- Unit ENV-Pro 示例 (读取温湿度、气压和室内空气质量数值)

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/ENV%20Pro%20Unit/ENV%20PRO%20UNIT.mp4" type="video/mp4"></video>

- Unit ENV-Pro UiFlow 上手示例 (读取温湿度、气压和室内空气质量数值)

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/ENV%20Pro%20Unit/ENV_PRO_UIFLOW.mp4" type="video/mp4"></video>

## 产品对比

::compare-table
| 产品对比               | [Unit ENV](/zh_CN/unit/env)![Unit ENV](https://static-cdn.m5stack.com/resource/docs/products/unit/env/env_cover_01.webp) | [Unit ENV-II](/zh_CN/unit/envII)![[Unit ENV-II]](https://static-cdn.m5stack.com/resource/docs/products/unit/envII/envII_cover_01.webp) | [Unit ENV-III](/zh_CN/unit/envIII) ![Unit ENV-III](https://static-cdn.m5stack.com/resource/docs/products/unit/envIII/envIII_cover_01.webp) | [Unit ENV-IV](/zh_CN/unit/Unit_ENV-IV)![Unit ENV-IV](https://static-cdn.m5stack.com/resource/docs/products/unit/ENV%E2%85%A3%20Unit/img-d658b7f3-ab10-463b-acfd-a182a6b05e59.webp) | [Unit ENV-Pro](/zh_CN/unit/ENV%20Pro%20Unit) ![Unit ENV-Pro](https://static-cdn.m5stack.com/resource/docs/products/unit/ENV%20Pro%20Unit/img-2aac2a0e-7546-4ccd-94ec-ef0114b76c23.webp) |
| ---------------------- | -----------------------                                                                                                  | --------------------------------                                                                                                       | -----------------------------------                                                                                                        | --------------------------------                                                                                                                                                   | ------------------------------------                                                                                                                                                    |
| 传感器                 | DHT12+BMP280                                                                                                             | SHT30+BMP280                                                                                                                           | SHT30+QMP6988                                                                                                                              | SHT40+BMP280                                                                                                                                                                       | BME688                                                                                                                                                                                  |
| 检测数据类型           | 温度 + 气压 + 湿度                                                                                                       | 温度 + 气压 + 湿度                                                                                                                     | 温度 + 气压 + 湿度                                                                                                                         | 温度 + 气压 + 湿度                                                                                                                                                                 | 温度 + 气压 + 湿度 + 气体                                                                                                                                                               |
| 接口                   | I2C                                                                                                                      | I2C                                                                                                                                    | I2C                                                                                                                                        | I2C                                                                                                                                                                                | I2C                                                                                                                                                                                     |
| I2C 地址               | DHT12:0x5C<br>BMP280:0x76                                                                                                | SHT30:0x44<br>BMP280:0x76                                                                                                              | SHT30:0x44<br>QMP6988:0x70                                                                                                                 | SHT40:0x44<br>BMP280:0x76                                                                                                                                                          | BME688:0x77                                                                                                                                                                             |
| 精度                   | 温度：±0.5℃<br>湿度：±5% RH<br>气压：±0.12 hPa                                                                           | 温度：±0.2℃<br>湿度：±2% RH<br>气压：±0.12 hPa                                                                                         | 温度：±0.2℃<br>湿度：±2% RH<br>气压：±0.12 hPa                                                                                             | 温度：±0.2℃<br>湿度：±1.8% RH<br>气压：±0.12 hPa                                                                                                                                   | 温度：±0.5℃<br>湿度：±3% RH<br>气压：±0.12 hPa                                                                                                                                          |
| 范围                   | 温度：-20~60℃<br>湿度：20~95% RH<br>气压：300~1100 hPa                                                                   | 温度：-40~125℃<br>湿度：0~100% RH<br>气压：300~1100 hPa                                                                                | 温度：-40~125℃<br>湿度：0~100% RH<br>气压：300~1100 hPa                                                                                    | 温度：-40~125℃<br>湿度：0~100% RH<br>气压：300~1100 hPa                                                                                                                            | 温度：-40~85℃<br>湿度：0~100% RH<br>气压：300~1100 hPa                                                                                                                                  |
::
