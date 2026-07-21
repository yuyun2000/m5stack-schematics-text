# Unit VMeter 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit VMeter |
| SKU | U087 |
| 产品 ID | `unit-vmeter-9e126bbd9b81` |
| 源文档 | `zh_CN/unit/vmeter.md` |

## 概述

Unit VMeter 功能框图以 ADS1115 16bit ADC 为采集核心，图面标注地址 0x49；正负测量端通过 680K/11K 衰减网络和 2.5V BIAS 接入 AIN1/AIN0。ADS1115 位于 5V/GND B 隔离域，其 I2C 经 CA IS3020S 跨隔离边界连接 PORT.A 主机侧；主机侧 EEPROM 地址为 0x53。PORT.A 提供 SCL、SDA、5V、GND，LDO 生成主机侧 3.3V，ISO DC-DC 生成隔离侧 5V/GND B。该资源是功能框图而非带位号原理图，未给出 ±36V 量程、精度/分辨率、隔离耐压、EEPROM 校准内容或电源指示灯电路。

## 检索关键词

`Unit VMeter`、`U087`、`ADS1115`、`16bit ADC`、`0x49`、`CA IS3020S`、`CA-IS3020S`、`EEPROM`、`E²PROM`、`0x53`、`ISO DC-DC`、`LDO`、`BIAS`、`2.5V`、`680K`、`11K`、`AIN0`、`AIN1`、`PORT.A I2C`、`SCL`、`SDA`、`5V`、`3.3V`、`GND A`、`GND B`、`isolated I2C`、`isolated voltage measurement`、`±36V`、`1000 VRMS`、`calibration EEPROM`、`voltage divider`、`differential ADC`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| ADS1115 block | ADS1115 | 16 位隔离侧 ADC，采集 AIN0/AIN1 并通过 I2C 通信，图面地址 0x49 | 图 f001298a771a / 第 1 页 / 页 1 中部 ADS1115 16bit ADC 方框，标注 Addr 0x49、AIN0/AIN1、I2C、5V/GND B |
| CA IS3020S block | CA IS3020S | 跨隔离边界连接 ADS1115 与 PORT.A 主机侧的双通道 I2C 数字隔离器 | 图 f001298a771a / 第 1 页 / 页 1 中下 CA IS3020S 方框跨橙色虚线隔离边界，上接 ADS1115 I2C，下接主机侧总线 |
| EEPROM block | 未标注 | 主机侧 I2C EEPROM，图面地址 0x53 | 图 f001298a771a / 第 1 页 / 页 1 下部蓝色 E²PROM 方框，标注 Addr 0x53 并连接 PORT.A I2C |
| ISO DC-DC block | 未标注 | 从 PORT.A 主机电源域向 5V/GND B 隔离域供电 | 图 f001298a771a / 第 1 页 / 页 1 右中绿色 ISO DC-DC 方框，跨隔离边界连接下方 PORT.A 电源与上方 5V/GND B |
| LDO block | 未标注 | 将 PORT.A 5V 转换为主机侧 3.3V，为隔离器与 EEPROM 侧供电 | 图 f001298a771a / 第 1 页 / 页 1 右下蓝色 LDO 方框，连接 PORT.A 5V/GND 与 3.3V/GND A |
| BIAS block | 未标注 | 在隔离侧 5V/GND B 电源域生成 2.5V 模拟偏置 | 图 f001298a771a / 第 1 页 / 页 1 右中 BIAS 方框，连接 GND B、5V 与 2.5V |
| 680K/11K network | 680K / 11K | 将正负测量端电压衰减并送入 ADS1115 AIN1/AIN0 | 图 f001298a771a / 第 1 页 / 页 1 上中，正端-680K-AIN1-11K-AIN0/负端/2.5V 链路 |
| measurement terminals | 未标注 | 隔离侧正负电压测量输入端 | 图 f001298a771a / 第 1 页 / 页 1 顶部黑色负端与红色正端，位于 ISOLATED 标识上方并连接 680K/11K 网络 |
| PORT.A I2C block | 未标注 | 主机侧 SCL、SDA、5V、GND Grove 接口 | 图 f001298a771a / 第 1 页 / 页 1 底部 PORT.A I2C 方框及 SCL/SDA/5V/GND 四个色块 |

