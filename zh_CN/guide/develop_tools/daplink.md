# M5 DAPLink

本教程将介绍如何将 M5 DAPLink 固件刷入 Core2 或 CoreS3，使其成为离线烧录器，从而方便为其他内置 STM32 芯片的产品更新固件。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/daplink_cores3_cover_01.png" width="40%"><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/daplink_core2_cover_01.png" width="40%">

## 1. 准备工作

- 使用到的硬件产品:
  - [Core2](https://shop.m5stack.com/products/m5stack-core2-esp32-iot-development-kit) / [CoreS3](https://shop.m5stack.com/products/m5stack-cores3-esp32s3-lotdevelopment-kit)
  - [Module Bus](https://shop.m5stack.com/products/bus-module)
  - microSD 卡
  - 读卡器
  - 公对母杜邦线
  - 母对母杜邦线

## 2. 烧录 DAPLink 固件

### M5Burner

- 请根据您所使用的操作系统，点击下方按钮下载相应的 M5Burner 固件烧录工具。解压打开应用程序。

| 软件版本         | 下载链接                                                                        |
| ---------------- | ------------------------------------------------------------------------------- |
| M5Burner_Windows | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-beta-win-x64.zip)   |
| M5Burner_MacOS   | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-mac-x64.dmg)        |
| M5Burner_Linux   | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-beta-linux-x64.zip) |

- 双击打开 Burner 烧录工具，在左侧菜单中选择对应的设备类型，下载匹配自己设备的固件。

### CoreS3 DAPLink

- 下载 CoreS3 设备固件：`CoreS3`->`CoreS3 DAPLink`固件，并参考[CoreS3文档](/zh_CN/core/CoreS3)学习如何控制设备进入下载模式，待电脑端成功识别到设备端口后，即可进行烧录。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/daplink_cores3_m5burner_01.jpg" width="70%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/daplink_cores3_m5burner_02.jpg" width="70%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/daplink_cores3_m5burner_03.jpg" width="70%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/daplink_cores3_show_01.jpg" width="50%">

### Core2 DAPLink

- 下载 Core2 设备固件：`Core2`->`Core2 DAPLink`固件，并参考[Core2文档](/zh_CN/core/core2)安装对应 USB 驱动程序，待电脑端成功识别到设备端口后，即可进行烧录。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/daplink_core2_m5burner_01.jpg" width="70%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/daplink_core2_show_01.jpg" width="50%">

## 3. 导入烧录算法与固件

下载下方 algorithm 烧录算法压缩包，该算法包与固件一同导入至主控设备，并在后续烧录固件时用于匹配不同的芯片型号，固件中已经内置了部分烧录算法选项，手动导入的方式可用于后续拓展更多烧录算法。不同的主控设备型号支持的文件导入方式上有些差异，具体请参考下方内容。

- [algorithm](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/algorithm.zip)

### 虚拟 U 盘导入

?> 虚拟 U 盘导入 | 虚拟 U 盘导入方法在当前固件版本中仅适用于 CoreS3

将下载的 algorithm 烧录算法压缩包解压并复制至 CoreS3 虚拟 U 盘中。并在根目录下创建`program`文件夹，其中放置后续用于烧录的固件文件 (hex/bin)。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/daplink_msc_01.jpg" width="50%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/daplink_msc_02.jpg" width="50%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/daplink_msc_03.jpg" width="50%">

### microSD 导入

?>microSD 导入 | microSD 导入方法在当前固件版本中仅适用于 Core2

将下载的 algorithm 烧录算法压缩包解压并复制至 microSD 卡中。并在根目录下创建`program`文件夹，其中放置后续用于烧录的固件文件 (hex/bin)。文件目录结构与 CoreS3 虚拟 U 盘导入一致。

### 网页导入

\#> 网页导入 | 网页导入方法仅适用于 Core2，CoreS3。导入的数据将自动保存至设备 flash storage 分区中。(注意事项：若是 Core2 使用 SD 卡情况下，则存储至 SD 卡。 CoreS3 使用网页导入方式前，需先在电脑端安全移除 U 盘设备后，才能正常导入。)

设备上电后开启 AP 热点 \`\`，电脑连接 AP 热点后浏览器访问`192.168.4.1`。点击`Program`跳转至文件上传页面，依次上传算法文件和固件文件。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/daplink_ap_upload_01.jpg" width="50%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/daplink_ap_upload_02.jpg" width="50%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/daplink_ap_upload_03.jpg" width="50%">

## 4. 设备连接

固件所使用的 DAPLink 管脚映射如下表所示:

| DAPLink | SWDIO | SWCLK | RESET | 3V3 | GND |
| ------- | ----- | ----- | ----- | --- | --- |
| Core2   | G27   | G19   | G32   | 3V3 | GND |
| CoreS3  | G6    | G7    | G2    | 3V3 | GND |

以 Unit EXT.IO2 固件更新为例，在拆开设备外壳后找到预留的程序下载焊孔，并根据其管脚映射依次进行连接，如遇接触不良的情况，可尝试将连接线 pin 针倾斜确保与焊盘接触。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/daplink_cores3_pinmap_01.png" width="50%">

## 5. 开始烧录

完成烧录算法与固件的导入后，设备启动将显示当前可选的烧录算法与固件。选中匹配当前烧录对象的烧录算法与更新固件。依次点击`Idle`，`Busy`按钮开始烧录。注：部分芯片如 STMF0xx 系列可能需要点击两次`Busy`才能开始烧录。

?>CoreS3 DAPLink 烧录注意事项 | CoreS3 连接电脑后默认将挂载虚拟 U 盘，点击烧录前需要在电脑端安全移除 U 盘设备后，才能进行烧录。为方便操作，推荐使用普通 5V 充电器直接供电。

| 烧录算法      | 适用的芯片类型 | Flash 大小 |
| ------------- | -------------- | ---------- |
| STM32F0xx_16  | STM32F0xx      | 16K        |
| STM32F0xx_64  | STM32F0xx      | 64K        |
| STM32G0xx_32  | STM32G0xx      | 32K        |
| STM32G0xx_64  | STM32G0xx      | 64K        |
| STM32G4xx_128 | STM32G4XX      | 128K       |

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/daplink_cores3_download_01.jpg" width="50%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/daplink_cores3_download_02.jpg" width="50%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/daplink_cores3_download_03.jpg" width="50%">

## 6. 搭配 Module Bus

\#> 搭配 Module Bus 使用 | 如果是作为日常 DAPLink 调试工具使用，为了接线连接更加方便，非常推荐搭配[Module Bus](https://shop.m5stack.com/products/bus-module)模块使用。Module Bus 能够将主控设备上 M5-Bus 总线引出至板子边缘侧，同时提供了 2 组 2.54-15P 的 90° 插针能够非常方便的连接杜邦线。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/daplink_cores3_module_bus_02.jpg" width="50%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/daplink_cores3_module_bus_01.png" width="50%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/daplink_cores3_module_bus_03.jpg" width="50%">
