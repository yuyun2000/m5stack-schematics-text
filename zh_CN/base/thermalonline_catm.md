# IoT Base Thermal Online CatM

<span class="product-sku">SKU:K119</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/thermalonline_catm/thermalonline_catm_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/995/K119_01.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/thermalonline_catm/thermalonline_catm_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/thermalonline_catm/thermalonline_catm_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/995/K119_02.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/thermalonline_catm/thermalonline_catm_06.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/thermalonline_catm/thermalonline_catm_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/995/K119_03.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/thermalonline_catm/thermalonline_catm_09.webp">
</PictureViewer>

## 描述

**IoT Base Thermal Online CatM**是一款工业级远程热成像监控套件，硬件采用**MLX90640 红外测温模块**(32x24 阵列) + M5Stack BASIC ( ESP32 核心主控) + **SIM7080G**通信模组方案，支持 CatM/NB-IoT/Wi-Fi 等多种通信方式实现**远程非接触式温度检测**。搭配集成丰富的接口资源 (I2C + UART + GPIO + RS485 + 电池供电接口) 的拓展底座，还可用于各类传感器拓展，适配更多应用场景。

## 产品特性

- MLX90640 (32x24 红外像素阵列，测温范围: -40°C ~ 300°C , I2C 接口：0x33)
- SIM7080G
  - CatM\&NB-IoT 双模式的无线通信模块
  - UART 接口 / AT 指令控制
  - 全球版 / 多频段支持
  - 卡槽规格：MicroSIM
  - 天线:`SMA`外部天线
  - 模块认证:
    - Softbank/Telec/RoHS/REACH/JATE/Docomo/KDDI/RCM/CE(RED)/GCF
    - Deutsche Telekom/FCC/PTCRB/AT\&T/Verizon/T-Mobile/US Cellular/IC
- ESP32 主控拓展接口:
  - 1 x I2C
  - 1 x TFCard
- 底座拓展接口:
  - 1 x PWR485(RS485 + DC 12V INPUT)
  - 1 x DC 电源接口
  - 1 x I2C
  - 1 x GPIO
  - 1 x UART
  - 1 x 电池拓展接口

## 包装内容

- 1 x Basic
- 1 x IoT Base Thermal Online CatM
- 1 x SMA 天线
- 1 x 12V DC 电源适配器
- 1 x VH-3.96-2P 端子
- 1 x VH-3.96-4P 端子
- 1 x Din-moute 导轨固定底板
- 2 x M3\*28 螺丝
- 1 x M3 六角扳手

## 应用场景

- 远程非接触式温控检测
- 远程控制 / 数据采集

## 规格参数

| 规格              | 参数                                                                                                                    |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------- |
| 非接触测温传感器  | MLX90640 (32x24 红外像素阵列，测温范围: -40°C ~ 300°C , I2C 通信 @ 0x33)                                                |
| 通信模组          | SIM7080G, 通信接口: UART baud 115200 8N1                                                                                |
| 支持 CAT-M 频段   | B1/B2/B3/B4/B5/B8/B12/B13/B14/B18/B19/B20/B25/B26 /B27/B28/B66/B85                                                      |
| 支持 CAT-NB 频段  | B1/B2/B3/B4/B5/B8/B12/B13/B18/B19/B20/B25/B26/B28 /B66/B71/B85                                                          |
| Cat-M 上下行速度  | Uplink: 1119Kbps Downlink:589Kbps                                                                                       |
| NB-IoT 上下行速度 | Uplink: 150Kbps Downlink:136Kbps                                                                                        |
| RF Power Class    | Class 5 (Typ. 21dbm)                                                                                                    |
| 卡槽规格          | MicroSIM                                                                                                                |
| 支持协议:         | TCP/UDP/HTTP/HTTPS/TLS/DTLS/PING/LWM2M/COAP/MQTT 等通信协议                                                             |
| 工作电流          | 54mA (DC 接口 12V 输入，设备入网情况下)                                                                                 |
| 接口规格          | I2C/GPIO/UART (HY2.0-4P)<br/>RS485(VH-3.96-4P)<br/>DC 接口 (圆孔 DC-IN-TH_DC-0440-2.5A-2.0)<br/>锂电池接口 (VH-3.96-2P) |
| 产品重量 (模块)   | 75.7g                                                                                                                   |
| 毛重              | 200.1g                                                                                                                  |
| 产品尺寸          | 80 x 54 x 33mm                                                                                                          |
| 包装尺寸          | 98 x 106 x 57mm                                                                                                         |