## 系统结构

### Unit VMeter 隔离测量架构

正负测量端经 680K/11K 与 2.5V BIAS 接入 ADS1115；ADS1115 I2C 经 CA IS3020S 隔离后连接 PORT.A，主机侧还挂接地址 0x53 的 EEPROM。

- 参数与网络：`adc=ADS1115 16bit,0x49`；`input=negative->AIN0/2.5V; positive->680K->AIN1; AIN1->11K->AIN0`；`isolator=CA IS3020S`；`eeprom=0x53`；`host_interface=PORT.A I2C`；`power=LDO 3.3V + ISO DC-DC 5V/GND B`
- 证据：图 f001298a771a / 第 1 页 / 页 1 完整功能框图：测量端、分压、ADS1115、隔离器、EEPROM、电源块与 PORT.A

## 核心器件

### ADS1115 ADC

图面标注 ADS1115、16bit ADC、Addr 0x49，并显示 AIN0/AIN1、I2C、5V 与 GND B 连接。

- 参数与网络：`device=ADS1115`；`resolution=16bit`；`address=0x49`；`analog_inputs=AIN0,AIN1`；`digital_bus=I2C`；`supply=5V`；`ground=GND B`
- 证据：图 f001298a771a / 第 1 页 / 页 1 中部 ADS1115 16bit ADC/Addr 0x49 方框及周边标签

### CA IS3020S

CA IS3020S 方框跨隔离边界，两侧分别使用隔离侧 5V/GND B 与主机侧 3.3V/GND A，并隔离两条 I2C 信号。

- 参数与网络：`device_label=CA IS3020S`；`isolated_supply=5V,GND B`；`host_supply=3.3V,GND A`；`channels=two I2C lines`；`pin_map=not shown`
- 证据：图 f001298a771a / 第 1 页 / 页 1 CA IS3020S 方框、上下两组信号与右侧 5V/3.3V 标签

## 电源

### 主机侧 LDO

PORT.A 5V/GND 连接 LDO 方框，LDO 输出标注 3.3V 并使用 GND A，为 CA IS3020S 主机侧与 EEPROM 域供电。

- 参数与网络：`input=PORT.A 5V`；`input_ground=GND A`；`output=3.3V`；`consumers=CA IS3020S host side,EEPROM domain`；`part_number=null`；`enable=not shown`
- 证据：图 f001298a771a / 第 1 页 / 页 1 右下 LDO 方框、3.3V/GND A 与 PORT.A 5V/GND 连线

### ISO DC-DC 隔离供电

ISO DC-DC 方框跨隔离边界，主机侧连接 PORT.A 5V/GND A，隔离侧输出 5V/GND B，为 ADS1115、BIAS 与 CA IS3020S 隔离侧供电。

- 参数与网络：`input=PORT.A 5V,GND A`；`output=5V,GND B`；`consumers=ADS1115,BIAS,CA IS3020S isolated side`；`part_number=null`；`enable=not shown`
- 证据：图 f001298a771a / 第 1 页 / 页 1 右中 ISO DC-DC 方框及上下 5V/GND A/GND B 电源路径

### GND A/GND B 电源域

PORT.A、EEPROM、LDO 与隔离器下侧属于 GND A/3.3V 主机域；ADS1115、BIAS 与隔离器上侧属于 GND B/5V 隔离域，图中未画 GND A 与 GND B 的导电连接。

