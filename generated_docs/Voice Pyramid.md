# Voice Pyramid 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Voice Pyramid |
| SKU | A167 |
| 产品 ID | `voice-pyramid-c17fa45aea23` |
| 源文档 | `zh_CN/atom/Echo_Pyramid.md` |

## 概述

Voice Pyramid 以外接 Atom S3R/Atom 系列主控承担业务处理，板载 STM32G030F6P6 管理四路触摸网络、两路 NEOPIXEL 和 AW87559 复位。音频链由 ES7210 多麦克风 ADC、ES8311 codec/DAC、SI5351 27MHz 可编程 MCLK 与 AW87559 扬声器功放组成，主控通过 G38/G39 I2C 和 G5/G6/G7/G8 I2S 网络连接。USB-C VBUS 或 Grove 的 USB_IN 经 U6 生成 USB_5V，TPS7A2033PDBVR 生成 AUDIO_VDD，CH213K 位于 USB_5V 与 SYS_5V 单向供电路径；Grove 同时引出 I2C。资源包含 PDF 第 1、2、4 页而缺少第 3 页，因此麦克风子板、第二条触控 RGB 板和完整器件数量需补页复核。

## 检索关键词

`Voice Pyramid`、`A167`、`STM32G030F6P6`、`Atom S3R`、`ES7210`、`ES8311`、`SI5351A-B-GTR`、`AW87559`、`PT2042AD4`、`WS2812C-2020`、`AW32901FCR`、`TPS7A2033PDBVR`、`CH213K`、`I2C_SDA_G38`、`I2C_SCL_G39`、`I2S_SCLK_GPIO6`、`I2S_LRCK_GPIO8`、`I2S_ASDOUT_MISO_GPIO5`、`I2S_DIN_MOSI_GPIO7`、`I2S_MCLK_ADC`、`I2S_MCLK_DAC`、`0x18`、`0x40`、`0x5B`、`0x60`、`0x1A`、`AUDIO_VDD`、`USB_5V`、`SYS_5V`、`SYS_3V3`、`MIC_BIAS`、`DAC_P`、`DAC_N`、`AEC_P`、`AEC_N`、`SPK_RST`、`NEOPIXEL_1`、`NEOPIXEL_2`、`TP_1`、`TP_4`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U2 | ES7210 | 多通道麦克风 ADC，连接 AMIC1、AEC 回灌、I2C、I2S、MCLK 与 MIC_BIAS | 图 2ecdb3acbccf / 第 1 页 / 音频页网格 A1-B2，U2 ES7210 pins1-32 |
| U3 | ES8311 | I2C/I2S 音频 codec/DAC，差分输出 DAC_P/DAC_N 并以 CE=GND 选择 0x18 | 图 2ecdb3acbccf / 第 1 页 / 音频页网格 B1-C2，U3 ES8311、CE、I2C/I2S、OUTP/OUTN |
| U1,X1 | SI5351A-B-GTR / 27MHZ 10pF | 0x60 可编程时钟发生器及 27MHz 晶体，生成 I2S_MCLK_ADC/DAC | 图 2ecdb3acbccf / 第 1 页 / 音频页网格 C1-D2，U1 SI5351A-B-GTR、X1 27MHZ、0x60 |
| U4 | AW87559 | 0x5B I2C Class-D/升压扬声器功放，接收 DAC_P/N 并输出 VOP/VON | 图 2ecdb3acbccf / 第 1 页 / 音频页网格 C3-D4，U4 AW87559、0x5B、DAC_P/N、VOP/VON |
| CON1,CON2 | FPC 8-pin | 左右触控/RGB/麦克风子板接口，承载 TP_1-TP_4、NEOPIXEL_1/2、MIC_BIAS、AUDIO_VDD、USB_5V 与 GND | 图 2ecdb3acbccf / 第 1 页 / 音频页网格 A3-A4，CON1/CON2 8P FPC |
| FPC1 | HC-FPC-05-09-4RLTAG | 4 针麦克风接口，引出 AUDIO_VDD、GND、AMIC1_N 与 AMIC1_P | 图 2ecdb3acbccf / 第 1 页 / 音频页网格 B3-B4，FPC1 HC-FPC-05-09-4RLTAG pins1-4 |
| D1,D2 | SMF16CA | AW87559 扬声器差分输出 VOP/VON 到 GND 的 TVS 防护 | 图 2ecdb3acbccf / 第 1 页 / 音频页网格 C4，D1/D2 SMF16CA、VOP/VON 与扬声器连接器 |
| U5 | STM32G030F6P6 | 辅助 MCU，管理触摸、NEOPIXEL、SPK_RST、I2C 和 SWD 调试 | 图 0828e8e77d40 / 第 1 页 / 主控电源页网格 C1-D2，U5 STM32G030F6P6 pins1-20 |
| U8 | Atom S3R | 外接主控接口模块，提供 G38/G39、G5-G8、5V、3.3V 与 GND | 图 0828e8e77d40 / 第 1 页 / 主控电源页网格 A2，U8 Atom S3R 与 J4 CONNECT_12P |
| USB-C connector | USB_C_16P_Horizontal | 底部 5V 电源输入，VBUS 形成 USB_IN，CC1/CC2 各有 5.1KΩ 下拉 | 图 0828e8e77d40 / 第 1 页 / 主控电源页网格 A1，USB_C_16P_Horizontal、USB_IN、R18/R19 |
| J2 | GROVE | 4 针 Grove I2C/供电接口，引出 I2C_SCL_G39、I2C_SDA_G38、USB_IN 与 GND | 图 0828e8e77d40 / 第 1 页 / 主控电源页网格 B1，J2 GROVE pins1-4、D9/D10 |
| U6 | AW32901FCR | USB_IN 到 USB_5V 的受控电源开关/保护器件，并输出 ADC_CH3 分压监测 | 图 0828e8e77d40 / 第 1 页 / 主控电源页网格 B2，U6 AW32901FCR、USB_IN/USB_5V、R25/R26 ADC_CH3 |
| U9 | TPS7A2033PDBVR | USB_5V 经 L2 滤波后生成 AUDIO_VDD 的 3.3V LDO | 图 0828e8e77d40 / 第 1 页 / 主控电源页网格 B2-B3，L2 与 U9 TPS7A2033PDBVR |
| U7 | CH213K | USB_5V 与 SYS_5V 之间的单向供电器件 | 图 0828e8e77d40 / 第 1 页 / 主控电源页网格 A4，U7 CH213K、USB_5V/SYS_5V 与 Atom_S3R单向供电注释 |
| J3 | ISP 5-pin | STM32 SWD 调试接口，提供 SYS_3V3、SWCLK、SWDIO、RST 与 GND | 图 0828e8e77d40 / 第 1 页 / 主控电源页网格 D1-D2，J3 ISP pins1-5 |
| U1 | SMD_6P | 触控 RGB 条的板间连接器，承载 5V0、MIC_VDD、TP_OUT_1/2、NEOPIXEL 与 GND | 图 ccc2ec45b8bc / 第 1 页 / 触控 RGB 页网格 A1-B2，U1 SMD_6P pins1-8 |
| U2,U3 | PT2042AD4 | 两路电容触摸检测器，输出 TP_OUT_1/TP_OUT_2 并连接 Finger 电极 | 图 ccc2ec45b8bc / 第 1 页 / 触控 RGB 页网格 B1-C2，U2/U3 PT2042AD4、U4/U5 Finger |
| LED1-LED14 | WS2812C-2020 | 5V 供电的 14 颗串联 RGB LED，从 NEOPIXEL 输入逐级传递数据 | 图 ccc2ec45b8bc / 第 1 页 / 触控 RGB 页网格 A3-C4，LED1-LED14 WS2812C-2020 链 |

