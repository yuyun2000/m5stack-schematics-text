# Hat ENV-II

<span class="product-sku">SKU:U053-B</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat_envII/hat_envII_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat_envII/hat_envII_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat_envII/hat_envII_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat_envII/hat_envII_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat_envII/hat_envII_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat_envII/hat_envII_06.webp">
</PictureViewer>

## 描述

**Hat ENV-II** 是一款多功能环境传感器，内部集成 SHT30、BMP280 以及 BMM150，用于检测温度、湿度、大气压值数据和磁场。SHT30 是高精度低功耗的数字温湿度传感器，并支持 I2C 接口（0x44）。BMP280（0x76）是一款专为移动应用而设计的绝对气压传感器，具有较高的精准度。BMM150（0x10）是磁力计，可用于监测磁场变化及磁场方向。对于需要对环境数据进行快速采集检测的项目来说，**Hat ENV-II** 是一个兼顾性能与性价比的不错选择。

## 产品特性

- 温湿度、气压、磁场测量
- 高可靠性和长期稳定性
- 较高精准度

## 包装内容

- 1 x Hat ENV-II
- 1 x 双面胶

## 应用场景

- 气象站
- 储谷仓环境监控
- 指南针

## 规格参数  

| 规格                  | 参数                                             |  
| --------------------- | ------------------------------------------------ |  
| 最大温度测量范围      | -40 ~ 120℃                                       |  
| 最高测量精度          | 0 ~ 60℃ / ±0.2℃                                  |  
| 湿度测量范围 / 误差   | 10 ~ 90% RH / ±2%                                 |  
| 大气压测量范围 / 误差 | 300 ~ 1100hPa / ±1hPa                             |  
| 磁力计范围 / 误差     | ±1300μT (x, y-axis), ±2500μT (z-axis), 0.3μT     |  
| 通信接口              | I2C 通信 @ SHT30 (0x44), BMP280 (0x76), BMM150 (0x10) |  
| 工作温度              | 0°C ~ 60°C                                       |  
| 外壳材质              | Plastic (PC)                                     |
| 产品尺寸              | 15.0 x 24.0 x 14.0mm                             |  
| 产品重量              | 4.0g                                             |  
| 包装尺寸              | 36.0 x 36.0 x 18.0mm                             |  
| 毛重                  | 8.0g                                             |  

## 操作说明

?> BMM150 磁场干扰 | 带有磁铁的产品可能对 BMM150 磁场传感器造成干扰，导致读数异常。当搭配含有磁铁的 M5 主控设备时，需拆除磁铁，同时避免 BMM150 传感器放置在强磁场附近。

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat_envII/hat_envII_sch_01.webp" width="80%">

## 管脚映射

| M5StickC   | G26 | G0  | 5V  | GND |
| ---------- | --- | --- | --- | --- |
| ENV II HAT | SCL | SDA | 5V  | GND |

## 数据手册

- [BMP280 Datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/hat/BMP280-DS001-11_en.pdf)
- [SHT30 Datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/SHT3x_Datasheet_digital.pdf)
- [bmm150 Datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/BMM150_datasheet_en.pdf)

## 软件开发

### Arduino

- [Hat ENV-II Example - with M5StickC](https://github.com/m5stack/M5Unit-ENV/tree/master/examples/Hat_ENVII_M5StickC/Hat_ENVII_M5StickC.ino)
- [Hat ENV-II Example - with M5StickC-Plus](https://github.com/m5stack/M5Unit-ENV/tree/master/examples/Hat_ENVII_M5StickCPlus/Hat_ENVII_M5StickCPlus.ino)

### UiFlow1

- [Hat ENV-II UiFlow1 文档](/zh_CN/uiflow/blockly/hat/env)

### EasyLoader

| Easyloader            | 下载链接                                                                                                  | 备注 |
| --------------------- | --------------------------------------------------------------------------------------------------------- | ---- |
| Hat ENV-II Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/HAT/EasyLoader_ENV-II_HAT.exe) | /    |

## 产品对比

### SHT30 与 DHT12 对比

| /                   | SHT30              | DHT12             |
| ------------------- | ------------------ | ----------------- |
| 最大温度测量范围    | -40 ~ 120 ℃        | -20 ~ 60 ℃        |
| 温度测量误差        | 0 ~ 60 ℃/±0.2℃     | ±0.2℃             |
| 湿度测量范围 / 误差 | 10 ~ 90 % RH / ±2% | 20 ~ 95 % RH/0.1% |

## 相关视频

<video id="example_video" controls>
  <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/HAT/ENV_HAT.mp4" type="video/mp4">
</video>
