# LLM630 Compute Kit - IPC 网络摄像头

本案例将演示将 LLM630 Compute Kit 搭配 CamModule SC850SL 实现网络摄像头功能。该案例基于[AXERA FRTDemo](https://github.com/AXERA-TECH/ax620e_bsp_sdk/tree/m5stack/app/demo/FRTDemo)实现，实现了网络摄像头和 AI 识别功能 PANO。

## 1. 准备工作

1. 按照下图接线方式，在设备上电前通过 FPC 排线连接 CamModule SC850SL 摄像头 和 LLM630 Compute Kit

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1152/llm630_compute_kit_cam_sc850sl_01.jpg" width="70%" />

2. 参考[LLM630 Compute Kit UART / ADB / SSH 连接调试](/zh_CN/stackflow/llm630_compute_kit/config)教程，学习如何为 LLM630 Compute Kit 配置网络与文件传输，并获取设备 IP 地址。

3. PC 端打开 PowerShell 或 Termnial， 通过 SSH 方式访问设备（注意替换成设备实际的 IP 地址）。

```shell
ssh root@192.168.20.64
```

4. 访问设备终端后，输入以下指令，开启 IPC 网络摄像头服务。

```shell
/opt/bin/FRTDemo/run.sh -p 0 -s 5 -n 1
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1152/llm630_compute_kit_cam_sc850sl_ipc_01.jpg" width="70%" />

5. LLM630 Compute Kit 默认的内置的 AXERA FRTDemo 使用的为中文页面。 如需更换英文页面，可下载以下软件包，通过 SCP 或者 ADB 等方式传输至设备和运行。

- [FRTDemo EN](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1152/FRTDemo.tar.gz)

```shell
scp .\FRTDemo.tar.gz root@192.168.20.64:/root
ssh root@192.168.20.64
tar -zxf FRTDemo.tar.gz
/root/FRTDemo/run.sh -p 0 -s 5 -n 1
```

## 2. 获取图像

1. 同一局域网下，PC 打开浏览器，访问设备图像 web 服务: `IP:8080`。默认的登录用户名和密码为`admin`，成功登录后即可开始实时预览图像。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1152/llm630_compute_kit_cam_sc850sl_ipc_02.jpg" width="70%" />

2. 当前默认提供两组 RTSP 流，Main Stream 0 (3840 x 2160)，Sub Stream 1 (720 x 576)，可以通过页面左下角进行切换。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1152/llm630_compute_kit_cam_sc850sl_ipc_03.jpg" width="70%" />

3. 同时，该 Demo 提供了**人、非机动车、机动车**的检测，下方记录区域将捕捉识别成功的目标。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1152/llm630_compute_kit_cam_sc850sl_ipc_04.jpg" width="70%" />

4. 点击上方导航栏的配置选项，在相机设置中可以实时调整画面旋转角度，是否开启镜像和翻转。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1152/llm630_compute_kit_cam_sc850sl_ipc_05.jpg" width="70%" />

5. 在视频设置选项中可以实时调整主码流和子码流的启用、编码类型、分辨率等参数。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1152/llm630_compute_kit_cam_sc850sl_ipc_06.jpg" width="70%" />

## 3. 视频流获取

开启 IPC 网络摄像头服务后，可通过以下 RTSP URL，拉取实时视频流。下面演示通过 VLC 和 ffmpeg 两种常用推流拉流工具，获取视频流并进行显示。

- 主码流，分辨率为 **3840 x 2160**

```shell
rtsp://192.168.20.49:8554/axstream0
```

- 子码流，分辨率为 **720 x 576**

```shell
rtsp://192.168.20.49:8554/axstream1
```

### VLC

1. 访问[VLC 官方网站](https://get.videolan.org) 下载软件。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1152/llm630_compute_kit_cam_sc850sl_vlc_01.jpg" width="60%" />

### ffmpeg

1. 访问[ffmpeg 官方网站](https://ffmpeg.org/download.html) 下载软件。

2. 命令行中使用 ffplay 指令拉取 RTSP 视频流。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1152/llm630_compute_kit_cam_sc850sl_ffplay_01.jpg" width="70%" />

### 4. Demo 源代码

- [AXERA FRTDemo 源码](https://github.com/AXERA-TECH/ax620e_bsp_sdk/tree/m5stack/app/demo/FRTDemo)
