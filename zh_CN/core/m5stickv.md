# StickV

<span class="product-sku">SKU:K027</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickv/m5stickv_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickv/m5stickv_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickv/m5stickv_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickv/m5stickv_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickv/m5stickv_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickv/m5stickv_06.webp">
</PictureViewer>

## 描述

**StickV** 是一款搭载 Kendryte K210 的 AIOT （AI + IOT） 摄像头，它集成了双核 64 位 RISC-V CPU 以及神经网络处理器边缘计算片上系统 （SoC） 。

StickV AI 摄像头具备机器视觉能力，配备了 OmniVision OV7740 图像传感器，采用 OmniPixel®3-HS 技术，拥有相较于同类产品更出色的低光灵敏度。它支持多种视觉识别功能，比如能够实时获取被检测目标的大小与坐标，还能实时获取被检测目标的种类等。并且，该摄像头能够在低功耗的情况下进行卷积神经网络计算，所以 StickV 是一个优秀的零门槛机器视觉嵌入式解决方案。

此外，它支持 MicroPython 开发环境，这使得在使用 StickV 进行项目开发时，程序代码会更加简洁精炼。

## 产品特性

- 双核 64-bit RISC-V RV64IMAFDC (RV64GC) CPU / 400Mhz (Normal)
- 双精度 FPU
- 神经网络处理器 (KPU) / 0.8Tops
- 可编程 IO 阵列 (FPIOA)
- 双硬件 512 点 16 位复数 FFT
- SPI，I2C，UART，I2S，RTC，PWM，定时器支持
- AES，SHA256 加速器
- 直接内存存取控制器 (DMAC)
- 支持 Micropython
- 固件加密支持
- 开发平台
  - PlatformIO

## 包装内容

- 1 x StickV
- 1 x USB Type-C(100cm)
- 1 x 支架
- 1 x 六角扳手

## 应用场景

- 面部识别 / 检测
- 物体检测 / 分类
- 实时获取目标的大小和坐标
- 实时获取检测到的目标类型
- 形状识别
- 视频 / 显示
- 游戏模拟器

## 规格参数

| 规格                 | 参数                                                |
| -------------------- | --------------------------------------------------- |
| SoC                  | Kendryte K210@双核 64 位 RISC-V RV64GC, 主频 400MHz |
| SRAM                 | 8MB                                                 |
| Flash                | 16MB                                                |
| 输入电压             | 5V@500mA                                            |
| KPU 神经网络参数大小 | 5.5MiB - 5.9MiB                                     |
| 主机接口             | USB Type-C x 1，HY2.0-4P (I2C+I/O+UART) x 1         |
| RGB LED              | RGBW x 1                                            |
| 按键                 | 自定义按键 x 2                                      |
| IPS 屏幕             | 1.14 TFT，135 x 240，ST7789                         |
| 摄像头               | OV7740 (0.3MP)                                      |
| FOV                  | 55°                                                 |
| PMU                  | AXP192                                              |
| 锂电池               | 200mAh                                              |
| 外部存储             | TF-card (microSD)                                   |
| MEMS 六轴传感器      | MPU6886                                             |
| 外壳材质             | Plastic ( PC )                                      |
| 产品尺寸             | 48.0 x 24.0 x 22.0mm                                |
| 产品重量             | 23.0g                                               |
| 包装尺寸             | 144.0 x 44.0 x 43.0mm                               |
| 毛重                 | 82.0g                                               |

## 操作说明

### 开关机操作

**开机**: 按复位按键，持续至少 2 秒<br/>**关机**: 按复位按键，持续至少 6 秒

### TF-card (microSD) 测试

M5StickV 目前并不能识别所有类型的 TF-card (microSD)，我们对一些常见的 TF-card 进行了测试，测试结果如下。

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickv/m5stickv_07.webp" width="30%" height="30%">

| 品牌     | 内存 | 类型 | 传输速度 | 分区格式 | 测试结果  |
| -------- | ---- | ---- | -------- | -------- | --------- |
| Kingston | 8G   | HC   | Class4   | FAT32    | OK        |
| Kingston | 16G  | HC   | Class10  | FAT32    | OK        |
| Kingston | 32G  | HC   | Class10  | FAT32    | NO        |
| Kingston | 64G  | XC   | Class10  | exFAT    | OK        |
| SanDisk  | 16G  | HC   | Class10  | FAT32    | OK        |
| SanDisk  | 32G  | HC   | Class10  | FAT32    | OK        |
| SanDisk  | 64G  | XC   | Class10  | /        | NO        |
| SanDisk  | 128G | XC   | Class10  | /        | NO        |
| XIAKE    | 16G  | HC   | Class10  | FAT32    | OK (紫色) |
| XIAKE    | 32G  | HC   | Class10  | FAT32    | OK        |
| XIAKE    | 64G  | XC   | Class10  | /        | NO        |
| TURYE    | 32G  | HC   | Class10  | /        | NO        |

