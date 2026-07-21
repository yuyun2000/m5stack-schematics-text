# Hat ADC

<span class="product-sku">SKU:U069</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-adc/hat-adc_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-adc/hat-adc_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/865/U069-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-adc/hat-adc_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-adc/hat-adc_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-adc/hat-adc_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-adc/hat-adc_06.webp">
</PictureViewer>

## 描述

Hat ADC 是一款专为 StickC 系列设计的高精度模数转换模块。它内部搭载 ADS1100 16 位 Δ-Σ ADC 芯片，具备全差分输入、自校准、可调增益等特性。该芯片本身支持 -5V ~ +5V 差分输入，通过优化的外围电路设计，模块将其扩展至 0 ~ 12V 直流电压测量范围。模块采用标准 I2C 接口通信，可实现精确、稳定的电压采集，适用于工业传感器信号处理、电池电压监测及各类模拟信号采集等应用场景。

## 产品特性

- 输入电压: 0-12V
- ADS1100：
  - 16 位无漏失码
  - 连续自校准
  - 单循环转换
  - 内置可编程增益放大器 (增益倍数 = 1, 2, 4, 8)
  - 低噪声：4μVp-p
  - 可编程数据速率：8SPS 至 128SPS
  - 内部系统时钟
  - I2C 通信接口 (0x48)
- 开发平台
  - UiFlow1
  - UiFlow2
  - Arduino IDE

## 包装内容

- 1 x Hat ADC
- 1 x HT3.96-2P 端子
- 1 x 双面胶

## 应用场景

- 模拟信号捕获

## 规格参数

| 规格     | 参数                  |
| -------- | --------------------- |
| 通信接口 | I2C 通信 @ 0x48       |
| 产品尺寸 | 24.9 x 24.0 x 13.7mm  |
| 产品重量 | 6.0g                  |
| 包装尺寸 | 138.0 x 93.0 x 15.0mm |
| 毛重     | 14.0g                 |

## 原理图

- [Hat ADC 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/865/U069-StickHat_ADC-SCHE.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/865/U069-StickHat_ADC-SCHE_page_01.png">
</SchViewer>

## 管脚映射

| M5StickC | G0  | G26 | 5V  | GND |
| -------- | --- | --- | --- | --- |
| HAT ADC  | SDA | SCL | 5V  | GND |

## 尺寸图

[Hat ADC模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/865/U069_HATADC.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/865/U069_HATADC_page_01.png" width="100%">

## 数据手册

- [ADS1100](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/hat/ads1100_en.pdf)

## 软件开发

### Arduino

- [Hat ADC Example - with M5StickC](https://github.com/m5stack/M5-ADS1100/blob/master/examples/ADC_M5StickC/ADC_M5StickC.ino)
- [Hat ADC Example - with M5StickC-Plus](https://github.com/m5stack/M5-ADS1100/blob/master/examples/ADC_M5StickCPlus/ADC_M5StickCPlus.ino)

### UiFlow1

- [Hat ADC UiFlow1 文档](/zh_CN/uiflow/blockly/hat/adc)

### UiFlow2

- [Hat ADC UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/hats/adc.html)

### EasyLoader

| Easyloader         | 下载链接                                                                                           | 备注 |
| ------------------ | -------------------------------------------------------------------------------------------------- | ---- |
| Hat ADC Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/HAT/ADC/EasyLoader_ADC_HAT.exe) | /    |

## 相关视频

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/HAT/ADC-DAC-HAT.mp4" type="video/mp4" >
</video>
