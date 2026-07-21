# Unit Joystick2

<span class="product-sku">SKU:U024-V2</span>

<PictureViewer>
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-JoyStick2/4.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-JoyStick2/11.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/775/U024-V2-package.jpg">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-JoyStick2/5.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-JoyStick2/6.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-JoyStick2/8.webp">
</PictureViewer>

## 描述

**Unit Joystick2** 是一款高精度霍尔电磁摇杆控制单元，内置 STM32G030F6P6 主控芯片，集成了摇杆控制信号采集固件。该单元通过 I2C 通信接口实现数据传输，支持三轴控制信号输入，其中包括 X/Y 轴的模拟量输入和 Z 轴的按键数字量输入。**Unit Joystick2** 采用了霍尔电磁摇杆，通过检测磁场变化实现高精度控制，具有无接触、耐磨损、精度高、抗干扰能力强等优点，确保了产品的稳定性和长寿命。此外，设备内置 WS2812 RGB 灯珠，用于状态指示和交互显示，并预留了 STM32 固件升级接口，方便进行固件更新。该产品适用于游戏控制、机器人操控等多种应用场景。

## 产品特性

- 霍尔电磁摇杆
- 三轴输入:
  - X/Y 轴偏移模拟量输入
  - Z 轴按键数字量输入
- 内置 stm32
- I2C 通讯
- RGB LED
- 2 x LEGO 兼容孔
- 开发平台: Arduino，UiFlow

## 包装内容

- 1 x Unit Joystick2
- 1 x HY2.0-4P GroFve 连接线 (20cm)

## 应用场景

- 游戏控制器
- 机器人远程控制

## 规格参数

| 规格              | 参数                                 |
| ----------------- | ------------------------------------ |
| MCU               | STM32G030F6P6@Cortex-M0+, 主频 64MHz |
| Flash             | 32KB                                 |
| SRAM              | 8KB                                  |
| 通信接口          | I2C 通信 @ 0x63                      |
| X、Y 轴偏移输出值 | 16 位 ADC 数值输出 (0-65535)         |
| Z 轴按键输出值    | 0/1                                  |
| RGB 灯珠          | 1x WS2812C                           |
| 产品尺寸          | 40.0 x 24.0 x 23.9mm                 |
| 产品重量          | 10.0g                                |
| 包装尺寸          | 138.0 x 93.0 x 24.9mm                |
| 毛重              | 15.7g                                |

## 原理图

<img alt="schematics" src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-JoyStick2/img-c9e7fc3b-846d-48c6-9813-7c834cbf1e61.png" width="100%" />

## 管脚映射

### Unit Joystick2

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

### STM32G030F6P6

| STM32G030F6P6 | PA1       | PA2       | PA3       | PA4 |
| ------------- | --------- | --------- | --------- | --- |
| X-Axis        | LEFT-SW-X |           |           |     |
| Y-Axis        |           | LEFT-SW-Y |           |     |
| Button        |           |           | LEFT-SW-B |     |
| WS2812C       |           |           |           | RGB |

## 尺寸图

<img alt="module size" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-JoyStick2/%E5%B0%BA%E5%AF%B8%E5%9B%BE.jpg" width="100%" />

## 软件开发

### Arduino

- [Unit Joystick2 Arduino 驱动库](https://github.com/m5stack/M5Unit-Joystick2)

### UiFlow1

- [Unit Joystick2 UiFlow1 文档](/zh_CN/uiflow/blockly/unit/joystick)

### UiFlow2

- [Unit Joystick2 UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/joystick2.html)

### 内置固件

- [Unit Joystick2 内置固件](https://github.com/m5stack/M5Unit-Joystick2-Internal-FW)

### 通信协议

<img style="width:100%" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-JoyStick2/5c89a128c77c6e9b7b13f85a8abdb91.png" alt="detail" />

## 相关视频

- Unit JoyStick2 产品介绍以及案例展示

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-JoyStick2/U024-V2%20%20JoyStick2%20Unit%20%E8%A7%86%E9%A2%91.mp4" type="video/mp4"></video>

- UiFlow2 Unit JoyStick2

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113088988709205&bvid=BV1gDHSeBEnK&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/WlHOvHNbEUc?si=YreUnA9JMLIu5pW4" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>

## 产品对比

::compare-table
| Product Compare               | [Unit Joystick v1.1](/zh_CN/unit/joystick_1.1) ![Unit Joystick v1.1](https://static-cdn.m5stack.com/resource/docs/products/unit/joystick_1.1/joystick_1.1_02.webp) | [Unit Joystick2](//zh_CN/unit/Unit-JoyStick2) ![Unit Joystick2](https://m5daily.oss-cn-shenzhen.aliyuncs.com/cover-images/62c342df5b764801877f607e41b9efc6.png) |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| MCU                           | MEGA8A                                                                                                                                                             | STM32G030F6P6                                                                                                                                                   |
| RGB                           | /                                                                                                                                                                  | WS2812C                                                                                                                                                         |
| X，Y axis offset output value | 8 bits (0-255)                                                                                                                                                     | 16 bits (0-65535)                                                                                                                                               |
| Communication Mode            | I2C (0x52)                                                                                                                                                         | I2C (0x63)                                                                                                                                                      |
| manufacturing technique       | Carbon film joystick                                                                                                                                               | Hall effect joystick                                                                                                                                            |
::
