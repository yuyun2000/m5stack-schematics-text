# Demo Board

<span class="product-sku">SKU:K024</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/demo-board/demo-board_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/demo-board/demo-board_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/demo-board/demo-board_03.webp">
</PictureViewer>

## 描述

**Demo Board** 是一款学习开发板。采用 M5Core 作为控制核心，完全兼容模块堆叠与硬件拓展体系。配备多组环境检测相关的传感器，提供摇杆、旋转编码、矩阵按键、无线射频识别等多种输入方式。包含三种电机驱动方式 (直流、步进、舵机),RGB LED 灯板、集成多组继电器控制与 ADC、DAC 转换电路，支持 RS485、RS232 总线通信，并为每一个模块提供独立电源开关。结合自带物联网属性的 M5Core 用作控制核心，板载模块涵盖了 "声、光、电、力" 学等多个方面，Demo Board 会是你学习硬件、编程的一大利器.

## 产品特性

- 兼容 Module 堆叠、Unit 拓展体系
- Proto 板、M5-BUS 总线拓展
- 各模块带有独立电源开关
- 环境传感器系列 (温度、湿度、气压、光线、麦克风)
- 摇杆输入
- 8 路继电器输出
- 4 路 DAC,4 路 ADC
- 4x4 按键矩阵
- 8x8 矩阵 RGB LED
- 旋转编码器
- 单路舵机
- 直流电机 (带反馈)
- 四相五线制步进电机
- 无线射频识别读卡器
- RS-485,RS232 通信功能

## 包装内容

- 1 x Demo Board
- 1 x DC 12V 电源适配器 (5.5 x 2.1mm)
- 1 x RS232 连接线
- 1 x RFID Card
- 1 x ID Card
- 16 x 面包线

## 操作说明

### 模块布局

<img src="https://static-cdn.m5stack.com/resource/docs/products/app/demo-board/demo-board_04.webp" width="100%">

### 模块参数

| 模块名称   | 工作电压 | 相关参数                             |
| ---------- | -------- | ------------------------------------ |
| ADC        | 5V       | 4 通道 ADC 接口 / 内置 ADS1115       |
| DAC        | 5V       | 4 通道 DAC 接口 / 内置 DAC6574       |
| Joystick   | 3.3V     | X/Y 轴电位器输入，Z 轴按键输入       |
| DHT12      | 3.3V     | I2C 地址 0x5C                        |
| BMP280     | 3.3V     | I2C 地址 0x76                        |
| Light      | 3.3V     | 支持模拟量 / 数字量采集 / 可调节阀值 |
| Microphone | 3.3V     | 支持模拟量 / 数字量采集 / 可调节阀值 |
| Relay      | 5V       | 8 路控制 / 3A-220V-AC/3A-30V-DC      |
| RGB LED    | 5V       | 8x8 矩阵灯                           |
| Servo      | 5V       | 10KG 扭力                            |
| DC-Motor   | 5V       | 带反馈，集成 LV8548MC                |
| Stepmotor  | 5V       | 四相五线制 集成 LV8548MC             |
| RFID       | 3.3V     | 读写距离: < 8 cm / 内置 MFRC522      |
| RS485      | 5V       | 内置 SP485EEN-L/TR                   |
| RS232      | 5V       | 内置 MAX232ESE                       |
| Encode     |          | 旋转编码器 / 带按键输入              |
| Proto      |          | 板孔数量 x170                        |
| Keyboard   |          | 4x4 按键矩阵                         |

## 原理图

- [Demo Board 原理图 PDF](https://github.com/m5stack/M5-Schematic/tree/master/Applications/M5IoT-kit)

## 数据手册

- [ADS1115](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/application/ads1115_en.pdf)
- [DAC6574](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/application/dac6574_en.pdf)
- [LV8548MC](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/application/LV8548MC_en.pdf)
- [TPS54360](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/application/tps54360_en.pdf)
- [MRC522](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/MFRC522_en.pdf)
- [MAX232ESE](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/application/MAX232ESE_en.pdf)
- [MAX4466](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/application/MAX4466_datasheet_en.pdf)
- [SP485EEN](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/hat/SP485EEN_en.pdf)
- [BMP280](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/hat/BMP280-DS001-11_en.pdf)

## 软件开发

### 快速上手

- [Demo Board上手教程PDF](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/Demo-Board_cn_sht30.pdf)

### Arduino

- [Demo Board 测试程序](https://github.com/m5stack/DEMO-BOARD)

\#> 注意事项 | DAC 功能和 ADC 功能不能同时使用，因为 ADS1115 和 DAC6574 芯片的广播地址 (0x48) 相同导致功能冲突。

### Easyloader

| Easyloader                 | 下载链接                                                                                                                   | 备注 |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ---- |
| Demo Board Test Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Application/Demo%20Board/EasyLoader_APP_Demo_Board.exe) | /    |
