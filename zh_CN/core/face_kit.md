# Faces Kit

<span class="product-sku">SKU:K005</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/face_kit/face_kit_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/face_kit/face_kit_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/face_kit/face_kit_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/face_kit/face_kit_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/face_kit/face_kit_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/face_kit/face_kit_06.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/face_kit/face_kit_07.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/face_kit/face_kit_08.webp">
</PictureViewer>

## 描述

**Faces Kit** 是一系列功能面板的集合。套件内包含了三个常用的功能面板，"GameBoy (游戏键盘)"、"Calculator ( 计算器键盘 )"、"QWERTY ( 输入全键盘 )"。内部集成 **MEGA328** 处理器，通过 I2C 通信协议 (0x08) 工作在从机模式下。根据需求去运用这 3 个不同的功能面板，进而实现用户与 M5Core 之间的人机交互。

## 教程 & 快速上手

learn>| ![UiFlow](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/uiflow1.0_banner_01.png) | [UiFlow](/zh_CN/uiflow/m5core/program) | 本教程将向你介绍，如何通过 UiFlow 图形化编程平台控制 Gray 设备 |

learn>| ![UiFlow2](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/uiflow2.0_banner_01.png) | [UiFlow2](/zh_CN/uiflow2/m5core/program) | 本教程将向你介绍，如何通过 UiFlow2 图形化编程平台控制 Gray 设备 |

learn>| ![Arduino IDE](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/arduino_banner_01.png) | [Arduino IDE](/zh_CN/arduino/m5core/program) | 本教程将向你介绍，如何通过 Arduino IDE 编程控制 Gray 设备 |

## 产品特性

- 基于 ESP32 开发
- 内置陀螺仪加速计与磁力计
- 内置扬声器，按键，LCD 屏幕，电源 / 复位按键 x1
- microSD 插槽 (最大可拓展 16GB)
- M5-Bus 总线母座
- 磁吸式充电设计
- 内置锂电池
- 可拓展的引脚与接口
- 开发平台
  - UiFlow1
  - UiFlow2
  - Arduino IDE
  - ESP-IDF
  - PlatformIO

## 包装内容

- 1 x Gray
- 1 x FACES 充电座
- 1 x FACES 挂绳
- 1 x 面板贴纸
- 3 x FACES 键盘 (GameBoy，Calculator，QWERTY)
- 8 x 杜邦线
- 6 x M3x12 螺丝
- 1 x 六角螺丝扳手
- 1 x USB Type-C 连接线 (100cm)

## 应用场景

- 游戏机
- 计算器
- 数据输入外设
- 物联网控制器

## 规格参数

| 主控资源      | 参数                                                                    |
| ------------- | ----------------------------------------------------------------------- |
| SoC           | ESP32-D0WDQ6@双核处理器，主频 240MHz                                    |
| DMIPS         | 600                                                                     |
| SRAM          | 520KB                                                                   |
| Flash         | 16MB (旧版 4MB)                                                         |
| Wi-Fi         | 2.4 GHz Wi-Fi                                                           |
| 输入电压      | 5V@500mA                                                                |
| 主机接口      | USB Type-C x 1，GROVE (I2C+I/O+UART) x 1                                |
| Core 底座接口 | PIN (G1，G2，G3，G16，G17，G18，G19，G21，G22，G23，G25，G26，G35，G36) |
| IPS 屏幕      | 2 inch，320x240 Colorful TFT LCD，ILI9342C，最高亮度 853nit             |
| 扬声器        | 1W-0928                                                                 |
| 按键          | 自定义按键 x 3                                                          |
| 天线          | 2.4G 3D 天线                                                            |
| 锂电池        | 600mAh@3.7V                                                             |
| MEMS          | MPU6886+BMM150                                                          |
| 2.4G 天线     | Proant 440                                                              |
| 工作温度      | 0 ~ 60°C                                                                |
| 外壳材质      | Plastic ( PC )                                                          |
| 产品尺寸      | 58.2 x 54.2 x 18.7mm                                                    |
| 产品重量      | 94.0g                                                                   |
| 包装尺寸      | 120.0 x 85.0 x 65.0mm                                                   |
| 毛重          | 264.0g                                                                  |

## 操作说明

?> BMM150 磁场干扰 | 带有磁铁的产品可能对 BMM150 磁场传感器造成干扰，导致读数异常。当搭配含有磁铁的 M5 主控设备时，需拆除磁铁，同时避免 BMM150 传感器放置在强磁场附近。

### 开关机

