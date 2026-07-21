# M5Stack 硬件产品与软件支持总览

M5Stack 作为领先的物联网解决方案提供商，打造面向 IoT 与快速原型开发的模块化平台，整合易用硬件、图形化软件及定制服务，助力开发者和企业在 IIoT、智慧零售、智能家居、AI 应用及 STEM 教育等场景中，将创意迅速转化为创新产品。

## 文档快速入口

| 入口链接                                   | 内容介绍                                                                                                                                                                    |
| ------------------------------------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [产品页面](/zh_CN/products)                | 每款产品的信息页面，包含产品图片、产品特性、包装内容、规格参数、原理图、管脚映射、<br>接口、尺寸、芯片数据手册、开发平台支持情况、产品视频等信息。                          |
| [UiFlow 开发](/zh_CN/uiflow2/uiflow_web)   | UiFlow1、UiFlow2 图形化开发平台的特点介绍与使用教程，<br>平台支持的各产品、各功能的简单开发例程。                                                                           |
| [Arduino 开发](/zh_CN/arduino/arduino_ide) | Arduino IDE、板管理、库管理安装教程，<br>支持 Arduino 开发的各款主控及外设产品、各项功能的简单开发例程，<br>M5Unified、M5GFX 库的 API 文档。                                |
| [拓展应用](/zh_CN/guide/product_guide)     | 产品接入第三方平台的教程（如 OpenAI、小智、Home Assistant、The Things Network、Meshtastic），<br>以及一些产品的专门教程（如摄像头固件操作、恢复出厂固件、DIP 拨码开关）等。 |

## 硬件产品体系

M5Stack 提供了丰富多样的硬件产品，涵盖了从主控到传感 / 执行单元等外设、从初级入门到高级应用的广泛需求。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/controller_family.png" width="90%">

### 主控产品

| 主控产品                                            | 主要形态                                                                                                                 | 特点介绍                                                                                                                                  |
| --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ | :----------------------------------------------------------------------------------------------------------------------------------------- |
| [Core 系列](/zh_CN/products?id=核心控制器-core)     | <img src="https://static-cdn.m5stack.com/resource/docs/products/core/basic_v2.7/basic_v2.7_cover_01.webp"   width="30%"> | - 集成了显示屏、按键、扬声器、麦克风、电池、扩展接口。<br>- 主要产品包括 Core（Basic、Gray、Fire）、Tough、Core2、CoreS3、Tab5 等。       |
| [Stick 系列](/zh_CN/products?id=核心控制器-stick)   | <img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5StickC%20PLUS2/3.webp" width="30%"> | - 为可穿戴和便携应用设计，外形修长紧凑。<br>- 主要产品包括 StickC Plus、StickC Plus2 等。                                                 |
| [Atom 系列](/zh_CN/products?id=核心控制器-atom)     | <img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3R/3.webp"          width="30%"> | - 体积微小，适合嵌入式应用、物联网节点、便携式项目。<br>- 主要产品包括 Atom Lite、Atom Echo、AtomS3、AtomS3U、AtomS3R、AtomS3R Cam 等。   |
| [Stamp 系列](/zh_CN/products?id=核心控制器-stamp)   | <img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1150/S007-V033_07.webp"                          width="30%"> | - 形似邮票，为最小形态的主控产品，通常嵌入不同的功能底座形成完整的可用产品。<br>- 如 Dial、Cardputer、Air Quality、DinMeter、VAMeter 等。 |
| [Paper 系列](/zh_CN/products?id=核心控制器-e-paper) | <img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/PaperS3/3.webp"          width="30%"> | - 使用电子墨水屏，功耗较低，适合持续显示信息的场景。<br>- 主要产品包括 CoreInk、Paper、PaperS3 等。                                       |
| [其他](/zh_CN/products?id=核心控制器-ai%20kit)      | —                                                                                                                        | - 其他非标准形态的主控产品。<br>- 如 LLM630 Compute Kit、Station、NanoC6 等。                                                             |

