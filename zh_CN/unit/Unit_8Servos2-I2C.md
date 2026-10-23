# Unit 8Servos2-I2C

<span class="product-sku">SKU:U222</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1281/U222_Unit_8Servos2-I2C_main_pictures_01.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1281/U222_Unit_8Servos2-I2C_main_pictures_02.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1281/U222_Unit_8Servos2-I2C_main_pictures_03.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1281/U222_Unit_8Servos2-I2C_main_pictures_04.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1281/U222_Unit_8Servos2-I2C_main_pictures_05.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1281/U222_Unit_8Servos2-I2C_main_pictures_06.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1281/U222_Unit_8Servos2-I2C_main_pictures_07.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1281/U222_Unit_8Servos2-I2C_main_pictures_08.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1281/U222_Unit_8Servos2-I2C_main_pictures_09.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1281/U222_Unit_8Servos2-I2C_main_pictures_10.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1281/U222_Unit_8Servos2-I2C_main_pictures_11.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1281/U222-weight.jpg">
</PictureViewer>

## 描述

**Unit 8Servos2-I2C** 是一款 8 通道舵机级联控制单元，内置 **STM32G031G8U6** 核心主控，采用 I2C 通信接口，提供 8x 可配置 IO 通道，支持配置多种工作模式：舵机控制、数字输入 / 输出、ADC 输入、RGB LED 控制和 PWM 模式。
板载两组 HY2.0-4P 接口，硬件上两组接口相连共用同一 I2C 总线，并且配备 16 档旋转编码开关，用于灵活配置设备 I2C 地址，方便扩展连接其他 I2C 设备。本单元支持 DC 9 ~ 24V 输入，内置 SY8303AIC 降压电路提供 5V 电源，降压电路最大输出总电流为 3A。板载 INA199A1DCKR 电流检测电路，可采集舵机总电流，并设有输入电压及 5V 电源电压采样电路、电源状态指示灯，适用于多舵机控制、机器人关节驱动、智能玩具等应用场景。

## 产品特性

- STM32G031G8U6 核心主控
- 8x 可配置 IO 通道，支持配置多种工作模式：
  - 舵机控制
  - 数字输入 / 输出
  - ADC 输入
  - RGB LED 控制
  - PWM 模式
- 通信接口与地址配置
  - I2C 通信接口
  - 2x HY2.0-4P 接口支持多 I2C 设备扩展
  - 16 档旋转编码开关配置 I2C 地址
- 电源与检测
  - DC 9 ~ 24V 电源输入，内部集成 5V@3A 降压电路（外设驱动 + HY2.0-4P 输出主控供电）
  - 集成舵机总电流监测
  - DC 输入电压检测
  - 5V 电源电压检测
- 状态指示
  - 红色指示灯：DC 电源接口状态指示灯（接口电压高于 8.5V 时点亮）
  - 绿色指示灯：HY2.0-4P 接口欠压状态指示灯（接口电压低于 4.5V 时点亮）

## 包装内容

- 1 x Unit 8Servos2-I2C
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 多舵机控制
- 机器人关节驱动
- 智能玩具
- STEAM 教育

## 规格参数

| 规格            | 参数                                                                       |
| --------------- | -------------------------------------------------------------------------- |
| MCU             | STM32G031G8U6                                                              |
| 可配置 IO 通道  | 8 路，支持工作模式：舵机控制、数字输入 / 输出、ADC 输入、RGB LED、PWM 模式 |
| IO 通道接口     | 8 x 2.54-3P                                                                |
| 通信接口        | I2C 通信 @ 0x25 ~ 0x34                                                     |
| DC 电源输入接口 | 输入电压：DC 9 ~ 24V，规格：5.5 x 2.1mm，极性：内正外负                    |
| 降压芯片        | SY8303AIC                                                                  |
| 电源输出        | DC 5V，最大 3A（板上各路负载共用）                                         |
| 电流检测电路    | INA199A1DCKR，搭配 10mΩ 采样电阻                                           |
| 指示灯          | 红色 DC 输入 监测指示灯、绿色欠压监测指示灯                                |
| 待机功耗        | DC 12V@4.56mA                                                              |
| 工作功耗        | DC 12V@1.6A（8 路舵机负载）                                                |
| 产品尺寸        | 56.0 x 24.0 x 11.5mm                                                       |
| 产品重量        | 11.6g                                                                      |
| 包装尺寸        | 138.0 x 93.0 x 13.0mm                                                      |
| 毛重            | 17.2g                                                                      |

