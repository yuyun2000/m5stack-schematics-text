# Unit DDS 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit DDS |
| SKU | U105 |
| 产品 ID | `unit-dds-233a84b8d205` |
| 源文档 | `zh_CN/unit/dds.md` |

## 概述

Unit DDS 由 IC1A/IC1B STM32F031G4x 控制 IC2 AD9833，主机通过 Grove I2C 配置 MCU，MCU 再以 SPI_SCK/SPI_DATA/SPI_NCSS 驱动 DDS。X1 25M 为 MCU 提供 SYS_CLK，MCU 的 RCC_CLK_25MHz 经 R9 接 AD9833 DDS_CLK/MCLK。IC4 SPX3819 将 5V 转为 3.3V；AD9833 的 DDS_OUT 经 IC3 OPA365 缓冲、R7 串联后输出到 COM1 IPEX 座子。

## 检索关键词

`Unit DDS`、`U105`、`AD9833`、`IC2`、`STM32F031G4x`、`STM32F031G4U6`、`IC1A`、`IC1B`、`OPA365`、`IC3`、`SPX3819`、`IC4`、`X1 25M`、`DDS_CLK`、`RCC_CLK_25MHz`、`SPI_SCK`、`SPI_DATA`、`SPI_NCSS`、`DDS_SCLK`、`DDS_SDATA`、`DDS_FSYNC`、`DDS_OUT`、`SMA_OUT`、`COM1`、`IPEX座子`、`I2C`、`I2C_SCL`、`I2C_SDA`、`0x31`、`SYS_SWDIO`、`SYS_SWCLK`、`SYS_NRST`、`BOOT0`、`VCC_5V`、`VCC_3V3`、`DGND`、`AGND`、`RP1 3R3`、`TP1`、`TP3`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| IC1A,IC1B | STM32F031G4x | 板载控制 MCU，作为 I2C 设备接受主机配置，以 SPI 控制 AD9833，并提供 SWD/复位与 DDS 时钟。 | 图 ec76bf6dc6ae / 第 1 页 / 左上 IC1A/IC1B STM32F031G4x，PA/PB/PF、VDD/VDDA/VSS 引脚 |
| IC2 | AD9833 | DDS 波形发生器，接收 MCLK 与三线串行控制，VOUT 输出 DDS_OUT。 | 图 ec76bf6dc6ae / 第 1 页 / 左下 IC2 AD9833，COMP/VDD/VCAP/DGND/MCLK/SDATA/SCLK/FSYNC/AGND/VOUT |
| IC3 | OPA365 | DDS_OUT 模拟缓冲放大器，输出经 R7 到 SMA_OUT/COM1。 | 图 ec76bf6dc6ae / 第 1 页 / 右下 IC3 OPA365、R6/R8、R7、TP3 DDS_OUT、COM1 |
| IC4 | SPX3819 | VCC_5V 到 VCC_3V3 的五引脚稳压器，EN 接 5V。 | 图 ec76bf6dc6ae / 第 1 页 / 右中 IC4 SPX3819，Vin/EN/GND/ADJ/Vout 与 VCC_5V/VCC_3V3 |
| X1 | 25M | 25M 有源时钟源，OUT 经 R4 3R3 输出 SYS_CLK 给 MCU。 | 图 ec76bf6dc6ae / 第 1 页 / 左中 X1 25M，VCC/EN-NC/OUT/GND、C7、R4、SYS_CLK |
| GROVE | GROVE | 四针 I2C 与供电接口，引出 DGND、VCC_5V、I2C_SDA、I2C_SCL。 | 图 ec76bf6dc6ae / 第 1 页 / 右上 GROVE 四针符号，1 DGND、2 VCC_5V、3 I2C_SDA、4 I2C_SCL |
| H1 | PAD1 | 四点 SWD 调试焊盘，引出 VCC_3V3、SYS_SWDIO、SYS_SWCLK、DGND。 | 图 ec76bf6dc6ae / 第 1 页 / 右上 H1 PAD1 四个焊盘及 VCC_3V3/SYS_SWDIO/SYS_SWCLK/DGND |
| COM1 | IPEX座子 | 模拟输出连接器，2 脚接 SMA_OUT，1 脚接 AGND。 | 图 ec76bf6dc6ae / 第 1 页 / 右下 COM1 IPEX座子，SMA_OUT/2 与 AGND/1 |
| RP1 | 3R3 | MCU SPI_DATA/SPI_SCK/SPI_NCSS 到 AD9833 DDS_SDATA/DDS_SCLK/DDS_FSYNC 的串联电阻阵列。 | 图 ec76bf6dc6ae / 第 1 页 / 页面中部 RP1 3R3，左侧 SPI 三线与右侧 DDS 三线 |
| R1,C1 | 10K / 104 | SYS_NRST 的 VCC_3V3 上拉与 DGND 电容复位网络。 | 图 ec76bf6dc6ae / 第 1 页 / 左上 IC1 SYS_NRST、R1 10K 到 VCC_3V3、C1 104 到 DGND |
| R2,R3 | 10K | I2C_SCL 与 I2C_SDA 到 VCC_3V3 的上拉电阻。 | 图 ec76bf6dc6ae / 第 1 页 / 左上偏下 R2 10K 上拉 I2C_SCL，R3 10K 上拉 I2C_SDA |
| TP1,TP3 | TEST | DDS_CLK 与 DDS_OUT 的测试点。 | 图 ec76bf6dc6ae / 第 1 页 / 左中 TP1 DDS_CLK TEST 与右下 TP3 DDS_OUT TEST |
| R5 | 0R | DGND 与 AGND 之间的 0Ω单点连接。 | 图 ec76bf6dc6ae / 第 1 页 / 左下 AD9833 区域 R5 0R 跨接 DGND 与 AGND |

