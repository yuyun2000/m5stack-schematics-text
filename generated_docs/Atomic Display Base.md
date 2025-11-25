# Atomic Display Base 原理图描述

---

## 原理图分析

好的，以下是基于 M5Stack Atomic Display Base (SKU:A115) 原理图的硬件结构与电路连接描述。

### 1. 总体概述
Atomic Display Base 是一款将 ATOM 系列主控的信号转换为标准高清多媒体信号（HDMI）输出的底座。其核心架构是利用 FPGA (Gowin GW1NR-9C) 接收来自 ATOM 主控的 SPI 数据，在内部生成并驱动 RGB 视频信号，再通过一颗 RGB 转 HDMI 芯片 (LT8618SX) 将其编码为 TMDS 差分信号，最终通过 HDMI 接口输出。

### 2. 核心芯片及其电路
#### 2.1. FPGA (U1: Gowin GW1NR-9C)
*   **功能**: 作为系统的逻辑核心，负责与 ATOM 主控通讯，生成视频时序（HSYNC, VSYNC, PCLK）和 24 位 RGB 数据，并通过 I2C 接口配置下游的 HDMI 转换芯片。
*   **供电**:
    *   **VCC (1.2V)**: 内核电压，由 5V 输入经 Buck 转换器 U4 (SY8089) 降压提供。
    *   **VCCO0 (3.3V)**: Bank 0 的 I/O 电压，由 3.3V 电源轨直接供电，用于与 ATOM 主控的 SPI 接口进行电平匹配。
    *   **VCCO1, VCCO2, VCCO3 (1.8V)**: Bank 1, 2, 3 的 I/O 电压，统一由 1.8V 电源轨供电，用于驱动与 LT8618SX 连接的 RGB 信号和 I2C 信号。
    *   **VCCIO (1.8V)**: Bank 1, 2, 3 的公共 I/O 电源，由 1.8V 电源轨供电。
*   **时钟**: FPGA 的主时钟由一个外部 27MHz 无源晶振 Y1 提供，连接至 FPGA 的 OSCI (G11) 和 OSCO (H11) 引脚。
*   **与 ATOM 主控的通讯**:
    *   通过 SPI 接口与 ATOM 主控通讯，用于接收图像数据或控制指令。
    *   `ATOM_G19` -> `SPI_SCK` (FPGA Pin P9, SCLK)
    *   `ATOM_G22` -> `SPI_MOSI` (FPGA Pin T9, MOSI)
    *   `ATOM_G33` -> `SPI_MISO` (FPGA Pin R8, MISO)
    *   `ATOM_G23` -> `SPI_CS` (FPGA Pin T8, SCSN)
    *   此外，`ATOM_G21` 和 `ATOM_G25` 也连接到 FPGA 的 I/O 引脚（分别为 Pin T7 和 Pin R7），用作通用 I/O。

#### 2.2. RGB 转 HDMI 芯片 (U2: LT8618SX)
*   **功能**: 将 FPGA 输出的并行 24 位 RGB 信号、时钟及同步信号编码为符合 HDMI 规范的 TMDS 差分信号。
*   **供电**:
    *   **PVDD (3.3V)**: I/O 电压，由 3.3V 电源轨供电。
    *   **DVDD, AVDD (1.8V)**: 数字和模拟部分的核心电压，由 1.8V 电源轨供电。
    *   **CVDD (1.2V)**: 芯片内部核心电压，通过芯片内部的 LDO 从其他电源域生成，其输出引脚 CVDD12 通过电容 C23 滤波至地。
*   **控制接口**: 芯片通过 I2C 总线接受 FPGA 的配置。
    *   `LT_SCL` (Pin 41) 连接至 FPGA 的 Pin C4。
    *   `LT_SDA` (Pin 42) 连接至 FPGA 的 Pin D4。
    *   该 I2C 总线上接有上拉电阻 R5 和 R6 到 1.8V 电源。
*   **复位**: `RESETB` 引脚 (Pin 43) 通过电阻 R7 上拉至 1.8V，确保正常工作时芯片处于非复位状态。

### 3. 信号路径与连接关系
*   **FPGA 到 LT8618SX 的视频信号路径**: FPGA 的 Bank 1 和 Bank 2 作为视频数据输出口，将并行 RGB 信号及同步信号传输给 LT8618SX。
    *   **数据信号**: `B_OUT[0:7]`, `G_OUT[0:7]`, `R_OUT[0:7]` (共 24 路) 分别连接至 LT8618SX 的 `B[0:7]`, `G[0:7]`, `R[0:7]` 输入引脚。
    *   **同步信号**: FPGA 输出的 `PCLK_OUT`, `VSYNC_OUT`, `HSYNC_OUT`, `DE_OUT` 分别连接至 LT8618SX 的 `PCLK`, `VSYNC`, `HSYNC`, `DE` 输入引脚。
*   **LT8618SX 到 HDMI 接口的信号路径**: LT8618SX 将编码后的 TMDS 差分信号对 `TXC+/-`, `TX0+/-`, `TX1+/-`, `TX2+/-` 直接输出到 HDMI-A 型接口 J3 的相应引脚。这些高速差分线路上串联了 ESD 保护器件 D2 (GESD0504V) 以防止静电损伤。

