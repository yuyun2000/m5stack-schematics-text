# Unit Accel

<span class="product-sku">SKU:U056</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/accel/accel_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/accel/accel_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/accel/accel_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/accel/accel_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/accel/accel_06.webp">
</PictureViewer>

## 描述

**Unit Accel**是一款运动数据传感器，内部集成 **ADXL345** 三轴加速度计，可测量范围高达 **±16g**（13 位分辨率）的加速度数据。输出数据格式为 16 位二进制补码，可通过 I2C 数字接口访问（地址 0x53）。加速度计是一种测量加速力的设备。这些力可能是静态的（如重力），或者是动态的，由加速度计的移动或振动引起。通过测量由于重力引起的加速度，你可以计算出设备相对于水平面的倾斜角度。通过分析动态加速度，你可以分析出设备移动的方式。

## 产品特性

- 低功耗设计
- 单振 / 双振检测
- 活动 / 非活动监控
- 自由落体检测
- I2C 数字接口

## 包装内容

- 1 x Unit Accel
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 建筑和结构监测
- 导航
- 方向感应

## 规格参数

| 规格         | 参数                                                               |
| ------------ | ------------------------------------------------------------------ |
| 测量范围     | ±16g                                                               |
| 通信接口     | I2C 通信 @ 0x53                                                    |
| 分辨率       | 10 位固定分辨率分辨率随 g 范围提高而提高，±16 g 时高达 13 位       |
| 功耗         | VS = 2.5 V 时 (典型值)，测量模式下低至 23 µA，待 机模式下为 0.1 µA |
| I/O 电压范围 | 1.7V ~ Vs                                                          |
| 工作温度     | −40°C ~ +85°C                                                      |
| 产品尺寸     | 32.0 x 24.0 x 8.0mm                                                |
| 产品重量     | 4.1g                                                               |
| 包装尺寸     | 138.0 x 93.0 x 9.0mm                                               |
| 毛重         | 9.4g                                                               |

## 管脚映射

### Unit Accel

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/accel/accel_sch_01.webp" width="80%">

## 数据手册

- [ADXL345](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/ADXL345_en.pdf)

## 尺寸图

<img alt="module size" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/accel/%E5%B0%BA%E5%AF%B8%E5%9B%BE.jpg" width="100%" />

## 结构文件

- [Unit Accel 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/U056_Unit_Accel/Structures)

## 软件开发

### Arduino

- [Unit Accel Arduino 驱动库](https://github.com/jakalada/Arduino-ADXL345)
- [Unit Accel Example with M5Core](https://github.com/m5stack/M5Stack/blob/29d6715385be4ca3609e95cc16dc6ba0bb42516e/examples/Unit/ACCEL_ADXL345/ACCEL_ADXL345.ino)
- [Unit Accel Example with M5StickC](https://github.com/m5stack/M5StickC/blob/202fddddf05d878381f3b4d5bfa6b6e70031a290/examples/Unit/ACCEL_ADXL345/ACCEL_ADXL345.ino)
- [Unit Accel Example with M5Core2](https://github.com/m5stack/M5Core2/blob/ede1d33798e6bfa1117a7a346176ed9d24e54178/examples/Unit/ACCEL_ADXL345/ACCEL_ADXL345.ino)

### UiFlow1

- [Unit Accel UiFlow1 文档](/zh_CN/uiflow/blockly/unit/accel)

### UiFlow2

- [Unit Accel UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/accel.html)

### EasyLoader

| Easyloader                     | 下载链接                                                                                      | 备注 |
| ------------------------------ | --------------------------------------------------------------------------------------------- | ---- |
| Unit Accel example with M5Core | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Unit/EasyLoader_ACCEL.exe) | /    |

## 相关视频

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/ACCEL.mp4" type="video/mp4">
</video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113382388729245&bvid=BV1ij1GYSEdh&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/77Ok_2r33vM?si=TCQkoe6iSF_1MhmN" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
