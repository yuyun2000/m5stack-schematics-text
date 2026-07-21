# Unit CO2L

<span class="product-sku">SKU:U104</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/CO2L/img-9d1ab7e5-8692-4652-8714-9300367c0d37.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/CO2L/img-c1f0e30d-0894-409c-9efd-e6bb0ae102c6.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/CO2L/img-d9d98d07-cb11-4d14-9f12-d923e7c85ab0.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/CO2L/img-b986f421-b9fd-4a95-a5bf-445d7c93e2b6.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/CO2L/img-141ee16c-438e-45d5-bf4c-2f6dd7380159.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/CO2L/img-b35f27a3-219c-4b8f-923e-25f2796f4d5b.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/CO2L/img-6406b7d6-32b3-468b-bc1f-8ed21ddda32a.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/CO2L/img-e356ce5a-d24c-4277-9b78-1a3f58c9dbe9.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/CO2L/img-db400d57-6ac3-4d71-ad3d-e62e70a562b1.webp">
</PictureViewer>

## 描述

**Unit CO2L** 是一颗数字式空气 CO₂ 浓度检测单元，具有单次测量的低功耗模式，内置 Sensirion 的 **SCD41** 传感器及电源降压电路，采用 I2C 通信。该单元适用于空气环境条件测量，CO₂ 测量的典型精度为 ± (40 ppm + 5 % 读数)，量程范围：400 ppm ~ 5000 ppm，同时测量环境温度和湿度。

## 产品特性

- CO2 浓度检测
- 温湿度测量
- 低功耗 (支持单次测量)
- 集成 5V -> 3.3V LDO
- HY2.0 4P 接口
- 2 x LEGO 兼容孔

## 包装内容

- 1 x Unit CO2L
- 1 x HY2.0 连接线 (20CM)

## 应用场景

- CO2 浓度检测
- 温湿度监测

## 规格参数

| 规格         | 参数                       |
| ------------ | -------------------------- |
| 传感器       | SCD41                      |
| CO2 测量范围 | 400 ~ 5000 ppm             |
| CO2 采样精度 | ± (40 ppm + 5% of reading) |
| 温度范围     | -10 ~ 60 °C                |
| 湿度范围     | 0 ~ 95 % RH                |
| 通信接口     | I2C 通信 @ 0x62            |
| 产品尺寸     | 48.0 x 24.0 x 16.0mm       |
| 产品重量     | 7.5g                       |
| 包装尺寸     | 138.0 x 93.0 x 17.0mm      |
| 毛重         | 12.8g                      |

## 原理图

- [Unit CO2L 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/591/SCH_UNIT_CO2L.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/591/SCH_UNIT_CO2L_sch_01.png">
</SchViewer>

## 管脚映射

### Unit CO2L

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 尺寸图

<img alt="module size" src="https://static-cdn.m5stack.com/resource/docs/products/unit/CO2L/img-6c5b69c0-95f2-45c8-8c6e-468135afb953.png" width="100%" />

## 数据手册

- [SCD41](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/co2/SCD41.pdf)
- [VRH3301NLX](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/co2/VRH3301NLX.pdf)
- [Pin Map](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/co2/pinmap.png)

## 软件开发

### Arduino

- [Unit CO2L with M5Core](https://github.com/m5stack/M5Unit-ENV/blob/master/examples/Unit_CO2_M5Core/Unit_CO2_M5Core.ino)
- [Unit CO2L with M5Atom](https://github.com/m5stack/M5Unit-ENV/blob/master/examples/Unit_CO2_M5Atom/Unit_CO2_M5Atom.ino)
- [Unit CO2L with M5StickC](https://github.com/m5stack/M5Unit-ENV/blob/master/examples/Unit_CO2_M5StickC/Unit_CO2_M5StickC.ino)
- [Unit CO2L with M5StickCPlus](https://github.com/m5stack/M5Unit-ENV/blob/master/examples/Unit_CO2_M5StickCPlus/Unit_CO2_M5StickCPlus.ino)

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/CO2L/arduinoCase-1669348273417微信图片_20221125113505.png" width="100%"/>

### UiFlow1

- [Unit CO2L UiFlow1 文档](/zh_CN/uiflow/blockly/unit/co2l)

### UiFlow2

- [Unit CO2L UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/co2l.html)

### EasyLoader

| Easyloader                | 下载链接                                                                                                  | 备注 |
| ------------------------- | --------------------------------------------------------------------------------------------------------- | ---- |
| Unit CO2L Test Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/CO2L/CO2L%20Unit.exe) | /    |

### Home Assistant

- [Unit CO2L Home Assistant 集成](/zh_CN/homeassistant/sensor/unit_co2_co2l_sensor)
