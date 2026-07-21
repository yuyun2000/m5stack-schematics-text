# Hat ENV-II.R

<span class="product-sku">SKU:U053-C</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat_envII.R/hat_envII.R_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat_envII.R/hat_envII.R_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat_envII.R/hat_envII.R_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat_envII.R/hat_envII.R_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat_envII.R/hat_envII.R_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat_envII.R/hat_envII.R_06.webp">
</PictureViewer>

## 描述

**Hat ENV-II.R** 是一款适配 M5StickC 系列的多功能环境传感器，内部集成 SHT30、BMP280，用于检测温度、湿度、大气压值数据。SHT30 是高精度低功耗的数字温湿度传感器，采用 I2C 接口（0x44）。BMP280（0x76）是一款专为移动应用而设计的绝对气压传感器，具有较高的精准度。对于需要对环境数据进行快速采集检测的项目来说，**Hat ENV-II.R** 是一个兼顾性能与性价比的不错选择。

## 产品特性

- 温湿度、气压
- 高可靠性和长期稳定性
- 较高精准度

## 包装内容

- 1 x Hat ENV-II.R
- 1 x 双面胶

## 应用场景

- 气象站
- 储谷仓环境监控

## 规格参数

| 规格                  | 参数                                   |
| --------------------- | -------------------------------------- |
| 最大温度测量范围      | -40 ~ 120℃                             |
| 最高测量精度          | 0 ~ 60℃ / ±0.2℃                        |
| 湿度测量范围 / 误差   | 10 ~ 90% RH / ±2%                      |
| 大气压测量范围 / 误差 | 300 ~ 1100hPa / ±1hPa                  |
| 通信接口              | I2C 通信 @ SHT30 (0x44), BMP280 (0x76) |
| 工作温度              | 0°C ~ 60°C                             |
| 外壳材质              | Plastic (PC)                           |
| 产品尺寸              | 15.0 x 24.0 x 14.0mm                   |
| 产品重量              | 4.0g                                   |
| 包装尺寸              | 36.0 x 36.0 x 18.0mm                   |
| 毛重                  | 8.0g                                   |

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat_envII.R/hat_envII.R_sch_01.webp" width="80%">

## 管脚映射

| M5StickC     | G26 | G0  | 3.3V | GND |
| ------------ | --- | --- | ---- | --- |
| ENV II.R HAT | SCL | SDA | 3.3V | GND |

## 数据手册

- [BMP280 Datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/hat/BMP280-DS001-11_en.pdf)
- [SHT30 Datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/SHT3x_Datasheet_digital.pdf)

## 软件开发

### Arduino

- [Hat ENV-II.R Example](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/Hat/ENVII_HAT/Arduino/ENVII_HAT)

## 产品对比

### SHT30 与 DHT12 对比

| /                   | SHT30              | DHT12             |
| ------------------- | ------------------ | ----------------- |
| 最大温度测量范围    | -40 ~ 120 ℃        | -20 ~ 60 ℃        |
| 温度测量误差        | 0 ~ 60 ℃/±0.2℃     | ±0.2℃             |
| 湿度测量范围 / 误差 | 10 ~ 90 % RH / ±2% | 20 ~ 95 % RH/0.1% |
