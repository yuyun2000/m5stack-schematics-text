# Unit RollerCAN-Lite

<span class="product-sku">SKU:U188-Lite</span>

<PictureViewer>
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-RollerCAN%20Lite/4.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-RollerCAN%20Lite/3.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-RollerCAN%20Lite/16.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-RollerCAN%20Lite/6.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-RollerCAN%20Lite/7.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-RollerCAN%20Lite/5.webp"/>
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-RollerCAN%20Lite/8.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-RollerCAN%20Lite/10.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-RollerCAN%20Lite/12.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-RollerCAN%20Lite/13.webp">
</PictureViewer>

## 描述

**Unit RollerCAN-Lite** 是一款集成多项控制功能的无刷直流电机运动执行套件，专为实现高效运动控制而设计。该产品支持 6-16V 直流电源输入（通过 **CAN** 接口）或 5V 输入（通过 Grove 接口），能自动调整动力系数，确保达到最佳性能。

其内置 FOC 闭环驱动系统，采用 3504 200KV 无刷电机，在无强制散热情况下，最大连续工作相电流为 0.5A，短时间可至 1A。驱动器借助磁编码器反馈，支持电流、速度、位置三环控制，保障控制精准。

此外，设备背部配有 0.66 英寸 OLED 显示屏，用于实时显示设备状态。同时，内置 RGB 指示灯与功能按键，方便人机交互。产品底座设计预留了 LEGO 兼容固定孔位与 M3 螺丝固定孔，便于快速搭建和集成。

**Unit RollerCAN-Lite** 的软硬件部分完全开源，支持通过 **CAN** 或 **I2C** 总线实现运动控制与参数调整，并提供 SWD 和 SWO 调试接口，进一步提升开发者使用的灵活性。该产品适用于机器关节、运动控制、工业自动化以及视觉演示项目等领域。

## 教程 & 快速上手

learn> | ![Unit RollerCAN-Lite 使用教程](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-RollerCAN%20Lite/3.webp) | [Unit RollerCAN-Lite](/zh_CN/guide/motor_ctl/rollercan/rollercan) | 本教程将向你介绍 Unit RollerCAN-Lite 的使用教程，包括设备的配置、工作模式设置以及接线方式说明等。 |

## 产品特性

- 无刷直流电机控制
- CAN 通讯 / I2C 通讯控制
- 集成 OLED 显示
- RGB 指示灯
- FOC 闭环驱动系统

## 包装内容

- 1 x Unit RollerCAN-Lite
- 1 x PwrCAN Cable (10cm)
- 1 x HY2.0-4P Grove 连接线 (5cm)
- 6 x 摩擦销
- 1 x 法兰盘
- 1 x 支架
- 1 x 电机转盘
- 1 x 六角钥匙 (2.5mm)
- 1 x 六角钥匙 (2mm)
- 6 x M3 螺母
- 2 x 内六角杯头 M3x14mm 螺丝
- 4 x 内六角杯头 M3x10mm 螺丝
- 1 x 内六角杯头 M2x5mm 螺丝
- 4 x 内六角沉头 M3x14mm 螺丝
- 2 x 内六角沉头 M3x12mm 螺丝
- 4 x 内六角沉头 M3x5mm 螺丝
- 1 x 单头端子线 5P 调试线 1.25mm 间距 长度 100mm

## 应用场景

- 机器人关节控制
- 智能制造设备
- 视觉演示

## 规格参数

| 规格       | 参数                                                                                                                                                                                |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| MCU        | STM32G431CBU6@Cortex-M4，128KB-Flash，32KB-SRAM，170MHz                                                                                                                             |
| 电机类型   | D3504 200KV 无刷电机 @直径：41mm                                                                                                                                                    |
| 驱动芯片   | DRV8311HRRWR                                                                                                                                                                        |
| 角度传感器 | TLI5012BE1000                                                                                                                                                                       |
| 通讯接口   | 2x CAN (XT30 接口) @XT30 (2+2) PW-M <br> 1x I2C (0x64)                                                                                                                              |
| 显示屏     | 0.66 寸 OLED 显示屏，分辨率：64 x 48，SPI 通讯                                                                                                                                      |
| RGB LEDs   | 2x WS2812-2020                                                                                                                                                                      |
| 电机供电   | CAN (XT30 接口) 供电 @6-16V<br>Grove 口 DC 5V 供电                                                                                                                                  |
| 负载       | 负载：50g 电机转速：2100rpm 电流：DC 16V/225mA<br>负载：200g 电机转速：1400rpm 电流：DC 16V/601mA<br>负载：500g (最大承重) 电机转速：560rpm 电流：DC 16V/918mA<br>空载：DC 16V/78mA |
| 待机电流   | Grove 口 DC 5V 供电 @70mA<br>CAN (XT30 接口) 供电 DC 16V@32mA                                                                                                                       |
| 噪音       | 48dB                                                                                                                                                                                |
| 输出扭矩   | Grove 口 DC 5V 供电：0.021N.m/0.2kgf.cm@电流 350mA<br>CAN (XT30 接口) 供电：0.065N.m/0.66kgf.cm@电流 927mA                                                                          |
| 工作温度   | 0 ~ 40°C                                                                                                                                                                            |
| 产品尺寸   | 40.0 x 40.0 x 40.0mm                                                                                                                                                                |
| 产品重量   | 72.2g                                                                                                                                                                               |
| 包装尺寸   | 105.0 x 76.0 x 54.0mm                                                                                                                                                               |
| 毛重       | 154.0g                                                                                                                                                                              |

