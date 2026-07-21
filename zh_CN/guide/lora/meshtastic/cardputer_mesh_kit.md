# 通过 Cardputer Mesh Kit 使用 Meshtastic

## 前言

**Cardputer Mesh Kit**是一款集便携卡片电脑与远距离通信、全球定位功能于一体的堆叠式组合套装，包含 **Cardputer-Adv** 核心主控与 **Cap LoRa-1262** 通信拓展模块。本教程介绍通过 Cardputer Mesh Kit 使用 Meshtastic 的方法。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1240/K152-Cardputer-Mesh-Kit-main-pictures_13.jpg" width="40%">

## 1.Meshtastic 介绍

详见 [通过 M5Stack 产品使用 Meshtastic](/zh_CN/guide/lora/meshtastic/start) 及 [Meshtastic 官网](https://meshtastic.org/)。

## 2.准备工作

### 硬件准备

- [Cardputer Mesh Kit](https://shop.m5stack.com/products/cardputer-mesh-kit-for-meshtastic-esp32-s3)
- Android / iOS 系统的智能手机
- Windows / macOS / Linux 系统的电脑

!> 安全提醒 | 请不要在没有安装天线的情况下连接 / 打开设备电源，否则设备硬件可能会永久损坏！

### 安装 M5Burner

M5Burner 是 M5Stack 推出的统一固件烧录工具，通过该工具用户可以很方便地给各种设备烧录各种固件。

根据电脑的操作系统，点击下方链接下载并安装对应的 M5Burner 固件烧录工具。

| 软件版本         | 下载链接                                                                        |
| ---------------- | ------------------------------------------------------------------------------- |
| M5Burner_Windows | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-beta-win-x64.zip)   |
| M5Burner_macOS   | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-mac-x64.dmg)        |
| M5Burner_Linux   | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-beta-linux-x64.zip) |

### 给主控刷入固件

#> 操作顺序 | 在给 Cardputer-Adv 刷入固件前，不建议连接 Cap LoRa-1262。

打开 M5Burner，选择左侧设备列表底部的 ALL，在顶部搜索框输入 "Meshtastic"，选择搜索结果中与 Cardputer-Adv 对应的固件，点击 `Download`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/Meshtastic_01burner.png" width="70%">

将 Cardputer-Adv 上侧面的开关置于 OFF，按住旁边的 G0 按键，通过 USB-C 数据线连接至电脑后松开按键，设备将进入下载模式。点击 `Burn`，选择对应的 USB 端口、波特率 1500000，点击 `Start` 开始刷入。等待显示 `Burn successfully, click here to return` 按钮即可点击，固件刷入完成，断开 Cardputer-Adv 与电脑的连接。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/Meshtastic_02burner.png" width="70%">

如果刷入过程中遇到问题，电脑可能需要安装 USB 驱动，有关操作请参考 [Cardputer-Adv 的产品文档页面](/zh_CN/core/Cardputer-Adv)。

### 安装并启动设备

将 Cap LoRa-1262 随附的天线安装到位，然后安装到 Cardputer-Adv 上。确保安装正确且紧密后，将上侧面的开关置于 ON 或连接 USB-C 线给设备供电。
设备启动后会弹出欢迎界面，按 ↩️ 回车键进入 Set the LoRa region 界面，需要根据硬件种类设定地区参数（本例为 EU_868），操作方式是**短按设备上侧面的 G0 按钮**滚动到下一个选项，**长按 G0 按钮**确认选择。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/welcome.jpg" width="70%">

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/Meshtastic_03SetRegion.jpg" width="70%">

确认选择后设备会重启，屏幕显示启动画面，包含 Meshtastic 的 "//\\" 图标、左上角地区参数、右上角固件版本和本机短名称（4 位字母数字编码），然后进入主界面。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/Meshtastic_04deviceLogo.jpg" width="70%">

### 绑定手机、修改名称

根据手机的操作系统，从下列渠道下载并安装 Meshtastic app。

