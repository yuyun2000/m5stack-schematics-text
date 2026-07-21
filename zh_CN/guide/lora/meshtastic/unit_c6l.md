# 通过 Unit C6L 使用 Meshtastic

## 1.Meshtastic 介绍

详见 [通过 M5Stack 产品使用 Meshtastic](/zh_CN/guide/lora/meshtastic/start) 及 [Meshtastic 官网](https://meshtastic.org/)。

## 2.准备工作

### 硬件准备

- [Unit C6L](https://shop.m5stack.com/products/m5stack-c6l-unit-for-meshtastic-sx1262-esp32-c6)
- Android / iOS 系统的智能手机
- Windows / macOS / Linux 系统的电脑

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1185/U202-Unit-C6L_10.webp" width="20%">

!> 安全提醒 | 请不要在没有安装天线的情况下连接 / 打开设备电源，否则设备硬件可能会永久损坏！

### 给主控刷入固件

将 Unit C6L 通过 USB-C 数据线连接至电脑后，长按设备左侧的开关，设备将进入下载模式。使用 Chrome 浏览器打开 [Meshtastic 官方网页烧录器](https://flasher.meshtastic.org/)，点击左侧的`Select Target Device`，然后点击上方的`M5Stack`并选择`M5Stack Unit C6L`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1185/Meshtastic_01flasher.png" width="70%">

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1185/Meshtastic_02device.png" width="70%">

点击网页中间的固件版本按钮，选择最新的 Alpha 版本固件，然后点击`Flash`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1185/Meshtastic_03firmware.png" width="70%">

在弹出的小窗口中滑到底部点击`Continue`，选择 115200 波特率，打开`Full Erase and Install`开关，点击`Erase Flash and Install`按钮。在 Chrome 的弹出菜单中选择对应的 USB 端口，开始刷入。等待按钮文字变成`Start Over`，此时固件刷入完成，可关闭网页。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1185/Meshtastic_04flash.png" width="70%">

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1185/Meshtastic_05finish.png" width="70%">

### 启动设备

断开并重新连接 USB-C 线。设备启动后会显示 LoRa Region 界面，需要根据硬件种类设定地区参数（本例为 US），操作方式是**短按设备正面的按钮**滚动到下一个选项，**长按按钮**确认选择。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1185/Meshtastic_06start.jpeg" width="30%">

确认选择后设备会重启，屏幕显示启动画面，包含 Meshtastic 的 "//\\" 图标、上方地区参数、左下角固件版本、右下角本机短名称（4 位字母数字编码），然后进入主界面。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1185/Meshtastic_07icon.jpeg" width="30%">

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

?> 注意 | ESP32-C6 芯片运行 Meshtastic 固件时，蓝牙和 WiFi 无法同时使用。设备默认启用蓝牙，未启用 Wi-Fi。如果手动修改配置启用了 Wi-Fi，则设备无法通过蓝牙连接到手机。这种情况下可以将设备通过 USB 数据线连接到电脑，使用 Chrome 浏览器打开 [Meshtastic Web Client](https://client.meshtastic.org/) 禁用 Wi-Fi，蓝牙将会自动重新启用。

## 3.功能使用

### 手机 app

Meshtastic 手机 app 与常见的即时通讯软件类似，可以收发频道（相当于群聊）和私聊消息，可以创建、分享（邀请）、加入频道。Unit C6L 没有搭载 GPS，但可以在手机 app 中授权后获得手机的位置信息。

有关手机 app 的详细说明，请见 Meshtastic 官方文档：

- [iOS App Usage](https://meshtastic.org/docs/software/apple/usage/)
- [Android App Usage](https://meshtastic.org/docs/software/android/usage/)

### 设备操作

Unit C6L 固件带有显示最新消息、发送预设短语等基础功能。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1185/Meshtastic_08home.jpeg" width="30%">

上图为主界面，底部图标默认隐藏。**短按正面按键**可向右切换页面，页面从左到右依次为：

- **主页**：显示附近在线节点数量、GNSS / GPS 卫星数量、本设备短名称等信息。
- **最近消息页**：显示最近收到消息的时间、发信人、消息内容。
- **节点信号页**：显示附近在线节点的信号信息，包括短名称、最近上线时间、信号强度、距离等。
- **节点方向页**：显示附近在线节点的方向信息，即以本节点为中心，其他节点相对于正北方向的顺时针角度。
- **位置信息页**：显示本机通过 GNSS / GPS 获取到的信息。由于 Unit C6L 没有搭载 GPS，所以此页面信息为空。
- **LoRa信息页**：显示本机 LoRa 配置信息，包括角色、地区、具体频率等。
- **内存占用页**：显示本机 Heap Memory 堆内存和 Flash Storage 闪存的占用情况、固件版本。
- **当前时间页**：显示当前小时、分钟，只有通过蓝牙连接手机时才会显示。
- **具体节点页**：用一个页面显示附近单个在线节点的信息，此页面可能有多个。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1185/Meshtastic_09menu.jpeg" width="30%">

如上图所示，在不同页面**长按正面按键**可调出对应的菜单，在菜单中**短按正面按键**滚动到下一个选项，**长按正面按键**确认选择。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1185/Meshtastic_10msgOps.jpeg" width="90%">

上图展示了消息接收和回复的操作。回复时可选择预设消息，预设消息可在手机 app 中修改。

## 4.相关链接

- [Meshtastic 官网](https://meshtastic.org/)
- [Meshtastic 文档](https://meshtastic.org/docs/introduction/)

## 5.相关视频

Coming soon...