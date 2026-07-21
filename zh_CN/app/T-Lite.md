# T-Lite

<span class="product-sku">SKU:K126</span>

<PictureViewer>
<img class="pic" src="https://static-cdn.m5stack.com/resource/docs/products/app/T-Lite/img-98729c1e-2056-4811-8c15-630bbff145b2.webp">
<img class="pic" src="https://static-cdn.m5stack.com/resource/docs/products/app/T-Lite/img-a193a656-0e96-40cb-b2de-2ac6e4fc906e.webp">
<img class="pic" src="https://static-cdn.m5stack.com/resource/docs/products/app/T-Lite/img-9ee2eff3-ea80-4da2-8163-fc09a527b355.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/T-Lite/img-f595f547-73bd-4fb0-9df9-a7ccc189c6f4.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/T-Lite/img-5fe96b98-c086-47ec-adbf-9c6145fc2f4f.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/T-Lite/img-4c08bc92-c3d8-44e0-829a-73346dff054c.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/T-Lite/img-667f2b2c-56bc-4ea7-8907-023b7648aac8.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/T-Lite/img-13090835-e199-4141-9e36-441287837c44.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/T-Lite/img-4bbead1b-63d4-42bc-9c00-9d5ffda3c394.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1068/K126-weight.jpg">
</PictureViewer>

## 描述

`T-Lite`是一款具有在线检测功能的一体化`热成像`采集测温装置，该产品主要由`M5StickC-Plus`与 `HAT THERMAL`结合而成，采用`MLX90640-BAA`红外成像传感器，主控采用`ESP32-PICO-D4`芯片，具备`WiFi`功能，`135 x 240`分辨率的`TFT`屏幕，内置`160mAh电池`，其 "T-Lite“名称的 T 代表 Temperature 温度，Lite 代表小的、高集成的意思。用户可设置`高温预警功能`，可以通过`云端`和`局域网`实时查看温度图像和数据。M5 同时提供线上数据 API 接口，能通过`EZData`获取远端图像和对应数据，为工程项目应用提供便利。

## 产品特性

- 基于 ESP32-PICO 开发，支持 WiFi
- 用户按键，LCD (1.14 寸), 电源 / 复位按键
- 160 mAh 锂电池
- 集成无源蜂鸣器
- 视场角: 110°×75°
- 测温范围: -40°C ~ 300°C

## 包装内容

- 1 × T-Lite
- 1 × StickC-Plus
- 1 × 挂线
- 1 × USB Type-C 连接线 (50cm)
- 1 × 用户使用手册

## 应用场景

- 温度检测预警
- 电路温度异常监测
- 高精度非接触性测温器
- 生物移动监测
- 可视化红外成像

## 规格参数

| 规格       | 参数                                               |
| ---------- | -------------------------------------------------- |
| MCU        | ESP32-PICO,240MHz dual core, 600 DMIPS, 520KB SRAM |
| 传感器     | MLX90640                                           |
| 视场角     | 110°×75°                                           |
| 分辨率     | 32×24                                              |
| Flash 闪存 | 4MB Flash                                          |
| 输入电压   | 5V @ 500mA                                         |
| 接口       | Type-C                                             |
| LCD 屏幕   | 1.14 inch, 135 x 240 Colorful TFT LCD, ST7789v2    |
| 麦克风     | SPM1423                                            |
| 蜂鸣器     | 无源蜂鸣器                                         |
| PMU        | AXP192                                             |
| 电池       | 160 mAh @ 3.7V                                     |
| 产品尺寸   | 69.0 x 26.6 x 16.4mm                               |
| 产品重量   | 31.0g                                              |
| 包装尺寸   | 110.0 x 87.0 x 25.0mm                              |
| 毛重       | 62.9g                                              |

## 操作说明

### 电子说明手册

<img alt="module size" src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1068/K126_Tlite_tutorial_cn.jpg" width="100%" />

## 尺寸图

<img alt="module size" src="https://static-cdn.m5stack.com/resource/docs/products/app/T-Lite/img-1b2d5722-f7d5-4071-ad56-95ac848ee049.png" width="100%" />

## 数据手册

- [MLX90640](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1068/MLX90640-Datasheet-Melexis.pdf)

## 软件开发

### 快速上手

- [T-Lite使用指导](/zh_CN/guide/iot_tools/t_lite/usage)

### PlatformIO

[T-Lite Firmware](https://github.com/m5stack/M5StickC-Plus-TLite-FW)

### EasyLoader

| Easyloader                 | 下载链接                                                                                                     | 备注 |
| -------------------------- | ------------------------------------------------------------------------------------------------------------ | ---- |
| T-Lite Firmware Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Application/T-Lite/T-Lite%20Firmware.exe) | /    |

### 发射率（Emissivity）修改说明

> 发射率（Emissivity）| 红外传感器默认以理想黑体（ε=1.0）为基准，但大多数材料会反射环境辐射，导致测温偏差。
通过设置正确的发射率 ε（反射率 ρ = 1–ε），可补偿反射影响，提高测温精度。T-Lite 的默认发射率为 0.98。

常见材料的发射率如下所示：

| 材料           | 发射率 ε |
| -------------- | -------- |
| 人体皮肤       | 0.98     |
| 水             | 0.93     |
| 塑料（不透明） | 0.95     |
| 沥青           | 0.95     |
| 混凝土         | 0.95     |
| 砖             | 0.90     |
| 玻璃（平板）   | 0.85     |
| 木材（自然）   | 0.94     |
| 铝（氧化）     | 0.30     |
| 钢（氧化）     | 0.80     |

- 更多材料的发射率 / 反射率数据，请参见[物体发射率参考表 (PDF)](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1068/K126_Ultimate-Emissivity-Table.pdf)。
- 关于设置 T-Lite 发射率的方法，可参见[T-Lite使用教程](/zh_CN/guide/iot_tools/t_lite/usage)。

## 相关视频

- 产品教学

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/T-Lite/T-Lite(en).mp4" type="video/mp4"></video>
