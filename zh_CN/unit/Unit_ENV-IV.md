# Unit ENV-IV

<span class="product-sku">SKU:U001-D</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/ENVⅣ Unit/img-c6f8993b-8df1-4327-aad8-44128f8ecace.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/ENVⅣ Unit/img-949651d3-241e-46c6-a355-833e97cecdb2.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/ENVⅣ Unit/img-ed0922ec-08ec-429f-84b5-8ac064491556.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/ENVⅣ Unit/img-7cfc7eaf-c497-4012-9b6c-2a6676e22e9e.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/ENVⅣ Unit/img-ab796899-2634-4e32-8cc5-03528cb76ffd.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/ENVⅣ Unit/img-f46cac07-2bb1-4abd-849e-16d935d8ada6.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/ENVⅣ Unit/img-6694f5e2-d5d0-4276-bbd7-29e5f80fb81b.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/724/U001-D_Weight.jpg">
</PictureViewer>

## 描述

**Unit ENV-IV** 是一款环境传感器单元，内嵌 SHT40 和 BMP280 传感器，用于测量 **温度、湿度和大气压** 数据。SHT40 是一款高精度、低功耗的数字温湿度传感器，支持 I2C 接口 （ SHT40 I2C 地址：0x44 ）。BMP280 则是绝对气压传感器，能够提供高精准度的大气压测量 （ BMP280 I2C 地址：0x76 ）。适用于气象监测、室内环境监控、农业和园艺和工业自动化等领域。

## 产品特性

- 集成传感器 (温湿度传感器 SHT40，气压传感器 BMP280)
- 高精度低功耗
- I2C 通信接口 (SHT40 I2C 地址：0x44，BMP280 I2C 地址：0x76)
- 实时监测
- 多平台编程 Arduino UiFlow

## 包含

- 1 x Unit ENV-IV
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 气象监测
- 室内环境监控
- 农业和园艺
- 工业自动化

## 规格参数

| 规格                       | 参数                                   |
| -------------------------- | -------------------------------------- |
| SHT40 测量范围 (温湿度)    | -40 ~ 125 °C，0 ~ 100 % RH             |
| BMP280 测量范围 (大气压力) | 300 ~ 1100hPa                          |
| SHT40 测量精度             | ±0.2 °C，±1.8 % RH                     |
| BMP280 测量精度            | ±0.12hPa                               |
| 通信协议                   | I2C 通信 @ SHT40 (0x44)，BMP280 (0x76) |
| 外壳材质                   | Plastic (PC)                           |
| 产品尺寸                   | 32.0 x 24.0 x 8.0mm                    |
| 产品重量                   | 3.9g                                   |
| 包装尺寸                   | 138.0 x 93.0 x 9.0mm                   |
| 毛重                       | 9.4g                                   |

## 原理图

