# Hat NCIR

<span class="product-sku">SKU:U061</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-ncir/hat-ncir_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-ncir/hat-ncir_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/851/U061-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-ncir/hat-ncir_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-ncir/hat-ncir_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/851/U061-weight.jpg">
</PictureViewer>

## 描述

**Hat NCIR**是一款兼容 M5SticKC 的单点红外测温传感器。内置红外传感器**MLX90614**，能够测量人体或其他物体的表面温度。与大多数接触式型传感器不同地方在于，该传感器通过测量远距离物体发射出的红外光波来检测温度，无需物理接触，这使得它比一般传感器拥有更广的测温范围： -70°C 至 + 380°C。视场角为 90°，能够方便快捷的测量某一位置的平均温度。

## 产品特性

- MLX90614ESF-AAA
- I2C 地址 (0x5A)
- 物体测温范围: -70°C ~ 380°C
- 环境测温范围: -40°C ~ 125 ˚C
- 室温下测量精度: ±0.5°C
- 视场角: 90°
- 开发平台: Arduino, UiFlow (Blockly, Python)

## 包装内容

- 1 x Hat NCIR
- 1 x 双面胶

## 应用场景

- 人体体温测量
- 物体 (生物) 移动检测

## 规格参数

| 规格     | 参数                  |
| -------- | --------------------- |
| 通信接口 | I2C 通信 @ 0x5A       |
| 产品尺寸 | 24.9 x 24.0 x 13.7mm  |
| 产品重量 | 5.2g                  |
| 包装尺寸 | 138.0 x 93.0 x 13.0mm |
| 毛重     | 7.6g                  |

## 原理图

- [Hat NCIR 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/851/U061-StickHat_NCIR-SCHE.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/851/U061-StickHat_NCIR-SCHE_page_01.png">
</SchViewer>

## 管脚映射

| M5StickC | G0  | G26 | 3.3V | GND |
| -------- | --- | --- | ---- | --- |
| HAT NCIR | SDA | SCL | 3.3V | GND |

## 尺寸图

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/851/U061_Model_Size_page_01.png" width="50%" height="50%">

## 数据手册

- [MLX90614 Datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/hat/MLX90614-Datasheet-Melexis_en.pdf)

## 软件开发

### Arduino

- [Hat NCIR Example](https://github.com/m5stack/M5StickC/tree/master/examples/Hat/NCIR_HAT)

### UiFlow1

- [Hat NCIR UiFlow1 文档](/zh_CN/uiflow/blockly/hat/ncir)

### UiFlow2

- [Hat NCIR UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/hats/ncir.html)

### EasyLoader

| Easyloader          | 下载链接                                                                                                    | 备注 |
| ------------------- | ----------------------------------------------------------------------------------------------------------- | ---- |
| Hat NCIR Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/HAT/NCIR/EasyLoader_StickC_HAT_NCIR.exe) | /    |

## 相关视频

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/HAT/NCIR-HAT.mp4" type="video/mp4">
</video>
