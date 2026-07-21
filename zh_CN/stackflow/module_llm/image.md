# Module LLM 镜像底包更新

\#> 镜像底包更新 | 用于整机系统升级或出现系统损坏情况，可采用该方式进行刷机或升级。烧录工具目前仅支持 windows 平台，参考以下操作。

## 烧录工具 & 驱动

### 固件版本

1. 下载更新的固件包 (`.axp`)

| 固件版本                         | 下载链接                                                                                                           |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| M5_LLM_ubuntu_v1.3_20241203-mini | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/llm/M5_LLM_ubuntu2022-02_20241203-mini.axp) |
| M5_LLM_ubuntu_v1.6_20250612      | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/llm/M5_LLM_ubuntu2022-02_20250612.axp)      |
| M5_LLM_ubuntu22.04_20251121 | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/linux/llm/M140-Module_LLM-AX630C-%E5%87%BA%E5%8E%82%E5%9B%BA%E4%BB%B6-20251121_ubuntu-%E6%9D%8E%E5%9B%BD%E9%80%89-20251121-0x00.axp) |

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/llm/llm/llm_driver_install_01.jpg" width="70%">

2. 下载烧录工具和驱动程序，并完成驱动程序安装。

| 烧录工具 & 驱动程序  | 下载链接                                                                                                 |
| -------------------- | -------------------------------------------------------------------------------------------------------- |
| AXDL_V1.24.13.1      | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/software/AXDL_Flash_Tool_V1.24.13.1.7z) |
| AXDL_Driver_V1.20.46 | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/AXDL_Driver_V1.20.46.1.7z)      |

3. 打开烧录工具，点击左上角 load 按钮加载固件包，

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/llm/llm/llm_flash_update_01.jpg" width="70%">

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/llm/llm/llm_flash_update_02.jpg" width="70%">

4. 点击 start 按键，此时将进入烧录等待模式，等待检测到模块。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/llm/llm/llm_flash_update_03.jpg" width="70%">

### 固件烧录

1. 模块上电前保持长按下载按钮。
2. 模块上的 Type-C 接口连接至电脑。
3. 设备将进入下载模式，此时烧录软件将自动开始固件烧录。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/llm/llm/llm_flash_update_04.png" width="70%">

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/llm/llm/llm_flash_update_05.jpg" width="70%">

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/llm/llm/llm_flash_update_06.jpg" width="70%">

## 注意事项

!> 禁止尝试对 /dev/mmcblk0 进行分区操作 | 禁止尝试对 /dev/mmcblk0 进行分区操作。/dev/mmcblk0 为板载 emmc，默认是作为系统磁盘使用，在没有分区的情况下，ax630c 将其视为 emmc 启动项，从分区映射中读取数据并启动，一但分区后，将会被视为 sd 卡，使用 sd 卡模式启动，且由于优先级较高，此时一但出错，几乎没有在线修复的可能，连烧录操作都无法完成，只能拆下 emmc 强制擦除扇区才可以。

\#> 非标准 uboot | 由于爱芯的固件格式的特殊性，不符合标准的 uboot 启动项，所以几乎无法使用标准的 uboot 启动操作，本固件中添加了 before_boot_cmd 作为在 ax_boot 之前的自动完成的操作。当前是开启模块的灯。
