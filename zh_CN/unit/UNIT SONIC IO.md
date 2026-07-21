# Unit Ultrasonic-IO

<span class="product-sku">SKU:U098-B2</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/UNIT SONIC IO/img-4ba90df3-6a11-4870-b605-c55983992d76.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/UNIT SONIC IO/img-a2699c07-ba13-43b2-a0ad-342cd284f2dc.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/UNIT SONIC IO/img-296b4dcc-1635-45e7-b1e1-503cb24cdb79.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/UNIT SONIC IO/img-ae43de81-b42d-4924-903b-ede2bf195831.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/UNIT SONIC IO/img-b6400e1d-1f68-4478-8959-73982ce70e9a.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/UNIT SONIC IO/img-a41cc887-0118-44bc-8c4d-6fe926b23d72.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/UNIT SONIC IO/img-2dd45ebd-26bc-4b0b-b346-b28cc4a9190c.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/UNIT SONIC IO/img-7ae90bae-208c-4595-bd0e-e0804ff9fd85.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/698/U098-B2-weight.jpg">
</PictureViewer>

## 描述

**Unit Ultrasonic-IO** 是一款 **GPIO** 接口的 **超声波测距** 传感器。硬件采用 RCWL-9620 超声波测距单芯片搭配 16 mm 探头，能够实现 **2 cm-450 cm** 范围内的精准测距 (精度达 ±2%)。控制器在给出触发信号后，传感器输出的脉冲时长对应声波反射时间，通过这一数据即可计算出距离，通过 IO 控制的方式使得该传感器有着极快的响应速度。非常适合应用于机器人避障，液面检测等应用场景。

\#> 注意：测量大于 3.5m 时，测距数据响应会稍有延迟。

## 产品特性

- RCWL-9620
- GPIO 通信接口
- 量程: 2cm-450cm
- 覆盖保护外壳，电路运行更稳定
- 内置温度补偿，减小探头温飘影响
- 支持 UiFlow 图形化编程

## 包装内容

- 1 x Unit Ultrasonic-IO
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 机器人避障
- 液位测量
- 坐姿检测

## 规格参数

| 规格             | 参数                 |
| ---------------- | -------------------- |
| 超声波测距单芯片 | RCWL-9620            |
| 量程             | 2cm-450cm            |
| 探头规格         | 16mm                 |
| 接收 / 发射频率  | 40KHz                |
| 接收灵敏度       | -65dB                |
| 指向角           | 60°                  |
| 测量精度         | ±2%                  |
| 测量周期         | 50ms                 |
| 工作电流         | 3mA                  |
| 产品尺寸         | 56.0 x 24.0 x 15.2mm |
| 产品重量         | 11.8g                |
| 包装尺寸         | 75.0 x 46.0 x 36.0mm |
| 毛重             | 27.0g                |

## 管脚映射

### Unit Ultrasonic-IO

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 尺寸图

<img alt="module size" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/UNIT%20SONIC%20I2C/model%20size.jpg" width="100%" />

## 结构文件

- [Unit Ultrasonic-IO 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/U098-B2_Unit_Ultrasonic-IO/Structures)

## 数据手册

- [RCWL-9620 Datasheet](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/697/RCWL-9620-V1.0.pdf)

## 软件开发

### Arduino

- [Unit Ultrasonic-IO with M5Atom](https://github.com/m5stack/M5Unit-Sonic/blob/master/examples/Unit_SonicIO_M5Atom/Unit_SonicIO_M5Atom.ino)
- [Unit Ultrasonic-IO with M5Core](https://github.com/m5stack/M5Unit-Sonic/blob/master/examples/Unit_SonicIO_M5Core/Unit_SonicIO_M5Core.ino)
- [Unit Ultrasonic-IO with M5Core2](https://github.com/m5stack/M5Unit-Sonic/blob/master/examples/Unit_SonicIO_M5Core2/Unit_SonicIO_M5Core2.ino)
- [Unit Ultrasonic-IO with M5StickC](https://github.com/m5stack/M5Unit-Sonic/blob/master/examples/Unit_SonicIO_M5StickC/Unit_SonicIO_M5StickC.ino)
- [Unit Ultrasonic-IO with M5StickCPlus](https://github.com/m5stack/M5Unit-Sonic/blob/master/examples/Unit_SonicIO_M5StickCPlus/Unit_SonicIO_M5StickCPlus.ino)

### UiFlow1

- [Unit Ultrasonic-IO UiFlow1 文档](/zh_CN/uiflow/blockly/unit/sonic_io)

### UiFlow2

- [Unit Ultrasonic-IO UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/ultrasonic_io.html)

## 相关视频

- 超声波小车避障

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Unit/sonic_i2c_gpio_video.mp4" type="video/mp4"></video>
