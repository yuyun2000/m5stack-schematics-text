# Module LLM - ADB / UART / SSH 连接调试

## ADB Tools

LLM Module 可通过 ADB 调试工具进行调试，本教程将说明如何通过 ADB 工具访问 LLM Module 终端，和传输文件。操作前请根据自己的操作系统下载[ADB Platform-Tools](https://developer.android.com/tools/releases/platform-tools)。

### 文件传输

1. USB 连接 LLM Module 的 TypeC 接口至电脑。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/llm/llm/llm_adb_01.png" width="50%" />

2. 切换至 ADB 工具所在路径，使用`push`指令传输文件。如果显示 “没有权限”，请执行以下命令。

```bash
adb.exe kill-server
```

3. 传输文件。

```bash
# adb.exe push local remote
adb.exe push data.json /opt
```

4. 进入设备终端。

```bash
adb.exe shell
```

```bash
sh-5.1# ls /opt/
bin  containerd  data  data.json  etc  lib  lost+found  m5stack  swupdate  usr
```

## Module LLM Debug Board

发布首批 Module LLM 含赠送的 Debug Board 提供了以太网接口与系统 Log 接口，可用于 LLM Module 接入网络与功能调试。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/992/module_llm_debug_board_connect_01.png" width="60%" />

## Module13.2 LLM Mate

与 Module13.2 LLM Mate 搭配使用，能够能更加稳定地连接 Module LLM 模块，同时提供以太网及系统 Log 接口。 注：使用前需移开扬声器露出下方的 FPC 座子。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1131/module_llm_mate_connect_01.jpg" width="70%" />
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1131/module_llm_mate_connect_02.png" width="70%" />

## UART

1. 接入调试板并连接系统 Log 调试接口，可通过[Putty](https://www.putty.org/)等调试工具通过串口的方式登录设备终端，实现调试与控制。(默认：115200bps 8N1, 默认账户为`root`, 密码为`123456`。)

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/llm/llm/llm_uart_01.jpg" width="70%" />
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/llm/llm/llm_uart_02.png" width="70%" />

## SSH

1. 接入调试板并连接网线，参考上方 ADB/UART 连接教程进入设备终端。通过以下指令获取 LLM Module IP 地址。

```bash
sh-5.1# ip addr
```

2. 局域网内可通过 ssh 远程访问设备，默认账户为`root`, 密码为`123456`。

```bash
ssh root@192.168.20.144
```

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/llm/llm/llm_ssh_01.png" width="70%" />