- 开机：单击左侧红色电源键
- 关机：快速双击左侧红色电源键<br/>注意：默认情况下，USB 供电时，无法进行关机

### 升级

<div class="product_pic">
 <img src="https://static-cdn.m5stack.com/resource/docs/products/core/face_kit/face_kit_09.webp">
</div>

## 原理图

- [原理图](<https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/schematic/Core/M5-Core-Schematic(20171206).pdf>)

- [有关主控 GRAY 相关原理图及管脚映射，请点击此处查看 GRAY 文档](/zh_CN/core/gray)

<SchViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/face_kit/face_kit_sch_01.webp" width="70%">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/face_kit/face_kit_sch_02.webp" width="70%">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/face_kit/face_kit_sch_03.webp" width="70%">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/face_kit/face_kit_sch_04.webp" width="70%">
</SchViewer>

## 管脚映射

**Mega328 ISP**下载接口 Pin 脚定义

<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-cardkb/mega328_isp_sch_01.webp" width="30%" height="30%">

### ESP32 ADC/DAC

| ADC1   | ADC2               | DAC1   | DAC2   |
| ------ | ------------------ | ------ | ------ |
| 8 通道 | 10 通道            | 2 通道 | 2 通道 |
| G32-39 | G0/2/4/12-15/25-27 | G25    | G26    |

### HY2.0-4P

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | G21    | G22   |
| PORT.B   | GND   | 5V  | G26    | G36   |
| PORT.C   | GND   | 5V  | G17    | G16   |
::

## IP5306 充 / 放电，电压参数

| 充电                | 放电                 |
| ------------------- | -------------------- |
| 0.00 ~ 3.40V -> 0%  | 4.20 ~ 4.07V -> 100% |
| 3.40 ~ 3.61V -> 25% | 4.07 ~ 3.81V -> 75%  |
| 3.61 ~ 3.88V -> 50% | 3.81 ~ 3.55V -> 50%  |
| 3.88 ~ 4.12V -> 75% | 3.55 ~ 3.33V -> 25%  |
| 4.12 ~ /-> 100%     | 3.33 ~ 0.00V -> 0%   |

### M5-Bus

::m5-bus-table
| FUNC    | PIN  | LEFT | RIGHT | PIN | FUNC    |
| ------- | ---- | ---- | ----- | --- | ------- |
|         | GND  | 1    | 2     | G35 | ADC     |
|         | GND  | 3    | 4     | G36 | ADC     |
|         | GND  | 5    | 6     | RST | EN      |
| MOSI    | G23  | 7    | 8     | G25 | DAC/SPK |
| MISO    | G19  | 9    | 10    | G26 | DAC     |
| SCK     | G18  | 11   | 12    | 3V3 |         |
| RXD0    | G3   | 13   | 14    | G1  | TXD0    |
| RXD2    | G16  | 15   | 16    | G17 | TXD2    |
| Int SDA | G21  | 17   | 18    | G22 | Int SCL |
| GPIO    | G2   | 19   | 20    | G5  | GPIO    |
| I2S_SK  | G12  | 21   | 22    | G13 | I2S_WS  |
| I2S_OUT | G15  | 23   | 24    | G0  | I2S_MK  |
|         | HPWR | 25   | 26    | G34 | I2S_IN  |
|         | HPWR | 27   | 28    | 5V  |         |
|         | HPWR | 29   | 30    | BAT |         |
::

有关引脚分配和引脚重新映射的更多信息，请参考[ESP32 datasheet](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/644/esp32_datasheet_cn.pdf)。

## 结构文件

- [Faces Kit 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/K005_Faces_Kit/Structures)

## 数据手册

- [ESP32](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/644/esp32_datasheet_cn.pdf)
- [ILI9342C](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/ILI9342C-ILITEK.pdf)
- [MPU6886](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/MPU-6886-000193%2Bv1.1_GHIC_en.pdf)
- [BMM150](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/BMM150_datasheet_en.pdf)
- [IP5306](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/IIC_IP5306_REG_V1.4_cn.pdf)

## 软件开发

### Arduino