- 参数与网络：`host_domain=GND A,3.3V,PORT.A,EEPROM`；`isolated_domain=GND B,5V,ADS1115,BIAS`；`domain_bridge=CA IS3020S + ISO DC-DC`；`galvanic_ground_connection=false`
- 证据：图 f001298a771a / 第 1 页 / 页 1 橙色隔离边界上下的 GND A/GND B 与 CA IS3020S/ISO DC-DC

## 接口

### 隔离侧正负测量端

顶部黑色负端连接 AIN0/2.5V 节点，红色正端连接 680K 电阻远端；两个输入均位于标注 ISOLATED 的隔离区域。框图未给端子针脚号或连接器型号。

- 参数与网络：`negative_terminal=AIN0 and 2.5V node`；`positive_terminal=680K high-side`；`domain=isolated,GND B`；`pin_numbers=not shown`；`connector_part=not shown`
- 证据：图 f001298a771a / 第 1 页 / 页 1 顶部负/正端子及其向下连接到 AIN0/680K 的线

### PORT.A I2C

PORT.A 底部从左到右明确标为 SCL、SDA、5V、GND，连接主机侧 I2C、电源和 GND A。图面未打印数字针脚号。

- 参数与网络：`position_1_left=SCL`；`position_2=SDA`；`position_3=5V`；`position_4_right=GND,GND A`；`signal_direction=I2C lines shown through isolator`；`pin_numbers=not shown`
- 证据：图 f001298a771a / 第 1 页 / 页 1 底部 PORT.A I2C 与 SCL/SDA/5V/GND 四个标签

## 总线

### ADS1115 到 PORT.A 的隔离 I2C

ADS1115 的两条 I2C 线进入 CA IS3020S 隔离器，跨橙色虚线隔离边界后连接主机侧 I2C，并继续到 PORT.A 的 SCL/SDA。

- 参数与网络：`isolated_device=ADS1115`；`isolator=CA IS3020S`；`host_connector=PORT.A`；`signals=SCL,SDA`；`isolated_ground=GND B`；`host_ground=GND A`；`pin_numbers=not shown`
- 证据：图 f001298a771a / 第 1 页 / 页 1 ADS1115-I2C-CA IS3020S-PORT.A 两条垂直信号线与隔离边界

### 其他外部总线

该框图只显示 I2C，未显示 SPI、UART、CAN、RS-485、USB、SDIO、MIPI 或 I2S。

- 参数与网络：`i2c=SCL,SDA`；`spi=null`；`uart=null`；`can=null`；`rs485=null`；`usb=null`；`sdio=null`；`mipi=null`；`i2s=null`
- 证据：图 f001298a771a / 第 1 页 / 页 1 PORT.A 与内部数字链路仅标 I2C/SCL/SDA

## 总线地址

### ADS1115 I2C 地址

功能框图明确标注 ADS1115 地址为 0x49。

- 参数与网络：`device=ADS1115`；`address=0x49`；`bus=isolated I2C`；`address_selector=not shown`
- 证据：图 f001298a771a / 第 1 页 / 页 1 ADS1115 方框黄色文字 Addr 0x49

### EEPROM I2C 地址

功能框图明确标注 EEPROM 地址为 0x53。

- 参数与网络：`device=E²PROM`；`address=0x53`；`bus=PORT.A host-side I2C`；`address_selector=not shown`
- 证据：图 f001298a771a / 第 1 页 / 页 1 E²PROM 方框黄色文字 Addr 0x53

## GPIO 与控制信号

### GPIO、时钟、复位与调试

框图未显示主控、GPIO 编号、BOOT、RESET、晶振/时钟、调试接口或测试点。

- 参数与网络：`controller=null`；`gpio_map=null`；`boot=null`；`reset=null`；`clock=null`；`debug_connector=null`；`test_points=null`
- 证据：图 f001298a771a / 第 1 页 / 页 1 完整功能框图，无 MCU/GPIO/时钟/复位/调试模块

## 保护电路

### I2C 与电源隔离

