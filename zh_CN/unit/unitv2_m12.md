# UnitV2-M12

<span class="product-sku">SKU:U078-M12</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/unitv2_m12/unitv2_m12_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/unitv2_m12/unitv2_m12_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1052/U078-M12-package-zheng.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1052/U078-M12-package-fan.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/unitv2_m12/unitv2_m12_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/unitv2_m12/unitv2_m12_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/unitv2_m12/unitv2_m12_06.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/unitv2_m12/unitv2_m12_07.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/unitv2_m12/unitv2_m12_08.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/unitv2_m12/unitv2_m12_09.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/unitv2_m12/unitv2_m12_10.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/unitv2_m12/unitv2_m12_12.webp">
</PictureViewer>

## 描述

**UnitV2-M12** 是 M5Stack 推出的一款高效率的 AI 识别模块，采用 SigmaStar SSD202D (集成 **双核 Cortex-A7 1.2GHz 处理器** ) 控制核心，集成 **128MB-DDR3 内存**，**512MB NAND Flash**，1080P 摄像头。配备 **1x 常规焦段 (FOV:85°)** + **1x 广角鱼眼镜头 (FOV:150°)** 两个 M12 通用规格镜头，支持手动调焦。内嵌 Linux 操作系统，集成丰富的软硬件资源与开发工具，致力带给用户开箱即用，简洁高效的 Ai 开发体验。

## 产品特性

- SigmaStar SSD202D
- 双核 Cortex-A7 1.2GHz 处理器
- 128MB DDR3
- 512MB NAND Flash
- GC2053 1080P Colored Sensor
- 配备双镜头：常规焦段 (FOV:85°) + 广角鱼眼镜头 (FOV:150°)
- 内置麦克风
- Wi-Fi 2.4GHz
- 开发方式:
  - 随机自带 12 种常用 AI 图像功能：二维码、人脸检测、巡线、移动、形状匹配、图像流、分类、颜色跟踪、人脸识别、目标追踪、形状检测、自定义对象识别
  - 支持 web 在线预览，UiFlow (用作串口 json 格式调用)
  - Linux 环境 (OpenCV、SSH、JupyterNotebook)

## 包装内容

- 1 x UnitV2-M12
- 1 x 16GB microSD 卡
- 1 x USB Type-C 连接线 (50cm)
- 1 x 支架
- 1 x 背夹
- 1 x 常规焦段镜头 (FOV:85°)
- 1 x 广角鱼眼镜头 (FOV:150°)

## 应用场景

- Ai 识别功能开发
- 工业视觉识别分类
- 机器视觉学习

## 规格参数

| 规格              | 参数                                                                             |
| ----------------- | -------------------------------------------------------------------------------- |
| SigmaStar SSD202D | Dual Cortex-A7 1.2GHz Processor                                                  |
| Flash             | 512MB NAND                                                                       |
| RAM               | 128MB-DDR3                                                                       |
| Camera            | GC2053 1080P Colored Sensor                                                      |
| Lens              | 1x 常规焦段 (FOV:85°) + 1x 广角鱼眼镜头 (FOV:150°)                               |
| 输入电压          | 5V@500mA                                                                         |
| 硬件外设          | USB Type-C x1，UART x1，TFCard x1，Button x1，Microphone x1，内置主动散热风扇 x1 |
| 指示灯            | 红，白                                                                           |
| Wi-Fi             | 150Mbps 2.4GHz 802.11 b/g/n                                                      |
| 以太网网卡        | SR9900                                                                           |
| 产品尺寸 (含镜头) | 48.0 x 24.0 x 32.0mm                                                             |
| 产品重量          | 26.5g                                                                            |
| 包装尺寸          | 147.0 x 45.0 x 39.0mm                                                            |
| 毛重              | 77.9g                                                                            |

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/unitv2_m12/unitv2_m12_sch_01.webp" width="70%">

## 尺寸图

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1052/U078-M12_Model_Size_page_01.png" width="70%">

## 软件开发

### 快速上手

- UnitV2 内部集成由 M5Stack 开发的基础 Ai 识别服务，内置多种识别功能 (如人脸识别，对象跟踪等常用功能)，能够快速帮助用户构建 Ai 识别应用。

