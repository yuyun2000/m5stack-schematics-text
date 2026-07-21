# Cardputer Mesh Kit

<span class="product-sku">SKU:K152</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1240/K152-Cardputer-Mesh-Kit-main-pictures_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1240/K152-Cardputer-Mesh-Kit-main-pictures_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1240/K152-Cardputer-Mesh-Kit-main-pictures_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1240/K152-Cardputer-Mesh-Kit-main-pictures_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1240/K152-Cardputer-Mesh-Kit-main-pictures_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1240/K152-Cardputer-Mesh-Kit-main-pictures_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1240/K152-Cardputer-Mesh-Kit-main-pictures_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1240/K152-Cardputer-Mesh-Kit-main-pictures_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1240/K152-Cardputer-Mesh-Kit-main-pictures_09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1240/K152-Cardputer-Mesh-Kit-main-pictures_10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1240/K152-Cardputer-Mesh-Kit-main-pictures_11.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1240/K152-Cardputer-Mesh-Kit-main-pictures_12.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1240/K152-Cardputer-Mesh-Kit-main-pictures_13.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1240/K152-weight.jpg">
</PictureViewer>

## 描述

**Cardputer Mesh Kit** 是一款集 LoRa Mesh 与全球定位功能于一体的便携式通信终端套件，套件核心包含 **Cardputer-Adv** 核心主控与 **Cap LoRa-1262** 通信拓展模块。

**Cardputer-Adv** 是一款卡片大小的便携式可编程控制器，采用 Stamp-S3A 主控模组（基于 ESP32-S3FN8），配备 1.14" LCD 屏幕与 56 键极简键盘，方便现场信息查看与指令输入。内置 1750mAh 锂电池保证长时间独立运行，集成 ES8311 音频芯片、MEMS 麦克风、1W 扬声器及 3.5mm 音频接口，支持语音交互与音频输出。此外还配备了 6 轴姿态传感器 BMI270、红外发射管、microSD 卡槽，并预留 HY2.0-4P Grove 接口与 EXT 2.54-14P 拓展总线，结构上支持磁吸与乐高孔兼容设计。

**Cap LoRa-1262** 作为套件的通信拓展模块，通过 EXT 2.54-14P 接口连接至 Cardputer-Adv ，由主机供电与驱动，即插即用。模块采用 SX1262 LoRa 方案，支持 868~923MHz 频段，具备 -147dBm 接收灵敏度与 +22dBm 发射功率，配备 RP-SMA 外置天线与屏蔽罩，确保远距离通信的抗干扰能力。同时集成 AT6668 GNSS 模组与内置陶瓷天线，支持 GPS、北斗、GLONASS、GALILEO 等多系统联合定位。模块另设 HY2.0-4P 接口，可用于连接外部传感器。

**Cardputer Mesh Kit** 出厂预装 Meshtastic 固件，开箱即用，无需复杂开发即可快速接入 LoRa Mesh 网络。Cardputer-Adv 与 Cap LoRa-1262 协同工作，配置便捷、定位直观，适用于户外通信、节点部署、位置追踪及工业巡检等场景。

## 教程 & 快速上手

learn>| ![Cardputer Mesh Kit](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1240/K152-Cardputer-Mesh-Kit-main-pictures_13.jpg) | [Meshtastic 使用教程](/zh_CN/guide/lora/meshtastic/cardputer_mesh_kit) | 本教程介绍如何通过 Cardputer Mesh Kit 使用 Meshtastic。|

learn>| ![UiFlow2](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/uiflow2.0_banner_01.png) | [UiFlow2](/zh_CN/uiflow2/cardputer-adv/program) | 本教程将向你介绍，如何通过 UiFlow2 图形化编程平台控制 Cardputer-Adv。 |

learn>| ![Arduino IDE](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/arduino_banner_01.png) | [Arduino IDE](/zh_CN/arduino/m5cardputer/program) | 本教程将向你介绍，如何通过 Arduino IDE 编程控制 Cardputer-Adv。 |

## 产品特性

**核心主机（Cardputer-Adv）**：

- Stamp-S3A 核心主控（ESP32-S3FN8）
- 56 键键盘，160gf 舒适按键手感
- 1.14" LCD 屏幕（240x135px）
- ES8311 音频编解码芯片 + NS4150B 功放 + 1W 扬声器 + MEMS 麦克风
- 3.5mm 音频输出接口
- 6 轴姿态传感器 BMI270
- 红外发射管
- microSD 卡槽
- 内置 1750mAh 锂电池
- HY2.0-4P Grove 接口 + EXT 2.54-14P 拓展总线
- 背面磁吸设计，兼容乐高孔

**通信拓展模块（Cap LoRa-1262）**：