CA IS3020S 隔离 I2C，ISO DC-DC 隔离供电，测量/ADC 侧 GND B 与主机/PORT.A 侧 GND A 在图面分开。

- 参数与网络：`signal_isolation=CA IS3020S`；`power_isolation=ISO DC-DC`；`measurement_ground=GND B`；`host_ground=GND A`；`boundary=orange dashed line`
- 证据：图 f001298a771a / 第 1 页 / 页 1 CA IS3020S 与 ISO DC-DC 跨橙色虚线，GND A/GND B 分域

## 关键网络

### Unit VMeter 关键连接索引

关键链路为正端→680K→AIN1→11K→AIN0/负端/2.5V→ADS1115，ADS1115 I2C→CA IS3020S→PORT.A SCL/SDA，PORT.A 5V→LDO 3.3V 与 ISO DC-DC 5V/GND B，以及主机 I2C→EEPROM 0x53。

- 参数与网络：`analog=positive-680K-AIN1-11K-AIN0-negative/2.5V`；`adc=ADS1115 0x49`；`isolated_bus=ADS1115-CA IS3020S-PORT.A`；`host_memory=EEPROM 0x53`；`host_power=PORT.A 5V-LDO-3.3V/GND A`；`isolated_power=PORT.A 5V-ISO DC-DC-5V/GND B`
- 证据：图 f001298a771a / 第 1 页 / 页 1 完整功能框图所有模拟、I2C、地址和电源连线

## 内存与 Flash

### 主机侧 EEPROM

E²PROM 方框位于隔离器主机侧，连接 PORT.A I2C 总线并标注地址 0x53；图面未给 EEPROM 型号或容量。

- 参数与网络：`device=E²PROM`；`address=0x53`；`bus=host-side I2C`；`ground=GND A`；`part_number=null`；`capacity=null`
- 证据：图 f001298a771a / 第 1 页 / 页 1 下部 E²PROM/Addr 0x53 方框与 I2C 连线

## 模拟电路

### 680K/11K 输入衰减网络

正端经 680K 接到 AIN1，AIN1 再经 11K 接到 AIN0；AIN0 同时连接负端与 2.5V 偏置节点。

- 参数与网络：`positive_path=positive terminal->680K->AIN1`；`lower_leg=AIN1->11K->AIN0`；`negative_path=negative terminal->AIN0`；`bias=AIN0,2.5V`；`adc_inputs=AIN0,AIN1`
- 证据：图 f001298a771a / 第 1 页 / 页 1 上中 680K/11K/AIN0/AIN1/2.5V 与正负端完整连线

### 2.5V BIAS

BIAS 方框位于隔离侧，使用 5V 与 GND B，并输出标注 2.5V 的偏置到 AIN0/负端节点。

- 参数与网络：`input_supply=5V isolated side`；`ground=GND B`；`output=2.5V`；`destination=AIN0/negative terminal node`；`part_number=null`
- 证据：图 f001298a771a / 第 1 页 / 页 1 右中 BIAS 方框与 5V/GND B/2.5V 标签

## 其他事实

### 音频、射频与其他传感器

框图未显示音频器件、射频收发器、天线或除电压采样链路之外的独立传感器。

