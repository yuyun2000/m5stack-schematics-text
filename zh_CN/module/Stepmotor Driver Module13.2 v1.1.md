# Module13.2 Stepmotor Driver v1.1

<span class="product-sku">SKU:M039-V11</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Stepmotor Driver Module13.2 v1.1/img-c2b8ceac-b6be-4cec-9a15-228fcf8623e7.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Stepmotor Driver Module13.2 v1.1/img-53ee19f2-b591-479c-a109-6c26e8f3d19a.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Stepmotor Driver Module13.2 v1.1/img-186c1add-042b-4a81-bada-8f0357168174.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Stepmotor Driver Module13.2 v1.1/img-86ff313a-1d75-4761-8501-217fce17add1.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Stepmotor Driver Module13.2 v1.1/img-92aff9cb-b2d7-4a42-845c-b0d4ba859c49.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Stepmotor Driver Module13.2 v1.1/img-01043ec7-ee09-4c88-9082-822ba3984383.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Stepmotor Driver Module13.2 v1.1/img-51b2bb8f-4d38-4e17-973d-0b561a994340.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Stepmotor Driver Module13.2 v1.1/img-64b8a33b-85d9-41c8-be3e-a9acca75b5d6.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Stepmotor Driver Module13.2 v1.1/img-cd73a3c0-5780-4418-8b6f-d881cf453826.webp">
</PictureViewer>

## 描述

**Module13.2 Stepmotor Driver v1.1** 是一款适配 M5 主控的步进电机驱动器，采用 **STM32 + HR8825** 步进电机驱动方案，提供 **3 路双极步进电机控制接口**。将该驱动器与 M5 主控堆叠后，由主控内部 ESP32 产生信号直连驱动芯片，能够实现**独立控制**或是**多轴电机联动**。模块集成 **STM32F030F4P6** 芯片充当 **IO 拓展**，**提供 4 组输入信号端子**、**1 组驱动芯片使能控制**，通过 **I2C 通讯**，能够 **控制和监听驱动芯片的复位与状态** ，可用于**外接限位开关、电机制动功能**。模块上含 3 个焊盘控制 3 组步进电机的**细分模式**，实现步进电机的细分调节。集成 **PWR485** 通信接口（**RS485** + **9-24V 电源输入**） 与 **DC-JACK** ，能够用于通信的同时，供电方式也将更加灵活。支持 **UiFlow 图形化编程** ，可轻松配置信号输出，对步进电机实现更加精准的控制。该模块适用于多种步进电机运动控制场景，如 **打印机，机械臂** 等。

## 注意事项

\#> 注意: | 使用时禁止带电插拔电机，一切操作请将设备断电后进行，避免损坏模块。

\#> 供电方式：|1. **PWR485 接口**：<br/>- 接口类型：3.96-4P 端子<br/>- 电压范围：DC 9 ~ 24V<br/>2. **DC 插孔**：<br/>- 电压范围：DC 9 ~ 24V<br/>- 接口类型：5.5/2.1mm DC 插孔<br/>- 极性：内正外负<br/>

## 产品特性

- STM32F030F4P6@: ARM® 32-bit Cortex™-M0 CPU
- 三轴 HR8825 步进电机驱动器
- 适用于双极步进电机
- 每路带电流调节电位器，驱动电流可达 1.5A
- 支持多种细分模式，最大可达 1/32 STEP 细分
- 4 组信号输入接口
- PWR485 通信接口 (RS485 + 9-24V 电源输入)
- DC-JACK 端子输入 (9-24V)
- 开发平台：Arduino、UiFlow

## 包装内容

- 1 x Module13.2 Stepmotor Driver v1.1
- 4 x 2.54-2P 端子
- 3 x 2.54-4P 端子
- 1 x 3.96-4P 端子

## 应用场景

- 打印机
- 扫描仪
- CNC 雕刻机控制
- 运动模组控制

## 规格参数

| 规格               | 参数                                                                                                  |
| ------------------ | ----------------------------------------------------------------------------------------------------- |
| IO 拓展芯片        | STM32F030F4P6                                                                                         |
| 通信接口           | I2C 通信 @ 0x27                                                                                       |
| 步进电机驱动芯片   | HR8825                                                                                                |
| 支持细分模式       | FULL、1/2、1/4、1/8、1/16、1/32                                                                       |
| 单通道最大驱动电流 | 1.5A                                                                                                  |
| 输入信号端子规格   | 2.54-2P                                                                                               |
| 步进电机供电方式   | DC9-24V (5.5/2.1mm DC 座)<br/> 电压范围：DC 9-24V<br/> 接口类型：5.5/2.1mm DC 插孔<br/>极性：内正外负 |
| 电机接线端子规格   | 2.54-4P                                                                                               |
| RS485 接线端子规格 | 3.96-4P (9-12V)                                                                                       |
| 工作温度           | 0-40°C                                                                                                |
| 产品尺寸           | 54.0 x 54.0 x 19.7mm                                                                                  |
| 包装尺寸           | 95 x 65 x 25mm                                                                                        |
| 产品重量           | 40g                                                                                                   |
| 毛重               | 60g                                                                                                   |

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

调节细分模式需通过焊接对应的焊盘来将其置为 1。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Stepmotor%20Driver%20Module13.2%20v1.1/step.png" width="50%"/>

### 驱动电流调节

步进电机规格不同，所需要的驱动电流也可能有所不同，使用时可以通过模块上的金属旋钮调整电流输出。为防止电机过热或损坏，调整时需缓慢调整旋钮，观察电机状态或接入电流计来判断合适的驱动电流。

<img src="https://static-cdn.m5stack.com/resource/docs/products/module/stepmotor_driver/stepmotor_driver_adj_01.webp" width="50%">

