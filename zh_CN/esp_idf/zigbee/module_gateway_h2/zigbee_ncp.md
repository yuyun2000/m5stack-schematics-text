# ESP Zigbee NCP

本教程将介绍如何使用 Module Gateway H2 搭配 CoreS3 主控运行 ESP Zigbee Host/NCP 案例程序。ESP Zigbee NCP (Network Co-Processor) 是一种网络协处理器模式，它将 Zigbee 协议栈运行在一个独立的处理器上，通过串口与主处理器通信。这种架构可以让主处理器专注于应用层逻辑，而将 Zigbee 网络相关的处理交给协处理器处理。参考下方教程为 Module Gateway H2 烧录 ESP Zigbee NCP 固件，为 CoreS3 烧录 ESP Zigbee Host 固件，实现创建 Coordinator 节点。

## 1. 准备工作

- 1\. 环境配置： 参考[ESP-IDF - ESP32S3上手教程](https://docs.espressif.com/projects/esp-idf/en/stable/esp32s3/index.html)完成基本编译环境。

\#>ESP-IDF 版本 | 该案例编译推荐使用 ESP-IDF 版本`v5.3.1`

```bash
git clone -b v5.3.1 --recursive https://github.com/espressif/esp-idf.git
cd esp-idf
./install.sh
. ./export.sh
```

- 2\. 使用 Git 指令`clone recursive`递归克隆 ESP-Zigbee-SDK 仓库

```bash
git clone --recursive https://github.com/espressif/esp-zigbee-sdk.git
cd esp-zigbee-sdk
```

- 3\. 使用到的硬件产品:
  - [ESP32 Downloader](https://shop.m5stack.com/products/esp32-downloader-kit)
  - [Module Gateway H2](https://shop.m5stack.com/products/esp32-h2-thread-zigbee-gateway-module)
  - [CoreS3](https://shop.m5stack.com/products/m5stack-cores3-esp32s3-lotdevelopment-kit)

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/CoreS3/img-2f6b5728-af80-4934-854f-4771a7fe859e.webp" width="20%"><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/464/M141_04.webp" width="20%"><img src="https://static-cdn.m5stack.com/resource/docs/products/accessory/esp32_downloader_kit/esp32_downloader_kit_03.webp" width="20%">

- 4\. 后续教程使用到的 idf.py 指令均依赖 ESP-IDF, 运行指令前需要执行 ESP-IDF 中`. ./export.sh`用于激活相关的环境变量。详细说明请参考[ESP-IDF - ESP32S3上手教程](https://docs.espressif.com/projects/esp-idf/en/stable/esp32s3/index.html)。

## 2. 编译 NCP 固件

- 1\. 参考下方指令进入对应的 NCP 固件目录，设置编译 target 为`esp32h2`。

```bash
cd examples/esp_zigbee_ncp
idf.py set-target esp32h2
idf.py menuconfig
```

- 2\. 使用`idf.py menuconfig`进入配置页面。在 menuconfig 中配置设备的引脚信息：`Component config` -> `Zigbee Network Co-processor`

```bash
- Component config → Zigbee Network Co-processor
  - UART RX Pin: 23
  - UART TX Pin: 24
- Component config → ESP Zigbee → Configure the Zigbee device type
  - Zigbee Coordinator or Router device # or Zigbee End Device
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/464/idf_zigbee_ncp_config_01.png" width="40%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/464/idf_zigbee_ncp_config_02.png" width="40%">

```bash
idf.py build
idf.py erase_flash
idf.py flash # 根据实际端口修改
```

## 3. 编译 HOST 固件

- 1\. 参考下方指令进入对应的 HOST 固件目录，设置编译 target 为`esp32s3`。

```bash
cd examples/esp_zigbee_host
idf.py set-target esp32s3 # 使用 CoreS3
idf.py menuconfig
```

- 2\. 使用`idf.py menuconfig`进入配置页面。在 menuconfig 中配置设备的引脚信息：`Component config` -> `Zigbee NCP Host`

```
- Component config → Zigbee NCP Host
  - UART RX Pin: 10
  - UART TX Pin: 17
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/464/idf_zigbee_host_config_01.png" width="40%">

```bash
idf.py build
idf.py flash
```

## 4. 开始运行

- 将 CoreS3 与 Module Gateway H2 连接。
- 将 CoreS3 连接至电脑
- 通过`idf.py monitor`或其他的串口调试工具在 115200bps 配置下查看运行日志。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/464/idf_zigbee_ncp_monitor_01.png" width="100%">

正常运行日志内容：

- NCP 端显示 Zigbee 协议栈初始化成功
- Host 端显示与 NCP 连接成功
- Zigbee 网络创建成功（Coordinator 模式）
