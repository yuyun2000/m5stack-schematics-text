# Atom SPK

<span class="product-sku">SKU:K054</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_spk/atom_spk_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_spk/atom_spk_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_spk/atom_spk_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_spk/atom_spk_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_spk/atom_spk_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_spk/atom_spk_06.webp">
</PictureViewer>

## 描述

**Atom SPK** 是一款适配 Atom-Lite 主控的音频播放器，内置 I2S 数字音频接口的功放芯片 NS4168，具备自动采样率检测，自适应功能，并能够有效防止音频信号失真。集成 TFCard 卡槽，便于音频文件的保存与读取。提供 3.5mm 耳机接口与外部扬声器接口，用户可通过外接耳机或是扬声器进行音频播放。

## 产品特性

- 功放芯片 NS4168
- I2S 串行数字音频输入接口
- 支持宽范围采样速率：8kHz~96kHz
- 自动采样率检测，自适应功能
- TFCard 卡槽
- 耳机接口
- 扬声器接口

## 包装内容

- 1 x Atom-Lite
- 1 x Atomic SPK Base
- 1 x 1W Speaker
- 1 x M2 内六角扳手
- 1 x M2\*8 杯头机械牙螺丝
- 1 x USB Type-C 连接线 (20cm)

## 应用场景

- 音频播放器
- 无线音响
- Wi-Fi 音响

## 规格参数

| 规格         | 参数           |
| ------------ | -------------- |
| 功放芯片     | NS4168         |
| 功放输出功率 | 1W（VDD=3.3V） |
| 耳机接口     | 3.5mm          |
| 扬声器接口   | 1.25mm-2P      |
| 扬声器功率   | 1W             |
| 产品尺寸     | 24.0 x 48.0 x 18.0mm |
| 产品重量     | 18.6g          |
| 包装尺寸     | 54.0 x 54.0 x 20.0mm |
| 毛重         | 37.0g            |

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_spk/atom_spk_sch_01.webp" width="80%">

## 管脚映射

::m5-bus-table
| PIN   | LEFT | RIGHT | PIN      |
| ----- | ---- | ----- | -------- |
|       |      | 1     | 3V3      |
| LRCLK | 2    | 3     | BLCK     |
| DATA  | 4    | 5     | SPI_MOSI |
| 5V    | 6    | 7     | SPI_CLK  |
| GND   | 8    | 9     | SPI_MISO |
::

- TFCard

| Atom   | G23 | G33  | G19  |
| ------ | --- | ---- | ---- |
| TFCard | SCK | MISO | MOSI |

- NS4168

| Atom   | G22  | G21   | G25  |
| ------ | ---- | ----- | ---- |
| NS4168 | BLCK | LRCLK | DATA |

## 数据手册

- [NS4168](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/NS4168_CN_datasheet.pdf)

## 软件开发

- [Atom SPK Play RawPCM Example](https://github.com/m5stack/M5Atom/tree/master/examples/ATOM_BASE/ATOM_SPK/PlayRawPCM)
- [Atom SPK Play MP3 From TFCard Example](https://github.com/m5stack/M5Atom/tree/master/examples/ATOM_BASE/ATOM_SPK/PlayMP3FromSD)

> 使用 ATOM SPK 播放 RawPCM 文件或 MP3，适用于主机箱：Atom-Lite。

```cpp
AtomSPK.h - API

//Init I2S  param(__rate: I2S sampling rate)
bool begin(int __rate = 44100);

//Play RawPCM param(___audioPtr: audio data pointer, __size: data length, freeFlag: whether to release the memory, __ticksToWait: allow the maximum duration of blocked playback)
size_t playRAW( const uint8_t* __audioPtr, size_t __size, bool __modal = false, bool freeFlag = true,TickType_t __ticksToWait = portMAX_DELAY );

//play Beep param(__freq: frequency, __timems: play market, __maxval: maximum volume, __modal: asynchronous or not)
size_t playBeep( int __freq = 2000, int __timems = 200, int __maxval = 10000, bool __modal = false );

```

### EasyLoader

| Easyloader          | 下载链接                                                                                                      | 备注 |
| ------------------- | ------------------------------------------------------------------------------------------------------------- | ---- |
| Atom SPK Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/ATOM_BASE/EasyLoader_Atom_SPK.exe) | /    |

## 相关视频

<video id="example_video" controls>
  <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/AtomBase/ATOM_SPK_VIDEO.mp4" type="video/mp4">
</video>
