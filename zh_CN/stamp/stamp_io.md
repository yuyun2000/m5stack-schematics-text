# Stamp IO

<span class="product-sku">SKU:S002</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/stamp/stamp_io/stamp_io_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/stamp/stamp_io/stamp_io_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1031/S002-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/stamp/stamp_io/stamp_io_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/stamp/stamp_io/stamp_io_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/stamp/stamp_io/stamp_io_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/stamp/stamp_io/stamp_io_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1031/S002_Stamp_IO_weight.jpg">
</PictureViewer>

## 描述

**Stamp IO** 是一款**IO 拓展板**, 该拓展板基于 STM32F030 主控开发，采用 I2C 通信接口，提供 8 路 IO 拓展。每路 IO 支持独立配置**数字输入 / 输出**， **ADC**, **SERVO 控制**, **RGB LED 控制**模式。适用于多路数字 / 模拟信号采集，与灯光 / 舵机控制等应用场景。

## 产品特性

- 8 通道输入输出拓展：
  - 数字输入 / 输出
  - ADC 输入
  - SERVO 控制 (PWM)
  - RGB LED 控制
  - IO 引脚 PWM 输出功能
- I2C 通信接口:
  - 支持配置 I2C 地址
- 多形态
  - 支持多种应用形态 (SMT,DIP, 飞线)
  - 配有高温塑料铠装，支持 SMT 过炉温度 (230°C)

## 包装内容

- 1 x Stamp IO
- 1 x HY2.0-4P 母座 (红色)
- 1 x 内六角扳手 L 形 1.5mm (适配 M2 螺丝)

## 应用场景

- IO 拓展
- 舵机控制
- 多路灯光控制
- 多路模拟信号采集

## 规格参数

| 规格                   | 参数                                           |
| ---------------------- | ---------------------------------------------- |
| MCU                    | STM32F030F4P6                                  |
| 通信接口               | I2C 通信 @ 0x45                                |
| IO 扩展数量            | 8                                              |
| IO 支持模式            | 数字输入 / 输出，ADC, SERVO 控制，RGB LED 控制 |
| IO 支持输入 / 输出电平 | 3.3V                                           |
| 产品尺寸               | 15.0 x 4.7 x 16.0mm                            |
| 产品重量               | 1.5g                                           |
| 包装尺寸               | 138.0 x 93.0 x 10.0mm                          |
| 毛重                   | 4.9g                                           |

## 操作说明

### 外壳支持回流焊温度曲线

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/stamp_pico/stamp_pico_11_cn.webp">

## 原理图

- [Stamp IO 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/568/Sch_StampIO.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/568/Sch_StampIO_sch_01.png">
</SchViewer>

## 尺寸图

- [Stamp IO 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1031/S002-model-size-STAMP-IO.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1031/S002-model-size-STAMP-IO_page_01.png" width="100%">

## 软件开发

### Arduino

- [ADC Input](https://github.com/m5stack/M5Unit-EXTIO2/blob/main/examples/Unit_EXTIO2_M5Core/ADC_INPUT/ADC_INPUT.ino)
- [Digital Input/Output](https://github.com/m5stack/M5Unit-EXTIO2/blob/main/examples/Unit_EXTIO2_M5Core/DIGITAL_INPUT_OUTPUT/DIGITAL_INPUT_OUTPUT.ino)
- [RGB LED Control](https://github.com/m5stack/M5Unit-EXTIO2/blob/main/examples/Unit_EXTIO2_M5Core/RGB_LED_CTL/RGB_LED_CTL.ino)
- [Servo Control](https://github.com/m5stack/M5Unit-EXTIO2/blob/main/examples/Unit_EXTIO2_M5Core/SERVO_CTL/SERVO_CTL.ino)

### 内置固件

- [M5Unit-EXTIO2-Internal-FW](https://github.com/m5stack/M5Unit-EXTIO2-Internal-FW)

### 通信协议

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/stamp/stamp_io/map.png" width="80%">
