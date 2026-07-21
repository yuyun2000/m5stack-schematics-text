# Unit TimerPWR

<span class="product-sku">SKU:U189</span>

<PictureViewer>
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-TimerPWR/4.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-TimerPWR/11.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-TimerPWR/13.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-TimerPWR/5.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-TimerPWR/6.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-TimerPWR/7.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-TimerPWR/8.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-TimerPWR/9.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-TimerPWR/12.webp">
</PictureViewer>

## 描述

**Unit TimerPWR** 是一款定时供电单元，具备 “充放电 + 定时开关 + 屏幕显示 + 升压输出” 等主要功能。其内置 STM32 微控制器，用于实现 RTC（实时时钟）及整体控制，方便用户依据自身需求设置自动开机与关机时间。

该单元通过 **Type-C** 接口进行 **供电**，并借助 1.25-2P 接口外接可充电电池。它内置电池充电电路，能支持 330mA 的充电电流。同时，还内置 DC-DC **升压**电路，可通过 Grove 口为外部设备提供 5V/800mA（1400mA@1C 电池供电）的电源输出。此外，内置 INA3221 传感器，可实时监控电源输入输出的电流和电压。

此单元配备 0.66 英寸 **OLED** 显示屏以及 2 个侧按钮，用于实现用户交互，用户能够便捷地查看系统实时状态并修改设置参数。用户既可以通过两侧按钮进行设置，也可以使用接入 Grove 接口的 I2C 总线，通过 I2C 指令来设置开关机参数等。本产品适用于智能家居、工业自动化及定时控制设备等场景。

## 产品特性

- RTC 循环定时控制
- 电池供电
- 内置 DC-DC 升压电路
- 电流 / 电压监测
- OLED 显示屏
- Grove 接口
- 按键控制开关机模式

## 包装内容

- 1 x Unit TimerPWR
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 定时控制设备
- 便携式电子设备
- 传感器节点供电

## 规格参数

| 规格                 | 参数                                                                                                                                        |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| MCU                  | STM32G031G8U6                                                                                                                               |
| 输入电压             | 支持 5V 直流输入 (通过 Type-C 接口)                                                                                                         |
| 输出电压             | 内置 DC-DC 升压电路，输出 5V 电压，供外部设备使用                                                                                           |
| 电池供电             | 3.7V 聚合物锂电池                                                                                                                           |
| 显示屏               | 0.66 英寸 OLED 显示屏，分辨率 64x48，SPI 通讯                                                                                               |
| 接口                 | Type-C 接口：用于为电池充电 (不可直接给 Grove 口供电) <br/>Grove 接口：用于外部传感器和模块扩展，支持通讯和对外供电<br/>电池接口：1.25mm@2P |
| I2C 通讯地址         | 0x56                                                                                                                                        |
| 电流传感器           | INA3221                                                                                                                                     |
| 充电电流             | DC 5V@330mA                                                                                                                                 |
| 充电芯片             | LGS4056H                                                                                                                                    |
| 充电温度             | 55°C                                                                                                                                        |
| Grove 口输出最大电流 | 与电池容量和放电能力相关 eg：<br/>1400mAh@1C 3.7V:DC4.96V@800mA<br/>500mAh@1C 3.7V：DC4.97V@700mAh<br/>110mAh@1C 3.7V: DC5.03V@400mAh       |
| 待机电流             | DC4.2V@36.67uA                                                                                                                              |
| 工作温度             | 0 ~ 40°C                                                                                                                                    |
| 产品尺寸             | 40.0 x 24.0 x 11.0mm                                                                                                                        |
| 产品重量             | 7.5g                                                                                                                                        |
| 包装尺寸             | 138.0 x 93.0 x 12.0mm                                                                                                                       |
| 毛重                 | 13.2g                                                                                                                                       |

## 操作说明

### 设备供电

?> 供电要求 | Unit TimerPWR 使用时必须连接锂电池，其 USB 接口仅用于电池充电使用，无法直接用于输出供电。

## 原理图

- [Unit TimerPWR 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/780/U189_SCH_UNIT_TimerPwr_V1.0.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/780/U189_SCH_UNIT_TimerPwr_V1.0_page_01.png">
</SchViewer>

## 管脚映射

### Unit TimerPWR

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

### STM32G031G8U6

| STM32G031G8U6  | PB6  | PB7  | PA11 | PA12 | PB4  | PA0   | PA4   |
| -------------- | ---- | ---- | ---- | ---- | ---- | ----- | ----- |
| I2C1 (GROVE)   | SCL1 | SDA1 |      |      |      |       |       |
| I2C2 (INA3221) |      |      | SCL2 | SDA2 |      |       |       |
| LED (充电提示) |      |      |      |      | CHAG |       |       |
| Button A       |      |      |      |      |      | BTN_A |       |
| Button B       |      |      |      |      |      |       | BTN_B |

### OLED

| STM32G031G8U6 | PA2       | PA1      | PA6     | PA7      | PB0     | PB1   |
| ------------- | --------- | -------- | ------- | -------- | ------- | ----- |
| OLED          | OLED_MOSI | OLED_SCK | OLED_DC | OLED_RST | OLED_CS | BL_EN |

## 尺寸图

<img alt="module size" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-TimerPWR/%E5%B0%BA%E5%AF%B8%E5%9B%BE.jpg" width="100%" />

## 数据手册

- [INA3221](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-TimerPWR/ina3221.pdf)
- [LGS4056H](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-TimerPWR/LGS4056H.pdf)

## 软件开发

### Arduino

- [Unit TimerPWR Arduino 驱动库](https://github.com/m5stack/M5Unit-TimerPWR)

### UiFlow1

- [Unit TimerPWR UiFlow1 文档](/zh_CN/uiflow/blockly/unit/timerpwr)

### UiFlow2

- [Unit TimerPWR UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/timerpwr.html)

### 内置固件

- [Unit TimerPWR 内置固件](https://github.com/m5stack/M5Unit-TimerPWR-Internal-FW)

### 通信协议

- [Unit TimerPWR I2C Protocol](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-TimerPWR/U189_UnitTimerPwr_I2C_Protocol_V1_20241018.pdf)

<img alt="module size" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-TimerPWR/%E5%8D%8F%E8%AE%AE.png" width="100%" />

## 相关视频

- Unit TimerPWR 产品介绍以及案例展示

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/envIII/timerpwr%20video.mp4" type="video/mp4"></video>

- UiFlow2 Use

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113423207629182&bvid=BV1cNDnYZETt&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/PuTkw8ALJQ0?si=ZgZyAZ1Oz7wowIyc" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
