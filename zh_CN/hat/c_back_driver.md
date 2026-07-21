# Hat CBack Driver

<span class="product-sku">SKU:A100</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/c_back_driver/c_back_driver_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/c_back_driver/c_back_driver_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/873/A100-weight.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/c_back_driver/c_back_driver_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/c_back_driver/c_back_driver_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/c_back_driver/c_back_driver_05.webp">
</PictureViewer>

## 描述

**Hat CBack Driver**是一款兼容 M5StickC 的舵机驱动板，采用 STM32F030F4P6 控制方案，采用 I2C 通信接口与 M5StickC 进行通信， 提供 4 组 PWM 舵机驱动接口（舵机的驱动电源直连 M5StickC 的内部的电池，能够驱动一般规格的舵机，如：SG90 等）。该模块对 StickC 顶部的 I2C 总线进行了引出，并通过 STM32 拓展额外提供一组 GPIO 接口。能够用于一般逻辑电平与 ADC 模拟信号输入读取。背部 LEGO 兼容孔设计，用户能够非常方便的将这个驱动板集成到 LEGO 积木结构中，可用于构建如舵机机械手等可控结构。

## 产品特性

- 4 x Servo 驱动
- 兼容 C/C Plus
- 接口拓展 (GPIO, I2C)

## 包装内容

- 1 x Hat CBack Driver
- 2 x 六角螺丝 M2\*5
- 1 x 内六角扳手
- 1 x 乐高兼容连接件

## 应用场景

- 舵机控制器
- 机器人控制

## 规格参数

| 规格     | 参数                  |
| -------- | --------------------- |
| MCU      | STM32F030F4P6         |
| 通信接口 | I2C 通信 @ 0x38       |
| 工作电流 | 15mA                  |
| 产品尺寸 | 23.7 x 49.2 x 21.0mm  |
| 产品重量 | 9.0g                  |
| 包装尺寸 | 138.0 x 93.0 x 22.0mm |
| 毛重     | 13.5g                 |

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/c_back_driver/c_back_driver_sch_01.webp" width="80%">

## 管脚映射

| M5StickC      | G0  | G26 | 3.3V | GND |
| ------------- | --- | --- | ---- | --- |
| C Back Driver | SDA | SCL | 3.3V | GND |

## 尺寸图

[Hat CBack Driver 模型尺寸 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/873/hatcback.pdf)

<img alt="module size" src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/873/A100-hatcback_page_01.png" width="100%" />

## 软件开发

- [Hat CBack Driver Example - with M5StickC](https://github.com/m5stack/M5StickC/tree/master/examples/Hat/CBACK_DRIVER)
- [Hat CBack Driver Example - with M5StickC-Plus](https://github.com/m5stack/M5StickC-Plus/tree/master/examples/Hat/C_BACK_DRIVER)

### UiFlow1

- [Hat CBack Driver UiFlow1 文档](/zh_CN/uiflow/blockly/hat/cback_driver)

### 通信协议

- 协议类型 I2C
- I2C Address: **0x38**

```cpp
/*------------------------------------------------ -------------------------------------------------- */
| SERVO_ANGLE_REG | 0x00-0x03
| ------------------------------------------------- -----------------------------------------------
| servo_1_reg[0] 0x00 | R/W | SERVO1 Angle value(0~180)
| servo_2_reg[1] 0x01 | R/W | SERVO2 Angle value(0~180)
| servo_3_reg[2] 0x02 | R/W | SERVO3 Angle value(0~180)
| servo_4_reg[3] 0x03 | R/W | SERVO4 Angle value(0~180)
/*------------------------------------------------ -------------------------------------------------- -

/*------------------------------------------------ -------------------------------------------------- */
| SERVO_PULSE_REG | 0x10-0x17
| ------------------------------------------------- -----------------------------------------------
| servo_1_reg[0:1] 0x10-0x11 | R/W | SERVO1 PULSE value(500~2500)
| servo_2_reg[2:3] 0x12-0x13 | R/W | SERVO2 PULSE value(500~2500)
| servo_3_reg[4:5] 0x14-0x15 | R/W | SERVO3 PULSE value(500~2500)
| servo_4_reg[6:7] 0x16-0x17 | R/W | SERVO4 PULSE value(500~2500)
/*------------------------------------------------ -------------------------------------------------- -

/*------------------------------------------------ -------------------------------------------------- */
| PPORTB_ADC_REG | 0x20-0x21
| ------------------------------------------------- -----------------------------------------------
| portb_adc_reg[0:1] 0x20-0x21 | R | PPORTB ADC value(0~4095)
/*------------------------------------------------ -------------------------------------------------- -

/*------------------------------------------------ -------------------------------------------------- */
| PPORTB_OUTPUT_REG | 0x30
| ------------------------------------------------- -----------------------------------------------
| portb_output_reg[0] 0x30 | R | PPORTB Output Digital value(0/1)
/*------------------------------------------------ -------------------------------------------------- -

/*------------------------------------------------ -------------------------------------------------- */
| PPORTB_INPUT_REG | 0x31
| ------------------------------------------------- -----------------------------------------------
| portb_input_reg[0] 0x31 | R | PPORTB Input Digital value(0/1)
/*------------------------------------------------ -------------------------------------------------- -

```

## 相关视频

- 使用 Hat CBACK Driver 制作四轮小车

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/HAT/C_BACK-DRIVER.mp4" type="video/mp4">
</video>
