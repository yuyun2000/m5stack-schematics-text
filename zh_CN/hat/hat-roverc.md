# RoverC

<span class="product-sku">SKU:K036</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-roverc/hat-roverc_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-roverc/hat-roverc_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-roverc/hat-roverc_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-roverc/hat-roverc_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-roverc/hat-roverc_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-roverc/hat-roverc_06.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-roverc/hat-roverc_07.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-roverc/hat-roverc_08.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-roverc/hat-roverc_09.webp">
</PictureViewer>

## 描述

**RoverC**是一款兼容 M5StickC 的可编程麦克纳姆轮全向移动机器人底座，只需插入 M5StickC 即可启动。主控芯片为 STM32F030F4，4 路 N20 蜗杆减速电机由电机驱动器直驱，带动麦克纳姆轮进行全向移动。此外，提供 2 个兼容 Grove 的 I2C 连接座方便扩展其他模块。底座兼容乐高孔，可以在结构上对其进行拓展。底座的背面装有 18350 (900mAh) 电池，并由独立开关控制，满足小车的动力和续航需求。

## 产品特性

- I2C 通讯 (0x38)
- 可编程机器人
- 远程控制
- 四路电机驱动器
- 全向移动
- 配备 18350 电池底座
- 运动灵活

## 包装内容

- 1 x RoverC

## 应用场景

- 小型移动式机器人
- 远程遥控
- 智能玩具

## 规格参数

| 规格     | 参数            |
| -------- | --------------- |
| MCU      | STM32F030F4P6   |
| 通信协议 | I2C:0x38        |
| 产品重量 | 213g            |
| 毛重     | 217g            |
| 产品尺寸 | 75 x 75 x 55mm  |
| 包装尺寸 | 115 x 85 x 65mm |

## 操作说明

<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-roverc_grip/hat-roverc_grip_04.webp" width="40%" height="30%">

## 管脚映射

| M5StickC   | G26 | G0  | 5V  | GND |
| ---------- | --- | --- | --- | --- |
| RoverC HAT | SCL | SDA | 5V  | GND |
| I2C①       | SCL | SDA | 5V  | GND |
| I2C②       | SCL | SDA | 5V  | GND |

## 软件开发

### Arduino

> 1: 该案例使用 RoverC 和 JoyC, 通过 UDP 通信实现无线控制。 请据你所使用的设备选择下方对应的案例程序。

- [RoverC-Pro & JoyC Remote Control - with M5StickC](https://github.com/m5stack/M5-RoverC/tree/master/examples/RoverC_M5StickC/JoyC_%26_RoverC)

- [RoverC-Pro & JoyC Remote Control - with M5StickC-Plus](https://github.com/m5stack/M5-RoverC/tree/master/examples/RoverC_M5StickCPlus/JoyC_%26_RoverC)

- 注意：开机后 RoverC 会显示 "M5AP+2 字节 mac 地址" 热点名称，同时 JoyC 会扫描到 RoverC 的 mac 地址名，长按 3 秒 JoyC 上的 M5StickC 的 Home 键，开始扫描小车的热点，即可配对成功。成功配对后屏幕左上角会高亮显示链接图标，同时屏幕显示摇杆数值。左摇杆上下控制前后，左右控制平移，右摇杆左右控制转向。

> 2: 该案例为 RoverC 单机控制程序，由主控直接控制。请据你所使用的设备选择下方对应的案例程序。

- [RoverC-Pro Example- with M5StickC](https://github.com/m5stack/M5-RoverC/blob/master/examples/RoverC_M5StickC/RunningRoverC/RunningRoverC.ino)
- [RoverC-Pro Example- with M5StickC-Plus](https://github.com/m5stack/M5-RoverC/blob/master/examples/RoverC_M5StickCPlus/RunningRoverC/RunningRoverC.ino)

### UiFlow1

- [RoverC-Pro UiFlow1 文档](/zh_CN/uiflow/blockly/hat/roverc)

### 通信协议

- 通讯类型：I2C

- I2C 通讯地址: **0x38**

- [RoverC-Pro I2C Protocol](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/hat/hat_roverc_pro/K036-B_I2C_PROTOCOL_CN.pdf)

### Easyloader

| Easyloader            | 下载链接                                                                                                        | 备注 |
| --------------------- | --------------------------------------------------------------------------------------------------------------- | ---- |
| RoverC-Pro Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/HAT/EasyLoader_RoverC_PRO_Alone.exe) | /    |

## 相关视频

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/HAT/RoverC.mp4" type="video/mp4">
</video>

## 版本变更

| 上市日期 | 产品变动                                       | 备注: |
| -------- | ---------------------------------------------- | ----- |
| 2019.11  | 首次发售                                       | /     |
| 2020.5   | 电池型号 16340（750mAh）变更为 18350（900mAh） | /     |
