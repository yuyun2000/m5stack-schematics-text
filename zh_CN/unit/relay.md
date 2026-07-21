# Unit Relay

<span class="product-sku">SKU:U023</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/relay/relay_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/relay/relay_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/784/U023-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/relay/relay_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/relay/relay_06.webp">
</PictureViewer>

## 描述

**Unit Relay** 是一款单路继电器控制的高压驱动单元。它基于 HK4100F-DC5V-SHG 继电器，提供 SPDT（单刀双掷）切换，支持 AC 220V / DC 30V 高压通断，额定电流为 3A。该单元通过单个 GPIO 电平直接控制，具备物理隔离与状态指示灯，并通过 Grove HY2.0-4P 接口通信，采用 LEGO 兼容孔设计，便于灵活对接 LEGO 结构或使用螺丝固定。适用于智能家居、电器控制及自动化设备的安全电源管理场景。

## 产品特性

- 通道类型： 1 路 SPDT 继电器
- 负载能力： AC 220V@3A 或 DC 30V@3A
- 状态指示： 继电器状态指示灯
- 控制方式： 单个 GPIO 电平直接驱动
- 通信接口： Grove HY2.0-4P
- 2 x LEGO 兼容孔
- 开发平台
  - UiFlow1
  - UiFlow2
  - Arduino IDE

## 包装内容

- 1 x Unit Relay
- 1 x HY2.0-4P Grove 连接线 (20cm)
- 1 x 3.96 端子

## 应用场景

- 远程控制大功率电器，如冰箱，空调，电视等

## 规格参数

| 规格           | 参数                 |
| -------------- | -------------------- |
| 单路继电器功耗 | 5V@40mA              |
| 线圈动作时间   | 6ms                  |
| 线圈释放时间   | 4ms                  |
| 产品尺寸       | 48.0 x 24.0 x 8.0mm  |
| 产品重量       | 9.5g                 |
| 包装尺寸       | 138.0 x 93.0 x 9.0mm |
| 毛重           | 17.1g                |

## 原理图

- [Unit Relay 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/577/UNIT-RELAY.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/577/UNIT-RELAY_sch_01.png">
</SchViewer>

## 管脚映射

### Unit Relay

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.B   | GND   | 5V  | DIN    | NC    |
::

## 尺寸图

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/relay/model%20size.png" width="80%">

## 结构文件

- [Unit Relay 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/U023_Unit_Relay/Structures)

## 数据手册

- [继电器规格书](<https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/4relay/Datasheet-Realy-HK4100F-DC5V-SHG(1).pdf>)

## 软件开发

### Arduino

- [Unit Relay Test Example with M5Atom](https://github.com/m5stack/M5Unit-RELAY/blob/master/examples/Unit_RELAY_M5Atom/Unit_RELAY_M5Atom.ino)
- [Unit Relay Test Example with M5Core](https://github.com/m5stack/M5Unit-RELAY/blob/master/examples/Unit_RELAY_M5Core/Unit_RELAY_M5Core.ino)
- [Unit Relay Test Example with M5Core2](https://github.com/m5stack/M5Unit-RELAY/blob/master/examples/Unit_RELAY_M5Core2/Unit_RELAY_M5Core2.ino)
- [Unit Relay Test Example with M5StickC](https://github.com/m5stack/M5Unit-RELAY/blob/master/examples/Unit_RELAY_M5StickC/Unit_RELAY_M5StickC.ino)
- [Unit Relay Test Example with M5StickC-Plus](https://github.com/m5stack/M5Unit-RELAY/blob/master/examples/Unit_RELAY_M5StickCPlus/Unit_RELAY_M5StickCPlus.ino)

### UiFlow2

- [UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/relay.html)

### EasyLoader

| Easyloader                 | 下载链接                                                                                                                            | 备注 |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ---- |
| Unit Relay Test Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/UNIT/For%20M5Core/EasyLoader_Relay_UNIT_With_M5Core.exe) | /    |

## 相关视频

- 继电器线圈循环通断，触点作为开关用于电路控制。

<video id="example_video" controls>
  <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Unit/Relay_UNIT.mp4" type="video/mp4">
</video>

- **用 UiFlow 和 Unit RELAY 控制 家庭灯**

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/LukeVideo/Blinking%20a%20bulb%20with%20the%20M5%20Relay%20unit..mp4" type="video/mp4">
</video>
