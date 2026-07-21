# Module DCMotor

<span class="product-sku">SKU:M021</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/lego_plus/lego_plus_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/lego_plus/lego_plus_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/lego_plus/lego_plus_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/lego_plus/lego_plus_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/lego_plus/lego_plus_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/lego_plus/lego_plus_06.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/lego_plus/lego_plus_07.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/lego_plus/lego_plus_08.webp">
</PictureViewer>

## 描述

**Module DCMotor** 是 M5Stack 堆叠模块系列中的一款，DC Motor 电机驱动模块。集成 MEGA328 和 L293DD 芯片，拥有 4 个电机驱动通道。采用直流电源输入设计用于功率补充，并通过 M5-Bus ，自动为顶部的 M5Core 供电。
使用 Module DCMotor 能够简单快速的驱动 RJ12 接口编码电机，比如乐高 ev3 电机 (本产品不附属于乐高或被乐高认可，LEGO 是乐高集团公司的商标)。

## 产品特性

- 通信协议: I2C (地址：0x56)
- DC 输入: 6-12V
- DC 连接器类型: XT30 (female)
- 4 x 电机驱动通道 (适用乐高 EV3-RJ12 接口编码电机)
- 2 x I2C HY2.0-4P 接口 (由 M5Core 的 A 端口进行拓展)

## 包装内容

- 1 x Module DCMotor
- 1 x 10cm 电机线
- 1 x DC 电源连接器

## 规格参数

| 规格         | 参数            |
| ------------ | --------------- |
| 通信接口     | I2C 通信 @ 0x56 |
| 电机驱动芯片 | L293DD          |
| 电源输入电压 | DC: 6-12V       |
| 电源接口规格 | XT30 (female)   |
| 电机接口规格 | ZH1.5-6P        |
| 产品重量     | 17g             |
| 毛重         | 48g             |
| 产品尺寸     | 54 x 54 x 12mm  |
| 包装尺寸     | 95 x 65 x 25mm  |
| 外壳材质     | Plastic ( PC )  |

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/module/lego_plus/lego_plus_sch_01.webp" width="80%">

## 管脚映射

### Mega328 ISP 下载接口 Pin 脚定义

<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-cardkb/mega328_isp_sch_01.webp" width="30%" height="30%">

MEGA328 芯片在默认情况下已经搭载了电机驱动程序。如果你想要更改其内部固件，则可以通过 **ISP** 端口进行升级。下图为 ISP 端口的位置.

<img src="https://static-cdn.m5stack.com/resource/docs/products/module/lego_plus/lego_plus_09.webp">

### M5-Bus

::m5-bus-table
| PIN      | LEFT | RIGHT | PIN      |
| -------- | ---- | ----- | -------- |
| GND      | 1    | 2     |          |
| GND      | 3    | 4     | PORT.B   |
| GND      | 5    | 6     |          |
|          | 7    | 8     |          |
|          | 9    | 10    | PORT.B   |
|          | 11   | 12    |          |
|          | 13   | 14    |          |
| TXD      | 15   | 16    | RXD      |
| SDA      | 17   | 18    | SCL      |
|          | 19   | 20    |          |
|          | 21   | 22    |          |
|          | 23   | 24    |          |
| HPWR     | 25   | 26    |          |
| HPWR     | 27   | 28    | 5V       |
| HPWR     | 29   | 30    | BAT+     |
::

## 软件开发

### Arduino

- [Module DCMotor Example with M5Core](https://github.com/m5stack/M5Stack/tree/master/examples/Modules/LEGO_PLUS)

### UiFlow1

- [Module DCMotor UiFlow1 文档](/zh_CN/uiflow/blockly/module/dc_motor)

### UiFlow2

- [Module DCMotor UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/module/dc_motor.html)

### 内置固件

- [Module DCMotor 内置固件](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/Module/LEGO_PLUS/firmware_328p)

### Easyloader

| Easyloader                                    | 下载链接                                                                                            | 备注 |
| --------------------------------------------- | --------------------------------------------------------------------------------------------------- | ---- |
| Module DCMotor Example Easyloader with M5Core | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Module/EasyLoader_LEGO_PLUS.exe) | /    |

## 相关视频

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Blog/Twitch201901/M5%20Tank.mp4" type="video/mp4">
</video>
