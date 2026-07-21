# Unit ASR

<span class="product-sku">SKU:U194</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/635/U914_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/635/U194_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/635/U194_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/635/U914_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/635/U914_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/635/U914_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/635/U914_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/635/U914_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/635/U194-weight.jpg">
</PictureViewer>

## 描述

**Unit ASR** 是一款 **AI** 离线语音识别单元，内置 **CI-03T** AI 智能离线语音模块。该单元具备强大的语音识别、声纹识别、语音增强和语音检测等功能。支持 AEC（回声消除）功能，有效去除回声和噪声干扰，提升语音识别准确性。同时支持中途语音打断功能，允许在语音识别过程中灵活打断并快速响应新的指令。产品出厂时已预设了 42 条英文唤醒词和反馈命令词，该设备采用 **UART** 串口通信进行数据传输，同时支持通过 UART 或语音关键词唤醒设备。该单元支持用户自定义修改多语言**唤醒**识别词，用户可以通过重新生成固件来修改唤醒词，最多支持 300 条命令词的识别。配备**麦克风**用于清晰音频采集，并内置**扬声器**提供高质量的音频反馈。该产品适用于 AI 助手、智能家居、安防监控、车载系统、机器人与智能硬件、医疗健康等领域，是实现智能语音交互的理想选择。

## 产品特性

- CI-03T AI 智能离线语音模块
- 降噪处理
- 出厂内置 42 条命令
- 支持最多 300 条命令词
- UART 串口通信方式
- 支持用户自定义唤醒词
- 麦克风与扬声器
- 开发平台
  - UiFlow1
  - UiFlow2
  - Arduino IDE

## 包装内容

- 1 x Unit ASR
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- AI 助手
- 智能家居
- 安防监控
- 车载系统
- 机器人与智能硬件
- 医疗健康

## 规格参数

| 规格       | 参数                                                       |
| ---------- | ---------------------------------------------------------- |
| AI 模块    | CI-03T AI 智能离线语音模块                                 |
| 命令词数量 | 支持最多 300 条命令词，出厂预设 42 条内置命令              |
| 唤醒方式   | UART 串口通信或语音关键词唤醒设备                          |
| 麦克风     | 模拟麦克风                                                 |
| 扬声器     | 腔体喇叭 8Ω@0.8W (用于输出设备唤醒反馈)                    |
| 通信方式   | UART 串口通信 波特率默认: 115200@8N1                       |
| 降噪功能   | AEC 回声消除降噪                                           |
| 功耗       | 待机电流: DC 5V / 47.73mA <br/> 工作电流: DC 5V / 250.12mA |
| 工作温度   | 0 ~ 40°C                                                   |
| 产品尺寸   | 48.0 x 24.0 x 16.0mm                                       |
| 产品重量   | 10.6g                                                      |
| 包装尺寸   | 138.0 x 93.0 x 17.0mm                                      |
| 毛重       | 16.0g                                                      |

## 原理图

- [Unit ASR 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/635/SCH_UNIT_ASR_V1.0.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/635/SCH_UNIT_ASR_V1.0_sch_01.png">
</SchViewer>

## 管脚映射

### Unit ASR

::grove-table
| HY2.0-4P | Black | Red | Yellow  | White   |
| -------- | ----- | --- | ------- | ------- |
| PORT.C   | GND   | 5V  | UART_RX | UART_TX |
::

## 尺寸图

- [Unit ASR 尺寸图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/635/U194_Unit_ASR_Model_Size.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/635/U194_Unit_ASR_Model_Size_sch_01.png" width="100%">

## 结构文件

- [Unit ASR 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/U194_Unit_ASR/Structures)

## 数据手册

- [CI-03T AI 模组规格手册](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/635/CI-03T1-V1.3-20230202-001Module_specification.pdf)
- [CI-03T AI 模组数据手册](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/635/CI1301_datasheet_V1.2_chs_20220913.pdf)
- [CI-03T AI 模组开发教程](https://help.aimachip.com/docs/offline_ci03t)

## 软件开发

### 快速上手

- [Unit ASR 自定义固件生成与烧录](/zh_CN/guide/offline_voice/unit_asr/firmware)

### Arduino

- [Unit ASR Arduino 使用教程](/zh_CN/arduino/projects/unit/unit_asr)
- [Unit ASR Arduino 驱动库](https://github.com/m5stack/M5Unit-ASR)

### UiFlow1

- [Unit ASR UiFlow1 文档](/zh_CN/uiflow/blockly/unit/asr)

### UiFlow2

- [Unit ASR UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/asr.html)

### 通信协议

- [Unit ASR出厂预设命令](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/635/UNIT-ASR-Command_CN.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/635/UNIT-ASR-Command_CN.png" width="50%">

### 内置固件

- [Unit ASR 内置固件](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/635/Unit_ASR_ci_03t_firmware.bin)

### 其他

- [CI-03T 串口烧录工具](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/635/CI-03T_Serial_burning_software_V3.7.3.zip)

## 相关视频

- Unit ASR 产品介绍和案例展示

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/635/U194_Unit_ASR_Video.mp4" type="video/mp4"></video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=114001753149264&bvid=BV1gWKKeVE9i&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" autoplay="0" ></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/UcpGtKouX2I?si=WxOBvqBqUQm1gq4d" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
