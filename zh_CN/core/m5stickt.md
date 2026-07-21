# StickT2

<span class="product-sku">SKU:K016-T2</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickt/m5stickt_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickt/m5stickt_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/671/K016-T2-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickt/m5stickt_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickt/m5stickt_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickt/m5stickt_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickt/m5stickt_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/671/K016-T2-weight.jpg">
</PictureViewer>

## 描述

**StickT2** 是一款精致小巧的红外热成像仪。它采用了最新的 FLIR Lepton 3.0 长波红外 （LWIR） 摄像头内核，有效分辨率为 160 x 120 ，成像画面清晰且稳定，是大面积非接触式红外测温的优质解决方案。其主控芯片选用了 ESP32 ，支持 Wi-Fi 连接，具备高达 240Mhz 的运算能力，有力地保障了图像输出，帧率 （FPS） 达到 7+ 。

屏幕规格为 1.14 寸，分辨率是 135 x 240 。此外，其内置的硬件资源也较为丰富，在交互操作方面配备了两个可编程按键和一个拨轮编码器。内部板载一个 6 轴 IMU （MPU6886）、麦克风 （SPM1423），电源管理芯片为 AXP192 ，并且内置了 300mAh 电池。
为了便于用户连接外设，在侧面设置了一个 4P HY2.0 接口。机身由黑色尼龙材质通过 3D 打印制成，而且在机身下方提供了一个 M3 螺丝孔和一个 1/4 螺丝孔用于固定。
在固件方面，提供了多达 5 种色彩显示模式，可指定测量最大最小值或中心值，并且显示温度色域范围是可调节的。

## 产品特性

- 基于 ESP32 开发
- 外壳： 3D 打印尼龙材质
- FLIR Lepton 3.0
- 内置 3 轴陀螺仪与 3 轴加速计
- 集成麦克风
- IPS LCD (1.14 寸)
- 带有拨轮编码器与可编程按键
- 内置电源管理芯片
- 内置锂电池供电
- 支持拓展的 GROVE/HY2.0 接口
- 开发平台
  - Arduino IDE
  - ESP-IDF
  - PlatformIO

## 包装内容

- 1 x StickT2
- 1 x USB Type-C 连接线 (20cm)

## 应用场景

- 车辆发动机故障检测
- 建筑除湿保温密封性检测
- 工业炉内壁耐火材料裂痕检测
- 夜晚户外观测动物

## 规格参数

| 主控资源    | 参数                                        |
| ----------- | ------------------------------------------- |
| SoC         | ESP32-PICO-D4@双核处理器，主频 240MHz       |
| Flash       | 4MB                                         |
| Wi-Fi       | 2.4 GHz Wi-Fi                               |
| DMIPS       | 600                                         |
| SRAM        | 520KB                                       |
| 输入电压    | 5V@500mA                                    |
| 主机接口    | USB Type-C x 1，HY2.0-4P (I2C+I/O+UART) x 1 |
| IPS 屏幕    | 1.14 inch，135x240 Colorful TFT LCD，ST7789 |
| 麦克风      | SPM1423                                     |
| 按键        | 自定义按键 x 2                              |
| 电源管理 IC | AXP192                                      |
| 天线        | 2.4G 3D 天线                                |
| MEMS        | MPU6886                                     |
| 电池容量    | 300mAh                                      |
| 编码器      | 拨轮编码器                                  |
| 热成像 IC   | Lepton 3.0                                  |
| 产品尺寸    | 48.0 x 24.0 x 24.0mm                        |
| 产品重量    | 28.6g                                       |
| 包装尺寸    | 73.0 x 45.0 x 28.0mm                        |
| 毛重        | 50.0g                                       |

**Lepton 3.0 参数**

| Parameter    | /                                                 |
| ------------ | ------------------------------------------------- |
| 有效像素     | 160 x 120                                         |
| 视野角度     | 56°                                               |
| 快速成像时间 | 500ms                                             |
| 有效帧率     | 8.7Hz                                             |
| 输入时钟     | 25MHz                                             |
| 像素尺寸     | 12μm                                              |
| 功耗         | 150 mW (典型工作)，650 mW (快门拍摄)，5 mW (待机) |
| 动态范围     | 低增益： -10 to 400°C; 高增益： -10 to 140°C      |
| 波长范围     | 8 to 14µm                                         |
| 热灵敏度     | 50 mK (0.050°C)                                   |
| 最佳温度范围 | -10°C to +80°C                                    |

## 操作说明

### 开关机操作

- 开机：按复位按键，持续至少 2 秒
- 关机：按复位按键，持续至少 6 秒