## 操作说明

\#> 供电电压 | 供电不能超过 16V，电压超过 18V 后会显示电机故障代码 E:1，电机不工作，显示 "Over Voltage"，LED 灯亮蓝灯.

\#> 编码器数值与旋转角度 | 绝对位置模式下，编码器数值 36000 pos = 360° 。由于机械安装角度与编码器角度不是严格对应，因此实际可能存在大约 2° 左右误差。

## 原理图

- [Unit RollerCAN-Lite 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/779/sch_Unit-RollerCAN_V1.0.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/778/sch_Unit-RollerCAN_V1.0_page_01.png">
</SchViewer>

## 管脚映射

### Unit RollerCAN-Lite

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

### I2C，CAN，RGB，Button

| STM32G431CBU6 | PA15        | PB7         | PA11     | PA12     | PB4     | PB5     | PC6    |
| ------------- | ----------- | ----------- | -------- | -------- | ------- | ------- | ------ |
| I2C           | SYS_I2C_SCL | SYS_I2C_SDA |          |          |         |         |        |
| CAN           |             |             | FDCAN_RX | FDCAN_TX | CAN_STB |         |        |
| WS2812C       |             |             |          |          |         | LED_DAT |        |
| Button A      |             |             |          |          |         |         | SYS_SW |

### OLED

| STM32G431CBU6 | PB15      | PB13     | PB14    | PB11     | PB12    |
| ------------- | --------- | -------- | ------- | -------- | ------- |
| OLED          | OLED_MOSI | OLED_SCK | OLED_DC | OLED_RST | OLED_CS |

## 尺寸图

<SchViewer>
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-Roller485/%E5%B0%BA%E5%AF%B8%E5%9B%BE.jpg">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-Roller485/%E5%B0%BA%E5%AF%B8%E5%9B%BE2.jpg">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-Roller485/%E5%B0%BA%E5%AF%B8%E5%9B%BE3.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/779/modelsize_01.png">
</SchViewer>

## 数据手册

- [角度传感器 TLI5012BE1000](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-Roller485/TLI5012BE1000.pdf)
- [电机驱动 DRV8311HRRWR](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-Roller485/DRV8311HRRWR.pdf)

## 软件开发

### Arduino

- [Unit RollerCAN Arduino 驱动库](https://github.com/m5stack/M5Unit-Roller)

### 内置固件

- [Unit RollerCAN 内置固件](https://github.com/m5stack/M5Unit-RollerCAN-Internal-FW)

### 通信协议

- I2C 协议

- [Unit RollerCAN-I2C Protocol](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-RollerCAN%20Lite/ROLLERCAN_I2C%E5%8D%8F%E8%AE%AE_V2_20241011.pdf)

- [Unit RollerCAN-I2C 用户手册](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/779/Unit-RollerCAN-I2C-Protocol-CN.pdf)

- CAN 协议

- [Unit RollerCAN-CAN Protocol](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-RollerCAN%20Lite/UnitBLDC_CAN_%E5%8D%8F%E8%AE%AE_V1_20241011-CN.pdf)

- [Unit RollerCAN-CAN 用户手册](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/779/Unit-RollerCAN-CAN-Protocol-CN.pdf)

## 相关视频

- Unit RollerCAN-Lite 产品介绍以及案例展示

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-RollerCAN/RollerCAN%20RollerCAN%20Lite%20product%20intro%20video.mp4" type="video/mp4"></video>

## 产品对比

::compare-table
| 产品对比          | [Unit RollerCAN](/zh_CN/unit/Unit-RollerCAN) ![Unit RollerCAN](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-RollerCAN/3.webp) | [Unit RollerCAN Lite](/zh_CN/unit/Unit-RollerCAN%20Lite) ![Unit RollerCAN Lite](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-RollerCAN%20Lite/3.webp) | [Unit Roller485](/zh_CN/unit/Unit-Roller485) ![Unit Roller485](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-Roller485/8.webp) | [Unit Roller485 Lite](/zh_CN/unit/Unit-Roller485%20Lite) ![Unit Roller485 Lite](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-Roller485%20Lite/8.webp) |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 驱动芯片          | DRV8311                                                                                                                                                        | DRV8311                                                                                                                                                                                | DRV8311                                                                                                                                                        | DRV8311                                                                                                                                                                                |
| 通讯方式          | CAN/I2C                                                                                                                                                        | CAN/I2C                                                                                                                                                                                | RS485/I2C                                                                                                                                                      | RS485/I2C                                                                                                                                                                              |
| 集电环            | 带集电环                                                                                                                                                       | 不带集电环                                                                                                                                                                             | 带集电环                                                                                                                                                       | 不带集电环                                                                                                                                                                             |
| 电源指示 LED 颜色 | 蓝色                                                                                                                                                           | 无                                                                                                                                                                                     | 绿色                                                                                                                                                           | 无                                                                                                                                                                                     |
| 产品颜色          | 黑色                                                                                                                                                           | 黑色                                                                                                                                                                                   | 灰色                                                                                                                                                           | 灰色                                                                                                                                                                                   |
::
