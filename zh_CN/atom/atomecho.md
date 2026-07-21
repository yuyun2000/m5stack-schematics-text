# Atom Voice

<span class="product-sku">SKU:C008-C</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/676/C008-C_01.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/676/C008-C_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/676/C008-C_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/676/C008-C_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/676/C008-C_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/676/C008-C_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/676/C008-C_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/676/C008-C.webp">
</PictureViewer>

## 描述

**Atom Voice** 是一款基于 ATOM 设计的可编程智能音箱，它的体积非常小巧，只有 24 x 24 x 17mm。通过 ESP32 自带的无线功能与手机、平板等进行连接即可播放音乐，也可以通过 Wi-Fi 播放指定的流媒体音乐。为了方便用户使用语音功能，我们在**Atom Voice**内集成了 STT（语音转文字）服务，您可以通过烧录指定固件开启该功能，通过语音下达指令完成多样化的操作。当然，您还可以通过自行编写代码接入 AWS、GOOGLE 等云平台，使用内置麦克风和扬声器进行语音交互，使得**Atom Voice**具备一定的 AI 能力，实现语音控制、智能对话、物联网等功能。音箱内嵌一颗 RGB LED (SK6812)，可以直观的显示连接状态。除了可以作为智能音箱使用外，它依然具备了 ATOM 系列的控制能力，你可以通过 GROVE 接口连接外部设备。其背面有一个 M2 螺丝孔，方便用户进行固定。

## 教程 & 快速上手