- [Faces Kit Arduino 快速上手](/zh_CN/arduino/m5core/program)
- [Faces Kit Arduino 测试程序](https://github.com/m5stack/M5Stack/tree/master/examples/Face)
- [Faces Kit Arduino API](/zh_CN/arduino/m5core/button)
- [GameBoy Arduino 测试程序](https://github.com/m5stack/FACES-Firmware/blob/master/GameBoy.ino)
- [KeyBoard Arduino 测试程序](https://github.com/m5stack/FACES-Firmware/blob/master/KeyBoard.ino)
- [Calculator Arduino 测试程序](https://github.com/m5stack/FACES-Firmware/blob/master/Calculator.ino)

### UiFlow1

- [Faces Kit UiFlow1 快速上手](/zh_CN/uiflow/m5core/program)

### UiFlow2

- [Faces Kit UiFlow2 快速上手](/zh_CN/uiflow2/m5core/program)

### USB 驱动

点击下方连接下载匹配操作系统的驱动程序。目前存在两种驱动芯片版本，CP210X（适用于**CP2104**版本）/CP34X（适用于**CH9102**版本）驱动程序压缩包。在解压压缩包后，选择对应操作系统位数的安装包进行安装。(若您不确定您的设备所使用的 USB 芯片，可同时安装两种驱动。**CH9102_VCP_SER_MacOS v1.7**在安装过程中，可能出现报错，但实际上已经完成安装，忽略即可。)

| 驱动名称                  | 适用驱动芯片 | 下载链接                                                                                             |
| ------------------------- | ------------ | ---------------------------------------------------------------------------------------------------- |
| CP210x_VCP_Windows        | CP2104       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CP210x_VCP_Windows.zip)     |
| CP210x_VCP_MacOS          | CP2104       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CP210x_VCP_MacOS.zip)       |
| CP210x_VCP_Linux          | CP2104       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CP210x_VCP_Linux.zip)       |
| CH9102_VCP_SER_Windows    | CH9102       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CH9102_VCP_SER_Windows.exe) |
| CH9102_VCP_SER_MacOS v1.7 | CH9102       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CH9102_VCP_MacOS_v1.7.zip)  |

### Easyloader

| Easyloader                   | 下载链接                                                                                                          | 备注 |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------- | ---- |
| Fack Kit 出厂固件 Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/CORE/EasyLoader_FACES_FactoryTest.exe) | /    |

### GameBoy Keyboard

如果你想用 M5Core 玩一些经典小游戏，那么使用 GameBoy 面板和 M5Core 会是完美的方案。你需要做的就是将游戏模拟器程序上传到 M5Core 上，并连接好 GameBoy 面板。连接图如下：

ESPTool 烧录游戏教程：[gameboy_burn_a_nes_game](/zh_CN/guide/hobby_kit/faces/gameboy_burn_a_nes_game)

<span class="product-sku"><a href="https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/M5Core/Faces_kit/Faces_GameBoy_BladeBuster.exe">点击此处一键烧录示例游戏</a></span>

另外两个面板是计算器键盘和输入全键盘，你可以将它们运用在那些需要输入信息以及复杂控制的应用场景中。 <mark>拆卸更换面板时，为降低拆卸难度，建议先拆卸 M5Core，然后拆解面板。</mark>

### Others

- Key string values

| Key | AC  | M   | %   | ÷   | 0-9 | X   | -   | +   | =   | +/- | .   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Val | A   | M   | %   | /   | 0-9 | \*  | -   | +   | =   | \`  | .   |

| ESP32 Chip | G23       | G19  | G18 | G14 | G27 | G33 | G32 | G4  |
| ---------- | --------- | ---- | --- | --- | --- | --- | --- | --- |
| ILI9342C   | MOSI/MISO | /    | CLK | CS  | DC  | RST | BL  |     |
| TF Card    | MOSI      | MISO | CLK |     |     |     |     | CS  |

Key Int Values (Int values are the ASCII value of each key)

| Key   | AC  | M   | %   | ÷   | 0-9 | X   | -   | +   | =   | +/- | .   |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Val   | 65  | 77  | 37  | 47  |
| 48-57 | 42  | 45  | 43  | 61  | 96  | 46  |

## 相关视频

- Faces Kit 出厂固件介绍

<video id="example_video" controls>
  <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Core/FACES.mp4">
</video>

\#>**案例描述：**<br/>该案例将默认运行 FACES 键盘输入测试程序，重启选择程序列表可以切换不同的面板测试项。

## 版本变更

| 上市日期 | 产品变动                          |
| -------- | --------------------------------- |
| 2019.7   | TN 屏幕变更为 IPS 屏幕            |
| 2019.6   | MPU9250 变更为 MPU6886+BMM150     |
| 2017.12  | 首次发售                          |

\#> 注意：**2018.2A**PCB 版本的设备不支持 C2C (Type-C to Type-C) 连接及 PD 供电。

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/basic_v2.6/basic_v2.6_2018.2a.webp" width="50%">
