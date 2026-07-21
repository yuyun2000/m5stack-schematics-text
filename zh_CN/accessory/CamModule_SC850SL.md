# CamModule SC850SL

<span class="product-sku">SKU:A157</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1152/A157-01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1152/A157-02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1152/A157-03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1152/A157-04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1152/A157-05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1152/A157-06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1152/A157-07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1152/A157-08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1152/A157-09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1152/A157-10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1152/A157-11.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1152/A157-12.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1152/A157-weight.jpg">

</PictureViewer>

## 描述

**CamModule SC850SL** 是一款专为 LLM630 Compute Kit 定制的高性能摄像头模组，集成 SmartSens SC850SL 8 MP 传感器，支持 4K 视频采集、宽动态范围 (HDR) 与弱光高灵敏度，实现复杂光照环境下的稳定成像，兼具低读取噪声、高信噪比与低功耗优势。配备 200 mm FPC 灵活布线，可通过 MIPI CSI-2 高速传输图像至 LLM630 进行实时 AI 推理与智能分析（如目标检测、图像分类与视觉导航）。适用于智能监控、机器人视觉、无人机巡检和智慧城市等 AI 视觉场景。

## 产品特性

- 适配 LLM630 Compute Kit
- SmartSens SC850SL CMOS 传感器
- YT10151-8MP-4mm 镜头
- Stack BSI + Rolling Shutter 架构
- MIPI 通信接口
- 4K 视频采集
- 高信噪比和动态范围
- 高速 DPC 功能
- 极佳夜视性能
- 高灵敏度 & 快速坏点校正

## 包装内容

- 1 x CamModule SC850SL
- 1 x 200 mm FPC 排线
- 1 x 散热垫

## 应用场景

- 智能监控
- 机器人视觉
- 无人机巡检
- 智慧城市

## 规格参数

| 规格              | 参数                                   |
| ----------------- | -------------------------------------- |
| 图像传感器        | SmartSens SC850SL CMOS                 |
| 分辨率            | 8 MP                                   |
| 像素阵列          | 3856H × 2176V                          |
| 像素尺寸          | 2.0 µm × 2.0 µm                        |
| 光学规格          | 1/1.8″                                 |
| 最大帧率          | 3840 × 2160 @ 60 fps                   |
| 输出接口          | MIPI CS1-2 (4 Lanes)                   |
| 图像格式          | RAW RGB                                |
| 对角视场角 (DFoV) | 110.8°                                 |
| 光敏度            | 5034 mV/（Lux・s）                     |
| 动态范围          | HDR 模式最高可达 100dB；线性模式 75 dB |
| 信噪比（SNR）     | 39 dB                                  |
| 工作温度          | –30 °C ~ +85 °C                        |
| 最佳图像质量温度  | –20 °C ~ +60 °C                        |
| 镜头规格          | M16                                    |
| 接口方式          | 200mm FPC Cable                        |
| 产品尺寸          | 28.0 x 23.5 x 33.9mm                   |
| 产品重量          | 单摄像头：13.0g                        |
| 包装尺寸          | 80.0 x 52.0 x 22.0mm                   |
| 毛重              | 27.3g                                  |

## 操作说明

### 安装方向

\#> 说明 | 摄像头上印有人形图标，用以标示摄像头的安装方向，请按照图示位置正确安装摄像头。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1152/A157-operation.jpg" width="70%">

### 成像优化

\#> AI-ISP | CamModule SC850SL 结合 LLM630 Compute Kit 的 AI-ISP 图像处理技术，能够大幅度优化暗光条件的成像表现。AI-ISP 默认打开，将会使用一半的 NPU 算力。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1152/cam_module_sc850sl_ai_isp_01.png" width="70%">

## 原理图

[CamModule SC850SL 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1152/K157-CamModule-SC850SL.pdf)

<SchViewer>
<img alt="schematics" src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1152/K157-CamModule-SC850SL_page_01.png" width="100%" />
</SchViewer>

## 管脚映射

### CamModule SC850SL

| Pin Number | CamModule SC850SL |
| ---------- | ----------------- |
| 1-5        | NC                |
| 6          | GND               |
| 7          | DVDD_1V2          |
| 8          | DOVDD_1V8         |
| 9          | AVDD_2V8          |
| 10         | GND               |
| 11         | CAM_SDA_1V8       |
| 12         | CAM_SCL_1V8       |
| 13         | CAM_RSTN          |
| 14         | CAM_MCLK          |
| 15         | GND               |
| 16         | MIPI_RX0_N        |
| 17         | MIPI_RX0_P        |
| 18         | GND               |
| 19         | MIPI_RX1_N        |
| 20         | MIPI_RX1_P        |
| 21         | GND               |
| 22         | MIPI_RX2_N        |
| 23         | MIPI_RX2_P        |
| 24         | GND               |
| 25         | MIPI_RX3_N        |
| 26         | MIPI_RX3_P        |
| 27         | GND               |
| 28         | MIPI_RX4_N        |
| 29         | MIPI_RX4_P        |
| 30         | GND               |

## 尺寸图

[CamModule SC850SL 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1152/A157-CamModule-SC850SL.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1152/A157-CamModule-SC850SL_page_01.png" width="100%">

## 软件开发

### 快速上手

- [LLM630 Compute Kit - IPC 网络摄像头](/zh_CN/stackflow/llm630_compute_kit/ipc_demo)
- [LLM630 Compute Kit - StackFlow API Camera Demo](/zh_CN/stackflow/llm630_compute_kit/stackflow_camera_demo)
- [LLM630 Compute Kit - StackFlow API DepthAnything](/zh_CN/stackflow/llm630_compute_kit/stackflow_camera_depth_anything_visual_demo)
- [LLM630 Compute Kit - StackFlow API Yolo11n Demo](/zh_CN/stackflow/llm630_compute_kit/stackflow_camera_yolo_demo)
- [LLM630 Compute Kit - StackFlow API Yolo11n Visual Demo](/zh_CN/stackflow/llm630_compute_kit/stackflow_camera_yolo_visual_demo)

## 相关视频

CamModule SC850SL 产品介绍以及案例展示

<video class="video-container" controls><source src="
https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1152/A157-CamModule-SC850SL_video.mp4" type="video/mp4"></video>
