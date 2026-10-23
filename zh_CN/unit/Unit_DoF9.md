# Unit DoF9

<span class="product-sku">SKU:U229</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1292/U229_Unit_DoF9_main_pictures_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1292/U229_Unit_DoF9_main_pictures_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1292/U229_Unit_DoF9_main_pictures_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1292/U229_Unit_DoF9_main_pictures_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1292/U229_Unit_DoF9_main_pictures_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1292/U229_Unit_DoF9_main_pictures_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1292/U229_Unit_DoF9_main_pictures_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1292/U229_Unit_DoF9_main_pictures_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1292/U229_Unit_DoF9_main_pictures_09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1292/U229_Unit_DoF9_main_pictures_10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1292/U229_Unit_DoF9_main_pictures_11.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1292/U229-weight.jpg">
</PictureViewer>

## 描述

**Unit DoF9** 是一款集成六轴惯性传感器和三轴地磁传感器的 9 轴姿态检测组合单元，搭载低功耗 BMI270 IMU 与 BMM350 三轴磁力计。BMI270 集成 16 位三轴加速度计与 16 位三轴陀螺仪，支持多量程配置与片上运动检测；BMM350 基于 TMR 隧道磁阻技术实现三轴磁场采集，磁场分辨率可达约 0.1 μT，温度稳定性优异。模块通过 I2C 总线传输数据，可实时输出加速度、角速度、温度、三轴磁场数据，适用于机器人姿态感知、航向检测、电子罗盘、运动追踪、导航辅助、云台控制等应用场景。

## 产品特性

- 集成六轴惯性与三轴地磁传感器
- 16 位加速度计与陀螺仪采样
- TMR 磁力计，0.1μT 高磁场分辨率
- 实时采集惯性、温度、磁场数据
- I2C 接口，支持 BMI270 地址切换

## 包装内容

- 1 x Unit DoF9
- 1 x HY2.0-4P Grove 连接线 (5cm)

## 应用场景

- 机器人姿态感知
- 航向检测
- 电子罗盘
- 运动追踪
- 导航辅助
- 云台控制

## 规格参数

| 规格            | 参数                                          |
| --------------- | --------------------------------------------- |
| 惯性传感器 IC   | BMI270                                        |
| 地磁传感器 IC   | BMM350                                        |
| 传感器类型      | 六轴惯性与三轴地磁传感器                      |
| 加速度计        | 16 位三轴加速度计                             |
| 加速度量程      | ±2 g / ±4 g / ±8 g / ±16 g                    |
| 加速度计精度    | ±20 mg（约 ±0.02 g）                          |
| 陀螺仪          | 16 位三轴陀螺仪                               |
| 陀螺仪量程      | ±125 / ±250 / ±500 / ±1000 / ±2000 °/s        |
| 陀螺仪精度      | ±0.5 °/s                                      |
| 磁力计          | BMM350 三轴磁力计                             |
| 磁场测量范围    | X/Y/Z 轴典型 ±2000 μT                         |
| 磁场分辨率      | 约 0.1 μT                                     |
| BMI270 通讯地址 | I2C @ 0x68 / 0x69（可通过板载开关切换）       |
| BMM350 通讯地址 | I2C @ 0x14                                    |
| 产品尺寸        | 24.0 x 24.0 x 8.0mm                           |
| 产品重量        | 3.1g                                          |
| 包装尺寸        | 138.0 x 93.0 x 7.0mm                          |
| 毛重            | 6.6g                                          |

## 操作说明

### I2C 地址切换

BMI270 I2C 地址可通过板载开关进行切换，拨至 `0` 时地址为 `0x68`；拨至 `1` 时地址为 `0x69`，用于避免 I2C 总线设备地址冲突。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1292/Unit_DoF9_witch_note.png" width="70%"/>

## 原理图

- [Unit DoF9 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1292/U229_Unit_DoF9_sche.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1292/U229_Unit_DoF9_sche_page_01.png">
</SchViewer>

## 管脚映射

### Unit DoF9

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 数据手册

- [BMI270 Datasheet](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1289/bst-bmi270-ds000.pdf)
- [BMM350 Datasheet](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1289/bst-bmm350-ds001.pdf)

## 尺寸图

- [Unit DoF9 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1289/Unit_DoF6DoF9DoF10_model_size.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1289/Unit_DoF6DoF9DoF10_model_size_page_01.png" width="100%">

## 结构文件

- [Unit DoF9 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/U229_Unit_DoF9/Structures)

## 软件开发

### Arduino

- [Unit DoF9 Arduino 快速上手](/zh_CN/arduino/projects/unit/unit_dof9)
- [Unit DoF9 Arduino 驱动库](https://github.com/m5stack/M5Unit-IMU)
- [M5Unified](https://github.com/m5stack/M5Unified)
- [M5UnitUnified](https://github.com/m5stack/M5UnitUnified)

### UiFlow2

- [Unit DoF9 UiFlow2 文档](https://uiflow-micropython.readthedocs.io/en/latest/unit/dof9.html)

## 相关视频

<VideoGallery>
  <VideoItem title="Unit DoF6 / Unit DoF9 / Unit DoF10 产品介绍以及功能展示" url="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1289/Unit_DoF_serials_video_CN.mp4" />
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
