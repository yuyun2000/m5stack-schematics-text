
# StickC-Plus SE (coming soon)

<span class="product-sku">SKU:K016-P-SE</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/coming-soon.png">
</PictureViewer>

## 描述

**StickC-Plus SE** 是 [StickC-Plus](/zh_CN/core/m5stickc_plus)的精简版本，在保留核心功能的基础上取消了板载 6 轴 IMU 传感器，外壳颜色采用透明的橙色设计，以满足不同应用场景的需求。主控采用 ESP32-PICO-D4 模组，内置 2.4GHz Wi-Fi 功能，并集成红外发射、RTC 实时时钟、板载麦克风、状态指示灯、自定义按键、无源蜂鸣器及电源管理单元（PMU）。配备 1.14 英寸 135×240 分辨率彩色 TFT 显示屏，显示效果清晰细腻。内置 120mAh 电池，接口兼容 Hat 与 Unit 系列扩展产品，具备灵活的扩展能力。本产品适用于无需姿态检测、追求高性价比的轻量化物联网开发及简易创意项目。

## 教程 & 快速上手

learn>| ![UiFlow](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/uiflow1.0_banner_01.png) | [UiFlow](/zh_CN/uiflow/m5stickc_plus/program) | 本教程将向你介绍，如何通过 UiFlow 图形化编程平台控制 StickC-Plus SE 设备。 |

learn>| ![UiFlow2](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/uiflow2.0_banner_01.png) | [UiFlow2](/zh_CN/uiflow2/m5stickcplus/program) | 本教程将向你介绍，如何通过 UiFlow2 图形化编程平台控制 StickC-Plus SE 设备。 |

learn>| ![Arduino IDE](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/arduino_banner_01.png) | [Arduino IDE](/zh_CN/arduino/m5stickc_plus/program) | 本教程将向你介绍，如何通过 Arduino IDE 编程控制 StickC-Plus SE 设备。 |

## 产品特性

- 基于 ESP32 开发，支持 2.4GHz Wi-Fi
- 板载红色状态指示灯
- 集成红外发射单元
- 内置 RTC 实时时钟模块
- 搭载麦克风
- 配备自定义按键、LCD 显示屏、电源键与复位键
- 内置 120 mAh 锂电池
- 集成无源蜂鸣器
- 外壳采用透明橙色设计
- 开发平台
  - UiFlow1
  - UiFlow2
  - Arduino IDE
  - ESP-IDF
  - PlatformIO

## 包装内容

- 1 x StickC-Plus SE

## 应用场景

- 轻量化可穿戴设备
- 物联网智能控制器
- 简易创意 DIY 项目
- 小型智能家居控制终端

## 规格参数

| 规格     | 参数                                                              |
| -------- | ----------------------------------------------------------------- |
| SoC      | ESP32-PICO-D4 双核处理器，主频 240MHz                             |
| DMIPS    | 600                                                               |
| Flash    | 4MB                                                               |
| SRAM     | 520KB                                                             |
| Wi-Fi    | 2.4 GHz Wi-Fi                                                     |
| 天线     | 2.4G 3D 天线                                                      |
| 输入电压 | 5V@500mA                                                          |
| 电池     | 内置 3.7V 120mAh 锂电池                                           |
| 电源管理 | AXP192                                                            |
| 拓展接口 | USB Type-C x 1，HY2.0-4P (I2C+I/O+UART) x 1，2.54-8P 总线接口 x 1 |
| LCD 屏幕 | 1.14 英寸彩色 TFT LCD，分辨率 135x240，驱动芯片 ST7789v2          |
| 麦克风   | SPM1423                                                           |
| RTC      | BM8563                                                            |
| 红外     | 红外发射功能                                                      |
| 按键     | 自定义按键 x 2                                                    |
| LED      | 红色 LED x 1                                                      |
| 蜂鸣器   | 板载蜂鸣器                                                        |
| 工作温度 | 0 ~ 60°C                                                          |
| 产品尺寸 | 48.0 x 24.0 x 13.5mm                                              |
| 产品重量 | 16.9g                                                             |
| 包装尺寸 | 104.4 x 65.0 x 18.0mm                                             |
| 毛重     | 24.1g                                                             |

## 操作说明

### 开关机操作

- 开机 / 复位：单击电源键
- 关机：长按电源键

## 原理图