- 参数与网络：`audio=null`；`rf=null`；`antenna=null`；`other_sensor=null`；`voltage_measurement=ADS1115 analog chain`
- 证据：图 f001298a771a / 第 1 页 / 页 1 完整框图仅包含电压测量、I2C、存储与电源隔离

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit VMeter 隔离测量架构 | `adc=ADS1115 16bit,0x49`；`input=negative->AIN0/2.5V; positive->680K->AIN1; AIN1->11K->AIN0`；`isolator=CA IS3020S`；`eeprom=0x53`；`host_interface=PORT.A I2C`；`power=LDO 3.3V + ISO DC-DC 5V/GND B` |
| 接口 | 隔离侧正负测量端 | `negative_terminal=AIN0 and 2.5V node`；`positive_terminal=680K high-side`；`domain=isolated,GND B`；`pin_numbers=not shown`；`connector_part=not shown` |
| 模拟电路 | 680K/11K 输入衰减网络 | `positive_path=positive terminal->680K->AIN1`；`lower_leg=AIN1->11K->AIN0`；`negative_path=negative terminal->AIN0`；`bias=AIN0,2.5V`；`adc_inputs=AIN0,AIN1` |
| 模拟电路 | 2.5V BIAS | `input_supply=5V isolated side`；`ground=GND B`；`output=2.5V`；`destination=AIN0/negative terminal node`；`part_number=null` |
| 核心器件 | ADS1115 ADC | `device=ADS1115`；`resolution=16bit`；`address=0x49`；`analog_inputs=AIN0,AIN1`；`digital_bus=I2C`；`supply=5V`；`ground=GND B` |
| 总线地址 | ADS1115 I2C 地址 | `device=ADS1115`；`address=0x49`；`bus=isolated I2C`；`address_selector=not shown` |
| 总线 | ADS1115 到 PORT.A 的隔离 I2C | `isolated_device=ADS1115`；`isolator=CA IS3020S`；`host_connector=PORT.A`；`signals=SCL,SDA`；`isolated_ground=GND B`；`host_ground=GND A`；`pin_numbers=not shown` |
| 核心器件 | CA IS3020S | `device_label=CA IS3020S`；`isolated_supply=5V,GND B`；`host_supply=3.3V,GND A`；`channels=two I2C lines`；`pin_map=not shown` |
| 内存与 Flash | 主机侧 EEPROM | `device=E²PROM`；`address=0x53`；`bus=host-side I2C`；`ground=GND A`；`part_number=null`；`capacity=null` |
| 总线地址 | EEPROM I2C 地址 | `device=E²PROM`；`address=0x53`；`bus=PORT.A host-side I2C`；`address_selector=not shown` |
| 存储 | EEPROM 校准数据 | `device=EEPROM at 0x53`；`content=null`；`layout=null`；`capacity=null`；`write_protection=null`；`version=null`；`product_document_claim=factory calibration parameters` |
| 接口 | PORT.A I2C | `position_1_left=SCL`；`position_2=SDA`；`position_3=5V`；`position_4_right=GND,GND A`；`signal_direction=I2C lines shown through isolator`；`pin_numbers=not shown` |
| 电源 | 主机侧 LDO | `input=PORT.A 5V`；`input_ground=GND A`；`output=3.3V`；`consumers=CA IS3020S host side,EEPROM domain`；`part_number=null`；`enable=not shown` |
| 电源 | ISO DC-DC 隔离供电 | `input=PORT.A 5V,GND A`；`output=5V,GND B`；`consumers=ADS1115,BIAS,CA IS3020S isolated side`；`part_number=null`；`enable=not shown` |
| 电源 | GND A/GND B 电源域 | `host_domain=GND A,3.3V,PORT.A,EEPROM`；`isolated_domain=GND B,5V,ADS1115,BIAS`；`domain_bridge=CA IS3020S + ISO DC-DC`；`galvanic_ground_connection=false` |
| 保护电路 | I2C 与电源隔离 | `signal_isolation=CA IS3020S`；`power_isolation=ISO DC-DC`；`measurement_ground=GND B`；`host_ground=GND A`；`boundary=orange dashed line` |
| 保护电路 | 隔离耐压 | `schematic_rating=null`；`creepage=null`；`clearance=null`；`test_duration=null`；`product_document_value=1000 VRMS` |
| 模拟电路 | 电压测量范围、分辨率与精度 | `divider=680K/11K`；`bias=2.5V`；`adc=ADS1115 16bit`；`input_range=null`；`pga=null`；`conversion_formula=null`；`resolution=null`；`accuracy=null`；`product_document_range=±36V`；`product_document_accuracy=1% full scale ±1 digit` |
| 其他事实 | 电源指示灯 | `product_document_indicator=power LED`；`schematic_led=null`；`series_resistor=null`；`control_net=null` |
| 总线 | 其他外部总线 | `i2c=SCL,SDA`；`spi=null`；`uart=null`；`can=null`；`rs485=null`；`usb=null`；`sdio=null`；`mipi=null`；`i2s=null` |
| GPIO 与控制信号 | GPIO、时钟、复位与调试 | `controller=null`；`gpio_map=null`；`boot=null`；`reset=null`；`clock=null`；`debug_connector=null`；`test_points=null` |
| 其他事实 | 音频、射频与其他传感器 | `audio=null`；`rf=null`；`antenna=null`；`other_sensor=null`；`voltage_measurement=ADS1115 analog chain` |
| 关键网络 | Unit VMeter 关键连接索引 | `analog=positive-680K-AIN1-11K-AIN0-negative/2.5V`；`adc=ADS1115 0x49`；`isolated_bus=ADS1115-CA IS3020S-PORT.A`；`host_memory=EEPROM 0x53`；`host_power=PORT.A 5V-LDO-3.3V/GND A`；`isolated_power=PORT.A 5V-ISO DC-DC-5V/GND B` |

