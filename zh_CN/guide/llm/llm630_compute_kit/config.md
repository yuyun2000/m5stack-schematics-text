# LLM630 Compute Kit Config

## ADB Tools

LLM630 Compute Kit 可通过 ADB 调试工具进行调试，本教程将说明如何通过 ADB 工具访问 LLM630 Compute Kit 终端，和传输文件。操作前请根据自己的操作系统下载[ADB Platform-Tools](https://developer.android.com/tools/releases/platform-tools)

### 文件传输

1.USB 连接 LLM630 Compute Kit 的`OTG`接口至电脑

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/llm/llm630_compute_kit/config/llm630_compute_kit_adb_01.jpg" width="50%" />

2\. 切换至 ADB 工具所在路径，使用`push`指令传输文件。如果显示 "没有权限"，请执行以下命令。

```bash
adb.exe kill-server
```

3\. 传输文件

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

## UART

1.USB 连接 LLM630 Compute Kit 的 UART 接口至电脑，可通过[Putty](https://www.putty.org/)等调试工具通过串口的方式登录设备终端，实现调试与控制。(默认：115200bps 8N1, 默认账户为`root`, 密码为`root`。)

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/llm/llm630_compute_kit/config/llm630_compute_kit_uart_01.jpg" width="50%" />
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/llm/llm630_compute_kit/config/llm630_compute_kit_uart_02.jpg" width="70%" />
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/llm/llm630_compute_kit/config/llm630_compute_kit_uart_03.jpg" width="70%" />

## Ethernet

LLM630 Compute Kit 提供了以太网接口可以非常方便的接入网络与功能调试。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/llm/llm630_compute_kit/config/llm630_compute_kit_eth_01.jpg" width="50%" />

## Wi-Fi

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

## SSH

1\. 将连接 LLM630 Compute Kit 网线，参考上方 ADB/UART 连接教程进入设备终端。通过以下指令获取设备 IP 地址。

```bash
ifconfig
```

2\. 局域网内可通过 ssh 远程访问设备，默认账户为`root`, 密码为`root`。

```bash
ssh root@192.168.20.167
```

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/llm/llm630_compute_kit/config/llm630_compute_kit_ssh_01.jpg" width="70%" />
