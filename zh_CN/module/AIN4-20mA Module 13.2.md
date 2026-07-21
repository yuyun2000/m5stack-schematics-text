# Module13.2 AIN4-20mA

<span class="product-sku">SKU:M133</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/AIN4-20mA Module 13.2/img-ddec758e-78ce-43e8-9af7-bc101f3dc175.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/AIN4-20mA Module 13.2/img-1810f070-c8c1-4fa7-af46-93c7c1b1cb13.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/AIN4-20mA Module 13.2/img-52974c69-1bf3-4259-a3c9-2fe02e852288.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/AIN4-20mA Module 13.2/img-4da8623d-df1b-4fb3-b5f0-cd4be53b45ab.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/AIN4-20mA Module 13.2/img-90c581c8-5ac1-474f-a672-d3ddac1d68e5.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/AIN4-20mA Module 13.2/img-64a2704b-88f5-431d-a873-aaca26ddb340.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/AIN4-20mA Module 13.2/img-17a12d45-3c11-4b80-bf23-44c6b875e943.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/AIN4-20mA Module 13.2/img-ed7b99ca-70bf-4cf1-bf96-892c9ce4376b.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/AIN4-20mA Module 13.2/img-afd42edd-82ec-4a00-a496-26e014e62df8.webp">
</PictureViewer>

## 描述

**Module13.2 AIN4-20mA** 是一款**四通道**的**4 ~ 20 mA**电流型模拟量采集模块。它采用了**STM32G030F6**主控芯片以及专用的带隔离的采集芯片，与 M5 主机进行**I2C**通讯。支持通过跳线帽切换为由内部或外部供电的接线方式。板载电源隔离芯片和内置运放电路，准确地测量外部电流传感器以及确保信号的准确性和系统的安全性。供电方面**DC-JACK**接口以及相应的**DC-DC**升压电路，可为整个设备提供电源。**适用于电力系统设备监测、电机控制、能源管理和自动化和工业过程控制等领域**。

## 产品特性

- STM32G030F6® 32-bit Cortex®-M0+ CPU
- I2C 通讯
- 支持四路 2 或 4 线制传感器，跳线帽切换
- 内置电气隔离芯片
- 支持 Arduino、UiFlow 等编程平台

## 包装内容

- 1 x AIN4-20mA Moudle 13.2
- 12 x 跳线帽
- 5 x KF2EDGK-2.54-2P 接线端子

## 应用场景

- 电力系统设备监测
- 电机控制
- 能源管理
- 自动化和工业过程控制

## 规格参数

| 规格                      | 参数                 |
| ------------------------- | -------------------- |
| MCU                       | STM32G030F6P6        |
| 信号隔离芯片              | HCNR200              |
| 电源隔离芯片              | F2424S-2WR3          |
| 运放芯片                  | SGM321YC5/TR         |
| 通信接口                  | I2C 通信 @ 0x55      |
| IN+ 与 IN- 输入阻抗典型值 | 200Ω                 |
| 通道接口规格              | KF2EDGR-2.54-2P      |
| 工作温度                  | 0 ~ 40°C             |
| 外部 DC 电源电压          | DC 9 ~ 24V           |
| 产品尺寸                  | 54.0 x 54.0 x 13.0mm |
| 产品重量                  | 26.9g                |
| 包装尺寸                  | 95.0 x 65.0 x 25.0mm |
| 毛重                      | 51.7g                |

## 操作说明

### 跳线帽的接法与说明

- 使用**无源电流型传感器**时，请连接 DC 24V 供电输入，传感器信号接入 IN+, IN- ， 并将跳线帽调整为下图所示：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1029/module13.2_ain4_20ma_passive_sensor_connect_01.png" width="80%">

- 使用**有源电流型传感器**时，传感器信号接入 IN+, IN- ，并将跳线帽调整为下图所示：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1029/module13.2_ain4_20ma_active_sensor_connect_01.png" width="80%">

## 原理图

- [Module13.2 AIN4-20mA 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/560/SCH_Module13.2_AIN4-20mA_V1.0.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/560/SCH_Module13.2_AIN4-20mA_V1.0_sch_01.png">
</SchViewer>

## 管脚映射

### M5-Bus

::m5-bus-table
| PIN  | LEFT | RIGHT | PIN     |
| ---- | ---- | ----- | ------- |
| GND  | 1    | 2     |         |
| GND  | 3    | 4     |         |
| GND  | 5    | 6     |         |
|      | 7    | 8     |         |
|      | 9    | 10    |         |
|      | 11   | 12    |         |
|      | 13   | 14    |         |
|      | 15   | 16    |         |
| SDA  | 17   | 18    | SCL     |
|      | 19   | 20    |         |
|      | 21   | 22    |         |
|      | 23   | 24    |         |
| HPWR | 25   | 26    |         |
| HPWR | 27   | 28    | BUS_5V  |
| HPWR | 29   | 30    | BAT_OUT |
::

## 尺寸图

- [Module13.2 AIN4-20mA 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1029/M133-al4-20ma.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1029/M133-al4-20ma_page_01.png" width="100%">

## 数据手册

- [STM32G030F6 Datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/U162%20AIN4-20mA%20Unit/STM32G030F6%20datasheet.PDF)
- [HCNR200 Datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/U162%20AIN4-20mA%20Unit/HCNR200%20datasheet.PDF)
- [SGM321YC5 Datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/U162%20AIN4-20mA%20Unit/SGM321YC5%20datasheet.PDF)

## 软件开发

### Arduino

- [Module13.2 AIN4-20mA Arduino 驱动库](https://github.com/m5stack/M5Module-4-20mA)

### UiFlow1

- [Module13.2 AIN4-20mA UiFlow1 文档](/zh_CN/uiflow/blockly/module/ain4_20ma)

### UiFlow2

- [Module13.2 AIN4-20mA UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/module/ain4.html)

### 内置固件

- [Module13.2 AIN4-20mA 内置固件](https://github.com/m5stack/M5Module-4-20mA-Internal-FW)

### 通信协议

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/AIN4-20mA%20Module%2013.2/6a0fdabe9611151a23f31a522b0bdc1.png" width="100%" />

## 相关视频

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=114097802710754&bvid=BV1jx9iYgEi3&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/GCWOfwzQBWY?si=APKU8rzcM-6Dufc0" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