### 外设产品

| 外设产品                                               | 主要形态                                                                                                                                          | 特点介绍                                                                                                                                                                                                                                                                                                                                                    |
| ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Unit 系列](/zh_CN/products?id=unit系列-传感器)        | <img src="https://static-cdn.m5stack.com/resource/docs/products/unit/ULTRASONIC%20I2C/img-765d42b8-3471-4151-841e-9fe803eb95ad.webp" width="30%"> | - 包含丰富多样的传感器、执行器、接口拓展、电机驱动、人机交互（屏幕、灯、按钮、旋钮等）、音频视频摄像头、通信等功能单元。<br>- 可以通过 **HY2.0-4P Grove 接口**（见下文介绍）方便地连接至各种主控，以增加相应的硬件功能。                                                                                                                                    |
| [Stack 系列](/zh_CN/products?id=stack系列-module)      | <img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/639/M029-V12_04.webp"                                                     width="30%"> | - 包含多种传感器、执行器、接口拓展、电机驱动、人机交互（键盘、按钮、旋钮等）、音频视频、通信、电池、LLM 等功能单元。<br>- 按照形态尺寸分为 **Module**、**Module13.2**、**Base**、**Faces** 四类，可以通过 **M5-Bus**（见下文介绍）方便地堆叠连接至 Core 系列主控（支持多个产品堆叠），以增加相应的硬件功能。                                                |
| [Stick 系列](/zh_CN/products?id=stick系列-传感器)      | <img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat_envIII/hat_envIII_cover_01.webp"                             width="30%"> | - 包含多种传感器、执行器、接口拓展、电机驱动、人机交互（按钮、旋钮等）、音频、通信、电池等功能单元。<br>- 可以通过 **8pin 排针**方便地连接至 Stick 系列主控，以增加相应的硬件功能。<br>- 由于安装方式像给 Stick 主控戴了一顶帽子，所以称为 **Hat** 系列。                                                                                                   |
| [Atom 系列](/zh_CN/products?id=atom系列-atomic%20base) | <img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/Atomic%20QRCode2%20Base/3.webp"                   width="30%"> | - 包含多种传感器、执行器、接口拓展、电机驱动、音频视频、通信、电池等功能单元。<br>- 可以通过 **4+5pin 排针**方便地连接至 Atom 系列主控，以增加相应的硬件功能。<br>- 其中大部分产品称为 **Atomic Base**，具有数据传输功能的称为 **Atom DTU**，产品中包含 Atom 主控的称为 **Atom Kit**，通过 **USB-C 及 4pin 排母**连接至 Atom 主控侧面的称为 **Atom Tail**。 |
| [Stamp 系列](/zh_CN/products?id=stamp系列-无线通信)    | <img src="https://static-cdn.m5stack.com/resource/docs/products/stamp/stamp_catm/stamp_catm_cover_01.webp"                           width="30%"> | - 与 Stamp 系列主控形态类似，可用于 PCB 贴片，或嵌入其他产品以增加相应的硬件功能。                                                                                                                                                                                                                                                                          |
| [兴趣套件](/zh_CN/products?id=兴趣套件-无人机)         | <img src="https://static-cdn.m5stack.com/resource/docs/products/app/Stamp%20Fly/3.webp"                                              width="30%"> | - 使用 M5Stack 主控设备的兴趣套件，如无人机、机器人小车等。                                                                                                                                                                                                                                                                                                 |
| [配件](/zh_CN/products?id=配件-线材)                   | <img src="https://static-cdn.m5stack.com/resource/docs/products/accessory/cable/grove_cable/grove_cable_cover_01.webp"               width="30%"> | - 包含线材、舵机、接口转换器、摄像头模组、结构件（用于固定 / 连接 / 安装）、下载器、耗材 / 替换件、维修套件等各种主控和外设产品所需的配件。                                                                                                                                                                                                                 |

