# Unit NCIR

<span class="product-sku">SKU:U028</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/ncir/ncir_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/ncir/ncir_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/715/U028-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/ncir/ncir_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/715/U028_Unit_NCIR_weight.jpg">
</PictureViewer>

## 描述

**Unit NCIR** 是一款单点红外测温传感器。内置红外传感器 **MLX90614**，能够测量人体或其他物体的表面温度。

与大多数接触式型传感器不同地方在于，该传感器通过测量远距离物体发射出的红外光波来检测温度，无需物理接触，这使得它比一般传感器拥有更广的测温范围： -70°C 至 + 380°C。视场角为 90°，能够方便快捷的测量某一位置的平均温度。

该 Unit 通过 PORT A I2C (0x5A) 与 M5Core 连接.

## 产品特性

- MLX90614ESF-AAA
- 物体与环境测量
- 开发平台: Arduino，UiFlow (Blockly，Python)
- 2 x LEGO 兼容孔

## 包装内容

- 1 x Unit NCIR
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 人体体温测量
- 物体 (生物) 移动检测

## 规格参数

| 规格         | 参数                               |
| ------------ | ---------------------------------- |
| 通信接口     | I2C 通信 @ 0x5A，接口速率：100Kbps |
| 物体测温范围 | -70°C ~ 380°C                      |
| 环境测温范围 | -40°C ~ 125 ˚C                     |
| 测量精度     | ±0.5˚C                             |
| 视场角       | 90°                                |
| 产品尺寸     | 32.0 x 24.0 x 8.6mm                |
| 产品重量     | 4.8g                               |
| 包装尺寸     | 138.0 x 93.0 x 13.0mm              |
| 毛重         | 10.0g                              |

## 原理图

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/715/U028-unit-ncir.jpg" width="100%">

## 管脚映射

### Unit NCIR

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 尺寸图

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/ncir/%E5%B0%BA%E5%AF%B8%E5%9B%BE.jpg" width="100%">

## 结构文件

- [Unit NCIR 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/U028_Unit_NCIR/Structures)

## 数据手册

- [MLX90614 Datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/hat/MLX90614-Datasheet-Melexis_en.pdf)

## 软件开发

### Arduino

- [Unit NCIR 测试程序](https://github.com/m5stack/M5Stack/tree/master/examples/Unit/NCIR_MLX90614)

### UiFlow2

- [Unit NCIR UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/ncir.html)

### Home Assistant

- [Unit NCIR Home Assistant 集成](/zh_CN/homeassistant/sensor/unit_ncir_sensor)

### EasyLoader

| Easyloader                | 下载链接                                                                                                                           | 备注 |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---- |
| Unit NCIR Test Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/UNIT/For%20M5Core/EasyLoader_NCIR_UNIT_With_M5Core.exe) | /    |

## 相关视频

- 屏幕显示当前检测温度值.

<video id="example_video" controls>
  <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Unit/NCIR_UNIT.mp4" type="video/mp4">
</video>