## 系统结构

### 整板架构

IC1 STM32F031G4x 通过 Grove I2C 接收主机控制，并以 SPI 与 DDS_CLK 驱动 IC2 AD9833；DDS_OUT 经 IC3 OPA365 到 COM1，IC4 从 5V 生成 3.3V。

- 参数与网络：`controller=IC1A,IC1B STM32F031G4x`；`dds=IC2 AD9833`；`output_buffer=IC3 OPA365`；`regulator=IC4 SPX3819`；`host_bus=I2C`；`dds_bus=3-wire SPI`；`output=COM1 IPEX座子`
- 证据：图 ec76bf6dc6ae / 第 1 页 / 第 1 页全图，IC1-IC4、X1、GROVE、COM1 功能分区

## 核心器件

### IC1 STM32F031G4x 关键引脚

IC1 的 SPI_SCK、SPI_DATA、RCC_CLK_25MHz、I2C_SCL、I2C_SDA、SYS_SWDIO、SYS_SWCLK 分别位于 PA5/11、PA7/13、PA8/18、PA9/19、PA10/20、PA13/21、PA14/22；SPI_NCSS 位于 PB0/14。

- 参数与网络：`spi_sck=PA5 pin11`；`spi_data=PA7 pin13`；`spi_ncss=PB0 pin14`；`rcc_clk_25mhz=PA8 pin18`；`i2c_scl=PA9 pin19`；`i2c_sda=PA10 pin20`；`swdio=PA13 pin21`；`swclk=PA14 pin22`；`sys_clk=PF0-OSC_IN pin2`；`nrst=pin4`；`boot0=pin1`
- 证据：图 ec76bf6dc6ae / 第 1 页 / 左上 IC1A 左右两侧网络与引脚号

### IC2 AD9833

IC2 VDD/2 接 VCC_3V3，DGND/4 接 DGND，AGND/9 接 AGND，MCLK/5 接 DDS_CLK，SDATA/6、SCLK/7、FSYNC/8 接 DDS 控制线，VOUT/10 输出 DDS_OUT。

