# Chain Mono

<span class="product-sku">SKU:U217</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1245/U217_Chain_Mono_main_pictures_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1245/U217_Chain_Mono_main_pictures_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1245/U217_Chain_Mono_main_pictures_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1245/U217_Chain_Mono_main_pictures_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1245/U217_Chain_Mono_main_pictures_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1245/U217_Chain_Mono_main_pictures_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1245/U217_Chain_Mono_main_pictures_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1245/U217_Chain_Mono_main_pictures_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1245/U217_Chain_Mono_main_pictures_09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1245/U217_Chain_Mono_main_pictures_10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1245/U217_Chain_Mono_main_pictures_11.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1245/U217-weight.jpg">
</PictureViewer>

## 描述

Chain Mono 是 M5Stack Chain 系列 LED 显示节点，搭载 8×8 单色 LED 点阵单元。设备支持单像素独立控制、批量像素写入与整屏缓冲区快速刷新，内置 ASCII 字符绘制取模、字符串滚动、亮度调节、多角度画面旋转等功能，可实现多样动态灯光与像素动画效果，适用于像素灯光创作、桌面氛围灯、创意灯光标识、智能设备灯光提示等场景。
Chain Mono 集成 STM32G031G8U6 核心主控，采用 UART 串口级联通信协议，通过两个 HY2.0-4P 拓展接口，可拓展更多 Chain 系列设备，构建更加丰富的交互应用。

## 产品特性

- M5Stack Chain 系列
- STM32G031G8U6 核心主控
- 8 x 8 单色 LED 点阵显示单元
- 内置 ASCII 字符取模，支持控制字符绘制
- 支持像素独立控制以及批量写入
- 采用 8 字节显存，支持整屏刷新
- 自定义图案、字符串滚动显示，单节点最大支持 32 字符串长度
- 支持设置画面 0°/90°/180°/270° 旋转
- 采用 UART 串口级联通信协议
- 2 x HY2.0-4P 拓展接口，可拓展 Chain 系列设备

## 包装内容

- 1 x Chain Mono
- 1 x Chain Bridge

## 应用场景

- 像素灯光创作
- 桌面氛围灯
- 创意灯光标识
- 智能设备灯光提示

## 规格参数

| 规格     | 参数                          |
| -------- | ----------------------------- |
| MCU      | STM32G031G8U6                 |
| 输入电源 | DC 5V                         |
| 通信方式 | UART 115200bps @ 8N1          |
| 接口规格 | 2 x HY2.0-4P                  |
| LED 颜色 | 白色                          |
| 待机功耗 | DC 5V@8.13mA                  |
| 工作功耗 | DC 5V@22.29mA（最大亮度全亮） |
| 工作温度 | 0 ~ 40°C                      |
| 产品尺寸 | 24.0 x 24.0 x 16.0mm          |
| 产品重量 | 6.2g                          |
| 包装尺寸 | 138.0 x 93.0 x 11.0mm         |
| 毛重     | 13.2g                         |

## 操作说明

用 Chain Bridge 连接器连接主控 Chain DualKey 和各个 Chain 系列输入设备。连接时需要注意方向，三角箭头从主控 Chain DualKey 指向外侧，如图：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/Chain_connect.jpg" width="50%">

## 原理图

- [Chain Mono 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1245/SCH_Chain_MONO_SCH_V0.1_2026_01_04_09_51_33.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1245/SCH_Chain_MONO_SCH_V0.1_2026_01_04_09_51_33_page_01.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1245/SCH_Chain_MONO_SCH_V0.1_2026_01_04_09_51_33_page_02.png">
</SchViewer>

## 管脚映射

### UART

| STM32G031 | PB6  | PB7  | PA2  | PA3  |
| --------- | ---- | ---- | ---- | ---- |
| UART1     | TXD1 | RXD1 |      |      |
| UART2     |      |      | TXD2 | RXD2 |

## 尺寸图

- [Chain Mono 模型尺寸 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1245/U217_Chain_Mono_model_size.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1245/U217_Chain_Mono_model_size_page_01.png" width="100%">

## 软件开发

### Arduino

- [Chain Mono Arduino 上手教程](/zh_CN/arduino/projects/chain/chain_mono)
- [Chain Mono Arduino 驱动库](https://github.com/m5stack/M5Chain)

### 内置固件

- [Chain Mono 内置固件](https://github.com/m5stack/M5Chain-Series-Internal-FW/tree/main/Chain-Mono)

### 通信协议

- [Chain Mono 通信协议](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1245/M5Stack-Chain-Mono-Protocol-CN.pdf)

## 相关视频

- Chain Mono 产品介绍以及功能展示

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1245/U217_Chain_Mono_video_CN.mp4" type="video/mp4"></video>