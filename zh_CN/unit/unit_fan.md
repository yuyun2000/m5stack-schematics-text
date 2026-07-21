# Unit Fan

<span class="product-sku">SKU:U063</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/unit_fan/unit_fan_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/unit_fan/unit_fan_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/759/U063-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/unit_fan/unit_fan_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/unit_fan/unit_fan_06.webp">
</PictureViewer>

## 描述

**Unit Fan** 是一款基于 N20 直流电机的动力驱动单元。它通过 GPIO 电平或 PWM 信号控制，输出轴空载转速高达 8800 RPM，支持精确的启停与无级调速。该单元通过 Grove HY2.0-4P 接口通信，内置高效驱动与保护电路，并采用 LEGO 兼容孔设计，便于灵活对接 LEGO 结构或使用螺丝固定。适用于机器人驱动、模型动力、主动散热及各类运动控制场景。

## 产品特性

- 电机类型： N20 直流电机
- 空载转速： 8800 RPM
- 旋转方向： 单向旋转
- 控制方式： GPIO / PWM 调速
- 通信接口： Grove HY2.0-4P
- 2 x LEGO 兼容孔
- 开发平台
  - UiFlow1
  - UiFlow2
  - Arduino IDE

## 包装内容

- 1 x Unit Fan
- 1 x HY2.0-4P Grove 连接线 (20cm)
- 2 x 螺旋桨

## 应用场景

- 运动控制

## 规格参数

| 规格     | 参数                  |
| -------- | --------------------- |
| 产品尺寸 | 32.0 x 24.0 x 12.2mm  |
| 产品重量 | 9.3g                  |
| 包装尺寸 | 138.0 x 93.0 x 13.2mm |
| 毛重     | 15.2g                 |

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/unit_fan/unit_fan_sch_01.webp" width="80%">

## 管脚映射

### Unit Fan

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.B   | GND   | 5V  | DIN    | NC    |
::

## 尺寸图

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/unit_fan/model%20size.png" width="100%">

## 结构文件

- [Unit Fan 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/U063_Unit_Fan/Structures)

## 软件开发

### Arduino

- [Unit Fan 测试程序](https://github.com/m5stack/M5Stack/tree/master/examples/Unit/FAN)

### UiFlow1

- [Unit Fan UiFlow1 文档](/zh_CN/uiflow/blockly/unit/fan)

### EasyLoader

| Easyloader               | 下载链接                                                                                    | 备注 |
| ------------------------ | ------------------------------------------------------------------------------------------- | ---- |
| Unit Fan Test Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Unit/EasyLoader_FAN.exe) | /    |
