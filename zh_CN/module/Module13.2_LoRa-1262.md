# Module13.2 LoRa-1262

<span class="product-sku">SKU:M149</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/coming-soon.png">
</PictureViewer>

## 描述

**Module13.2 LoRa-1262** 是一款基于 Stamp LoRa-1262 的 M5Stack 堆叠式 LoRa 通信模块，内部集成 SX1262 LoRa 射频收发器，**支持 868 ~ 923 MHz 频段**，与主控通过 SPI 接口通信，模块板载 RP-SMA 天线接口，并通过拨码开关灵活配置 **NSS**、**BUSY** 和 **IRQ** 引脚，可适配不同主控设备的 GPIO 配置。

模块还集成了基于 I2C 协议的 IO 扩展芯片，用于控制 LoRa 模组复位、旁通、关断、3.3V 电源。IO 扩展芯片的 I2C 地址由 SW2 的 A、B 拨码位选择，可在 0x71 ~ 0x74 范围内配置，多个模块堆叠使用时可为每个模块设置不同的 I2C 地址，适用于远程监测、智能家居、工业自动化和物联网 (IoT) 等应用场景。

## 注意事项

!> 天线连接 | 使用 LoRa 模块前请先连接匹配的外置天线，禁止在未连接天线的情况下进行发射，否则设备硬件可能会永久损坏！

## 产品特性

- 集成 Stamp LoRa-1262 模组 (基于 SX1262)
- 支持 868 ~ 923 MHz 工作频段
- 支持 SPI 串行通信协议
- 支持 FSK、GFSK、MSK、GMSK、LoRa 和 OOK 调制模式
- LoRa 最大发射功率约 +22 dBm，接收灵敏度低至 -147 dBm（LoRa 低速率模式下）
- 板载 RP-SMA 外置天线接口
- DIP 拨码开关灵活切换 NSS、BUSY 和 IRQ 引脚
- IO 扩展芯片支持 4 档 I2C 地址选择
- 支持多个模块堆叠使用
- 开发平台：
  - Arduino
  - UiFlow2

## 包装内容

- 1 x Module13.2 LoRa-1262
- 1 x 868 MHz RP-SMA 胶棒天线

## 应用场景

- 远程监测
- 智能家居
- 工业自动化
- 物联网 (IoT) 设备

## 规格参数

| 规格                 | 参数                                                                                                                                                                   |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| LoRa 模组            | Stamp LoRa-1262                                                                                                                                                        |
| 工作频段             | 868 ~ 923 MHz                                                                                                                                                          |
| 通信接口             | SPI                                                                                                                                                                    |
| 天线规格             | 长 108mm，接口类型 RP-SMA（内螺内孔），工作频段 868 MHz，增益 3dBi                                                                                                     |
| 支持调制方式         | FSK / GFSK / MSK / GMSK / LoRa / OOK                                                                                                                                   |
| 发射功率             | 最大约为 +22 dBm                                                                                                                                                       |
| 接收灵敏度           | -147 dBm (LoRa 低速率模式)                                                                                                                                             |
| 天线接口             | RP-SMA                                                                                                                                                                 |
| 拉距实测             | 62.5kHz: 3.8 km<br>125kHz: 3.6 km<br>500kHz: 2.7 km                                                                                                                    |
| 工作功耗             | LoRa 模块最大功率传输数据：<br>发送: **4.2V** @ 277.45 mA / **5V** @ 137.10 mA / **12V** @ 71.38 mA<br>接收: **4.2V** @ 174.52 mA/ **5V** @ 9.94 mA / **12V** @ 4.5 mA |
| IO 拓展芯片 I2C 地址 | 0x71 ~ 0x74，拨码开关控制                                                                                                                                              |
| 待机功耗             | LoRa 模块待机或睡眠：**4.2V** @ 79.4 uA / **5V** @ 693.03 uA / **12V** @ 1.06 mA<br>LoRa 模块电源关闭： **5V** @ 2.76 uA                                               |
| 工作电压             | DC 9 ~ 24V                                                                                                                                                             |
| 工作电流             | DC 5V@163.4mA                                                                                                                                                          |
| 产品尺寸             | 59.1 x 54.0 x 20.2mm                                                                                                                                                   |
| 产品重量             | XXXg（不含天线）                                                                                                                                                       |
| 包装尺寸             | XXX x XXX x XXXmm                                                                                                                                                      |
| 毛重                 | XXXg                                                                                                                                                                   |

## 原理图

- [Module13.2 LoRa-1262 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1277/SCH_Module13.2_LoRa1262_V1.0_2026_09_02_17_15_18.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1277/SCH_Module13.2_LoRa1262_V1.0_2026_09_02_17_15_18_page_01.png">
</SchViewer>

## 管脚映射

### M5-Bus

\#> DIP Switch | 下方 M5-Bus 中标记 `SW1` 和 `SW3` 的引脚，可通过拨码开关进行切换，用于适配不同的主控设备。

::m5-bus-table
| PIN        | LEFT | RIGHT | PIN        |
| ---------- | ---- | ----- | ---------- |
| GND        | 1    | 2     | IRQ (SW3)  |
| GND        | 3    | 4     | BUSY (SW1) |
| GND        | 5    | 6     | EN         |
| MOSI       | 7    | 8     | BUSY (SW1) |
| MISO       | 9    | 10    | IRQ (SW3)  |
| SCK        | 11   | 12    | 3V3        |
|            | 13   | 14    |            |
|            | 15   | 16    |            |
| SDA        | 17   | 18    | SCL        |
| BUSY (SW1) | 19   | 20    | NSS (SW1)  |
| NSS (SW1)  | 21   | 22    | BUSY (SW1) |
| NSS (SW1)  | 23   | 24    | NSS (SW1)  |
| HPWR       | 25   | 26    | IRQ (SW3)  |
| HPWR       | 27   | 28    | 5V         |
| HPWR       | 29   | 30    | VBAT       |
::

<!--todo:补引脚切换开关示意图-->

### IO_EXP

| IO_EXP 引脚 | 连接信号           | 功能说明         |
| ----------- | ------------------ | ---------------- |
| IO2         | `PY_IO2_LORA_RST`  | LoRa 模组复位    |
| IO3         | `PY_IO3_BYPASS`    | LoRa Bypass 控制 |
| IO5         | `PY_IO5_PWR_EN`    | 3.3V 电源使能    |
| I2C_SDA     | `SDA`              | I2C 数据         |
| I2C_SCL     | `SCL`              | I2C 时钟         |
| ADD_SEL     | `ADD_SEL`          | I2C 地址选择     |

### I2C 地址选择

通过 SW2 的 `A`、`B` 两个地址选择位，可以为 IO_EXP 配置以下 I2C 地址。多个模块堆叠使用时，请为每个模块设置不同的地址。

| A   | B   | I2C 地址 |
| --- | --- | -------- |
| 0   | 0   | 0x74     |
| 1   | 0   | 0x73     |
| 0   | 1   | 0x72     |
| 1   | 1   | 0x71     |

## 尺寸图

......

## 数据手册

- [SX1262 数据手册](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1177/DS_SX1261_2_V2-2.pdf)
- [M5IOE1 IO 拓展管理芯片](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1210/IO_Expander_Datasheet_CN.pdf)

## 软件开发

### Arduino

- [Module13.2 LoRa-1262 Arduino 驱动库](https://github.com/jgromes/RadioLib)
- [Module13.2 LoRa-1262 Arduino 快速上手](/zh_CN/arduino/projects/module/module13.2_lora-1262)
