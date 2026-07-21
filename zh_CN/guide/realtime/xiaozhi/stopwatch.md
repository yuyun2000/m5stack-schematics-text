# StopWatch 小智语音助手

本教程将使用 StopWatch 开发板，通过 M5Burner 烧录小智语音助手固件，构建个人语音助手应用。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1242/stopwatch-Xiaozhi_Cover_01.jpg" width="60%">

## 1. 准备工作

请根据您所使用的操作系统，点击下方按钮下载相应的 M5Burner 固件烧录工具，并解压打开应用程序。

| 软件版本         | 下载链接                                                                        |
| ---------------- | ------------------------------------------------------------------------------- |
| M5Burner_Windows | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-beta-win-x64.zip)   |
| M5Burner_MacOS   | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-mac-x64.dmg)        |
| M5Burner_Linux   | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-beta-linux-x64.zip) |

## 2. 固件烧录

1. 双击打开 Burner 烧录工具，在左侧菜单中选择设备类型`STOPWATCH`，点击`Download`下载 StopWatch 小智语音助手。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1242/stopwatch_xiaozhi_tutorial_01.jpg" width="80%">

2. 将设备通过 USB Type-C 数据线连接至电脑，长按复位按键（大约 2 秒）直到绿色 LED 灯亮起，便可松开，此时设备已进入下载模式，等待烧录。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1242/C132-download-mode.gif" width="40%">

3. 单击`Burn`，选择设备对应的端口后，单击`Start`，等待烧录完成。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1242/stopwatch_xiaozhi_tutorial_04.jpg" width="80%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1242/stopwatch_xiaozhi_tutorial_05.jpg" width="80%">

## 3.Wi-Fi 配置

1. 设备启动后，将提示连接 AP 热点。可在手机/电脑连接热点**Xiaozhi-xxx**，或者访问`192.168.4.1`进入网络配置页面。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1242/C152-xiaozhi_tutorial_06.jpg" width="50%">

2. 根据页面提示完成 Wi-Fi 配置。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1242/C152-xiaozhi_assistant_wifi_config_02.jpg" width="80%">

## 4. 注册小智 AI

1. 访问[小智 AI 控制面板](https://xiaozhi.me/)，注册并登录账号。

2. 获取设备验证码。Wi-Fi 配置成功后，设备会自动播报`请登录到控制面板添加设备，输入验证码xxx`，带有屏幕的设备同时会在屏幕上显示验证码。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1242/C152-xiaozhi_tutorial_07.jpg" width="50%" >

3. 在小智 AI 控制面板，依次单击`控制台` > `添加设备`，并填入设备显示的验证码信息，实现设备绑定。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1214/echo_pyramid_xiaozhi_tutorial_04.png" width="80%" >
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1214/echo_pyramid_xiaozhi_tutorial_05.png" width="80%" >
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1214/echo_pyramid_xiaozhi_tutorial_09.png" width="80%" >

## 5. 开始使用

完成上述配置后，通过唤醒词“你好小智”唤醒，开始对话。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1242/C152-xiaozhi_tutorial_08.jpg" width="50%" >

## 6. 音色切换

小智 AI 提供了一些音色模板，您可以在控制面板中进入`配置角色`页面进行配置。注意：完成配置后需重启设备后生效。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1214/echo_pyramid_xiaozhi_tutorial_10.png" width="80%" >
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1214/echo_pyramid_xiaozhi_tutorial_11.png" width="80%" >
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1214/echo_pyramid_xiaozhi_tutorial_12.png" width="80%" >