### 4. 电源管理系统
*   **电源输入**: 系统接受来自 ATOM 接口 J2 的 5V 电源，或通过板载 USB-C 接口 J1 的 VBUS 提供 5V 电源。二极管 D1 (SS14) 起到电源路径选择和防反灌的作用。
*   **电压调节**:
    *   **5V 转 3.3V**: LDO 稳压器 U3 (ME6211C33M5G-N) 将 5V 输入转换为 3.3V，为 FPGA 的 VCCO0 和 LT8618SX 的 PVDD 供电。
    *   **5V 转 1.2V**: 同步 Buck 转换器 U4 (SY8089) 将 5V 输入高效降压至 1.2V，专用于为 FPGA 的内核 (VCC) 供电。其外围包含电感 L2 和滤波电容。
    *   **3.3V 转 1.8V**: LDO 稳压器 U5 (SGM2036-ADJ) 将 3.3V_IN (来自 U3 输出) 转换为 1.8V，为 FPGA 的 VCCO1/2/3 和 VCCIO，以及 LT8618SX 的 DVDD/AVDD 供电。其输出电压由电阻 R11 和 R12 构成的分压网络设定。
*   **电源滤波**: 在 5V, 3.3V, 1.8V, 1.2V 各主要电源轨上均布置了多个不同容值的陶瓷电容（如 C1-C6, C15-C16, C19-C22 等）进行去耦和滤波，以确保电源的稳定性和信号完整性。

### 5. 接口与连接器
*   **ATOM 接口 (J2)**: 一个 2x5 Pin 的排母连接器，用于连接 ATOM 主控。
    *   **电源**: Pin 1 (5V), Pin 6 (GND)。
    *   **信号**: Pin 3 (G19), Pin 4 (G21), Pin 5 (G22), Pin 8 (G23), Pin 9 (G25), Pin 10 (G33)。
*   **USB-C 接口 (J1)**: 仅用作 5V 电源输入，连接了 VBUS 和 GND 引脚。
*   **HDMI 输出接口 (J3)**: 标准 HDMI-A 型母座。
    *   **TMDS 信号**: Pin 1/3 (TMDS Data2), Pin 4/6 (TMDS Data1), Pin 7/9 (TMDS Data0), Pin 10/12 (TMDS Clock)。
    *   **控制/辅助信号**: Pin 13 (CEC), Pin 15 (SCL), Pin 16 (SDA), Pin 19 (Hot Plug Detect)。
    *   **电源**: Pin 18 (+5V Power)。
    *   CEC 和 HPD 信号线也经过 ESD 保护器件 D2。

---

## 补充信息

好的，基于对原理图的进一步分析，以下是针对 Atomic Display Base 电路设计的补充细节：

### 1. 电路设计细节
*   **FPGA 启动与配置**: 原理图显示 FPGA (U1) 的 `PROGRAMN` 引脚通过电阻 R3 上拉至 VCCO0 (3.3V)，这使得 FPGA 在上电后默认从内部闪存加载配置。`JTAGENB` 引脚通过 R4 下拉至地，默认禁用了 JTAG 调试接口。`DONE` 引脚通过 R9 上拉至 VCCO0 (3.3V)，用于指示 FPGA 已成功完成配置。
*   **音频信号处理**: HDMI 转换芯片 LT8618SX (U2) 的 `SPDIF` 音频输入引脚被直接接地。这表明该设计在硬件上没有为独立的数字音频输入（如 SPDIF）预留通道，专注于视频信号的转换。如果需要传输音频，必须由 FPGA 内部生成并嵌入到符合 HDMI 规范的视频数据流中。
*   **电源稳压器使能逻辑**:
    *   3.3V LDO (U3) 和 1.2V Buck (U4) 的使能引脚（EN）均连接至 5V 输入端，这意味着只要有 5V 电源输入，这两个稳压器就会立即工作。
    *   1.8V LDO (U5) 的使能引脚连接至其 3.3V 输入端，因此它会在 3.3V 电源轨稳定后启动。
    *   这种设计构成了一个简单的、无时序控制的“始终开启”（Always-on）的电源架构。

### 2. 电源系统补充
*   **电源指示灯**: 电路板上包含一个绿色 LED (LED1)，它通过一个限流电阻 R2 连接到 3.3V 电源轨。当底座上电且 3.3V 电源正常工作时，该 LED 会点亮，作为电源状态的直观指示。
*   **1.8V 电压调节反馈**: 用于生成 1.8V 电压的可调 LDO (U5, SGM2036-ADJ) 使用了一个由 R11 (10kΩ) 和 R12 (8kΩ) 组成的外部电阻分压网络。该网络连接到其反馈（ADJ）引脚，精确地将其输出电压设定为 1.8V。

### 3. 接口与保护补充
*   **热插拔检测 (HPD)**: HDMI 接口 (J3) 的 `Hot Plug Detect` (Pin 19) 信号线直接连接到 LT8618SX 芯片的 `HPDIN` 引脚。这是一个关键的反馈机制，它允许 LT8618SX 感知到显示设备（Sink）是否已连接并上电，从而触发 HDMI 输出。
*   **HDMI 5V 电源输出**: HDMI 接口的 Pin 18 (+5V Power) 直接取自板上的主 5V 电源轨。该引脚用于向所连接的显示设备提供少量电源，或作为其内部逻辑的电源存在信号。
*   **ESD 保护**: 除了 TMDS 高速差分对外，HDMI 接口的控制信号线（如 SCL, SDA, CEC）和 HPD 信号线同样通过 ESD 保护二极管阵列（D2, D3）连接，以增强接口的抗静电能力。

---

*该文档由 AI 自动生成，生成时间: 2025-11-17 18:48:27*
