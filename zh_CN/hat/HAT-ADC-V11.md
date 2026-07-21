# Hat ADC v1.1

<span class="product-sku">SKU:U069-V11</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/U069-B%20HAT-ADC/hat-adc_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/U069-B%20HAT-ADC/hat-adc_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/U069-B%20HAT-ADC/hat-adc_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/U069-B%20HAT-ADC/hat-adc_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/U069-B%20HAT-ADC/hat-adc_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/U069-B%20HAT-ADC/hat-adc_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/866/U069-V11-weight.jpg">
</PictureViewer>

## 描述

**Hat ADC v1.1** 是一款专为 StickC 系列设计的高精度模数转换模块。它内部搭载 ADS1110 16 位 Δ-Σ ADC 芯片，具备全差分输入、自校准、可调增益等特性。该芯片本身支持 -5V ~ +5V 差分输入，通过优化的外围电路设计，模块将其扩展至 0 ~ 12V 直流电压测量范围，并内置 2.048V 参考电压，无需外部参考源即可实现稳定、精确的信号采集。模块采用标准 I2C 接口通信，适用于工业传感器信号处理、电池电压监测及各类模拟信号采集等应用场景。

## 产品特性

- 输入电压: DC 0 ~ 12V
- ADS1110:
  - 内置 2.048V 参考电压
  - 16 位无漏失码
  - 连续自校准
  - 单循环转换
  - 内置可编程增益放大器 (增益倍数 = 1, 2, 4, 8)
  - 内部系统时钟
  - 可编程数据速率：15SPS 至 240SPS
  - I2C 接口 (0x48)
- 开发平台
  - UiFlow1
  - UiFlow2
  - Arduino IDE

## 包装内容

- 1 x Hat ADC v1.1
- 1 x HT3.96-2P 端子

## 应用场景

- 模拟信号捕获

## 规格参数

| 规格     | 参数                 |
| -------- | -------------------- |
| 通信接口 | I2C 通信 @ 0x48      |
| 产品尺寸 | 24.0 x 24.9 x 13.7mm |
| 产品重量 | 4.7g                 |
| 包装尺寸 | 40.0 x 42.0 x 30.0mm |
| 毛重     | 8.4g                 |

## 原理图

- [Hat ADC v1.1 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/582/StickHat_ADC_v1.1.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/582/StickHat_ADC_v1.1_sch_01.png">
</SchViewer>

## 管脚映射

| M5StickC     | G0  | G26 | 5V  | GND |
| ------------ | --- | --- | --- | --- |
| ADC HAT V1.1 | SDA | SCL | 5V  | GND |

## 尺寸图

[Hat ADC v1.1 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/865/U069_HATADC.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/865/U069_HATADC_page_01.png" width="100%">

## 数据手册

- **Datasheet** - [ADS1110](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/hat/U069-V11%20HAT-ADC/ads1110.pdf)

## 软件开发

### Arduino

- [Hat ADC v1.1 Example - with M5StickC](https://github.com/m5stack/M5-ADS1100/blob/master/examples/ADC_M5StickC/ADC_M5StickC.ino)
- [Hat ADC v1.1 Example - with M5StickCPlus](https://github.com/m5stack/M5-ADS1100/blob/master/examples/ADC_M5StickCPlus/ADC_M5StickCPlus.ino)

### UiFlow1

- [Hat ADC v1.1 UiFlow1 文档](/zh_CN/uiflow/blockly/hat/adc)

### Easyloader

| Easyloader              | 下载链接                                                                                           | 备注 |
| ----------------------- | -------------------------------------------------------------------------------------------------- | ---- |
| Hat ADC v1.1 Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/HAT/ADC/EasyLoader_ADC_HAT.exe) | /    |

## 相关视频

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/HAT/ADC-DAC-HAT.mp4" type="video/mp4" >
</video>

## 产品对比

| 特性         | ADS1110                   | ADS1100              |
| ------------ | ------------------------- | -------------------- |
| SKU          | HAT ADC V1.1 (U069-V11)   | HAT ADC (U069)       |
| 分辨率       | 16 位                     | 16 位                |
| I2C 地址选项 | 四个选项 (ADDR0 和 ADDR1) | 四个选项 (ADDR)      |
| 内部参考电压 | 2.048V                    | 无                   |
| 输入范围     | ±2.048V                   | 取决于外部参考电压   |
| 增益设置     | 可编程 (1, 2, 4, 8)       | 固定 (1)             |
| 封装类型     | SOT23, MSOP               | SOT23, MSOP          |
| 数据速率     | 可编程，典型值 15 SPS     | 固定，典型值 128 SPS |
