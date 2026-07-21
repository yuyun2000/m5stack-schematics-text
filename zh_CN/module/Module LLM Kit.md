# Module LLM Kit

<span class="product-sku">SKU:K144</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1131/K144_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1131/K144_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1131/K144_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1131/K144_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1131/K144_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1131/K144_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1131/K144_09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1131/K144_10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1131/K144_11.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1131/K144_12.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1131/K144_13.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1131/K144_14.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1131/K144_15.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1131/K144_16.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1131/K144_17.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1131/K144_Weight.jpg">
</PictureViewer>

## 描述

**Module LLM Kit**是一款专注于离线 AI 推理与数据通信接口应用的智能模块套件，整合了 Module LLM 与 Module13.2 LLM Mate 模块，满足多场景下的离线 AI 推理与数据交互需求。

**Module LLM** 是一款集成化的离线大语言模型 (LLM) 推理模块，专为需要高效、智能交互的终端设备设计。无论是在智能家居、语音助手，还是在工业控制中，Module LLM 都能为您带来流畅、自然的 AI 体验，无需依赖云端，确保隐私安全与稳定性。

**Module13.2 LLM Mate 模块**提供多种接口功能，便于系统集成和扩展。通过 M5-Bus 接口实现与 Module LLM 的堆叠供电；其内置 CH340N USB 转换芯片提供 USB 到串口的调试功能，而 Type-C 接口用于 USB Log 输出；同时，RJ45 接口与板载网络变压器协同工作，可扩展出百兆以太网口及内核串口（支持 SBC 应用）；另外，FPC-8P 接口直接对接 Module LLM，实现稳定的串口通信；此外，还预留了 HT3.96\*9P 焊盘，方便用户进行 DIY 扩展。

**Module LLM**模块集成 StackFlow 框架，配合 Arduino/UiFlow 库，几行代码就可轻松实现端侧智能。搭载爱芯 AX630C SoC 处理器，集成 3.2TOPs 高能效 NPU，原生支持 Transformer 模型，轻松应对复杂 AI 任务。配备 4GB LPDDR4 内存（其中 1GB 供用户使用，3GB 专用于硬件加速）和 32GB eMMC 存储，支持多模型并行加载与串联推理，确保多任务处理流畅无阻。运行功耗仅约 1.5W，远低于同类产品，节能高效，适合长时间运行。

**Module LLM**多模型兼容，出厂预装 **Qwen2.5-0.5B** 大语言模型，内置 **KWS**（唤醒词），**ASR**（语音识别），**LLM**（大语言模型）及 **TTS**（文本生成语音）功能，且支持 apt 快速更新软件和模型包。安装 openai-api 插件后，即可兼容 OpenAI 标准 API，支持聊天，对话补全，语音转文字和文字转语音等多种应用模式。官方 apt 仓库提供丰富的大模型资源，包括 deepseek-r1-distill-qwen-1.5b，InternVL2_5-1B-MPO，Llama-3.2-1B，Qwen2.5-0.5B 以及 Qwen2.5-1.5B，同时还涵盖文本转语音模型（melotts）与语音转文本模型（whisper-tiny，whisper-base）和视觉模型（如 yolo11 等 SOTA 模型）。仓库将持续更新，以支持最前沿的模型应用，满足各种复杂 AI 任务。

**Module LLM Kit** 即插即用，搭配 M5 主机，实现即插即用的 AI 交互体验。用户无需繁琐设置，即可将其集成到现有智能设备中，快速启用智能化功能，提升设备智能水平。该产品适用于离线语音助手，文本语音转换，智能家居控制，互动机器人等领域。

## 教程 & 快速上手

learn>| ![Arduino IDE](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/arduino_banner_01.png) | [Arduino IDE](/zh_CN/stackflow/module_llm/arduino) | 本教程将向你介绍，如何通过 Arduino IDE 编程控制 Module LLM 设备，需搭配 M5Core 系列主机使用 |

learn>| ![UiFlow2](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/uiflow2.0_banner_01.png) | [UiFlow2](/zh_CN/stackflow/module_llm/uiflow2) | 本教程将向你介绍，如何通过 UiFlow2 图形化编程平台控制 Module LLM 设备 |

## 产品特性

- 离线推理，3.2T@INT8 精度算力
- 集成 KWS (唤醒词)，ASR (语音识别)，LLM (大语言模型)，TTS (文本生成语音)
- 多模型并行
- 板载 32GB eMMC 存储和 4GB LPDDR4 内存
- 板载麦克风及扬声器
- 串口通信
- SD 卡固件升级
- 支持 ADB 调试
- RGB 提示灯
- 内置 ubuntu 系统
- 支持 OTG 功能
- 开发平台
  - UiFlow1
  - UiFlow2
  - Arduino IDE

