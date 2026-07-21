# Module Servo

<span class="product-sku">SKU:M014</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/servo/servo_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/servo/servo_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/966/M014-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/servo/servo_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/servo/servo_06.webp">
</PictureViewer>

## 描述

**Module Servo** 是 M5Stack 堆叠模块系列中的一款，舵机驱动模块 。拥有 12 个舵机驱动通道，最大功率 14 瓦 ，可同时驱动多个 Module Servo 舵机。采用直流电源输入设计用于功率补充，并通过 M5-Bus ，自动为顶部的 M5Core 供电。将这一种简单快捷的舵机驱动方式应用在你的项目中，将提升你的开发效率。Module Servo 基于 MEGA328 芯片进行 I2C 通信 (0x53) 。

## 产品特性

- 12 x 舵机驱动通道
- DC 输入: 5-7V
- DC 连接器类型: XT30 (母头)
- 电源设配器接口: 5.5mm x 2.1mm

## 包装内容

- 1 x Module Servo
- 1 x 常规公对公 XT30 DC 连接器

## 应用场景

- 人形机器人
- 仿生多关节机器人
- 3 轴舵机云台

## 规格参数

| 规格     | 参数                 |
| -------- | -------------------- |
| 通信接口 | I2C 通信 @ 0x53      |
| 产品尺寸 | 54.2 x 54.2 x 12.8mm |
| 产品重量 | 25.0g                |
| 包装尺寸 | 95.0 x 65.0 x 25.0mm |
| 毛重     | 45.0g                |

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/module/servo/servo_sch_01.webp" width="80%">

## 管脚映射

### Mega328 ISP 下载接口 Pin 脚定义

<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-cardkb/mega328_isp_sch_01.webp" width="30%" height="30%">

### M5-Bus

::m5-bus-table
| PIN       | LEFT | RIGHT | PIN       |
| --------- | ---- | ----- | --------- |
| GND       | 1    | 2     |           |
| GND       | 3    | 4     |           |
| GND       | 5    | 6     |           |
|           | 7    | 8     |           |
|           | 9    | 10    |           |
|           | 11   | 12    | 3V3       |
|           | 13   | 14    |           |
|           | 15   | 16    |           |
| SDA       | 17   | 18    | SCL       |
|           | 19   | 20    |           |
|           | 21   | 22    |           |
|           | 23   | 24    |           |
|           | 25   | 26    |           |
|           | 27   | 28    | 5V        |
|           | 29   | 30    |           |
::

## 软件开发

### Arduino

- [Module Servo Example with M5Core](https://github.com/m5stack/M5Stack/tree/master/examples/Modules/SERVO)

### UiFlow1

- [Module Servo UiFlow1 文档](/zh_CN/uiflow/blockly/module/servo)

## 数据手册

- [Module Servo 内置固件](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/Module/SERVO/firmware_328p)

### Easyloader

| Easyloader                                  | 下载链接                                                                                                       | 备注 |
| ------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | ---- |
| Module Servo Example Easyloader with M5Core | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/MODULE/EasyLoader_Servo_MODULE.exe) | /    |

## 相关视频

- 控制舵机旋转角度

<video id="example_video" controls>
  <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Module/SERVO_MODULE.mp4" type="video/mp4">
</video>

- Module Servo 的使用教程

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/%E6%95%99%E7%A8%8B/Servo/E4%20-%20Servo%20Demo(UIFlow%20Tutorials%205).mp4" type="video/mp4">
</video>
