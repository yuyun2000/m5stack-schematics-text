# LLM‑8850 Card

<span class="product-sku">SKU:AI-001</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1184/AI-001_LLM-8850-main-pictures_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1184/AI-001_LLM-8850-main-pictures_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1184/AI-001_LLM-8850-main-pictures_00.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1184/AI-001_LLM-8850-main-pictures_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1184/AI-001_LLM-8850-main-pictures_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1184/AI-001_LLM-8850-main-pictures_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1184/AI-001_LLM-8850-main-pictures_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1184/AI-001_LLM-8850-main-pictures_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1184/AI-001_LLM-8850-main-pictures_09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1184/AI-001_LLM-8850-main-pictures_10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1184/AI-001_LLM-8850-main-pictures_11.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1184/AI-001_LLM-8850-main-pictures_12.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1184/AI-001_LLM-8850-main-pictures_13.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1184/AI-001-weight.jpg">
</PictureViewer>

## 描述

**LLM‑8850 Card** 是一款面向边缘设备的 **M.2 M-KEY 2242** AI 加速卡，把 42 mm 的袖珍体积与 Axera AX8850 SoC 的 24 TOPS @ INT8 算力结合起来，为 Raspberry Pi 5、RK3588 SBCs、x86 PC 等主机 “一插即强” 地扩展多模态大模型与视频分析能力。卡上配备微型涡轮风扇 + 铝合金 CNC 鳍片的主动散热系统，由板载 EC 根据温度‑电流曲线智能调速，长期满载也能维持低温稳态，避免密闭机壳内的热衰减。

板载 **DCDC + PMIC** 电源链路由 EC 进行实时功耗管理，实现 “按需供电、按需散热”，大幅提升整机稳定性。支持 **AXCL Runtime**，支持 C / Python API 一键部署 YOLO‑v8/11、CLIP、Whisper、Llama3.2、InternVL3 、Qwen3 等主流 CNN、Transformer、LLM 与多模态模型；同时利用 AX8850 的 VPU 硬件管线，提供 H.264/H.265 8K 编解码与同编同解转码加速与缩放 / 裁切，兼顾 AI 与视频流处理。支持 host 使用 ffmpeg 直接调用硬件视频编解码器。

## 教程 & 快速上手

learn>| ![LLM‑8850 Card](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1184/AI-001_LLM-8850-main-pictures_15.webp) | [LLM‑8850 Card](/zh_CN/guide/ai_accelerator/overview) | 本教程介绍 LLM‑8850 Card 的快速上手流程、模型列表以及进阶使用的方法。|

## 产品特性

- 超紧凑形态：NGFF M.2 M-KEY 2242 尺寸，支持 PCIe 2.0 ×2 通道即插即用
- 高算力 NPU：24 TOPS @ INT8，八核 Cortex‑A55 1.7 GHz CPU
- 智能散热 / 供电：板载涡轮风扇 + CNC 铝合金一体化散热器，EC 监控温‑流‑转速闭环
- 高带宽内存：64‑bit LPDDR4x，4266 Mbps 速率，8GB 容量
- 硬件视频引擎：8 K @ 30 fps H.264/H.265 编码，8 K @ 30 fps 解码，支持 16 路 1080P 并行解码
- 安全启动 & 加密：AES / DES / 3DES / SHA‑256 硬件安全模块
- 原生 AXCL：CNN、Transformer、CLIP、Whisper、Llama3.2、Qwen3、InternVL3 等全栈模型一键运行，支持 H.264/H.265 同编同解转码

## 包装内容

- 1 x LLM‑8850 Card

## 应用场景

- 工业 / 商用 SBC 算力升级：Raspberry Pi 5、RK3588、TI AM62x 等板卡本地运行目标检测、缺陷识别
- 具身智能机器人：AMR / AGV / 服务机器人即插即得 “感知‑决策‑控制” 本地链
- AIPC & 边缘智能终端：在迷你 PC 内提供离线 Copilot、客服问答、会议字幕 & 即时翻译
- NVR / NAS 智能化改造：旧存储盒增添多路 AI 车牌抓拍、事件摘要检索 + 硬件转码
- 智能交互设备：语音助手、智能门铃、广告机实现本地 LLM + TTS 的低时延对话
- AI 视觉网关：交通路口、园区闸机前端推理，实时客流统计与危险行为告警