## 待确认事项

- `storage.calibration-content-not-shown`：框图确认地址 0x53 的 EEPROM，但未标注其存储布局、校准参数格式、容量、写保护或校准版本。（证据：图 f001298a771a / 第 1 页 / 页 1 E²PROM/Addr 0x53 方框仅给地址，无内容或保护说明）
- `protection.isolation-rating-not-shown`：框图显示信号与电源隔离拓扑，但未打印隔离耐压、爬电距离、电气间隙或测试条件。（证据：图 f001298a771a / 第 1 页 / 页 1 ISOLATED 标识、隔离虚线、CA IS3020S 与 ISO DC-DC，无 VRMS 或距离标注）
- `analog.measurement-performance-not-shown`：框图确认 680K/11K、2.5V BIAS 与 ADS1115 16bit，但未打印允许输入范围、量程档位、ADC PGA 配置、输出换算、分辨率、精度或校准误差。（证据：图 f001298a771a / 第 1 页 / 页 1 测量端-680K/11K-BIAS-ADS1115 链路，无量程/精度/分辨率文字）
- `other.power-led-not-shown`：产品正文列出 LED 电源指示灯，但当前框图未绘出 LED、限流电阻或控制网络。（证据：图 f001298a771a / 第 1 页 / 页 1 完整框图无 LED/D 位号或指示灯支路）
- `review.eeprom-calibration`：0x53 EEPROM 的型号、容量、校准数据布局、版本、校验与写保护机制是什么？；原因：框图只确认 EEPROM 和地址，无法验证正文所述出厂校准参数及禁止写入要求。
- `review.isolation-rating`：整机 1000 VRMS 隔离耐压适用的测试时间、条件、爬电距离和电气间隙是什么？；原因：当前框图只展示隔离拓扑，没有额定值和安规结构数据。
- `review.measurement-performance`：±36V 量程、不同电压区间的分辨率、PGA 配置、换算公式和 1%FS±1digit 精度条件是什么？；原因：框图只给分压阻值、偏置和 ADC 位数，未给固件配置与校准模型。
- `review.power-led`：电源指示 LED 的位号、颜色、供电轨、限流电阻和连接方式是什么？；原因：产品正文列出 LED，但当前框图没有任何指示灯电路。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `f001298a771ac9643dd618b5cde918eca1706b35311f05b65c08fb02be79db7c` | `https://static-cdn.m5stack.com/resource/docs/products/unit/vmeter/vmeter_sch_01.webp` |

---

源文档：`zh_CN/unit/vmeter.md`

源文档 SHA-256：`21d20bdde9136d89e5778e006638aa56beab90a7f4f4a917412d29f3188c1c66`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
