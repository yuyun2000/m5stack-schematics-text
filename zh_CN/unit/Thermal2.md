# Unit Thermal2

<span class="product-sku">SKU:U149</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Thermal2 Unit/img-af8390fb-5df9-4811-867f-25a5fade4809.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Thermal2 Unit/img-71205bff-6de0-4b79-88f3-1756a52c3cf9.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/738/U149-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Thermal2 Unit/img-a08584df-9aff-4fcd-8422-1c36401986dd.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Thermal2 Unit/img-64cdbff8-eec2-4584-aa72-41f689143603.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Thermal2 Unit/img-5ab96af1-cf9e-4ceb-a3fe-5107f9f3ef38.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Thermal2 Unit/img-0f585676-503c-4d71-9f0c-18217edff1af.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Thermal2 Unit/img-e4586e43-44fa-48fb-a034-47cd8578cc0f.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Thermal2 Unit/img-6f7f04da-d235-4214-be3b-4ac5b702a426.webp">
</PictureViewer>

## 描述

**Unit Thermal2** 是一款搭载数据处理 MCU 的 MLX90640 热成像采集单元，成像像素为 32 x 24，视场角 110° x 75°，测温范围 -40℃ ~ 300℃，MCU 采用 ESP32，通过数据处理能实现高、低温告警，平均值、最高、最低值读取、数据缓存等功能。板上集成了蜂鸣器、RGB 指示灯、一个功能按键和一个复位按键，采用 I2C 与上位机通信。该产品可与上位机一并使用，也能单独使用，适合用于温度测量及异常告警等场合。

## 产品特性

- ESP32-PICO-D4
- MLX90640 红外 (IR) 传感器
- 复位按钮
- 内置无源蜂鸣器
- 集成可编程 RGB LED
- GROVE I2C/HY2.0-4P 接口
- 编程平台：Arduino/UiFlow

## 包装内容

- 1 x Unit Thermal2
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 高精度非接触式温度测量
- 移动检测
- 可视红外测温仪
- DIY 项目

## 规格参数

| 规格     | 参数                 |
| -------- | -------------------- |
| MCU      | ESP32-PICO-D4        |
| 传感器   | MLX90640             |
| 通信接口 | I2C 通信 @ 0x33      |
| 电源     | 5V @ 0.5A            |
| FOV      | 110°×75°             |
| 测量范围 | -40 ~ 300°C          |
| 分辨率   | 32 x 24              |
| 刷新率   | 0.5Hz-64Hz           |
| 工作温度 | -10 ~ 60°C           |
| 外壳材料 | 塑料                 |
| 产品尺寸 | 48.0 x 24.0 x 8.0mm  |
| 产品重量 | 7.7g                 |
| 包装尺寸 | 138.0 x 93.0 x 7.0mm |
| 毛重     | 12.8g                |

## 原理图

- [Unit Thermal2 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/603/SCH_UNIT-THERMAL2.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/603/SCH_UNIT-THERMAL2_sch_01.png">
</SchViewer>

## 管脚映射

### Unit Thermal2

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 尺寸图

<img alt="module size" src="https://static-cdn.m5stack.com/resource/docs/products/unit/Thermal2 Unit/img-6960aad1-5b8c-41aa-9fae-fee7abaf2cb5.png" width="100%" />

## 数据手册

- [MLX90640](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/hat/MLX90640-Datasheet-Melexis.pdf)
- [ESP32-PICO-D4](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/669/esp32-pico_series_datasheet_cn.pdf)

## 软件开发

### Arduino

- [Unit Thermal2 Arduino 驱动库](https://github.com/m5stack/M5Unit-Thermal2)
- [Unit Thermal2 FactoryTest](https://github.com/m5stack/M5Unit-Thermal2-Internal-FW/blob/main/examples/FactoryTest/FactoryTest.ino)

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Thermal2 Unit/arduinoCase-微信图片_20220923175447.jpg" width="100%"/>

### UiFlow1

- [Unit Thermal2 测试程序](https://flow.m5stack.com/?examples=unit_thermal2_demo)

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Thermal2 Unit/uiflowCase-1663845747734.jpg" width="100%"/>

### 内置固件

- [Unit Thermal2 内置固件](https://github.com/m5stack/M5Unit-Thermal2-Internal-FW)

### 通信协议

- [Unit Thermal2 I2C 通信协议](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/738/U149_M5UnitThermal2-I2C-Protocol.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/738/U149_M5UnitThermal2-I2C-Protocol_page_01.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/738/U149_M5UnitThermal2-I2C-Protocol_page_02.png">