## 系统结构

### Voice Pyramid 系统架构

外接 Atom S3R 通过 G38/G39 I2C 与 G5-G8 I2S 网络控制 ES7210、ES8311、SI5351 和 AW87559；STM32G030F6P6 独立处理触摸、RGB 与 SPK_RST，USB-C/Grove 提供 5V 输入。

- 参数与网络：`host=U8 Atom S3R`；`coprocessor=U5 STM32G030F6P6`；`audio_adc=U2 ES7210`；`codec_dac=U3 ES8311`；`clock=U1 SI5351A-B-GTR`；`amplifier=U4 AW87559`；`input_power=USB-C or J2 Grove USB_IN`
- 证据：图 2ecdb3acbccf / 第 1 页 / 音频页完整 CODEC/DAC/SI5351/AMP/FPC 架构; 图 0828e8e77d40 / 第 1 页 / 主控电源页完整 Atom S3R/STM32/USB/Grove/供电架构; 图 ccc2ec45b8bc / 第 1 页 / 触控 RGB 页 PT2042AD4 与 LED1-LED14

## 电源

### USB_IN 到 USB_5V 电源路径

USB_IN 进入 U6 AW32901FCR 多个 IN 脚，OUT 形成 USB_5V；R25/R26 各 10KΩ 构成 ADC_CH3 分压，STM32 PA3 采样 ADC_CH3。