- 参数与网络：`pin_1=COMP/DDS_COMP`；`pin_2=VDD/VCC_3V3`；`pin_3=CAP/2V5/DDS_VCAP`；`pin_4=DGND`；`pin_5=MCLK/DDS_CLK`；`pin_6=SDATA/DDS_SDATA`；`pin_7=SCLK/DDS_SCLK`；`pin_8=FSYNC/DDS_FSYNC`；`pin_9=AGND`；`pin_10=VOUT/DDS_OUT`
- 证据：图 ec76bf6dc6ae / 第 1 页 / 左下 IC2 AD9833 1-10 脚与网络标注

## 电源

### IC4 5V 到 3.3V 稳压

IC4 SPX3819 的 Vin（1 脚）与 EN（3 脚）接 VCC_5V，Vout（5 脚）输出 VCC_3V3，GND/ADJ（2、4 脚）接地。

- 参数与网络：`regulator=IC4 SPX3819`；`input=Vin pin1/VCC_5V`；`enable=EN pin3/VCC_5V`；`output=Vout pin5/VCC_3V3`；`ground_adjust=pins2,4`
- 证据：图 ec76bf6dc6ae / 第 1 页 / 右中 IC4 SPX3819 五脚与 VCC_5V/VCC_3V3/DGND

### IC4 输入滤波

C13 标注 104、E2 标注 10uF/10V，均从 VCC_5V 接 DGND，位于 IC4 Vin/EN 输入侧。

- 参数与网络：`ceramic=C13 104`；`bulk=E2 10uF/10V`；`rail=VCC_5V`；`return=DGND`
- 证据：图 ec76bf6dc6ae / 第 1 页 / 右中 IC4 左侧 C13/E2 与 VCC_5V/DGND

## 接口

### GROVE 四针接口

GROVE 的 1-4 脚分别连接 DGND、VCC_5V、I2C_SDA、I2C_SCL。

- 参数与网络：`pin_1=DGND`；`pin_2=VCC_5V`；`pin_3=I2C_SDA`；`pin_4=I2C_SCL`
- 证据：图 ec76bf6dc6ae / 第 1 页 / 右上 GROVE 符号及 I2C_SCL/4、I2C_SDA/3、VCC_5V/2、DGND/1

### COM1 模拟输出

IC3 输出经 R7 3R3 形成 SMA_OUT，连接 COM1 IPEX 座子 2 脚；COM1.1 接 AGND。

- 参数与网络：`source=IC3 OPA365 output pin1`；`series_resistor=R7 3R3`；`net=SMA_OUT`；`connector=COM1 IPEX座子`；`signal_pin=2`；`ground_pin=1/AGND`
- 证据：图 ec76bf6dc6ae / 第 1 页 / 右下 IC3-R7-SMA_OUT-COM1/AGND

## 总线

### 主机 I2C

I2C_SCL 从 GROVE.4 连接 IC1 PA9（19 脚），I2C_SDA 从 GROVE.3 连接 IC1 PA10（20 脚）；R2/R3 各以 10K 上拉到 VCC_3V3。

- 参数与网络：`device=IC1 STM32F031G4x`；`scl=GROVE.4 -> PA9 pin19`；`sda=GROVE.3 -> PA10 pin20`；`scl_pullup=R2 10K to VCC_3V3`；`sda_pullup=R3 10K to VCC_3V3`
- 证据：图 ec76bf6dc6ae / 第 1 页 / IC1 PA9/PA10、R2/R3 与右上 GROVE I2C 网络

### MCU 到 AD9833 三线串行总线

IC1 的 SPI_DATA、SPI_SCK、SPI_NCSS 分别经 RP1 的 3R3 串联单元形成 DDS_SDATA、DDS_SCLK、DDS_FSYNC，并连接 IC2 的 SDATA/6、SCLK/7、FSYNC/8。