- [Unit ENV-IV 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/573/Sch_UNIT_ENVIV.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/573/Sch_UNIT_ENVIV_sch_01.png">
</SchViewer>

## 管脚映射

### Unit ENV-IV

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 尺寸图

<img alt="module size" src="https://static-cdn.m5stack.com/resource/docs/products/unit/ENVⅣ Unit/img-3a3fce36-48d8-4335-a67f-ed93f11bedbb.jpg" width="100%" />

## 数据手册

- [BMP280 Datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/ENV%E2%85%A3%20Unit/BMP280.pdf)
- [SHT40 Datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/ENV%E2%85%A3%20Unit/SHT40.pdf)

## 软件开发

### Arduino

- [Unit ENV-IV Test Example with M5Core](https://github.com/m5stack/M5Unit-ENV/blob/master/examples/Unit_ENVIV_M5Core/Unit_ENVIV_M5Core.ino)

### UiFlow1

- [Unit ENV-IV UiFlow1 文档](/zh_CN/uiflow/blockly/unit/env)

### UiFlow2

- [Unit ENV-IV UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/env.html)

### Home Assistant

- [Home Assistant](/zh_CN/homeassistant/sensor/unit_env_iv_sensor)

### EasyLoader

| Easyloader                          | 下载链接                                                                                                                             | 备注 |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ---- |
| Unit ENV-IV Test Example Easyloader | [download](https://static-cdn.m5stack.com/resource/docs/products/unit/ENVⅣ%20Unit/ezLoader-a0c7ef88-87ce-4149-a1ca-f7c39e652502.exe) | /    |

## 相关视频

- 测量温湿度，大气压力例子

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/ENV%E2%85%A3%20Unit/34f2dcf2563f4fa8aa9039250fadc90b.mp4" type="video/mp4"></video>

## 产品对比

::compare-table
| 产品对比               | [Unit ENV](/zh_CN/unit/env)![Unit ENV](https://static-cdn.m5stack.com/resource/docs/products/unit/env/env_cover_01.webp) | [Unit ENV-II](/zh_CN/unit/envII)![[Unit ENV-II]](https://static-cdn.m5stack.com/resource/docs/products/unit/envII/envII_cover_01.webp) | [Unit ENV-III](/zh_CN/unit/envIII) ![Unit ENV-III](https://static-cdn.m5stack.com/resource/docs/products/unit/envIII/envIII_cover_01.webp) | [Unit ENV-IV](/zh_CN/unit/Unit_ENV-IV)![Unit ENV-IV](https://static-cdn.m5stack.com/resource/docs/products/unit/ENV%E2%85%A3%20Unit/img-d658b7f3-ab10-463b-acfd-a182a6b05e59.webp) | [Unit ENV-Pro](/zh_CN/unit/ENV%20Pro%20Unit) ![Unit ENV-Pro](https://static-cdn.m5stack.com/resource/docs/products/unit/ENV%20Pro%20Unit/img-2aac2a0e-7546-4ccd-94ec-ef0114b76c23.webp) |
| ---------------------- | -----------------------                                                                                                  | --------------------------------                                                                                                       | -----------------------------------                                                                                                        | --------------------------------                                                                                                                                                   | ------------------------------------                                                                                                                                                    |
| 传感器                 | DHT12+BMP280                                                                                                             | SHT30+BMP280                                                                                                                           | SHT30+QMP6988                                                                                                                              | SHT40+BMP280                                                                                                                                                                       | BME688                                                                                                                                                                                  |
| 检测数据类型           | 温度 + 气压 + 湿度                                                                                                       | 温度 + 气压 + 湿度                                                                                                                     | 温度 + 气压 + 湿度                                                                                                                         | 温度 + 气压 + 湿度                                                                                                                                                                 | 温度 + 气压 + 湿度 + 气体                                                                                                                                                               |
| 接口                   | I2C                                                                                                                      | I2C                                                                                                                                    | I2C                                                                                                                                        | I2C                                                                                                                                                                                | I2C                                                                                                                                                                                     |
| I2C 地址               | DHT12:0x5C<br>BMP280:0x76                                                                                                | SHT30:0x44<br>BMP280:0x76                                                                                                              | SHT30:0x44<br>QMP6988:0x70                                                                                                                 | SHT40:0x44<br>BMP280:0x76                                                                                                                                                          | BME688:0x77                                                                                                                                                                             |
| 精度                   | 温度：±0.5℃<br>湿度：±5% RH<br>气压：±0.12 hPa                                                                           | 温度：±0.2℃<br>湿度：±2% RH<br>气压：±0.12 hPa                                                                                         | 温度：±0.2℃<br>湿度：±2% RH<br>气压：±0.12 hPa                                                                                             | 温度：±0.2℃<br>湿度：±1.8% RH<br>气压：±0.12 hPa                                                                                                                                   | 温度：±0.5℃<br>湿度：±3% RH<br>气压：±0.12 hPa                                                                                                                                          |
| 范围                   | 温度：-20~60℃<br>湿度：20~95% RH<br>气压：300~1100 hPa                                                                   | 温度：-40~125℃<br>湿度：0~100% RH<br>气压：300~1100 hPa                                                                                | 温度：-40~125℃<br>湿度：0~100% RH<br>气压：300~1100 hPa                                                                                    | 温度：-40~125℃<br>湿度：0~100% RH<br>气压：300~1100 hPa                                                                                                                            | 扫描速度：10.8 秒                                                                                                                                                                       |
::