- 参数与网络：`input=USB_IN`；`device=U6 AW32901FCR`；`output=USB_5V`；`monitor=R25 10K/R26 10K -> ADC_CH3`；`adc=STM32 U5 PA3`
- 证据：图 0828e8e77d40 / 第 1 页 / 主控电源页网格 B2-C2，U6/R25/R26/ADC_CH3 与 U5 PA3

### AUDIO_VDD 生成

USB_5V 经 L2 100R@100MHz 磁珠和 C59/C61 滤波进入 U9 TPS7A2033PDBVR，U9 OUT 输出 AUDIO_VDD，C62 1uF/10V 对地。

- 参数与网络：`source=USB_5V`；`filter=L2 100R@100MHz,C59/C61`；`ldo=U9 TPS7A2033PDBVR`；`output=AUDIO_VDD`；`output_capacitor=C62 1uF/10V`
- 证据：图 0828e8e77d40 / 第 1 页 / 主控电源页网格 B2-B3，L2/U9/AUDIO_VDD

### Atom S3R 单向供电

U7 CH213K 的 VIN+ 接 USB_5V、VIN- 接 SYS_5V，页面标注“Atom_S3R单向供电”；J5 将 SYS_5V 与 SYS_3V3 引到系统连接器。

- 参数与网络：`device=U7 CH213K`；`vin_plus=USB_5V`；`vin_minus=SYS_5V`；`annotation=Atom_S3R单向供电`；`connector=J5 CONNECT_12P`；`system_rails=SYS_5V,SYS_3V3`
- 证据：图 0828e8e77d40 / 第 1 页 / 主控电源页网格 A3-A4，U7/J5 与单向供电箭头

## 接口

### USB Type-C 电源输入

USB_C_16P_Horizontal 的 VBUS 汇入 USB_IN，GND 与 SHIELD 接地，CC1/CC2 分别经 R18/R19 5.1KΩ 下拉；DP1/DN1/DP2/DN2 未接出数据网络。

- 参数与网络：`connector=USB_C_16P_Horizontal`；`vbus=USB_IN`；`ground=GND/SHIELD`；`cc1=R18 5.1K to GND`；`cc2=R19 5.1K to GND`；`usb_data=null`；`role=5V power sink`
- 证据：图 0828e8e77d40 / 第 1 页 / 主控电源页网格 A1，USB-C 全部引脚、R18/R19

### J2 Grove I2C 针脚

J2 pin1=I2C_SCL_G39、pin2=I2C_SDA_G38、pin3=USB_IN、pin4=GND；D9/D10 从 SCL/SDA 接 GND 提供接口防护。

- 参数与网络：`connector=J2 GROVE`；`pin1=I2C_SCL_G39`；`pin2=I2C_SDA_G38`；`pin3=USB_IN 5V`；`pin4=GND`；`protection=D9/D10 to GND`；`direction=I2C bidirectional`
- 证据：图 0828e8e77d40 / 第 1 页 / 主控电源页网格 B1，J2 pins1-4 与 D9/D10

### 左右侧 FPC 信号

CON1/CON2 各为 8 针 FPC：两者均含 GND、USB_5V、AUDIO_VDD；CON1 引出 TP_3、NEOPIXEL_1、TP_1，CON2 引出 TP_4、NEOPIXEL_2、TP_2 与 MIC_BIAS。

- 参数与网络：`left=CON1: TP_3,NEOPIXEL_1,TP_1,AUDIO_VDD,USB_5V,GND`；`right=CON2: TP_4,NEOPIXEL_2,TP_2,MIC_BIAS,AUDIO_VDD,USB_5V,GND`；`connector_type=FPC 8-pin`
- 证据：图 2ecdb3acbccf / 第 1 页 / 音频页网格 A3-A4，CON1/CON2 网络标注

## 总线

### G38/G39 系统 I2C 总线

I2C_SDA_G38 与 I2C_SCL_G39 连接 Atom S3R、J2 Grove、ES7210、ES8311、SI5351、AW87559，并在 STM32 侧映射为 STM_SDA/STM_SCL；R23/R22 各 4.7KΩ 上拉到 MAIN_3V3。

- 参数与网络：`controller=Atom S3R G38/G39`；`sda=I2C_SDA_G38`；`scl=I2C_SCL_G39`；`devices=ES7210,ES8311,SI5351,AW87559,STM32G030F6P6`；`external=J2 Grove pins2/1`；`pullups=R23 SDA 4.7K,R22 SCL 4.7K to MAIN_3V3`
- 证据：图 2ecdb3acbccf / 第 1 页 / 音频页各 U1-U4 的 I2C_SDA_G38/I2C_SCL_G39; 图 0828e8e77d40 / 第 1 页 / 主控电源页 U8/J2/U5 与 R22/R23

### 主控与音频器件 I2S

