# Bala

<span class="product-sku">SKU:K014</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/bala/bala_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/bala/bala_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/bala/bala_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/bala/bala_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/bala/bala_05.webp">
</PictureViewer>

## 描述

**Bala** 是一款平衡车应用。该产品是由 M5 FIRE 与 双路直流电机底座组合而成的一款自平衡机器人，其 "BALA" 名称的由来出自 "Balance" 一词的缩写。默认预装平衡车应用程序，在运行时使用闭环算法保持垂直平衡。使用加速度计与陀螺仪姿态数据来校正其方向和位置.

## 产品特性

- 2 路直流驱动器模块
- I2C 通信：0x56
- 兼容 LEGO
- POGO Pin
- 支持 microSD 拓展

## 包装内容

- 1 x Bala
- 1 x 电机驱动
- 2 x N20 电机 (内置编码器)
- 1 x Type-C USB

## 规格参数

| 规格     | 参数                                           |
| -------- | ---------------------------------------------- |
| ESP32    | 240MHz 双核，600 DMIPS,520KB SRAM,Wi-Fi        |
| Flash    | 16MB Flash + 4MB PSRAM                         |
| 输入     | 5V @ 500mA                                     |
| 接口     | Type-C x 1, GROVE (I2C+I/O+UART), Pogo Pin x 1 |
| LCD      | 2 英寸，320x240 彩色 TFT LCD, ILI9341          |
| 扬声器   | 1W-0928                                        |
| 麦克风   | MEMS 模拟 BSE3729 麦克风                       |
| LED      | SK6812 3535 RGB LED x 10                       |
| MEMS     | BMM150+(MPU6886/SH200Q)                        |
| 电池     | 内置 550mAh @ 3.7V                             |
| 工作温度 | 32°F 至 104°F ( 0°C 至 40°C )                  |
| 主控尺寸 | 54 x 54 x 21 mm                                |
| C.A.S.E  | 塑料 ( PC )                                    |
| 产品重量 | 130g                                           |
| 毛重     | 247g                                           |
| 产品尺寸 | 90 x 54 x 61mm                                 |
| 包装尺寸 | 185 x 108 x 81mm                               |

## 操作说明

?> BMM150 磁场干扰 | 带有磁铁的产品可能对 BMM150 磁场传感器造成干扰，导致读数异常。当搭配含有磁铁的 M5 主控设备时，需拆除磁铁，同时避免 BMM150 传感器放置在强磁场附近。

### 传感器进行校准

注意：首次使用务必先进行校准！按住最右侧 C 键开机，听到 "滴" 声后松开按键，传感器会进入校准设置，保持主机水平静止放置，3 秒后传感器校准完成，校准完成后会自动进入平衡模式。如果在使用过程中发现 BALA 无法保持平衡，可通过尝试校准传感器进行解决。

## 管脚映射

**Mega328 ISP**下载接口 Pin 脚定义

<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-cardkb/mega328_isp_sch_01.webp" width="30%" height="30%">

## 软件开发

### Arduino

- [Bala Balancing Example](https://github.com/m5stack/M5Stack/tree/master/examples/Modules/BALA).

### EasyLoader

| Easyloader                                    | 下载链接                                                                                                             | 备注 |
| --------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ---- |
| Bala Test Firmware MPU6050 Version Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Application/BALA/EasyLoader_APP_BALA.exe)         | /    |
| Bala Test Firmware MPU6886 Version Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Application/BALA/EasyLoader_APP_BALA_MPU6886.exe) | /    |

## 相关视频

**BALA 的演示**

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Blog/Twitch201812/M5BALA%20.mp4" type="video/mp4">
</video>

**BALA 的演示 - 手机控制**

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Blog/Twitch201811/Iphone%20Controlled%20M5Bala%20.mp4" type="video/mp4">
</video>

**BALA 的演示 - 巡线**

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Blog/Twitch201901/M5BALA.mp4" type="video/mp4">
</video>

**BALA 的演示 - 使用手机巡线**

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Blog/Twitch201812/Self-tracing%20Car.mp4" type="video/mp4">
</video>
