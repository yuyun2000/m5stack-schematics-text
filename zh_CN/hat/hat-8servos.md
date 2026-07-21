# Hat 8Servos

<span class="product-sku">SKU:U076</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-8servos/hat-8servos_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-8servos/hat-8servos_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-8servos/hat-8servos_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-8servos/hat-8servos_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-8servos/hat-8servos_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-8servos/hat-8servos_06.webp">
</PictureViewer>

## 描述

**Hat 8Servos**是一款兼容 M5StickC 的 8 路舵机控制板，主控为 STM32F030F4，通过 I2C 的方式与 M5StickC 进行通信。为了保证多个舵机同时工作，控制板配备了独立的 16340 电池底座用来供电，由独立开关进行控制。此外在控制板上集成了一颗 RGB 指示灯。你可以使用它来控制 SG90 舵机，完成一些角度的精准操作。

## 产品特性

- 八路舵机控制
- 1xRGB LED
- 16340 电池底座
- I2C 协议控制 (0x38)

## 包装内容

- 1 x Hat 8Servos
- 1 x 16340 电池 (700mAh)

## 应用场景

- 舵机控制器
- 机器人控制
- 智能玩具

## 规格参数

| 规格     | 参数                 |
| -------- | -------------------- |
| MCU      | STM32F030F4P6        |
| 通信接口 | I2C 通信 @ 0x38      |
| 产品尺寸 | 54.0 x 24.0 x 20.0mm |
| 产品重量 | 27.0g                |
| 包装尺寸 | 75.0 x 46.0 x 29.0mm |
| 毛重     | 38.0g                |

## 管脚映射

| M5StickC | G0  | G26 | 3.3V | GND |
| -------- | --- | --- | ---- | --- |
| 8Servos  | SDA | SCL | Vin  | GND |

<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-8servos/hat-8servos_07.webp" width="50%">

## 软件开发

### Arduino

- [Hat 8Servos Example](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/Hat/8serves-hat/Arduino)

### UiFlow1

- [Hat 8Servos UiFlow1 文档](/zh_CN/uiflow/blockly/hat/8servo)

### UiFlow2

- [Hat 8Servos UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/hats/servo8.html)

### 通信协议

#### 舵机控制说明

```cpp
> 1.功能说明

	(1)八路舵机控制

	(2)板载sk6812 LED控制

> 2.通讯方式

	I2C,速率最大400HZ,地址支持自加

	设备地址:0x38

    地址	默认值	说明

    00H	0X00	CH1角度输出

    01H	0X00	CH2角度输出

    02H	0X00	CH3角度输出

    03H	0X00	CH4角度输出

    04H	0X00	CH5角度输出

    05H	0X00	CH6角度输出

    06H	0X00	CH7角度输出

    07H	0X00	CH8角度输出

> 3.I2C地址说明

	00H(R/W)舵机角度寄存器

	说明:

	(1)数据可连续读写

	(2)每个寄存器值表示度数可写入0-180

>	10H(R/W)舵机脉宽寄存器

    地址	默认值	说明

    10H	0X00	CH1_WIDTH[8:15]

    11H	0X00	CH1_WIDTH[0:7]

    12H	0X00	CH2_WIDTH[8:15]

    13H	0X00	CH2_WIDTH[0:7]

    14H	0X00	CH3_WIDTH[8:15]

    15H	0X00	CH3_WIDTH[0:7]

    16H	0X00	CH4_WIDTH[8:15]

    17H	0X00	CH4_WIDTH[0:7]

    18H	0X00	CH5_WIDTH[8:15]

    19H	0X00	CH5_WIDTH[0:7]

    1AH	0X00	CH6_WIDTH[8:15]

    1BH	0X00	CH6_WIDTH[0:7]

    1CH	0X00	CH7_WIDTH[8:15]

    1DH	0X00	CH7_WIDTH[0:7]

    1EH	0X00	CH8_WIDTH[8:15]

    1FH	0X00	CH8_WIDTH[0:7]

    说明:

	(1)数据可连续读写

>   20H(R/W)LED_RGB寄存器

    地址	默认值	说明

    20H	0X00	G[0:7]

    21H	0X00	R[0:7]

    22H	0X00	B[0:7]

说明:

	(1)数据可连续读写

	(2)RGB888
```

### EasyLoader

| Easyloader             | 下载链接                                                                                                   | 备注 |
| ---------------------- | ---------------------------------------------------------------------------------------------------------- | ---- |
| Hat 8Servos Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/HAT/EasyLoader_8Servos_HAT.exe) | /    |

## 相关视频

<video id="example_video" controls>
  <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/HAT/8Servos_hat.mp4" type="video/mp4">
</video>
