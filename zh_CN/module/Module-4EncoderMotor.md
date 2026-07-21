# Module 4EncoderMotor

<span class="product-sku">SKU:M138</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Module-4EncoderMotor/img-b0ee8659-161f-4ffd-ac50-3702aa06a60b.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Module-4EncoderMotor/img-307ac5c9-8c75-4671-94d4-2353e2edb3d8.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Module-4EncoderMotor/img-9fecb43c-8282-4035-88fe-662f53d0048c.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Module-4EncoderMotor/img-40f26607-4844-4974-a0a0-512f17cf15bb.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Module-4EncoderMotor/img-49c730ec-493b-4246-be03-361334984480.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Module-4EncoderMotor/img-61742204-6731-4010-a31c-58c6a794e279.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Module-4EncoderMotor/img-4b944517-423a-4bc3-8ad4-d7d1d15349f4.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Module-4EncoderMotor/img-6662d022-e83f-41db-8edc-b1e38c2481ac.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Module-4EncoderMotor/img-e37c789d-4f98-4e6a-8d79-a9b5bec45245.webp">
</PictureViewer>

## 描述

**Module 4EncoderMotor** 是一款 4 通道编码电机驱动模块，采用 **STM32 + BL5617 H 桥驱动 IC** 方案。以 I2C 通信方式，支持从机地址修改，提供灵活的控制方式。通过 AB 脉冲编码信号输入，实现精准的电机运动状态和位置检测。支持占空比控制、绝对位置定位和速度调节等模式，实现电机的正转、反转、停止和制动等多种功能。集成 INA199 电源监控，实时监测电压和电流状态。板载电源输入开关，可选择 DC 5V 或外部 DC 6 ~ 12V 电源输入。适用于机器人运动控制、自动化设备、智能车辆、实验室设备和工业自动化系统等领域。

## 产品特性

- 4 通道编码电机驱动
- AB 脉冲信号输入
- 占空比，绝对位置定位，速度调节控制模式
- I2C 通讯方式
- 电源电流电压监控

## 包装内容

- 1 x Module 4EncoderMotor
- 1 x DC5521 Female To XT30 Female 线缆
- 4 x KF2510-2P 100mm

## 应用场景

- 机器人运动控制
- 自动化设备
- 智能车辆
- 工业自动化系统

## 规格参数

| 规格            | 参数                 |
| --------------- | -------------------- |
| MCU             | STM32F030C8T6        |
| 编码电机驱动 IC | BL5617               |
| 支持最大电流    | 3.0A                 |
| 功率            | 最大 10W             |
| 外接 DC 电源    | 6 ~ 12V              |
| 通信接口        | I2C 通信 @ 0x24      |
| 工作温度        | 0°C ~ 40°C           |
| 产品尺寸        | 54.0 x 54.0 x 13.1mm |
| 产品重量        | 15.8g                |
| 包装尺寸        | 95.0 x 66.0 x 26.0mm |
| 毛重            | 45.7g                |

## 原理图

- [Module 4EncoderMotor 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/564/SCH_4EncoderMotor_V1.0.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/564/SCH_4EncoderMotor_V1.0_sch_01.png">
</SchViewer>

## 管脚映射

### 电流电压检测引脚

| STM32                | PB0      | PB1      |
| -------------------- | -------- | -------- |
| Motor Voltage Detect | ADC1_OUT |          |
| Current Detect       |          | ADC2_OUT |

### 电机方向控制引脚

| STM32              | PB14/PB15               | PB12/PB13               | PB4/PB5                 | PA15/PB3                |
| ------------------ | ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| BL5617 (Direction) | MCU_DIR_M1R/MCU_DIR_M1F | MCU_DIR_M2R/MCU_DIR_M2F | MCU_DIR_M3R/MCU_DIR_M3F | MCU_DIR_M4R/MCU_DIR_M4F |

### PWM 控制引脚

| STM32        | PA9        | PA8        | PA11       | PA10       |
| ------------ | ---------- | ---------- | ---------- | ---------- |
| BL5617 (PWM) | MCU_PWM_M1 | MCU_PWM_M2 | MCU_PWM_M3 | MCU_PWM_M4 |

### A/B 信号检测引脚

| STM32             | PA6/PA7   | PA4/PA5   | PB9/PB8   | PB7/PB6   |
| ----------------- | --------- | --------- | --------- | --------- |
| Encodering motors | E1_A/E1_B | E2_A/E2_B | E3_A/E3_B | E4_A/E4_B |

### M5-Bus

::m5-bus-table
| PIN  | LEFT | RIGHT | PIN |
| ---- | ---- | ----- | --- |
| GND  | 1    | 2     |     |
| GND  | 3    | 4     |     |
| GND  | 5    | 6     | RST |
|      | 7    | 8     |     |
|      | 9    | 10    |     |
|      | 11   | 12    |     |
|      | 13   | 14    |     |
|      | 15   | 16    |     |
| SDA  | 17   | 18    | SCL |
|      | 19   | 20    |     |
|      | 21   | 22    |     |
|      | 23   | 24    |     |
| HPWR | 25   | 26    |     |
| HPWR | 27   | 28    | 5V  |
| HPWR | 29   | 30    | BAT |
::

## 尺寸图

<img alt="module size" src="https://static-cdn.m5stack.com/resource/docs/products/module/Module-4EncoderMotor/img-73870d56-ff90-4f1d-aec1-caa153976af3.jpg" width="100%" />

## 数据手册

- [BL5617 Datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Module-4EncoderMotor/BL5617.pdf)

## 软件开发

### Arduino

- [Module 4EncoderMotor Arduino 驱动库](https://github.com/m5stack/M5Module-4EncoderMotor)
- [Module 4EncoderMotor Example with Basic](https://github.com/m5stack/M5Stack/blob/master/examples/Modules/4EncoderMotor/4EncoderMotor.ino)
- [Module 4EncoderMotor Example with Core2](https://github.com/m5stack/M5Core2/blob/master/examples/Module/4EncoderMotor/4EncoderMotor.ino)
- [Module 4EncoderMotor Example with CoreS3](https://github.com/m5stack/M5CoreS3/blob/main/examples/Module/4EncoderMotor/4EncoderMotor.ino)

### UiFlow1

- [Module 4EncoderMotor UiFlow1 文档](/zh_CN/uiflow/blockly/module/4encoder_motor)

### UiFlow2

- [Module 4EncoderMotor UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/module/encoder4_motor.html)

### Internal Firmware

- [Module 4EncoderMotor 内置固件](https://github.com/m5stack/M5Module-4EncoderMotor-Internal-FW/tree/V1.0)

### 通信协议

- [Module 4EncoderMotor I2C 通信协议](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/974/4EncoderModule.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/975/Module-4EncodeMotorV1.1-PROTOCOL_page_01.png" width="100%" />

### Easyloader

\#>Module 4EncoderMotor 内置固件升级程序 Easyloader。

| Easyloader                                       | 下载链接                                                                                                                                      | 备注 |
| ------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------- | ---- |
| Module 4EncoderMotor Firmware Upgrade Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Module-4EncoderMotor/4Encoder%20Firmware%20Upgrade.exe) | /    |

## 相关视频

- Module 4EncoderMotor 功能介绍

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Module-4EncoderMotor/M138%204EncoderMotor%20Module%20%E8%A7%86%E9%A2%91.mp4" type="video/mp4"></video>
