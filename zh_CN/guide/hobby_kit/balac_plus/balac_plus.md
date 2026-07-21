# BalaC-Plus 上手体验

\#> 说明 | 本教程将演示如何为 BalaC-Plus 烧录平衡车固件，并说明校准操作，使得 BalaC-Plus 能够平衡站立。

## 1. 准备工作

- [参考 M5Burner 教程](/zh_CN/uiflow/m5burner/intro)完成烧录工具下载，并参考下图，下载对应的固件。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1074/balac_plus_burner_01.png" width="80%" />

## 2. USB 驱动安装

\#> 驱动程序安装提示 | 将设备连接至 PC，打开设备管理器为设备安装[FTDI驱动](https://ftdichip.com/drivers/vcp-drivers/)。以 win10 环境为例，下载匹配操作系统的驱动文件，并解压，通过设备管理器进行安装。(注：某些系统环境下，需要安装两次，驱动才会生效，未识别的设备名通常为`M5Stack`或`USB Serial`, Windows 系统推荐使用驱动文件在设备管理器直接进行安装 (自定义更新), **可执行文件**安装方式可能无法正常工作)。[点击此处，前往下载FTDI驱动](https://ftdichip.com/drivers/vcp-drivers/)

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/ftdi_01.webp" width="30%"><img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/ftdi_02.webp" width="30%"><img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/ftdi_03.webp" width="30%">

\#> 对于 MacOS 用户，安装前请勾选 `系统偏好设置` - >`安全性与隐私` - >`通用` - >`允许以下位置下载的App` - > `App Store和认可的开发者选项`。

## 3. 固件烧录

将设备通过 USB 线连接至电脑，在 M5Burner 中选择对应设备的端口，点击`Start`烧录平衡车固件至 BalaC-Plus 。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1074/balac_plus_burner_02.png" width="80%" />
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1074/balac_plus_burner_03.png" width="80%" />

## 4. 校准与平衡

1. 将 BalaC-Plus 的电源开关切换到`ON`, 整机平放，单击 StickC-Plus 左侧开机键。
2. 等待提示 Cal-1（俯仰陀螺仪校准）完成。
3. 将 BalaC-Plus 直立并略微向前倾斜，保持静止，直到 Cal-2（加速度计与偏航陀螺仪校准）完成。
4. 开始平衡站立。注意：该案例仅作为功能测试使用，外部干扰推动将无法继续保持站立。若电机转动后，屏幕熄灭，可能是供电不足的原因，可尝试将电源开关切换到 `ON` 后，通过 StickC-Plus 的 USB Type-C 进行充电。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1074/balac_plus_power_on_01.jpg" width="50%" />

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1074/balac_plus_guide_video_01.mp4" type="video/mp4"></video>