I2S_SCLK_GPIO6 与 I2S_LRCK_GPIO8 同时连接 ES7210 和 ES8311；ES7210 ASDOUT 连接 I2S_ASDOUT_MISO_GPIO5，主控 I2S_DIN_MOSI_GPIO7 连接 ES8311 DSDIN。

- 参数与网络：`host=Atom S3R`；`bit_clock=G6 I2S_SCLK_GPIO6`；`frame_clock=G8 I2S_LRCK_GPIO8`；`adc_to_host=ES7210 ASDOUT -> G5 I2S_ASDOUT_MISO_GPIO5`；`host_to_dac=G7 I2S_DIN_MOSI_GPIO7 -> ES8311 DSDIN`
- 证据：图 2ecdb3acbccf / 第 1 页 / 音频页 U2/U3 SCLK/LRCK/ASDOUT/DSDIN 与右下跨页网络

## 总线地址

### ES8311 I2C 地址

原理图标注 ES8311 CE 低为 0x18、CE 高为 0x19；U3 CE pin20 接 GND，因此本板地址为 0x18。

- 参数与网络：`device=U3 ES8311`；`address_7bit=0x18`；`ce=GND`；`ce_high_address=0x19`
- 证据：图 2ecdb3acbccf / 第 1 页 / 音频页 U3 上方 ES8311 address 注释与 CE pin20 接 GND

### SI5351 I2C 地址

U1 SI5351A-B-GTR 下方明确标注 0x60。

- 参数与网络：`device=U1 SI5351A-B-GTR`；`address_7bit=0x60`；`bus=I2C_SCL_G39/I2C_SDA_G38`
- 证据：图 2ecdb3acbccf / 第 1 页 / 音频页网格 C1-D2，U1 SI5351 与 0x60 标注

### AW87559 I2C 地址

U4 AW87559 上方明确标注 0x5B。

- 参数与网络：`device=U4 AW87559`；`address_7bit=0x5B`；`bus=I2C_SCL_G39/I2C_SDA_G38`
- 证据：图 2ecdb3acbccf / 第 1 页 / 音频页网格 C3，U4 AW87559 与 0x5B 标注

## GPIO 与控制信号

### STM32 触摸/RGB/功放控制

STM32 PA0=GPIOA_0/TP_1、PA1=GPIOA_1/TP_2、PA4=TP_4_audio、PA5=TP_3_audio、PA6=TIM3_CH1/NEOPIXEL_2、PA7=NEOPIXEL_1，PB7=GPIOB_7/SPK_RST。

- 参数与网络：`PA0=TP_1`；`PA1=TP_2`；`PA4=TP_4`；`PA5=TP_3`；`PA6=TIM3_CH1/NEOPIXEL_2`；`PA7=NEOPIXEL_1`；`PB7=SPK_RST`
- 证据：图 0828e8e77d40 / 第 1 页 / 主控电源页网格 C1-D4，U5 GPIO 标签与 TP10-TP14 网络映射

### 14 颗 WS2812C RGB 链

触控 RGB 页显示 LED1-LED14 共 14 颗 WS2812C-2020，全部由 5V0 供电，NEOPIXEL 接 LED1 DI，随后各级 DO 接下一颗 DI，LED14 DO 未继续连接。

- 参数与网络：`input=NEOPIXEL`；`count_shown=14`；`parts=LED1-LED14 WS2812C-2020`；`supply=5V0`；`topology=daisy chain`；`last_output=LED14 DO NC`
- 证据：图 ccc2ec45b8bc / 第 1 页 / 触控 RGB 页网格 A3-C4，NEOPIXEL 与 LED1-LED14

## 时钟

### SI5351 音频主时钟

U1 SI5351 使用 X1 27MHZ 10pF 晶体，时钟输出经 22Ω 串联电阻形成 I2S_MCLK_DAC 与 I2S_MCLK_ADC，分别连接 ES8311 MCLK 与 ES7210 MCLK。

- 参数与网络：`generator=U1 SI5351A-B-GTR`；`crystal=X1 27MHZ 10pF`；`dac_clock=I2S_MCLK_DAC -> ES8311 MCLK`；`adc_clock=I2S_MCLK_ADC -> ES7210 MCLK`；`series_resistors=R27/R28 22R/1%`
- 证据：图 2ecdb3acbccf / 第 1 页 / 音频页网格 C1-D2，X1/U1/R27/R28 与 I2S_MCLK_ADC/DAC

## 保护电路

### 外部接口与扬声器保护

J2 Grove 的 I2C_SCL/SDA 各由 D9/D10 接 GND防护；Atom 接口的 G5/G6/G7/G8/G38/G39 各有到 GND 的离散防护器件；扬声器 VOP/VON 由 D1/D2 SMF16CA 防护。

