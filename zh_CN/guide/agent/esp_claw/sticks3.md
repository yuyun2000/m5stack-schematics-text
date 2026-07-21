# StickS3 ESP-Claw 固件烧录

本教程详细介绍如何在 StickS3 上烧录 ESP-Claw 固件，帮助用户快速将 StickS3 设备配置为支持 AI 交互、硬件编程与自动化控制的智能终端。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/StickS3-ESP-Claw-cover.jpg" width="50%" />

## 1. 准备工作

请根据您所使用的操作系统，点击下方按钮下载相应的 M5Burner 固件烧录工具，并解压打开应用程序。

| 软件版本         | 下载链接                                                                        |
| ---------------- | ------------------------------------------------------------------------------- |
| M5Burner_Windows | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-beta-win-x64.zip)   |
| M5Burner_MacOS   | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-mac-x64.dmg)        |
| M5Burner_Linux   | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-beta-linux-x64.zip) |

## 2. 固件烧录

1. 双击打开 Burner 烧录工具，在左侧菜单中选择设备类型`STICKS3`，点击`Download`下载 StickS3 的 ESP-Claw 固件。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/StickS3-ESP-Claw-tutorial_01.png" width="80%">

2. 将 StickS3 连接 USB 线，长按机身侧边复位按键。当设备内部绿色 LED 闪烁时，表示设备已成功进入下载模式，等待烧录。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/stickS3_operate_01.gif" width="50%">

3. 单击`Burn`，选择设备对应的端口后，单击`Start`，等待烧录完成。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/StickS3-ESP-Claw-tutorial_02.png" width="80%" />
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/StickS3-ESP-Claw-tutorial_03.png" width="80%" />

烧录完成示意图：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/StickS3-ESP-Claw-tutorial_04.png" width="80%" />

## 3.设备配置

1. 重启设备，设备启动后，将提示连接 AP 热点。在手机/电脑连接热点**esp-claw-xxx**，然后访问`192.168.4.1`进入设备配置页面。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/StickS3-ESP-Claw-tutorial_09.png" width="40%" />
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/CoreS3-ESP-Claw-tutorial_10.png" width="40%" />

2. 在 `WI-FI SETTINGS`区域内填写 Wi-Fi 名称和密码后，选择模型供应商，并填写对应的 API Key。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/StickS3-ESP-Claw-tutorial_055.png" width="80%" />

#>说明|1.详细的 Web 配置以及上手流程介绍可参见[ESP‑Claw 官方教程](https://esp-claw.com/zh-cn/tutorial/web-config/)。<br>2.使用阿里云模型服务时，需完成阿里云账号实名认证。

3. 配置 ClawBot 聊天接口，如 QQ。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/StickS3-ESP-Claw-tutorial_06.png" width="80%" />

4. 单击页面底部的`Save Changes`保存配置。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/StickS3-ESP-Claw-tutorial_07.png" width="80%" />

5. 重启 StickS3 设备，配置完成。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/StickS3-ESP-Claw-tutorial_09.png" width="40%" />

配置完成后，即可使用 ESP-Claw 实现硬件编程、自动化控制、本地 AI 运行等各类任务。

示例：ESP-Claw 支持通过即时通讯工具（如 QQ）接入，用户可像和普通好友聊天一样发送指令。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/StickS3-ESP-Claw-tutorial_08.png" width="70%" />

## 相关视频

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/ESP-Claw-ZH.mp4" type="video/mp4"></video>