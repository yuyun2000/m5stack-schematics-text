# Unit Mini BPS

<span class="product-sku">SKU:U090</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/bps/bps_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/bps/bps_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/bps/bps_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/bps/bps_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/bps/bps_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/bps/bps_06.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/bps/bps_07.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/bps/bps_08.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/bps/bps_09.webp">
</PictureViewer>

## 描述

**Unit Mini BPS** 是一款气压计单元，采用博世 BMP280 气压传感器，用于测量大气压强与高度估算。相对精度可达到 ±0.12 hPa，相当于 ±1 m 的高度差。同时温漂系数相当低，可以达到 1.5 Pa/K，即温度漂移为 12.6 cm/K。此外，在芯片内部还集成有温度传感器。

## 产品特性

- 气压传感器，片上带有温度传感器，可同时测量温度
- 精度达到 ±0.12hPa
- 温漂系数 1.5Pa/K
- 支持周期性测量
- 内部集成 5 段式滤波器
- 支持低功耗
- I2C 通讯：0x76
- 开发平台: Arduino，UiFlow (Blockly，Pyhton)
- 2 x LEGO 兼容孔

## 包装内容

- 1 x Unit Mini BPS
- 1 x HY2.0-4P Grove 连接线 (5cm)

## 应用场景

- 高度检测
- 气象站

## 规格参数

| 规格         | 参数                           |
| ------------ | ------------------------------ |
| 气压测量范围 | 300 ~ 1100hPa (+9000m ~ -500m) |
| 相对精度     | 0.12hPa                        |
| 绝对精度     | 1hPa                           |
| 温度测量范围 | -40 ~ +85°C                    |
| 温度分辨率   | 0.01°C                         |
| 气压分辨率   | 0.16Pa                         |
| 温度漂移     | 1.5Pa/K (12.6cm/K)             |
| 电流消耗     | 2.7μA@1Hz 采样率               |
| 通信接口     | I2C 通信 @0x76                 |
| 产品尺寸     | 24.0 x 24.0 x 13.0mm           |
| 产品重量     | 4.0g                           |
| 包装尺寸     | 35.0 x 36.0 x 18.0mm           |
| 毛重         | 9.0g                           |

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/bps/bps_sch_01.webp" width="70%">

## 管脚映射

### Unit Mini BPS

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 数据手册

- [BMP280 Datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/hat/BMP280-DS001-11_en.pdf)

## 软件开发

### Arduino

- [Unit Mini BPS with M5Atom](https://github.com/m5stack/M5Unit-ENV/blob/master/examples/Unit_BPS_M5Atom/Unit_BPS_M5Atom.ino)
- [Unit Mini BPS with M5AtomS3](https://github.com/m5stack/M5Unit-ENV/blob/master/examples/Unit_BPS_M5AtomS3/Unit_BPS_M5AtomS3.ino)
- [Unit Mini BPS with M5AtomS3Lite](https://github.com/m5stack/M5Unit-ENV/blob/master/examples/Unit_BPS_M5AtomS3Lite/Unit_BPS_M5AtomS3Lite.ino)
- [Unit Mini BPS with M5Core](https://github.com/m5stack/M5Unit-ENV/blob/master/examples/Unit_BPS_M5Core/Unit_BPS_M5Core.ino)
- [Unit Mini BPS with M5Core2](https://github.com/m5stack/M5Unit-ENV/blob/master/examples/Unit_BPS_M5Core2/Unit_BPS_M5Core2.ino)
- [Unit Mini BPS with M5StickC](https://github.com/m5stack/M5Unit-ENV/blob/master/examples/Unit_BPS_M5StickC/Unit_BPS_M5StickC.ino)
- [Unit Mini BPS with M5StickCPlus](https://github.com/m5stack/M5Unit-ENV/blob/master/examples/Unit_BPS_M5StickCPlus/Unit_BPS_M5StickCPlus.ino)

### UiFlow1

- [Unit Mini BPS UiFlow1 文档](/zh_CN/uiflow/blockly/unit/bps)

### UiFlow2

- [Unit Mini BPS UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/bps.html)

### EasyLoader

| Easyloader                        | 下载链接                                                                                                                          | 备注 |
| --------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | ---- |
| Unit Mini BPS example with M5Core | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/UNIT/For%20M5Core/EasyLoader_BPS_Unit_With_M5Core.exe) | /    |

### 相关视频

<video class="video-container" controls>
  <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Unit/BPS.mp4">
</video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113185944243017&bvid=BV13gsSe2EUZ&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/jyh07uxdIRI?si=lI9SNwmglk9qKsiW" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
