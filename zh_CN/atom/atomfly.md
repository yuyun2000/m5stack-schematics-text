# Atom Fly

<span class="product-sku">SKU:K040</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomfly/atomfly_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomfly/atomfly_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomfly/atomfly_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomfly/atomfly_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomfly/atomfly_06.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomfly/atomfly_07.webp">
</PictureViewer>

## 描述

**Atom Fly** 是一款支持 ATOM 的可编程迷你四轴无人机，适用于室内或无风情况下飞行。机架采取 PCB 一体化设计，直接将电机固定于 PCB 上，最大程度减轻机身重量。机臂采用 X 型布局，操控更加灵活，机身搭载气压计与三轴加速计和陀螺仪 (IMU) 可进行定高与姿态保持，同时底部配备 ToF 可用于自动起降与避障。机头有一颗 LED 电源指示灯，整机由外置 200mAh 锂电池供电。(出厂无任何固件程序，用户需自行编写程序进行控制)

## 产品特性

- 支持 WiFi 遥控、可编程
- 内置气压计、三轴加速计、陀螺仪、ToF
- 机身小巧、紧凑

## 包装内容

- 1 x Atom-Lite
- 1 x Atom Fly 机体
- 1 x 200mAh 电池
- 1 x 电池充电器
- 2 x 正桨
- 2 x 反桨

## 应用场景

- 遥控无人机

## 规格参数

| 规格                | 参数                   |
| ------------------- | ---------------------- |
| ToF                 | VL53L0x                |
| 陀螺仪加速计（IMU） | MPU6886                |
| 气压计              | BMP280                 |
| 动力电池            | 200mAh/1S/25C/JST      |
| 螺旋桨直径          | 2 英寸                 |
| 空心杯电机          | 负载转速 31000±10% RPM |
| 外壳材质            | PCB                    |
| 产品尺寸            | 70 x 70 x 30mm         |
| 产品重量            | 32g                    |
| 包装尺寸            | 150 x 75 x 40mm        |
| 毛重                | 70g                    |

## 操作说明

<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomfly/atomfly_04.webp" width="70%">

Atom Fly 所有硬件功能出厂均经过测试，其中 Atom-Lite 主控无任何内置固件，以下提供的程序均只提供基本功能测试，您需要通过自行编程来实现遥控飞行的目的。测试时请注意安全，身体远离螺旋桨，防止意外发生。锂电池使用随机附送的充电线进行充电，通过指示灯观察电池充电状态，红色表示正在充电，绿色表示充电完成 (30 分钟左右)。电池充满后不可长时间继续充电，防止电池发热造成安全隐患。

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomfly/atomfly_sch_01.webp" width="70%">

## 管脚映射

| Atom     | G21 | G25 | G22  | G19  | G23  | G33  |
| -------- | --- | --- | ---- | ---- | ---- | ---- |
| Atom FLY | SCL | SDA | PWM1 | PWM2 | PWM3 | PWM4 |
| MPU6886  | SCL | SDA |      |      |      |      |
| VL53L0X  | SCL | SDA |      |      |      |      |
| BMP280   | SCL | SDA |      |      |      |      |

## 数据手册

- [MPU6886](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/MPU-6886-000193%2Bv1.1_GHIC_en.pdf)
- [BMP280](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/hat/BMP280-DS001-11_en.pdf)
- [VL53L0X](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/hat/VL53L0X_en.pdf)
- [DC Moter C.W](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/atombase/AtomFLY/Motor_716-37A-14.pdf)
- [DC Moter CCW](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/atombase/AtomFLY/Motor_716-37B-14.pdf)

## 软件开发

### Arduino

- [Atom Fly 测试程序](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/AtomBase/AtomFLY)

### EasyLoader

| Easyloader                       | 下载链接                                                                                                     | 备注 |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------ | ---- |
| Atom Fly Test Example Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/ATOM_BASE/EasyLoader_AtomFLY.exe) | /    |

## 相关视频

按下 Atom 按键，螺旋桨依次旋转，串口监视器输出 IMU 状态

<video id="example_video" controls>
  <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/AtomBase/AtomFLY.mp4" type="video/mp4">
</video>