- [StickC-Plus SE 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1234/K016-P-SE-SCH_StickC-Plus-SE_SCH.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1234/K016-P-SE-SCH_StickC-Plus-SE_SCH.png" width="100%">

## 管脚映射

### LED & IR & BUTTON A/B & 蜂鸣器

| ESP32-PICO-D4 | G10      | G9         | G37      | G39      | G2         |
| ------------- | -------- | ---------- | -------- | -------- | ---------- |
| 红色 LED      | LED 管脚 |            |          |          |            |
| 红外发射管 IR |          | 发射管引脚 |          |          |            |
| 按键 BUTTON A |          |            | 按键管脚 |          |            |
| 按键 BUTTON B |          |            |          | 按键管脚 |            |
| 无源蜂鸣器    |          |            |          |          | 蜂鸣器管脚 |

### 彩色 TFT 屏幕

| ESP32-PICO-D4 | G15      | G13     | G23    | G18     | G5     |
| ------------- | -------- | ------- | ------ | ------- | ------ |
| TFT 屏幕      | TFT_MOSI | TFT_CLK | TFT_DC | TFT_RST | TFT_CS |

### 麦克风 MIC (SPM1423)

| ESP32-PICO-D4 | G0  | G34  |
| ------------- | --- | ---- |
| 麦克风 MIC    | CLK | DATA |

### AXP192 控制接口 (AXP192)

| ESP32-PICO-D4 | G22 | G21 |
| ------------- | --- | --- |
| AXP192        | SCL | SDA |

### 电源输出分配 (AXP192)

| AXP192   | LDO1    | LDO2   | LDO3          | GPIO0   | EXT_EN       |
| -------- | ------- | ------ | ------------- | ------- | ------------ |
| RTC      | RTC_VDD |        |               |         |              |
| LCD      |         | LCD_BL | LCD_LOGIC_VCC |         |              |
| MIC      |         |        |               | MIC_VCC |              |
| Grove 5V |         |        |               |         | EXT_BOOST_EN |

### Power Switch

| APX192       | PWRON   |
| ------------ | ------- |
| Power Switch | pwr_key |

### Hat Bus

| Hat Bus | StickC-Plus SE |
| ------- | -------------- |
| 1       | GND            |
| 2       | 5V_OUT         |
| 3       | G26            |
| 4       | G36            |
| 5       | G0             |
| 6       | BAT            |
| 7       | 3V3            |
| 8       | 5V_IN          |

### HY2.0-4P

::grove-table
| HY2.0-4P    | Black | Red | Yellow | White |
| ----------- | ----- | --- | ------ | ----- |
| PORT.CUSTOM | GND   | 5V  | G32    | G33   |
::

## 尺寸图

- [StickC-Plus SE 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1234/K016-P-SE-model-size.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1234/K016-P-SE-model-size_page_01.png" width="100%">

## 结构文件

- [StickC-Plus SE 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/K016-P_StickC-Plus/Structures)

## 数据手册

- [ESP32-PICO](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/669/esp32-pico_series_datasheet_cn.pdf)
- [ST7789v2](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/ST7789V.pdf)
- [BM8563](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/BM8563_V1.1_cn.pdf)
- [AXP192 datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/AXP192_datasheet_en.pdf)
- [AXP192 register](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/AXP192_datasheet_cn.pdf)
- [SPM1423](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/SPM1423HM4H-B_datasheet_en.pdf)

## 软件开发

### Arduino

- [StickC-Plus SE Arduino 快速上手](/zh_CN/arduino/m5stickc_plus/program)
- [StickC-Plus SE Arduino 驱动库](https://github.com/m5stack/M5StickC-Plus)
- [StickC-Plus SE 出厂测试例程](https://github.com/m5stack/M5StickC-Plus/tree/master/examples/FactoryTest)

### UiFlow1

- [StickC-Plus SE UiFlow1 快速上手](/zh_CN/uiflow/m5stickc_plus/program)

### UiFlow2

- [StickC-Plus SE UiFlow2 快速上手](/zh_CN/uiflow2/m5stickcplus/program)

### USB 驱动

?> 波特率限制 | 在进行设备程序下载操作时，推荐选用以下串口波特率选项。若采用其他速度，可能导致程序无法正常下载。<br/>**1500000 bps** / **750000 bps** / **500000 bps** / **250000 bps** / **115200 bps**

将设备连接至 PC，打开设备管理器为设备安装[FTDI 驱动](https://ftdichip.com/drivers/vcp-drivers/)。以 win10 环境为例，下载匹配操作系统的驱动文件，并解压，通过设备管理器进行安装。(注意：某些系统环境下，需要安装两次，驱动才会生效，未识别的设备名通常为**M5Stack**或**USB Serial**，Windows 推荐使用驱动文件在设备管理器直接进行安装 (自定义更新)，可执行文件安装方式可能无法正常工作)。[点击此处，前往下载 FTDI 驱动](https://ftdichip.com/drivers/vcp-drivers/)

<div class="product_pic"><img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/ftdi_01.webp"><img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/ftdi_02.webp"><img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/ftdi_03.webp"></div>

### 其他

- [StickC-Plus SE 恢复出厂固件教程](/zh_CN/guide/restore_factory/m5stickc_plus)

**注意：**

- StickC-Plus SE 支持的波特率： 1200 ~115200，250K，500K，750K，1500K

- G36/G25 共用同一个端口，当使用其中一个引脚时要将另外一个引脚设置为浮空输入

- 比如要使用 G36 引脚作为 ADC 输入，则配置 G25 引脚为浮空状态

- VBUS_VIN 与 VBUS_USB 的输入范围限制在 4.8-5.5V，VBUS 供电时将通过 AXP192 电源管理为内置电池进行充电。

```cpp
setup()
{
   M5.begin();
   pinMode(36，INPUT);
   gpio_pulldown_dis(GPIO_NUM_25);
   gpio_pullup_dis(GPIO_NUM_25);
}
```

### Easyloader

| Easyloader                         | 下载链接                                                                                                   | 备注 |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---- |
| StickC-Plus SE 出产固件 Easyloader | [download](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1234/K016-P-SE-StickC-Plus-SE-FactoryTest.exe) | /    |

## 产品对比

::compare-table
| Product Compare | [StickC-Plus SE](/zh_CN/core/StickC-Plus_SE) ![StickC-Plus SE](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/coming-soon.png) | [StickC-Plus](/zh_CN/core/m5stickc_plus) ![StickC-Plus](https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc_plus/m5stickc_plus_cover_01.webp) |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| IMU             | 无                                                                                                                                    | 有（MPU6886）                                                                                                                                                 |
| 外壳颜色        | 橙色，透明                                                                                                                            | 橙色，不透明                                                                                                                                                  |
::

如需对比 Stick 系列产品信息，可访问[产品选型表](/zh_CN/products_selector/m5stick_compare?select=K016-P)，勾选目标产品即可获取对比结果。选型表涵盖核心参数、功能特性等关键信息，支持多产品同步比对。
