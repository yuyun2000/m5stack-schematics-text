# Unit Mini IMU

<span class="product-sku">SKU:U095</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/imu/imu_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/imu/imu_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/719/U095-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/imu/imu_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/imu/imu_07.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/imu/imu_08.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/imu/imu_09.webp">
</PictureViewer>

## 描述

**Unit Mini IMU** 是一款 6 轴姿态传感器，内部集成了 3 轴重力加速计与 3 轴陀螺仪，可以实时计算倾斜角度与加速度。芯片采用 MPU6886，片上具有 16 位 ADC，内置可编程的数字滤波器与片上温度传感器，采用 I2C 接口 (addr:0x68) 与主机通讯，支持低功耗模式。

## 产品特性

- 3 轴重力加速计与 3 轴陀螺仪
- 片上温度传感器
- 1KB FIFO
- 支持低功耗
- 开发平台: Arduino，UiFlow (Blockly，Python)
- 2 x LEGO 兼容孔

## 包装内容

- 1 x Unit Mini IMU
- 1 x HY2.0-4P Grove 连接线 (5cm)

## 应用场景

- 可穿戴设备
- 运动追踪
- 无人机姿态判断

## 规格参数

| 规格       | 参数                                           |
| ---------- | ---------------------------------------------- |
| 通信接口   | I2C 通信 @ 0x68                                |
| 加速计量程 | ±2g，±4g，±8g，or ±16g                         |
| 加速计噪声 | 100 μg/√Hz                                     |
| 陀螺仪量程 | ±250，±500，±1000，or ±2000 degrees per second |
| 陀螺仪误差 | 1%                                             |
| 陀螺仪噪声 | ±4 mdps/√Hz                                    |
| 产品尺寸   | 24.0 x 24.0 x 8.0mm                            |
| 产品重量   | 3.2g                                           |
| 包装尺寸   | 138.0 x 93.0 x 9.0mm                           |
| 毛重       | 6.6g                                           |

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/imu/imu_sch_01.webp" width="80%">

## 管脚映射

### Unit Mini IMU

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 数据手册

- [MPU6886](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/MPU-6886-000193%2Bv1.1_GHIC_en.pdf)

## 尺寸图

<img alt="module size" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/imu/%E5%B0%BA%E5%AF%B8%E5%9B%BE.jpg" width="100%" />

## 结构文件

- [Unit Mini IMU 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/U095_Unit_Mini_IMU/Structures)

## 软件开发

### Arduino

- [Unit Mini IMU 测试程序](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/Unit/IMU_Unit)

### UiFlow1

- [Unit Mini IMU UiFlow1 文档](/zh_CN/uiflow/blockly/unit/imu)

### UiFlow2

- [Unit Mini IMU UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/imu.html)

### EasyLoader

| Easyloader                    | 下载链接                                                                                                                          | 备注 |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | ---- |
| Unit Mini IMU Test Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/UNIT/For%20M5Core/EasyLoader_IMU_UNIT_With_M5Core.exe) | /    |

## 相关视频

- 获取 IMU 加速度、角速度及温度

<video id="example_video" controls>
  <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Unit/IMU.mp4">
</video>

- UiFlow2 IMU Unit

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113066490528215&bvid=BV1EFHke8ELd&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
      <iframe width="560" height="315" src="https://www.youtube.com/embed/Rrxen39HHU8?si=13FulIwR1QauyCg7" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