- 参数与网络：`controller=IC1 STM32F031G4x`；`device=IC2 AD9833`；`data=PA7/SPI_DATA -> RP1 3R3 -> DDS_SDATA -> IC2 pin6`；`clock=PA5/SPI_SCK -> RP1 3R3 -> DDS_SCLK -> IC2 pin7`；`chip_select=PB0/SPI_NCSS -> RP1 3R3 -> DDS_FSYNC -> IC2 pin8`
- 证据：图 ec76bf6dc6ae / 第 1 页 / IC1 SPI 网络、页面中 RP1、左下 IC2 SDATA/SCLK/FSYNC

## GPIO 与控制信号

### IC1 BOOT0

IC1 BOOT0（1 脚）直接连接 DGND。

- 参数与网络：`mcu_pin=IC1 BOOT0 pin1`；`connection=DGND`
- 证据：图 ec76bf6dc6ae / 第 1 页 / 左上 IC1 BOOT0/1 脚至 DGND

## 时钟

### X1 MCU 时钟

X1 标注 25M，VCC 与 EN/NC 接 VCC_3V3，GND 接 DGND，OUT 经 R4 3R3 形成 SYS_CLK 并连接 IC1 PF0-OSC_IN（2 脚）。

- 参数与网络：`oscillator=X1 25M`；`supply=VCC_3V3`；`enable=VCC_3V3`；`output_resistor=R4 3R3`；`output_net=SYS_CLK`；`mcu_pin=PF0-OSC_IN pin2`；`decoupling=C7 104`
- 证据：图 ec76bf6dc6ae / 第 1 页 / 左中 X1 25M-R4-SYS_CLK 与左上 IC1 PF0-OSC_IN

### AD9833 MCLK

IC1 PA8（18 脚）的 RCC_CLK_25MHz 经 R9 3R3 连接 DDS_CLK、TP1，并接 IC2 AD9833 MCLK（5 脚）。

- 参数与网络：`mcu_pin=PA8 pin18`；`source_net=RCC_CLK_25MHz`；`series_resistor=R9 3R3`；`dds_net=DDS_CLK`；`test_point=TP1`；`dds_pin=IC2 MCLK pin5`
- 证据：图 ec76bf6dc6ae / 第 1 页 / IC1 PA8 RCC_CLK_25MHz、左中 TP1/R9 DDS_CLK 与 IC2 MCLK/5

## 复位

### IC1 SYS_NRST

IC1 NRST（4 脚）连接 SYS_NRST，由 R1 10K 上拉至 VCC_3V3，并由 C1 104 接 DGND。

- 参数与网络：`mcu_pin=IC1 NRST pin4`；`net=SYS_NRST`；`pullup=R1 10K to VCC_3V3`；`capacitor=C1 104 to DGND`
- 证据：图 ec76bf6dc6ae / 第 1 页 / 左上 IC1 NRST/SYS_NRST 与 R1/C1

## 保护电路

### Grove 与模拟输出保护

原理图未显示 Grove 5V/I2C 或 COM1 SMA_OUT 上的 TVS、保险丝、反接保护或输出过压/短路保护器件。

- 参数与网络：`grove=GROVE`；`analog_output=COM1`；`tvs=原理图未显示`；`fuse=原理图未显示`；`reverse_protection=原理图未显示`；`output_protection=原理图未显示`
- 证据：图 ec76bf6dc6ae / 第 1 页 / 右上 GROVE 至 IC4/I2C 直接路径与右下 R7-COM1 直接路径

## 关键网络

### DGND 与 AGND

R5 0R 连接 DGND 与 AGND；AD9833 DGND/4 与数字去耦使用 DGND，AGND/9、OPA365 和 COM1 使用 AGND。

- 参数与网络：`link=R5 0R`；`digital_ground=DGND`；`analog_ground=AGND`；`digital_consumers=IC1,IC2 pin4`；`analog_consumers=IC2 pin9,IC3,COM1`
- 证据：图 ec76bf6dc6ae / 第 1 页 / 左下 R5 0R DGND-AGND 与 IC2/IC3/COM1 地网络

## 存储

### 外部存储

本页未显示外部 Flash、EEPROM、SD 卡或其他存储器件。

