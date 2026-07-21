# M5Core2 恢复出厂固件

\#> 出厂固件 | 当设备出现工作异常时，可尝试重新烧录出厂固件来检验设备硬件是否存在故障。参考以下教程。使用 M5Burner 固件烧录工具，为设备烧录出厂固件。

## 1. 准备工作

- [参考M5Burner教程](/zh_CN/uiflow/m5burner/intro)完成烧录工具下载，并参考下图，下载对应的固件。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/restore_factory/m5core2/m5core2_burner_factory_01.jpg" width="80%" />

## 2.USB 驱动安装

\#> 驱动程序安装提示 | 点击下方连接下载匹配操作系统的驱动程序。目前存在两种驱动芯片版本，CP210X (适用于`CP2104`版本)/CP34X (适用于`CH9102`版本) 驱动程序压缩包。在解压压缩包后，选择对应操作系统位数的安装包进行安装。(若您不确定您的设备所使用的 USB 芯片，可同时安装两种驱动。`CH9102_VCP_SER_MacOS v1.7`在安装过程中，可能出现报错，但实际上已经完成安装，忽略即可。)

| 驱动名称                  | 适用驱动芯片 | 下载链接                                                                                             |
| ------------------------- | ------------ | ---------------------------------------------------------------------------------------------------- |
| CP210x_VCP_Windows        | CP2104       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CP210x_VCP_Windows.zip)     |
| CP210x_VCP_MacOS          | CP2104       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CP210x_VCP_MacOS.zip)       |
| CP210x_VCP_Linux          | CP2104       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CP210x_VCP_Linux.zip)       |
| CH9102_VCP_SER_Windows    | CH9102       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CH9102_VCP_SER_Windows.exe) |
| CH9102_VCP_SER_MacOS v1.7 | CH9102       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CH9102_VCP_MacOS_v1.7.zip)  |

## 3. 端口选择

将设备通过 USB 线连接至电脑，在完成驱动安装后， M5Burner 中可选中对应设备的端口。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/restore_factory/m5core2/m5core2_burner_factory_02.jpg" width="80%" />

## 4. 固件烧录

点击 Burn 开始烧录。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/restore_factory/m5core2/m5core2_burner_factory_03.jpg" width="80%" />

效果如下图：

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/restore_factory/m5core2/m5core2_burner_factory_04.png" width="80%" />
