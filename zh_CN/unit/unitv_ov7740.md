# UnitV-OV7740

<span class="product-sku">SKU:U078-C</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1055/U078-C_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/unitv_ov7740/unitv_ov7740_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/unitv_ov7740/unitv_ov7740_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1055/U078-C_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/unitv_ov7740/unitv_ov7740_06.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/unitv_ov7740/unitv_ov7740_07.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/unitv_ov7740/unitv_ov7740_08.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/unitv_ov7740/unitv_ov7740_10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1055/U078-C-weight.jpg">
</PictureViewer>

## 描述

**UnitV-OV7740**是一款功能强大的 AI 视觉处理摄像头单元，搭载 Kendryte K210 芯片，集成了双核 64 位 RISC-V CPU 以及神经网络处理器边缘计算片上系统。

该摄像头体积小巧，便于嵌入各类设备，拥有出色的机器视觉处理能力。它支持多种图像识别功能，例如能够实时获取被检测目标的大小、坐标以及种类等信息，并且在低功耗状态下也能进行卷积神经网络计算，为用户提供了零门槛的机器视觉嵌入式解决方案。

在开发环境方面，它支持 MicroPython，这使得项目开发时的程序代码更加精简。其搭载的 OV7740 图像传感器，使其成为机器视觉项目的理想之选。

从硬件配置来看，机身设有两个可编程按键，正面配备一颗 RGB LED 指示灯，便于进行状态显示。底部提供一个兼容 HY2.0 x 4P 接口和一个 TYPE-C 接口，方便与主控设备连接。此外，还支持 microSD 扩展内存，方便调用相关素材及模型文件。

## 产品特性

- 双核 64-bit RISC-V RV64IMAFDC (RV64GC) CPU / 400Mhz (Normal)
- 双精度 FPU
- 8MiB 64bit 片上 SRAM
- 神经网络处理器 (KPU) / 0.8Tops
- 可编程 I/O 阵列 (FPIOA)
- AES，SHA256 加速器
- 直接内存存取控制器 (DMAC)
- 支持 MicroPython
- 固件加密支持
- 板载硬件资源:
  - Flash: 16M
  - Camera :OV7740
  - 按键: button \* 2
  - 状态灯: WS2812 LED
  - 拓展卡接口: TF card/microSD
  - 接口: HY2.0/compatible GROVE

## 包装内容

- 1 x UnitV-OV7740
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 物体检测 / 分类
- 实时获取目标的大小和坐标
- 实时获取检测到的目标类型
- 形状识别
- 视频录制

## 规格参数

| 规格                 | 参数                                                         |
| -------------------- | ------------------------------------------------------------ |
| Kendryte K210        | 双核 64-bit RISC-V RV64IMAFDC (RV64GC) CPU / 400Mhz (Normal) |
| SRAM                 | 8MiB                                                         |
| Flash                | 16M                                                          |
| 输入电压             | 5V @ 500mA                                                   |
| KPU 神经网络参数大小 | 5.5MiB-5.9MiB                                                |
| 接口                 | Type-C x 1，HY2.0-4P (I2C+I/O+UART) x 1                      |
| RGB LED              | WS2812 x 1                                                   |
| 按键                 | 自定义按键 x 2                                               |
| 摄像头               | OV7740 (30W pixels)                                          |
| FOV                  | 65°                                                          |
| 外部存储             | TF Card/microSD                                              |
| 产品尺寸             | 40 x 24 x 12.7mm                                             |
| 产品重量             | 8.4g                                                         |
| 包装尺寸             | 54.0 x 37.0 x 15.0mm                                         |
| 毛重                 | 14.5g                                                        |
| 外壳材质             | Plastic (PC)                                                 |

## 操作说明

### KENDRYTE K210

Kendryte K210 是集成机器视觉能力的系统级芯片 (SoC)。使用台积电 (TSMC) 超低功耗的 28nm 制程，具有双核 64 位处理器，拥有较好的功耗性能，稳定性与可靠性。该方案力求零门槛开发，可在最短时效部署于用户的产品中，赋予人工智能应用.