- 参数与网络：`controller=IC1 STM32F031G4x`；`flash=原理图未显示`；`eeprom=原理图未显示`；`sd_card=原理图未显示`
- 证据：图 ec76bf6dc6ae / 第 1 页 / 第 1 页全图，无外部存储器位号或连接器

## 调试与烧录

### H1 SWD 调试焊盘

H1 四点 PAD1 依次引出 VCC_3V3、SYS_SWDIO、SYS_SWCLK、DGND；SYS_SWDIO/SYS_SWCLK 分别连接 IC1 PA13/21、PA14/22。

- 参数与网络：`reference=H1`；`signals=VCC_3V3,SYS_SWDIO,SYS_SWCLK,DGND`；`swdio_mcu=PA13 pin21`；`swclk_mcu=PA14 pin22`
- 证据：图 ec76bf6dc6ae / 第 1 页 / 右上 H1 PAD1 与左上 IC1 PA13/PA14 网络

## 模拟电路

### AD9833 COMP/VCAP 与去耦

C5 103 位于 DDS_COMP 与 VCC_3V3 之间，C6 105 位于 DDS_VCAP 与 DGND 之间；C10/C8/C9 均为 104，分别对 VCC_3V3 进行 AGND/DGND 去耦。

- 参数与网络：`comp_capacitor=C5 103 DDS_COMP-to-VCC_3V3`；`vcap_capacitor=C6 105 DDS_VCAP-to-DGND`；`analog_decoupling=C10 104,C9 104 to AGND`；`digital_decoupling=C8 104 to DGND`
- 证据：图 ec76bf6dc6ae / 第 1 页 / 左下 IC2 周围 C5/C6/C8/C9/C10 与 VCC_3V3/DGND/AGND

### DDS_OUT 输出缓冲

DDS_OUT/TP3 经 R8 100K 接 IC3 OPA365 非反相输入（3 脚），R6 100K 从输出（1 脚）反馈至反相输入（4 脚）；IC3 以 VCC_3V3/AGND 供电。

