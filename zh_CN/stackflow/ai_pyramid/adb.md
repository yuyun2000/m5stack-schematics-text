# AI Pyramid ADB 连接调试

## ADB 安装

AI Pyramid 可通过 ADB 调试工具进行调试，本教程将说明如何通过 ADB 工具访问 AI Pyramid 终端，和传输文件。操作前请根据自己的操作系统下载[ADB Platform-Tools](https://developer.android.com/tools/releases/platform-tools)。

## 文件传输

1. AI Pyramid 的 USB ADB 接口连接至 PC。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1213/ai_pyramid_usb_adb_01.jpg" width="50%" />

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
bin  containerd  data  etc  lib  lost+found
```
