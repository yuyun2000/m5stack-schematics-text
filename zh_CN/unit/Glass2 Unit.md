# Unit Glass2

<span class="product-sku">SKU:U158-B</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Glass2 Unit/img-d882d0b7-dce0-4202-9b76-b9f25e7ad829.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Glass2 Unit/img-8ed5b80e-0ebe-4fd1-988a-749ecb959759.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Glass2 Unit/img-51aa514b-6e78-4a4e-a7e7-64b54daf8c71.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Glass2 Unit/img-fc55857f-9551-4c3a-ad49-d21155adb434.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Glass2 Unit/img-e76a0426-d74e-4615-b6d4-c13ad180b5d1.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Glass2 Unit/img-b6e6f375-a35d-47d4-8a7d-6f759dd95bff.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Glass2 Unit/img-483765b0-330b-4a4b-a384-ca3f2c10e96d.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Glass2 Unit/img-b54af17c-414a-41d1-92ea-cbf59d9f9955.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Glass2 Unit/img-66b4380b-f0dd-4f5f-a8d3-87952228597c.webp">
</PictureViewer>

## 描述

**Unit Glass2** 是一款 **1.51 英寸** 的 **透明 OLED** 拓展屏幕单元，采用 **SSD1309** 驱动方案，支持 I2C 通信接口（默认地址为 0x3C，可通过预留焊盘更改为 0x3D）。该屏幕具有卓越的亮度和对比度，在各种光照条件下都有出色的表现。它适用于信息显示、状态指示器或用户界面，可嵌入到各种家居产品或控制设备中，实现与用户的交互。

## 产品特性

- 128×64 总像素
- 显示区域 35.05×18mm
- 玻璃面积 42.04×27.22mm
- 1 位颜色深度
- I2C 通信（默认地址 0x3C，可更改为 0x3D）
- 支持编程平台：Arduino、UiFlow

## 包装内容

- 1 x Unit Glass2
- 1 x HY2.0-4P Grove 连接线（20cm）

## 应用场景

- 家居产品
- 控制设备
- 显示面板

## 规格参数

| 规格     | 参数                                        |
| -------- | ------------------------------------------- |
| 屏幕     | 1.51 英寸透明 OLED 屏幕                     |
| 分辨率   | 128 x 64                                    |
| 显示颜色 | 蓝色                                        |
| 显示区域 | 35.05 x 18mm                                |
| 面板尺寸 | 42.04 x 27.22 x 1.25mm                      |
| 视角方向 | 全视角                                      |
| 工作温度 | 0 ~ 40°C                                    |
| 逻辑电压 | 3.3V                                        |
| 通信接口 | 默认 I2C 通信 @ 0x3C，可通过焊盘切换为 0x3D |
| 产品尺寸 | 53.0 x 42.0 x 6.0mm                         |
| 产品重量 | 8.5g                                        |
| 包装尺寸 | 138.0 x 93.0 x 7.0mm                        |
| 毛重     | 14.3g                                       |

## 操作说明

左右两个 HY2.0-4P Grove 接口是连通的，可互换使用，用于连接其他 I2C 设备。默认 I2C 地址为 `0x3C`，可通过预留焊盘修改为 `0x3D`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/757/Unit_Glass_2_I2C.png" width="70%">

如上图所示，用六角扳手取下两颗螺丝，向上取下盖板，推开屏幕排线，露出圆圈里的两个半圆形焊盘。在圆圈内点锡使两个焊盘导通，即可将 I2C 地址修改为 `0x3D`；移除点锡即可恢复为 `0x3C`。

I2C 地址若修改为 `0x3D`，可能也需要在程序中修改相关配置。

## 原理图

- [Unit Glass2 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/613/SCH_UNIT_GLASS2.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/613/SCH_UNIT_GLASS2_sch_01.png">
</SchViewer>

## 管脚映射

### Unit Glass2

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 尺寸图

- [Unit Glass2 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/757/U158BUnitGlass2-model-size.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/757/U158BUnitGlass2-model-size_page_01.png" width="100%">

## 数据手册

- [SSD1309](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/U158%20unit%20glass/SSD1309.pdf)
- [128\*64 Transparent OLED](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/U158%20unit%20glass/ZJY-2856KLBAG01.pdf)

## 软件开发

### Arduino

- [Unit Glass2 Arduino 教程](/zh_CN/arduino/projects/unit/unit_glass2)

### UiFlow1

- [Unit Glass2 UiFlow1 文档](/zh_CN/uiflow/blockly/unit/glass2)

### UiFlow2

- [Unit Glass2 UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/glass2.html)

## 相关视频

- Unit Glass2 显示案例

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Glass2%20Unit/GLASS2%20UNIT%20%E8%A7%86%E9%A2%91.mp4" type="video/mp4"></video>

## 产品对比

::compare-table
| Product Compare | [Unit Glass2](/zh_CN/unit/Glass2%20Unit) ![Unit Glass2](https://static-cdn.m5stack.com/resource/docs/products/unit/Glass2%20Unit/img-b54af17c-414a-41d1-92ea-cbf59d9f9955.webp) | [Unit Glass](/zh_CN/unit/Glass%20Unit) ![Unit Glass](https://static-cdn.m5stack.com/resource/docs/products/unit/Glass%20Unit/img-467f2a5f-e95c-4e39-b99a-baf0f1505c72.webp) |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 芯片方案        | STM32 + SSD1309                                                                                                                                                                 | SSD1309                                                                                                                                                                     |
| 硬件接口        | 2 个 HY2.0-4P Grove 接口，无按钮、蜂鸣器                                                                                                                                        | 1 个 HY2.0-4P Grove 接口、2 个按钮、1 个蜂鸣器                                                                                                                              |
| I2C 地址        | 固定 0x3D                                                                                                                                                                       | 0x3C / 0x3D（通过焊盘修改）                                                                                                                                                 |
::