- LoRa 调制技术 + GNSS 全球定位系统
- 工作频率 868 ~ 923 MHz
- 接收灵敏度低至 -147 dBm，发射功率 +22 dBm
- 外置 RP-SMA 天线接口，内置陶瓷 GPS 天线
- 支持 GPS / QZSS / BD2 / BD3 / GAL / GLO 多系统定位
- HY2.0-4P 拓展接口（用于外接传感器）

开发平台：
- Arduino
- UiFlow2
- ESP-IDF
- PlatformIO

## 包装内容

- 1 x Cardputer-Adv（绿色背壳版本）
- 1 x Cap LoRa-1262
- 1 x LoRa 胶棒天线（RP-SMA 接口）
- 2 x M2 * 4mm 螺丝 (杯头，机械牙)
- 1 x 内六角扳手 L 形 1.5mm (适配 M2 螺丝)
- 1 x 安全警示贴纸

## 应用场景

- 远程 GPS 追踪器
- 户外组网通信
- 快速功能验证和原型设计
- 工业控制和自动化
- 智能城市 / 智慧家居
- 车载定位与导航
- 嵌入式系统开发和学习

## 规格参数

| 规格              | 参数                                                                       |
| ----------------- | -------------------------------------------------------------------------- |
| SoC               | ESP32-S3FN8 @ 双核 Xtensa LX7，最高 240MHz                                 |
| Flash             | 8MB                                                                        |
| 外部存储扩展      | microSD                                                                    |
| 屏幕              | ST7789V2@1.14", 240 x 135px                                                |
| 键盘              | 56 按键 (4 x 14)，160gf 操作力                                             |
| 拓展接口          | HY2.0-4P + EXT 2.54-14P                                                    |
| IR                | 1x 红外发射管                                                              |
| 音频编解码芯片    | ES8311                                                                     |
| 扬声器            | NS4150B 功放 + 8Ω@1W 扬声器                                                |
| 麦克风            | MEMS 麦克风，SNR：65 dB                                                    |
| 姿态传感器        | BMI270                                                                     |
| 电池容量          | 1750mAh                                                                    |
| 工作温度          | 0 ~ 40°C                                                                   |
| 工作电流          | DC4.2V@120.2mA                                                             |
| LoRa 模组         | SX1262                                                                     |
| LoRa 频段范围     | 868 ~ 923 MHz                                                              |
| LoRa 可编程比特率 | 最高 300kbps                                                               |
| LoRa 天线         | 尺寸 108 x 9.3mm，接口类型 RP-SMA（内螺内孔），增益 3dBi                   |
| LoRa 发射功率     | +22dBm                                                                     |
| LoRa 接收灵敏度   | -147dBm（低速率模式）                                                      |
| LoRa 工作电流     | DC 5V@163.4mA                                                              |
| 支持调制方式      | FSK / GFSK / MSK / LoRa / OOK                                              |
| GPS 模组          | ATGM336H-6N@AT6668                                                         |
| GPS 通讯接口      | UART，默认 115200bps@8N1                                                   |
| 支持卫星导航系统  | GPS / QZSS / BD2 / BD3 / GAL / GLO                                         |
| GPS 通道          | 50 通道                                                                    |
| GPS 定位精度      | <1.5m (CEP50)                                                              |
| GPS 更新率        | 最高 10Hz                                                                  |
| GPS 启动时间      | 冷启动 23s，热启动 1s                                                      |
| 产品尺寸          | Cardputer-Adv：84.0 x 54.0 x 19.6mm<br>Cap LoRa-1262：84.0 x 24.0 x 15.2mm |
| 产品重量          | 77.2g                                                                      |
| 包装尺寸          | 103.0 x 90.0 x 25mm                                                        |
| 毛重              | 127.2g                                                                     |

## 操作说明

### Cardputer-Adv 进入下载模式

将 Cardputer-Adv 侧面的开关键置于 `OFF`，按住 `G0` 按键后通电，释放后设备进入下载模式。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1240/K152-operate_02.jpg" width="60%" />

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1240/K152-download-mode-demo.gif" width="60%" />

### 充电注意事项

充电时请将电源开关切换至 `ON`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1240/K152-operate_04.jpg" width="60%" />

### 组合安装说明

Cap LoRa-1262 通过 EXT 2.54-14P 接口与 Cardputer-Adv 连接：

1. 将 Cardputer-Adv 底部朝上，找到 **EXT 2.54-14P** 接口（14 针排母）。
2. 将 Cap LoRa-1262 的对应排针对准接口，轻轻按压直至完全插入。
3. 将 LoRa 胶棒天线拧入 Cap LoRa-1262 的 RP-SMA 天线接口。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1240/operate.png" width="60%" />

### 设备注册

Cardputer Mesh Kit 套装获得了 Meshtastic 官方 License 授权，可通过以下操作方式注册为正版授权设备：

