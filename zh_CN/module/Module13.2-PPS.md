# Module13.2 PPS

<span class="product-sku">SKU:M137</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Module13.2-PPS/img-20342b36-9573-4baa-8c91-0952802bc631.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Module13.2-PPS/img-654af383-0355-4cf9-a744-2990a360b274.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Module13.2-PPS/img-6ba55bbb-bc33-41bb-905b-9fb3bd185b54.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Module13.2-PPS/img-3ce0f002-8d9b-4e9f-8717-28e7916cc2f1.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Module13.2-PPS/img-28f619d3-70f9-40e6-ba93-1a3a7a191689.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Module13.2-PPS/img-d4567373-2d8f-4bf3-8a0b-c25db3350896.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Module13.2-PPS/img-6f6cf3f7-7134-4dae-88b6-53d3718b72b6.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Module13.2-PPS/img-e3678054-a49f-4699-8d5c-fcd458f63f01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Module13.2-PPS/img-0d76fd41-bf3e-427a-bbe6-b38533c18332.webp">
</PictureViewer>

## 描述

**Module13.2 PPS** 是一款可编程电源模块。该模块采用 STEP-DOWN 降压技术，支持 DC 9 ~ 36V 宽电压输入，内置 STM32 控制处理器及 AD8418 高分辨率电流放大器，通过高精度闭环控制，实现额定输出功率 100W（峰值 150W）的电流和电压输出，能输出 0.5 ~ 30V/0 ~ 5A，回读精度为正负 30mV/5mA。此外，模块上集成的隔离芯片 CA-IS3020S 和 B0505S-1WR3，为电路提供了电源及通信总线的电气隔离。输出接口采用标准 4MM 香蕉头插座，正负极间距 19mm。该模块出厂时均进行过全量程精度校准，用户需要另行采购直流电源适配器配套使用。该模块适合用于科研实验、工业自动化、嵌入式系统开发以及可调节性电源的 DIY 项目等领域。

## 教程 & 快速上手

learn>| ![Module13.2 PPS使用教程](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/991/PPS_10.jpg) | [Module13.2 PPS使用教程](/zh_CN/guide/iot_tools/module13.2_pps/usage) | 本教程将向你介绍使用 Core/Core2/Core3 系列主机，堆叠 Module13.2 PPS 进行额定电流和电压输出的操作方法。 |

## 注意事项

?> 注意 | 使用 Module13.2 PPS 需要外接 DC 9 ~ 36V 电源，否则会提示无 I2C 设备，设备不工作。输出的最大值取决于输入 DC 电源的输出能力。

\#> 电源检测 | 电源输入检测接口 (5-24V@5A):<br/>- USB PD 电源输入<br/>- Relay Base 电源输入

## 产品特性

- DC 9-36V 宽电压输入，输出 0.5V ~ 30V @ 0~5A
- 高精度额定输出功率 100W (峰值 150W)
- 具备电气隔离安全性能
- 标准 4mm 香蕉头插座，正负极间距 19mm
- 适用于 Core/Core2/CoreS3 系列主机

## 包装内容

- 1 x Module13.2 PPS

## 应用场景

- 科研实验
- 工业自动化
- 嵌入式系统开发
- 可调节性电源的 DIY 项目

## 规格参数

| 规格                   | 参数                      |
| ---------------------- | ------------------------- |
| MCU                    | STM32G030F6P6             |
| 通信接口               | I2C 通信 @ 0x35           |
| 电源及通信总线隔离芯片 | CA-IS3020S 和 B0505S-1WR3 |
| 电流放大器芯片         | AD8418                    |
| 输入电压               | DC 9-36V                  |
| 输出功率               | 100W (峰值 150W)          |
| 输出电流电压           | 0.5V ~ 30V @ 0~5A         |
| 精度                   | ±30mV@5mA                 |
| 待机电流               | Avg:DC 36V@12mA           |
| 工作电流               | Avg:DC 36V@32mA           |
| 香蕉头规格 (间距)      | 4MM (间距 19mm)           |
| 工作温度               | 0 ~ 40°C                  |
| 产品尺寸               | 54.0 x 54.0 x 19.7mm      |
| 产品重量               | 43.4g                     |
| 包装尺寸               | 132.0 x 95.0 x 21.0mm     |
| 毛重                   | 64.6g                     |

## 原理图

