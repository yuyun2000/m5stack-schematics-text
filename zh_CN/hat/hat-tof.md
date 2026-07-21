# Hat ToF

<span class="product-sku">SKU:U072</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-tof/hat-tof_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-tof/hat-tof_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-tof/hat-tof_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/854/U072_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-tof/hat-tof_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/854/U072-weight.jpg">
</PictureViewer>

## 描述

**Hat ToF** 是一款专为 SticKC 设计的高精度激光测距传感器，内部集成 ST 激光测距芯片 **VL53L0X**、**940nm VCSEL** 发射器，通过测量激光信号到被测物体的往返时间，能够在不到 30ms 的时间内测量 2m 范围内的绝对距离。与传统测距不同的地方在于，无论检测目标的反射率如何，它都能提供精确的距离测量数据。在一些对数据精度有一定要求的距离测量、障碍物识别项目中，**Hat ToF** 能够有不错的表现。

## 产品特性

- 高精度
- 最大测量距离 2m
- 测量精度 ±3%
- 940nm 激光 VCSEL
- 安全方面:
  - 符合最新标准的 1 级激光设备
  - 标准 IEC 60825-1:2014 - 第 3 版
- 通信协议：I2C 地址为 **0x29**(G0/G26)
- 开发平台
  - UiFlow1
  - UiFlow2
  - Arduino IDE

## 包装内容

- 1 x Hat ToF
- 1 x Sticker

## 应用场景

- 障碍物识别
- 手势识别
- 激光测距
- 3D 结构光成像（3D 感应）
- 摄像机辅助（超快速自动对焦和景深图）

## 规格参数

| 规格     | 参数                  |
| -------- | --------------------- |
| 通信接口 | I2C 通信 @ 0x29       |
| 测量距离 | 0.3 ~ 2m              |
| 测量精度 | ±3%                   |
| 产品尺寸 | 24.0 x 20.0 x 13.7mm  |
| 产品重量 | 4.0g                  |
| 包装尺寸 | 138.0 x 93.0 x 15.0mm |
| 毛重     | 6.2g                  |

## 操作说明

\#> 测量环境 | 常规环境下，最大测试距离为 120cm；如果测试距离要到达 200cm， 需要设置 Long Range 模式且需处于无红外线干扰的黑暗环境下。

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-tof/hat-tof_sch_01.webp" width="50%">

## 管脚映射

| StickC  | G0  | G26 | 3.3V | GND |
| ------- | --- | --- | ---- | --- |
| ToF HAT | SDA | SCL | 3.3V | GND |

## 尺寸图

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/854/U072_model_size_page_01.png" width="50%" height="50%">

## 数据手册

- [VL53L0X Datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/hat/VL53L0X_en.pdf)

## 软件开发

### Arduino

- [Hat ToF 测试程序](https://github.com/m5stack/M5StickC/tree/master/examples/Hat/TOF)

### UiFlow1

- [Hat ToF UiFlow1 文档](/zh_CN/uiflow/blockly/hat/tof)

### UiFlow2

- [Hat ToF UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/hats/tof.html)

### Easyloader

| Easyloader         | 下载链接                                                                                           | 备注 |
| ------------------ | -------------------------------------------------------------------------------------------------- | ---- |
| Hat ToF Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/HAT/ToF/EasyLoader_ToF_HAT.exe) | /    |

## 相关视频

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/HAT/ToF_HAT.mp4" type="video/mp4">
</video>