- 所有功能！即插即用！UnitV2 内置了一张有线网卡，当你通过 Type-C 接口连接 PC 时，将自动与 UnitV2 建立起网络连接。还可以通过 WiFi 形式连接与调试，具备高自由度。

- UART 串口输出，所有识别内容自动通过串口输出**JSON**格式，方便调用。

- [内置识别功能使用教程](/zh_CN/guide/ai_camera/unitv2/base_functions)

- [V-Training在线AI模型训练服务](/zh_CN/guide/ai_camera/unitv2/v_training)

- [Jupyter Notebook开发教程/Example](/zh_CN/guide/ai_camera/unitv2/jupyter_notebook)

- [SSH连接 & WIFI配置](/zh_CN/guide/ai_camera/unitv2/config)

- [固件更新教程](/zh_CN/guide/ai_camera/unitv2/update)

### SDK

- [UnitV2Framework](https://github.com/m5stack/UnitV2Framework)

### USB 驱动

| Driver Name    | Download Link                                                                                                                                |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| SR9900_Windows | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/sr9900.inf_amd64.zip)                                               |
| SR9900_MacOS   | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/SR9900_macos_v1.3%20driver%20and%20installation%20instructions.zip) |

#### For Windows10

- 将驱动压缩包解压至桌面路径 -> 进入设备管理器中选中当前未识别的设备 (名称为**USB 10/100 LAN**或带有**SR9900**字符) -> 右键选择自定义更新 -> 选中压缩包解压的路径 -> 点击确认，等待更新完成。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/ai_camera/unitv2/sr9900_01.png" width="70%">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/ai_camera/unitv2/sr9900_02.jpg" width="70%">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/ai_camera/unitv2/sr9900_03.jpg" width="70%">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/ai_camera/unitv2/sr9900_04.jpg" width="70%">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/ai_camera/unitv2/sr9900_05.jpg" width="70%">

#### For MacOS

- 解压驱动压缩包 -> 双击打开 SR9900_v1.x.pkg 文件 -> 根据提示点击下一步安装。(压缩包内包含了详细版本的驱动安装教程 pdf)

- 安装完成后，若网卡无法正常启用，可以打开终端，使用下方命令重新启用网卡。

```python
sudo ifconfig en10 down
sudo ifconfig en10 up
```

### 其他

learn>| ![使用M5Stack UnitV2和边缘脉冲进行物体检测](https://static-cdn.m5stack.com/resource/docs/products/unit/unitv2/demo.png) | [使用M5Stack UnitV2和边缘脉冲进行物体检测](https://www.hackster.io/naveenbskumar/object-detection-using-m5stack-unitv2-and-edge-impulse-650a2f) | 使用 M5Stack 出品的最新 Linux AI 智能摄像头 UnitV2，搭建一个模拟工业应用场景下的不良品筛选功能.|

## 相关视频

**UnitV2 内置功能开箱使用**

<video width="500" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Unit/UnitV2_video_en.mp4" type="video/mp4">
</video>

**UnitV2 应用场景**

<video width="500" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Unit/UnitV2_video_release.mp4" type="video/mp4">
</video>

## 产品对比

::compare-table
| 规格     | [UnitV2](/zh_CN/unit/unitv2) ![UnitV2](https://static-cdn.m5stack.com/resource/docs/products/unit/unitv2/unitv2_cover_01.webp) | [UnitV2-M12](/zh_CN/unit/unitv2_m12) ![UnitV2-M12](https://static-cdn.m5stack.com/resource/docs/products/unit/unitv2_m12/3.webp) | [UnitV2-USB](/zh_CN/unit/unitv2_usb) ![UnitV2-USB](https://static-cdn.m5stack.com/resource/docs/products/unit/unitv2_usb/3.webp) |
| -------- | ------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| 镜头配备 | 常规焦段 (FOV 68°)                                                                                                             | 常规焦段 (FOV 85°) + 广角焦段 (FOV:150°)                                                                                         | 不配备镜头，USB-A 通用接口，可外接各种 UVC 摄像头                                                                                |
| CMOS     | GC2145                                                                                                                         | GC2053                                                                                                                           | /                                                                                                                                |
::

如需对比 UnitV 系列产品信息，可访问[产品选型表](/zh_CN/products_selector/unitv_compare?select=U078-M12)，勾选目标产品即可获取对比结果。选型表涵盖核心参数、功能特性等关键信息，支持多产品同步比对。
