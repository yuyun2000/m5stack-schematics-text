# Hat ENV

<span class="product-sku">SKU:U053</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-env/hat-env_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-env/hat-env_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-env/hat-env_03.webp">
</PictureViewer>

## 描述

**Hat ENV**是一款兼容 M5SticKC 的多功能环境传感器，内部集成 DHT12、BMP280 和 BMM150，能够检测温度、湿度、大气压值、三轴磁力计数据。该模块采用的统一的 I2C 协议接口，因此在引脚上没有过多的占用。对于希望同时拥有精致体积与丰富功能的项目来说，**Hat ENV**是一个不错的选择。

## 产品特性

- 温度:
  - 测量范围: -20 ~ 60 ℃
- 湿度:
  - 测量范围: 20 ~ 95 % RH
- 大气压:
  - 测量范围: 300 ~ 1100hPa
- 磁场范围典型:
  - ±1300μT (x,y 轴),±2500μT (z 轴)
  - 磁场分辨率约为 0.3μT

## 包装内容

- 1x Hat ENV

## 应用场景

- 气象站
- 指南针

## 规格参数

| 规格     | 参数                             |
| -------- | -------------------------------- |
| 通信协议 | I2C:DHT12（0x5C）,BMM150（0x10） |
| 产品尺寸 | 24.0 x 20.0 x 14.0mm             |
| 产品重量 | 4.0g                             |
| 包装尺寸 | 36.0 x 38.0 x 18.0mm             |
| 毛重     | 8.0g                             |

## 操作说明

?> BMM150 磁场干扰 | 带有磁铁的产品可能对 BMM150 磁场传感器造成干扰，导致读数异常。当搭配含有磁铁的 M5 主控设备时，需拆除磁铁，同时避免 BMM150 传感器放置在强磁场附近。

## 原理图

- [Hat ENV原理图PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/857/StickHat_ENV.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/857/StickHat_ENV_page_01.png">

## 管脚映射

| M5StickC | G0  | G26 | 3.3V | GND |
| -------- | --- | --- | ---- | --- |
| HAT ENV  | SDA | SCL | 3.3V | GND |

## 数据手册

- [BMP280 datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/hat/BMP280-DS001-11_en.pdf)
- [DHT12 datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/hat/DHT12_en.pdf)
- [BMM150 datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/BMM150_datasheet_en.pdf)

## 软件开发

### Arduino

- [Hat ENV BMP280 Arduino 驱动库](https://github.com/adafruit/Adafruit_BMP280_Library)
- [Hat ENV 测试程序](https://github.com/m5stack/M5StickC/tree/master/examples/Hat/ENV)

### UiFlow1

- [Hat ENV UiFlow1 文档](/zh_CN/uiflow/blockly/hat/env)

### UiFlow2

- [Hat ENV UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/hats/env.html)

### EasyLoader

| Easyloader         | 下载链接                                                                                               | 备注 |
| ------------------ | ------------------------------------------------------------------------------------------------------ | ---- |
| Hat ENV Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/HAT/EasyLoader_ENV_HAT.exe) | /    |

## 相关视频

<video id="example_video" controls>
  <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/HAT/ENV_HAT.mp4" type="video/mp4">
</video>
