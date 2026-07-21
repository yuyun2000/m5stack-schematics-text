# Unit DDS

<span class="product-sku">SKU:U105</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/dds/dds_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/dds/dds_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/dds/dds_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/dds/dds_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/dds/dds_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/dds/dds_06.webp">
</PictureViewer>

## 描述

**Unit DDS** 是一款信号源 Unit。采用 AD9833 可编程波形发生器 + STM32F0 控制方案。提供 I2C 通信接口 （ addr : 0x31 ），实际使用时以配置寄存器的方式进行操作。能够非常方便的控制该信号源输出多种波形 （ 正弦波、三角波、方波输出、锯齿波，信号输出幅值 0-0.6V ），与调整频率、相位。并且支持休眠策略，空闲状态时能够进一步减小电能损耗。该 Unit 适用于各种测试仪器的电子线路原型设计中充当信号源。

## 产品特性

- 数字可编程频率和相位
- 信号输出幅值 0-0.6V
- 正弦波 / 三角波 / 方波 / 锯齿波 (固定频率：13.6KHz) /DC 输出
- 输出频率范围：0MHz 至 1MHz (10MHz 基准时钟)
- 28bit 频率分辨率
- 11bit 相位分辨率

## 包装内容

- 1 x Unit DDS
- 1 x HY2.0-4P Grove 连接线 (20cm)
- 1 x SMA-2.54mm 线缆

## 应用场景

- 频率刺激 / 波形发生
- 液流和气流测量
- 传感器应用：接近度、运动和缺陷检测
- 线路损耗 / 衰减
- 测试与医疗设备
- 扫描 / 时钟发生器
- 时域反射 (TDR) 应用

## 规格参数

| 规格         | 参数                                                         |
| ------------ | ------------------------------------------------------------ |
| MCU          | STM32F031G4U6                                                |
| 通信接口     | I2C 通信 @ 0x31                                              |
| 支持波形     | 正弦波 / 三角波 / 方波 / 锯齿波 (固定频率：13.6KHz) /DC 输出 |
| 信号输出幅值 | 0-0.6V                                                       |
| 输出频率范围 | 0 MHz 至 1MHz (10 MHz 基准时钟)                              |
| 频率分辨率   | 28bit                                                        |
| 相位分辨率   | 11bit                                                        |
| 产品尺寸     | 71.4 x 24.0 x 8.0mm                                          |
| 产品重量     | 11.2g                                                        |
| 包装尺寸     | 88.0 x 60.0 x 21.0mm                                         |
| 毛重         | 34.0g                                                        |

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/dds/dds_sch_01.webp" width="80%">

## 管脚映射

### Unit DDS

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 尺寸图

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/787/U105_Model_Size.jpg" width="100%">

## 数据手册

- [AD9833](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/dds/ad9833.pdf)

## 软件开发

### Arduino

- [Unit DDS Test Example with M5Core](https://github.com/m5stack/M5Unit-DDS/blob/master/examples/Unit_DDS_M5Core/Unit_DDS_M5Core.ino)

### UiFlow2

- [Unit DDS UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/dds.html)

### 通讯协议

- 协议类型 I2C
- I2C Address: **0x31**

\#> 注意事项:| 写寄存器时，需要将最高位置 1。mclk 置 1 将保持输出最后一个信号幅值，DAC 置 1 将停止 Unit 输出。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/dds/%E5%8D%8F%E8%AE%AE%E5%9B%BE.png" width="100%">

### EasyLoader

| Easyloader          | 下载链接                                                                                                                          | 备注 |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------- | ---- |
| Unit DDS Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/UNIT/For%20M5Core/EasyLoader_DDS_UNIT_With_M5Core.exe) | /    |

## 相关视频

控制 Unit DDS 输出正弦波 / 三角波 / 方波 / 锯齿波.

<video id="example_video" controls>
  <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Unit/DDS_UNIT.mp4" type="video/mp4">
</video>
