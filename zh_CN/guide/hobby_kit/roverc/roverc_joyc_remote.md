# RoverC & JoyC Remote Control

\#> 说明 | 本教程将演示如何为 RoverC, 和 JoyC 烧录无线控制固件，并实现配对和基本控制操作。本教程固件兼容`StickC/StickC-Plus/StickC-Plus2`主控设备，可参考以下教程，在 M5Burner 中直接烧录使用。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/hobby_kit/roverc/roverc_joyc_remote_controller_01.jpg" width="50%" />

## 1. 准备工作

- [参考M5Burner教程](/zh_CN/uiflow/m5burner/intro)完成烧录工具下载，并参考下图，下载对应的固件。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/hobby_kit/roverc/roverc_joyc_remote_01.jpg" width="80%" />

## 2.USB 驱动安装

- 烧录程序前，需根据实际使用的主控设备安装对应的驱动程序。

### For StickC/StickC-Plus

\#> 驱动程序安装提示 | 将设备连接至 PC，打开设备管理器为设备安装[FTDI驱动](https://ftdichip.com/drivers/vcp-drivers/)。以 win10 环境为例，下载匹配操作系统的驱动文件，并解压，通过设备管理器进行安装。(注：某些系统环境下，需要安装两次，驱动才会生效，未识别的设备名通常为`M5Stack`或`USB Serial`, Windows 推荐使用驱动文件在设备管理器直接进行安装 (自定义更新), 可执行文件安装方式可能无法正常工作)。[点击此处，前往下载FTDI驱动](https://ftdichip.com/drivers/vcp-drivers/)

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/ftdi_01.webp" width="30%"><img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/ftdi_02.webp" width="30%"><img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/ftdi_03.webp" width="30%">

\#> 对于 MacOS 用户安装前请勾选 `系统偏好设置` - >`安全性与隐私` - >`通用` - >`允许以下位置下载的App` - > `App Store和认可的开发者选项`。

### For StickC-Plus2

\#> 驱动程序安装提示 | 点击下方连接下载匹配操作系统的驱动程序。CP34X (适用于`CH9102`) 驱动程序压缩包。在解压压缩包后，选择对应操作系统位数的安装包进行安装。 在使用时，若出现无法正常下载程序 (提示超时或者是 Failed to write to target RAM) 的情况，可尝试重新安装设备驱动。

| 驱动名称                  | 适用驱动芯片 | 下载链接                                                                                             |
| ------------------------- | ------------ | ---------------------------------------------------------------------------------------------------- |
| CH9102_VCP_SER_Windows    | CH9102       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CH9102_VCP_SER_Windows.exe) |
| CH9102_VCP_SER_MacOS v1.7 | CH9102       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CH9102_VCP_MacOS_v1.7.zip)  |

## 3. 端口选择

将设备通过 USB 线连接至电脑，在设备进入下载模式后， M5Burner 中可选中对应设备的端口。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/hobby_kit/roverc/roverc_joyc_remote_02.jpg" width="80%" />

## 4. 固件烧录

为 RoverC 和 JoyC 分别烧录对应的 Master 和 Remote 固件。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/hobby_kit/roverc/roverc_joyc_remote_03.jpg" width="80%" />

## 5. 配对连接

将 RoverC 与 JoyC 的电源开关切换到`ON`, 先开启 RoverC 上的 StickC 主控 (AP 启动), 再开启 JoyC 上的 StickC。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/hobby_kit/roverc/roverc_joyc_remote_05.jpg" width="50%" />

待 JoyC 上的 StickC 扫描到 RoverC, 持续长按中间按钮进行连接，直到显示遥控状态信息则表示已经连接。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/hobby_kit/roverc/roverc_joyc_remote_04.jpg" width="50%" />

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/hobby_kit/roverc/roverc_joyc_remote_06.jpg" width="50%" />

## 6. 开始使用

\#> 操作说明 | 左侧遥杆控制移动，右侧摇杆控制转向。左右侧摇杆按键控制舵机夹持与释放。(注：夹持功能仅 RoverC-Pro 支持)

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/hobby_kit/roverc/roverc_joyc_remote_07.jpg" width="50%" />