## 规格参数

| 规格                 | 参数                                                                      |
| -------------------- | ------------------------------------------------------------------------- |
| SoC                  | Axera AX8850                                                              |
| CPU                  | 八核 Cortex‑A55 1.7 GHz                                                   |
| NPU                  | 24 TOPS @ INT8                                                            |
| 视频编码器           | 8 K @ 30 fps H.264/H.265 编码，支持缩放 / 裁切                            |
| 视频解码器           | 8 K @ 30 fps H.264/H.265 解码，支持 16 路 1080P 并行解码，支持缩放 / 裁切 |
| 内存                 | 64‑bit LPDDR4x，4266 Mbps，8GB 容量                                       |
| 存储                 | 32Mbits QSPI NOR Flash (仅用于 Bootloader)                                |
| 形态                 | M.2 M-KEY 2242，PCIe 2.0 ×2                                               |
| 散热                 | 微型涡轮风扇 + 铝合金 CNC 一体化散热片，EC 智能温控                       |
| 工作环境温度         | 0 ~ 60 °C                                                                 |
| 室温下的满载工作温度 | 70 °C                                                                     |
| 供电                 | 7W @ 3.3V                                                                 |
| 产品尺寸             | 42.6 x 24.0 x 9.7mm                                                       |
| 产品重量             | 14.7g                                                                     |
| 包装尺寸             | 66.0 x 44.0 x 13.5mm                                                      |
| 毛重                 | 19.8g                                                                     |

## 操作说明

?> 提醒 | 设备工作时会发热，请勿触摸，以免造成烫伤。

?> 供电要求 | 连接树莓派或其他 PC 时，请使用具备 DC 5V@3A 供电能力的开关电源 (非 PD 协议) 适配器；若使用 PD 电源适配器，可能因协议适配问题导致无法正常输出最大功率，进而造成设备工作异常。

?> 设备要求 | 由于树莓派内部中断资源不足，在使用 PCIE 转 4 通道 M.2 下，不支持 M.2 固态硬盘与 LLM-8850 共用。目前已知不支持微雪电子的 PCIe 转双通道 M.2 转接板。

1. 结构要求: PCIe M.2 M-Key
2. 接口要求：支持 PCIe 2.0 ×2 通道，支持向下兼容 x1 (如树莓派 PCIe 2.0 x1 通道)。注：不支持使用 M.2 SSD NVMe 协议的硬盘接口。
3. 硬件要求：搭配树莓派使用的情况下，推荐使用树莓派官方主控和转接板，或 M5Stack 推出转接板。其余厂商硬件可能存在兼容性问题。
4. 系统要求：参考下方系统兼容性表格，其他系统可能无法正常安装驱动。

### 硬件兼容性

以下板卡经官方和第三方用户测试，可正常搭配 LLM‑8850 Card 使用:

| 板卡                 | 是否支持 |
| -------------------- | -------- |
| 树莓派 5             | ✅        |
| Radxa Rock 5B RK3588 | ✅        |

### 系统兼容性

| 操作系统    | 是否支持 |
| ----------- | -------- |
| Ubuntu20.04 | ✅        |
| Ubuntu22.04 | ✅        |
| Ubuntu24.04 | ✅        |
| Debian12    | ✅        |
| Debian13    | ✅        |
| Windows10   | ✅        |
| Windows11   | ✅        |
| macOS       | ❌        |
| WSL         | ❌        |
| VMware      | ❌        |
| VBox        | ❌        |

## 尺寸图

- [LLM‑8850 Card 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1184/AI-001-MODELSIZE-LLM-8850.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1184/AI-001-MODELSIZE-LLM-8850_page_01.png" width="100%">

## 数据手册

- [Axera AX8850 产品简介 ](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1184/AXera-AX8850-product-Brief_V0.3-ZH.pdf)

## 软件开发

### 快速上手

- [LLM‑8850 Card 使用指南](/zh_CN/guide/ai_accelerator/overview)

## 相关视频

- LLM‑8850 Card 产品介绍以及功能展示

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1184/AI-001-LLM8850-video_ZH.mp4" type="video/mp4"></video>