## 包装内容

- 1 x Module LLM
- 1 x Module LLM Mate
- 2 x FPC-8P 通讯线

## 应用场景

- 离线语音助手
- 文本语音转换
- 智能家居控制
- 互动机器人

## 规格参数

| 规格         | 参数                                                                                 |
| ------------ | ------------------------------------------------------------------------------------ |
| 处理器 SoC   | AX630C@Dual Cortex A53 1.2 GHz <br/> MAX.12.8 TOPS @INT4, 3.2 TOPS @INT8             |
| 内存         | 4GB LPDDR4 (1GB 系统内存 + 3GB 硬件加速专用内存)                                     |
| 存储         | 32GB eMMC5.1                                                                         |
| 通信         | 串口通信，默认波特率 115200@8N1（可调）                                              |
| 麦克风       | MSM421A                                                                              |
| 音频驱动     | AW8737                                                                               |
| 扬声器       | 8Ω@1W，尺寸: 2014 腔体喇叭                                                           |
| 内置功能单元 | KWS（唤醒词），ASR（语音识别），LLM（大语言模型），TTS（文本生成语音）               |
| RGB 灯       | 3x RGB LED@2020，由 LP5562 驱动（状态指示）                                          |
| 功耗         | 空载：5V@0.5W，满载：5V@1.5W                                                         |
| 按键         | 用于升级固件进入下载模式                                                             |
| 升级接口     | SD 卡 / Type C 口                                                                    |
| 转换芯片     | CH340N                                                                               |
| 以太网接口   | RJ45 接口搭配板载网络变压器（11FB-05NL SOP-16）                                      |
| 串口接口     | FPC-8P 接口，Type-C 接口，RJ45 接口                                                  |
| DIY 扩展接口 | HT3.96\*9P 焊盘                                                                      |
| 工作温度     | 0-40°C                                                                               |
| 产品尺寸     | Module LLM : 54.0 x 54.0 x 13.0mm <br/> Module13.2 LLM Mate : 54 x 54 x 19.7mm       |
| 包装尺寸     | Module LLM : 192.0 x 95.0 x 17.0mm <br/> Module13.2 LLM Mate : 192.0 x 95.0 x 21.0mm |
| 产品重量     | Module LLM + Module13.2 LLM Mate : 36.7g                                             |
| 毛重         | Module LLM : 32.0g <br/> Module13.2 LLM Mate : 34.8g                                 |

## 操作说明

### Module LLM 与 Module13.2 LLM Mate 的连接步骤与接口展示

#>注意|连接排线前，请先掀开接口卡扣；排线插接到位后，再扣合卡扣完成固定。<br>连接 Module LLM 排线前建议拆除设备外框；其排线接口在 SPK 模块下方，操作前需先拆卸 SPK 模块。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1131/module_llm_mate_connect_01.jpg" width="100%" />
<img alt="module size" src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1131/module_llm_mate_connect_02.png" width="50%" />

## 原理图

