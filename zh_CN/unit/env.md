# Unit ENV

<span class="product-sku">SKU:U001</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/env/env_01.webp">
</PictureViewer>

## 描述

**Unit ENV** 是一款环境传感器，内部集成 DHT12 和 BMP280，用于检测温度、湿度、大气压值数据。DHT12 是 DHT11 湿度温度传感器的升级版本，完全向下兼容，测量数值更精确，并添加了 I2C 接口。BMP280 是一款专为移动应用而设计的绝对气压传感器，具有较高的精准度。适合应用在一些小型低功耗终端上。对于需要对环境数据进行快速采集检测的项目来说，Unit ENV 是一个兼顾性能与性价比的不错选择。

## 产品特性

- HY2.0-4P 接口，支持平台 [UiFlow](http://flow.m5stack.com) 、 [Arduino](http://www.arduino.cc).
- 2 x LEGO 兼容孔

## 包装内容

- 1 x Unit ENV
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 气象站
- 储谷仓环境监控

## 规格参数

| 规格                  | 参数                            |
| --------------------- | ------------------------------- |
| 温度测量范围 / 误差   | -20 ~ 60 ℃ / ±0.2℃              |
| 湿度测量范围 / 误差   | 20 ~ 95 % RH / ±0.1%            |
| 大气压测量范围 / 误差 | 300 ~ 1100hPa / ±1hPa           |
| 通信协议              | I2C:DHT12 (0x5C)，BMP280 (0x76) |
| 工作温度              | 0 ~ 60°C                        |
| 产品重量              | 4g                              |
| 毛重                  | 17g                             |
| 产品尺寸              | 24.2 x 32.2 x 8.1mm             |
| 包装尺寸              | 67 x 53 x 12mm                  |
| 外壳材质              | Plastic (PC)                    |

## 原理图

- [Unit ENV 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/721/U001_UNIT_ENV_SCHE.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/721/U001_UNIT_ENV_SCHE_page_01.png">
</SchViewer>

## 管脚映射

### Unit ENV

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 数据手册

- [BMP280](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/hat/BMP280-DS001-11_en.pdf)
- [DHT12](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/hat/DHT12_en.pdf)

## 软件开发

### Arduino

- [Unit ENV Example with M5Atom](https://github.com/m5stack/M5Unit-ENV/blob/master/examples/Unit_ENV_M5Atom/Unit_ENV_M5Atom.ino)
- [Unit ENV Example with M5Core](https://github.com/m5stack/M5Unit-ENV/blob/master/examples/Unit_ENV_M5Core/Unit_ENV_M5Core.ino)
- [Unit ENV Example with M5Core2](https://github.com/m5stack/M5Unit-ENV/blob/master/examples/Unit_ENV_M5Core2/Unit_ENV_M5Core2.ino)
- [Unit ENV Example with M5StickC](https://github.com/m5stack/M5Unit-ENV/blob/master/examples/Unit_ENV_M5StickC/Unit_ENV_M5StickC.ino)
- [Unit ENV Example with M5StickCPlus](https://github.com/m5stack/M5Unit-ENV/blob/master/examples/Unit_ENV_M5StickCPlus/Unit_ENV_M5StickCPlus.ino)

### UiFlow1

- [Unit ENV UiFlow1 文档](/zh_CN/uiflow/blockly/unit/env)

### UiFlow2

- [Unit ENV UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/env.html)

### EasyLoader

| Easyloader               | 下载链接                                                                                                                          | 备注 |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------- | ---- |
| Unit ENV Test Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/UNIT/For%20M5Core/EasyLoader_ENV_UNIT_With_M5Core.exe) | /    |

## 相关视频

- 显示温湿度与大气压数据.

<video id="example_video" controls>
  <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Unit/ENV_UNIT.mp4" type="video/mp4">
</video>

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
