# Unit ToF

<span class="product-sku">SKU:U010</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/TOF/img-1389686c-b643-4b4f-a74b-4dc070a32103.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/TOF/img-b7d05799-9772-4e4b-a8ef-8398360f57f1.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/699/U010_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/TOF/img-17380a9a-eded-4cb1-8696-9cacb917b89a.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/TOF/img-6cdbc534-a578-4c37-bd1b-fde80b1b62e8.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/TOF/img-f6efea74-b1c5-495b-8c46-75d78268ca90.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/699/U010-weight.jpg">
</PictureViewer>

## 描述

**Unit ToF** 是一款高精度激光测距单元。它内置 VL53L0X 激光测距传感器，采用 Time-of-Flight (ToF) 技术，通过测量激光往返时间精确计算距离，且不受目标反射率影响。该单元通过 I2C 接口通信 (0x29)，集成了 940nm VCSEL 激光发射器和 SPAD 阵列接收器，支持 3cm ~ 200cm 的测距范围，响应时间小于 30ms，并采用 LEGO 兼容孔设计，可灵活对接 LEGO 结构或进行螺丝固定。适用于机器人避障、智能家居控制、自动对焦等多种需要进行距离测量的应用场景。

## 产品特性

- 测量范围：3cm ~ 200cm
- 测量精度：±3%
- 分辨率：1mm
- 响应时间：< 30ms
- 激光波长: 940nm
- 2 x LEGO 兼容孔
- 开发平台
  - UiFlow1
  - UiFlow2
  - Arduino IDE

## 包装内容

- 1 x Unit ToF
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 激光测距
- 3D 结构光成像 (3D 感应)
- 摄像机辅助 (超快速自动对焦和景深图)

## 规格参数

| 规格     | 参数                 |
| -------- | -------------------- |
| 传感器   | VL53L0X              |
| 通信接口 | I2C 通信 @ 0x29      |
| 测量距离 | 3cm ~ 200cm          |
| 测量精度 | ±3%                  |
| 产品尺寸 | 32.0 x 24.0 x 8.0mm  |
| 产品重量 | 4.1g                 |
| 包装尺寸 | 138.0 x 93.0 x 9.0mm |
| 毛重     | 9.4g                 |

## 操作说明

\#> 测量距离 | 常规环境下，最大测试距离为 120cm；如果测试距离要到达 200cm， 需要设置 Long Range 模式且需处于无红外线干扰的黑暗环境下。

## 原理图

<img alt="schematics" src="https://static-cdn.m5stack.com/resource/docs/products/unit/TOF/img-5d9d3c7d-dd82-47e9-8917-f8d6733fcfb5.webp" width="100%" />

## 管脚映射

### Unit ToF

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 尺寸图

<img alt="module size" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/TOF/%E5%B0%BA%E5%AF%B8%E5%9B%BE.jpg" width="100%" />

## 结构文件

- [Unit ToF 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/U010_Unit_ToF/Structures)

## 数据手册

- [VL53L0X Datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/hat/VL53L0X_en.pdf)

## 软件开发

### Arduino

- [Unit ToF 测试程序](https://github.com/m5stack/M5Stack/tree/master/examples/Unit/ToF_VL53L0X)

### UiFlow1

- [Unit ToF UiFlow1 文档](/zh_CN/uiflow/blockly/unit/tof)

### UiFlow2

- [Unit ToF UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/tof.html)

### Home Assistant

- [Home Assistant 集成](/zh_CN/homeassistant/sensor/unit_tof)

### EasyLoader

| Easyloader                       | 下载链接                                                                                                                     | 备注 |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---- |
| Unit ToF Test Example Easyloader | [download](https://static-cdn.m5stack.com/resource/docs/products/unit/TOF/ezLoader-68a06700-8b57-4eeb-a98b-ad26830d568f.exe) | /    |

## 相关视频

- Unit TOF 示例

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Unit/ToF_UNIT.mp4" type="video/mp4" type="video/mp4"></video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=112868267788683&bvid=BV15TvPeEELQ&p=1autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/9JLDu_g6vfQ?si=46EVcApIsFOojU1t" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>

## 产品对比

::compare-table
| Product Compare          | [Unit-ToF4M](/zh_CN/unit/Unit-ToF4M) ![Unit-ToF4M](https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-ToF4M/img-bb6247a0-82d1-4060-8725-b230c2affcae.webp) | [Unit-TOF](/zh_CN/unit/TOF) ![Unit-TOF](https://static-cdn.m5stack.com/resource/docs/products/unit/TOF/img-b7d05799-9772-4e4b-a8ef-8398360f57f1.webp) |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| Chip                     | VL53L1X                                                                                                                                                                 | VL53L0X                                                                                                                                               |
| Maximum Range            | 4 meters                                                                                                                                                                | 2 meters                                                                                                                                              |
| Typical Accuracy         | ±1-2%                                                                                                                                                                   | ±3%                                                                                                                                                   |
| Field of View (FoV)      | 27° (adjustable)                                                                                                                                                        | 25°                                                                                                                                                   |
| Adjustable Field of View | YES                                                                                                                                                                     | NO                                                                                                                                                    |
::