- 参数与网络：`grove=D9/D10 on G39/G38`；`atom_gpio=six protection devices on G5/G6/G7/G8/G38/G39`；`speaker=D1/D2 SMF16CA on VOP/VON`
- 证据：图 0828e8e77d40 / 第 1 页 / 主控电源页网格 B1 与 C3-D3，D9/D10 及六路 GPIO 防护; 图 2ecdb3acbccf / 第 1 页 / 音频页网格 C4，D1/D2 SMF16CA

## 音频

### ES7210 麦克风采集路径

ES7210 MIC1N/MIC1P 通过 C3/C4 1uF 接 AMIC1_N/AMIC1_P，FPC1 将 AMIC1_N/P、AUDIO_VDD 和 GND 引到麦克风子板；MIC_BIAS 从 U2 pin24 引出到 CON2。

- 参数与网络：`adc=U2 ES7210`；`channel=MIC1N/MIC1P`；`coupling=C3/C4 1uF/25V`；`connector=FPC1 pins3/4 AMIC1_N/P`；`power=FPC1 pin1 AUDIO_VDD,pin2 GND`；`bias=U2 pin24 MIC_BIAS -> CON2 pin7 via R15 10R`
- 证据：图 2ecdb3acbccf / 第 1 页 / 音频页网格 A1-B4，U2 MIC1、MIC_BIAS、FPC1 与 CON2

### ES8311 差分 DAC 输出

ES8311 OUTP/OUTN 通过 C30/C29 1uF/25V 形成 DAC_P/DAC_N；两路分别送入 AW87559 INP/INN，并并行进入 AEC 被动网络。

- 参数与网络：`dac=U3 ES8311`；`positive=OUTP -> C30 1uF -> DAC_P`；`negative=OUTN -> C29 1uF -> DAC_N`；`amplifier=AW87559 INP/INN via C37/C38 68nF/50V`；`aec=DAC_P/DAC_N -> passive AEC network`
- 证据：图 2ecdb3acbccf / 第 1 页 / 音频页网格 B1-D4，U3 OUTP/N、C29/C30、DAC_P/N、AEC 与 U4 INP/N

### AW87559 扬声器输出

AW87559 由 USB_5V 供电，SPK_RST 控制 RSTN，差分 VOP/VON 经输出磁性/滤波器件连接 2 针扬声器接口；D1/D2 SMF16CA 分别对 VOP/VON 提供到 GND 的 TVS 防护。

- 参数与网络：`amplifier=U4 AW87559`；`supply=USB_5V`；`reset=SPK_RST -> RSTN`；`input=DAC_P/DAC_N`；`output=VOP/VON differential`；`connector=2-pin speaker`；`protection=D1/D2 SMF16CA to GND`
- 证据：图 2ecdb3acbccf / 第 1 页 / 音频页网格 C3-D4，U4 电源/复位/输入/输出与 D1/D2

## 传感器

### PT2042AD4 触摸检测

触控 RGB 页显示 U2/U3 PT2042AD4 由 MIC_VDD 供电，QD 输出分别为 TP_OUT_1/TP_OUT_2并由 R1/R3 4.7KΩ 上拉；TCH 经 R2/R4 2KΩ 与 C4/C5 12pF 连接 U4/U5 Finger 电极。

- 参数与网络：`devices=U2/U3 PT2042AD4`；`supply=MIC_VDD`；`outputs=TP_OUT_1,TP_OUT_2`；`output_pullups=R1/R3 4.7K`；`touch_series=R2/R4 2K`；`touch_caps=C4/C5 12pF`；`electrodes=U4/U5 Finger`
- 证据：图 ccc2ec45b8bc / 第 1 页 / 触控 RGB 页网格 B1-C2，U2/U3/R1-R4/C4/C5/U4/U5

## 调试与烧录

### STM32 SWD/复位接口

J3 ISP pin1=SYS_3V3、pin2=SWCLK、pin3=SWDIO、pin4=RST、pin5=GND；SWDIO/SWCLK 连接 STM32 pins18/19，RST 连接 pin6。

- 参数与网络：`connector=J3 ISP`；`pin1=SYS_3V3`；`pin2=SWCLK`；`pin3=SWDIO`；`pin4=RST`；`pin5=GND`；`target=U5 STM32G030F6P6`
- 证据：图 0828e8e77d40 / 第 1 页 / 主控电源页网格 C1-D2，U5 RST/SWDIO/SWCLK 与 J3

## 模拟电路

### DAC 到 ES7210 的 AEC 回灌网络