learn>| ![Home Assistant](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/hhome_assistant_cover_02.jpg) | [Home Assistant](https://www.home-assistant.io/voice_control/thirteen-usd-voice-remote/) | 本教程将向你介绍，如何将 Atom Voice 连接到 Home Assistant。 |

learn>| ![Arduino IDE](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/arduino_banner_01.png) | [Arduino IDE](/zh_CN/arduino/m5atomecho/program) | 本教程将向你介绍，如何通过 Arduino IDE 编程控制 Atom Voice 设备。 |

learn>| ![UiFlow Echo STT](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/uiflow1.0_banner_01.png) | [UiFlow Echo STT](/zh_CN/uiflow/blockly/media_trans/echo_stt) | 本教程将向你介绍，其他的 M5 设备如何通过 UiFlow 获取 Atom Voice STT 的识别结果。 |

learn>| ![Atom Voice 蓝牙音箱](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/676/atom-voice_BT_09.jpg) | [Atom Voice 蓝牙音箱](/zh_CN/guide/input_device/atom_voice) | 本教程介绍如何使用 M5Burner 为 Atom Voice 烧录蓝牙音箱固件，并介绍其无线音箱的使用方法。 |

## 注意事项

### 引脚使用注意事项

!>注意|Atom Voice 底部总线 G19、G22、G23、G33 引脚已作为设备内部音频 I2S 通信接口使用，禁止外部复用、外接扩展模块及二次接线。外接 Atomic 系列外设时，切勿占用以上引脚，违规使用易造成音频通路异常，严重时将导致硬件永久性损坏。

### 播放注意事项

为了防止人为损坏 Atom Voice, 请在使用时避免以下操作。 <br/>- 使用 I2S 通道输出 DC 信号<br/> - 长时间播放白噪音<br/> - 不要播放全幅方波音频。

## 产品特性

- 轻便小巧
- 支持 STT 服务
- 基于 ESP32, 支持 A2DP、BLE 4.0
- Wi-Fi 协议 IEEE 802.11b/g/n
- 内置麦克风与扬声器
- RGB LED 状态显示
- GROVE 扩展接口
- 录音与声音回放
- 独立可编程按键
- 编程平台：Arduino、ESP-IDF/ADF

## 包装内容

- 1 x Atom Voice

## 应用场景

- 无线音箱
- 语音控制
- 物联网

## 规格参数

| 规格      | 参数                                    |
| --------- | --------------------------------------- |
| SoC       | ESP32-PICO-D4,240MHz,Dual Core,Wi-Fi    |
| Flash     | 4MB                                     |
| Interface | 1 x IR-TX，1 x Button，1 x Reset Button |
| PinOut    | G21/G25/5V/GND, 3V3/G22/G19/G23/G33     |
| RGB LED   | SK6812                                  |
| SPEAKER   | 0.8W/NS4168 I2S                         |
| MIC       | SPM1423 PDM                             |
| 外壳材质  | Plastic （ PC ）                        |
| 产品尺寸  | 24.0 x 24.0 x 16.8mm                    |
| 产品重量  | 9.0g                                    |
| 包装尺寸  | 85.0 x 65.0 x 17.0mm                    |
| 毛重      | 15.5g                                   |

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atomecho/atomecho_sch_01.webp" width = "50%">

## 管脚映射

### SPK & MIC

| Atom Voice | G22      | G19      | G33      | G23      |
| ---------- | -------- | -------- | -------- | -------- |
| NS4168     | AMP DATA | AMP BCLK | AMP LRCK |          |
| SPM1423    |          |          | MIC CLK  | MIC DATA |

### HMI

| Atom Voice | G27  | G39   |
| ---------- | ---- | ----- |
| RGB LED    | Data |       |
| Button     |      | Input |

### HY2.0‑4P

::grove-table
| HY2.0‑4P    | Black | Red | Yellow | White |
| ----------- | ----- | --- | ------ | ----- |
| PORT.CUSTOM | GND   | 5V  | G26    | G32   |
::

## 尺寸图

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/atomecho/module%20size.jpg" width="80%">

## 结构文件

- [Atom Voice 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/C008-C_Atom_Voice/Structures)

## 数据手册

- [ESP32-PICO-D4](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/669/esp32-pico_series_datasheet_cn.pdf)
- [SPM1423](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/SPM1423HM4H-B_datasheet_en.pdf)
- [NS4168](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/NS4168_CN_datasheet.pdf)

## 软件开发

### 快速上手

- [Atom Voice 蓝牙音箱](/zh_CN/guide/input_device/atom_voice)

### Arduino

- [Atom Voice Arduino 快速上手](/zh_CN/arduino/m5atomecho/program)
- [Atom Voice 录制与播放示例](https://github.com/m5stack/M5Atom/tree/master/examples/Echo/RecordPlay)
- [Atom Voice 播放音乐示例](https://github.com/m5stack/M5Atom/tree/master/examples/Echo/PlayMusic)
- [Atom Voice EchoSTT示例](https://github.com/m5stack/M5Atom/tree/master/examples/Echo/EchoRest)

### ESP-IDF

- [出厂蓝牙音箱固件](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/Core/Atom/AtomEcho/Factory_BT_SPEAKER_Firmware)

### USB 驱动

#### 驱动安装

将设备连接至 PC，打开设备管理器为设备安装[FTDI驱动](https://ftdichip.com/drivers/vcp-drivers/)。以 win10 环境为例，下载匹配操作系统的驱动文件，并解压，通过设备管理器进行安装。(注：某些系统环境下，需要安装两次，驱动才会生效，未识别的设备名通常为`M5Stack`或`USB Serial`, Windows 推荐使用驱动文件在设备管理器直接进行安装 (自定义更新), 可执行文件安装方式可能无法正常工作)。[点击此处，前往下载FTDI驱动](https://ftdichip.com/drivers/vcp-drivers/)

\#>MacOS 用户注意事项 | 对于 MacOS 用户安装前请勾选 `系统偏好设置` - >`安全性与隐私` - >`通用` - >`允许以下位置下载的App` - > `App Store和认可的开发者选项`。

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/ftdi_01.webp" width="30%"><img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/ftdi_02.webp" width="30%"><img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/ftdi_03.webp" width="30%">

### Easyloader

\#> 无线音箱 | 采用 A2DP 协议传输音频数据（暂不支持接打电话）。通电后显示红色 LED，当与无线设备建立连接后 LED 变为绿色，此时可以将声音通过 Atom Voice 进行输出。断开连接后 LED 变回红色。该固件在 ESP-IDF 平台下进行编译，普通用户可直接通过下载 EasyLoader 进行烧录。高级用户如需自行开发其他功能，可根据乐鑫官方文档进行 ESP-IDF 环境搭建，出厂固件源码及 BIN 文件见以下链接，其中 BIN 文件烧录地址为 0x0000。

| Easyloader                                | 下载链接                                                                                                                    | 备注 |
| ----------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | ---- |
| Atom Voice RecordPlay Example Easyloader  | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/atomecho/Atom%20Echo%20RecordPlay.exe)  | /    |
| Atom Voice BT Speaker Firmware Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/ATOM_BASE/EasyLoader_ECHO_Bluetooth_Speaker.exe) | /    |

## 相关视频

<video id="example_video" controls>
  <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Core/AtomEcho.mp4" type="video/mp4">
</video>

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Core/ATOM_ECHO.mp4" type="video/mp4" >
</video>

**设置 M5Stack Atom Voice 作为家庭语音助手的教程**

<video class="video-container" controls>
    <source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/676/Atom-Echo-Home-Assistant-VIDEO.mp4" type="video/mp4">
</video>

## 产品对比

如需对比 Atom 系列产品信息，可访问[产品选型表](/zh_CN/products_selector/m5atom_compare?select=C008-C)，勾选目标产品即可获取对比结果。选型表涵盖核心参数、功能特性等关键信息，支持多产品同步比对。