- 具备机器视觉能力
- 更好的低功耗视觉处理速度与准确率
- 具备卷积人工神经网络硬件加速器 KPU，可高性能进行卷积人工神经网络运算
- TSMC 28nm 制程，温度范围 - 40°C ~ 125°C，稳定可靠
- 支持固件加密，难以使用普通方法破解
- 独特的可编程 IO 阵列，使产品设计更加灵活
- 低电压，与相同处理能力的系统相比具有更低功耗
- 3.3V/1.8V 双电压支持，无需电平转换，节约成本

本产品搭载基于 RISC-V ISA 的双核心 64 位的高性能低功耗 CPU，具备以下特性

- 核心数量：双核处理器
- 处理器位宽: 64-bit CPU 400MHz
- 标称频率: 400MHz
- 指令集扩展: IMAFDC
- 浮点处理单元 (FPU) : 双精度
- 平台中断管理: PLIC
- 本地中断管理: CLINT
- 指令缓存: 32KiB x 2
- 数据缓存: 32KiB x 2
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
- 电源:- 内核：1.5VDC±5％- 模拟：3.3V±5％ - I / O:1.7~3.47V
- 温度范围:- 工作:-30°C 至 70°C - 稳定图像：0°C 至 50°C
- 输出格式: - 8/10 位原始 RGB 数据 - 8 位 YUV
- 镜头尺寸：1/5"
- 输入时钟频率：6~27 MHz
- 灵敏度：6800 mV / (Lux-sec)
- 最大曝光间隔：502 x tROW
- 像素尺寸：4.2μm×4.2μm
- 图像面积：2755.2μm×2049.6μm

### SD 卡测试

Unit V 目前并不能识别所有类型的 microSD 卡，我们对一些常见的 microSD 卡进行了测试，测试结果如下.

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/unitv_ov7740/unitv_ov7740_11.webp" width="40%" height="40%"><br>

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

<!--## 原理图 暂时不开源 -->

## 管脚映射

### UnitV-OV7740

| UnitV    | G8      | G19      | G18      | G34，G35  |
| -------- | ------- | -------- | -------- | --------- |
| Hardware | RGB LED | Button A | Button B |           |
| HY2.0-4P |         |          |          | Interface |

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/unitv_ov7740/unitv_ov7740_12.webp" width="30%">

## 尺寸图

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1055/U078-C_Model_Size_page_01.png" width="75%">

## 数据手册

- [K210 Datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/kendryte_datasheet.pdf)
- [OV7740 Datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/stickv/OV7740_datasheet.pdf)

## 软件开发

### 快速上手

选择你想使用的开发平台，查看对应的教程 & 快速上手。

- [UnitV-OV7740 V-Function Guide](/zh_CN/guide/ai_camera/unitv/v_function)
- [UnitV-OV7740 V-Training Guide](/zh_CN/guide/ai_camera/unitv/v-training)
- [UnitV-OV7740 Maixpy Guide](/zh_CN/guide/ai_camera/unitv/maixpy)

### Arduino

- [UnitV-OV7740 Arduino 使用教程](/zh_CN/arduino/projects/unit/unitv)

### UiFlow1

- [UnitV-OV7740 UiFlow1 文档](/zh_CN/uiflow/blockly/unit/unitv)

### USB 驱动

?> 常见问题 | UnitV 在部分系统中，可能无法免驱工作，用户可以通过手动安装 FTDI VCP 驱动修复该问题。以 win10 环境为例，下载匹配操作系统的驱动文件，并解压，通过设备管理器进行安装。(注：某些系统环境下，需要安装两次，驱动才会生效，未识别的设备名通常为**M5Stack**或**USB Serial**，Windows 推荐使用驱动文件在设备管理器直接进行安装 (自定义更新)，可执行文件安装方式可能无法正常工作)。

[FTDI VCP 驱动下载页面：](https://ftdichip.com/drivers/vcp-drivers/)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1040/U082-X-USB-note-02.png" width="100%">

**安装方法：**

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1040/U082-X-USB-note-01.png" width="100%">

### 其他

- [UnitV-OV7740 with RoverC Track Ball Example](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/App/UnitV/track_ball)

## 相关视频

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Unit/unitV.mp4" type="video/mp4">
</video>

## 产品对比

如需对比 UnitV 系列产品信息，可访问[产品选型表](/zh_CN/products_selector/unitv_compare?select=U078-C)，勾选目标产品即可获取对比结果。选型表涵盖核心参数、功能特性等关键信息，支持多产品同步比对。
