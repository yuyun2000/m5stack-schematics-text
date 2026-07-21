# Unit Mini TVOC/eCO2

<span class="product-sku">SKU:U088</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/tvoc/tvoc_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/tvoc/tvoc_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/727/U088-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/tvoc/tvoc_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/tvoc/tvoc_06.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/tvoc/tvoc_08.webp">
</PictureViewer>

## 描述

**Unit Mini TVOC/eCO2** 是一款数字式多像素气体传感器单元，内部集成 SGP30，主要测量空气中的各种 VOC (挥发性有机化合物) 和 H2。通过编程可实现对 TVOC (总挥发性有机化合物) 和 eCO2 (二氧化碳等效) 浓度的测量，在测量范围内典型测量精度为 15%。SGP30 读数经过内部校准输出，可保持长期稳定。SGP30 采用 I2C 协议通讯，带有片上湿度补偿功能，可通过外接湿度传感器开启该功能。如果您需要获取精确的结果，您需要根据已知测量源进行校准，SGP30 内置校准功能。此外，eCO2 是根据 H2 浓度计算得出的，并不能完全替代 CO2 传感器。

## 产品特性

- TVOC 与 eCO2 浓度检测
- I2C 通讯 (0x58)
- 读数稳定
- 具备片上湿度补偿功能
- 2 x LEGO 兼容孔
- HY2.0 4P 接口

## 包装内容

- 1 x Unit Mini TVOC/eCO2
- 1 x HY2.0-4P Grove 连接线 (5cm)

## 应用场景

- 空气质量监测
- eCO2 浓度检测

## 规格参数

| 规格                  | 参数                                                                  |
| --------------------- | --------------------------------------------------------------------- |
| 测量范围              | Ethanol:0-1000ppm，H2:0-1000ppm，TVOC:0-60000 ppb，eCO2:400-60000 ppm |
| TVOC 与 eCO2 采样率   | 1Hz                                                                   |
| TVOC 与 eCO2 采样精度 | TVOC:1/6/32bbp，eCO2:1/3/9/31ppm                                      |
| 通信接口              | I2C 通信 @ 0x58                                                       |
| 外壳材质              | Plastic (PC)                                                          |
| 产品尺寸              | 24.0 x 24.0 x 8.0mm                                                   |
| 产品重量              | 3.2g                                                                  |
| 包装尺寸              | 138.0 x 93.0 x 9.0mm                                                  |
| 毛重                  | 6.7g                                                                  |

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/tvoc/tvoc_sch_01.webp" width="80%">

## 管脚映射

### Unit Mini TVOC/eCO2

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 尺寸图

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/tvoc/%E5%B0%BA%E5%AF%B8%E5%9B%BE.jpg" width="100%">

## 结构文件

- [Unit Mini TVOC/eCO2 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/U088_Unit_Mini_TVOC_eCO2/Structures)

## 数据手册

- [SGP30](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/Sensirion_Gas_Sensors_SGP30_Datasheet.pdf)

## 软件开发

### Arduino

- [Unit Mini TVOC/eCO2 测试程序](https://github.com/m5stack/M5Stack/tree/master/examples/Unit/TVOC_SGP30)

### UiFlow1

- [Unit Mini TVOC/eCO2 测试程序](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/Unit/TVOC/UIFlow)

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/tvoc/tvoc_uiflow_01.webp" width="65%">

### UiFlow2

- [Unit Mini TVOC/eCO2 UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/tvoc.html)

### Home Assistant

- [Unit Mini TVOC/eCO2 Home Assistant 集成](/zh_CN/homeassistant/sensor/unit_mini_tvoc_eco2)

### EasyLoader

| Easyloader                          | 下载链接                                                                                                               | 备注 |
| ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---- |
| Unit Mini TVOC/eCO2 Test Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/UNIT/For%20M5Core/EasyLoader_TVOC_Unit.exe) | /    |

## 相关视频

- 显示 TVOC 和 eCO2 读数

<video id="example_video" controls>
  <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Unit/TVOC%20eCO2.mp4" type="video/mp4">
</video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=114227540919219&bvid=BV1m2oeYZESY&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/P0R5Mw2GeZ0?si=9dwpTCinfNUapWLv" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