1. 确认设备已参考[烧录教程](/zh_CN/guide/lora/meshtastic/cardputer_mesh_kit)，完成 Meshtastic 固件烧录（出厂固件已默认烧录）。
2. 确认 Cardputer-Adv 已正确连接 Cap LoRa-1262 拓展。
3. 将 Cardputer Mesh Kit 通过 USB Type-C 数据线连接至电脑，访问 [M5 Meshtastic Device](https://meshtastic-reg.m5stack.com/) 设备注册页面。
4. 在注册网页上点击 `Connect Device` 选项, 选中设备端口后，单击`Connect`，等待提示注册完成。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1240/K152_Cardputer_Mesh_Kit_operate_05.jpg" width="70%" />

设备注册成功后，Meshtastic app 页面可识别出设备型号与授权标识：

?>注意|仅 Cardputer Mesh Kit 套装中的设备可进行注册，其他 Cardputer/-Adv 设备不参与 Meshtastic 授权注册。如果注册失败，请联系 M5Stack 官方售后处理。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1240/K152_Cardputer_Mesh_Kit_operate_06.jpg" width="40%" />

## 管脚映射

### Cardputer-Adv EXT 2.54-14P

::m5-bus-table
| FUNC  | PIN | LEFT | RIGHT | PIN   | FUNC    |
| ----- | --- | ---- | ----- | ----- | ------- |
| RESET | G3  | 1    | 2     | 5VIN  |         |
| INT   | G4  | 3    | 4     | GND   |         |
| BUSY  | G6  | 5    | 6     | 5VOUT |         |
| SCK   | G40 | 7    | 8     | G8    | I2C_SDA |
| MOSI  | G14 | 9    | 10    | G9    | I2C_SCL |
| MISO  | G39 | 11   | 12    | G13   | UART_RX |
| CS    | G5  | 13   | 14    | G15   | UART_TX |
::

### Cardputer-Adv LCD

| Stamp-S3A | G38     | G33 | G34 | G35 | G36 | G37 |
| --------- | ------- | --- | --- | --- | --- | --- |
| ST7789V2  | DISP_BL | RST | RS  | DAT | SCK | CS  |
| RGB LED   | PWR_EN  |     |     |     |     |     |

### Cardputer-Adv Audio

| Stamp-S3A | G8  | G9  | G41  | G46    | G43  | G42   |
| --------- | --- | --- | ---- | ------ | ---- | ----- |
| ES8311    | SDA | SCL | SCLK | ASDOUT | LRCK | DSDIN |

### Cardputer-Adv IMU

| Stamp-S3A | G8  | G9  |
| --------- | --- | --- |
| BMI270    | SDA | SCL |

### Cardputer-Adv IR

| Stamp-S3A | G44 |
| --------- | --- |
| IR TX     | TX  |

### Cardputer-Adv Battery

| Stamp-S3A | G10 |
| --------- | --- |
| Battery   | ADC |

### Cardputer-Adv Keyboard

| Stamp-S3A   | G8  | G9  | G11 |
| ----------- | --- | --- | --- |
| TCA8418RTWR | SDA | SCL | INT |

### Cardputer-Adv microSD

| Stamp-S3A | G12 | G14  | G40 | G39  |
| --------- | --- | ---- | --- | ---- |
| microSD   | CS  | MOSI | CLK | MISO |

### Cardputer-Adv HY2.0-4P

::grove-table
| HY2.0-4P    | Black | Red | Yellow | White |
| ----------- | ----- | --- | ------ | ----- |
| PORT.CUSTOM | GND   | 5V  | G2     | G1    |
::

### Cap LoRa-1262 Cap-Bus

::m5-bus-table
| PIN    | LEFT | RIGHT | PIN       |
| ------ | ---- | ----- | --------- |
| GPS_TX | 1    | 14    | LoRa_NSS  |
| GPS_RX | 2    | 13    | LoRa_MISO |
| SCL    | 3    | 12    | LoRa_MOSI |
| SDA    | 4    | 11    | LoRa_SCK  |
| 5V_OUT | 5    | 10    | LoRa_BUSY |
| GND    | 6    | 9     | LoRa_IRQ  |
| 5V_IN  | 7    | 8     | LoRa_RST  |
::

| Cardputer-Adv        | G3  | G4  | G6   | G40 | G14  | G39  | G5  |
| -------------------- | --- | --- | ---- | --- | ---- | ---- | --- |
| Cap LoRa-1262 (LoRa) | RST | IRQ | BUSY | SCK | MOSI | MISO | NSS |

| Cardputer-Adv       | G13    | G15    |
| ------------------- | ------ | ------ |
| Cap LoRa-1262 (GPS) | GPS-RX | GPS-TX |

| Cardputer-Adv                | G8  | G9  |
| ---------------------------- | --- | --- |
| Cap LoRa-1262 (PI4IOE5V6408) | SDA | SCL |
| Cap LoRa-1262 (HY2.0-4P)     | SDA | SCL |

| PI4IOE5V6408 | P0        |
| ------------ | --------- |
| FM8625H      | SX_ANT_SW |

LoRa 模组初始化需要执行以下操作：

- 使能射频天线开关：将 PI4IOE IO 拓展芯片的 P0 设置为高电平

### Cap LoRa-1262 HY2.0-4P

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 原理图

- [Cardputer-Adv 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/Sch_M5CardputerAdv_v1.0_2025_06_20_17_19_58.pdf)
- [Stamp-S3A 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1150/Sch_StampS3_v0.3.3.pdf)
- [Cap LoRa-1262 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1208/U214-sche-Cap-LoRa1262_SCH_V1.1_20251029_2025_11_07_22_53_19.pdf)
- [Stamp LoRa-1262 Mini 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1208/NEW-1262-SCH_A1-Lora_2025_08_27_10_58_52.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/Sch_M5CardputerAdv_v1.0_2025_06_20_17_19_58_page_01.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/Sch_M5CardputerAdv_v1.0_2025_06_20_17_19_58_page_02.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/Sch_M5CardputerAdv_v1.0_2025_06_20_17_19_58_page_03.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/Sch_M5CardputerAdv_v1.0_2025_06_20_17_19_58_page_04.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1150/Sch_StampS3_v0.3.3_page_01.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1208/U214-sche-Cap-LoRa1262_SCH_1.1_20251029_2025_11_07_22_53_19_page_02.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1208/NEW-1262-SCH_A1-Lora_2025_08_27_10_58_52_page_01.png">
</SchViewer>

## 尺寸图

- [Cardputer-Adv 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/K132-Adv-cardputer-ADV.pdf)
- [Cap LoRa-1262 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1208/U214-00-cap1262-model-size.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/K132-Adv-cardputer-ADV_page_01.png" width="100%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1208/U214-00-cap1262-model-size_page_01.png" width="100%">
</SchViewer>

## 结构文件

- [Cardputer-Adv 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/K132-Adv_Cardputer-Adv/Structures)

## 数据手册

- [ESP32-S3](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/472/esp32-s3_datasheet_cn.pdf)  <!--中英链接不一样-->
- [ST7789V2](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/lcd/ST7789V2_SPEC_V1.0.pdf)
- [ES8311](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/Atomic%20Echo%20Base/ES8311.pdf)
- [NS4150B](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/Atomic%20Echo%20Base/NS4150B.pdf)
- [BMI270](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/K128%20CoreS3/BMI270.PDF)
- [SX1262](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1177/DS_SX1261_2_V2-2.pdf)
- [ATGM336H-6N](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-GPS%20v1.1/ATGM336H-6N.pdf)
- [CASIC 多模卫星导航接收机协议规范](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1173/CASIC_Multi-mode_Satellite_Navigation_Receiver_Protocol_Specification.pdf)

## 软件开发

### Arduino

- [Cardputer-Adv Arduino 快速上手](/zh_CN/arduino/m5cardputer/program)
- [Cap LoRa-1262 Arduino 快速上手](/zh_CN/arduino/projects/cap/cap_lora868)
- [Cardputer-Adv Arduino 驱动库](https://github.com/m5stack/M5Cardputer)
- [Cap LoRa-1262 LoRa 驱动库 (RadioLib)](https://github.com/jgromes/RadioLib)
- [Cap LoRa-1262 GPS 驱动库 (TinyGPSPlus)](https://github.com/m5stack/TinyGPSPlus)

### UiFlow2

- [Cardputer-Adv UiFlow2 快速上手](/zh_CN/uiflow2/cardputer-adv/program)
- [Cap LoRa-1262 UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/cap/lora1262.html)

### PlatformIO

```bash
[env:m5stack-cardputer-mesh-kit]
platform = espressif32@6.12.0
board = esp32-s3-devkitc-1
framework = arduino
upload_speed = 1500000
build_flags =
    -DESP32S3
    -DCORE_DEBUG_LEVEL=5
    -DARDUINO_USB_CDC_ON_BOOT=1
          -DARDUINO_USB_MODE=1

lib_deps =
    M5Cardputer=https://github.com/m5stack/M5Cardputer
    RadioLib=https://github.com/jgromes/RadioLib
    TinyGPSPlus=https://github.com/m5stack/TinyGPSPlus
```

### Easyloader

| Easyloader                        | 下载链接                                                                                            |
| --------------------------------- | --------------------------------------------------------------------------------------------------- |
| Cardputer-Adv 出厂固件 Easyloader | [download](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1240/K152-factory-firmware.exe)         |

## 相关视频

- Cardputer Mesh Kit 产品介绍与使用案例

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1240/K152-Cardpute-Mes-Kit-video-ZH.mp4" type="video/mp4"></video>
