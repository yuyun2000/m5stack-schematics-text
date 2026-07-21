# Unit CO2

<span class="product-sku">SKU:U103</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/co2/co2_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/co2/co2_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/726/U103-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/co2/co2_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/co2/co2_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/co2/co2_06.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/co2/co2_07.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/co2/co2_08.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/co2/co2_09.webp">
</PictureViewer>

## 描述

**Unit CO2** 是一颗数字式空气 CO₂ 浓度检测单元，内置 Sensirion 的 **SCD40** 传感器及电源降压电路，采用 I2C 通信。该单元适用于空气环境条件测量，CO₂ 测量的典型精度为 ± (50 ppm + 5 % 读数)，量程范围：400 ppm ~ 2000 ppm，同时测量环境温度和湿度。

## 产品特性

- CO2 浓度检测
- 温湿度测量
- I2C 通讯 (0x62)
- 集成 5V -> 3.3V DC-DC
- 2 x LEGO 兼容孔
- HY2.0 4P 接口

## 包装内容

- 1 x Unit CO2
- 1 x HY2.0 连接线 (20CM)

## 应用场景

- CO2 浓度检测
- 温湿度监测

## 规格参数

| 规格         | 参数                       |
| ------------ | -------------------------- |
| CO2 测量范围 | 400 ~ 2000 ppm             |
| CO2 采样精度 | ± (50 ppm + 5% of reading) |
| 温度范围     | -10 ~ 60 °C                |
| 湿度范围     | 0 ~ 95 % RH                |
| 通信协议     | I2C:0x62                   |
| 外壳材质     | Plastic (PC)               |
| 产品尺寸     | 48.0 x 24.0 x 16.0mm       |
| 产品重量     | 7.6g                       |
| 包装尺寸     | 138.0 x 93.0 x 17.0mm      |
| 毛重         | 13.0g                      |

## 原理图

- [Unit CO2 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/590/SCH_UNIT_CO2.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/590/SCH_UNIT_CO2_sch_01.png">
</SchViewer>

## 管脚映射

### Unit CO2

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 尺寸图

<img alt="module size" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/co2/%E5%B0%BA%E5%AF%B8%E5%9B%BE.jpg" width="100%" />

## 结构文件

- [Unit CO2 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/U103_Unit_CO2/Structures)

## 数据手册

- [SCD40](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/co2/SCD40.pdf)
- [SY8089AAAC](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/co2/SY8089AAAC.pdf)

## 软件开发

### Arduino

- [Unit CO2 with M5Atom](https://github.com/m5stack/M5Unit-ENV/blob/master/examples/Unit_CO2_M5Atom/Unit_CO2_M5Atom.ino)
- [Unit CO2 with M5AtomS3](https://github.com/m5stack/M5Unit-ENV/blob/master/examples/Unit_CO2_M5AtomS3/Unit_CO2_M5AtomS3.ino)
- [Unit CO2 with M5AtomS3Lite](https://github.com/m5stack/M5Unit-ENV/blob/master/examples/Unit_CO2_M5AtomS3Lite/Unit_CO2_M5AtomS3Lite.ino)
- [Unit CO2 with M5Core](https://github.com/m5stack/M5Unit-ENV/blob/master/examples/Unit_CO2_M5Core/Unit_CO2_M5Core.ino)
- [Unit CO2 with M5Core2](https://github.com/m5stack/M5Unit-ENV/blob/master/examples/Unit_CO2_M5Core2/Unit_CO2_M5Core2.ino)
- [Unit CO2 with M5StickC](https://github.com/m5stack/M5Unit-ENV/blob/master/examples/Unit_CO2_M5StickC/Unit_CO2_M5StickC.ino)
- [Unit CO2 with M5StickCPlus](https://github.com/m5stack/M5Unit-ENV/blob/master/examples/Unit_CO2_M5StickCPlus/Unit_CO2_M5StickCPlus.ino)

### UiFlow1

- [Unit CO2 UiFlow1 文档](/zh_CN/uiflow/blockly/unit/co2)

### UiFlow2

- [Unit Co2 UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/co2.html)

### Home Assistant

- [Unit CO2 Home Assistant 集成](/zh_CN/homeassistant/sensor/unit_co2_co2l_sensor)
