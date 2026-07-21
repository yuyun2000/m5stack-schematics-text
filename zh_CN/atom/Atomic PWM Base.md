# Atomic PWM Base

<span class="product-sku">SKU:A114</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic PWM Base/img-44bfbe9c-c370-4bfd-b439-8cfd0bf3fd6d.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic PWM Base/img-19ea5c5f-9bb4-4b1d-9d72-fe28207072f5.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic PWM Base/img-30913cf3-c70f-41da-91d8-e48a1b428365.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic PWM Base/img-b53ab201-9ab2-4fc7-8d09-1da9626ae474.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic PWM Base/img-0a1311c7-6040-4857-944c-cfc955f9d009.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic PWM Base/img-8e7588b5-82a0-4065-9c7d-a08243178960.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic PWM Base/img-8e7588b5-82a0-4065-9c7d-a08243178960.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/928/A114_Atomic_PWM_Base_weight.jpg">
</PictureViewer>

## 描述

**Atomic PWM Base** 是一款适配 Atom 系列主机的单通道 PWM 可调直流驱动器。支持 DC12 ~ 24V 电源输入，通过内置的 MOSFET 开关控制实现输出信号占空比调节，最大负载能力可达 12V@100W ，内置 DC-DC 降压电路，输入电源用于负载驱动的同时可为设备整机供电，应用部署更加便捷。结合 Atom 系列主控内置的 Wi-Fi 功能，可实现远程控制功能，适用于大功率直流电机 PWM 调速以及工业发热丝控制等应用场景。

## 产品特性

- 适用于 Atom-Lite/Atom-Matrix/AtomS3/AtomS3-Lite
- 单通道低延时 PWM 信号输出
- 大功率 MOSFET，输出能力 12V@100W
- 预留 1xGROVE 拓展接口
- 内置 DC-DC (12V->5V) 转换电路
- 一体化设计，自带保护外壳
- 开发平台：Arduino、UiFlow

## 包装内容

- 1 x Atomic PWM Base
- 1 x HT3.96-4P 端子

## 应用场景

- 直流电机控制
- LED 亮度调节
- 电源控制
- 温度控制

## 规格参数

| 规格         | 参数                  |
| ------------ | --------------------- |
| 驱动芯片     | EG27324               |
| MOSFET       | FDD8447L              |
| 最大输出功率 | 100W                  |
| 输入电压范围 | DC 12V-24V            |
| 驱动通道数   | 1                     |
| 电源指示灯   | 红色                  |
| 产品尺寸     | 24.0 x 48.0 x 18.0mm  |
| 产品重量     | 13.0g                 |
| 包装尺寸     | 136.0 x 92.0 x 20.0mm |
| 毛重         | 15.2g                 |

## 原理图

<img alt="schematics" src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic PWM Base/img-2d6a7113-0f87-4c13-be7a-4a9eecf72550.webp" width="100%" />

## 管脚映射

::m5-bus-table
| PIN | LEFT | RIGHT | PIN |
| --- | ---- | ----- | --- |
|     |      | 1     | 3V3 |
|     | 2    | 3     | PWM |
|     | 4    | 5     |     |
| 5V  | 6    | 7     |     |
| GND | 8    | 9     |     |
::

## 尺寸图

- [Atomic PWM Base模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/931/A092-atom-pwm.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/931/A092-atom-pwm_page_01.png" width="100%">

## 数据手册

- [FDD8447L](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/atombase/atom_pwm/C247783_FDD8447L_2018-10-11.PDF)
- [EG27324](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/atombase/atom_pwm/C189546_EG27324_2018-03-27.PDF)
- [ME3116AM6G](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/atombase/atom_pwm/C97643_ME3116AM6G_2017-03-22.PDF)

## 软件开发

### Arduino

- [Atomic PWM Base Arduino 快速上手](/zh_CN/arduino/projects/atomic/atomic_pwm_base)

### UiFlow1

- [Atomic PWM Base UiFlow1 文档](/zh_CN/uiflow/blockly/hardwares/pwm)

<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic PWM Base/uiflowCase-1702441811414atom_pwm_uiflow_01.png" width="100%"/>

### UiFlow2

- [Atomic PWM Base UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/base/pwm.html)

## 相关视频

- Atomic PWM Base 控制灯的亮度

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/AtomBase/ATOM_PWM_VIDEO.mp4" type="video/mp4"></video>
