# Voice Pyramid 蓝牙音箱使用教程

本教程将介绍使用[Atom-Matrix](/zh_CN/core/ATOM%20Matrix)搭配 Voice Pyramid 开发底座，通过 M5Burner 烧录 Voice Pyramid 蓝牙音箱固件的方法。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1214/Echo_Pyramid_BT_Audio_Cover_01.jpg" width="60%" />

## 1. 准备工作

1. 请根据您所使用的操作系统，点击下方按钮下载相应的 M5Burner 固件烧录工具，解压打开应用程序。

| 软件版本         | 下载链接                                                                        |
| ---------------- | ------------------------------------------------------------------------------- |
| M5Burner_Windows | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-beta-win-x64.zip)   |
| M5Burner_MacOS   | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-mac-x64.dmg)        |
| M5Burner_Linux   | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-beta-linux-x64.zip) |

2. 安装 USB 驱动

将设备连接至 PC，打开设备管理器为设备安装[FTDI 驱动](https://ftdichip.com/drivers/vcp-drivers/)。以 win10 环境为例，下载匹配操作系统的驱动文件， 并解压，通过设备管理器进行安装。(注：某些系统环境下，需要安装两次，驱动才会生效，未识别的设备名通常为`M5Stack`或`USB Serial`, Windows 推荐使用驱动文件在设备管理器直接进行安装 (自定义更新), 可执行文件安装方式可能无法正常工作)。[点击此处，前往下载 FTDI 驱动](https://ftdichip.com/drivers/vcp-drivers/)

<div class="product_pic"><img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/ftdi_01.webp"><img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/ftdi_02.webp"><img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/ftdi_03.webp"></div>

\#> 对于 MacOS 用户安装前请勾选 `系统偏好设置` - >`安全性与隐私` - >`通用` - >`允许以下位置下载的 App` - > `App Store 和认可的开发者选项`。

## 2. 下载固件

1. 双击打开 Burner 烧录工具，在左侧菜单中选择设备类型 `ATOM`, 点击 `Download` 下载`Voice Pyramid 蓝牙音箱`固件。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1214/echo_pyramid_audio_tutorial_01.png" width="70%" />

2. 将 Atom-Matrix 通过 USB 线连接至电脑。连接后，软件弹出 `Found New Device`表示此时连接成功，且屏幕不展示内容，进入编程模式。
3. 单击`Voice Pyramid 蓝牙音箱`固件的 Burn 按钮，选择对应设备端口后，单击`Start`开始烧录固件。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1214/echo_pyramid_audio_tutorial_02.png" width="70%" />
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1214/echo_pyramid_audio_tutorial_03.png" width="70%" />

?> 波特率限制 | 在进行设备程序下载操作时，推荐选用以下串口波特率选项。若采用其他速度，可能导致程序无法正常下载。<br/>**1500000 bps** / **750000 bps** / **500000 bps** / **250000 bps** / **115200 bps**

当提示`Burn successful，click here to return`时，表示烧录完成。

## 3. 连接蓝牙

1. 通过 Voice Pyramid 底部的 USB 接口为 Voice Pyramid 供电。

2. 设备通电后，在手机搜索蓝牙`EchoPyramid-xxxx`并连接。连接成功后即可使用 Voice Pyramid 蓝牙音箱。

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1214/echo_pyramid_audio_tutorial_video_01.mp4" type="video/mp4"></video>

- 用指腹在 Voice Pyramid 设备的左边区域往上滑动，可以选择上一曲；往下滑动，可以选择下一曲。
- 用指腹在 Voice Pyramid 设备的右边区域往上滑动，可以调大音量；往下滑动，可以调小音量。
