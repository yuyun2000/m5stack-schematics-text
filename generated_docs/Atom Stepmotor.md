# Atom Stepmotor 原理图描述

---

## 原理图分析

以下是 Atom Stepmotor 模块的原理图技术描述：

### 1. 核心驱动电路 (Core Driver Circuit)
*   **驱动芯片**：采用 Texas Instruments DRV8825 步进电机驱动芯片，集成双 H 桥，支持 PWM 微步驱动。
*   **电机连接**：
    *   DRV8825 的输出引脚 `AOUT1`, `AOUT2` 连接至 KF128L 接口的电机 A 相端子。
    *   输出引脚 `BOUT1`, `BOUT2` 连接至 KF128L 接口的电机 B 相端子。
*   **外围组件**：
    *   `CP1`, `CP2` 引脚之间连接电荷泵电容，用于驱动内部高侧 N 沟道 MOSFET。
    *   `V3P3` 引脚连接旁路电容，为内部逻辑提供 3.3V 参考电压。
    *   `ISENA`, `ISENB` 引脚分别通过低阻值采样电阻（Sense Resistor）接地，用于电流检测和 PWM 斩波控制。

### 2. 电源管理系统 (Power Management System)
*   **电源输入**：通过 KF128L 6P 接口的 VIN 和 GND 引脚输入外部直流电源（9V-18V）。
*   **降压转换（DC-DC）**：
    *   输入电压经滤波电容进入 DC-DC 降压芯片（通常为 MP1584 或类似的高效 Buck 转换器）。
    *   该电路包含电感、肖特基二极管和反馈电阻网络，将 9V-18V 的输入电压转换为稳定的 5V 直流电压。
*   **系统供电**：
    *   生成的 5V 电压连接至 Atom 接口的 `5V` 引脚，为插接在模块上的 Atom-Lite 主机供电。
    *   外部输入的高压（VM）直接供给 DRV8825 的 `VM` 引脚，用于驱动步进电机。

### 3. 逻辑与控制信号映射 (Logic & Control Signal Mapping)
*   **控制信号路径**（连接至 Atom 主机 GPIO）：
    *   **STEP (步进脉冲)**：连接至 Atom 的 `G22` 引脚。主机产生的脉冲频率决定电机转速。
    *   **DIR (方向控制)**：连接至 Atom 的 `G19` 引脚。高/低电平决定电机旋转方向。
    *   **EN (使能控制)**：连接至 Atom 的 `G23` 引脚。低电平使能驱动器输出，高电平禁用输出（H 桥进入高阻态）。
    *   **FAULT (故障反馈)**：DRV8825 的 `nFAULT` 引脚连接至 Atom 的 `G25` 引脚。该引脚为开漏输出，外部接有上拉电阻。当驱动芯片检测到异常时，该引脚被拉低。
*   **电压监测 (PWR-ADC)**：
    *   输入电源 VIN 经过一个电阻分压网络连接至 Atom 的 `G33` 引脚。
    *   Atom 主机通过 ADC 读取该引脚电压，从而计算出外部电池或电源的实际输入电压。

### 4. 硬件配置与调节机制 (Hardware Configuration & Adjustment)
*   **细分设置 (Microstepping)**：
    *   板载 3 位拨码开关（DIP Switch 的前 3 位）分别连接至 DRV8825 的 `MODE0`, `MODE1`, `MODE2` 引脚。
    *   开关通断控制这些引脚的高低电平组合，实现从全步进（Full Step）到 1/32 微步进（1/32 Step）的 6 种分辨率切换。
*   **衰减模式 (Decay Mode)**：
    *   DIP 开关的第 4 位连接至 DRV8825 的 `DECAY` 引脚。
    *   配置该引脚电平可选择混合衰减（Mixed Decay）、慢衰减（Slow Decay）或快衰减（Fast Decay）模式，优化电流波形以减少电机噪音或震动。
