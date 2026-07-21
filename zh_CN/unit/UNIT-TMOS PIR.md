# Unit TMOS PIR

<span class="product-sku">SKU:U185</span>

<PictureViewer>
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/UNIT-TMOS%20PIR/4.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/UNIT-TMOS%20PIR/6.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/UNIT-TMOS%20PIR/10.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/UNIT-TMOS%20PIR/5.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/UNIT-TMOS%20PIR/7.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/UNIT-TMOS%20PIR/8.webp">
</PictureViewer>

## 描述

**Unit TMOS PIR** 是一种用于在场和运动检测的高灵敏度红外传感器单元，采用 STHS34PF80 芯片方案。它通过 I2C 通讯方式（默认地址：0x5A）与 M5 设备进行通讯。工作原理基于普朗克定律描述的黑体辐射原理，不仅能监测环境温度，还可检测人体存在和运动。该传感器能区分静止与移动的物体，拥有 80 度的视场角，提供了广阔的检测范围。另外，它支持可调节的采样频率和增益模式，以满足不同应用场景的需求。适用于警报系统、智能照明和占用检测等多种应用场景。

\#> 注意事项 | 1. 设置 TMOS 的增益模式: <br/>默认增益模式：灵敏度高，但容易导致传感器过饱和。过饱和会导致运动 / 存在检测的标志位更新迟滞；<br/>宽模式：检测距离短，但可以避免传感器饱和。<br/>2. 温度差异的敏感性：TMOS 传感器的输出信号对传感器自身的环境温度和测量所在房间的环境温度之间的温度差异 (温度差) 非常敏感。这种温度差可能会影响传感器测量。<br/>3. 掉电模式设置：当设备处于掉电模式时，每次启动或重启设备时，该寄存器都会恢复到默认值。需要重新设定标定温度。因此，如果应用需要覆盖广泛的操作温度范围以及房间温度和传感器热耦合环境温度之间的温差，用户在设备启动时需要设置宽模式。

## 产品特性

- 高灵敏度红外检测
- 宽视场角
- 在场和运动检测
- I2C 通讯 (0x5A)
- 可编程输出数据速率

## 包装内容

- 1 x Unit TMOS PIR
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 存在和接近感应
- 报警 / 安全系统
- 家具自动化
- 智能照明
- 物联网
- 智能储物柜

## 规格参数

| 规格               | 参数                     |
| ------------------ | ------------------------ |
| 传感器             | STHS34PF80               |
| 通信接口           | I2C 通信 @ 0x5A          |
| 测量距离           | 2 米以上                 |
| 识别最小尺寸       | 70 x 25 cm²              |
| 视场角             | 80°                      |
| 可编程输出数据速率 | 0.25 Hz 至 30 Hz         |
| 红外光波长         | 5 到 20µm 范围内的红外光 |
| 红外灵敏度         | 2000 LSB/°C              |
| 传感器精度         | ±0.3°C                   |
| 增益模式           | 默认增益模式，宽模式     |
| 产品尺寸           | 32.0 x 24.0 x 5.2mm      |
| 产品重量           | 4.5g                     |
| 包装尺寸           | 138.0 x 93.0 x 6.2mm     |
| 毛重               | 10.0g                    |

## 原理图

<img alt="schematics" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/UNIT-TMOS%20PIR/img-296f83d1-ddc1-473e-9542-c157eb6c5b95.png" width="100%" />

## 管脚映射

### Unit TMOS PIR

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 尺寸图

<img alt="module size" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/UNIT-TMOS%20PIR/%E5%B0%BA%E5%AF%B8%E5%9B%BE.png" width="100%" />

## 数据手册

- [STHS34PF80_Datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/UNIT-TMOS%20PIR/STHS34PF80_Datasheet.pdf)
- [STHS34PF80_Application_note](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/UNIT-TMOS%20PIR/STHS34PF80_Application_note.pdf)
- [STHS34PF80_Hardware_Application_note](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/UNIT-TMOS%20PIR/STHS34PF80_Hardware_Application_note.pdf)

## 软件开发

### Arduino

- [Unit TMOS PIR Arduino 驱动库](https://github.com/m5stack/M5-STHS34PF80)

### UiFlow2

- [Unit TMOS PIR UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/tmos.html)

### Home Assistant

- [Home Assistant 集成](/zh_CN/homeassistant/sensor/unit_tmos_pir)

## 视频

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/UNIT-TMOS%20PIR/U185%20TMOS%20PIR%20UNIT%20%E8%A7%86%E9%A2%91.mp4" type="video/mp4"></video>

- UiFlow2 Unit TMOS PIR

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=114215075448105&bvid=BV1YYoCYbEPC&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/fDVw3zn7pa8?si=fYgYriIXNsme_u4l" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>

## 产品对比

| 产品                 | 芯片方案   | 测量范围               | FOV               | 通讯方式   | 功能特点               |
| -------------------- | ---------- | ---------------------- | ----------------- | ---------- | ---------------------- |
| TMOS PIR Unit (U185) | STHS34PF80 | 2M                     | 80°               | I2C (0x5A) | 热辐射源在场和运动检测 |
| PIR Unit (U004)      | AS312      | 5M                     | 100°              | IO         | 热辐射源运动检测       |
| Thermal2 Unit (U149) | MLX90640   | 与距离和材质反射率相关 | 110° (32x24 像素) | I2C (0x52) | 热成像                 |
| NCIR2 Unit (U150)    | MLX90614   | 与距离和材质反射率相关 | 90°               | I2C (0x5A) | 单点热量温度检测       |
