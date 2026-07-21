# Chain RGB

<span class="product-sku">SKU:U218</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1252/U218_Chain_RGB_main_pictures_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1252/U218_Chain_RGB_main_pictures_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1252/U218_Chain_RGB_main_pictures_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1252/U218_Chain_RGB_main_pictures_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1252/U218_Chain_RGB_main_pictures_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1252/U218_Chain_RGB_main_pictures_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1252/U218_Chain_RGB_main_pictures_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1252/U218_Chain_RGB_main_pictures_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1252/U218_Chain_RGB_main_pictures_09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1252/U218_Chain_RGB_main_pictures_10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1252/U218_Chain_RGB_main_pictures_11.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1252/U218_Chain_RGB_main_pictures_weight.webp">
</PictureViewer>

## 描述

Chain RGB 是 M5Stack Chain 系列中的**全彩 LED 点阵显示节点**，核心配备 8×8 像素的 RGB LED 点阵单元，支持**单像素独立控制**、批量像素写入与整屏缓冲区高速刷新，能够流畅呈现细腻的动态灯效与像素动画。在字符显示方面，Chain RGB 内置完整的 ASCII 字符绘制与取模引擎，支持字符串滚动显示，可自由指定颜色，或使用固件内置彩色渐变效果，满足不同场景的视觉表达需求。设备同时提供亮度多级调节、多角度画面旋转等实用功能，适配多样化的安装与观看角度，适用于**彩色像素灯光创作、桌面氛围灯、创意灯光标识、智能设备状态提示**等应用场景。
硬件层面，Chain RGB 搭载 **STM32G031G8U6** 主控芯片，采用 UART 串口级联通信协议，并通过两个 HY2.0-4P 扩展接口，可灵活连接更多 Chain 系列模块，助力构建层次丰富、交互性更强的灯光联动系统。

?> 灯珠亮度 | 长时间高亮度驱动可能导致 LED 损坏，推荐使用 50% 亮度，减少发热和功耗。

## 产品特性

- M5Stack Chain 系列
- 全彩 LED 点阵显示节点
- STM32G031G8U6 核心主控
- 8 x 8 RGB LED 点阵显示单元
- 内置 ASCII 字符取模，支持控制字符绘制
- 支持 RGB565 像素独立控制以及批量写入
- 采用 64 点 RGB565 显存，支持整屏刷新
- 自定义图案、字符串滚动显示，单节点最大支持 32 字符串长度
- 字符串滚动支持固定颜色与彩色渐变效果
- 支持设置画面 0°/90°/180°/270° 旋转
- 采用 UART 串口级联通信协议
- 2 x HY2.0-4P 拓展接口，可拓展 Chain 系列设备

## 包装内容

- 1 x Chain RGB
- 1 x Chain Bridge

## 应用场景

- 像素灯光创作
- 桌面氛围灯
- 创意灯光标识
- 智能设备灯光提示

## 规格参数

| 规格     | 参数                               |
| -------- | ---------------------------------- |
| MCU      | STM32G031G8U6                      |
| 输入电源 | DC 5V                              |
| 通信方式 | UART 115200bps @ 8N1               |
| 接口规格 | 2 x HY2.0-4P                       |
| RGB LED  | 64 x WS2812E                       |
| 颜色格式 | RGB565                             |
| 待机功耗 | DC 5V@13.46mA                      |
| 工作功耗 | DC 5V@127.51mA（最大亮度白色全亮） |
| 工作温度 | 0 ~ 40°C                           |
| 产品尺寸 | 24.0 x 24.0 x 16.0mm                  |
| 产品重量 | 6.5g                               |
| 包装尺寸 | 138.0 x 93.0 x 11.0mm                  |
| 毛重     | 13.5g                               |

## 操作说明

用 Chain Bridge 连接器连接主控 Chain DualKey 和各个 Chain 系列输入设备。连接时需要注意方向，三角箭头从主控 Chain DualKey 指向外侧，如图：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1176/Chain_connect.jpg" width="50%">

## 原理图

- [Chain RGB 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1252/SCH_Chain_RGB_2026_04_02_10_35_51.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1252/SCH_Chain_RGB_2026_04_02_10_35_51_page_01.png">
</SchViewer>

## 管脚映射

### UART

| STM32G031 | PB6  | PB7  | PA2  | PA3  |
| --------- | ---- | ---- | ---- | ---- |
| UART1     | TXD1 | RXD1 |      |      |
| UART2     |      |      | TXD2 | RXD2 |

## 尺寸图

- [Chain RGB 模型尺寸 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1252/U218_Chain_RGB_model_size.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1252/U218_Chain_RGB_model_size_page_01.png" width="100%">

## 软件开发

### Arduino

- [Chain RGB Arduino 上手教程](/zh_CN/arduino/projects/chain/chain_rgb)
- [Chain RGB Arduino 驱动库](https://github.com/m5stack/M5Chain)

### 内置固件

- [Chain RGB 内置固件](https://github.com/m5stack/M5Chain-Series-Internal-FW/tree/main/Chain-RGB)

### 通信协议

- [Chain RGB 通信协议](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1252/M5Stack-Chain-RGB-Protocol-CN.pdf)

<!-- 英文版链接：https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1252/M5Stack-Chain-RGB-Protocol-EN.pdf -->

## 相关视频

- Chain RGB 产品介绍以及功能展示

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1252/U218_Chain_RGB_video_CN.mp4" type="video/mp4"></video>
