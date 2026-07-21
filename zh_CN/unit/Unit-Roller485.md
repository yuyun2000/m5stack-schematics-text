# Unit Roller485

<span class="product-sku">SKU:U182</span>

<PictureViewer>
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-Roller485/4.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-Roller485/8.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/776/U182-zheng-package.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/776/U182-fan-package.jpg">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-Roller485/6.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-Roller485/7.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-Roller485/5.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-Roller485/10.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-Roller485/13.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-Roller485/14.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-Roller485/15.webp">
</PictureViewer>

## 描述

**Unit Roller485** 是一款集成多项控制功能的无刷直流电机运动执行套件，专为实现高效运动控制而设计。该产品支持 6-16V 直流电源输入（通过 PWR485 接口）或 5V 输入（通过 Grove 接口），能够自动调整动力系数，以确保达到最佳性能。

其内置 **FOC** 闭环驱动系统，采用 3504 200KV 无刷电机，在无强制散热的情况下，最大连续工作相电流为 0.5A，短时间内可达 1A。驱动器采用磁编码器作为反馈，支持电流、速度、位置三环控制，从而保证控制的精准度。设备轴心提供电滑环可选，滑环版本的顶部 Grove 接口与底部保持连接，即便在 360° 旋转的情况下，也能在顶部扩展额外的模块，确保旋转部分的供电与数据传输。

此外，设备背部配备 0.66 英寸 **OLED** 显示屏，可实时显示设备状态。同时，内置 RGB 指示灯和功能按键，方便进行人机交互。产品顶部与底座设计均预留了 LEGO 兼容的固定孔位和 M3 螺丝固定孔，便于快速搭建和集成。**Unit Roller485** 的软硬件部分完全开源，支持通过 **RS485** 或 **I2C** 总线实现运动控制和参数调整，并提供 SWD 和 SWO 调试接口，进一步提升了开发者使用的灵活性。该产品适用于机器关节、运动控制、工业自动化和视觉演示项目等领域。

## 教程 & 快速上手

learn> | ![Unit Roller485 使用教程](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-Roller485/8.webp) | [Unit Roller485 使用教程](/zh_CN/guide/motor_ctl/roller485/roller485) | 本教程将向你介绍 Unit Roller485 的使用教程，包括设备的配置、工作模式设置以及接线方式说明等。 |

## 产品特性

- 无刷直流电机控制
- RS-485 通讯 / I2C 通讯控制
- 集成 OLED 显示
- RGB 指示灯
- FOC 闭环驱动系统
- 集电环

## 包装内容

- 1 x Unit Roller485
- 1 x HT3.96R-4P 插头
- 2 x HY2.0-4P Grove 线 (5cm)
- 6 x 摩擦销
- 1 x 法兰盘
- 1 x 支架
- 1 x 六角钥匙 (2.5mm)
- 1 x 六角钥匙 (2mm)
- 6 x M3 螺母
- 2 x 内六角杯头 M3x14mm 螺丝
- 4 x 内六角沉头 M3x14mm 螺丝
- 4 x 内六角沉头 M3x12mm 螺丝
- 1 x 单头端子线 5P 调试线

## 应用场景

- 机器人关节控制
- 智能制造设备
- 视觉演示

## 规格参数

| 规格                       | 参数                                                                                                                                                                                    |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| MCU                        | STM32G431CBU6@Cortex-M4，128KB-Flash，32KB-SRAM，170MHz                                                                                                                                 |
| 电机类型                   | D3504 200KV 无刷电机 @直径：41mm                                                                                                                                                        |
| 驱动芯片                   | DRV8311HRRWR                                                                                                                                                                            |
| 角度传感器                 | TLI5012BE1000                                                                                                                                                                           |
| 通讯接口                   | 1x PWR-485 (HT3.96-4P 接口) <br>2x I2C (0x64)                                                                                                                                           |
| 显示屏                     | 0.66 寸 OLED 显示屏，分辨率：64 x 48，SPI 通讯                                                                                                                                          |
| RGB LEDs                   | 2x WS2812-2020                                                                                                                                                                          |
| 电机供电                   | PWR-485 (HT3.96-4P 接口) @6-16V 供电<br>Grove 口 DC 5V 供电<br>集电环\_Grove 口 DC 5V 供电                                                                                              |
| 负载                       | 负载：50g 电机转速：2100rpm 电流：DC 16V/225mA<br>负载：200g 电机转速：1400rpm 电流：DC 16V/601mA<br>负载：500g (**最大承重**) 电机转速：560rpm 电流：DC 16V/918mA<br>空载：DC 16V/78mA |
| 待机电流                   | Grove 口 DC 5V 供电 @70mA<br>RS-485 (HT3.96-4P 接口) 供电 DC 16V@32mA                                                                                                                   |
| 输出扭矩                   | Grove 口 DC 5V 供电: 0.021N.m/0.2kgf.cm@电流 350mA<br>RS485 (HT3.96-4P 接口) DC 16V 供电: 0.065N.m/0.66kgf.cm@电流 927mA                                                                |
| 集电环 (Grove 口) 输出能力 | DC 5V/300mA                                                                                                                                                                             |
| 噪音                       | 48dB                                                                                                                                                                                    |
| 工作温度                   | 0 ~ 40°C                                                                                                                                                                                |
| 产品尺寸                   | 40.0 x 40.0 x 40.0mm                                                                                                                                                                    |
| 产品重量                   | 82.9g                                                                                                                                                                                   |
| 包装尺寸                   | 102.0 x 73.0 x 51.0mm                                                                                                                                                                   |
| 毛重                       | 156.8g                                                                                                                                                                                  |

