# Module13.2 Stepmotor Driver

<span class="product-sku">SKU:M039</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/stepmotor_driver/stepmotor_driver_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/stepmotor_driver/stepmotor_driver_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/stepmotor_driver/stepmotor_driver_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/stepmotor_driver/stepmotor_driver_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/stepmotor_driver/stepmotor_driver_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/stepmotor_driver/stepmotor_driver_06.webp">
</PictureViewer>

## 描述

**Module13.2 Stepmotor Driver** 是一款适配 M5 主控的步进电机驱动器，采用 **HR8825** 步进电机驱动芯片方案，提供 3 路双极步进电机控制接口。将该驱动器与 M5 主控堆叠后，由主控内部 ESP32 产生信号直连驱动芯片，能够实现独立控制或是多轴电机联动。模块集成 TCA9554 IO 拓展芯片，提供 **4 组输入信号端子** + **3 组步进电机细分控制** + **1 组驱动芯片使能控制** ，通过 I2C 接口控制，能够监听与控制这 8 个拓展 IO 状态，可用于外接限位开关、动态细分调节、电机制动功能。集成 **PWR485** 通信接口（**RS485** + **9-24V 电源输入**） 与 DC-JACK ，能够用于通信的同时，供电方式也将更加灵活。支持 UiFlow 图形化编程，与 ESP32-GRBL 固件，Web 控制，可轻松配置信号输出，对步进电机实现更加精准的控制。该模块适用于多种步进电机运动控制场景，如打印机，机械臂等 。

## 注意事项

?> 注意事项 | 使用时禁止带电插拔电机，一切操作请将设备断电后进行，避免损坏模块。

## 产品特性

- 三轴 HR8825 步进电机驱动器
- 适用于双极步进电机
- 每路带电流调节电位器，驱动电流可达 1.5A
- 支持多种细分模式，最大可达`1/32` STEP 细分
- 多组信号输入接口
- PWR485 通信接口 (RS485 + 9-24V 电源输入)
- DC-JACK 端子输入 (9-24V)
- 内置 DC-DC, 集成 9-24V 转 5V 电路
- 开发平台:
  - Arduino、UiFlow

## 包装内容

- 1 x Module13.2 Stepmotor Driver
- 4 x 2.54-2P 端子
- 3 x 2.54-4P 端子
- 1 x 3.96-4P 端子

## 应用场景

- 打印机
- 扫描仪
- CNC 雕刻机控制
- 运动模组控制

## 规格参数

| 规格               | 参数                            |
| ------------------ | ------------------------------- |
| 步进电机驱动芯片   | HR8825                          |
| IO 拓展芯片        | TCA9554                         |
| 通信接口           | I2C 通信 @ 0x27                 |
| 支持细分模式       | FULL、1/2、1/4、1/8、1/16、1/32 |
| 单通道最大驱动电流 | 1.5A                            |
| 输入信号端子规格   | 2.54-2P                         |
| 电机接线端子规格   | 2.54-4P                         |
| RS485 接线端子规格 | 3.96-4P                         |
| 产品尺寸           | 54.2 x 54.2 x 13.2mm            |
| 产品重量           | 40.0g                           |
| 包装尺寸           | 95.0 x 65.0 x 25.0mm            |
| 毛重               | 60.0g                           |

## 操作说明

### 细分 / 微步真值表

| M2  | M1  | M0  | 分辨率 |
| --- | --- | --- | ------ |
| 0   | 0   | 0   | FULL   |
| 0   | 0   | 1   | 1/2    |
| 0   | 1   | 0   | 1/4    |
| 0   | 1   | 1   | 1/8    |
| 1   | 0   | 0   | 1/16   |
| 1   | 0   | 1   | 1/32   |
| 1   | 1   | 0   | 1/32   |
| 1   | 1   | 1   | 1/32   |

### TCA9554 寄存器

`I2C Addr: 0x27`

读取状态时使用寄存器`0x00`<br/>写入状态时使用寄存器`0x01`<br/>寄存器`0x02`中对应的 bit 配置为 1 可实现极性反转，配置为 0 则不反转<br/>寄存器`0x03`中对应的 bit 配置为 1 为输入模式，0 为输出模式。<br/>以上寄存器字节对应的引脚关系如下表所示。

