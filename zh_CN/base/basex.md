# Base X

<span class="product-sku">SKU:K037</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/basex/basex_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/basex/basex_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1010/K037_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/basex/basex_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/basex/basex_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/basex/basex_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/basex/basex_06.webp">
</PictureViewer>

## 描述

**Base X** 是一款兼容乐高 EV3 电机的专用底座，结构设计上与 BASE26 类似，支持多种方式进行固定，并且额外提供一个乐高连接底座，在搭建乐高结构时可以将 **Base X** 轻松嵌入到作品中。**Base X** 可同时接入 4 路（RJ11）乐高电机，支持角度 / 速度的读取和控制，完美兼容原有电机功能。此外，底座提供 2 个舵机接口，可以直接控制舵机旋转角度，一个内置的 PDM 麦克风可以采集声音。为了适应不同的使用场景，提供一个 UART 接口（16/17）与一个 GPIO 接口（26/36），接入各类传感器更加灵活。底座内置一块 950mAh 电池，可通过 M5Core 的 USB Type-C 接口进行充电，延长续航时间。为了提高接口的驱动能力，在底座上配备了 DC 电源插孔，可以通过外部 9 ~ 12V 直流电源为电机供电（不能通过底座进行充电）。

## 产品特性

- 4 路 RJ12 乐高电机接口（底座合计最大电流输出能力 2A）
- 2 路舵机驱动（底座合计最大电流输出能力 2A）
- 1 路 UART
- 1 路 GPIO
- 内置 PDM 麦克风（G34）
- 板载 DC-DC 转换（9 ~ 12V 输入，仅为电机独立供电）
- 内置 950mAh 电池
- 多种固定方式 / 支持乐高孔连接

## 应用场景

- 乐高编码电机 / 舵机控制器
- 乐高玩具 DIY 智能控制

## 包装内容

- 1 x Base X
- 1 x 乐高底座
- 2 x M3 \* 5mm 304 不锈钢内六角螺栓
- 2 x M3 \* 32mm 304 不锈钢内六角螺栓
- 1 x 内六角扳手 L 形 2.5mm (适配 M3 螺丝)

## 规格参数

| 规格     | 参数                  |
| -------- | --------------------- |
| MCU      | STM32F030C8T6         |
| 通信接口 | I2C 通信 @ 0x22       |
| 产品尺寸 | 54.0 x 54.0 x 26.0mm  |
| 产品重量 | 59.0g                 |
| 包装尺寸 | 150.0 x 65.0 x 40.0mm |
| 毛重     | 110.0g                |

## 管脚映射

### M5-Bus

\#> Switch | 下方 M5-Bus 中标记 `SW` 的引脚，可通过拨码开关进行切换，用于适配不同的主控设备。

::m5-bus-table
| PIN     | LEFT | RIGHT | PIN           |
| ------- | ---- | ----- | ------------- |
| GND     | 1    | 2     | NC            |
| GND     | 3    | 4     | PORT.B        |
| GND     | 5    | 6     | NC            |
| NC      | 7    | 8     | NC            |
| NC      | 9    | 10    | PORT.B        |
| NC      | 11   | 12    | 3V3           |
| NC      | 13   | 14    | NC            |
| PORT.C  | 15   | 16    | PORT.C        |
| I2C_SDA | 17   | 18    | I2C_SCL       |
| NC      | 19   | 20    | NC            |
| NC      | 21   | 22    | NC            |
| NC      | 23   | 24    | I2S_LRCK (SW) |
| HPWR    | 25   | 26    | I2S_DIN (SW)  |
| HPWR    | 27   | 28    | 5V            |
| HPWR    | 29   | 30    | BAT           |
::

## 尺寸图

- [Base X 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1010/BASE-X-K037.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1010/BASE-X-K037_page_01.png" width="100%">

## 结构文件

- [Base X 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/K037_BaseX/Structures)

## 软件开发

### Arduino

- [Base X 测试程序](https://github.com/m5stack/M5Stack/tree/master/examples/Modules/BaseX)

### UiFlow1

- [Base X UiFlow1 文档](/zh_CN/uiflow/blockly/base/basex)

### 通信协议

#### I2C 控制说明

- I2C 从机地址: 0x22

| 功能                 | 寄存器地址 | 值                  |
| -------------------- | ---------- | ------------------- |
| SERVO1_ANGLE_ADDR    | 0X00       | 0~180               |
| SERVO2_ANGLE_ADDR    | 0x01       | 0~180               |
| SERVO1_PULSE_ADDR    | 0x10       | (uint16_t) 500~2500 |
| SERVO2_PULSE_ADDR    | 0x12       | (uint16_t) 500~2500 |
| MOTOR1_PWM_DUTY_ADDR | 0x20       | -127~127            |
| MOTOR2_PWM_DUTY_ADDR | 0x21       | -127~127            |
| MOTOR3_PWM_DUTY_ADDR | 0x22       | -127~127            |
| MOTOR4_PWM_DUTY_ADDR | 0x23       | -127~127            |
| MOTOR1_ENCODER_ADDR  | 0x30       | int32_t             |
| MOTOR2_ENCODER_ADDR  | 0x34       | int32_t             |
| MOTOR3_ENCODER_ADDR  | 0x38       | int32_t             |
| MOTOR4_ENCODER_ADDR  | 0x3C       | int32_t             |
| MOTOR1_SPEED_ADDR    | 0x40       | -127~127            |
| MOTOR2_SPEED_ADDR    | 0x41       | -127~127            |
| MOTOR3_SPEED_ADDR    | 0x42       | -127~127            |
| MOTOR4_SPEED_ADDR    | 0x43       | -127~127            |

I2C 电机地址:

| 电机编号 | 电机地址 |
| -------- | -------- |
| MOTOR1   | 0x50     |
| MOTOR2   | 0x60     |
| MOTOR3   | 0x70     |
| MOTOR4   | 0x80     |

配置方法
电机地址 + nBit

| 位      | 值                        |
| ------- | ------------------------- |
| 0       | 电机运行模式              |
| 1       | position-p (3)            |
| 2       | position-i (1)            |
| 3       | position-d (15)           |
| 4/5/6/7 | position-point (低位有效) |
| 8       | position-max-speed        |
| 9       | speed-p                   |
| 10      | speed-i                   |
| 11      | speed-d                   |
| 12      | speed-point               |

| 电机运行模式 | 值       |
| ------------ | -------- |
| Normal       | 0X00     |
| Position     | 0x01     |
| Encoder      | 0x02     |
| 3            | position |

### EasyLoader

| Easyloader             | Download                                                                                      | Note |
| ---------------------- | --------------------------------------------------------------------------------------------- | ---- |
| Base X Test Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Base/EasyLoader_BaseX.exe) | /    |

## 相关视频

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Base/BaseX.mp4" type="video/mp4">
</video>
