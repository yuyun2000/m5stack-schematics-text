# Module Fan v1.1

<span class="product-sku">SKU:M013-V11</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1125/M013-V11_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1125/M013-V11_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1125/M013-V11_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1125/M013-V11_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1125/M013-V11_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1125/M013-V11_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1125/M013-V11_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1125/M013-V11_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1125/M013-V11_09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1125/M013-V11-weight.jpg">
</PictureViewer>

## 描述

**Module Fan v1.1** 是一款为 M5Stack 堆叠系统设计的散热模块，内置 STM32 微控制器，采用 **I2C** 协议进行控制，支持散热风扇转速的**读取和控制**，并具备**堵转保护**功能。该模块主要用于堆叠系统的散热，能够有效提高系统的散热性能，适用于嵌入式设备，智能硬件及其他需要散热管理的应用场景。

## 产品特性

- M5Stack 堆叠系统
- STM32 微控制器
- I2C 协议控制
- 风扇转速读取与控制
- 堵转保护功能
- 开发平台
  - UiFlow1
  - UiFlow2
  - Arduino IDE

## 包装内容

- 1 x Module Fan v1.1

## 应用场景

- M5Stack 设备散热

## 规格参数

| 规格                       | 参数                                                                     |
| -------------------------- | ------------------------------------------------------------------------ |
| MCU                        | STM32F030F4P6                                                            |
| 通讯方式                   | I2C (0x18)                                                               |
| 工作电压                   | 5V                                                                       |
| 噪音测试 (环境噪声 40.8dB) | PWM20%:48.6dB<br/>PWM60%:64.5dB<br/>PWM100%:70.6dB                       |
| 工作功耗                   | PWM20%:DC 5V@13.52mA<br/>PWM60%:DC 5V@56.19mA<br/>PWM100%:DC 5V@125.14mA |
| 待机功耗                   | DC 5V@503.49uA                                                           |
| 风扇转数速                 | 11500RPM±10%                                                             |
| 最大风量                   | 1.23 CFM                                                                 |
| 风扇转速                   | 支持读取风扇转速和 PWM 调速                                              |
| 堵转保护                   | 支持堵转保护功能                                                         |
| 工作温度                   | 0~40°C                                                                   |
| 产品尺寸                   | 54.0 x 54.0 x 13.1mm                                                     |
| 产品重量                   | 14.7g                                                                    |
| 包装尺寸                   | 95 x 184 x 15.7mm                                                        |
| 毛重                       | 28.3g                                                                    |

## 操作说明

?> 堵转说明 | 如果风扇因异物导致堵转锁死，需排除异物后，风扇将会自动恢复转动。然而，长时间堵转可能会导致风扇损坏，甚至存在烧坏的风险，因此请及时清理堵塞物并确保风扇正常运转。

\#> 散热模块安装 | Module Fan v1.1 设计的进风口在模块底部，为了取得较为有效的散热效果，推荐将其堆叠在需要散热的模块的顶部，如下图所示。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1125/module_fan_v1.1_arduino_example_04.jpg" width="30%">

## 原理图

- [Module Fan v1.1 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1125/M013_v11_Schematic.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1125/M013_v11_Schematic_sch_01.png">
</SchViewer>

## 管脚映射

### Fan

| Fan   | VCC | GND   | FG_OUT | PWM  |
| ----- | --- | ----- | ------ | ---- |
| Color | Red | Black | Yellow | Blue |

> FG_OUT 为散热风扇的转速波形输出引脚，PWM 为散热风扇的转速控制引脚。

### STM32

| STM32F030F4P6 | PA6    | PA7    | PA9 | PA10 |
| ------------- | ------ | ------ | --- | ---- |
| Fan           | FanCtr | FG_OUT | SCL | SDA  |

### M5-Bus

::m5-bus-table
| PIN      | LEFT | RIGHT | PIN      |
| -------- | ---- | ----- | -------- |
| GND      | 1    | 2     |          |
| GND      | 3    | 4     |          |
| GND      | 5    | 6     |          |
|          | 7    | 8     |          |
|          | 9    | 10    |          |
|          | 11   | 12    | 3V3      |
|          | 13   | 14    |          |
|          | 15   | 16    |          |
| SDA      | 17   | 18    | SCL      |
|          | 19   | 20    |          |
|          | 21   | 22    |          |
|          | 23   | 24    |          |
| HPWR     | 25   | 26    |          |
| HPWR     | 27   | 28    | 5V       |
| HPWR     | 29   | 30    |          |
::

## 尺寸图

- [Module Fan v1.1 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1125/M013_v11_Model_Size.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1125/M013_v11_Model_Size_sch_01.png" width="100%">

## 数据手册

- [散热风扇规格书](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1125/M013_Fan_Datasheet.pdf)

## 软件开发

### Arduino

- [Module Fan v1.1 Arduino Guide](/zh_CN/arduino/projects/module/module_fan_v1.1)
- [Module Fan v1.1 Arduino 驱动库](https://github.com/m5stack/M5Module-Fan)

### UiFlow1

- Coming soon...

### UiFlow2

- [Module Fan v1.1 UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/module/fan.html)

### 内置固件

- [Module Fan v1.1 内置固件](https://github.com/m5stack/M5Module-Fan-Internal-FW)

### 通信协议

- [Module Fan v1.1 I2C Protocol](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1125/Module-FAN_Protol_ZH.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1125/Module-FAN_Protol_ZH.png" width="100%">

## 相关视频

- Module Fan v1.1 产品介绍以及案例展示

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1125/M013_V11_Module_Fan_v11_video.mp4" type="video/mp4"></video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=114141121480152&bvid=BV1UkRJY7EV8&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/uxfyvA2DdY8?si=RpUN6ELLW3HkyAFA" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>

## 产品对比

::compare-table
| 产品对比表 | [Module Fan v1.1](/zh_CN/module/Module%20Fan%20v1.1) ![Module Fan v1.1](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1125/M013-V11_02.webp)                         | [Module Fan](/zh_CN/module/fan) ![Module Fan](https://static-cdn.m5stack.com/resource/docs/products/module/fan/fan_01.webp)                         |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| 通讯方式   | I2C 通讯 (0x18)                                                                                                                                                         | /                                                                                                                                                   |
| 转速       | 11500RPM ±10%                                                                                                                                                           | 7500RPM ±10%                                                                                                                                        |
| 调速控制   | 支持（通过 I2C 协议控制转速）                                                                                                                                           | 不支持                                                                                                                                              |
::
