# Unit Mini IMU-Pro

<span class="product-sku">SKU:U171</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/IMU Pro Mini Unit/img-293fc203-f17e-48aa-86bd-0c45b4dd09e3.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/IMU Pro Mini Unit/img-9087b68a-bd52-4a8f-b92f-aae33ce585d5.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/IMU Pro Mini Unit/img-059f068b-ebc8-4c9a-9264-7095e60d063e.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/IMU Pro Mini Unit/img-98fe7ac4-6037-4e0d-a753-0967ba6ee4af.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/IMU Pro Mini Unit/img-38df2183-9162-48f9-81c4-10a08bd70e5a.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/IMU Pro Mini Unit/img-a6cd6214-06ee-4dc1-be7e-74fbc96f4886.webp">
</PictureViewer>

## 描述

**Unit Mini IMU-Pro**是一款多功能一体的 10 自由度的惯性运动单元，采用六轴姿态传感器 (BMI270) 、三轴地磁式传感器 (BMM150) 和大气压力传感器 (BMP280) 的方案，测量和检测物体的加速度和角速度 、地磁场方向和强度，以及大气压力。此单元通过 I2C 接口进行通讯，板载拨动开关，可切换 BMI270 的 I2C 地址。适用于导航 、自动化控制 、机器人技术 、飞行器导航 、气象检测和地理定位等领域。

## 产品特性

- 多功能传感器单元
- 高精度测量
- 采用 I2C 通讯接口
- 小型化设计
- 使用编程平台：UiFlow、Arduino 等

## 包装内容

- 1 x Unit Mini IMU-Pro
- 1 x HY2.0-4P Grove 连接线 (5cm)

## 应用场景

- 导航
- 自动化控制
- 机器人技术
- 飞行器导航
- 地理定位

## 规格参数

| 规格                      | 参数                                                                    |
| ------------------------- | ----------------------------------------------------------------------- |
| 六轴姿态传感器 (BMI270)   | 精度：0.05% (加速度)，0.05°/s (角速度) <br/> I2C 通信地址 @ 0x68 (默认) |
| 三轴地磁式传感器 (BMM150) | 精度：0.3 μT <br/> I2C 通信地址 @ 0x10                                  |
| 大气压力传感器 (BMP280)   | 精度：±1°C (温度)，±1 Pa (气压) <br/> I2C 通信地址 @ 0x76               |
| 产品尺寸                  | 24.0 x 24.0 x 8.0mm                                                     |
| 产品重量                  | 3.1g                                                                    |
| 包装尺寸                  | 138.0 x 93.0 x 9.0mm                                                    |
| 毛重                      | 6.6g                                                                    |

## 操作说明

?> BMM150 磁场干扰 | 带有磁铁的产品可能对 BMM150 磁场传感器造成干扰，导致读数异常。当搭配含有磁铁的 M5 主控设备时，需拆除磁铁，同时避免 BMM150 传感器放置在强磁场附近。

## 原理图

- [Unit Mini IMU-Pro 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/625/SCH_UNIT_IMU_ProV1.0.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/625/SCH_UNIT_IMU_ProV1.0_sch_01.png">
</SchViewer>

## 管脚映射

### Unit Mini IMU-Pro

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 尺寸图

<img alt="module size" src="https://static-cdn.m5stack.com/resource/docs/products/unit/IMU Pro Mini Unit/img-58117f7b-4cf6-4f29-871c-e327a368b436.jpg" width="100%" />

## 数据手册

- [BMI270](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/K128%20CoreS3/BMI270.PDF)
- [BMM150](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/K128%20CoreS3/BMM150.PDF)
- [BMP280](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/hat/BMP280-DS001-11_en.pdf)

## 软件开发

### Arduino

- [Unit Mini IMU-Pro Arduino 驱动库](https://github.com/m5stack/M5Unit-IMU-Pro-Mini)
- [Unit Mini IMU-Pro Get Raw Data](https://github.com/m5stack/M5Unit-IMU-Pro-Mini/tree/main/examples/getSensorData)
- [Unit Mini IMU-Pro Get XYZ Value AHRS Example](https://github.com/m5stack/M5Unit-IMU-Pro-Mini/tree/main/examples/AHRS)

### UiFlow1

- [Unit Mini IMU-Pro UiFlow1 文档](/zh_CN/uiflow/blockly/unit/imu_pro)

### UiFlow2

- [Unit Mini IMU-Pro UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/imupro.html)

## 相关视频

- Unit Mini IMU-Pro 应用案例

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/IMU%20Pro%20Mini%20Unit/U171%20IMU%20Pro%20%E8%A7%86%E9%A2%91.mp4" type="video/mp4"></video>
