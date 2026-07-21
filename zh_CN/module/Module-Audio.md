# Module Audio

<span class="product-sku">SKU:M144</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1141/M144_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1141/M144_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1141/M144_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1141/M144_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1141/M144_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1141/M144_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1141/M144_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1141/M144_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1141/M144_09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1141/M144_10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1141/M144_Weight.jpg">
</PictureViewer>

## 描述

**Module Audio** 是一款面向音频交互的 M5Stack 扩展模块，基于 **ES8388** 音频编解码方案，提供双通道 3.5 mm 音频接口（**TRS** 音频接口仅支持输入，**TRRS** 复合接口支持麦克风输入与耳机播放），可满足各类麦克风录音与立体声音频播放需求。内置 STM32G030F6P6 微控制器，支持 TRRS 插孔插拔检测及 WS2812C **RGB** 灯效驱动。可通过寄存器配置实现 CTIA（美标）与 OMTP（国标）两种耳机接线标准的切换，兼容市面主流带麦耳机。该产品适用于智能语音，交互艺术，教育娱乐，便携录播等多种音频应用场景。

## 产品特性

- STM32G030F6P6 MCU 控制
- 高保真音频编解码
- 双路麦克风输入
- TRS + TRRS 双 3.5 mm 插孔
- 支持 CTIA/OMTP 接口切换
- WS2812C RGB 指示灯
- 开发平台
  - UiFlow1
  - UiFlow2
  - Arduino IDE

## 包装内容

- 1 x Moduel Audio

## 应用场景

- 智能音箱
- 语音识别
- 教育娱乐
- 交互式艺术装置

## 规格参数

| 规格            | 参数                                                        |
| --------------- | ----------------------------------------------------------- |
| MCU             | STM32G030F6P6，I2C 通信 @ 0x33                              |
| 音频编解码器    | ES8388，I2C 通信 @ 0x10                                     |
| 音频输入 / 输出 | 2 路麦克风输入，1 路立体声耳机输出 (HPOUT_L/HPOUT_R)        |
| 插孔类型        | 1 x TRS（麦克风专用），1 x TRRS（麦克风 / 扬声器 组合插孔） |
| 状态指示灯      | 3 x WS2812C_2020                                            |
| 耳机标准切换    | CTIA (美标) / OMTP (国标)                                   |
| 工作电流        | DC 3.3V@23.53mA                                             |
| 待机电流        | DC 3.3V@8.58mA                                              |
| 工作温度        | 0 ~ 40 °C                                                   |
| 产品尺寸        | 54.0 x 54.0 x 13.1mm                                        |
| 产品重量        | 12.8g                                                       |
| 包装尺寸        | 132.0 x 95.0 x 16.0mm                                       |
| 毛重            | 26.3g                                                       |

## 操作说明

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1141/M144_Earphone_instruction.jpg" width="60%">

\#> 耳机插头类型与接线标准 | 在音频接口方面，常见的插头分为三节触点的 TRS 和四节触点的 TRRS 两种： <br/> - **TRS（Tip-Ring-Sleeve）** 三触点结构仅用于单声道麦克风输入或立体声输出，此产品仅做麦克风输入； <br/> - **TRRS（Tip-Ring-Ring-Sleeve）** 四触点结构在提供左右声道播放的同时，额外增加麦克风通道，可实现麦克风输入与立体声播放合一。 <br/>针对 TRRS 插头，还存在两种不同的接线标准： <br/> - **CTIA（美标）**：L (Tip) = 左声道，R (Ring1) = 右声道，MIC (Ring2) = 麦克风，GND (Sleeve) = 地线；<br/> - **OMTP（国标）**：L (Tip) = 左声道，R (Ring1) = 右声道，GND (Ring2) = 地线，MIC (Sleeve) = 麦克风。

## 原理图

- [Module Audio 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1141/M144_sch_moduleaudio_v10.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1141/M144_sch_moduleaudio_v10_page_01.png">
</SchViewer>

## 管脚映射

### RGB & FSUSB42MUX & I2C

| STM32G030F6P6 | PA7     | PA2         | PA1    | PA12 | PA11 |
| ------------- | ------- | ----------- | ------ | ---- | ---- |
| WS2812C       | LED_DAT |             |        |      |      |
| FSUSB42MUX    |         | HP_MODE_SET | HP_DET |      |      |
| I2C           |         |             |        | SDA  | SCL  |

\#> 引脚说明 | Module Audio 板上预留 A/B 两组 对应 I2S 引脚用于切换 I2S 信号与主机默认管脚映射用： <br/>- 引脚预设 A 对应 Basic/Core2 的 I2S 默认管脚 <br/>- 引脚预设 B 对应 CoreS3 的 I2S 默认管脚，因为 CoreS3 板载 ES7210 已占用原有 I2S 引脚，需要切换以避免冲突 <br/> <img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1141/M144_AB_Mode.jpg" width="50%">

### M5-Bus

::m5-bus-table
| PIN      | LEFT | RIGHT | PIN               |
| -------- | ---- | ----- | --------          |
| GND      | 1    | 2     |                   |
| GND      | 3    | 4     |                   |
| GND      | 5    | 6     | RST               |
|          | 7    | 8     |                   |
|          | 9    | 10    |                   |
|          | 11   | 12    | 3V3               |
|          | 13   | 14    |                   |
|          | 15   | 16    |                   |
| SDA      | 17   | 18    | SCL               |
|          | 19   | 20    |                   |
| I2S_LRCK | 21   | 22    | I2S_MCLK/I2S_SCLK |
| I2S_OUT  | 23   | 24    | I2S_MCLK/I2S_SCLK |
|          | 25   | 26    | I2S_IN            |
|          | 27   | 28    | 5V                |
|          | 29   | 30    |                   |
::

## 尺寸图

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1141/M144_Model_sizel_page_01.png" width="100%">

## 数据手册

- [ES8388](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1141/ES8388.pdf)

## 软件开发

### Arduino

- [Module Audio Arduino Quick Start](/zh_CN/arduino/projects/module/module_audio)
- [Module Audio Arduino 驱动库](https://github.com/m5stack/Module-Audio)

### UiFlow1

- Coming Soon...

### UiFlow2

- [Module Audio UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/module/audio.html)

### 内置固件

- [Module Audio 内置固件](https://github.com/m5stack/M5Module-Audio-Internal-FW)

### 通信协议

- [Module Audio I2C Protocol](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1141/M144_Protocol.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1141/M144_Protocol_page_01.png" width="100%">

- I2C Address

| Chip          | I2C Address |
| ------------- | ----------- |
| STM32G030F6P6 | 0x33        |
| ES8388        | 0x10        |

## 相关视频

- Module Audio 产品介绍以及案例展示

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1141/M144_Video.mp4" type="video/mp4"></video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=114589056372328&bvid=BV1PhjyzZE87&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/D7Fz5ni-gmI?si=swsVvUZbaQhmT5od" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