- 参数与网络：`input_net=DDS_OUT/TP3`；`input_resistor=R8 100K`；`op_amp=IC3 OPA365`；`non_inverting_pin=3`；`feedback=R6 100K output pin1 to inverting pin4`；`supply=VCC_3V3 pin5`；`ground=AGND pin2`
- 证据：图 ec76bf6dc6ae / 第 1 页 / 右下 TP3-R8-IC3 OPA365-R6 输出反馈电路

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 整板架构 | `controller=IC1A,IC1B STM32F031G4x`；`dds=IC2 AD9833`；`output_buffer=IC3 OPA365`；`regulator=IC4 SPX3819`；`host_bus=I2C`；`dds_bus=3-wire SPI`；`output=COM1 IPEX座子` |
| 核心器件 | IC1 STM32F031G4x 关键引脚 | `spi_sck=PA5 pin11`；`spi_data=PA7 pin13`；`spi_ncss=PB0 pin14`；`rcc_clk_25mhz=PA8 pin18`；`i2c_scl=PA9 pin19`；`i2c_sda=PA10 pin20`；`swdio=PA13 pin21`；`swclk=PA14 pin22`；`sys_clk=PF0-OSC_IN pin2`；`nrst=pin4`；`boot0=pin1` |
| 核心器件 | STM32F031 完整料号 | `schematic_part=STM32F031G4x`；`documented_candidate=STM32F031G4U6`；`exact_suffix=未标注` |
| 电源 | IC4 5V 到 3.3V 稳压 | `regulator=IC4 SPX3819`；`input=Vin pin1/VCC_5V`；`enable=EN pin3/VCC_5V`；`output=Vout pin5/VCC_3V3`；`ground_adjust=pins2,4` |
| 电源 | IC4 输入滤波 | `ceramic=C13 104`；`bulk=E2 10uF/10V`；`rail=VCC_5V`；`return=DGND` |
| 接口 | GROVE 四针接口 | `pin_1=DGND`；`pin_2=VCC_5V`；`pin_3=I2C_SDA`；`pin_4=I2C_SCL` |
| 总线 | 主机 I2C | `device=IC1 STM32F031G4x`；`scl=GROVE.4 -> PA9 pin19`；`sda=GROVE.3 -> PA10 pin20`；`scl_pullup=R2 10K to VCC_3V3`；`sda_pullup=R3 10K to VCC_3V3` |
| 总线地址 | Unit DDS I2C 地址 | `controller=IC1 STM32F031G4x`；`documented_candidate=0x31`；`schematic_address=未标注`；`address_straps=未显示` |
| 调试与烧录 | H1 SWD 调试焊盘 | `reference=H1`；`signals=VCC_3V3,SYS_SWDIO,SYS_SWCLK,DGND`；`swdio_mcu=PA13 pin21`；`swclk_mcu=PA14 pin22` |
| 复位 | IC1 SYS_NRST | `mcu_pin=IC1 NRST pin4`；`net=SYS_NRST`；`pullup=R1 10K to VCC_3V3`；`capacitor=C1 104 to DGND` |
| GPIO 与控制信号 | IC1 BOOT0 | `mcu_pin=IC1 BOOT0 pin1`；`connection=DGND` |
| 时钟 | X1 MCU 时钟 | `oscillator=X1 25M`；`supply=VCC_3V3`；`enable=VCC_3V3`；`output_resistor=R4 3R3`；`output_net=SYS_CLK`；`mcu_pin=PF0-OSC_IN pin2`；`decoupling=C7 104` |
| 时钟 | AD9833 MCLK | `mcu_pin=PA8 pin18`；`source_net=RCC_CLK_25MHz`；`series_resistor=R9 3R3`；`dds_net=DDS_CLK`；`test_point=TP1`；`dds_pin=IC2 MCLK pin5` |
| 时钟 | DDS 实际参考频率 | `schematic_oscillator=X1 25M`；`schematic_mcu_net=RCC_CLK_25MHz`；`documented_candidate=10MHz`；`runtime_mclk=需确认`；`divider=未标注` |
| 总线 | MCU 到 AD9833 三线串行总线 | `controller=IC1 STM32F031G4x`；`device=IC2 AD9833`；`data=PA7/SPI_DATA -> RP1 3R3 -> DDS_SDATA -> IC2 pin6`；`clock=PA5/SPI_SCK -> RP1 3R3 -> DDS_SCLK -> IC2 pin7`；`chip_select=PB0/SPI_NCSS -> RP1 3R3 -> DDS_FSYNC -> IC2 pin8` |
| 核心器件 | IC2 AD9833 | `pin_1=COMP/DDS_COMP`；`pin_2=VDD/VCC_3V3`；`pin_3=CAP/2V5/DDS_VCAP`；`pin_4=DGND`；`pin_5=MCLK/DDS_CLK`；`pin_6=SDATA/DDS_SDATA`；`pin_7=SCLK/DDS_SCLK`；`pin_8=FSYNC/DDS_FSYNC`；`pin_9=AGND`；`pin_10=VOUT/DDS_OUT` |
| 模拟电路 | AD9833 COMP/VCAP 与去耦 | `comp_capacitor=C5 103 DDS_COMP-to-VCC_3V3`；`vcap_capacitor=C6 105 DDS_VCAP-to-DGND`；`analog_decoupling=C10 104,C9 104 to AGND`；`digital_decoupling=C8 104 to DGND` |
| 模拟电路 | DDS_OUT 输出缓冲 | `input_net=DDS_OUT/TP3`；`input_resistor=R8 100K`；`op_amp=IC3 OPA365`；`non_inverting_pin=3`；`feedback=R6 100K output pin1 to inverting pin4`；`supply=VCC_3V3 pin5`；`ground=AGND pin2` |
| 接口 | COM1 模拟输出 | `source=IC3 OPA365 output pin1`；`series_resistor=R7 3R3`；`net=SMA_OUT`；`connector=COM1 IPEX座子`；`signal_pin=2`；`ground_pin=1/AGND` |
| 关键网络 | DGND 与 AGND | `link=R5 0R`；`digital_ground=DGND`；`analog_ground=AGND`；`digital_consumers=IC1,IC2 pin4`；`analog_consumers=IC2 pin9,IC3,COM1` |
| 保护电路 | Grove 与模拟输出保护 | `grove=GROVE`；`analog_output=COM1`；`tvs=原理图未显示`；`fuse=原理图未显示`；`reverse_protection=原理图未显示`；`output_protection=原理图未显示` |
| 存储 | 外部存储 | `controller=IC1 STM32F031G4x`；`flash=原理图未显示`；`eeprom=原理图未显示`；`sd_card=原理图未显示` |
| 模拟电路 | 波形、频率、幅值与分辨率 | `waveform_candidates=sine,triangle,square,sawtooth,DC`；`amplitude_candidate=0-0.6V`；`frequency_range_candidate=0-1MHz`；`sawtooth_candidate=13.6KHz`；`frequency_resolution_candidate=28bit`；`phase_resolution_candidate=11bit`；`schematic_performance=未标注` |

