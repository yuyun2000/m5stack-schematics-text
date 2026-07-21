# LLM630 Compute Kit UART / ADB / SSH 连接调试

\#> 连接调试 | LLM630 Compute Kit 提供多种连接和调试方式，包括 ADB、UART 串口和 SSH 远程访问。本指南将详细介绍如何通过这些接口与设备建立连接、进行网络配置以及解决常见问题，帮助开发者快速上手并充分利用设备的各项功能。

## 1. 连接调试

### ADB Tools

本小节将说明如何通过 ADB 工具访问 LLM Module 终端，和传输文件。操作前请根据自己的操作系统下载[ADB Platform-Tools](https://developer.android.com/tools/releases/platform-tools)

1. 连接 LLM630 Compute Kit 的`USB-OTG`接口至电脑

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/llm/llm630_compute_kit/config/llm630_compute_kit_adb_01.jpg" width="50%" />

2. 使用命令行切换至 ADB 工具所在路径，使用`push`指令传输文件。如果显示 "没有权限"，请执行以下命令。

```bash
adb.exe kill-server
```

3. 传输文件示例：将本地的`data.json`传输至 LLM630 Compute Kit 路径 `/opt`中。

```bash
# adb.exe push local remote
adb.exe push data.json /opt
```

4\. 进入设备终端

```bash
adb.exe shell
```

```bash
/ # ls /opt/
bin  data  etc  include  jupyter  lib  m5stack  swupdate  usr
```

### UART

1.USB 连接 LLM630 Compute Kit 的 UART 接口至电脑，可通过[Putty](https://www.putty.org/)等调试工具通过串口的方式登录设备终端，实现调试与控制。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/llm/llm630_compute_kit/config/llm630_compute_kit_uart_01.jpg" width="50%" />

2. 默认串口连接配置为：115200bps 8N1。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/llm/llm630_compute_kit/config/llm630_compute_kit_uart_02.jpg" width="70%" />

3. 点击 open 后，按下回车键， 根据提示依次输入登录信息。 默认账户为`root`, 密码为`root`。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/llm/llm630_compute_kit/config/llm630_compute_kit_uart_03.jpg" width="70%" />

## 2. 网络配置

### Ethernet

LLM630 Compute Kit 提供了以太网接口可以非常方便的接入网络与功能调试。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/llm/llm630_compute_kit/config/llm630_compute_kit_eth_01.jpg" width="50%" />

### Wi-Fi

LLM630 Compute Kit 板载了 ESP32-C6 作为 Wi-Fi 芯片，方便接入无线网络。可参考下方操作流程，启用 Wi-Fi 功能与配置连接。使用前请安装配套的 SMA 外置天线。

```bash
core-config
```

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/llm/llm630_compute_kit/config/llm630_compute_kit_core_config_01.jpg" width="70%" />
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/llm/llm630_compute_kit/config/llm630_compute_kit_core_config_02.jpg" width="70%" />
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/llm/llm630_compute_kit/config/llm630_compute_kit_core_config_03.jpg" width="70%" />
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/llm/llm630_compute_kit/config/llm630_compute_kit_core_config_04.jpg" width="70%" />

LLM630 Compute Kit 默认底包中，采用`ntmui`作为网络配置工具。通过`nmtui`工具能够非常方便的配置 Wi-Fi 连接

```bash
nmtui
```

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/llm/llm630_compute_kit/config/llm630_compute_kit_wifi_01.jpg" width="70%" />
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/llm/llm630_compute_kit/config/llm630_compute_kit_wifi_02.jpg" width="70%" />
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/llm/llm630_compute_kit/config/llm630_compute_kit_wifi_03.jpg" width="70%" />
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/llm/llm630_compute_kit/config/llm630_compute_kit_wifi_04.jpg" width="70%" />

## 3. SSH 远程访问

1\. 将连接 LLM630 Compute Kit 网线，参考上方 ADB/UART 连接教程进入设备终端。通过以下指令获取设备 IP 地址。

```bash
ifconfig
```

2\. 局域网内可通过 ssh 远程访问设备，默认账户为`root`, 密码为`root`。

```bash
ssh root@192.168.20.167
```

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/llm/llm630_compute_kit/config/llm630_compute_kit_ssh_01.jpg" width="70%" />