### KENDRYTE K210

Kendryte K210 是集成机器视觉能力的系统级芯片 (SoC)。使用台积电 (TSMC) 超低功耗的 28nm 制程，具有双核 64 位处理器，拥有较好的功耗性能，稳定性与可靠性。该方案力求零门槛开发，可在最短时效部署于用户的产品中，赋予产品人工智能。<br/><br/>

- 具备机器视觉能力
- 更好的低功耗视觉处理速度与准确率
- 具备卷积人工神经网络硬件加速器 KPU，可高性能进行卷积人工神经网络运算
- TSMC 28nm 制程，温度范围 - 40°C ~ 125°C，稳定可靠
- 支持固件加密，难以使用普通方法破解
- 独特的可编程 IO 阵列，使产品设计更加灵活
- 低电压，与相同处理能力的系统相比具有更低功耗
- 3.3V/1.8V 双电压支持，无需电平转换，节约成本

### CPU

本芯片搭载基于 RISC-V ISA 的双核心 64 位的高性能低功耗 CPU，具备以下特性：

- 核心数量： 双核处理器
- 处理器位宽： 64-bit CPU 400MHz
- 标称频率： 400MHz
- 指令集扩展： IMAFDC
- 浮点处理单元 (FPU): 双精度
- 平台中断管理： PLIC
- 本地中断管理： CLINT
- 指令缓存： 32KiB x 2
- 数据缓存： 32KiB x 2
- 片上 SRAM: 8MiB

### OV7740

- 支持输出格式：RAW RGB 和 YUV
- 支持图像尺寸：VGA，QVGA，CIF 或其他更小尺寸
- 支持太阳黑子消除
- 支持内部和外部帧同步
- 标准 SCCB 串行接口
- 数字视频端口 (DVP) 并行输出接口
- 嵌入式一次性可编程 (OTP) 存储器
- 片上锁相环 (PLL)
- 用于内核的嵌入式 1.5 V 稳压器
- 阵列尺寸：656 x 488
- 电源： - 内核：1.5VDC±5％ - 模拟：3.3V±5％ - I / O:1.7~3.47V
- 温度范围： - 工作：-30°C 至 70°C - 稳定图像：0°C 至 50°C
- 输出格式： - 8/10 位原始 RGB 数据 - 8 位 YUV
- 镜头尺寸：1/5"
- 输入时钟频率：6~27 MHz
- 最大图像传输速率：VGA (640x480):60 fps - QVGA (320 x 240):120 fp
- 灵敏度：6800 mV /(Lux-sec)
- 最大曝光间隔：502 x tROW
- 像素尺寸：4.2μm×4.2μm
- 图像面积：2755.2μm×2049.6μm
- 封装 / 管芯尺寸： - CSP3:4185μm×4345 μm-COB:4200μm×4360μm

### MAX98357

- 单电源工作 (2.5V 至 5.5V)
- 3.2W 输出功率：4Ω，5V
- 2.4mA 静态电流
- 92% 效率 (RL = 8Ω，POUT = 1W)
- 22.8µVRMS 输出噪声 (AV = 15dB)
- 1kHz 时，0.015% THD+N
- 无需 MCLK
- 8kHz 至 96kHz 采样速率
- 支持左声道、右声道以及 (左声道 / 2 + 右声道 / 2) 输出
- 成熟的边沿速率控制可使 D 类放大器输出无需滤波
- 1kHz 下，具有 77dB PSRR
- 低 RF 敏感度，可抑制 GSM 发射的 TDMA 噪声
- 喀嗒声抑制电路

### AXP192

- 可配置的智能电源选择系统
- 自适应 USB 或 AC 适配器输入的电流和电压限制
- 内部理想二极管的电阻低于 100mΩ

### MPU6886

#### 陀螺仪功能

- 数字输出 X，Y 和 Z 轴角速率传感器 (陀螺仪)，用户可编程满量程范围为 ±250 dps，±500 dps，±1000 dps 和 ±2000 dps，集成 16- 位 ADC
- 数字可编程低通滤波器
- 低功率陀螺仪操作
- 工厂校准的灵敏度比例因子
- 镜头尺寸：1/5"
- 自我测试