DAC_P/DAC_N 经对称 R6/R7、C41/C42、R8/R9、R10/R11、R13/R14 与 C51/C52 网络形成 AEC_P/AEC_N，并经 C24/C25 1uF/25V 接入 ES7210 MIC3P/MIC3N。

- 参数与网络：`source=DAC_P/DAC_N`；`series=R6/R7 2.2K,R8/R9 10K,R10/R11 20K,R13/R14 0R`；`capacitors=C41/C42 0.47uF,C51/C52 0.22uF`；`destination=AEC_P/AEC_N -> C25/C24 -> ES7210 MIC3P/MIC3N`；`shunt=R12 4.3K,R16 NC and C43/C50`
- 证据：图 2ecdb3acbccf / 第 1 页 / 音频页网格 B3-C4，AEC 对称被动网络及 U2 MIC3P/N

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Voice Pyramid 系统架构 | `host=U8 Atom S3R`；`coprocessor=U5 STM32G030F6P6`；`audio_adc=U2 ES7210`；`codec_dac=U3 ES8311`；`clock=U1 SI5351A-B-GTR`；`amplifier=U4 AW87559`；`input_power=USB-C or J2 Grove USB_IN` |
| 总线 | G38/G39 系统 I2C 总线 | `controller=Atom S3R G38/G39`；`sda=I2C_SDA_G38`；`scl=I2C_SCL_G39`；`devices=ES7210,ES8311,SI5351,AW87559,STM32G030F6P6`；`external=J2 Grove pins2/1`；`pullups=R23 SDA 4.7K,R22 SCL 4.7K to MAIN_3V3` |
| 总线 | 主控与音频器件 I2S | `host=Atom S3R`；`bit_clock=G6 I2S_SCLK_GPIO6`；`frame_clock=G8 I2S_LRCK_GPIO8`；`adc_to_host=ES7210 ASDOUT -> G5 I2S_ASDOUT_MISO_GPIO5`；`host_to_dac=G7 I2S_DIN_MOSI_GPIO7 -> ES8311 DSDIN` |
| 总线地址 | ES8311 I2C 地址 | `device=U3 ES8311`；`address_7bit=0x18`；`ce=GND`；`ce_high_address=0x19` |
| 总线地址 | SI5351 I2C 地址 | `device=U1 SI5351A-B-GTR`；`address_7bit=0x60`；`bus=I2C_SCL_G39/I2C_SDA_G38` |
| 总线地址 | AW87559 I2C 地址 | `device=U4 AW87559`；`address_7bit=0x5B`；`bus=I2C_SCL_G39/I2C_SDA_G38` |
| 时钟 | SI5351 音频主时钟 | `generator=U1 SI5351A-B-GTR`；`crystal=X1 27MHZ 10pF`；`dac_clock=I2S_MCLK_DAC -> ES8311 MCLK`；`adc_clock=I2S_MCLK_ADC -> ES7210 MCLK`；`series_resistors=R27/R28 22R/1%` |
| 音频 | ES7210 麦克风采集路径 | `adc=U2 ES7210`；`channel=MIC1N/MIC1P`；`coupling=C3/C4 1uF/25V`；`connector=FPC1 pins3/4 AMIC1_N/P`；`power=FPC1 pin1 AUDIO_VDD,pin2 GND`；`bias=U2 pin24 MIC_BIAS -> CON2 pin7 via R15 10R` |
| 音频 | ES8311 差分 DAC 输出 | `dac=U3 ES8311`；`positive=OUTP -> C30 1uF -> DAC_P`；`negative=OUTN -> C29 1uF -> DAC_N`；`amplifier=AW87559 INP/INN via C37/C38 68nF/50V`；`aec=DAC_P/DAC_N -> passive AEC network` |
| 模拟电路 | DAC 到 ES7210 的 AEC 回灌网络 | `source=DAC_P/DAC_N`；`series=R6/R7 2.2K,R8/R9 10K,R10/R11 20K,R13/R14 0R`；`capacitors=C41/C42 0.47uF,C51/C52 0.22uF`；`destination=AEC_P/AEC_N -> C25/C24 -> ES7210 MIC3P/MIC3N`；`shunt=R12 4.3K,R16 NC and C43/C50` |
| 音频 | AW87559 扬声器输出 | `amplifier=U4 AW87559`；`supply=USB_5V`；`reset=SPK_RST -> RSTN`；`input=DAC_P/DAC_N`；`output=VOP/VON differential`；`connector=2-pin speaker`；`protection=D1/D2 SMF16CA to GND` |
| 接口 | USB Type-C 电源输入 | `connector=USB_C_16P_Horizontal`；`vbus=USB_IN`；`ground=GND/SHIELD`；`cc1=R18 5.1K to GND`；`cc2=R19 5.1K to GND`；`usb_data=null`；`role=5V power sink` |
| 接口 | J2 Grove I2C 针脚 | `connector=J2 GROVE`；`pin1=I2C_SCL_G39`；`pin2=I2C_SDA_G38`；`pin3=USB_IN 5V`；`pin4=GND`；`protection=D9/D10 to GND`；`direction=I2C bidirectional` |
| 电源 | USB_IN 到 USB_5V 电源路径 | `input=USB_IN`；`device=U6 AW32901FCR`；`output=USB_5V`；`monitor=R25 10K/R26 10K -> ADC_CH3`；`adc=STM32 U5 PA3` |
| 电源 | AUDIO_VDD 生成 | `source=USB_5V`；`filter=L2 100R@100MHz,C59/C61`；`ldo=U9 TPS7A2033PDBVR`；`output=AUDIO_VDD`；`output_capacitor=C62 1uF/10V` |
| 电源 | Atom S3R 单向供电 | `device=U7 CH213K`；`vin_plus=USB_5V`；`vin_minus=SYS_5V`；`annotation=Atom_S3R单向供电`；`connector=J5 CONNECT_12P`；`system_rails=SYS_5V,SYS_3V3` |
| GPIO 与控制信号 | STM32 触摸/RGB/功放控制 | `PA0=TP_1`；`PA1=TP_2`；`PA4=TP_4`；`PA5=TP_3`；`PA6=TIM3_CH1/NEOPIXEL_2`；`PA7=NEOPIXEL_1`；`PB7=SPK_RST` |
| 调试与烧录 | STM32 SWD/复位接口 | `connector=J3 ISP`；`pin1=SYS_3V3`；`pin2=SWCLK`；`pin3=SWDIO`；`pin4=RST`；`pin5=GND`；`target=U5 STM32G030F6P6` |
| 传感器 | PT2042AD4 触摸检测 | `devices=U2/U3 PT2042AD4`；`supply=MIC_VDD`；`outputs=TP_OUT_1,TP_OUT_2`；`output_pullups=R1/R3 4.7K`；`touch_series=R2/R4 2K`；`touch_caps=C4/C5 12pF`；`electrodes=U4/U5 Finger` |
| GPIO 与控制信号 | 14 颗 WS2812C RGB 链 | `input=NEOPIXEL`；`count_shown=14`；`parts=LED1-LED14 WS2812C-2020`；`supply=5V0`；`topology=daisy chain`；`last_output=LED14 DO NC` |
| 接口 | 左右侧 FPC 信号 | `left=CON1: TP_3,NEOPIXEL_1,TP_1,AUDIO_VDD,USB_5V,GND`；`right=CON2: TP_4,NEOPIXEL_2,TP_2,MIC_BIAS,AUDIO_VDD,USB_5V,GND`；`connector_type=FPC 8-pin` |
| 保护电路 | 外部接口与扬声器保护 | `grove=D9/D10 on G39/G38`；`atom_gpio=six protection devices on G5/G6/G7/G8/G38/G39`；`speaker=D1/D2 SMF16CA on VOP/VON` |
| 系统结构 | 原理图资源页完整性 | `available_pdf_pages=1,2,4`；`missing_pdf_page=3`；`complete_bom=null`；`complete_cross_page_nets=null` |
| 总线地址 | 正文 ES7210 与 STM32 I2C 地址 | `documented_es7210=0x40`；`es7210_ad0=GND`；`es7210_ad1=GND`；`documented_stm32=0x1A`；`stm32_firmware_address=null` |
| 音频 | 正文麦克风型号与 AEC 性能 | `documented_microphone=LMA3729T381-0Y3S`；`confirmed_input=AMIC1_P/N`；`confirmed_aec_feedback=DAC_P/N -> AEC_P/N -> ES7210 MIC3`；`microphone_count=null`；`array_geometry=null`；`sensitivity=null`；`gain=null`；`aec_algorithm=null` |
| GPIO 与控制信号 | 正文 28 颗 RGB LED | `documented_total=28`；`documented_per_bar=14`；`shown_chain=LED1-LED14`；`shown_channels=NEOPIXEL_1,NEOPIXEL_2`；`second_chain_details=null` |
| 电源 | 正文 5V 与功耗参数 | `documented_input=DC 5V`；`documented_standby=14.92mA`；`documented_max_audio=578.47mA`；`input_range=null`；`current_limit=null`；`fuse_rating=null`；`measurement_conditions=null` |

