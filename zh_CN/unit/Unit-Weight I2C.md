# Unit Weight-I2C

<span class="product-sku">SKU:U180</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-Weight I2C/img-0634712b-2a27-48cf-894f-d6708a771d47.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-Weight I2C/img-15df7cc2-ace5-40dc-a2c7-5ab83cdc38d3.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/750/U180-weight.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-Weight I2C/img-a4d8bc9a-3926-4265-b108-6501b25fcf3d.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-Weight I2C/img-da7c0ae5-b2ca-4371-9d0a-1b7e06b262f5.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-Weight I2C/img-d890ef48-fe47-4ae6-bc79-4e920f913e53.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-Weight I2C/img-f0cbbc11-3f81-4d72-8080-b4ad1eacdb7a.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-Weight I2C/img-c6a9d8b4-a856-4eb1-9590-456113a5f7ff.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-Weight I2C/img-a34e63d1-fb5a-4f49-bf40-94e4c287b700.webp">
</PictureViewer>

## 描述

**Unit Weight-I2C** 是一款称重采集变送器单元，采用 “STM32 + HX711 芯片” 的方案，借助 I2C 通讯方式达成 24 位精度的重量测量。该单元具备独特优势，支持多个设备并联于同一 I2C 总线上，这为用户在更大范围开展测量工作、获取更多数据采集点提供了灵活性。该产品适用于工业生产、医疗保健、物流运输、实验室研究以及食品加工等诸多领域。

## 产品特性

- STM32F030F4P6+HX711
- 24Bit 测量精度
- I2C 通讯
- 开发平台: Arduino，UiFlow 等

## 包装内容

- 1 x Unit Weight-I2C
- 1 x HY2.0-4P Grove 连接线 (20cm)
- 1 x HT3.96-4P

## 应用场景

- 微型重量计
- 食品加工
- 物流运输
- 实验室研究

## 规格参数

| 规格     | 参数                     |
| -------- | ------------------------ |
| MCU      | STM32F030F4P6@32-bit ARM |
| 分辨率   | 24Bit                    |
| 通信接口 | I2C 通信 @ 0x26          |
| 工作温度 | 0 ~ 40°C                 |
| 产品尺寸 | 56.0 x 24.0 x 11.3mm     |
| 产品重量 | 5.2g                     |
| 包装尺寸 | 138.0 x 93.0 x 12.3mm    |
| 毛重     | 13.3g                    |

## 操作说明

- 连接示意图

<img alt="schematics" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-Weight%20I2C/ch.png" width="100%" />

## 原理图

- [Unit Weight-I2C 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/632/SCH_UNIT_WEIGHT_I2C.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/632/SCH_UNIT_WEIGHT_I2C_sch_01.png">
</SchViewer>

## 管脚映射

### Unit Weight-I2C

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 尺寸图

<img alt="module size" src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-Weight I2C/img-c48c5579-3111-4266-8f9b-9e748e4bccef.jpg" width="100%" />

## 数据手册

- [Datasheet-HX711](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/HX711_en.pdf)

## 软件开发

### Arduino

- [Unit Weight-I2C Arduino 驱动库](https://github.com/m5stack/M5Unit-WeightI2C)

### UiFlow1

- [Unit Weight-I2C UiFlow1 文档](/zh_CN/uiflow/blockly/unit/weight_i2c)

### UiFlow2

- [Unit Weight-I2C UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/weight_i2c.html)

### 内置固件

- [Unit Weight-I2C 内置固件](https://github.com/m5stack/M5Unit-Miniscale-Internal-FW/tree/main/weight-i2c-code)

| 固件版本 | 修改记录                                                      | 通信协议                                                                                                                   | 备注 |
| -------- | ------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ---- |
| v3       | 首次发布时版本                                                | [Unit Weight-I2C I2C Protocol v3](https://github.com/m5stack/M5Unit-WeightI2C/blob/main/docs/Unit_Weight_I2C_Protocol.pdf) | /    |
| v4       | 取消了对 ADC 变化值的绝对值限制，以便能够显示负的重量测量值。 | 通信协议无变更，使用 v3 版本                                                                                               | /    |

\#> M5 DAPLink | 若您没有 STM32 下载器工具，可参考[M5 DAPLink](/zh_CN/guide/develop_tools/daplink)教程，使用 Core2 或 CoreS3 作为烧录器，为设备完成固件更新。

### 通信协议

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/750/Unit_Weight_I2C_Protocol_page_01.png" width="100%"/>

## 产品对比

::compare-table
| 产品对比表   | [Unit Scales](/zh_CN/unit/UNIT%20Scales) ![Unit Scales](https://static-cdn.m5stack.com/resource/docs/products/unit/UNIT%20Scales/img-d095bc9f-0f3f-4243-abde-82f8d6b67949.webp) | [Scales Kit](/zh_CN/app/scales_kit) ![Scales Kit](https://static-cdn.m5stack.com/resource/docs/products/app/scales_kit/scales_kit_cover_01.webp) | [Unit Mini Scales](/zh_CN/unit/Unit-Mini%20Scales) ![Unit Mini Scales](https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-Mini%20Scales/img-c370a473-d300-42c0-bf4c-cdf6d7963a6a.webp) | [Unit Weight](/zh_CN/unit/WEIGHT) ![Unit Weight](https://static-cdn.m5stack.com/resource/docs/products/unit/WEIGHT/img-e051022a-5e26-4ca5-9080-71eeb98fdf5e.webp) | [Unit Weight-I2C](/zh_CN/unit/Unit-Weight%20I2C) ![Unit Weight-I2C](https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-Weight%20I2C/img-998f3dae-bddd-4eea-8361-0c24821f367e.webp) |
| ------------ | ---------------------                                                                                                                                                           | --------------------                                                                                                                             | --------------------------                                                                                                                                                                          | ---------------------                                                                                                                                             | -------------------------                                                                                                                                                                       |
| 通信协议     | I2C                                                                                                                                                                             | ADC                                                                                                                                              | I2C                                                                                                                                                                                                 | ADC                                                                                                                                                               | I2C                                                                                                                                                                                             |
| 芯片方案     | STM32+HX711                                                                                                                                                                     | HX711                                                                                                                                            | STM32+HX711                                                                                                                                                                                         | HX711                                                                                                                                                             | STM32+HX711                                                                                                                                                                                     |
| 传感器量程   | 0~20kg                                                                                                                                                                          | 0~200kg                                                                                                                                          | 0~5kg                                                                                                                                                                                               | 取决应变片与控制芯片                                                                                                                                              | 取决应变片与控制芯片                                                                                                                                                                            |
::