- [Module13.2 PPS 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/563/Sch_M5PPS_V1.3.pdf)
- [Module13.2 PPS ISO 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/563/Sch_M5PPS_ISO_V1.3.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/563/Sch_M5PPS_V1.3_sch_01.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/563/Sch_M5PPS_ISO_V1.3_sch_01.png">
</SchViewer>

## 管脚映射

### M5-Bus

::m5-bus-table
| PIN     | LEFT | RIGHT | PIN     |
| ------- | ---- | ----- | ------- |
| GND     | 1    | 2     |         |
| GND     | 3    | 4     |         |
| GND     | 5    | 6     |         |
|         | 7    | 8     |         |
|         | 9    | 10    |         |
|         | 11   | 12    | 3V3     |
|         | 13   | 14    |         |
|         | 15   | 16    |         |
| ISO_SDA | 17   | 18    | ISO_SCL |
|         | 19   | 20    |         |
|         | 21   | 22    |         |
|         | 23   | 24    |         |
|         | 25   | 26    |         |
|         | 27   | 28    | 5V      |
|         | 29   | 30    |         |
::

## 尺寸图

<img alt="module size" src="https://static-cdn.m5stack.com/resource/docs/products/module/Module13.2-PPS/img-44fd167e-cfab-4a22-8ad4-675ee9cbf907.jpg" width="100%" />

## 数据手册

- [AD8418BRMZ](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/M137%20Module13.2-PPS/AD8418BRMZ.PDF)
- [B0505S-1WR3](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/M137%20Module13.2-PPS/B0505S-1WR3.pdf)
- [CA-IS3020S](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/M137%20Module13.2-PPS/CA-IS3020S.pdf)

## 软件开发

### 快速上手

- [Module13.2 PPS 使用教程](/zh_CN/guide/iot_tools/module13.2_pps/usage)

### Arduino

- [Module13.2 PPS Arduino 驱动库](https://github.com/m5stack/M5Module-PPS)
- [Module13.2 PPS 出厂固件](https://github.com/m5stack/M5Module-PPS-UserDemo)

### UiFlow1

- [Module13.2 PPS UiFlow1 文档](/zh_CN/uiflow/blockly/module/pps)

### UiFlow2

- [Module13.2 PPS UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/module/pps.html)

### 内置固件

- [Module13.2 PPS 内置固件](https://github.com/m5stack/M5Module-PPS-Internal-FW)

### 通信协议

- [Module13.2 PPS I2C 通信协议](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/991/M137_ModulePPS.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/991/M137_ModulePPS_page_01.png" width="100%">

### Easyloader

!> 固件升级｜首批版本的 Module13.2 PPS 固件可能问题，需通过以下操作下载对应的固件升级程序，进行更新。

<img alt="image" width="30%" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/M137%20Module13.2-PPS/1.png"><img alt="image" width="30%" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/M137%20Module13.2-PPS/4.png">

| Easyloader                                                    | 下载链接                                                                                                                                | 备注 |
| ------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | ---- |
| Module13.2 PPS Firmware Upgrade v1 Easyloader with Core/Core2 | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/M137%20Module13.2-PPS/pps_upgrade_v1_esp32.exe)   | /    |
| Module13.2 PPS Firmware Upgrade v1 Easyloader with CoreS3     | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/M137%20Module13.2-PPS/pps_upgrade_v1_esp32s3.exe) | /    |

| Easyloader                                      | 下载链接                                                                                                | 备注 |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ---- |
| Module13.2 PPS User Demo Easyloader with Basic  | [download](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/991/Module13.2_PPS_For_CORE1_and_CORE2.exe) | /    |
| Module13.2 PPS User Demo Easyloader with CoreS3 | [download](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/991/Module13.2_PPS_For_CoreS3.exe)          | /    |

?> 校准数据 | 内置 STM32 的最后一个扇区存储了校准数据，请勿修改该扇区内容，否则可能导致模块无法正常使用。

## 相关视频

- Module13.2 PPS 产品介绍以及例子

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/M137%20Module13.2-PPS/PPS%20MODULE%2013.2%20%E8%A7%86%E9%A2%91.mp4" type="video/mp4"></video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
		<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113722613893100&bvid=BV1WECJYyEyN&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
      <iframe width="560" height="315" src="https://www.youtube.com/embed/xTTqXfDD-uM?si=K2hWDECufRGJmIp-" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
