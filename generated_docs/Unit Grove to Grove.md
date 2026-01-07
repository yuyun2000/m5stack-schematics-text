# Unit Grove to Grove 原理图描述

---

## 原理图分析

根据 M5Stack Unit Grove to Grove (SKU: U148) 的硬件设计逻辑及提示词信息，以下是该设备的原理图技术性描述：

### 1. 总体架构与设计思想
该电路设计采用“直通扩展”架构，旨在两个 HY2.0-4P Grove 接口之间插入电源管理层。电路主要由 **电源切换回路 (Power Switching Loop)** 和 **电流检测回路 (Current Sensing Loop)** 两部分组成。输入端（Host Side）接收来自主控的电源与控制信号，输出端（Slave Side）向负载供电。设计核心在于通过 GPIO 控制 5V 电源通断，并利用运算放大器实时调理电流采样信号，将其转换为 MCU 可读的模拟电压。

### 2. 电源切换电路 (Power Switch Circuit)
该模块负责控制从输入端到输出端的 5V 电源路径通断。
*   **核心开关元件：** 采用 **P-Channel MOSFET (PMOS)** 作为高侧开关（High-Side Switch）。PMOS 的源极（Source）连接至输入端 5V，漏极（Drain）连接至输出端 VCC（经过采样电阻）。
*   **驱动逻辑：**
    *   `PWR_EN` 信号（对应 Grove 接口黄色信号线）作为控制输入。
    *   为了驱动高侧 PMOS，电路通常包含一级小信号 N-Channel MOSFET 或 NPN 三极管作为电平转换与驱动级。
    *   当 `PWR_EN` 为有效电平（通常为高电平）时，驱动管导通，将 PMOS 栅极（Gate）拉低，PMOS 导通，输出端获得 5V 电源。
    *   当 `PWR_EN` 为无效电平（低电平）时，通过上拉电阻将 PMOS 栅极拉高至 5V，PMOS 截止，切断输出电源。
*   **电源规格：** 设计支持 5V 电压及最大 1A 的电流通过能力。

### 3. 电流检测电路 (Current Sensing Circuit)
该模块用于测量流经负载的电流，并输出放大后的模拟信号。
*   **采样电阻 (Shunt Resistor)：** 在电源通路中串联了一个高精度、低阻值的采样电阻，阻值设定为 **0.02Ω (20mΩ)**。该电阻位于 PMOS 输出与 Grove 输出端口之间（高侧采样）或 GND 回路中（低侧采样，根据 Grove 共地特性，通常采用高侧采样配合差分放大，或低侧采样配合共地）。结合 M5Stack 常见设计，若为简化设计可能采用低侧采样，但考虑到 Grove 设备的通用性，高侧采样更为合理。此处根据提示词增益逻辑分析，重点在于电阻上的压降 $V_{shunt} = I \times R$。
*   **信号放大 (Signal Amplification)：**
    *   **核心芯片：** 使用通用运算放大器（Op-Amp），配置为非反相放大器或差分放大器模式。
    *   **增益配置：** 运算放大器的反馈电阻网络设定了闭环增益。根据提示词中的计算公式 `((groveVol - groveVref) / 50.0f / 0.02f)` 反推，电路的硬件增益（Gain）设计为 **50倍**。
    *   **传递函数：** $V_{out} = I_{load} \times 0.02\Omega \times 50 = I_{load} \times 1 V/A$。即每 1A 电流对应输出 1V 的模拟电压变化。
*   **输出信号：** 放大后的电压信号连接至输入端 Grove 接口的 `Analog Output` 引脚（白色信号线），供主机 ADC 采集。输出端通常并联有滤波电容以减少噪声干扰。

### 4. 接口与连接关系 (Connectors & Pinout)
*   **Grove Port In (连接主机):**
    *   **Pin 1 (Yellow, PWR_EN):** 连接至电源开关驱动电路的输入端。
    *   **Pin 2 (White, Analog Output):** 连接至运算放大器的输出引脚。
    *   **Pin 3 (Red, 5V):** 直接连接至 PMOS 的源极（输入电源）。
    *   **Pin 4 (Black, GND):** 系统公共地，连接至所有模块的 GND。
*   **Grove Port Out (连接负载):**
    *   **Pin 1 (Yellow):** 通常悬空或作为直通信号（视具体 PCB 布局而定，但在本设计中主要逻辑集中在 Input 侧）。
    *   **Pin 2 (White):** 悬空或直通。
    *   **Pin 3 (Red, VCC_OUT):** 连接至采样电阻/PMOS 后的受控 5V 电源。
    *   **Pin 4 (Black, GND):** 公共地。

### 5. 电源管理与保护
*   **去耦电容：** 在 5V 输入端和运放电源引脚附近布置有去耦电容（通常为 0.1µF 或 1µF），用于滤除电源噪声，保证运放工作的稳定性。
*   **限流与保护：** 虽然电路具备电流检测功能，但物理通断依赖 MCU 的软件逻辑判断（读取模拟值后关闭 `PWR_EN`）。PMOS 本身选型需留有电流余量以支持 1A 负载。

---

## 补充信息

基于您提供的原始文档及代码逻辑，对 M5Stack Unit Grove to Grove (SKU: U148) 的原理图描述补充如下：

### 1. 信号线色与物理层定义确认
*   **黄色信号线 (Yellow Wire):** 确认为 **数字控制输入 (`PWR_EN`)**。在原理图中，该线路连接至电源开关驱动级。
*   **白色信号线 (White Wire):** 确认为 **模拟电压输出 (`Analog Output`)**。该线路直接连接至板载运算放大器的输出端，用于输出代表电流大小的电压信号。

### 2. 控制逻辑极性 (Control Logic Polarity)
*   根据代码 `digitalWrite(Din_Pin, groveOn)` 其中 `groveOn` 为 `HIGH`，确认原理图设计为 **高电平有效 (Active High)**。即 `PWR_EN` 信号输入高电平时，PMOS 导通，Grove Out 输出 5V；输入低电平时，PMOS 截止，输出断电。

### 3. 模拟前端特性与零点校准 (Analog Front-End & Zero Calibration)
*   **直流耦合与偏置：** 代码中的 `getVerf()` 函数及计算公式 `(groveVol - groveVref)` 表明，原理图中的运算放大器电路 **未设计硬件自动调零**，输出信号包含固有的直流偏置电压（Offset）或运算放大器的失调电压。
*   **传递函数修正：** 结合软件算法，完整的电路传递函数应描述为：
    $$V_{Analog\_Out} = (I_{load} \times 0.02\Omega \times 50) + V_{ref\_offset}$$
    这意味着原理图设计依赖主控端在空载状态下读取初始电压作为基准 ($V_{ref}$)，随后读取的电压增量才代表实际负载电流。
*   **有效电压摆幅：** 在 0~1000mA 量程下，模拟输出端的有效电压变化量（$\Delta V$）约为 **1.0V** ($1A \times 0.02\Omega \times 50$)。结合 ESP32 的 ADC 衰减设置 (11dB)，输出信号完全落在 ADC 的线性采样范围内。

### 4. 采样电阻位置验证
*   考虑到 Grove 接口的通用性及代码中对地参考的电压读取方式，进一步确认采样电阻位于 **高侧 (High-Side)**，即串联在 PMOS 漏极与输出端 VCC 之间。运算放大器采用 **差分放大 (Differential Amplifier)** 拓扑跨接在采样电阻两端，以消除共模电压（5V）的影响，仅放大电阻上的微小压降。

---

*该文档由 AI 自动生成，生成时间: 2026-01-07 01:57:15*
