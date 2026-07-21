# AI Pyramid 镜像烧录

\#> 镜像烧录 | 用于整机系统升级或出现系统损坏情况，可采用该方式进行刷机或升级。烧录工具目前仅支持 windows 平台，参考以下操作。

## 1. 烧录工具 & 驱动

1. 下载更新的固件包 (`.axp`)

| 固件版本                                              | 下载链接                                                                                                                                                                   |
| ----------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AI_Pyramid_emmc_ubuntu_rootfs_desktop_V3.6.4          | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/AI_Pyramid/AI_Pyramid_emmc_ubuntu_rootfs_desktop_V3.6.4_20250822020158_20260115105829.axp)          |
| AI_Pyramid_openclaw_emmc_ubuntu_rootfs_desktop_V3.6.4 | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/AI_Pyramid/AI_Pyramid_openclaw_emmc_ubuntu_rootfs_desktop_V3.6.4_20250822020158_20260306105829.axp) |

2. 下载烧录工具和驱动程序，并完成驱动程序安装。

| 烧录工具 & 驱动程序  | 下载链接                                                                                                |
| -------------------- | ------------------------------------------------------------------------------------------------------- |
| AXDL_V1.25.8.1       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/software/AXDL_Flash_Tool_V1.25.8.1.7z) |
| AXDL_Driver_V1.20.46 | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/AXDL_Driver_V1.20.46.1.7z)     |

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1213/ai_pyramid_driver_install_01.png" width="70%">

3. 打开烧录工具，点击左上角 load 按钮加载固件包。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1213/ai_pyramid_image_flash_01.png" width="70%">

4. 点击 start 按键，此时将进入烧录等待模式，等待检测到设备端口。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1213/ai_pyramid_image_flash_02.png" width="70%">

## 2. 固件烧录

1. 设备断开电源连接，USB 下载接口连接至 PC (该接口仅用于通信，并不作为供电使用)，保持长按顶部的 BOOT 按钮。
2. 连接设备底部 USB PD 供电接口上电。注意：请使用 PD 适配器进行供电，设备供电能力要求 DC 9V@3A (27W) 以上。使用 DC 5V 供电将无法正常启动。
3. 设备将进入下载模式，此时烧录软件将自动开始固件烧录。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1213/ai_pyramid_download_mode_01.jpg" width="70%">

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1213/ai_pyramid_image_flash_03.png" width="70%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1213/ai_pyramid_image_flash_04.png" width="70%">
