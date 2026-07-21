# Unit Joystick

<span class="product-sku">SKU:U024</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/joystick/joystick_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/joystick/joystick_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/joystick/joystick_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/joystick/joystick_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/joystick/joystick_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/joystick/joystick_06.webp">
</PictureViewer>

## 描述

**Unit Joystick** 是一款摇杆控制输入单元，采用 I2C 通信接口，支持三轴控制信号输入 (X / Y 轴偏移模拟量输入，Z 轴按键数字量输入)。适用于游戏 / 机器人控制等应用场景。

## 产品特性

- 三轴输入:
  - X/Y 轴偏移模拟量输入
  - Z 轴按键数字量输入
- 2 x LEGO 兼容孔
- 开发平台: Arduino，UiFlow (Blockly，Python)

## 包装内容

- 1 x Unit Joystick
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 游戏控制器
- 机器人远程控制

## 规格参数

| 规格              | 参数           |
| ----------------- | -------------- |
| 通讯协议          | I2C:0x52       |
| X、Y 轴偏移输出值 | 0-255          |
| Z 轴按键输出值    | 0/1            |
| 产品重量          | 11g            |
| 毛重              | 27g            |
| 产品尺寸          | 48 x 24 x 32mm |
| 包装尺寸          | 75 x 45 x 30mm |

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/joystick/joystick_sch_01.webp" width="80%">

## 管脚映射

### Unit Joystick

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 软件开发

### Arduino

- [Unit Joystick Get Value Example](https://github.com/m5stack/M5Stack/tree/master/examples/Unit/JOYSTICK)

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/joystick/joystick_08.webp" width="70%">

### UiFlow1

- [Unit Joystick UiFlow1 文档](/zh_CN/uiflow/blockly/unit/joystick)

### UiFlow2

- [Unit Joystick UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/joystick.html)

### 通讯协议

- 协议类型 I2C
- I2C Address: **0x52**

> JOYSTICK REG 0x52

| REG  | len | description  | return values                                     |
| :--: | :-: | :----------- | :-----------------------------------------------: |
| 0x52 | 3   | 读取摇杆状态 | \[0] X VALUE<br/>\[1] Y VALUE<br/>\[2] BTN STATUS |

### EasyLoader

| Easyloader               | 下载链接                                                                                                                               | 备注 |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------- | ---- |
| Unit Joystick Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/UNIT/For%20M5Core/EasyLoader_Joystick_UNIT_With_M5Core.exe) | /    |

## 相关视频

- 显示摇杆 XY 数据及按钮状态.

<video id="example_video" controls>
  <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Unit/Joystick_UNIT.mp4" type="video/mp4">
</video>
