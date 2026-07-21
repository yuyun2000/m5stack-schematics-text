# Unit 2Relay

<span class="product-sku">SKU:U131</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/2relay/2relay_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/2relay/2relay_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/783/U131-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/2relay/2relay_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/2relay/2relay_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/2relay/2relay_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/2relay/2relay_07.webp">
</PictureViewer>

## 描述

**Unit 2Relay** 是一款双路继电器控制的高压驱动单元。它集成 2 路常开型（NO）机械继电器，通过 GPIO 电平直接控制，支持 AC 250V / DC 28V 高压通断，每路额定电流为 8A。该单元通过 Grove HY2.0-4P 接口通信，具备物理隔离与状态指示灯，并采用 LEGO 兼容孔设计，便于灵活对接 LEGO 结构或使用螺丝固定。适用于智能家居、电器控制及工业设备的安全电源管理场景。

## 产品特性

- 通道数量： 2 路继电器独立控制
- 负载能力： AC 250V@8A 或 DC 28V@8A
- 状态指示： 每路独立 LED 指示灯
- 控制方式： GPIO 电平直接驱动
- 通信接口： Grove HY2.0-4P
- 2 x LEGO 兼容孔
- 开发平台
  - UiFlow1
  - UiFlow2
  - Arduino IDE

## 包装内容

- 1 x Unit 2Relay
- 1 x HY2.0-4P Grove 连接线 (20cm)
- 2 x HT3.96-4P 端子

## 应用场景

- 交流 / 直流信号切换
- 数字设备电源通断

## 规格参数

| 规格         | 参数                  |
| ------------ | --------------------- |
| 最大通断电压 | AC 250V / DC 28V      |
| 额定电流     | 8A                    |
| 线圈控制电压 | DC 5V                 |
| 线圈功耗     | 5V@154mA              |
| 线圈动作时间 | ≤ 8ms                 |
| 线圈释放时间 | ≤ 5ms                 |
| 触点形式     | A 常开型              |
| 触点材料     | AgSnO2                |
| 继电器指示灯 | 蓝色 x2               |
| 产品尺寸     | 56.0 x 24.0 x 19.0mm  |
| 产品重量     | 20.0g                 |
| 包装尺寸     | 138.0 x 93.0 x 17.0mm |
| 毛重         | 31.2g                 |

## 操作说明

\#> 该继电器通过 IO 输出高低电平信号驱动，因此在连接主控前，请确保连接的端口 IO 支持配置为输出模式。(注: ESP32 的 G36 不允许配置为输出模式，因此 PORT.B 将无法正常驱动)

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/2relay/2relay_sch_01.webp" width="80%">

## 管脚映射

### Unit 2Relay

::grove-table
| HY2.0-4P | Black | Red | Yellow  | White   |
| -------- | ----- | --- | ------- | ------- |
| PORT.A   | GND   | 5V  | RELAY-2 | RELAY-1 |
::

## 尺寸图

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/2relay/model%20size.png" width="100%">

## 结构文件

- [Unit 2Relay 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/U131_Unit_2Relay/Structures)

## 软件开发

### Arduino

- [Unit 2Relay Example with M5Atom](https://github.com/m5stack/M5Unit-RELAY/blob/master/examples/Unit_2RELAY_M5Atom/Unit_2RELAY_M5Atom.ino)
- [Unit 2Relay Example with M5Core](https://github.com/m5stack/M5Unit-RELAY/blob/master/examples/Unit_2RELAY_M5Core/Unit_2RELAY_M5Core.ino)
- [Unit 2Relay Example with M5Core2](https://github.com/m5stack/M5Unit-RELAY/blob/master/examples/Unit_2RELAY_M5Core2/Unit_2RELAY_M5Core2.ino)
- [Unit 2Relay Example with M5StickC](https://github.com/m5stack/M5Unit-RELAY/blob/master/examples/Unit_2RELAY_M5StickC/Unit_2RELAY_M5StickC.ino)
- [Unit 2Relay Example with M5StickC-Plus](https://github.com/m5stack/M5Unit-RELAY/blob/master/examples/Unit_2RELAY_M5StickCPlus/Unit_2RELAY_M5StickCPlus.ino)

### UiFlow1

- [Unit 2Relay UiFlow1 文档](/zh_CN/uiflow/blockly/unit/2relay)

### UiFlow2

- [Unit 2Relay UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/relay.html)
