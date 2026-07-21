# Unit INA226-1A

<span class="product-sku">SKU:U200-1A</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1172/Unit_INA226-1A_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1172/Unit_INA226-1A_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1172/Unit_INA226-1A_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1172/Unit_INA226-1A_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1172/Unit_INA226-1A_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1172/Unit_INA226-1A_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1172/Unit_INA226-1A_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1172/Unit_INA226-1A_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1172/Unit_INA226-1A_09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1172/Unit_INA226-1A_10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1172/Unit_INA226-1A_11.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1172/U200-1A_Weight.jpg">
</PictureViewer>

## 描述

**Unit INA226-1A** 是一款全隔离的高精度电流、电压及功率测量单元，适用于 DC 0 ~ 30V 电压、最大 1A 电流的测量场景，支持同时测量电压电流。用户可通过 I2C 通信接口读取该单元获取的电流、电压、功率等关键参数，并支持多种主控平台使用。其内部还集成了隔离电源模块和 I2C 信号隔离器，实现测量端与主控端的全面电气隔离，且有自恢复保险丝，在超过电流量程时可自行熔断，能有效保障设备及人员安全，提升系统抗干扰能力，适用于电源管理、电池监控、工业安全等多种电气参数采集应用场景。

## 产品特性

- 集成 16 位高精度 ADC
- 电流电压功率一体测量
- ±1A 量程，双向电流
- 宽电压输入（DC 0 ~ 30V）
- I2C 通信接口
- 电源与信号隔离
- 开发平台：
  - Arduino
  - UiFlow2

## 包装内容

- 1 x Unit INA226-1A
- 1 x HY2.0-4P Grove 连接线 (20cm)
- 1 x HT3.96-4P 端子

## 应用场景

- 电源监控
- 功耗分析
- 电机控制电流反馈

## 规格参数

| 规格         | 参数                                    |
| ------------ | --------------------------------------- |
| 功率检测芯片 | INA226，高精度、双向电流 / 功率监测芯片 |
| 电压检测范围 | DC 0 ~ 30V                              |
| 电流检测范围 | ±1A（双向电流测量）                     |
| 通信接口     | I2C 通信 @0x41                          |
| 工作电流     | DC 5.01V@16.55mA                        |
| 产品尺寸     | 58.0 x 24.0 x 10.2mm                    |
| 产品重量     | 8.5g                                    |
| 包装尺寸     | 138.0 x 93.0 x 11.2mm                   |
| 毛重         | 16.7g                                   |

## 原理图

- [Unit INA226-1A 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1172/SCH_Unit_ina226-1A_SCH_Main_V0.3_20250625_2025_08_11_11_28_24.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1172/SCH_Unit_ina226-1A_SCH_Main_V0.3_20250625_2025_08_11_11_28_24_page_01.png">
</SchViewer>

## 管脚映射

### HY2.0-4P

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 尺寸图

- [Unit INA226-1A 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/839/U085_MODEL_SIZE.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/839/U085_Model_Size.jpg" width="100%">

## 结构文件

- [Unit INA226-1A 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/U200-1A_Unit_INA226-1A/Structures)

## 数据手册

- [INA226 数据手册](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1171/INA226.pdf)

## 软件开发

### Arduino

- [Unit INA226-10A / Unit INA226-1A Arduino 使用教程](/zh_CN/arduino/projects/unit/unit_ina226_1a_10a)
- [Unit INA226-1A Arduino 测试程序](https://github.com/m5stack/M5Unit-METER/blob/develop/examples/UnitUnified/UnitINA226/PlotToSerial)

### Home Assistant

- [Unit INA226 10A/1A Home Assistant 集成](/zh_CN/homeassistant/sensor/unit_ina226_10a_1a)

## 相关视频

- Unit INA226-10A / Unit INA226-1A 功能介绍

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1171/U200_U200-1A_video.mp4" type="video/mp4"></video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=115171712437580&bvid=BV1JFYPz1ECT&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/5BERvcfdzj4?si=WbUOfeQmwcqffkMn" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>

## 产品对比

::compare-table
| 产品对比表 | [Unit INA226-1A](/zh_CN/unit/Unit_INA226-1A) ![Unit INA226-1A](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1172/Unit_INA226-1A_02.webp) | [Unit INA226-10A](/zh_CN/unit/Unit_INA226-10A) ![Unit INA226-1A](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1171/Unit_INA226-10A_02.webp) |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| 量程       | ±1A，双向电流                                                                                                                                | ±10A，双向电流                                                                                                                                  |
| 分流电阻   | 80mΩ                                                                                                                                         | 5mΩ                                                                                                                                             |
| 电流分辨率 | 32μA                                                                                                                                         | 0.32mA                                                                                                                                          |
::
