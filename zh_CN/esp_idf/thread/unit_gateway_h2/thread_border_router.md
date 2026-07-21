# ESP Thread Boarder Router

Unit Gateway H2 支持搭配 ESP32 系列 Wi-Fi SoC 运行 ESP Thread Boarder Router SDK，该 SDK 构建基于 ESP-IDF 和 OpenThread，将 Thread 网络运行在 H2 上，H2 通过串口与主处理器通信。

## 1. 准备工作

- 1\. 环境配置： 参考[ESP-IDF - ESP32S3上手教程](https://docs.espressif.com/projects/esp-idf/en/stable/esp32s3/index.html)完成基本编译环境。

\#>ESP-IDF 版本 | 该案例编译推荐使用 ESP-IDF 版本`v5.3.1`

```bash
git clone -b v5.3.1 --recursive https://github.com/espressif/esp-idf.git
cd esp-idf
./install.sh
. ./export.sh
```

- 2\. 使用到的硬件产品:
  - [Unit Gateway H2](https://shop.m5stack.com/products/esp32-h2-thread-zigbee-gateway-unit)
  - [CoreS3](https://shop.m5stack.com/products/m5stack-cores3-esp32s3-lotdevelopment-kit)

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/CoreS3/img-2f6b5728-af80-4934-854f-4771a7fe859e.webp" width="20%"><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1128/U195_10.webp" width="20%">

- 3\. 后续教程使用到的 idf.py 指令均依赖 ESP-IDF, 运行指令前需要执行 ESP-IDF 中`. ./export.sh`用于激活相关的环境变量。详细说明请参考[ESP-IDF - ESP32S3上手教程](https://docs.espressif.com/projects/esp-idf/en/stable/esp32s3/index.html)。

## 2. 编译 RCP 固件

- 1\. 在编译 Thread Boarder Router 固件之前，需要先生成 RCP 固件。参考下方指令进入对应的 rcp 固件目录，设置编译 target 为`esp32h2`。

\#> 波特率修改 | 由于芯片的引脚驱动能力等因素，使用长的连接线连接 Unit 时串口有可能无法正常工作，如遇到这种情况则需适当降速处理，此处将默认波特率 460800 降速为 230400。

- 2\. 修改波特率，打开 `main/esp_ot_config.h` ，将 43 行 `.baud_rate = 460800;` 修改为 `.baud_rate = 230400;`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1128/esp_thread_boarder_rcp_baudrate_change_01.png" width="50%">

```bash
cd examples/openthread/ot_rcp
vim main/esp_ot_config.h
# line 43 .baud_rate = 460800; 修改为 .baud_rate = 230400;
```

- 3\. 完成配置后，执行以下指令进行 RCP 固件编译。

```bash
cd $IDF_PATH/examples/openthread/ot_rcp
idf.py set-target esp32h2
idf.py build
```

- 3\. 打开 Unit Gateway H2 外壳，按住设备 boot 按键，然后连接 USB 供电使其进入下载模式。并执行以下指令进行烧录。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1128/U195_download_mode1.gif" width="50%">

```bash
idf.py flash
```

## 3. 编译 ESP Thread BR 固件

- 1\. 拉取项目。

```bash
git clone https://github.com/Ocean-lhy/esp-thread-br.git
```

\#> 使用 Unit Gateway H2 作为 RCP 实现 ESP Thread Boarder Router，需要关闭 RCP 烧录，修改波特率，修改串口引脚。以下对应的代码分支已进行修改，可直接切换使用。

- 2\. 根据使用的主控设备，切换到对应的分支。

```bash
# coreS3
git checkout demo_for_unit_coreS3
cd examples/thread_border_router_credential_sharing
idf.py set-target esp32s3
# core2 v1.0和v1.1的电源管理芯片分别为AXP192和AXP2101，需要在menuconfig中配置
git checkout demo_for_unit_core2
cd examples/thread_border_router_credential_sharing
idf.py set-target esp32
# core
git checkout demo_for_unit_core
cd examples/thread_border_router_credential_sharing
idf.py set-target esp32
```

- 3\. 使用`idf.py menuconfig`进入配置页面。在 menuconfig 中配置 WiFi 信息：`Component config` -> `Example Connection Configuration`

```bash
idf.py menuconfig
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1128/esp_thread_boarder_router_config_01.png" width="50%">

- 4\. 编译并烧录 ESP Thread BR 固件

```bash
idf.py build
idf.py erase_flash
idf.py flash
```

## 4. 开始运行

- 1\. 将 Unit Gateway H2 连接至主控设备 PORT.C ，等待设备连接 Wi-Fi 和 Thread 网络。完成设备初始化将显示以下信息内容：

- **generate epskc**按钮

- **factoryreset**按钮

- **Border router web server**网址

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1128/esp_thread_boarder_router_unit_connect_01.jpg" width="50%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1128/esp_thread_boarder_router_start_01.jpg" width="50%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1128/esp_thread_boarder_router_start_02.jpg" width="50%">

- 2\. 点击`generate epskc`按钮，设备将生成一个 epskc，并显示在屏幕上，可用于快捷入网使用。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1128/esp_thread_boarder_router_start_03.jpg" width="50%">

- 3\. 在局域网内，使用浏览器访问 Border router web server 网址，可以查看 Thread 网络信息。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1128/esp_thread_boarder_router_web_01.jpg" width="100%">

- 4\. 如果想修改连接的 WIFI 可以用串口连接指令界面，输入指令`wifi -s SSID -p PASSWORD`，然后重启设备。

## 5. 测试

使用 Unit Gateway H2 (ESP32-H2) 或 NanoC6 (ESP32-C6)，参考案例程序烧录[OpenThread SimpleCLI](https://github.com/espressif/arduino-esp32/blob/master/libraries/OpenThread/examples/SimpleCLI/SimpleCLI.ino)例程，连接到 Thread 网络，查看 Thread 网络信息。

1. 在 ThreadBoarderRouter 的后台输入`networkkey`、`panid`、`channel`，获取 Thread 网络的网络密钥、panid 和 channel。

2. 在 SimpleCLI 例程中输入配置命令并启动 Thread 网络

```bash
networkkey <networkkey>
panid <panid>
channel <channel>
ifconfig up
thread start
```

3. 在 SimpleCLI 串口交互输入`state`，查看 Thread 网络状态，如果作为 child/router 连接上网络，则 Thread 网络连接成功。如果作为 leader 成立网络，则配置可能有误。
4. 在 SimpleCL 串口交互输入`parent`，查看 Thread 网络的父节点；输入`extaddr`，查看此节点的扩展地址。
5. 在 ThreadBoarderRouter 的串口交互输入`extaddr`，查看此节点的扩展地址，应与 SimpleCLI 例程中的`parent extaddr`一致。
6. 在 ThreadBoarderRouter 的串口交互输入`neighbor table`，查看 Thread 网络的邻居节点，应包含 SimpleCLI 例程的节点。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1128/esp_thread_boarder_router_monitor_01.png" width="100%">
