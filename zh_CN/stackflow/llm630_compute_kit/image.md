# LLM630 Compute Kit 镜像底包更新

#>镜像底包更新 | 用于整机系统升级或出现系统损坏情况, 可采用该方式进行刷机或升级。烧录工具目前仅支持windows平台, 参考以下操作。

## 烧录工具&驱动

### 固件版本

1.下载更新的固件包(`.axp`)


| 固件版本                    | 下载链接                                                                                                                      |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| M5_LLM_ubuntu22.04_20250328 | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/ax630_kit/M5_LLM_ubuntu22.04_20250328_AX630C_LITE.axp) |


<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/llm/llm630_compute_kit/image/llm630_compute_kit_driver_install_01.jpg" width="70%">

2.下载烧录工具和驱动程序, 并完成驱动程序安装。

| 烧录工具&驱动程序    | 下载链接                                                                                                 |
| -------------------- | -------------------------------------------------------------------------------------------------------- |
| AXDL_V1.24.13.1      | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/software/AXDL_Flash_Tool_V1.24.13.1.7z) |
| AXDL_Driver_V1.20.46 | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/AXDL_Driver_V1.20.46.1.7z)      |


3.打开烧录工具, 点击左上角load按钮加载固件包, 

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/llm/llm630_compute_kit/image/llm630_compute_kit_flash_update_01.jpg" width="70%">

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/llm/llm630_compute_kit/image/llm630_compute_kit_flash_update_02.jpg" width="70%">

4.点击start按键, 此时将进入烧录等待模式, 等待检测到模块。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/llm/llm630_compute_kit/image/llm630_compute_kit_flash_update_03.jpg" width="70%">

### 固件烧录

- 1.模块上电前保持长按下载按钮。
- 2.模块上的USB-OTG接口连接至电脑。
- 3.设备将进入下载模式, 此时烧录软件将自动开始固件烧录。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/459/llm630_compute_kit_flash_update_04.png" width="70%">

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/llm/llm630_compute_kit/image/llm630_compute_kit_flash_update_05.jpg" width="70%">

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/llm/llm630_compute_kit/image/llm630_compute_kit_flash_update_06.jpg" width="70%">

## 注意事项

!> 禁止尝试对 /dev/mmcblk0 进行分区操作 | 禁止尝试对 /dev/mmcblk0 进行分区操作。/dev/mmcblk0 为板载 emmc，默认是作为系统磁盘使用，在没有分区的情况下，ax630c 将其视为 emmc 启动项，从分区映射中读取数据并启动，一但分区后，将会被视为 sd 卡，使用 sd 卡模式启动，且由于优先级较高，此时一但出错，几乎没有在线修复的可能，连烧录操作都无法完成，只能拆下 emmc 强制擦除扇区才可以。

#> 非标准uboot | 由于爱芯的固件格式的特殊性，不符合标准的 uboot 启动项，所以几乎无法使用标准的 uboot 启动操作，本固件中添加了before_boot_cmd作为在ax_boot之前的自动完成的操作。当前是开启模块的灯。

