# Module13.2 Servo2

<span class="product-sku">SKU:M014-B</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/servo2/servo2_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/servo2/servo2_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/servo2/servo2_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/965/M014-B-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/servo2/servo2_06.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/servo2/servo2_07.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/servo2/servo2_08.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/servo2/servo2_09.webp">
</PictureViewer>

## 描述

**Module13.2 Servo2** 是一款适用于 M5Stack 堆叠式主机的 16 通道舵机驱动模块。模块采用 PCA9685 12 位 PWM 控制器，可独立控制 16 路舵机信号，并通过 M5-Bus I2C 与主机通信。板载 3 位地址拨码开关，支持在 `0x40`（默认）至 `0x47` 之间配置 I2C 地址，最多支持 8 个模块堆叠使用（每个模块独立供电）。

模块的逻辑控制与舵机供电相互独立：PCA9685 由 M5-Bus 3.3V 供电，16 路舵机接口则分为两组，每组 8 路，由两颗 SY8368AQQC 降压转换器分别提供 5V 电源，每路降压转换器给 8 组舵机供电。通过 XT60 接口输入 DC 6 ~ 12V 时，两组舵机接口同时输出最高可达 5V/3.5A x 2（总功率 35W），单组最高可达 5V/5A（25W）；使用兼容电池底座供电时，最高支持 5V/2A 输出。板载电源开关用于控制 Module13.2 Servo2 电源通断，两颗绿色指示灯分别显示两组 5V 输出状态。

## 注意事项

?> 模块供电 | 该模块驱动舵机时必须使用 DC 接口外部供电。使用电源管理芯片的主控 (如 Core2/CoreS3)，在程序初始化时需要将 M5-Bus 电源模式配置为输入（即 `cfg.output_power = false`）。

## 产品特性

- 16 x 舵机驱动通道
- 2 x 电源指示灯
- I2C 地址可调
- 独立开关电源控制
- 外部 DC 电源输入: 6-12V
- DC 连接器类型: XT60

## 包装内容

- 1 x Module13.2 Servo2
- 1 x XT60 电源连接线（11.5cm）

## 应用场景

- 人形机器人
- 仿生多关节机器人
- 3 轴舵机云台

## 规格参数

| 规格                 | 参数                         |
| -------------------- | ---------------------------- |
| PWM 控制器           | PCA9685                      |
| PWM 分辨率           | 12 位（4096 级）             |
| 舵机通道             | 16 路，分为 2 组，每组 8 路  |
| 通信接口             | I2C @ 0x40（默认）~ 0x47     |
| 外部电源输入         | DC 6 ~ 12V                   |
| 外部电源接口         | XT60                         |
| 舵机输出电压         | 5V                           |
| 双组同时带载能力     | 每组 5V/3.5A，总功率最高 35W |
| 单组最大带载能力     | 5V/5A，功率最高 25W          |
| 电池底座供电带载能力 | 最高 5V/2A                   |
| 电源指示灯           | 2 x 绿色 LED                 |
| 产品尺寸             | 54.2 x 54.2 x 19.7mm         |
| 产品重量             | 28.0g                        |
| 包装尺寸             | 135.0 x 95.0 x 20.5mm        |
| 毛重                 | 60.0g                        |

## 操作说明

### I2C 地址切换

Module13.2 Servo2 板载 3 位 I2C 地址配置拨码，拨码 1、2、3 分别对应地址位 A0、A1、A2；拨码置上记为 1，置下记为 0。请在设备断电状态下设置拨码，重新上电后生效。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/965/i2c.png" width="80%">

|  A0   |  A1   |  A2   | 7 位 I2C 地址 |
| :---: | :---: | :---: | :-----------: |
|   0   |   0   |   0   |     0x40      |
|   1   |   0   |   0   |     0x41      |
|   0   |   1   |   0   |     0x42      |
|   1   |   1   |   0   |     0x43      |
|   0   |   0   |   1   |     0x44      |
|   1   |   0   |   1   |     0x45      |
|   0   |   1   |   1   |     0x46      |
|   1   |   1   |   1   |     0x47      |

## 原理图

- [Module13.2 Servo2 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/965/M014-B_Module13.2_Servo2_Sche.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/965/M014-B_Module13.2_Servo2_Sche_page_01.png">
</SchViewer>

## 管脚映射

### M5-Bus

::m5-bus-table
| PIN  | LEFT | RIGHT | PIN |
| ---- | ---- | ----- | --- |
| GND  | 1    | 2     |     |
| GND  | 3    | 4     |     |
| GND  | 5    | 6     |     |
|      | 7    | 8     |     |
|      | 9    | 10    |     |
|      | 11   | 12    | 3V3 |
|      | 13   | 14    |     |
|      | 15   | 16    |     |
| SDA  | 17   | 18    | SCL |
|      | 19   | 20    |     |
|      | 21   | 22    |     |
|      | 23   | 24    |     |
| HPWR | 25   | 26    |     |
| HPWR | 27   | 28    | 5V  |
| HPWR | 29   | 30    |     |
::

## 尺寸图

- [Module13.2 Servo2 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/965/servo2.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/965/servo2_page_01.png" width="100%">

## 数据手册

- [PCA9685 - datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/PCA9685.pdf)

## 软件开发

#> I2C 地址冲突 | Module13.2 Servo2 内置 `PCA9685` 芯片默认使能 ALL_CALL 广播地址`0x70`，用于多个芯片同步控制。模块上电后，除接收本机的 I2C 通信地址 (0x40 ~ 0x47) 的请求以外，还会额外响应 ALL_CALL 功能的 I2C 地址 `0x70`。如果当前 I2C 总线上连接了相同地址的设备，将引发地址冲突，导致通信异常。该情况可通过配置 PCA9685 的工作模式寄存器 (0x00H) 中的 `ALLCALL` (bit:0)，将其设置为 `0` 即可禁用`ALL_CALL`功能。可参考 [Module13.2 Servo2 ALL_CALL 功能配置](/zh_CN/arduino/projects/module/module13.2_servo2#32-all_call-%E5%8A%9F%E8%83%BD%E9%85%8D%E7%BD%AE) 案例程序。

### Arduino

- [Adafruit-PWM-Servo-Driver-Library](https://github.com/adafruit/Adafruit-PWM-Servo-Driver-Library)
- [Module13.2 Servo2 Arduino 上手教程](/zh_CN/arduino/projects/module/module13.2_servo2)

### UiFlow1

- [Module13.2 Servo2 UiFlow1 文档](/zh_CN/uiflow/blockly/module/servo2)

### UiFlow2

- [Module13.2 Servo2 UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/module/servo2.html)

## 相关视频

<video id="example_video" controls> <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Module/Servo2.mp4" type="video/mp4"></video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=114057386394083&bvid=BV1vYPsewEXE&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div>
        <iframe width="560" height="315" src="https://www.youtube.com/embed/tgN8T9_Nju0?si=feyFbVjPnrIp0XPX" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