## 原理图

- [Module13.2 Stepmotor Driver v1.1 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/547/SCH_DirectStepMotor_V1.1.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/547/SCH_DirectStepMotor_V1.1_sch_01.png">
</SchViewer>

## 管脚映射

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Stepmotor%20Driver%20Module13.2%20v1.1/M5PPT%20(2).png" width="70%">

### M5-Bus

::m5-bus-table
| PIN       | LEFT | RIGHT | PIN       |
| --------- | ---- | ----- | --------- |
| GND       | 1    | 2     |           |
| GND       | 3    | 4     |           |
| GND       | 5    | 6     |           |
|           | 7    | 8     | RS485_TX  |
|           | 9    | 10    |           |
|           | 11   | 12    | 3V3       |
|           | 13   | 14    |           |
| STEP_X    | 15   | 16    | DIR_X     |
| SDA       | 17   | 18    | SCL       |
|           | 19   | 20    |           |
| STEP_Y    | 21   | 22    | DIR_Y     |
| STEP_Z    | 23   | 24    | DIR_Z     |
| HPWR      | 25   | 26    | RS485_RX  |
| HPWR      | 27   | 28    | 5V        |
| HPWR      | 29   | 30    |           |
::

## 尺寸图

- [Module13.2 Stepmotor Driver v1.1 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/972/stepmotorDriver.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/972/stepmotorDriver_page_01.png" width="100%">

## 数据手册

- [HR8825 Datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/stepmotor_driver/HR8825_2017-09-25.PDF)
- [STM32F030F4P6 Datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/STM32F030F4P6.PDF)

## 软件开发

### Arduino

- [Module13.2 Stepmotor Driver v1.1 Arduino 驱动库](https://github.com/m5stack/M5Module-Stepmotor)

### UiFlow1

- [Module13.2 Stepmotor Driver v1.1 UiFlow1 文档](/zh_CN/uiflow/blockly/module/stepmotor_driver)
- [Module13.2 Stepmotor Driver v1.1 UiFlow 示例](https://flow.m5stack.com/?examples=step_motor_ctrl_demo)

### UiFlow2

- [Module13.2 Stepmotor Driver v1.1 UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/module/step_motor_driver.html)

### 内置固件

- [Module13.2 Stepmotor Driver v1.1 内置固件](https://github.com/m5stack/M5Module-StepMotor-Driver-V1.1-Internal-FW)

### 通信协议

- [Module13.2 Stepmotor Driver v1.1 Protocol](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/972/M039_V11_M5Stack_Step-Motor-Driver_V1_1_I2C.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/972/M039_v11_M5Stack_Step-Motor-Driver_V1_1_I2C_page_01.png" width="100%">

## 相关视频

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Stepmotor%20Driver%20Module13.2%20v1.1/M039-v11.mp4" type="video/mp4">
</video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=115570070586790&bvid=BV1J1yGBjEv8&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
      <iframe width="560" height="315" src="https://www.youtube.com/embed/rDBB5HBrjmA?si=s5p-PwQCjW176XkF" title="YouTube video player" frameborder="0"  loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>

## 产品对比

::compare-table
| 产品对比       | [GRBL 13.2 MODULE ](/zh_CN/module/grbl13.2) ![GRBL 13.2 MODULE ](https://static-cdn.m5stack.com/resource/docs/products/module/grbl13.2/grbl13.2_cover_01.webp) | [STEPMOTOR DRIVER](/zh_CN/module/stepmotor_driver) ![STEPMOTOR DRIVER](https://static-cdn.m5stack.com/resource/docs/products/module/stepmotor_driver/stepmotor_driver_cover_01.webp) | [STEPMOTOR DRIVER V1.1 ](/zh_CN/module/Stepmotor%20Driver%20Module13.2%20v1.1) ![STEPMOTOR DRIVER V1.1 ](https://static-cdn.m5stack.com/resource/docs/products/module/Stepmotor%20Driver%20Module13.2%20v1.1/img-b2f4ea5a-bfa2-4000-913e-93ed459aea01.webp) |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------       |
| 控制方式       | 脉冲信号                                                                                                                                                       | 脉冲信号                                                                                                                                                                             | 脉冲信号                                                                                                                                                                                                                                                    |
| MCU            | 板载 MEGA328                                                                                                                                                   | Core 主机直接控制                                                                                                                                                                    | 板载 STM32F030F4P6                                                                                                                                                                                                                                          |
| I2C 片选       | I2C 通信 (0x70 , 0x71)                                                                                                                                         | /                                                                                                                                                                                    | /                                                                                                                                                                                                                                                           |
| 模块可堆叠数量 | 2                                                                                                                                                              | 1                                                                                                                                                                                    | 1                                                                                                                                                                                                                                                           |
| 驱动芯片       | DRV8825                                                                                                                                                        | HR8825                                                                                                                                                                               | HR8825                                                                                                                                                                                                                                                      |
| 细分调节       | 拨码开关                                                                                                                                                       | TCA9554 芯片控制                                                                                                                                                                     | 焊盘焊接选择控制                                                                                                                                                                                                                                            |
| 接口           | DC 电源供电接口 + 3 组限位开关接口                                                                                                                             | DC 电源供电接口 + 4 组自定义信号输入接口 + RS485 通信接口                                                                                                                            | DC 电源供电接口 + 4 组自定义信号输入接口 + RS485 通信接口                                                                                                                                                                                                   |
| 步进电机接口   | 3 x XH2.54-4P                                                                                                                                                  | 3 x XH2.54-4P                                                                                                                                                                        | 3 x XH2.54-4P                                                                                                                                                                                                                                               |
::
