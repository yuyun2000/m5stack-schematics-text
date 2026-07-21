# Unit ENV-III

<span class="product-sku">SKU:U001-C</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/envIII/envIII_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/envIII/envIII_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/723/U001-C-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/envIII/envIII_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/envIII/envIII_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/723/U001-C-weight.jpg">
</PictureViewer>

## 描述

**Unit ENV-III** 是一款环境传感器，内部集成 SHT30 和 QMP6988，用于检测温度、湿度、大气压值数据。SHT30 是高精度低功耗的数字温湿度传感器，并支持 I2C 接口 （ SHT30: 0x44，QMP6988: 0x70 ）。QMP6988 是一款专为移动应用而设计的绝对气压传感器，具有较高的精准度与稳定性，适用于环境数据采集检测类型的项目。

## 产品特性

- 简单易用
- 高精准度
- I2C 通信接口
- HY2.0-4P 接口，支持平台 [UiFlow](http://flow.m5stack.com) 、 [Arduino](http://www.arduino.cc).
- 2 x LEGO 兼容孔

## 包装内容

- 1 x Unit ENV-III
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 气象站
- 储谷仓环境监控

## 规格参数

| 规格                           | 参数                                    |
| ------------------------------ | --------------------------------------- |
| 最大温度测量范围               | -40 ~ 120 ℃                             |
| 最高测量精度                   | 0 ~ 60 ℃/±0.2℃                          |
| 湿度测量范围 / 误差            | 10 ~ 90 % RH / ±2%                      |
| 气压最大测量值 / 分辨率 / 误差 | 300 ~ 1100hPa / 0.06Pa / ±3.9Pa         |
| 通信协议                       | I2C 通信 @ SHT30 (0x44)，QMP6988 (0x70) |
| 工作温度                       | 0 ~ 60°C                                |
| 外壳材质                       | Plastic (PC)                            |
| 产品尺寸                       | 32.0 x 24.0 x 8.0mm                     |
| 产品重量                       | 6.2g                                    |
| 包装尺寸                       | 138.0 x 93.0 x 9.0mm                    |
| 毛重                           | 14.8g                                   |

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/envIII/envIII_sch_01.webp" width="80%">

## 管脚映射

### Unit ENV-III

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 尺寸图

<img alt="module size" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/envIII/%E5%B0%BA%E5%AF%B8%E5%9B%BE.jpg" width="100%" />

## 结构文件

- [Unit ENV-III 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/U001-C_Unit_ENV-III/Structures)

## 数据手册

- [QMP6988](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/enviii/QMP6988%20Datasheet.pdf)
- [SHT30](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/SHT3x_Datasheet_digital.pdf)

## 软件开发

### Arduino

- [Unit ENV-III Test Example with M5Atom](https://github.com/m5stack/M5Unit-ENV/blob/master/examples/Unit_ENVIII_M5Atom/Unit_ENVIII_M5Atom.ino)
- [Unit ENV-III Test Example with M5AtomS3](https://github.com/m5stack/M5Unit-ENV/blob/master/examples/Unit_ENVIII_M5AtomS3/Unit_ENVIII_M5AtomS3.ino)
- [Unit ENV-III Test Example with M5AtomS3Lite](https://github.com/m5stack/M5Unit-ENV/blob/master/examples/Unit_ENVIII_M5AtomS3Lite/Unit_ENVIII_M5AtomS3Lite.ino)
- [Unit ENV-III Test Example with M5Core](https://github.com/m5stack/M5Unit-ENV/blob/master/examples/Unit_ENVIII_M5Core/Unit_ENVIII_M5Core.ino)
- [Unit ENV-III Test Example with M5Core2](https://github.com/m5stack/M5Unit-ENV/blob/master/examples/Unit_ENVIII_M5Core2/Unit_ENVIII_M5Core2.ino)
- [Unit ENV-III Test Example with M5StickC](https://github.com/m5stack/M5Unit-ENV/blob/master/examples/Unit_ENVIII_M5StickC/Unit_ENVIII_M5StickC.ino)
- [Unit ENV-III Test Example with M5StickCPlus](https://github.com/m5stack/M5Unit-ENV/blob/master/examples/Unit_ENVIII_M5StickCPlus/Unit_ENVIII_M5StickCPlus.ino)

### UiFlow1

- [Unit ENV-III UiFlow1 文档](/zh_CN/uiflow/blockly/unit/env)

### UiFlow2

- [Unit ENV-III UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/env.html)

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
