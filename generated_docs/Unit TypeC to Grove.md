# Unit TypeC to Grove 原理图描述

---

## 原理图分析

以下是基于 M5Stack Unit TypeC to Grove (SKU: U151) 原理图的详细技术描述：

### 1. 主要接口与组件
电路主要由以下连接器组成：
*   **USB Type-C 接口**：作为主要的电源输入端，用于接收外部 5V 电源。
*   **Grove 接口 (HY2.0-4P) x 3**：
    *   **INPUT CH (信号输入)**：用于连接主控设备（如 M5Core），仅用于接收控制信号。
    *   **OUTPUT CH1 & OUTPUT CH2 (信号与电源输出)**：用于连接下游高功耗外设（如 LED 灯带、舵机等），提供信号与增强电源。

### 2. 电源管理与注入电路
该电路的核心功能是电源注入（Power Injection），其电源路径设计如下：
*   **输入端配置**：USB Type-C 接口的 VBUS 引脚接入 5V 电源，GND 引脚接入公共地。
*   **CC 配置通道**：Type-C 接口的 CC1 和 CC2 引脚分别通过 5.1kΩ 下拉电阻连接至 GND。此配置将设备标识为从机（Sink）或受电端，从而向供电设备（Source）请求标准的 5V 供电输出。
*   **电源分配**：
    *   来自 Type-C 的 5V (VBUS) 直接并联连接至两个输出接口（OUTPUT CH1 和 OUTPUT CH2）的第 2 脚 (VCC/Red)。
    *   来自 Type-C 的 GND 直接并联连接至两个输出接口的第 1 脚 (GND/Black)。
*   **电源隔离设计**：输入接口（INPUT CH）的第 2 脚 (VCC) 和第 1 脚 (GND) 在 PCB 上处于悬空（NC, Not Connected）状态。此设计实现了电气隔离，防止 Type-C 引入的大电流或电压波动反向灌入主控端，保护主控器的电源管理模块。

### 3. 信号路由逻辑
电路采用无源信号透传设计，信号路径如下：
*   **信号线 S1 (Pin 4, White)**：INPUT CH 的第 4 脚直接物理连接至 OUTPUT CH1 和 OUTPUT CH2 的第 4 脚。
*   **信号线 S2 (Pin 3, Yellow)**：INPUT CH 的第 3 脚直接物理连接至 OUTPUT CH1 和 OUTPUT CH2 的第 3 脚。
*   **拓扑结构**：信号线形成“一进两出”的总线式结构，INPUT 端的控制信号（如 GPIO、I2C SDA/SCL 等）被无损分发至两个 OUTPUT 端口，且不经过任何电平转换或逻辑门芯片。

### 4. 电路连接关系总结
*   **USB Type-C**：
    *   VBUS -> OUTPUT CH1 Pin 2, OUTPUT CH2 Pin 2
    *   GND -> OUTPUT CH1 Pin 1, OUTPUT CH2 Pin 1, R_CC1, R_CC2
*   **INPUT CH (HY2.0-4P)**：
    *   Pin 1 (GND): NC (不连接)
    *   Pin 2 (VCC): NC (不连接)
    *   Pin 3 (S2): -> OUTPUT CH1 Pin 3, OUTPUT CH2 Pin 3
    *   Pin 4 (S1): -> OUTPUT CH1 Pin 4, OUTPUT CH2 Pin 4
*   **OUTPUT CH1 & CH2 (HY2.0-4P)**：
    *   Pin 1 (GND): <- Type-C GND
    *   Pin 2 (VCC): <- Type-C VBUS (5V)
    *   Pin 3 (S2): <- INPUT CH Pin 3
    *   Pin 4 (S1): <- INPUT CH Pin 4

### 5. 电路特性
*   **大电流支持**：电源走线直接将 Type-C 输入与 Grove 输出端相连，设计上支持 USB Type-C 标准下的 5V 供电（通常支持最高 3A 电流），解决了传统 Grove 接口通过主控板供电能力不足的问题。
*   **混合架构**：该原理图展示了一个混合架构：电源部分为外部有源注入，信号部分为内部无源直通。

---

## 补充信息

基于提供的原始文档，对原理图的技术描述补充如下：

### 1. 电气规格确认
*   **额定电流负载**：文档确认了电路的电源注入路径（从 USB Type-C VBUS 到 Grove OUTPUT VCC）具备 **MAX 5V@3A** 的电流承载能力。这表明原理图对应的 PCB 布局中，电源主干走线宽度设计符合 3A 大电流通流标准，且 Type-C 连接器选型支持该电流等级。

### 2. 系统逻辑定义
*   **端口角色分工**：文档在系统层面明确了各 Grove 接口的逻辑角色。INPUT 接口被严格定义为 **“信号来源” (Signal Source)**，不参与供电回路；而两个 OUTPUT 接口被定义为 **“合并端口” (Merged Ports)**，负责将输入的信号与注入的 5V 电源合并后输出。这一定义进一步印证了电路设计中 INPUT 端 VCC/GND 悬空（NC）是为了彻底阻断电源反向灌入信号源设备（主控）。

---

*该文档由 AI 自动生成，生成时间: 2026-01-07 00:42:26*