## 待确认事项

- `system.missing-pdf-page-3`：资源 URL 依次对应 sche_ECHOPyramid_page_01、page_02 与 page_04，没有 page_03；因此现有三页不能证明已覆盖完整 PDF 的全部器件和跨页网络。（证据：图 2ecdb3acbccf / 第 1 页 / 资源 URL sche_ECHOPyramid_page_01.png; 图 0828e8e77d40 / 第 1 页 / 资源 URL sche_ECHOPyramid_page_02.png; 图 ccc2ec45b8bc / 第 1 页 / 资源 URL sche_ECHOPyramid_page_04.png）
- `address.documented-es7210-stm32`：正文管脚表列出 ES7210=0x40、STM32G030F6P6=0x1A；现有页面显示 ES7210 AD0/AD1 接 GND和 STM32 I2C 网络，但没有直接写出 0x40/0x1A，也未显示 STM32 从机地址固件实现。（证据：图 2ecdb3acbccf / 第 1 页 / 音频页 U2 ES7210 AD0/AD1 与 I2C 网络，无 0x40 文本; 图 0828e8e77d40 / 第 1 页 / 主控电源页 U5 STM32 STM_SCL/STM_SDA，无 0x1A 文本）
- `audio.documented-microphones-aec`：正文列出 LMA3729T381-0Y3S 麦克风、ES7210 麦克风采集和 AEC 回声消除；音频页确认 AMIC1 与 DAC 回灌网络，但缺失第 3 页，无法确认麦克风数量、准确型号、阵列几何、灵敏度、增益和 AEC 算法/性能。（证据：图 2ecdb3acbccf / 第 1 页 / 音频页 ES7210 AMIC1/MIC3、FPC1 与 AEC 网络；麦克风实体页不在资源中）
- `gpio.documented-28-rgb`：正文规格称共有 28 颗 WS2812、每条 RGB Bar 14 颗；现有 page_04 只明确画出一条 LED1-LED14 链，page_01 显示 NEOPIXEL_1/2 两路接口，但第二条 14 颗链未在现有资源中展开。（证据：图 ccc2ec45b8bc / 第 1 页 / 触控 RGB 页仅显示 LED1-LED14 一条链; 图 2ecdb3acbccf / 第 1 页 / 音频页 CON1/CON2 引出 NEOPIXEL_1/NEOPIXEL_2）
- `power.documented-input-consumption`：正文称输入 DC 5V、无主控待机 14.92mA、连接主控最大音量 578.47mA；原理图确认 USB_IN/USB_5V/SYS_5V/AUDIO_VDD 路径，但没有输入允许范围、保险丝额定值、限流阈值、测试条件或功耗标注。（证据：图 0828e8e77d40 / 第 1 页 / 主控电源页 USB_IN/USB_5V/SYS_5V/AUDIO_VDD 路径，无功耗参数）
- `review.missing-page-3`：请补充 Voice Pyramid 正式原理图 PDF 第 3 页并核对完整 BOM、麦克风子板、第二触控 RGB 条和跨页网络。；原因：资源清单只有 PDF 第 1、2、4 页。
- `review.i2c-addresses`：请由 ES7210 datasheet、STM32 内置固件和总线扫描确认 0x40 与 0x1A，并确认地址修改与冲突处理。；原因：地址仅见正文，现有原理图未直接写出。
- `review.microphones-aec`：请确认麦克风数量/型号/阵列位置、ES7210 增益与采样配置，以及 AEC 是模拟回灌、固件算法还是组合实现及其指标。；原因：缺少麦克风实体页和音频配置资料。
- `review.rgb-count`：请用第 3 页或装配 BOM 确认第二条 14 颗 WS2812C 链、总数 28、两路数据方向和供电分配。；原因：现有页面只展开一条 14 颗链。
- `review.power-consumption`：请确认 5V 输入范围、USB-C/Grove 反灌边界、U6 限流/保护阈值、各电源轨电流预算及 14.92mA/578.47mA 测试条件。；原因：原理图未给额定范围与功耗数据。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `2ecdb3acbccf6e5d9614a7911c96f15f8e36d40d6f6a60a160798b98547cd567` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1214/sche_ECHOPyramid_page_01.png` |
| 2 | 1 | `0828e8e77d400acff2f396e134d9aa959f1d6ae57e9e464f8da0ac7d3ef23e92` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1214/sche_ECHOPyramid_page_02.png` |
| 3 | 1 | `ccc2ec45b8bc322a054a253fa04b4b3079342d3d8b6537a3c21a0c7772a3b08e` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1214/sche_ECHOPyramid_page_04.png` |

---

源文档：`zh_CN/atom/Echo_Pyramid.md`

源文档 SHA-256：`303c29f29f7516e3b7fdf103733026d99c28e6368dce23f2f2e08537183b544a`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
