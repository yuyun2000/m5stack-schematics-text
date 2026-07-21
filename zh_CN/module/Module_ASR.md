# Module ASR

<span class="product-sku">SKU:M147</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1190/M147-Module-ASR-main-pictures_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1190/M147-Module-ASR-main-pictures_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1190/M147-Module-ASR-main-pictures_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1190/M147-Module-ASR-main-pictures_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1190/M147-Module-ASR-main-pictures_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1190/M147-Module-ASR-main-pictures_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1190/M147-Module-ASR-main-pictures_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1190/M147-Module-ASR-main-pictures_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1190/M147-Module-ASR-main-pictures_09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1190/M147-Module-ASR-main-pictures_10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1190/M147-Module-ASR-main-pictures_11.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1190/M147-Module-ASR-main-pictures_12.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1190/M147-weight.jpg">
</PictureViewer>

## 描述

**Module ASR** 是一款基于 CI1302 芯片设计的 AI 智能离线语音模块。配备麦克风用于清晰音频采集，并内置扬声器提供高质量的音频反馈。同时支持中途语音打断功能，允许在语音识别过程中灵活打断并快速响应新的指令。内置 AEC（回声消除），有效去除回声和噪声干扰，提升语音识别准确性。产品出厂时预设了 53 条英文唤醒词和反馈命令词，支持通过 UART 指令或语音关键词唤醒设备。同时支持用户自定义**中英日韩**识别词，用户可以通过重新生成固件来修改唤醒词，最多支持 300 条命令词的识别。设备采用 UART 通信接口进行数据传输，支持通过拨码开关切换选择不同串口引脚 。该产品适用于 AI 助手、智能家居、安防监控、车载系统、机器人与智能硬件、医疗健康等领域，是实现智能语音交互的理想选择。

## 产品特性

- 智能离线语音模块
- AEC 降噪处理
- 出厂内置 53 条英语命令，最多支持 300 条命令词
- UART 通信接口
- 支持用户自定义唤醒词
- 可通过预留的 USB Type-C 接口烧录固件
- 配备麦克风，内置扬声器
- 开发平台
  - UiFlow2
  - Arduino

## 包装内容

- 1 x Module ASR

## 应用场景

- AI 助手
- 智能家居
- 安防监控
- 车载系统
- 机器人与智能硬件
- 医疗健康

## 规格参数

| 规格        | 参数                                                                                                                                |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| AI 语音芯片 | CI1302                                                                                                                              |
| 命令词数量  | 支持最多 300 条命令词，出厂预设 53 条命令                                                                                           |
| 唤醒方式    | 语音关键词或 UART 串口通信唤醒设备                                                                                                  |
| 麦克风      | 模拟麦克风，型号 GMI4527P-2C-32db                                                                                                   |
| 扬声器      | 腔体喇叭 8Ω@0.8W (用于输出设备唤醒反馈)                                                                                             |
| 通信方式    | UART 串口通信 波特率默认: 115200@8N1                                                                                                |
| 降噪功能    | AEC 回声消除降噪                                                                                                                    |
| 唤醒距离    | 环境噪音 40dB 时，唤醒距离可达 6.4 米 <br>环境噪音 54dB 时 唤醒距离可达 1.8 米                                                      |
| 功耗        | 待机状态: DC 5V@52.14mA <br> 工作状态：<br>小音量档位：DC 5V@43.38mA <br> 中音量档位：DC 5V@85.26mA <br> 大音量档位：DC 5V@161.34mA |
| 产品尺寸    | 54.0 x 54.0 x 13.1mm                                                                                                                |
| 产品重量    | 15.2g                                                                                                                               |
| 包装尺寸    | 132.0 x 95.0 x 13.1mm                                                                                                               |
| 毛重        | 28.9g                                                                                                                               |

## 操作说明

\#>USB Type-C 接口 | Module ASR 上的 USB Type-C 接口仅用于程序下载， 无法为 M5-Bus 提供 5V 供电。

## 原理图

- [Module ASR 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1190/SCH_Module_ASR_SCH_Main_V0.4_20250710_2025_07_10_10_30_34.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1190/SCH_Module_ASR_SCH_Main_V0.4_20250710_2025_07_10_10_30_34_page_01.png">
</SchViewer>

## 管脚映射

### M5-Bus

\#> DIP Switch | 下方 M5-Bus 中标记 `SW` 的引脚，可通过拨码开关进行切换，用于适配不同的主控设备。

::m5-bus-table
| PIN          | LEFT | RIGHT | PIN          |
| ------------ | ---- | ----- | ------------ |
| GND          | 1    | 2     |              |
| GND          | 3    | 4     |              |
| GND          | 5    | 6     |              |
|              | 7    | 8     |              |
|              | 9    | 10    |              |
|              | 11   | 12    | 3V3          |
| UART_RX (SW) | 13   | 14    | UART_TX (SW) |
| UART_RX (SW) | 15   | 16    | UART_TX (SW) |
|              | 17   | 18    |              |
|              | 19   | 20    |              |
| UART_TX (SW) | 21   | 22    | UART_RX (SW) |
| UART_TX (SW) | 23   | 24    |              |
| HPWR         | 25   | 26    | UART_RX (SW) |
| HPWR         | 27   | 28    | 5V           |
| HPWR         | 29   | 30    |              |
::

## 尺寸图

- [Module ASR 尺寸图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1190/M147-moudle-asr-00-01.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1190/M147-moudle-asr-00-01_page_01.png" width="100%">

## 数据手册

- [CI1302 数据手册](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/635/CI1301_datasheet_V1.2_chs_20220913.pdf)

## 软件开发

### 快速上手

- [Module ASR 自定义固件生成与烧录](/zh_CN/guide/offline_voice/module_asr/firmware)

### Arduino

- [Module ASR Arduino 使用教程](/zh_CN/arduino/projects/module/module_asr)
- [Module ASR Arduino 驱动库](https://github.com/m5stack/M5Unit-ASR)

### UiFlow2

- [Module ASR UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/module/asr.html)

### 通信协议

- [Module ASR 出厂预设命令](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1190/Module_ASR_Command.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1190/Module_ASR_Command_page_01.png" width="75%">

### 内置固件

- [Module ASR 内置固件](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1190/M147-Module-ASR-CI03T-Tinyu-V2.bin)

### 其他

- [固件烧录工具](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/635/CI-03T_Serial_burning_software_V3.7.3.zip)

## 相关视频

- Module ASR 产品介绍以及功能展示

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1190/M147-Module-ASR-video-ZH.mp4" type="video/mp4"></video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=115687074826397&bvid=BV1i32mBVEus&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/nStWxqSkgq0?si=xi-7D3Ul4Ekg8PeN" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
