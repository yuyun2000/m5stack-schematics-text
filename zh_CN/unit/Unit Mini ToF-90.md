# Unit Mini ToF-90°

<span class="product-sku">SKU:U196</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1143/U196_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1143/U196_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1143/U196_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1143/U196_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1143/U196_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1143/U196_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1143/U196_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1143/U196_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1143/U196_09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1143/U196_10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1143/U196-weight.jpg">
</PictureViewer>

## 描述

Unit Mini ToF-90° 是一款超紧凑型飞行时间（ToF）测距单元，集成 VL53L0X 激光测距模块，通过将激光发射模块旋转 90° 实现水平前向 25° 视场探测，可测量 3-200cm 范围内目标，测量精度 ±3%，激光波长 940 nm，响应时间 < 30 ms，适用标准 HY2.0-4P Grove 接口进行 I2C 通信。该产品适用于智能交通、机器人编程、安防监控、智慧家居等领域。

## 产品特性

- 测量距离可达 2 米
- 视场角: 25°
- 快速响应
- I2C 通讯
- 编程平台
  - Arduino
  - UiFlow1
  - UiFlow2

## 包装内容

- 1 x Unit Mini ToF-90°
- 1 x HY2.0-4P Grove 连接线 (5cm)

## 应用场景

- 智能交通
- 机器人编程
- 安防监控
- 智慧家居

## 规格参数

| 规格         | 参数                                                                                                    |
| ------------ | ------------------------------------------------------------------------------------------------------- |
| 传感器       | VL53L0X                                                                                                 |
| 测量范围     | 3-200cm                                                                                                 |
| 分辨率       | 1 mm                                                                                                    |
| 测量速度     | 23 ms／最短 8 ms                                                                                        |
| 视场角 (FoV) | 25°                                                                                                     |
| 光源类型     | 激光 (ToF)                                                                                              |
| 激光波长     | 940 nm VCSEL（Class 1 安全等级）                                                                        |
| 通信接口     | I2C 通信 @ 0x29                                                                                         |
| 工作温度范围 | 0 ~ 40°C                                                                                                |
| 功耗         | 待机模式：不包含 LED 灯： DC 5.03V@15.01uA；包含 LED 灯 DC 5.02V@1.92mA<br/> 工作模式：DC 5.02V@10.99mA |
| 产品尺寸     | 24.0 x 24.0 x 8.0mm                                                                                     |
| 产品重量     | 1.7g                                                                                                    |
| 包装尺寸     | 138.0 x 93.0 x 9.0mm                                                                                    |
| 毛重         | 3.5g                                                                                                    |

## 操作说明

\#> 测量距离 | 常规环境下，最大测试距离为 120cm；如果测试距离要到达 200cm，需要设置 Long Range 模式且需处于无红外线干扰的黑暗环境下。

## 原理图

[Unit Mini ToF-90° 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1143/U196_SCH.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1143/U196_SCH.png">
</SchViewer>

## 管脚映射

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 尺寸图

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1143/U196_size.png" width="100%">

## 数据手册

- [VL53L0X](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/hat/VL53L0X_en.pdf)

## 软件开发

### Arduino

- [Unit Mini ToF-90° Arduino 驱动库](https://github.com/m5stack/M5Unit-TOF)

- [Unit Mini ToF-90° Arduino 测试程序](https://github.com/m5stack/M5Stack/tree/master/examples/Unit/ToF_VL53L0X)

### UiFlow2

- [Unit Mini ToF-90° UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/tof90.html)

### UiFlow1

- [Unit Mini ToF-90° UiFlow1 文档](/zh_CN/uiflow/blockly/unit/tof)

## 相关视频

Unit Mini ToF-90° 产品介绍以及案例展示

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1143/U196-Unit_Mini_ToF-90_video.mp4" type="video/mp4"></video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=114690373980137&bvid=BV1TqMYz1ESd&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/GMU9khmNRnc?si=wyX1_PtsAQ-55k_O" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>

## 产品对比

::compare-table
| Product Compare          | [Unit Mini ToF-90°](/zh_CN/unit/Unit%20Mini%20ToF-90) ![Unit Mini ToF-90°](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1143/U196_11.webp) | [Unit-ToF4M](/zh_CN/unit/Unit-ToF4M) ![Unit-ToF4M](https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-ToF4M/img-bb6247a0-82d1-4060-8725-b230c2affcae.webp) | [Unit-TOF](/zh_CN/unit/TOF) ![Unit-TOF](https://static-cdn.m5stack.com/resource/docs/products/unit/TOF/img-b7d05799-9772-4e4b-a8ef-8398360f57f1.webp) |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| Adjustable Field of View | NO                                                                                                                                             | YES                                                                                                                                                                     | NO                                                                                                                                                    |
| Chip                     | VL53L0X                                                                                                                                        | VL53L1X                                                                                                                                                                 | VL53L0X                                                                                                                                               |
| Maximum Range            | 2 meters                                                                                                                                       | 4 meters                                                                                                                                                                | 2 meters                                                                                                                                              |
| Field of View (FoV)      | 25°                                                                                                                                            | 27° (adjustable)                                                                                                                                                        | 25°                                                                                                                                                   |
| 传感器安装角度           | 90°                                                                                                                                            | 0°                                                                                                                                                                      | 0°                                                                                                                                                    |
| Typical Accuracy         | ±3%                                                                                                                                            | ±1-2%                                                                                                                                                                   | ±3%                                                                                                                                                   |
::
