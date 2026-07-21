# StickS3 小智语音助手

本教程将使用[StickS3](/zh_CN/core/StickS3)主控，通过 M5Burner 烧录小智语音助手固件，构建个人语音助手应用。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/sticks3_xiaozhi_cover.jpg" width="60%" />

## 1. 准备工作

请根据您所使用的操作系统，点击下方按钮下载相应的 M5Burner 固件烧录工具，解压打开应用程序。

| 软件版本         | 下载链接                                                                        |
| ---------------- | ------------------------------------------------------------------------------- |
| M5Burner_Windows | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-beta-win-x64.zip)   |
| M5Burner_MacOS   | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-mac-x64.dmg)        |
| M5Burner_Linux   | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-beta-linux-x64.zip) |

## 2. 固件烧录

1. 双击打开 Burner 烧录工具，在左侧菜单中选择对应的设备类型 `STICK`, 点击 `Download` 下载`StickS3 小智语音助手`固件。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/sticks3_operate_01.jpg" width="70%" />

2. 设备连接 USB 线，长按机身侧边复位按键。当设备内部绿色 LED 闪烁时，表示设备已成功进入下载模式。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/stickS3_operate_01.gif" width="50%">

3. 点击`Burn`，选择设备对应的端口后，点击`Start`, 等待烧录完成。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/sticks3_operate_02.jpg" width="70%" />
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/sticks3_operate_03.jpg" width="70%" />

4. 烧录完成后，按下复位键，设备将重新启动，进入配网模式。

## 3.Wi-Fi 配置

1. 在手机连接热点`Xiaozhi-xxxx`，或者访问`192.168.4.1`进入网络配置页面。

2. 根据页面提示完成 Wi-Fi 配置。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/sticks3_operate_13.jpg" width="50%" />

Wi-Fi 配置成功后，设备重新启动，并自动播报 `请登录到控制面板添加设备，输入验证码xxxxxx`。也可以通过串口日志的方式查看设备的验证码。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/sticks3_operate_14.jpg" width="70%" />

## 4. 注册小智 AI

1. 访问[小智 AI 控制面板](https://xiaozhi.me/), 注册并登录账号。

2. 在小智 AI 控制面板，点击`添加设备`，并填入设备的验证码信息，实现设备绑定。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/sticks3_operate_08.jpg" width="70%" />
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/sticks3_operate_09.jpg" width="70%" />

## 5. 开始使用

完成上述配置后，通过唤醒词 “你好小智” 唤醒，开始对话。

## 6. 音色切换

小智 AI 提供了一些音色模板，你可以在控制面板中进入`配置角色`页面进行配置。完成配置后需重启设备生效。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/sticks3_operate_10.jpg" width="70%" />
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/sticks3_operate_11.jpg" width="70%" />
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/sticks3_operate_12.jpg" width="70%" />
