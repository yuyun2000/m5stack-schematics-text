# Hat 8Servos v1.1

<span class="product-sku">SKU:U076-B</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat_8servos_1.1/hat_8servos_1.1_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat_8servos_1.1/hat_8servos_1.1_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat_8servos_1.1/hat_8servos_1.1_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat_8servos_1.1/hat_8servos_1.1_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat_8servos_1.1/hat_8servos_1.1_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat_8servos_1.1/hat_8servos_1.1_06.webp">
</PictureViewer>

## 描述

**Hat 8Servos v1.1** 是一款适配 M5Stick 系列的 8 通道舵机驱动板，采用 STM32F030F4 主控产生多路 PWM 信号用于舵机驱动，使用 I2C 通信协议控制，有效节省 IO 资源。内嵌由 MOS 管组成的舵机电源控制电路，支持编程动态控制电机释放 / 锁定。供电部分使用可反复充电的 16340/18350 锂电池（700mAh），亦可支持 18350 锂电池，8 通道同时工作下最大负载可达 **1.3A**，能够满足常规舵机规格驱动要求。

## 产品特性

- 8 通道舵机驱动
- 可编程电机供电控制
- 16340/18350 锂电池供电
- I2C 协议控制 (0x36)
- 带电池反接保护

## 包装内容

- 1 x Hat 8Servos v1.1
- 1 x 16340/18350 电池 (700mAh)

## 应用场景

- 舵机控制器
- 机器人控制
- 智能玩具

## 规格参数

| 规格               | 参数                            |  
| ------------------ | ------------------------------- |  
| MCU                | STM32F030F4P6                   |  
| 锂电池             | 规格: 16340 / 18350, 容量: 700mAh|  
| 驱动器舵机驱动通道 | 8 通道                          |  
| 驱动器最大负载能力 | 8 通道最大负载能力: DC 4.2V@1.3A|  
| 驱动器空载待机电流 | DC 4.2V@2.2uA                    |  
| 固定孔规格         | M3                              |  
| 通信接口           | I2C 通信 @ 0x36                  |  
| 产品尺寸           | 52.0 x 24.0 x 25.0mm             |  
| 产品重量           | 28.3g                           |  
| 包装尺寸           | 75.0 x 46.0 x 29.0mm             |  
| 毛重               | 39.7g                           |

## 原理图

- [Hat 8Servos v1.1 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/583/Sch_8ServoV1.1.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/583/Sch_8ServoV1.1_sch_01.png">
</SchViewer>

## 管脚映射

| M5StickC         | G0  | G26 | 3.3V | GND |
| ---------------- | --- | --- | ---- | --- |
| 8Servos HAT v1.1 | SDA | SCL | VIN  | GND |

## 尺寸图

- [Hat 8Servos v1.1 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/872/U076-B-8servov1_1.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/872/U076-B-8servov1_1_page_01.png" width="100%">

## 软件开发

### Arduino

- [Hat 8Servos v1.1 Arduino 驱动库](https://github.com/m5stack/M5Hat-8Servos)
- [Hat 8Servos v1.1 Example - with M5StickC](https://github.com/m5stack/M5Hat-8Servos/blob/master/examples/Hat_8Servos1.1_M5StickC/Hat_8Servos1.1_M5StickC.ino)
- [Hat 8Servos v1.1 Example - with M5StickC-Plus](https://github.com/m5stack/M5Hat-8Servos/blob/master/examples/Hat_8Servos1.1_M5StickCPlus/Hat_8Servos1.1_M5StickCPlus.ino)

### UiFlow1

- [Hat 8Servos v1.1 UiFlow1 文档](/zh_CN/uiflow/blockly/hat/8servo_v1.1)

### 内置固件

- [Hat 8Servos v1.1 内置固件](https://github.com/m5stack/HAT_8Servos_v1.1_Firmware)

### 通信协议

- 协议类型 I2C
- I2C Address: **0x36**

| hex  | len | R/W | description      | send params                                                             |
| ---- | --- | --- | ---------------- | ----------------------------------------------------------------------- |
| 0x00 | 1   | R/W | CH1 角度输出     | \[0] CH1 角度<br/>有效值范围：0-180                                     |
| 0x01 | 1   | R/W | CH2 角度输出     | \[0] CH2 角度<br/>有效值范围：0-180                                     |
| 0x02 | 1   | R/W | CH3 角度输出     | \[0] CH3 角度<br/>有效值范围：0-180                                     |
| 0x03 | 1   | R/W | CH4 角度输出     | \[0] CH4 角度<br/>有效值范围：0-180                                     |
| 0x04 | 1   | R/W | CH5 角度输出     | \[0] CH5 角度<br/>有效值范围：0-180                                     |
| 0x05 | 1   | R/W | CH6 角度输出     | \[0] CH6 角度<br/>有效值范围：0-180                                     |
| 0x06 | 1   | R/W | CH7 角度输出     | \[0] CH7 角度<br/>有效值范围：0-180                                     |
| 0x07 | 1   | R/W | CH8 角度输出     | \[0] CH8 角度<br/>有效值范围：0-180                                     |
| 0x10 | 2   | R/W | CH1 输出脉冲宽度 | \[0] CH1 脉冲宽度 HB<br/>\[1] CH1 脉冲宽度 LB<br/>有效值范围： 500-2500 |
| 0x12 | 2   | R/W | CH2 输出脉冲宽度 | \[0] CH2 脉冲宽度 HB<br/>\[1] CH1 脉冲宽度 LB<br/>有效值范围： 500-2500 |
| 0x14 | 2   | R/W | CH3 输出脉冲宽度 | \[0] CH3 脉冲宽度 HB<br/>\[1] CH1 脉冲宽度 LB<br/>有效值范围： 500-2500 |
| 0x16 | 2   | R/W | CH4 输出脉冲宽度 | \[0] CH4 脉冲宽度 HB<br/>\[1] CH1 脉冲宽度 LB<br/>有效值范围： 500-2500 |
| 0x18 | 2   | R/W | CH5 输出脉冲宽度 | \[0] CH5 脉冲宽度 HB<br/>\[1] CH1 脉冲宽度 LB<br/>有效值范围： 500-2500 |
| 0x1A | 2   | R/W | CH6 输出脉冲宽度 | \[0] CH6 脉冲宽度 HB<br/>\[1] CH1 脉冲宽度 LB<br/>有效值范围： 500-2500 |
| 0x1C | 2   | R/W | CH7 输出脉冲宽度 | \[0] CH7 脉冲宽度 HB<br/>\[1] CH1 脉冲宽度 LB<br/>有效值范围： 500-2500 |
| 0x1E | 2   | R/W | CH8 输出脉冲宽度 | \[0] CH8 脉冲宽度 HB<br/>\[1] CH1 脉冲宽度 LB<br/>有效值范围： 500-2500 |
| 0x30 | 1   | R/W | MOS 舵机电源控制 | \[0] MOS_CTL<br/>有效值范围： 0 (断电)/1 (供电)                         |

## 产品对比

| 规格           | 8Servos HAT | 8Servos HAT v1.1   |
| -------------- | ----------- | ------------------ |
| 电机电源控制   | /           | MOS 管控制电源通断 |
| 电池反接保护   | /           | 带保护电路         |
| 固定耳         | /           | 4x 易拆带孔固定耳  |
| 可编程 RGB LED | SK6812      | /                  |
| I2C ADDR       | 0x38        | 0x36               |
