# Unit EXT.IO2

<span class="product-sku">SKU:U011-B</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/extio2/extio2_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/extio2/extio2_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/789/U011-B-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/extio2/extio2_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/extio2/extio2_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/extio2/extio2_05.webp">
</PictureViewer>

## 描述

**Unit EXT.IO2**是一款**IO 拓展单元**，模块基于 STM32F030 主控开发，采用 I2C 通信接口，提供 8 路 IO 拓展。每路 IO 支持独立配置 **数字输入 / 输出**，**ADC**，**SERVO 控制**，**RGB LED 控制**模式。支持配置设备 I2C 地址，这意味着在同一 I2C 总线上允许用户挂载多个 **Unit EXT.IO2** UNIT 拓展出更多的 IO 资源。适用于多路数字 / 模拟信号采集，与灯光 / 舵机控制等应用场景。

## 产品特性

- 8 通道输入输出拓展：
  - 数字输入 / 输出
  - ADC 输入
  - SERVO 控制 (PWM)
  - RGB LED 控制
- I2C 通信接口:
  - 支持配置 I2C 地址

## 包装内容

- 1 x Unit EXT.IO2
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- IO 拓展
- 舵机控制
- 多路灯光控制
- 多路模拟信号采集

## 规格参数

| 规格                   | 参数                                           |
| ---------------------- | ---------------------------------------------- |
| MCU                    | STM32F030F4P6                                  |
| 通信接口               | I2C 通信 @ 0x45                                |
| IO 扩展数量            | 8                                              |
| IO 接口 PIN 间距       | 2.54mm                                         |
| IO 支持模式            | 数字输入 / 输出，ADC，SERVO 控制，RGB LED 控制 |
| IO 支持输入 / 输出电平 | 3.3V                                           |
| 产品尺寸               | 32.0 x 24.0 x 10.2mm                           |
| 产品重量               | 5.0g                                           |
| 包装尺寸               | 138.0 x 93.0 x 11.2mm                          |
| 毛重                   | 10.0g                                          |

## 原理图

- [Unit EXT.IO2 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/574/Sch_UNIT-EXTIO2.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/574/Sch_UNIT-EXTIO2_sch_01.png">
</SchViewer>

## 管脚映射

### Unit EXT.IO2

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 尺寸图

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/extio2/3ad33fb83c15cac23cfb9ae5dccf684.png" width="80%">

## 软件开发

### Arduino

- [Unit EXT.IO2 ADC Input Example](https://github.com/m5stack/M5Unit-EXTIO2/blob/main/examples/Unit_EXTIO2_M5Core/ADC_INPUT/ADC_INPUT.ino)
- [Unit EXT.IO2 Digital Input/Output Example](https://github.com/m5stack/M5Unit-EXTIO2/blob/main/examples/Unit_EXTIO2_M5Core/DIGITAL_INPUT_OUTPUT/DIGITAL_INPUT_OUTPUT.ino)
- [Unit EXT.IO2 RGB LED Control Example](https://github.com/m5stack/M5Unit-EXTIO2/blob/main/examples/Unit_EXTIO2_M5Core/RGB_LED_CTL/RGB_LED_CTL.ino)
- [Unit EXT.IO2 Servo Control Example](https://github.com/m5stack/M5Unit-EXTIO2/blob/main/examples/Unit_EXTIO2_M5Core/SERVO_CTL/SERVO_CTL.ino)

### UiFlow1

- [Unit EXT.IO2 UiFlow1 文档](/zh_CN/uiflow/blockly/unit/ext_io2)

### UiFlow2

- [Unit EXT.IO2 UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/extio2.html)

### 内置固件

- [Unit EXT.IO2 内置固件](https://github.com/m5stack/M5Unit-EXTIO2-Internal-FW)

| 固件版本 | 修改记录                                            | 通信协议                                                                                                          |
| -------- | --------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| v1       | 首次发布时版本                                      | [Unit EXT.IO2 I2C Protocol v1](https://github.com/m5stack/M5Unit-EXTIO2/blob/main/docs/V1/EXTIO2_V1_Protocol.pdf) |
| v3       | 1. 新增 PWM 控制模式 <br/> 2. 新增 I2C IAP 升级功能 | [Unit EXT.IO2 I2C Protocol v3](https://github.com/m5stack/M5Unit-EXTIO2/blob/main/docs/V3/EXTIO2_V3_Protocol.pdf) |

\#> M5 DAPLink | 若您没有 STM32 下载器工具，可参考[M5 DAPLink](/zh_CN/guide/develop_tools/daplink)教程，使用 Core2 或 CoreS3 作为烧录器，为设备完成固件更新。

### 通信协议

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/789/EXTIO2_V3_Protocol_page_01.png" width="100%">

## 相关视频

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113423190853328&bvid=BV1AcDnYhEFa&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/goepTBsgYWk?si=uyT2ye0dgfuswlo3" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