| Bit | Desc                   | R/W |
| --- | ---------------------- | --- |
| 7   | P7 细分调节位 M0       | R/W |
| 6   | P6 细分调节位 M1       | R/W |
| 5   | P5 细分调节位 M2       | R/W |
| 4   | P4 DRV EN 驱动芯片使能 | R/W |
| 3   | P3 输入信号 3          | R/W |
| 2   | P2 输入信号 2          | R/W |
| 1   | P1 输入信号 1          | R/W |
| 0   | P0 输入信号 0          | R/W |

### 驱动电流调节

步进电机规格不同，所需要的驱动电流也可能有所不同，使用时可以通过模块上的金属旋钮调整电流输出。为防止电机过热或损坏，调整时需缓慢调整旋钮，观察电机状态或接入电流计来判断合适的驱动电流。

<img src="https://static-cdn.m5stack.com/resource/docs/products/module/stepmotor_driver/stepmotor_driver_adj_01.webp" width="70%">

## 管脚映射

### M5-Bus

::m5-bus-table
| PIN    | LEFT | RIGHT | PIN      |
| ------ | ---- | ----- | -------- |
| GND    | 1    | 2     |          |
| GND    | 3    | 4     |          |
| GND    | 5    | 6     |          |
|        | 7    | 8     | RS485_TX |
|        | 9    | 10    |          |
|        | 11   | 12    | 3V3      |
|        | 13   | 14    |          |
| STEP_X | 15   | 16    | DIR_X    |
| SDA    | 17   | 18    | SCL      |
|        | 19   | 20    |          |
| STEP_Y | 21   | 22    | DIR_Y    |
| STEP_Z | 23   | 24    | DIR_Z    |
| HPWR   | 25   | 26    | RS485_RX |
| HPWR   | 27   | 28    | 5V       |
| HPWR   | 29   | 30    |          |
::

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/module/stepmotor_driver/stepmotor_driver_sch_01.webp" width="70%">

## 数据手册

- [HR8825 Datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/stepmotor_driver/HR8825_2017-09-25.PDF)
- [TCA9554 Datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/stepmotor_driver/tca9554.pdf)

## 软件开发

### Arduino

- [Module13.2 Stepmotor Driver Arduino 驱动库](https://github.com/m5stack/M5Module-Stepmotor)
- [ESP32-GRBL & WEB-UI](https://github.com/m5stack/Grbl_Esp32)

\#> 案例编译 |[ESP32-GRBL & WEB-UI](https://github.com/m5stack/Grbl_Esp32)程序要求使用 ESP32 板管理`1.0.3`版本，高于该版本会出现无法正常编译的情况。有关使用说明与使用 WEB-UI 控制请查看[ESP32-GRBL-WIKI](https://github.com/bdring/Grbl_Esp32/wiki)

### UiFlow1

- [Module13.2 Stepmotor Driver UiFlow1 文档](/zh_CN/uiflow/blockly/module/stepmotor_driver)

## 相关视频

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Module/STEPMOTOR%20DRIVER_VIDEO.mp4" type="video/mp4">
</video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=115570070586790&bvid=BV1J1yGBjEv8&&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div>
        <iframe width="560" height="315" src="https://www.youtube.com/embed/rDBB5HBrjmA?si=cRY3wufbgQjHlgdZ" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>

## 产品对比

| 功能           | GRBL 13.2 MODULE           | STEPMOTOR DRIVER                        |
| -------------- | -------------------------- | --------------------------------------- |
| 控制方式       | I2C 通信                   | 脉冲信号                                |
| 固件程序       | 板载 STM32，内置 GRBL 固件 | 无固件，可通过 ESP32 直接信号驱动       |
| 模块可堆叠数量 | 2                          | 1                                       |
| 驱动芯片       | DRV8825                    | HR8825                                  |
| 细分调节       | 拨码开关                   | TCA9554 芯片控制                        |
| 接口           | 3 组限位开关接口           | 4 组自定义信号输入接口 + RS485 通信接口 |