### IMU 三轴方向示意图

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/671/IMU-StickT2.jpg" width="70%">

### 使用介绍

按压复位按键进入开机画面，开机默认进入 RGB 显示模式，左侧为温度图像，右侧上方为电量显示，右侧下方为直方图和温度范围，温度范围随目标温度自动调整。默认靶心自动跟踪温度最大值，按压机身右侧按键 (B 键) 切换跟踪模式 (最小值 / 中心值 / 最大值)，按压机身正面按键 A 键切换图像显示模式 (GRAY / GOLDEN / RAINBOW / IRONBLACK / RGB)，拨轮编码器控制显示灵敏度 (调整显示温度色域范围)，长按复位键 6 秒关机。

## 管脚映射

### 按键 BUTTON A & 按键 BUTTON B

| ESP32-PICO-D4 | G37      | G39      |
| ------------- | -------- | -------- |
| 按键 BUTTON A | 按键管脚 |          |
| 按键 BUTTON B |          | 按键管脚 |

### 彩色 IPS 屏幕

驱动芯片：ST7789

分辨率：135 x 240

| ESP32-PICO-D4 | G15  | G13 | G23 | G18 | G5  |
| ------------- | ---- | --- | --- | --- | --- |
| IPS 屏幕      | MOSI | CLK | DC  | RST | CS  |

### 麦克风 MIC (SPM1423)

| ESP32-PICO-D4 | G0  | G34 |
| ------------- | --- | --- |
| 麦克风 MIC    | SCL | SDA |

### 六轴 IMU (MPU6886) & 电源管理芯片 (AXP192)

| ESP32-PICO-D4 | G22 | G21 |
| ------------- | --- | --- |
| MPU6886(0x68) | SCL | SDA |
| AXP192(0x34)  | SCL | SDA |

### 拨轮编码器

| ESP32-PICO-D4 | PA2 | PA3  | PA4  |
| ------------- | --- | ---- | ---- |
| 拨轮编码器    | SW  | EN_B | EN_A |

### 电源管理芯片 (AXP192)

| Microphone | RTC  | TFT backlight | TFT IC | ESP32/3.3V MPU6886 | 5V GROVE |
| ---------- | ---- | ------------- | ------ | ------------------ | -------- |
| LDOio0     | LDO1 | LDO2          | LDO3   | DC-DC1             | IPSOUT   |

### HY2.0-4P

::grove-table
| HY2.0-4P    | Black | Red | Yellow | White |
| ----------- | ----- | --- | ------ | ----- |
| PORT.CUSTOM | GND   | 5V  | G32    | G33   |
::

## 尺寸图

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/m5stickt/model%20size.jpg" width="80%">

## 结构文件

- [StickT2 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/K016-T2_StickT2/Structures)

## 数据手册

- [ESP32-PICO](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/669/esp32-pico_series_datasheet_cn.pdf)
- [MPU6886](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/MPU-6886-000193%2Bv1.1_GHIC_en.pdf)
- [AXP192 datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/AXP192_datasheet_en.pdf)
- [AXP192 register](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/AXP192_datasheet_cn.pdf)
- [SPM1423](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/SPM1423HM4H-B_datasheet_en.pdf)
- [Lepton datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/application/lepton-3-3.5-datasheet_en.pdf)
- [Lepton enigneering datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/application/flir-lepton-engineering-datasheet_en.pdf)
- [Lepton software interface description](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/application/flir-lepton-software-interface-description-document_en.pdf)

## 软件开发

### Arduino

- [StickT2 Arduino 驱动库](https://github.com/m5stack/M5-StickT)

\#> 板管理要求 | 编译该案例要求使用 M5Stack Arduino 板管理版本 v1.0.8，型号选择**M5Stick-C**。

### Easyloader

| Easyloader                  | 下载链接                                                                                                             | 备注 |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------- | ---- |
| StickT2 Firmware Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/CORE/EasyLoader_M5StickT_FactoryTest.exe) | /    |

## 相关视频

- 热成像操作说明：A 键切换跟踪模式，B 键切换显示模式，拨轮调整灵敏度。

<video id="example_video" controls>
  <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Core/StickT.mp4" type="video/mp4">
</video>

## 产品对比

如需对比 Stick 系列产品信息，可访问[产品选型表](/en/products_selector/m5stick_compare?select=K016-T2)，勾选目标产品即可获取对比结果。选型表涵盖核心参数、功能特性等关键信息，支持多产品同步比对。

## 版本变更

| 上市日期 | 产品变动                             |
| -------- | ------------------------------------ |
| 2021.5   | 优化内部结构，减小波轮体积，细节优化 |
| 2020.1   | 首次发售                             |
