# RoverC-Pro

<span class="product-sku">SKU:K036-B</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat_roverc_pro/hat_roverc_pro_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat_roverc_pro/hat_roverc_pro_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat_roverc_pro/hat_roverc_pro_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat_roverc_pro/hat_roverc_pro_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat_roverc_pro/hat_roverc_pro_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat_roverc_pro/hat_roverc_pro_06.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat_roverc_pro/hat_roverc_pro_07.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat_roverc_pro/hat_roverc_pro_08.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat_roverc_pro/hat_roverc_pro_09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1075/K036-B-weight.jpg">
</PictureViewer>

## 描述

**RoverC-Pro** 是一款可编程麦克纳姆轮全向移动机器人底座。与 M5StickC/M5StickC PLUS 兼容，只需插入 M5StickC/M5StickC PLUS 即可使用。主控芯片为 STM32F030C6T6, 由四个 N20 蜗杆减速电机组成，由电机驱动器 L9110S 驱动。PRO 版本提供了一个由舵机控制的夹持机构，用于夹持物体。底座上提供了两个舵机接口。此外，还有两个 Grove 兼容的 I2C 接口，以便于扩展其他模块。底座与乐高孔兼容，在结构上可以扩展。背面有一个 16340 (700mAh) 的可更换充电电池。底座电池可通过 M5StickC/M5StickC Plus 进行充电。在底座尾部有一个电源开关和指示灯。

## 产品特性

- I2C 地址 0x38
- 可遥控
- 带有夹持结构
- 可编程
- 全方位灵活移动
- 四通道电机驱动器
- 兼容乐高
- 额外的 Grove 接口用于扩展
- 配备 16340 (700mAh)

## 包装内容

- 1 x RoverC-Pro
- 1 x 夹爪套件

## 应用场景

- 迷你侦察车
- 小型移动机器人
- 智能玩具

## 规格参数

| 规格     | 参数                  |
| -------- | --------------------- |
| MCU      | STM32F030C8T6         |
| 通信协议 | I2C:0x38              |
| 产品尺寸 | 120.0 x 75.0 x 58.0mm |
| 产品重量 | 169.3g                |
| 包装尺寸 | 115.0 x 85.0 x 65.0mm |
| 毛重     | 245.0g                |

<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat_roverc_pro/hat_roverc_pro_010.webp" width="60%">

## 管脚映射

| M5StickC   | G26 | G0  | 5V  | GND |
| ---------- | --- | --- | --- | --- |
| RoverC HAT | SCL | SDA | 5V  | GND |
| I2C①       | SCL | SDA | 5V  | GND |
| I2C②       | SCL | SDA | 5V  | GND |

## 结构文件

- [RoverC-Pro 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/K036-B_RoverC-Pro/Structures)

## 软件开发

### Arduino

> 1: 该案例使用 RoverC 和 JoyC, 通过 UDP 通信实现无线控制。 请据你所使用的设备选择下方对应的案例程序。

- [RoverC-Pro & JoyC Remote Control - with M5StickC](https://github.com/m5stack/M5-RoverC/tree/master/examples/RoverC_M5StickC/JoyC_%26_RoverC)

- [RoverC-Pro & JoyC Remote Control - with M5StickC-Plus](https://github.com/m5stack/M5-RoverC/tree/master/examples/RoverC_M5StickCPlus/JoyC_%26_RoverC)

- 注意：开机后 RoverC 会显示 "M5AP+2 字节 mac 地址" 热点名称，同时 JoyC 会扫描到 RoverC 的 mac 地址名，长按 3 秒 JoyC 上的 M5StickC 的 Home 键，开始扫描小车的热点，即可配对成功。成功配对后屏幕左上角会高亮显示链接图标，同时屏幕显示摇杆数值。左摇杆上下控制前后，左右控制平移，右摇杆左右控制转向。

> 2: 该案例为 RoverC 单机控制程序，由主控直接控制。请据你所使用的设备选择下方对应的案例程序。

- [RoverC-Pro Example- with M5StickC](https://github.com/m5stack/M5-RoverC/blob/master/examples/RoverC_M5StickC/RunningRoverC/RunningRoverC.ino)
- [RoverC-Pro Example- with M5StickC-Plus](https://github.com/m5stack/M5-RoverC/blob/master/examples/RoverC_M5StickCPlus/RunningRoverC/RunningRoverC.ino)

### UiFlow1

- [RoverC-Pro UiFlow1 文档](/zh_CN/uiflow/blockly/hat/roverc)

### 通信协议

- 通讯类型：I2C

- I2C 通讯地址: **0x38**

- [RoverC-Pro I2C Protocol](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/hat/hat_roverc_pro/K036-B_I2C_PROTOCOL_CN.pdf)

### Easyloader

| Easyloader            | 下载链接                                                                                                        | 备注 |
| --------------------- | --------------------------------------------------------------------------------------------------------------- | ---- |
| RoverC-Pro Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/HAT/EasyLoader_RoverC_PRO_Alone.exe) | /    |

## 相关视频

<video id="example_video" controls>
  <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/HAT/RoverC.Pro.mp4" type="video/mp4">
</video>

## 产品对比

::compare-table

| 产品对比     | [RoverC PRO](/zh_CN/hat/hat_roverc_pro) ![RoverC PRO](https://static-cdn.m5stack.com/resource/docs/products/hat/hat_roverc_pro/hat_roverc_pro_cover_01.webp) | [RoverC](/zh_CN/hat/hat-roverc) ![RoverC](https://static-cdn.m5stack.com/resource/docs/products/hat/hat-roverc/hat-roverc_01.webp) |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------- |
| 舵机爪手     | x1                                                                                                                                                           | /                                                                                                                                  |
| 舵机拓展接口 | x2                                                                                                                                                           | /                                                                                                                                  |
| 电池         | 可拆卸                                                                                                                                                       | 不可拆卸                                                                                                                           |

::
