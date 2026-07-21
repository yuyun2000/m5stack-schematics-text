# Module 4EncoderMotor v1.1

<span class="product-sku">SKU:M138-V11</span>

<PictureViewer>
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Module_4EncoderMotor_V1.1/4.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Module_4EncoderMotor_V1.1/6.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Module_4EncoderMotor_V1.1/12.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Module_4EncoderMotor_V1.1/3.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Module_4EncoderMotor_V1.1/5.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Module_4EncoderMotor_V1.1/7.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Module_4EncoderMotor_V1.1/8.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Module_4EncoderMotor_V1.1/10.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Module_4EncoderMotor_V1.1/11.webp">
</PictureViewer>

## 描述

**Module 4EncoderMotor v1.1** 是一款 4 通道编码电机驱动模块，采用 STM32 + BL5617 H 桥驱动 IC 方案。以 I2C 通信的方式，支持从机地址修改，提供灵活的控制方式。通过 AB 脉冲编码信号输入，实现精准的电机运动状态和位置检测。支持占空比控制、绝对位置定位和速度调节等模式，实现电机的正转、反转、停止和制动等多种功能。集成 INA199 电源监控，实时监测电流状态。板载电源输入开关，可选择 DC 5V 或外部 DC 6 ~ 12V 电源输入。相比之前的 4EncoderMotor Module，本产品对接口进行了统一优化，采用统一的 HY2.0-6P 接口。适用于机器人运动控制、自动化设备、智能车辆、实验室设备和工业自动化系统等领域。

## 产品特性

- 4 通道编码电机驱动
- AB 脉冲信号输入
- 占空比，绝对位置定位，速度调节控制模式
- I2C 通讯方式
- (电机) 电压输入端及电流监控

## 包装内容

- 1 x Module 4EncoderMotor v1.1
- 4 x HY2.0-6P 单头接线 (20cm)
- 4 x PH2.0-6P 接口
- 1 x DC5521 Female To XT30 Female 线缆

## 应用场景

- 机器人运动控制
- 自动化设备
- 工业自动化系统

## 规格参数

| 规格             | 参数                           |
| ---------------- | ------------------------------ |
| MCU              | STM32F030C8T6                  |
| 编码电机驱动 IC  | BL5617                         |
| 电流检测芯片     | INA199                         |
| 支持最大电流     | 3.0A                           |
| 功率             | 最大 10W                       |
| 外接 DC 电源     | 6 ~ 12V                        |
| 通信接口         | I2C 通信 @ 0x24                |
| 待机电流         | DC 6V@35.03mA / DC 12V@19.25mA |
| PWM 驱动信号频率 | 1KHz                           |
| 工作温度         | 0°C ~ 40°C                     |
| 产品尺寸         | 54.0 x 54.0 x 13.1mm           |
| 产品重量         | 16.1g                          |
| 包装尺寸         | 95.0 x 66.0 x 26.0mm           |
| 毛重             | 57.8g                          |

## 操作说明

### 编码电机接线示例

<img style="width:70%" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Module_4EncoderMotor_V1.1/%E7%BA%BF%E5%BA%8F.jpg" alt="detail" />

## 原理图

- [Module 4EncoderMotor v1.1 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/566/SCH_4EncoderMotor_V1.1.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/566/SCH_4EncoderMotor_V1.1_sch_01.png">
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

<img alt="schematics" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Module_4EncoderMotor_V1.1/%E5%B0%BA%E5%AF%B8%E5%9B%BE.jpg" width="100%" />

## 数据手册

- [BL5617 Datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Module-4EncoderMotor/BL5617.pdf)

## 软件开发

### Arduino

- [Module 4EncoderMotor v1.1 Arduino 驱动库](https://github.com/m5stack/M5Module-4EncoderMotor)
- [Module 4EncoderMotor v1.1 Example with Basic](https://github.com/m5stack/M5Stack/blob/master/examples/Modules/4EncoderMotor/4EncoderMotor.ino)
- [Module 4EncoderMotor v1.1 Example with Core2](https://github.com/m5stack/M5Core2/blob/master/examples/Module/4EncoderMotor/4EncoderMotor.ino)
- [Module 4EncoderMotor v1.1 Example with CoreS3](https://github.com/m5stack/M5CoreS3/blob/main/examples/Module/4EncoderMotor/4EncoderMotor.ino)

### 内置固件

- [Module 4EncoderMotor v1.1 内置固件](https://github.com/m5stack/M5Module-4EncoderMotor-Internal-FW)

| 固件版本 | 修改记录                                                | 通信协议                                                                                                                                                            |
| -------- | ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| v3       | 首次发布时版本                                          | [Module 4EncoderMotor v1.1 I2C Protocol v3](https://github.com/m5stack/M5Module-4EncoderMotor-Internal-FW/blob/main/documents/Module-4EncodeMotorV1.1-PROTOCOL.pdf) |
| v4       | 1. 调整软启动功能，并允许为每台电机设置单独的旋转方向。 | 通信协议无变更，使用 v3 版本                                                                                                                                        |

\#> M5 DAPLink | 若您没有 STM32 下载器工具，可参考[M5 DAPLink](/zh_CN/guide/develop_tools/daplink)教程，使用 Core2 或 CoreS3 作为烧录器，为设备完成固件更新。

### 通信协议

- [Module 4EncoderMotor v1.1 I2C Protocol](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/975/Module-4EncodeMotorV1.1-PROTOCOL.pdf)

<img  src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/975/Module-4EncodeMotorV1.1-PROTOCOL_page_01.png" width="100%" />

## 相关视频

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Module_4EncoderMotor_V1.1/M138-V11%204EncoderMotor%20V1.1%20%E8%A7%86%E9%A2%91.mp4" type="video/mp4"></video>

## 产品对比

| 产品                            | 通信协议   | 芯片方案      | 控制电机类型        | 通道 | 控制模式                               | 备注                                                    |
| ------------------------------- | ---------- | ------------- | ------------------- | ---- | -------------------------------------- | ------------------------------------------------------- |
| 4EncoderMotor Module (M138)     | I2C (0x24) | STM32+BL5617  | 直流电机 / 编码电机 | 4    | 占空比，绝对位置定位，速度调节控制模式 |                                                         |
| 4EncoderMotor Module (M138-V11) | I2C (0x24) | STM32+BL5617  | 直流电机 / 编码电机 | 4    | 占空比，绝对位置定位，速度调节控制模式 | M138-V11 较 M138 修改了编码电机接口为 HY2.0-6P Grove 口 |
| DC Motor Module (M021)          | I2C (0x56) | MEGA328+L293D | 直流电机 / 编码电机 | 4    | 速度调节控制模式                       |                                                         |

<img style="width:70%" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Module_4EncoderMotor_V1.1/对比.jpg" alt="detail" />