- [Module LLM 原理图下载](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Module%20LLM/Sch_M5_Module-LLM.pdf)
- [Module13.2 LLM Mate 原理图下载](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1131/K144_Sch_Module13.2_LLM_MATE.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/992/M140_Sch_M5_Module-LLM_page_02.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/992/M140_Sch_M5_Module-LLM_page_03.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/992/M140_Sch_M5_Module-LLM_page_04.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/992/M140_Sch_M5_Module-LLM_page_05.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/992/M140_Sch_M5_Module-LLM_page_06.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/992/M140_Sch_M5_Module-LLM_page_07.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/992/M140_Sch_M5_Module-LLM_page_08.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/992/M140_Sch_M5_Module-LLM_page_09.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/992/M140_Sch_M5_Module-LLM_page_10.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1131/K144_Sch_Module13.2_LLM_MATE_page_01.png">
</SchViewer>

## 管脚映射

\#>Module LLM 引脚切换 | Module LLM 预留了引脚切换焊盘，一些出现引脚复用冲突的情况下，可以通过切割 PCB 线路然后跳线连接至其他组引脚，参考[教程](/zh_CN/guide/llm/llm/pins_change)。

<img alt="module size" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Module%20LLM/03.jpg" width="50%" />

### M5-Bus

- Module LLM

\#> Net-Tie | 下方 M5-Bus 中标记 `NT` 的引脚，可通过上述操作进行切换，用于适配不同的主控设备。

::m5-bus-table
| PIN         | LEFT | RIGHT | PIN         |
| ----------- | ---- | ----- | --------    |
| GND         | 1    | 2     | TRM_TXD(NT) |
| GND         | 3    | 4     |             |
| GND         | 5    | 6     | RST         |
|             | 7    | 8     |             |
|             | 9    | 10    |             |
|             | 11   | 12    | 3V3         |
|             | 13   | 14    |             |
| TRM_TXD(NT) | 15   | 16    | TRM_RXD(NT) |
| SoC_SCL     | 17   | 18    | SoC_SDA     |
|             | 19   | 20    |             |
| TRM_RXD(NT) | 21   | 22    | TRM_TXD(NT) |
| TRM_RXD(NT) | 23   | 24    | TRM_RXD(NT) |
|             | 25   | 26    | TRM_TXD(NT) |
|             | 27   | 28    | 5V          |
|             | 29   | 30    |             |
::

- Module LLM Mate

::m5-bus-table
| PIN     | LEFT | RIGHT | PIN     |
| ------- | ---- | ----- | ------- |
| GND     | 1    | 2     |         |
| GND     | 3    | 4     |         |
| GND     | 5    | 6     |         |
|         | 7    | 8     |         |
|         | 9    | 10    |         |
|         | 11   | 12    |         |
|         | 13   | 14    |         |
|         | 15   | 16    |         |
| SCL     | 17   | 18    | SDA     |
|         | 19   | 20    |         |
|         | 21   | 22    |         |
|         | 23   | 24    |         |
| HPWR    | 25   | 26    |         |
| HPWR    | 27   | 28    | 5V      |
| HPWR    | 29   | 30    | BAT     |
::

## 尺寸图

<SchViewer>
<img alt="module size" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Module%20LLM/%E5%B0%BA%E5%AF%B8%E5%9B%BE.jpg" width="100%" />
<img alt="module size" src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1131/K144_Module13.2_LLM_Mate_page_01.png" width="100%" />
</SchViewer>

## 数据手册

- [AX630C](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/992/AX630C.pdf)

## 软件开发

### 快速上手

- [Module LLM ADB / UART / SSH 连接调试](/zh_CN/stackflow/module_llm/config)

- [Module LLM 软件包应用更新](/zh_CN/stackflow/module_llm/software)

- [Module LLM 镜像底包更新](/zh_CN/stackflow/module_llm/image)

- Module LLM 工作状态指示灯:

  - 红色：设备正在初始化
  - 绿色：设备初始化完成

- Module LLM 应用升级状态指示灯:
  - 蓝灯闪烁：应用包更新中
  - 红色：应用包升级失败
  - 绿色：应用包升级成功

?>Module LLM 模型替换注意事项 | LLM Module 支持的模型为爱芯特有格式，需经过特殊处理才可正常使用。因此并不能直接使用市面现有模型。

### Arduino

- [Module LLM Arduino 快速上手](/zh_CN/stackflow/module_llm/arduino)
- [Module LLM Arduino 驱动库](https://github.com/m5stack/M5Module-LLM)
- [Module LLM Arduino API](/zh_CN/stackflow/module_llm/arduino_api)

### UiFlow2

- [Module LLM UiFlow2 快速上手](/zh_CN/guide/llm/llm/uiflow2)
- [Module LLM UiFlow2 API](https://uiflow-micropython.readthedocs.io/zh-cn/latest/module/llm.html)

### OpenAI API

- [Module LLM Kit OpenAI API 使用指南](/zh_CN/stackflow/openai_api/intro)

### 开发框架

- [StackFlow](https://github.com/m5stack/StackFlow.git)

### 开发资料

- [AX630C Databrief](https://en.axera-tech.com/Product/126.html)
- [Module LLM JSON API Documentation](https://github.com/m5stack/StackFlow/tree/main/doc)
- [Module LLM AX630C API Docs](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/llm/M5_LLM_AXERA_DOC_RELEASE.zip)
- [Module LLM AX620E MSP/Sample](https://github.com/AXERA-TECH/ax620e_bsp_sdk.git)
- [Module LLM Linux Kernel 4.19.125-head](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/llm/linux-4.19.125-head.tar.gz)
- [AXERA LLM Example](https://github.com/AXERA-TECH/ax-llm)
- [AXERA CV Example](https://github.com/AXERA-TECH/ax-samples)
- [Module LLM Large Model Compilation Guide](https://pulsar2-docs.readthedocs.io/zh-cn/latest/appendix/build_llm.html)

## 相关视频

- Module LLM 产品介绍以及例子展示

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Module%20LLM/Module_LLM_Video.mp4" type="video/mp4"></video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113461845560481&bvid=BV1dhmyYjEfZ&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/s4E1ua7V9GM?si=AcHq9I5ttKktMklr" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>

## 产品对比

### AI Benchmark 对比

<img alt="compare" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Module%20LLM/Benchmark对比.png" width="100%" />