- [Meshtastic 官网下载页](https://meshtastic.org/downloads/)
- iOS - [App Store](https://apps.apple.com/cn/app/meshtastic/id1586432531)
- Android - [Google Play](https://play.google.com/store/apps/details?id=com.geeksville.mesh) 或者 [从GitHub下载APK文件](https://github.com/meshtastic/Meshtastic-Android/releases/latest)

Meshtastic app 的 iOS 版和 Android 版功能基本相同但界面差异巨大，所以这里分别提供操作步骤和截图。应用功能与界面随时可能更新，以下说明仅供参考，请以最新版 app 实际操作为准。

<TabPanel>
  <template #tab-iOS>
    <p>打开 Meshtastic app，授予蓝牙等权限后，会进入 Bluetooth 页面并显示手机扫描到的附近节点。如果附近有多个节点，你可以查看设备屏幕右上角显示的四位编码。在手机上点击扫描结果中与设备对应的四位编码，把设备上显示的六位蓝牙配对码输入手机，即可将设备与手机绑定。</p>
    <img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/iOS_setup.webp" width="75%">
    <p>Meshtastic 中默认用于区分不同节点设备的是不易记住的四位编码，我们可以设定用户名，在设备管理和通信中可以更直观地区分。</p>
    <p>在 Meshtastic app 的 Settings 页面中下滑点击 User，输入长名称和短名称。点击底部的 Save 把修改的设置保存到设备。</p>
    <p>短名称最多四个字符，用于显示在头像中。</p>
    <img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/639/iOS_username.webp" width="50%">
  </template>
  <template #tab-Android>
    <p>打开 Meshtastic app，查看应用介绍并点击右下角的 ">" 按钮，进入 Node Settings 页面。点击 "+" 按钮，授予蓝牙权限后，手机会扫描附近的节点。如果附近有多个节点，你可以查看设备屏幕右上角显示的四位编码。在手机上点击扫描结果中与设备对应的四位编码，把设备上显示的六位蓝牙配对码输入手机，即可将设备与手机绑定。</p>
    <img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/Android_setup.webp" width="75%">
    <p>Meshtastic 中默认用于区分不同节点设备的是不易记住的四位编码，我们可以设定用户名，在设备管理和通信中可以更直观地区分。</p>
    <p>在 Meshtastic app 的 Node Settings 页面点击右上角三点菜单中的 Radio configuration，点击 User，输入长名称和短名称。点击底部的 Send 把修改的设置发送到设备。</p>
    <p>短名称最多四个字符，用于显示在头像中。</p>
    <img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/639/Android_username.webp" width="50%">
  </template>
</TabPanel>

到此就完成了所有的准备工作，可以开始日常使用。

?> 注意 | ESP32-S3 芯片运行 Meshtastic 固件时，蓝牙和 WiFi 无法同时使用。设备默认启用蓝牙，未启用 Wi-Fi。如果手动修改配置启用了 Wi-Fi，则设备无法通过蓝牙连接到手机。这种情况下可以将设备通过 USB 数据线连接到电脑，使用 Chrome 浏览器打开 [Meshtastic Web Client](https://client.meshtastic.org/) 禁用 Wi-Fi，蓝牙将会自动重新启用。

## 3.功能使用

### 手机 app

Meshtastic 手机 app 与常见的即时通讯软件类似，可以收发频道（相当于群聊）和私聊消息，可以创建、分享（邀请）、加入频道。

有关手机 app 的详细说明，请见 Meshtastic 官方文档：

- [iOS App Usage](https://meshtastic.org/docs/software/apple/usage/)
- [Android App Usage](https://meshtastic.org/docs/software/android/usage/)

### 位置信息

Cap LoRa-1262 搭载了 GNSS / GPS，可在 Meshtastic 手机 app 的 Mesh Map / Map 页面查看附近各个 Meshtastic 设备的位置，在户外等场景中方便队友之间互相查看位置。

### 设备操作

Cardputer-Adv 搭载全键盘，支持输入文字，本机固件也带有消息收发等基础功能。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/Meshtastic_05Page.jpg" width="70%">

上图为主界面，底部图标默认隐藏。**短按 G0 按键**可向右切换页面，**短按键盘右上角的 ⬅️ 退格键**可向左切换页面。页面从左到右依次为：

- **主页**：显示附近在线节点数量及最近上线时间、GNSS / GPS 卫星数量、ChUtil 频道占用率、本设备长短名称等信息。
- **最近消息页**：显示最近收到消息的时间、发信人、消息内容。
- **节点信号页**：显示附近在线节点的信号信息，包括短名称、最近上线时间、距离、信号强度等。
- **节点方向页**：显示附近在线节点的方向信息，即以本节点为中心，其他节点相对于正北方向的顺时针角度。
- **位置信息页**：显示本机通过 GNSS / GPS 获取到的信息，包括日期、经纬度、海拔高度、指北针等。
- **LoRa 信息页**：显示本机 LoRa 配置信息，包括地区、预设、具体频率、频道占用率等。
- **内存占用页**：显示本机 Heap Memory 堆内存和 Flash Storage 闪存的占用情况、固件版本、运行时长。
- **当前时间页**：显示当前时分秒，只有通过蓝牙连接手机或者 GNSS / GPS 有信号时才会显示。
- **具体节点页**：用一个页面显示附近单个在线节点的信息，此页面可能有多个。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/Meshtastic_06Menu.jpg" width="70%">

如上图所示，在不同页面**长按 G0** 或**短按 ↩️ 回车键**可调出对应的菜单，在菜单中**短按 G0** 滚动到下一个选项，**长按 G0** 或**短按 ↩️ 回车键**确认选择。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/Meshtastic_13Message.jpg" width="70%">

上图展示了消息接收和回复的操作，回复时可选择预设消息或自由输入文字。预设消息可在手机 app 中修改，自由输入文字后**短按 ↩️ 回车键**发送。

在主界面的任意页面直接按键盘上的字母 / 数字 / 符号键，也可以快速自由输入文字。输入文字时**短按 Aa 键**切换大写锁定，**短按 ⬅️ 退格键**删除左侧一个字符。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/Meshtastic_10Destination.jpg" width="70%">

如上图所示，在文字输入页面**短按 tab 键**显示可发送的频道（群聊）或节点（私聊），**短按 G0** 滚动到下一个选项，**长按 G0** 或**短按 ↩️ 回车键**确认选择。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/Meshtastic_12Emoji.jpg" width="70%">

固件还支持显示某些 Emoji 哦 😀

## 4.相关链接

<!--
- [M5Stack Meshtastic Firmware](https://github.com/m5stack/meshtastic-firmware)
-->
- [Meshtastic 官网](https://meshtastic.org/)
- [Meshtastic 文档](https://meshtastic.org/docs/introduction/)

## 5.相关视频

Coming soon...