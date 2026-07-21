# Atomic Audio-3.5 Base

<span class="product-sku">SKU:A166</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1219/A166_Atomic_Audio-3.5_Base_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1219/A166_Atomic_Audio-3.5_Base_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1219/A166_Atomic_Audio-3.5_Base_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1219/A166_Atomic_Audio-3.5_Base_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1219/A166_Atomic_Audio-3.5_Base_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1219/A166_Atomic_Audio-3.5_Base_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1219/A166_Atomic_Audio-3.5_Base_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1219/A166_Atomic_Audio-3.5_Base_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1219/A166_Atomic_Audio-3.5_Base_09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1219/A166_Atomic_Audio-3.5_Base_10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1219/A166_Atomic_Audio-3.5_Base_11.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1219/A166-weight.jpg">
</PictureViewer>

## 描述

**Atomic Audio-3.5 Base** 是一款为 Atom 系列主控设计的语音识别与音频播放底座 (不兼容 Atom Voice)，机身集成 ES8311 单声道音频解码器、MEMS 麦克风以及 NS4150B 功放芯片，配备标准 3.5mm 音频接口与四段式 TRRS 接口（CTIA 标准），支持音频输出以及麦克风输入。ES8311 支持 24 位音频分辨率，采样率范围为 16kHz~64kHz，采用 I2S 通信接口，可实现高保真音频处理。板载 MEMS 麦克风具备高信噪比和数字输出能力，针对自动语音识别场景进行了优化；集成扬声器可提供高效音频输出。该底座支持全双工通信，可同时进行音频信号的发送与接收，适用于语音助手、语音控制终端、智能家居语音网关、语音交互设备等场景。

## 产品特性

- 内置麦克风与扬声器
- 3.5mm 音频接口
  - 支持音频输出 + 麦克风输入
  - 内置插入检测，自动切换外置麦克风线路
- 集成 ES8311 高保真音频解码，支持 24bit 高解析音频处理
- 支持全双工语音通信，可同步实现音频收发

## 包装内容

- 1 x Atomic Audio-3.5 Base
- 1 x 内六角扳手 L 形 1.5mm (适配 M2 螺丝)
- 1 x M2 \* 8mm 螺丝 (杯头，机械牙)

## 应用场景

- Atom 扩展底座
- DIY 节点控制器
- 外设接口扩展

## 规格参数

| 项目         | 参数                                                                                                 |
| ------------ | ---------------------------------------------------------------------------------------------------- |
| 音频编解码器 | ES8311                                                                                               |
| MEMS 麦克风  | ME1502AM5G                                                                                           |
| 扬声器       | 1W@8Ω NS4150B                                                                                        |
| 音频接口     | 3.5mm 耳机插座，四段式 TRRS 接口（CTIA 标准），兼容 15mm 标准插头                                    |
| 稳压器       | TPS7A2033PDQNR                                                                                       |
| GPIO 扩展    | PI4IOE5V6408ZTAEX                                                                                    |
| 功耗         | 待机模式：5V@1.83mA<br>录音模式：5V@12.71mA<br>50% 音量播放：5V@21.19mA<br>100% 音量播放：5V@26.46mA |
| 产品尺寸     | 48.0 x 24.0 x 17.5mm                                                                                 |
| 产品重量     | 12.0g                                                                                                |
| 包装尺寸     | 138.0 x 93.0 x 18.0                                                                                  |
| 毛重         | 15.5g                                                                                                |

## 操作说明

### 麦克风开关切换

板载麦克风切换开关，可适应不同应用场景需求：

- ON: 保持板载麦克风供电，外接音箱时继续使用内置麦克风。
- OFF: 3.5mm 接口接入外设时，自动切换至外置麦克风，适合外接耳机场景。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1219/switch-operate.jpg" width="40%">

### 耳机插头类型与接线标准说明

音频接口采用四触点 TRRS（Tip-Ring-Ring-Sleeve） 结构，可同时支持立体声播放与麦克风输入，实现音频输出与语音输入一体化；接口遵循 CTIA 美标接线规范。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1219/A166-earphone-note.png" width="40%">

## 原理图

- [Atomic Audio-3.5 Base 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1219/A166_SCHE_Atomic_Audio-3.5.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1219/A166_SCHE_Atomic_Audio-3.5_page_01.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1219/A166_SCHE_Atomic_Audio-3.5_page_02.png">
</SchViewer>

## 管脚映射

### 功放芯片控制

| PI4IOE5V6408 (0x43) | P0     |
| ------------------- | ------ |
| NS4150B             | PW_AMP |

### Atomic Audio-3.5 Base-Bus

::m5-bus-table
| PIN | LEFT | RIGHT | PIN    |
| --- | ---- | ----- | ------ |
|     |      | 1     | 3V3    |
| SCL | 2    | 3     | DSDIN  |
| SDA | 4    | 5     | LRCK   |
| 5V  | 6    | 7     | ASDOUT |
| GND | 8    | 9     | SCLK   |
::

## 尺寸图

- [Atomic Audio-3.5 Base](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1219/A166-model-size.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1219/A166-model-size_page_01.png" width="100%">

## 数据手册

- [ES8311](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/Atomic%20Echo%20Base/ES8311.pdf)
- [NS4150B](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/Atomic%20Echo%20Base/NS4150B.pdf)
- [PI4IOE5V6408ZTAEX](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1219/PI4IOE5V6408ZTAEX.pdf)

## 软件开发

### Arduino

- [Atomic Audio-3.5 Base Arduino 使用教程](/zh_CN/arduino/projects/atomic/atomic_audio-3.5_base)
- [Atomic Audio-3.5 Base Arduino 驱动库](https://github.com/m5stack/M5Atomic-EchoBase)

## 相关视频

- Atomic Audio-3.5 Base 产品介绍以及功能展示

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1219/A166-Atomic-Audio-3.5-Base-video_ZH.mp4" type="video/mp4"></video>
