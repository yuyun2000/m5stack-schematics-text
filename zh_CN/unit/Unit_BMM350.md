# Unit BMM350

<span class="product-sku">SKU:U231</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1293/U231_Unit_BMM350_main_pictures_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1293/U231_Unit_BMM350_main_pictures_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1293/U231_Unit_BMM350_main_pictures_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1293/U231_Unit_BMM350_main_pictures_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1293/U231_Unit_BMM350_main_pictures_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1293/U231_Unit_BMM350_main_pictures_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1293/U231_Unit_BMM350_main_pictures_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1293/U231_Unit_BMM350_main_pictures_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1293/U231_Unit_BMM350_main_pictures_09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1293/U231_Unit_BMM350_main_pictures_10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1293/U231_Unit_BMM350_main_pictures_11.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1293/U231-weight.jpg">
</PictureViewer>

## 描述

**Unit BMM350** 是一款三轴地磁传感器单元，搭载 BMM350 三轴磁力计，支持 100 kHz、400 kHz 通信速率。芯片基于 TMR 隧道磁阻技术，可实现 X/Y/Z 三轴磁场测量，磁场分辨率约 0.1 μT，温度稳定性优异。模块通过 I2C 总线传输数据，能够实时采集三轴地磁场数据，支持校准后航向角检测，适用于机器人导航、航向检测、电子罗盘、运动追踪、磁场感知等应用场景。

## 产品特性

- 搭载 BMM350 三轴 TMR 磁力计
- 测量轴：X / Y / Z
- 磁场分辨率：约 0.1 μT
- 磁场测量范围：典型 ±2000 μT
- 磁传感技术：TMR 隧道磁阻
- 通信速率：100 kHz / 400 kHz
- 支持航向角读取及校准

## 包装内容

- 1 x Unit BMM350
- 1 x HY2.0-4P Grove 连接线 (5cm)

## 应用场景

- 机器人导航
- 航向检测
- 电子罗盘
- 运动追踪
- 磁场感知

## 规格参数

| 规格         | 参数                   |
| ------------ | ---------------------- |
| IC 型号      | BMM350                 |
| 传感器类型   | 三轴地磁传感器         |
| 磁场测量范围 | X/Y/Z 轴典型 ±2000 μT  |
| 磁场分辨率   | 约 0.1 μT              |
| 通信接口     | I2C @ 0x14             |
| I2C 通信速率 | 100 kHz / 400 kHz      |
| 休眠功耗     | 实测 6.42 μA           |
| 连续读取功耗 | 实测 167.02 μA         |
| 航向角测试   | 校准后误差小于 10°     |
| 工作温度范围 | -40 ~ 85°C（芯片规格） |
| 产品尺寸     | 24.0 x 24.0 x 8.0mm    |
| 产品重量     | 3.1g                   |
| 包装尺寸     | 138.0 x 93.0 x 7.0mm   |
| 毛重         | 6.6g                   |

## 原理图

- [Unit BMM350 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1293/U231_Unit_BMM350_sche.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1293/U231_Unit_BMM350_sche_page_01.png">
</SchViewer>

## 管脚映射

### Unit BMM350

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 数据手册

- [BMM350 Datasheet](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1289/bst-bmm350-ds001.pdf)

## 尺寸图

- [BMM350 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1293/Unit_BMM350__model_size.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1293/Unit_BMM350__model_size_page_01.png" width="100%">

## 结构文件

- [Unit BMM350 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/U231_Unit_BMM350/Structures)

## 软件开发


### Arduino

- [Unit BMM350 Arduino 快速上手](/zh_CN/arduino/projects/unit/unit_bmm350)
- [Unit BMM350 Arduino 驱动库](https://github.com/m5stack/M5Unit-IMU)
- [M5Unified](https://github.com/m5stack/M5Unified)
- [M5UnitUnified](https://github.com/m5stack/M5UnitUnified)

### UiFlow2

- [Unit BMM350 UiFlow2 文档](https://uiflow-micropython.readthedocs.io/en/latest/unit/bmm350.html)

## 相关视频

<VideoGallery>
  <VideoItem title="Unit BMM350 产品介绍以及功能展示" url="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1293/U231_Unit_BMM350_video_CN.mp4" />
</VideoGallery>

## 产品对比

::compare-table
| 产品对比     | [Unit DoF6](/zh_CN/unit/Unit_DoF6) ![Unit DoF6](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1289/U228_Unit_DoF6_main_pictures_02.webp) | [Unit DoF9](/zh_CN/unit/Unit_DoF9) ![Unit DoF9](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1292/U229_Unit_DoF9_main_pictures_02.webp) | [Unit DoF10](/zh_CN/unit/Unit_DoF10) ![Unit DoF10](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1291/U230_Unit_DoF10_main_pictures_02.webp) | [Unit BMM350](/zh_CN/unit/Unit_BMM350) ![Unit BMM350](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1293/U231_Unit_BMM350_main_pictures_02.webp) |
| ------------ | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| 传感器组合   | BMI270                                                                                                                 | BMI270 + BMM350                                                                                                        | BMI270 + BMM350 + SPA06-003                                                                                               | BMM350                                                                                                                       |
| 传感器类型   | 六轴惯性传感器                                                                                                         | 六轴惯性 + 三轴地磁传感器                                                                                              | 六轴惯性 + 三轴地磁 + 气压传感器                                                                                          | 三轴地磁传感器                                                                                                               |
| 加速度计     | 16 位三轴                                                                                                              | 16 位三轴                                                                                                              | 16 位三轴                                                                                                                 | ❌                                                                                                                            |
| 陀螺仪       | 16 位三轴                                                                                                              | 16 位三轴                                                                                                              | 16 位三轴                                                                                                                 | ❌                                                                                                                            |
| 磁力计       | ❌                                                                                                                      | BMM350（TMR，约 0.1 μT）                                                                                               | BMM350（TMR，约 0.1 μT）                                                                                                  | BMM350（TMR，约 0.1 μT）                                                                                                     |
| 气压传感器   | ❌                                                                                                                      | ❌                                                                                                                      | SPA06-003                                                                                                                 | ❌                                                                                                                            |
| I2C 地址     | 0x68 / 0x69（板载开关切换）                                                                                            | BMI270：0x68 / 0x69（板载开关切换）<br>BMM350：0x14                                                                    | BMI270：0x68 / 0x69（板载开关切换）<br>BMM350：0x14<br>SPA06-003：0x76                                                    | 0x14                                                                                                                         |
| 主要功能     | 加速度、角速度、温度采集；片上运动检测                                                                                 | 加速度、角速度、温度、三轴磁场采集；片上运动检测                                                                       | 加速度、角速度、温度、三轴磁场、气压采集；片上运动检测                                                                    | 三轴磁场采集；校准后航向角输出                                                                                               |
::