### 连接关系

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/hardware_connection.png" width="50%">

## 软件开发支持

M5Stack 产品体系的丰富易用不仅体现在硬件，软件支持方面也提供了多样的选择，以适应不同背景和水平的开发者。

### M5Burner

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/m5burner/m5burner_intro_01.png" width="70%">

M5Burner 是 M5Stack 产品的固件平台，集成了固件烧录、导出、发布、分享与串口监视等功能。软件内提供了官方定期更新的产品 UserDemo（出厂固件）、UiFlow 固件，还有众多用户上传的有趣程序，可以方便快速地烧录至设备中。

- [下载地址及使用教程](/zh_CN/uiflow/m5burner/intro)

### 图形化编程

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/uiflow2.0_banner_02.jpg" width="70%">

- 由 M5Stack 基于 MicroPython 和 Blockly 研发
- 在图形化界面中拖拽式编程，极大降低入门门槛
- 实时更新代码，无需编译即可运行和调试
- 适用于教育、初学者或快速原型演示
- 使用教程：[UiFlow1](/zh_CN/uiflow/uiflow_web)、[UiFlow2](/zh_CN/uiflow2/uiflow_web)
- 工具地址：[UiFlow1](https://flow.m5stack.com)、[UiFlow2](https://uiflow2.m5stack.com)

### 代码编程

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/Arduino_IDE_2.png" width="70%">

- 支持 Arduino、PlatformIO、ESP-IDF、MicroPython 等语言、框架、IDE
- 业界广泛使用的嵌入式编程工具，开发生态完善
- 丰富的示例和社区支持，适合大多数开发者
- 适合复杂项目，提供强大的调试工具和灵活的项目配置

### 板管理器与驱动库

| 项目                         | 相关链接                                                                                                                                                                            | 介绍                                                                                                                                                                                       |
| ---------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 板管理器<br>Board Manager    | - [Arduino IDE 板管理器安装教程](/zh_CN/arduino/arduino_board)                                                                                                                      | M5Stack 专属板管理器，使开发者轻松安装和管理各款硬件开发板定义，确保兼容性和便捷性。                                                                                                       |
| M5Unified                    | - [M5Unified - GitHub](https://github.com/m5stack/M5Unified)<br>- [M5Unified 文档](/zh_CN/arduino/m5unified/helloworld)<br>- [迁移至 M5Unified](/zh_CN/arduino/m5unified/migration) | 各系列主控产品的统一硬件驱动库，抽象了不同硬件的差异，提供统一的接口，简化了跨设备开发的体验。<br>M5Unified 库基本替代了原先每款产品专门的驱动库，**建议将原先的驱动库迁移至 M5Unified**。 |
| M5GFX                        | - [M5GFX - GitHub](https://github.com/m5stack/M5GFX)<br>- [M5GFX 文档](/zh_CN/arduino/m5gfx/m5gfx)                                                                                  | 与 M5Unified 配合使用的图形库。                                                                                                                                                            |
| 各款主控<br>对应的硬件驱动库 | ——                                                                                                                                                                                  | 如 M5Stack、M5StickC 等。如上所述，**建议迁移至 M5Unified**。                                                                                                                              |
| M5UnitUnified                | - [M5UnitUnified - GitHub](https://github.com/m5stack/M5UnitUnified)                                                                                                                | Unit 系列外设产品的统一硬件驱动库，目前为 alpha 版本。                                                                                                                                     |
| 各款外设<br>对应的硬件驱动库 | ——                                                                                                                                                                                  | 如 M5Unit-ENV、M5Unit-UHF-RFID、M5Unit-Roller 等。                                                                                                                                         |
| uiflow-micropython           | - [uiflow-micropython - GitHub](https://github.com/m5stack/uiflow-micropython)                                                                                                      | UiFlow 的底层驱动库，也可以使用此库进行纯 MicroPython 的开发。                                                                                                                             |
| lv_m5_emulator               | - [lv_m5_emulator - GitHub](https://github.com/m5stack/lv_m5_emulator)                                                                                                              | 通过 PlatformIO 运行在电脑上的 M5Stack LVGL 设备模拟器，支持 LVGL V8 和 V9。                                                                                                               |
| M5_Hardware                  | - [M5_Hardware - GitHub](https://github.com/m5stack/M5_Hardware)                                                                                                                    | 部分产品的结构和 PCB 文件。                                                                                                                                                                |

## 接口通信协议

为了方便开发，我们为 M5Stack 设备提供了标准化的接口和协议支持。

### HY2.0-4P Grove 接口

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/start/interface/grove_connect_01.png" width="50%">

模块化的通用接口，无需焊接即可快速连接各种传感器、执行器等外设，实现硬件调试。具有防反插设计。

::grove-table
| 接口分类 | Black | Red | Yellow | White | <span style="color:black">标准协议</span> |
| -------- | ----- | --- | ------ | ----- | ----------------------------------------- |
| PORT.A   | GND   | 5V  | SDA    | SCL   | I2C                                       |
| PORT.B   | GND   | 5V  | IO1    | IO2   | GPIO                                      |
| PORT.C   | GND   | 5V  | TX     | RX    | UART                                      |
| 其他     | GND   | 5V  | 通用   | 通用  | 通用                                      |
::

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/start/interface/grove_01.jpg" width="50%">

### M5-Bus

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/M5-Bus.png" width="70%">

Core 系列主控与 Module、Module13.2、Base 系列外设所用的可堆叠总线接口，由 2 排 15pin 2.54mm 间距的排针组成。

### UART（Universal Asynchronous Receiver-Transmitter）

经典且常用的串行通信协议，用于设备间数据传输、串口监控和调试。常见引脚定义为 TX、RX，请注意一个设备的 TX 需要连接到另一个设备的 RX，反之亦然。

### I2C（Inter-Integrated Circuit）

双线式通信协议，简单易用，适用于传感器和显示模块的通信。常见引脚定义为 SDA、SCL。

### SPI（Serial Peripheral Interface）

高速的串行通信接口，常用于连接显示屏、存储器和高级外设。常见引脚定义为 SS、SCLK、MOSI、MISO。

## 开发辅助工具

### EzData

<img src="https://static-cdn.m5stack.com/resource/docs/static/image/iotservice/ezdata/ezdata_01.webp" width="70%">

EzData 是 M5Stack 提供的一个 IoT 云端数据储存服务，不同的设备之间可以通过唯一 token，向储存队列中插入或提取数据，实现数据共享。

- [EzData Arduino 教程](/zh_CN/arduino/ezdata/ezdata_arduino)
- [EzData UiFlow2 教程](/zh_CN/uiflow2/blockly/ezdata/ezdata_manager)
- [EzData API 文档](https://ezdata2.m5stack.com/doc.html#/home)

### EasyLoader

EasyLoader Packer 工具可以将代码打包生成 exe 可执行文件，分享给他人后可以直接将你的程序载入他们的设备中，而无需使用 Arduino IDE 等额外的工具。生成端为网页，支持 Windows、macOS、Linux；生成的 exe 仅支持 Windows 使用。

- [使用教程](/zh_CN/guide/easyloader/easyloader_packer)
- [工具地址](https://tools.m5stack.com/easyloader-packer/)

## 数据查询对比

### I2C 地址

列举了各款主控和外设产品中 I2C 部件的地址，包括固定地址、可编程地址、可切换地址。

- [页面地址](/zh_CN/product_i2c_addr)

### 产品参数对比

各系列同类产品的硬件参数对比，方便产品选型。

- [页面地址](/zh_CN/products_selector/m5core_compare)

### Stack 堆叠螺丝长度

不同的 Core、Module、Module13.2、Base 堆叠时所需的螺丝长度。

- [页面地址](/zh_CN/learn/extension/module)
