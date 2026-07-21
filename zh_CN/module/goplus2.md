# Module13.2 GoPlus2

<span class="product-sku">SKU:M025-B</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/goplus2/goplus2_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/goplus2/goplus2_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/977/M025-B-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/goplus2/goplus2_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/goplus2/goplus2_06.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/goplus2/goplus2_07.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/goplus2/goplus2_08.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/goplus2/goplus2_09.webp">
</PictureViewer>

## 描述

**Module13.2 GoPlus2** 是一款可堆叠的多功能电机舵机控制模块。下位机采用 STM32F030C8T6，模块配备 2 路直流电机驱动接口，4 路舵机驱动接口，可扩展 3 个 PORT-B 接口，满足模拟输入、数字输入输出的需求，同时支持红外 (IR) 发射与接收。模块提供一个 DC 直流电源接口用于外部供电，此外模块内部有 500mAh 电池，可通过 M5Core 主机对其充电。

### 产品特性

- 2x 直流电机驱动通道
- 4x 舵机驱动通道
- IR 发射 & 接收
- 3x 拓展 PORT B
- 电源指示灯
- 内置 500mAh 电池
- 主控芯片 STM32F030C8T6
- 通信协议：I2C (0x38)

### 包装内容

- 1 x Module13.2 GoPlus2
- 2 x DC Motor 连接线

## 应用场景

- 舵机 / 电机驱动器
- 多路输入输出信号采集与控制
- 红外控制器
- DIY 玩具底座

## 规格参数

| 规格     | 参数                                |
| -------- | ----------------------------------- |
| 主控芯片 | STM32F030C8T6                       |
| 外设接口 | DC Motor x 2, PORT-B x 3, Servo x 4 |
| 电机驱动 | DRV8833                             |
| 红外     | 发射与接收功能                      |
| 电池     | 500mAh                              |
| 通信接口 | I2C 通信 @ 0x38                     |
| 产品尺寸 | 54.0 x 54.0 x 13.0mm                |
| 产品重量 | 38.0g                               |
| 包装尺寸 | 133.0 x 95.0 x 20.0mm               |
| 毛重     | 58.0g                               |

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/module/goplus2/goplus2_sch_01.webp" width="80%">

## 管脚映射

### M5-Bus

::m5-bus-table
| PIN      | LEFT | RIGHT | PIN      |
| -------- | ---- | ----- | -------- |
| GND      | 1    | 2     | IR_IN    |
| GND      | 3    | 4     |          |
| GND      | 5    | 6     | RST      |
|          | 7    | 8     |          |
|          | 9    | 10    |          |
|          | 11   | 12    | 3V3      |
|          | 13   | 14    |          |
|          | 15   | 16    |          |
| SDA      | 17   | 18    | SCL      |
|          | 19   | 20    |          |
|          | 21   | 22    | IR_OUT   |
|          | 23   | 24    |          |
| HPWR     | 25   | 26    |          |
| HPWR     | 27   | 28    | 5V       |
| HPWR     | 29   | 30    | BAT      |
::

## 尺寸图

[Module13.2 GoPlus2 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/977/goplus2.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/977/goplus2_page_01.png" width="100%">

## 数据手册

- [DRV8833 数据手册](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/DRV8833_datasheet.pdf)

## 软件开发

### Arduino

- [Module13.2 GoPlus2 Example with M5Core](https://github.com/m5stack/M5Stack/tree/master/examples/Modules/GoPLUS2)

### UiFlow1

- [Module13.2 GoPlus2 UiFlow1 文档](/zh_CN/uiflow/blockly/module/goplus2)

### UiFlow2

- [Module13.2 GoPlus2 UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/module/goplus2.html)

### 通信协议

- [Module13.2 GoPlus2 I2C Protocol](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/GO%20PLUS2%20Guide.docx)

### Easyloader

| Easyloader                                        | 下载链接                                                                                                  | 备注 |
| ------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | ---- |
| Module13.2 GoPlus2 Example Easyloader with M5Core | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/MODULE/EasyLoader_GoPlus2.exe) | /    |

## 相关视频

<video id="example_video" controls>
  <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Module/GoPlus2.mp4" type="video/mp4">
</video>
