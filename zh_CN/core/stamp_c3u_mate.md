# Stamp-C3U Mate

<span class="product-sku">SKU:K122</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/526/K122_01.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/526/K122_02.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/526/K122_03.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/526/K122_04.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/526/K122_05.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/526/K122_06.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/526/K122_07.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/526/K122_08.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/526/K122_09.jpg">
</PictureViewer>

## 描述

**Stamp-C3U Mate** 是 Stamp-C3U 最小核心板的配件套装。套装内配备了 Stamp-C3U，以及排母、排针、HY2.0-4P 母座等实用配件，能够非常方便的将 Stamp-C3U 快速集成至您的电路中。Stamp-C3U 是一款具有高性价比的 RISC-V 最小核心板。采用乐鑫 **ESP32-C3** 主控芯片，内置 **RISC-V 32 bit 单核处理器**，时钟频率可高达 160 MHz 。其内置 400 KB SRAM + 4MB Flash ，并且集成了 2.4 GHz Wi-Fi。该核心板支持安全启动、Flash 加密、数字签名等安全机制。其体积小巧，但功能却十分强大，能够满足多样化的物联网应用需求。

## 产品特性

- 支持多种应用形态 (SMT，DIP，飞线)
- 配有高温塑料铠装，支持 SMT 过炉温度 (230°C)
- 内含 5V->3.3V DC/DC 电路，GPIOx14
- Type-C 接口
- 可编程 RGB 灯 x1，复位按钮 x1，按键 x1
- 高性能 3D 天线，提供稳定可靠的无线通信质量
- ESP32 最小系统板
- 开发平台
  - Arduino IDE
  - ESP-IDF
  - PlatformIO

## 包装内容

- 1 x Stamp-C3U
- 1 x 耐高温贴纸
- 2 x 2.54-12P 排母
- 2 x 2.54-10P 排针
- 2 x HY2.0-4P 母座（90°）
- 1 x 内六角扳手 L 形 1.5mm (适配 M2 螺丝)

## 应用场景

- DIY，原型制作
- 工业自动化
- 智能家居

## 规格参数

| 规格             | 参数                                                               |
| ---------------- | ------------------------------------------------------------------ |
| SoC              | ESP32-C3@32 位 RISC-V 单核处理器，主频高达 160MHz                  |
| Flash            | 4MB                                                                |
| SRAM             | 400KB                                                              |
| ROM              | 384KB                                                              |
| RTC SRAM         | 8KB                                                                |
| Wi-Fi            | 2.4 GHz Wi-Fi (支持 20/40MHz 频宽，802.11 b/g/n, 速率高达 150Mbps) |
| 输入电压         | 5V@500mA                                                           |
| 人机交互         | 可编程物理按键 x 1，复位调试按键 x 1，可编程 RGB LED (SK6812) x 1  |
| USB 接口         | USB Type-C x1                                                      |
| 天线类型         | 2.4G 3D 天线                                                       |
| 模组外设接口资源 | ADC、GPIO、SPI、UART、I2C、I2S、PWM、RMT、DMA、USB 串口、TWAI      |
| IO 接口 x14      | G0，G1，G3，G4，G5，G6，G7，G8，G9，G10，G18，G19，G21，G22        |
| IO 接口间距      | 2.54mm                                                             |
| 固定螺丝规格     | M2 x 4 沉头内六角机械牙                                            |
| 产品尺寸         | 34.0 x 20.0 x 4.6mm                                                |
| 产品重量         | 3.5g                                                               |
| 包装尺寸         | 138.0 x 93.0 x 5.6mm                                               |
| 毛重             | 9.8g                                                               |

## 操作说明

\#> 进入程序下载模式操作：<br/>1. 断电情况下长按 Stamp-C3U 的中心按钮 (G9)<br/>2. 接入电脑，成功识别端口后，进行程序烧录。<br/>USB CDC 启用：<br/>默认情况下 USB CDC 为未启用状态，C3U 启动的串口输出将通过 UART0 进行输出，若需要通过 USB 进行输出，请在下载程序前，通过 IDE 将其 USB CDC 选项启用。(Arduino 用户可通过**Tools**->**USB CDC on Boot**-**Enabled**启用，IDF 用户请参考 ESP IDF 官方文档。)

### 外壳支持回流焊温度曲线

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/stamp_pico/stamp_pico_11_cn.webp">

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/stamp_c3u/stamp_c3u_sch_01.webp" width="80%">

## 管脚映射

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/stamp_c3u/stamp_c3u_09.webp" width="100%">

### SK6812，Button

| ESP32-C3 | G2  | G9  |
| -------- | --- | --- |
| SK6812   | DI  | /   |
| Button   | /   | SW  |

## 尺寸图

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/stamp_c3u/stamp_c3&c3u_size_01.webp" width="100%">

## 结构文件

- [Stamp-C3U Mate 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/K122_Stamp-C3U_Mate/Structures)

## PCB

- [LCEDA Stamp-C3U Component](https://lceda.cn/component/6c5b322e8ed848f9874383222600f34e)

## 数据手册

- [ESP32-C3](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/525/esp32-c3_datasheet_cn.pdf)

## 软件开发

### ESP-IDF

- [Stamp-C3U RGB LED 使用示例](https://github.com/m5stack/STAMP-C3/tree/master/idf/RGB_LED_Control)

## 相关视频

<video width="500" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Core/STAMP_C3U_VIDEO_01.mp4" type="video/mp4">
</video>

## 产品对比

C3U 与 C3 不同的地方是：STAMP-C3U 取消了 USB 下载芯片改用了 ESP32-C3 内置的 USB Serial 进行程序下载。

| 型号      | 主控     | IO 数量 | 按键 IO | USB 下载芯片 | USB 接口功能                 |
| --------- | -------- | ------- | ------- | ------------ | ---------------------------- |
| STAMP-C3  | ESP32-C3 | 13      | G3      | CH9102       | Download / Serial            |
| STAMP-C3U | ESP32-C3 | 14      | G9      | /            | Download / JTAG / CDC Serial |

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/stamp/对比.png" width="80%">
