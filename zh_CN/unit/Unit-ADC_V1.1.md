# Unit ADC v1.1

<span class="product-sku">SKU:U013-V11</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-ADC_V1.1/img-240867ba-46d2-4cc6-beb9-79ac68af51d5.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-ADC_V1.1/img-53c84a8a-00c3-4cbe-8a48-3e52c9db6ae6.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-ADC_V1.1/img-46de4de7-6871-497f-be22-d2ab502383b1.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-ADC_V1.1/img-ea3d2857-9446-463e-af71-0df7b56c7218.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-ADC_V1.1/img-fcea998d-6c16-483f-8b34-6eeb32a7e34a.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-ADC_V1.1/img-61ce5d9c-1c35-4091-ada6-0f652d69779a.webp">
</PictureViewer>

## 描述

**Unit ADC v1.1** 是一款集成了 16 位模数转换器的单元，采用了 ADS1110 芯片，拥有内部参考电压 (2.048V)。通过 I2C 接口，实现每秒 15、30、60 或 240 次的高精度转换。该单元内置可编程增益放大器 ( PGA )，最大增益可达 8 倍，使其能够直接测量微弱信号。ADS1110 还配备了内部基准电压 ( 2.048V )，为高分辨率测量提供支持。适用于工业过程控制、工厂自动化、便携式仪表等领域。

## 产品特性

- 可编程增益放大器 (PGA = 1、2、4 或 8 连续自校准)
- 低噪声 (10uVP-P)
- I2C 通讯
- 内置基准 (精度：2.048V ± 0.05%)

## 包装内容

- 1 x Unit ADC v1.1
- 1 x HY2.0-4P Grove 连接线 (20cm)
- 1 x HT3.96-2P 端子

## 应用场景

- 工业过程控制
- 温度测量
- 工厂自动化
- 便携式仪表
- 智能型发送器

## 规格参数

| 规格             | 参数                          |
| ---------------- | ----------------------------- |
| 可编程增益放大器 | PGA=1、2、4 或 8              |
| 输入电压范围     | DC 0 ~ 12V                    |
| 通信接口         | I2C 通信 @ 0x48               |
| 温度漂移         | 5ppm/℃                        |
| INL              | 满标度是量程的 0.01% (最大值) |
| 基准电压         | VDD 基准电压                  |
| 采样速率         | 8,16,32,128 SPS               |
| ADS1110 分辨率   | 16-bit                        |
| 工作温度         | 0 ~ 40°C                      |
| 产品尺寸         | 32.0 x 24.0 x 10.2mm          |
| 产品重量         | 4.5g                          |
| 包装尺寸         | 138.0 x 93.0 x 11.2mm         |
| 毛重             | 11.2g                         |

## 原理图

- [Unit ADC v1.1 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/576/Sch_UNIT_ADC_v1.1.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/576/Sch_UNIT_ADC_v1.1_sch_01.png">
</SchViewer>

## 管脚映射

### Unit ADC v1.1

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 尺寸图

<img alt="module size" src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-ADC_V1.1/img-51a08ca2-6a38-4a21-acd4-b5a5eb470ab4.jpg" width="100%" />

## 数据手册

- [ADS1110 Datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-ADC_V1.1/ads1110.pdf)

## 软件开发

### Arduino

- [Unit ADC v1.1 with M5Core](https://github.com/m5stack/M5-ADS1100/blob/master/examples/Unit_ADC_M5Core/Unit_ADC_M5Core.ino)
- [Unit ADC v1.1 with M5Core2](https://github.com/m5stack/M5-ADS1100/blob/master/examples/Unit_ADC_M5Core2/Unit_ADC_M5Core2.ino)
- [Unit ADC v1.1 with M5Atom](https://github.com/m5stack/M5-ADS1100/blob/master/examples/Unit_ADC_M5Atom/Unit_ADC_M5Atom.ino)
- [Unit ADC v1.1 with M5StickC](https://github.com/m5stack/M5-ADS1100/blob/master/examples/ADC_M5StickC/ADC_M5StickC.ino)
- [Unit ADC v1.1 with M5StickCPlus](https://github.com/m5stack/M5-ADS1100/blob/master/examples/ADC_M5StickCPlus/ADC_M5StickCPlus.ino)

### UiFLow2

- [Unit ADC v 1.1 UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/adc_v11.html)

### EasyLoader

| Easyloader                    | 下载链接                                                                                                                               | 备注 |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | ---- |
| Unit ADC v1.1 Test Easyloader | [download](https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-ADC_V1.1/ezLoader-b2d4a451-f9b0-45be-8feb-756b4767245f.exe) | /    |

## 产品对比

::compare-table
| 产品对比表   | [Unit ADC v1.1](/zh_CN/unit/Unit-ADC_V1.1) ![Unit ADC v1.1](https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-ADC_V1.1/img-4482473a-9ddb-4fc7-8bd5-cc30de9a2e14.webp) | [Unit ADC](/zh_CN/unit/adc) ![Unit ADC](https://static-cdn.m5stack.com/resource/docs/products/unit/adc/adc_cover_01.webp) |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| ADC 方案     | ADS1100                                                                                                                                                                             | ADS1100                                                                                                                   |
| 分辨率       | 16-bit                                                                                                                                                                              | 16-bit                                                                                                                    |
| 输入电压范围 | DC 0 ~ 12V                                                                                                                                                                          | DC 0 ~ 12V                                                                                                                |
| 基准电压     | VDD 基准电压                                                                                                                                                                        | 内置基准电压                                                                                                              |
| 采样速率     | 8, 16, 32, 128 SPS                                                                                                                                                                  | 15, 30, 60, 240 SPS                                                                                                       |
::
