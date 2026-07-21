# Tab5 Keyboard

<span class="product-sku">SKU:A164</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1241/A164_tab5_keyboard_main_pictures_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1241/A164_tab5_keyboard_main_pictures_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1241/A164_tab5_keyboard_main_pictures_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1241/A164_tab5_keyboard_main_pictures_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1241/A164_tab5_keyboard_main_pictures_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1241/A164_tab5_keyboard_main_pictures_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1241/A164_tab5_keyboard_main_pictures_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1241/A164_tab5_keyboard_main_pictures_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1241/A164_tab5_keyboard_main_pictures_09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1241/A164_tab5_keyboard_main_pictures_10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1241/A164_tab5_keyboard_main_pictures_11.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1241/A164_tab5_keyboard_main_pictures_12.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1241/A164_tab5_keyboard_main_pictures_13.webp">
</PictureViewer>

## 描述

**Tab5 Keyboard** 是一款专为 Tab5 打造的 70 键物理键盘输入扩展模块，可通过 Tab5 Ext.Port1 直接连接主机，实现即插即用的输入体验。
模块内置 STM32F030C8T6 主控芯片，负责键盘矩阵扫描与通信处理；预置固件支持 **普通**、**HID**、**字符** 三种工作模式，适配不同交互需求。
键盘采用 14 x 5 矩阵设计，支持多键同时按下，提供完整字母、数字、符号及 Aa、Ctrl、Sym、Alt、Tab、Esc、方向键等常用功能键。
设备通过 I2C 与 Tab5 通信，并提供独立中断引脚，可实现按键事件的低延迟实时上报。板载两颗 RGB LED，可用于全彩状态指示。整体结构紧凑、连接方式简单，适用于文本输入、指令交互，以及各类需要实体键盘的便携式应用场景。

## 教程 & 快速上手

learn>| ![用户案例教程](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1241/A164_user_demo_doc_01.jpg) | [用户案例教程](/zh_CN/guide/input_device/tab5_keyboard) | 本教程介绍 Tab5 Keyboard 搭配 Tab5 使用的用户案例，包括固件烧录的方法，以及 USB HID 输出，寄存器显示等功能。|

## 产品特性

- 采用 STM32F030C8T6 作为主控芯片
- 适配 Tab5，直连拓展口即插即用
- 三种工作模式，适配多样需求
- 14×5 矩阵，支持多键同时按压
- 按键齐全，含各类常用功能键
- I2C 通信，中断引脚低延迟上报
- 板载双 RGB LED，多彩状态指示
- 两侧卡扣可稳固锁紧 Tab5；背部预留两个 M3 螺丝固定孔
- 结构紧凑，便携场景适配性强

## 包装内容

- 1 x Tab5 Keyboard

## 应用场景

- 文本输入
- 指令交互
- 便携式应用场景
- 教育编程与创客项目

## 规格参数

| 规格     | 参数                                                              |
| -------- | ----------------------------------------------------------------- |
| MCU      | STM32F030C8T6                                                     |
| 按键     | 70 键键盘                                                         |
| I2C 地址 | 0x6D（默认）                                                      |
| RGB LED  | 2 x WS2812E-1313                                                  |
| 接口     | 2 x 5 PIN 排针，间距 2.54mm                                       |
| 待机功耗 | DC 3.3V@14.5mA                                                    |
| 工作功耗 | RGB（白色）最大亮度：3.3V@21.5mA<br>输入（RGB 关闭）：3.3V@14.5mA |
| 产品尺寸 | 128.0 x 59.4 x 13.1mm                                             |
| 产品重量 | 65.2g                                                             |
| 包装尺寸 | 147.0 x 82.0 x 16.5mm                                             |
| 毛重     | 97.4g                                                             |

## 操作说明

### 设备连接示意图

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1241/A164_operate_01.jpg" width="70%">

## 原理图

- [Tab5 Keyboard 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1241/SCH_Tab5_Keyboard_SCH_V1.0_20251109_2026_05_06_16_24_34.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1241/SCH_Tab5_Keyboard_SCH_V1.0_20251109_2026_05_06_16_24_34_page_01.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1241/SCH_Tab5_Keyboard_SCH_V1.0_20251109_2026_05_06_16_24_34_page_02.png">
</SchViewer>

## 管脚映射

| Tab5          | G0  | G1  | G50 |
| ------------- | --- | --- | --- |
| Tab5 Keyboard | SDA | SCL | INT |

## 尺寸图

- [Tab5 Keyboard 模型尺寸 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1241/a164-Tab5-Keyboard.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1241/a164-Tab5-Keyboard_page_01.png" width="100%">

## 结构文件

- [Tab5 Keyboard 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/A164_Tab5_Keyboard/Structures)

## 数据手册

- [STM32F030C8T6](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/Unit%208Encoder/STM32F030C8T6.pdf)
- [WS2812E](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-Puzzle/ws2812e.pdf)

## 软件开发

### 快速上手

- [Tab5 Keyboard 用户案例介绍](/zh_CN/guide/input_device/tab5_keyboard)

### Arduino

- [Tab5 Keyboard Arduino Library](https://github.com/m5stack/M5Unit-KEYBOARD)
- [Tab5 Keyboard Arduino 快速上手](/zh_CN/arduino/projects/tab5/tab5_keyboard)

### ESP-IDF

- [Tab5 Keyboard 用户案例](https://github.com/m5stack/M5Tab5-Keyboard-UserDemo)

### 内置固件

- [Tab5 Keyboard 内置固件](https://github.com/m5stack/M5Tab5-Keyboard-Internal-FW)

### 通信协议

- [Tab5 Keyboard 使用手册](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1241/Tab5_Keyboard_User_Manual_CN.pdf)
- [Tab5 Keyboard 通信协议](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1241/Tab5_Keyboard-I2C-Protocol-CN-V1.0.pdf)

Tab5 Keyboard 支持三种数据报文模式，适配不同应用场景。

- 普通模式：返回按键状态与所在行列坐标
- HID 模式：返回 HID 报文，结合 Tab5 USB / BLE 转发，可实现 HID 输入设备功能
- 字符模式：返回按下的一般按键的名称字符串、Ctrl/Alt 修饰符状态，Sym/Aa 直接实现相应功能。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1241/Tab5_Keyboard-I2C-Protocol-CN-V1.0_page_01.png" width="100%">

## 相关视频

- Tab5 Keyboard 产品介绍以及功能展示

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1241/A164_Tab5_keyboard_video_ZH.mp4" type="video/mp4"></video>