## 操作说明

\#> Unit Roller485 Lite 和 Unit Roller485 的主要区别是 Unit Roller485 Lite 不带集电环扩展 Grove 接口以及顶部乐高拓展接口。

\#> 供电电压 | 供电不能超过 16V，电压超过 18V 后会显示电机故障代码 E:1，电机不工作，显示 "Over Voltage"，LED 灯亮红灯.

\#> 编码器数值与旋转角度 | 绝对位置模式下，编码器数值 36000 pos = 360° 。由于机械安装角度与编码器角度不是严格对应，因此实际可能存在大约 2° 左右误差。

## 原理图

- [Unit Roller485 Main Board 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/776/sch_Unit-Roller485_V1.0.pdf)
- [Unit Roller485 Top Ring Board 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/776/sch_bldc_top_v1.0.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/776/sch_Unit-Roller485_V1.0_page_01.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/776/sch_bldc_top_v1.0_page_01.png">
</SchViewer>

## 管脚映射

### Unit Roller485

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

### I2C，PWR485，RGB，Button

| STM32G431CBU6 | PA15        | PB7         | PC11     | PC10     | PB4       | PB5     | PA12   |
| ------------- | ----------- | ----------- | -------- | -------- | --------- | ------- | ------ |
| I2C           | SYS_I2C_SCL | SYS_I2C_SDA |          |          |           |         |        |
| PWR485        |             |             | RS485_RX | RS485_TX | RS485_DIR |         |        |
| WS2812C       |             |             |          |          |           | LED_DAT |        |
| Button A      |             |             |          |          |           |         | SYS_SW |

### OLED

| STM32G431CBU6 | PB15      | PB13     | PB14    | PB11     | PB12    |
| ------------- | --------- | -------- | ------- | -------- | ------- |
| OLED          | OLED_MOSI | OLED_SCK | OLED_DC | OLED_RST | OLED_CS |

## 尺寸图

<SchViewer>
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-Roller485/%E5%B0%BA%E5%AF%B8%E5%9B%BE.jpg">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-Roller485/%E5%B0%BA%E5%AF%B8%E5%9B%BE2.jpg">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-Roller485/%E5%B0%BA%E5%AF%B8%E5%9B%BE3.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/776/modelsize_01.png">
</SchViewer>

## 数据手册

- [角度传感器 TLI5012BE1000](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-Roller485/TLI5012BE1000.pdf)
- [电机驱动 DRV8311HRRWR](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-Roller485/DRV8311HRRWR.pdf)

## 软件开发

### Arduino

- [Unit Roller485 Arduino 驱动库](https://github.com/m5stack/M5Unit-Roller)

### 内置固件

- [Unit Roller485 内置固件](https://github.com/m5stack/M5Unit-Roller485-Internal-FW)

### 通信协议

- I2C 协议

- [Unit Roller485 I2C Protocol](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-Roller485/Unit_Roller485_I2C_Protocol_V1_20240905.pdf)

- [Unit Roller485 I2C 用户手册](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/776/Unit-Roller485-I2C-Protocol-CN.pdf)

- RS485 协议

- [Unit Roller485 RS485 Protocol](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-Roller485/Unit_Roller485_RS485_Protocol_V1_20240905.pdf)

- [Unit Roller485 RS485 用户手册](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/776/Unit-Roller485-RS485-Protocol-CN.pdf)

### UiFlow2

- [Unit Roller485 UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/roller485.html)

## 相关视频

- Unit Roller485 产品介绍以及案例展示

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-Roller485/3e5ec07a60735d6943fa7659b7978182.mp4" type="video/mp4"></video>

- Unit Roller485 在 UiFlow 上的使用

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113423224406575&bvid=BV1cPDnYbEd9&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/Yzv2ebayh-0?si=1phbFtvdEa_T7Opk" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