## 认证信息

- [SIM7080G_AT\&T_Certificate_2020](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/sim7080g/en/SIM7080G_AT%26amp%3BT_Certificate_2020.pdf)
- [SIM7080G_GCF_Certificate_2020](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/sim7080g/en/SIM7080G_GCF_Certificate_2020.pdf)
- [SIM7080G_NCC_2020](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/sim7080g/en/SIM7080G_NCC_2020.pdf)
- [SIM7080G_PTCRB_Certificate_2020](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/sim7080g/en/SIM7080G_PTCRB_Certificate_2020.pdf)
- [SIM7080G_RCM_Compliance Certificate_2020](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/sim7080g/en/SIM7080G_RCM_Compliance%20Certificate_2020.pdf)
- [SIM7080G_T-mobile_Certificate_2021](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/sim7080g/en/SIM7080G_T-mobile_Certificate_2021.pdf)
- [SIM7080G_US Cellular_Certificate_2021](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/sim7080g/en/SIM7080G_US%20Cellular_Certificate_2021.pdf)

## 原理图

<SchViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/thermalonline_catm/thermalonline_catm_sch_01.webp" width="80%">
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/thermalonline_catm/thermalonline_catm_sch_02.webp" width="80%">
</SchViewer>

## 管脚映射

### SIM7080G

| M5Core   | G0  | G35 | G12 | 5V  | GND |
| -------- | --- | --- | --- | --- | --- |
| SIM7080G | RX  | TX  | PWR | VCC | GND |

### MLX90640

| M5Core   | G21 | G22 | 5V  | GND |
| -------- | --- | --- | --- | --- |
| MLX90640 | SDA | SCL | VCC | GND |

### RS485

| CORE  | G15 | G13 | 5V  | GND |
| ----- | --- | --- | --- | --- |
| RS485 | TX  | RX  | VIN | GND |

### HY2.0-4P

| M5Core   | G21 | G22 | 5V  | GND |
| -------- | --- | --- | --- | --- |
| I2C PORT | SDA | SCL | VCC | GND |

| M5Core    | G36 | G26 | 5V  | GND |
| --------- | --- | --- | --- | --- |
| GPIO PORT | ADC | DAC | VCC | GND |

| M5Core    | G17 | G16 | 5V  | GND |
| --------- | --- | --- | --- | --- |
| UART PORT | TX  | RX  | VCC | GND |

### M5-Bus

::m5-bus-table
| PIN      | LEFT | RIGHT | PIN      |
| -------- | ---- | ----- | -------- |
| GND      | 1    | 2     | NC       |
| GND      | 3    | 4     | PORT.B   |
| GND      | 5    | 6     | NC       |
| NC       | 7    | 8     | NC       |
| NC       | 9    | 10    | PORT.B   |
| NC       | 11   | 12    | NC       |
| NC       | 13   | 14    | NC       |
| UART_RX  | 15   | 16    | UART_TX  |
| I2C_SDA  | 17   | 18    | I2C_SCL  |
| NC       | 19   | 20    | NC       |
| NC       | 21   | 22    | RS485_TX |
| RS485_RX | 23   | 24    | NC       |
| NC       | 25   | 26    | NC       |
| NC       | 27   | 28    | 5V       |
| NC       | 29   | 30    | BAT      |
::

## 尺寸图

