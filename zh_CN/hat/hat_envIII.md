# Hat ENV-III

<span class="product-sku">SKU:U053-D</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat_envIII/hat_envIII_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat_envIII/hat_envIII_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat_envIII/hat_envIII_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat_envIII/hat_envIII_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat_envIII/hat_envIII_06.webp">
</PictureViewer>

## 描述

**Hat ENV-III** 是一款适配 M5StickC 系列的多功能环境传感器，内部集成 SHT30、QMP6988，用于检测温度、湿度、大气压值数据。SHT30（0x44）是高精度低功耗的数字温湿度传感器。QMP6988（0x56）是一款专为移动应用而设计的绝对气压传感器，具有较高的精准度。对于需要对环境数据进行快速采集检测的项目来说， **Hat ENV-III** 是一个兼顾性能与性价比的不错选择。

## 产品特性

- 温湿度、气压
- 高可靠性和长期稳定性
- 较高精准度

## 包装内容

- 1 x Hat ENV-III
- 1 x 双面胶

## 应用场景

- 气象站
- 储谷仓环境监控

## 规格参数

| 规格                           | 参数                                      |
| ------------------------------ | ----------------------------------------- |
| 最大温度测量范围               | -40 ~ 120 ℃                               |
| 最高测量精度                   | 0 ~ 60 ℃/±0.2℃                            |
| 湿度测量范围 / 误差            | 10 ~ 90 % RH / ±2%                        |
| 气压最大测量值 / 分辨率 / 误差 | 300 ~ 1100hPa / 0.06Pa / ±3.9Pa           |
| 通信接口                       | I2C 通信 @ SHT30（0x44），QMP6988（0x56） |
| 工作温度                       | 0°C to 60°C                               |
| 外壳材质                       | Plastic （PC ）                           |
| 产品尺寸                       | 20.0 x 24.0 x 13.7mm                      |
| 产品重量                       | 4.0g                                      |
| 包装尺寸                       | 138.0 x 93.0 x 14.7mm                     |
| 毛重                           | 8.0g                                      |

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat_envIII/hat_envIII_sch_01.webp" width="80%">

## 管脚映射

| M5StickC    | G26 | G0  | 3.3V | GND |
| ----------- | --- | --- | ---- | --- |
| ENV III HAT | SCL | SDA | 3.3V | GND |

## 尺寸图

[Hat ENV-III 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/857/U053_HATENV.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/857/U053_HATENV_page_01.png" width="100%">

## 数据手册

- [QMP6988](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/enviii/QMP6988%20Datasheet.pdf)
- [SHT30](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/SHT3x_Datasheet_digital.pdf)

## 软件开发

### Arduino

- [Hat ENV-III Example - with M5StickC](https://github.com/m5stack/M5Unit-ENV/tree/master/examples/Hat_ENVIII_M5StickC/Hat_ENVIII_M5StickC.ino)
- [Hat ENV-III Example - with M5StickC-Plus](https://github.com/m5stack/M5Unit-ENV/tree/master/examples/Hat_ENVIII_M5StickCPlus/Hat_ENVIII_M5StickCPlus.ino)

## 常见问题

`ENVIII HAT与M5StackC CPLUS I2C总线不兼容解决？`

<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat_envIII/hat_envIII_01.webp" width="10%"><img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc_plus/m5stickc_plus_01.webp" width="10%">

- M5Stack ENV III HAT 不通过 I2C 总线向 M5Stick CPlus 提供数据 (Wire.begin (0,26))。其他 HAT，如 M5StickC Heart Rate Hat，在同一个 M5Stick CPlus 上可以正常使用。
- 修改头文件 SHT3X.cpp，添加总线设置 Wire.begin (0,26,100000UL); 如下图:

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/hat/hat_envIII/%E5%9B%BE%E7%89%871.webp" width="10%">

- 并将主程序的总线设置修改为如下图：

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/hat/hat_envIII/%E5%9B%BE%E7%89%872.webp" width="10%">
