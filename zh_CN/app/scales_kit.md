# Scales Kit

<span class="product-sku">SKU:K121</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/scales_kit/scales_kit_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/scales_kit/scales_kit_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1063/K121_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/scales_kit/scales_kit_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/scales_kit/scales_kit_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/scales_kit/scales_kit_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/scales_kit/scales_kit_06.webp">
</PictureViewer>

## 描述

Scales Kit 是一款电子称套件，采用四组半桥式电阻应变片构成，总称重量程可达`200kg`。搭配高精度 24 位 A/D 转换器芯片`HX711`. 内置低噪声可编程放大器，支持`32`/`64`/`128`倍增益调节。搭配 M5Stack 主控进行编程，仅需几分钟既可轻松构建一个 IoT 称重应用。

\#> 注意：Scales Kit 需要搭配一个称重面板才能使用，盖板边长不应超过 50cm。

## 产品特性

- 套件总量程 200kg
- HX711:
  - 高精度 24bit ADC
  - 可编程增益放大 32, 64 and 128
  - 10SPS 输出数据速率
- 半桥式电阻应变片：
  - 输出灵敏度：1.0±0.1mV/V
  - 非线性： 0.3% F.S
  - 综合精度： 0.3% F.S
  - 零点输出：±0.3mv/V
  - 每片应变计上下阻抗相差: 0.8Ω
  - 输出 (入) 阻抗：1000±5Ω

## 包装内容

- 4 x 半桥式电阻应变片
- 1 x Unit Weight
- 1 x HY2.0-4P Cable(20cm)
- 4 x 双面胶纸 (39 x 20 x 0.8mm)
- 4 x 双面胶纸 (39 x 12 x 0.8mm)
- 1 x 传感器接线端子

## 应用场景

- 电子称设计

## 规格参数

| 规格             | 参数                                                                                                                                                      |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| HX711            | 输出灵敏度：高精度 24bit ADC<br/>可编程增益放大 32, 64, 128<br/>10SPS 输出数据速率                                                                        |
| 半桥式电阻应变片 | 输出灵敏度：1.0±0.1mV/V<br/>非线性： 0.3% F.S<br/>综合精度： 0.3% F.S<br/>零点输出：±0.3mv/V<br/>每片应变计上下阻抗相差: 0.8Ω<br/>输出 (入) 阻抗：1000±5Ω |
| 产品尺寸         | 105.0 x 65.0 x 40.0mm                                                                                                                                     |
| 产品重量         | 88.5g                                                                                                                                                     |
| 包装尺寸         | 152.0 x 82.0 x 20.0mm                                                                                                                                     |
| 毛重             | 113.2g                                                                                                                                                    |

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/app/scales_kit/scales_kit_sch_01.webp" width="80%">

## 管脚映射

### Unit Weight

| M5Core      | G36            | G26             | 5V  | GND |
| ----------- | -------------- | --------------- | --- | --- |
| Unit Weight | DATA Pin (DAT) | CLOCK Pin (CLK) | VCC | GND |

## 尺寸图

- [Scales kit 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1063/K121-sacle-kit.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1063/K121-sacle-kit_page_01.png" width="100%">

## 数据手册

- [HX711](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/HX711_en.pdf)

## 软件开发

### Arduino

- [HX711 Arduino 驱动库](https://github.com/bogde/HX711)
- [Scales kit with M5Core](https://github.com/m5stack/M5Stack/blob/master/examples/KIT/SCALES_KIT/SCALES_KIT.ino)
- [Scales kit with M5Core2](https://github.com/m5stack/M5Core2/blob/master/examples/KIT/SCALES_KIT/SCALES_KIT.ino)
- [Scales kit with ATOM](https://github.com/m5stack/M5Atom/tree/master/examples/KIT/SCALES_KIT/SCALES_KIT.ino)
- [Scales kit with M5StickC](https://github.com/m5stack/M5StickC/tree/master/examples/KIT/SCALES_KIT/SCALES_KIT.ino)
- [Scales kit with M5StickC Plus](https://github.com/m5stack/M5StickC-Plus/tree/master/examples/KIT/SCALES_KIT/SCALES_KIT.ino)
- [Scales kit with CoreInk](https://github.com/m5stack/M5Core-Ink/tree/master/examples/KIT/SCALES_KIT/SCALES_KIT.ino)
- [Scales kit with M5Paper](https://github.com/m5stack/M5EPD/blob/main/examples/KIT/SCALES_KIT/SCALES_KIT.ino)

\#> 校准操作 | 设置 ADC 芯片 GAIN=128, 10SPS 输出速率，5kg 重物测量条件下，误差约为 ±1%。开始称重前需进行校准，可参考下方代码进行操作。

```cpp

#include "HX711.h"

HX711 scale;

void setup() {
    // 1. 设置0g情况下ADC数值，并设为offset
    scale.tare();
}

void loop() {
    // 2. 读取标准重物(如5kg)情况下的ADC平均数值
    long kg_adc = scale.read_average(20);
    // 3. 读取当前0g情况下的offset
    kg_adc = kg_adc - scale.get_offset();
    // 4. 计算并配置scale参数
    scale.set_scale( kg_adc / (5 * 1000.0));
}

```

## 产品对比

::compare-table
| 产品对比表 | [Unit Scales](/zh_CN/unit/UNIT%20Scales) ![Unit Scales](https://static-cdn.m5stack.com/resource/docs/products/unit/UNIT%20Scales/img-d095bc9f-0f3f-4243-abde-82f8d6b67949.webp) | [Scales Kit](/zh_CN/app/scales_kit) ![Scales Kit](https://static-cdn.m5stack.com/resource/docs/products/app/scales_kit/scales_kit_cover_01.webp) | [Unit Mini Scales](/zh_CN/unit/Unit-Mini%20Scales) ![Unit Mini Scales](https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-Mini%20Scales/img-c370a473-d300-42c0-bf4c-cdf6d7963a6a.webp) | [Unit Weight](/zh_CN/unit/WEIGHT) ![Unit Weight](https://static-cdn.m5stack.com/resource/docs/products/unit/WEIGHT/img-e051022a-5e26-4ca5-9080-71eeb98fdf5e.webp) | [Unit Weight-I2C](/zh_CN/unit/Unit-Weight%20I2C) ![Unit Weight-I2C](https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-Weight%20I2C/img-998f3dae-bddd-4eea-8361-0c24821f367e.webp) |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 通信协议   | I2C                                                                                                                                                                             | ADC                                                                                                                                              | I2C                                                                                                                                                                                                 | ADC                                                                                                                                                               | I2C                                                                                                                                                                                             |
| 芯片方案   | STM32+HX711                                                                                                                                                                     | HX711                                                                                                                                            | STM32+HX711                                                                                                                                                                                         | HX711                                                                                                                                                             | STM32+HX711                                                                                                                                                                                     |
| 传感器量程 | 0~20kg                                                                                                                                                                          | 0~200kg                                                                                                                                          | 0~5kg                                                                                                                                                                                               | 取决应变片与控制芯片                                                                                                                                              | 取决应变片与控制芯片                                                                                                                                                                            |
::