- [IoT Base Thermal Online CatM 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/995/K119-iotbase-Thermal.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/995/K119-iotbase-Thermal_page_01.png" width="100%">

## 数据手册

- [SIM7070_SIM7080_SIM7090 Series_CTBURST_Application Note_V1.02](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/sim7080g/en/SIM7070_SIM7080_SIM7090%20Series_CTBURST_Application%20Note_V1.02.pdf)
- [SIM7070_SIM7080_SIM7090 Series_CoAP(S)_Application Note_V1.03](<https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/sim7080g/en/SIM7070_SIM7080_SIM7090%20Series_CoAP(S)_Application%20Note_V1.03.pdf>)
- [SIM7070_SIM7080_SIM7090 Series_Email_Application Note_V1.02](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/sim7080g/en/SIM7070_SIM7080_SIM7090%20Series_Email_Application%20Note_V1.02.pdf)
- [SIM7070_SIM7080_SIM7090 Series_FOTA_Application Note_V1.02](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/sim7080g/en/SIM7070_SIM7080_SIM7090%20Series_FOTA_Application%20Note_V1.02.pdf)
- [SIM7070_SIM7080_SIM7090 Series_FS_Application Note_V1.02](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/sim7080g/en/SIM7070_SIM7080_SIM7090%20Series_FS_Application%20Note_V1.02.pdf)
- [SIM7070_SIM7080_SIM7090 Series_FTP(S)_Application Note_V1.02](<https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/sim7080g/en/SIM7070_SIM7080_SIM7090%20Series_FTP(S)_Application%20Note_V1.02.pdf>)
- [SIM7070_SIM7080_SIM7090 Series_GNSS_Application Note_V1.02](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/sim7080g/en/SIM7070_SIM7080_SIM7090%20Series_GNSS_Application%20Note_V1.02.pdf)
- [SIM7070_SIM7080_SIM7090 Series_HTTP(S)_Application Note_V1.02](<https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/sim7080g/en/SIM7070_SIM7080_SIM7090%20Series_HTTP(S)_Application%20Note_V1.02.pdf>)
- [SIM7070_SIM7080_SIM7090 Series_Linux_Application Note_V1.02](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/sim7080g/en/SIM7070_SIM7080_SIM7090%20Series_Linux_Application%20Note_V1.02.pdf)
- [SIM7070_SIM7080_SIM7090 Series_Low Power Mode_Application Note_V1.02](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/sim7080g/en/SIM7070_SIM7080_SIM7090%20Series_Low%20Power%20Mode_Application%20Note_V1.02.pdf)
- [SIM7070_SIM7080_SIM7090 Series_LwM2M_Application Note_V1.02](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/sim7080g/en/SIM7070_SIM7080_SIM7090%20Series_LwM2M_Application%20Note_V1.02.pdf)
- [SIM7070_SIM7080_SIM7090 Series_MQTT(S)_Application Note_V1.03](<https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/sim7080g/en/SIM7070_SIM7080_SIM7090%20Series_MQTT(S)_Application%20Note_V1.03.pdf>)
- [SIM7070_SIM7080_SIM7090 Series_PING_Application Note_V1.02](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/sim7080g/en/SIM7070_SIM7080_SIM7090%20Series_PING_Application%20Note_V1.02.pdf)
- [SIM7070_SIM7080_SIM7090 Series_SAT_Application Note_V1.02](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/sim7080g/en/SIM7070_SIM7080_SIM7090%20Series_SAT_Application%20Note_V1.02.pdf)
- [SIM7070_SIM7080_SIM7090 Series_SSL_Application Note_V1.00](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/sim7080g/en/SIM7070_SIM7080_SIM7090%20Series_SSL_Application%20Note_V1.00.pdf)
- [SIM7070_SIM7080_SIM7090 Series_TCPUDP(S)_Application Note_V1.03](<https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/sim7080g/en/SIM7070_SIM7080_SIM7090%20Series_TCPUDP(S)_Application%20Note_V1.03.pdf>)
- [SIM7080_Series_SPEC_20200427](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/sim7080g/en/SIM7080_Series_SPEC_20200427.pdf)
- [MLX90640 Datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/hat/MLX90640-Datasheet-Melexis_en.pdf)

## 软件开发

### Arduino

- [IoT Base Thermal Online CatM MLX90640 Array Example](https://github.com/m5stack/M5Stack/tree/master/examples/Unit/THERMAL_MLX90640)
- [IoT Base Thermal Online CatM MQTT Example](https://github.com/m5stack/IoT_BASE_SIM7080/tree/master/examples/MQTT)
- [IoT Base Thermal Online CatM Modbus Master Example](https://github.com/m5stack/IoT_BASE_SIM7080/tree/master/examples/Modbus/ModBus-RTU/Master)
- [IoT Base Thermal Online CatM Modbus Slave Example](https://github.com/m5stack/IoT_BASE_SIM7080/tree/master/examples/Modbus/ModBus-RTU/Slave)

### 通信协议

- [SIM7070_SIM7080_SIM7090 Series_AT Command Manual_V1.04](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/sim7080g/en/SIM7070_SIM7080_SIM7090%20Series_AT%20Command%20Manual_V1.04.pdf)

### EasyLoader

| Easyloader                              | 下载链接                                                                                       | 备注 |
| --------------------------------------- | ---------------------------------------------------------------------------------------------- | ---- |
| IoT Base Thermal Online CatM Easyloader | [download](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/995/EasyLoader_Thermal-Online.exe) | /    |
