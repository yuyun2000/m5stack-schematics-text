# Atom DTU LoRaWAN-EU868 原理图描述

---

## 原理图分析

**1. Core LoRaWAN Communication Module**
*   **Module & SoC:** The circuit utilizes the **RAK3172** module, which integrates the **STM32WLE5** System-on-Chip (SoC). This component handles the LoRaWAN protocol stack and RF signal modulation.
*   **RF Path:** The RF output pin of the RAK3172 is routed to an **SMA antenna interface** via a 50-ohm impedance-matched transmission line. The circuit typically includes passive filtering components for impedance matching and harmonic suppression between the module and the connector.
*   **Communication:** The module interacts with the main controller via a UART interface, receiving AT commands to manage network joining and data transmission.
*   **Power:** The module is powered by a regulated 3.3V rail.

**2. RS485 Interface & Logic**
*   **Transceiver:** The schematic features an **SP3485EN** (or equivalent) RS485 transceiver chip, responsible for converting TTL logic levels from the Atom controller into differential RS485 bus signals.
*   **Terminal Connection:** The transceiver's differential outputs (A and B) are routed to the **HT3.96-4P** terminal block.
*   **Control Logic:** The transceiver includes Driver Enable (DE) and Receiver Enable (RE#) pins, controlled by the MCU to switch between transmission and reception modes.

**3. Power Management Circuit**
*   **Input Stage:** Power enters the system via the **HT3.96-4P** terminal block, supporting a DC input range of 9V-12V.
*   **Voltage Regulation:**
    *   A **DC-DC Step-Down (Buck) Converter** steps down the high-voltage input (12V) to **5V** to supply power to the M5Stack Atom Lite base.
    *   A **Low Dropout Regulator (LDO)** converts the voltage to **3.3V** to power the RAK3172 module, the RS485 transceiver logic, and other onboard peripherals.
*   **Efficiency:** The power circuit is designed for low standby power consumption (referenced as ~170uA in specs) to support energy-efficient operation.

**4. Controller Interface & Port Mapping**
*   **UART Connections:**
    *   **Atom to LoRa:** A dedicated UART pair connects the Atom controller to the RAK3172 for AT command communication (Default Baud: 115200).
    *   **Atom to RS485:** A separate UART interface connects the Atom to the SP3485EN transceiver for RS485 data exchange.
*   **Expansion Port (PORT.A):** The schematic routes GPIO signals **G25** and **G21** from the Atom base to the external **HY2.0-4P (Grove)** connector, providing I2C or GPIO expansion capabilities alongside 5V and GND.

**5. Pin Configuration & Signal Flow**
*   **Logic Flow:** The Atom controller acts as the central bridge. It receives data from the RS485 bus (via SP3485EN), processes it, and forwards it to the LoRaWAN network (via RAK3172/STM32WLE5), or vice versa.
*   **Bus Map:**
    *   **RS485 Bus:** Connected to Pins A/B on the terminal block.
    *   **Power Bus:** VCC/GND on the terminal block feeds the internal regulators.
    *   **Internal Signals:** UART TX/RX lines and RS485 direction control lines are mapped to specific GPIOs on the Atom's bottom header.

---

## 补充信息

基于提供的原始文档，对上述原理图分析进行以下技术细节补充：

**1. 射频前端特性补充 (RF Specifics)**
*   **频段优化：** 射频电路与阻抗匹配网络专门针对 **EU868 (868-870 MHz)** 频段进行了调优，配合 0.5dBi 的胶棒天线工作。
*   **性能指标：** 在该硬件实现下，RAK3172 模组支持的最大发射功率为 **22 dBm**，接收灵敏度可达 **-137 dBm**。

**2. 电源路径负载特性 (Power Consumption Characteristics)**
*   **转换效率验证：** 电源管理电路（Buck + LDO）实现了极低的静态功耗，在 RS485 接口供电（DC 9V）下，整机待机电流仅为 **167.98uA**。
*   **动态负载：** 在 9V 输入下，接收模式电流约为 **50mA**；发送模式电流根据速率不同在 **51.56mA** (500Kbps) 至 **102.79mA** (125Kbps) 之间波动。

**3. 内部总线信号映射详情 (Internal Bus Signal Mapping)**
根据文档定义的 M5-Bus 内部引脚排列，信号连接的具体定义如下：
*   **LoRa UART 接口：** 映射至总线右侧 **Pin 3 (UART_RX)** 和 **Pin 5 (UART_TX)**。
*   **RS485 逻辑接口：** 映射至总线右侧 **Pin 7 (RS485_RX)** 和 **Pin 9 (RS485_TX)**。
*   **电源轨分布：** 3.3V 系统电源位于右侧 **Pin 1**，5V 电源通过左侧 **Pin 6** 及 PORT.A 红色引脚传输。

**4. 固件协议栈支持 (Firmware & Protocol)**
*   **协议实现：** STM32WLE5 SoC 内部固件已集成 **LoRaWAN 1.0.3** 协议栈，硬件上支持 **Class A、Class B、Class C** 三种模式及 **LoRa P2P** 点对点通信模式，所有模式切换与配置均通过上述 UART 物理链路使用 AT 指令集控制。

---

*该文档由 AI 自动生成，生成时间: 2026-01-06 15:37:01*
