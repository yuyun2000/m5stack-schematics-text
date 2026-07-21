# BugC2

<span class="product-sku">SKU:K033-C</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/BUGC2/img-1348bb61-bfa8-43bf-b7a0-9b4353cab25f.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/BUGC2/img-57e04d34-ca5c-4d90-95e9-a90fa53791d8.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/BUGC2/img-0bc5a9cd-2d54-4c55-bd16-cea54c367344.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/BUGC2/img-1e381892-5f06-457e-9501-4d0061fd0004.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/BUGC2/img-a9740828-2fce-41dd-9c4a-180dc5490463.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/BUGC2/img-395c2110-df6d-42d8-a993-1c83a5c13e63.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/BUGC2/img-0f70d596-edf8-4f78-a486-1b2e09cdce16.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/BUGC2/img-6a8f50ef-1fb1-43e2-b8fa-9c6e34b59358.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/BUGC2/img-8da4d0e8-e35f-405d-84ee-fcf01e6845c4.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/541/K033-C-weight.jpg">
</PictureViewer>

## 描述

**BugC2**是一款与 M5StickC 系列控制器兼容的可编程机器人底座，这款底座集成了四路 L9110S 电机驱动和直流减速电机，采用 STM32F030F4 作为其核心控制芯片，并配备了两个灵活可编程的 RGB LED、一个红外编码器以及专用的电池座。通过其顶部插槽，BugC2 能够与 M5StickC 控制器紧密连接，利用 I2C 协议 (地址 0x38) 精确接收控制指令。除了提供基础的机动能力，BugC2 还拥有 Type-C 充电接口、电池防反接保护和电压检测等高级功能，确保使用的安全性和便利性。它内置的 700mAh 16340 型可充电锂电池，保证了长时间的续航能力，使其成为一个多功能且高效的可编程机器人平台，适合各种教育和创新应用。

## 注意事项

#>脚部弹簧保护套说明|BugC2 脚部弹簧外侧的透明塑料膜为防脱落设计，请勿拆除，否则弹簧会脱落，影响设备正常使用。

## 产品特性

- 可编程机器人
- 远程控制
- 四路电机驱动器 (L9110S)
- 2xRGB LED
- 红外遥控解码
- 电池电压检测
- 板载 Type-C 口电池充电
- 电池防反接

## 包装内容

- 1 x StickC Plus2
- 1 x BugC2 底座
- 12 x 硅胶脚垫

## 应用场景

- 远程电机控制
- 机器人控制
- 智能玩具

## 规格参数

| 规格                       | 参数                                                                      |
| -------------------------- | ------------------------------------------------------------------------- |
| MCU                        | STM32F030F4P6                                                             |
| 电机驱动                   | L9110S                                                                    |
| 红外接收                   | SL0038GD                                                                  |
| RGB                        | WS2812C-2020                                                              |
| 电池容量                   | 700mAh (规格：16340)                                                      |
| 待机电流                   | Avg:DC4.2V@20.8uA                                                         |
| 工作电流                   | Avg:DC4.2V@285.1mA                                                        |
| IR 检测距离 (StickC Plus2) | ∠180° 时红外线发射距离 (直线距离)：560CM<br/>∠90° 时红外线发射距离：400CM |
| 工作温度                   | 0 ~ 40°C                                                                  |
| 产品尺寸                   | 53.5 x 53.5 x 51.5mm                                                      |
| 产品重量                   | 75.3g                                                                     |
| 包装尺寸                   | 71.7 x 70 x 58mm                                                          |
| 毛重                       | 88.1g                                                                     |

## 原理图

- [BugC2 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/541/SCH_BugC2_V1.0.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/541/SCH_BugC2_V1.0_sch_01.png">
</SchViewer>

## 管脚映射

| STM32F030F4P6       | PA1 | PA2 | PA3 | PA4 | PA1 | PB1 | PA5 | PA6 | PA7 | PA0         |
| ------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- |
| Motor1(left front)  |     |     | 1B  | 1A  |     |     |     |     |     |             |
| Motor2(Left Rear)   | 1B  |     |     |     |     |     |     |     | 1A  |             |
| Motor3(Right Rear)  |     |     |     |     |     |     | 1A  | 1B  |     |             |
| Motor4(Right front) |     | 1A  |     |     |     | 1B  |     |     |     |             |
| BAT_Detect(WS2812)  |     |     |     |     |     |     |     |     |     | BAT_ADC/RGB |

| STICKC PLUS2(ESP32-PICO-V3-02) | G36  |
| ------------------------------ | ---- |
| IR(SL0038GD)                   | IR_R |

## 尺寸图

- [BugC2 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/541/K033-C-bugc2_1_.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/541/K033-C-bugc2_1__page_01.png" width="100%">

## 数据手册

- [L9110S](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/hat/BUGC2/L9110S.PDF)

## 软件开发

### Arduino

- [BugC2 Arduino 驱动库](https://github.com/m5stack/M5Hat-BugC)

### UiFlow1

- [Hat BugC2 测试程序](/zh_CN/uiflow/blockly/hat/bugc2)

### 内置固件

- [BugC2 内置固件](https://github.com/m5stack/M5Hat-BugC-Internal-FW)

### 通信协议

<img  src="https://static-cdn.m5stack.com/resource/docs/products/app/BUGC2/protocol-b0d34b3d-3154-465e-810e-5cfd6ba909ee.png" width="100%"/>

### Easyloader

| Easyloader                    | 下载链接                                                                                                                      | 备注 |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ---- |
| BugC2 Test Example Easyloader | [download](https://static-cdn.m5stack.com/resource/docs/products/app/BUGC2/ezLoader-34f719b3-b4b9-43ff-8db8-85f8b80283c8.exe) | /    |

## 相关视频

<video id="example_video" controls>
   <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/App/BugC2.mp4" type="video/mp4">
</video>
