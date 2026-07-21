# Module13.2 Dual Kmeter

<span class="product-sku">SKU:M127</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/DualKmeter Module13.2/img-91942504-2fb3-4d8e-90d2-fbf0761bb1d1.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/DualKmeter Module13.2/img-1dae3c86-d038-4451-8009-6e454ce141eb.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/DualKmeter Module13.2/img-2d93739a-460b-44a9-97ad-78c470e51eee.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/DualKmeter Module13.2/img-989af2ea-8de0-4f19-9963-420ef22bd6cf.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/DualKmeter Module13.2/img-b5b6da8a-3ffd-4d16-a0c9-fe6685ca728b.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/DualKmeter Module13.2/img-759ea6d0-018d-46bf-adb8-b7abe0a04960.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/DualKmeter Module13.2/img-d9b3f638-258b-4aab-8c52-a5f8349189fe.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/DualKmeter Module13.2/img-fea0c719-1d64-4244-8cb1-6b449e5a5537.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/DualKmeter Module13.2/img-f7090344-96b9-4fb9-ba44-6d78005a2754.webp">
</PictureViewer>

## 描述

**Module13.2 Dual Kmeter** 是一款**基于 “MAX31855KASA + stm32f030f4p6 + 电气隔离” 方案**的双通道 K 型温度测量模块。该模块内置了**两路 K 型热电偶传感器接口**，采用信号**继电器轮流测量两路的温度值**，支持的测量范围为 **-200°C ~ 1350°C** ，测量精度为 ±2°C 。同时，该模块还内置了 **B0505LS-1WR2 和 CA-IS3020S** 等电压和信号隔离芯片，保证了系统的**稳定性和安全性**。此外，模块内置**拨码开关**，可方便地切换不同的 I2C 地址，以满足用户不同的应用需求。能应用于**工业自动化、仪表检测**等多个场景。

## 产品特性

- STM32F030F4P6,Cortex-M0 内核的 32 位微控制器
- MAX31855KASA+T:(14Bit ADC、0.25°C 分辨率，精度 ±2%)
- 支持探头类型: K 型 - 支持接入探头测量范围 -200°C ~ 1350°C
- 具有电气隔离
- 双路 K 型热电偶
- 拨码切换 I2C 地址 (默认 0x11)
- 编程平台：Arduino、UiFlow

## 包装内容

- 1 × Module13.2 Dual Kmeter
- 2 × K 型热电偶

## 应用场景

- 工业自动化
- 仪表检测

## 规格参数

| 规格           | 参数                                        |
| -------------- | ------------------------------------------- |
| MCU            | STM32F030F4P6@Cortex-M0 内核，32 位微控制器 |
| Flash          | 64KB                                        |
| SRAM           | 8KB                                         |
| 通信接口       | I2C 通信 @ 0x11 ~ 0x20                      |
| DC-DC          | ME3116                                      |
| LDO            | HX6306P332、MD5333                          |
| 数字温度传感器 | MAX31855KASA+T                              |
| 继电器         | AGQ200A4H                                   |
| 电气隔离       | B0505LS-1WR2、CA-IS3020S                    |
| 测量温度       | -270°C ~ + 1800°C                           |
| 模块工作温度   | 0 ~ 40°C                                    |
| 热电偶类型     | K 型                                        |
| 产品尺寸       | 54.0 x 54.0 x 13.2mm                        |
| 产品重量       | 37.2g                                       |
| 包装尺寸       | 95.0 x 65.0 x 25.0mm                        |
| 毛重           | 65.6g                                       |

## 原理图

- [Module13.2 Dual Kmeter 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/554/SCH_Module13.2_Dualkmeter_V1.0..pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/554/SCH_Module13.2_Dualkmeter_V1.0._sch_01.png">
</SchViewer>

## 管脚映射

### M5-Bus

::m5-bus-table
| PIN  | LEFT | RIGHT | PIN |
| ---- | ---- | ----- | --- |
| GND  | 1    | 2     |     |
| GND  | 3    | 4     |     |
| GND  | 5    | 6     |     |
|      | 7    | 8     |     |
|      | 9    | 10    |     |
|      | 11   | 12    | 3V3 |
|      | 13   | 14    |     |
|      | 15   | 16    |     |
| SDA  | 17   | 18    | SCL |
|      | 19   | 20    |     |
|      | 21   | 22    |     |
|      | 23   | 24    |     |
| HPWR | 25   | 26    |     |
| HPWR | 27   | 28    | 5V  |
| HPWR | 29   | 30    | BAT |
::

## 尺寸图

- [Module13.2 Dual Kmeter 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1028/M127-dualkmeter.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1028/M127-dualkmeter_page_01.png" width="100%">

## 数据手册

- [STM32F030F4P6](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/STM32F030F4P6.PDF)
- [B0505LS-1WR2](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/M127%20DualKmeter%20Module13.2/B0505LS-1WR2.pdf)
- [CA-IS3020S](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/M127%20DualKmeter%20Module13.2/CA-IS3020S.pdf)
- [HX6306P332](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/M127%20DualKmeter%20Module13.2/HX6306P332.pdf)
- [MAX31855KASA](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/M127%20DualKmeter%20Module13.2/MAX31855KASA.pdf)
- [MD5333](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/M127%20DualKmeter%20Module13.2/MD5333.pdf)
- [ME3116AM6G](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/M127%20DualKmeter%20Module13.2/ME3116AM6G.pdf)

## 软件开发

### Arduino

- [Module13.2 Dual Kmeter Arduino 驱动库](https://github.com/m5stack/M5Module-DualKmeter-13.2)

### UiFlow1

- [Module13.2 Dual Kmeter UiFlow1 文档](/zh_CN/uiflow/blockly/module/dual_kmeter)

### UiFlow2

- [Module13.2 Dual Kmeter UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/module/dualkmeter.html)

### 内置固件

- [Module13.2 Dual Kmeter 内置固件](https://github.com/m5stack/M5Module-DualKmeter-13.2-Internal-FW)

### 通信协议

- [Module13.2 Dual Kmeter I2C 通信协议](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1028/M127-Module-DualKmeter-I2C-Protocol.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1028/M127-Module-DualKmeter-I2C-Protocol_page_01.png" width="100%">

## 相关视频

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=115760978461953&bvid=BV16UBnB9EpE&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div>
        <iframe width="560" height="315" src="https://www.youtube.com/embed/GjXIT3ZcEsQ?si=u0j6gbvDPxW0Pc_K" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>