*   **电流调节 (Current Adjustment)**：
    *   板载可变电阻（电位器）连接在 DRV8825 的 `VREF` 引脚与地之间，与上拉电阻构成从 3.3V 参考电压取电的分压电路。
    *   调节电位器改变 `VREF` 的电压值，进而设定斩波电流阈值（$I_{CHOP}$），从而控制输出到电机的最大驱动电流（最大支持 1.2A）。

### 5. 保护与指示 (Protection & Indication)
*   **保护机制**：DRV8825 芯片内部集成了过流保护（OCP）、热关断（Thermal Shutdown）和欠压锁定（UVLO）。
*   **故障指示**：
    *   当上述保护机制触发时，DRV8825 内部逻辑将 `nFAULT` 引脚拉低。
    *   原理图中 `nFAULT` 信号不仅传输给 Atom 主机，通常也连接不到复位引脚或通过 LED 指示电路（如有）反映故障状态。
    *   `nSLEEP` 和 `nRESET` 引脚在原理图中默认通过上拉电阻连接至逻辑高电平，保持芯片处于工作状态。

### 6. 接口定义 (Interface Definition)
*   **KF128L-2.54-6P 端子定义**（从左至右或根据丝印顺序）：
    1.  **B2**：步进电机 B 相线圈端子 2。
    2.  **B1**：步进电机 B 相线圈端子 1。
    3.  **A1**：步进电机 A 相线圈端子 1。
    4.  **A2**：步进电机 A 相线圈端子 2。
    5.  **GND**：外部电源输入地。
    6.  **VIN**：外部电源输入正极（9V - 18V）。

---

## 补充信息

基于提供的原始文档，对 Atom Stepmotor 模块原理图描述进行以下技术细节补充：

### 1. 硬件配置逻辑补充 (Configuration Logic Detail)
*   **细分设置真值表 (Microstepping Logic)**：
    *   原理图中连接至 `MODE0`, `MODE1`, `MODE2` 的 DIP 开关（对应文档中的开关 1, 2, 3），其具体的通断状态与步进分辨率对应关系如下：
        *   **Full-step**: SW1=Off, SW2=Off, SW3=Off
        *   **Half-step**: SW1=Off, SW2=Off, SW3=On
        *   **1/4 step**: SW1=Off, SW2=On, SW3=Off
        *   **1/8 step**: SW1=Off, SW2=On, SW3=On
        *   **1/16 step**: SW1=On, SW2=Off, SW3=Off
        *   **1/32 step**: SW1=On, SW2=Off, SW3=On; 或 SW1=On, SW2=On, SW3=Off; 或 SW1=On, SW2=On, SW3=On (三种组合均有效)。
*   **衰减模式逻辑 (Decay Mode Logic)**：
    *   连接至 `DECAY` 引脚的第 4 位 DIP 开关控制逻辑明确为：
        *   **慢衰减 (Slow Decay)**: 开关置于 Off 位置（对应低电平或悬空被下拉，视具体上拉/下拉电阻配置而定）。
        *   **快衰减 (Fast Decay)**: 开关置于 On 位置（对应高电平）。

### 2. 物理接口映射补充 (Physical Interface Mapping)
*   **Atom 模块互联接口定义**：
    *   模块与 Atom-Lite 主机连接的底部 9Pin 接口（2.54mm 间距，双排分布）物理引脚分配如下：
        *   **Pin 1**: 3V3 系统电源
        *   **Pin 2**: RESET 复位信号
        *   **Pin 3**: EN 电机使能信号
        *   **Pin 4**: FAULT 故障输出信号
        *   **Pin 5**: STEP 步进脉冲信号
        *   **Pin 6**: 5V 电源输出（来自板载 DC-DC）
        *   **Pin 7**: DIR 方向控制信号
        *   **Pin 8**: GND 地线
        *   **Pin 9**: PWR-ADC 电源电压检测信号

---

*该文档由 AI 自动生成，生成时间: 2026-01-06 16:20:13*
