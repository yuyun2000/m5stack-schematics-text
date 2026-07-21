# PM2.5 Kit

<span class="product-sku">SKU:K023</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/pm2.5/pm2.5_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/pm2.5/pm2.5_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/pm2.5/pm2.5_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/pm2.5/pm2.5_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/pm2.5/pm2.5_05.webp">
</PictureViewer>

## 描述

**PM2.5 Kit** 是一款空气质量监测套件。由 Basic 主控、内置 PMSA003 数字式颗粒物浓度传感器的 Module Air Quality，以及内置 SHT20 温湿度传感器的 Base BTC 组合而成，可同时采集环境颗粒物浓度与温湿度数据。套件支持多种粒径范围的悬浮颗粒物检测，并可输出 PM2.5 标准值相关的质量浓度数据，适用于家庭、办公、教室、实验室等固定点位的空气质量实时监测、数据记录与趋势分析，也可为空气净化器、新风系统等环境改善设备提供数据参考。

## 产品特性

- 基于 M5Stack Basic 主控
  - 配备屏幕与按键，便于本地数据显示与交互
- Module Air Quality 
  - 内置 PMSA003 颗粒物浓度传感器
  - 支持多粒径颗粒物与 PM2.5 质量浓度检测
  - 提供 2.54-8P 扩展接口，SPI/I2C IO 引脚引出
- Base BTC
  - SHT20 温湿度传感器，可同步采集环境温湿度数据
- 支持 DC 5V / USB Type-C 供电，兼容 M5Stack 模块化堆叠扩展体系

## 包装内容

- 1 x Basic
- 1 x Module Air Quality
- 1 x 底座
- 1 x USB Type-C cable (100cm)
- 2 x M3x16 螺丝

## 规格参数

| 规格                                   | 参数                                                            |
| -------------------------------------- | --------------------------------------------------------------- |
| PM2.5 传感器                           | PMSA003                                                         |
| 最小分辨粒径                           | 0.3μm                                                           |
| 颗粒物质量浓度分辨率                   | 1μg/m³                                                          |
| 颗粒物测量范围                         | 0.3-1.0、1.0-2.5、2.5-10 微米                                   |
| 颗粒物计数效率                         | 50%@0.3 微米；98%@≥0.5 微米                                     |
| 颗粒物质量浓度有效量程（PM2.5 标准值） | 0~500 微克/立方米                                               |
| 颗粒物质量浓度最大量程（PM2.5 标准值） | ≥1000 微克/立方米                                               |
| 颗粒物质量浓度一致性（PM2.5 标准值）   | ±10%@100~500 微克/立方米 <br> ±10 微克/立方米@0~100 微克/立方米 |
| 温湿度传感器                           | SHT20                                                           |
| 温度测量范围                           | -40 ~ 125°C                                                     |
| 温度测量精度                           | Typ. 0 ~ 60°C, ±0.3°C                                           |
| 湿度测量范围                           | 0 ~ 100%RH                                                      |
| 湿度测量精度                           | ±3% RH                                                          |
| 供电电压                               | DC 5V                                                           |
| 产品尺寸                               | 63.0 x 52.0 x 46.0mm                                            |
| 产品重量                               | 70.0g                                                           |
| 包装尺寸                               | 125.0 x 67.0 x 23.0mm                                           |
| 毛重                                   | 135.0g                                                          |

## 原理图

- [PM2.5 Kit 原理图PDF](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/schematic/Units/UNIT_PM25.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1065/UNIT_PM25_page_01.png">
</SchViewer>

## 数据手册

- [SHT20](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/hat/SHT20_Datasheet_en.pdf)
- [PMSA003](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/base/PMSA003_cn.pdf)

## 软件开发

### Arduino

- [PM2.5 Kit 测试程序](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/Base/PM2.5)

### UiFlow1

- [PM2.5 Kit UiFlow1 文档](/zh_CN/uiflow/blockly/base/pm2.5)

### EasyLoader

| Easyloader                | Download                                                                                                                 | Note |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------ | ---- |
| PM2.5 Kit Test Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/APPLICATION/EasyLoader_PM2.5_APPLICATION.exe) | /    |

## 相关视频

- 温湿度显示、PM1.0 PM2.5 PM10 标准颗粒物浓度与环境颗粒物浓度及颗粒物数量显示.

<video id="example_video" controls>
  <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/App/PM2.5.mp4" type="video/mp4">
</video>