## 原理图

- [Unit 8Servos2-I2C 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1281/SCH_Unit_8Servos2-I2C_V0.4_SCH_PDF_20260526_2026_05_26_11_47_47.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1281/SCH_Unit_8Servos2-I2C_V0.4_SCH_PDF_20260526_2026_05_26_11_47_47_page_01.png">
</SchViewer>

## 管脚映射

### HY2.0-4P

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| IN & OUT | GND   | 5V  | SDA    | SCL   |
::

#>输入输出接口说明|Unit 8Servos2-I2C 输入与输出接口，内部相连，可用于级联挂载更多 Unit 8Servos2-I2C 或 I2C 设备。

### I2C 地址对照表

| 旋转编码开关 | I2C 地址 |
| ------------ | -------- |
| 0            | 0x25     |
| 1            | 0x26     |
| 2            | 0x27     |
| 3            | 0x28     |
| 4            | 0x29     |
| 5            | 0x2A     |
| 6            | 0x2B     |
| 7            | 0x2C     |
| 8            | 0x2D     |
| 9            | 0x2E     |
| A            | 0x2F     |
| B            | 0x30     |
| C            | 0x31     |
| D            | 0x32     |
| E            | 0x33     |
| F            | 0x34     |

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1281/U222_Unit_8Servos2-I2C_Rotary_Encoder.png" width="60%">

## 尺寸图

- [Unit 8Servos2-I2C 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1281/U222_Unit_8Servos2-I2C_model_size.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1281/U222_Unit_8Servos2-I2C_model_size_page_01.png" width="100%">

## 数据手册

- [INA199A1DCKR 数据手册](https://www.ti.com/lit/ds/symlink/ina199.pdf)

## 软件开发

### Arduino

- [Unit 8Servos2-I2C Arduino 驱动库](https://github.com/m5stack/M5Unit-8Servos2-I2C)
- [Unit 8Servos2-I2C Arduino 使用教程](/zh_CN/arduino/projects/unit/unit_8servos2_i2c)

### 内置固件

- [Unit 8Servos2-I2C 内置固件](https://github.com/m5stack/M5Unit-8Servos2-I2C-Internal-FW)

### 通信协议

<MarkdownPreview src="/zh_CN/protocol/U222/I2C" title="查看通信协议" />

## 相关视频

<VideoGallery>
  <VideoItem title="Unit 8Servos2-I2C 与 Unit 8Servos2-Chain 产品介绍以及功能展示" url="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1281/U222_U223_video_CN.mp4" />
</VideoGallery>

## 产品对比

::compare-table
| 产品对比表   | [Unit 8Servos2-I2C](/zh_CN/unit/Unit_8Servos2-I2C) ![Unit 8Servos2-I2C](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1281/U222_Unit_8Servos2-I2C_main_pictures_02.jpg) | [Unit 8Servos2-Chain](/zh_CN/unit/Unit_8Servos2-Chain) ![Unit 8Servos2-Chain](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1280/U223_Unit_8Servos2-Chain_main_pictures_02.jpg) |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 通信接口     | I2C                                                                                                                                                                        | UART (Chain Protocol)                                                                                                                                                              |
| 节点扩展     | I2C 地址：0x25 ~ 0x34                                                                                                                                                      | Chain 链路级联                                                                                                                                                                     |
| 通道数量     | 8                                                                                                                                                                          | 8                                                                                                                                                                                  |
| 工作模式     | 数字输入输出 / 舵机 / ADC / RGB / PWM                                                                                                                                      | 数字输入输出 / 舵机 / ADC / RGB / PWM                                                                                                                                              |
| 电源输入     | DC 9 ~ 24V                                                                                                                                                                 | DC 9 ~ 24V                                                                                                                                                                         |
| 舵机供电     | DC 5V                                                                                                                                                                      | DC 5V                                                                                                                                                                              |
| 电流检测     | INA199                                                                                                                                                                     | INA199                                                                                                                                                                             |
| 主控芯片     | STM32G031G8U6                                                                                                                                                              | STM32G031G8U6                                                                                                                                                                      |
::