#### 加速度计功能

- 数字输出 X，Y 和 Z 轴加速度计，可编程满量程范围为 ±2g，±4g，±8g 和 ±16g，集成 16 位 ADC
- 用户可编程中断
- 唤醒动作中断，用于应用处理器的低功耗操作
- 自我测试

#### SPI/I2C 双通信模式

\#> 注意事项： | 当前 M5Stack 发行的 M5StickV 存在两种版本，用户编程使用时需根据其对应的引脚映射进行不同的配置，具体区别如下。

- I2C 单模式 (蓝色 PCB) 版本的 M5StickV 电路设计中，MPU6886 仅支持用户配置其通信模式为 I2C，其引脚映射为 SCL-28，SDA-29.

- SPI/I2C 双模式 (黑色 PCB) 版本的 M5StickV 电路设计中，MPU6886 支持用户配置其通信模式为 SPI 或 I2C，其引脚映射为 SCL-26，SDA-27 使用时，可通过切换 CS 引脚电平来切换模式 (高电平 1 为 I2C 模式，低电平 0 为 SPI 模式)

- 具体引脚映射如下图所示：

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickv/m5stickv_sch_01.webp" width="80%">

## 原理图

- [StickV 原理图PDF](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/schematic/Core/k210_CAMv2.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1056/k210_CAMv2_page_01.png">
</SchViewer>

## 数据手册

- [MPU6886](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/MPU-6886-000193%2Bv1.1_GHIC_en.pdf)
- [SH200Q](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/SH200Q_en.pdf)
- [OV7740](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/stickv/OV7740_datasheet.pdf)

## 软件开发

### 快速上手

- [V-Function](/zh_CN/guide/ai_camera/unitv/v_function)
- [V-Training](/zh_CN/guide/ai_camera/unitv/v-training)
- [Maixpy](/zh_CN/guide/ai_camera/m5stickv/maixpy)

### USB 驱动

?> 波特率限制 | 在进行设备程序下载操作时，推荐选用以下串口波特率选项。若采用其他速度，可能导致程序无法正常下载。<br/>**1500000 bps** / **750000 bps** / **500000 bps** / **250000 bps** / **115200 bps**

\#> 将设备连接至 PC，打开设备管理器为设备安装[FTDI 驱动](https://ftdichip.com/drivers/vcp-drivers/)。以 win10 环境为例，下载匹配操作系统的驱动文件，并解压，通过设备管理器进行安装。(注：某些系统环境下，需要安装两次，驱动才会生效，未识别的设备名通常为**M5Stack**或**USB Serial**，Windows 推荐使用驱动文件在设备管理器直接进行安装 (自定义更新)，可执行文件安装方式可能无法正常工作)。[点击此处，前往下载 FTDI 驱动](https://ftdichip.com/drivers/vcp-drivers/)

<div class="product_pic"><img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/ftdi_01.webp"><img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/ftdi_02.webp"><img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/ftdi_03.webp"></div>

### Easyloader

| Easyloader             | 下载链接                                                                                                        | 备注 |
| ---------------------- | --------------------------------------------------------------------------------------------------------------- | ---- |
| StickV Test Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/CORE/EasyLoader_M5StickV_v5.1.2.exe) | /    |

## 相关视频

- 搭载 Maixpy 固件，测试摄像头，屏幕图形显示功能，单击 HOME 键可开关背部补光灯。

<video id="example_video" controls>
  <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Core/M5StickV.mp4" type="video/mp4">
</video>

## 产品对比

如需对比 UnitV 系列产品信息，可访问[产品选型表](/zh_CN/products_selector/unitv_compare?select=K027)，勾选目标产品即可获取对比结果。选型表涵盖核心参数、功能特性等关键信息，支持多产品同步比对。

## 版本变更

| 上市日期 | 产品变动                                                                                   | 备注：                                                                           |
| -------- | ------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------- |
| 2020.4   | 添加支架配件                                                                               | /                                                                                |
| 2020.3   | 电路支持配置 MPU6886 使用 SPI 或 I2C 协议进行通信。I2C 引脚变更 SCL (28=>26)，SDA (29=>27) | 程序上驱动片选引脚 CS 进行模式修改，高电平 1 为 I2C 模式，低电平 0 为 SPI 模式。 |
| 2020.3   | 增加麦克风                                                                                 | /                                                                                |
| 2019.7   | 首次发售                                                                                   | /                                                                                |