## 待确认事项

- `component.mcu-suffix-undetermined`：原理图符号只标 STM32F031G4x，不能仅由图纸确认正文所列完整料号 STM32F031G4U6 及封装后缀。（证据：图 ec76bf6dc6ae / 第 1 页 / IC1A/IC1B 符号下方仅印 STM32F031G4x）
- `address.i2c-address-undetermined`：原理图没有打印 I2C 地址或地址选择硬件，无法仅由本页确认正文中的 0x31。（证据：图 ec76bf6dc6ae / 第 1 页 / GROVE I2C 到 IC1 PA9/PA10 路径，整页无 0x31 或地址配置）
- `clock.reference-frequency-undetermined`：原理图标注 X1 为 25M、MCU 输出网络为 RCC_CLK_25MHz，而产品正文写 10MHz 基准；无法从现有资料闭环确认 AD9833 运行时 MCLK 的实际频率及 MCU 是否分频。（证据：图 ec76bf6dc6ae / 第 1 页 / X1 25M、IC1 PA8 RCC_CLK_25MHz、R9/DDS_CLK/IC2 MCLK 链）
- `analog.output-capabilities-undetermined`：原理图确认 AD9833 与 OPA365 输出链，但没有列出支持波形、输出幅值、频率范围、锯齿波频率、频率/相位分辨率或休眠行为，不能由图纸确认正文中的对应参数。（证据：图 ec76bf6dc6ae / 第 1 页 / IC2 AD9833、IC3 OPA365 与 COM1 电路，无波形/幅值/频率文字）
- `review.mcu-suffix`：Unit DDS 实际装配的 MCU 完整料号和封装是否为 STM32F031G4U6？；原因：原理图只标 STM32F031G4x，未给出完整尾缀。
- `review.i2c-address`：当前固件的 I2C 地址是否固定为 0x31，是否存在配置方式？；原因：地址属于 MCU 固件行为，原理图没有地址文字或选择硬件。
- `review.dds-reference-clock`：AD9833 实际 MCLK 是 25MHz、10MHz 还是由 MCU 运行时分频得到的其他频率？；原因：图中 X1=25M 且网络名为 RCC_CLK_25MHz，但正文写 10MHz，存在直接冲突。
- `review.output-capabilities`：该硬件/固件版本确认支持哪些波形，输出幅值、频率范围、分辨率与休眠行为分别是什么？；原因：这些参数未出现在原理图中，且依赖 AD9833 时钟与 MCU 固件配置。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `ec76bf6dc6ae3fd13b08846d12e89734db2aa87d13b67e60879f6c6d915ade37` | `https://static-cdn.m5stack.com/resource/docs/products/unit/dds/dds_sch_01.webp` |

---

源文档：`zh_CN/unit/dds.md`

源文档 SHA-256：`56bf3d39b15df3a157d6377e50e9846a7a9e4a33dd97f307324819b6542e18db`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
