# LLM630 Compute Kit - ISP Tuning 成像调优

本教程介绍 LLM630 Compute Kit 如何连接 CamModule SC850SL , 并借助 ISP Tuning 软件实现摄像头成像质量调优。

## 1. 准备工作

1. 按照下图接线方式，在设备上电前通过 FPC 排线连接 CamModule SC850SL 摄像头 和 LLM630 Compute Kit。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1152/llm630_compute_kit_cam_sc850sl_01.jpg" width="70%" />

2. 参考[LLM630 Compute Kit UART / ADB / SSH 连接调试](/zh_CN/stackflow/llm630_compute_kit/config)教程，学习如何为 LLM630 Compute Kit 配置网络与文件传输，并获取设备 IP 地址。

## 2 软件

### 2.1 工具概述

\#> 工具概述 | ISP Tuning 是专门用于摄像头图像质量效果调优的工具，由离线校准，在线参数调试，实时预览，图片质量分析等部分组成。

- 离线校准：自动生成各个支持 ISP 模块的算法参数。
- 在线参数调试：各参数精细化，差异化的调节，可以通过预览窗口实时观察调试效果。
- 实时预览：图像效果的实时观察窗口，有效地辅助在线调试。
- 图片质量分析等工具：辅助调试工具，提供一系列的图片分析调试手段。

### 2.2 准备环境

目前软件仅支持 Win10/11 操作系统，点击下方链接下载，ISPTuning 工具发布包并解压文件.

- [ISPTuning v8.1 Win10/11 64-bit](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1152/ISPTuning_V1.24.14.1_PH02.7z)

解压后包含以下文件：

- bin/lib：工具执行的依赖文件。
- cfg：工具执行的配置文件。
- wsp：一些 Sample 的图片和参数文件。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1152/llm630_compute_kit_cam_sc850sl_ISPTuning_02.png" width="70%" />

### 2.3 工具界面

打开 **ISPTuning.exe** 工具

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1152/llm630_compute_kit_cam_sc850sl_ISPTuning_01.png" width="70%" />

- 1：标题栏：主要显示工具的版本信息。
- 2：菜单栏：提供一些高级的操作。
- 3：工具栏：提供一些常用的操作。
- 4：模块面版区域：显示当前可调试的模块。
- 5：参数调试区域：显示当前模块下可调节的参数，并提供调节手段。

### 2.4 快速启动

1. 登录访问 LLM630 Compute Kit 的终端，输入以下命令开启 tuning-server。后续的操作中 ISP Tuning 将通过连接开发板的 tuning-server 进行调试。

?> 注意事项 | 使用 ISP Tuning 软件连接 tuning-serve 进行调试要求，开发板与 PC 处于同一局域网内，确保能够互相通信。

```bash
tuning-server -p  /opt/etc/sc850sl_single_sdr_4lane_entry.ini
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1152/llm630_compute_kit_cam_sc850sl_ISPTuning_03.png" width="70%" />

2. 等待下方显示监听端口。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1152/llm630_compute_kit_cam_sc850sl_ISPTuning_04.png" width="70%" />

3. 点击工具栏图标，Chip 下拉选择 **AX620E**，Channel 下拉选择 **tcp**，Server 填写板子的 IP 地址，端口保持默认。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1152/llm630_compute_kit_cam_sc850sl_ISPTuning_05.png" width="70%" />

1. 连接上服务器后，点击 Start `Preview` 打开预览窗口。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1152/llm630_compute_kit_cam_sc850sl_ISPTuning_06.png" width="70%" />

5. 格式选择 **VENC_H264:3840x2160, 0**

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1152/llm630_compute_kit_cam_sc850sl_ISPTuning_07.png" width="70%" />

6. 即可实时预览摄像头画面。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1152/llm630_compute_kit_cam_sc850sl_ISPTuning_08.png" width="70%" />

7. 有关摄像头参数调优与软件操作，请参考下方提供的 AXERA 官方文档。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1152/llm630_compute_kit_cam_sc850sl_ISPTuning_09.png" width="70%" />

## 3 相关文档

- [AX IQ Tool User Manual](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1152/01%20-%20AXIQ%20Tool%20User%20Manual.pdf)
- [AX Image Online Tuning Guide](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1152/03%20-%20AX%20Image%20Online%20Tuning%20Guide.pdf)
- [AX Image Calibration and Tuning Cuide](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1152/04%20-%20AX%20Image%20Calibration%20and%20Tuning%20Guide.pdf)
