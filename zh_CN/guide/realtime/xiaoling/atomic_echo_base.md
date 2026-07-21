# AtomS3R 小聆语音助手

本教程将使用 AtomS3R 设备 + [Atomic Voice Base](/zh_CN/atom/Atomic%20Echo%20Base)硬件组合，通过 M5Burner 烧录小聆语音助手固件，构建个人语音助手应用。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/903/atomic-echo-base-xiaoling-10.jpg" width="50%" />

## 1. 准备工作

请根据您所使用的操作系统，点击下方按钮下载相应的 M5Burner 固件烧录工具，并解压打开应用程序。

| 软件版本         | 下载链接                                                                        |
| ---------------- | ------------------------------------------------------------------------------- |
| M5Burner_Windows | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-beta-win-x64.zip)   |
| M5Burner_MacOS   | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-mac-x64.dmg)        |
| M5Burner_Linux   | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-beta-linux-x64.zip) |

## 2. 固件烧录

1. 双击打开 Burner 烧录工具，在左侧菜单中选择对应的设备类型`ATOMS3`，单击`Download`下载`AtomS3R小聆语音助手`固件。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/903/atomic-echo-base-xiaoling-01.jpg" width="80%" />

2. 设备连接 USB 后，长按复位按键（大约 2 秒）到内部绿色 LED 灯亮起，便可松开，此时设备已进入下载模式，等待烧录。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/680/AtomS3R_download_mode.gif" width="40%">

3. 单击`Burn`，选择设备对应的端口后，单击`Start`，等待烧录完成。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/903/atomic-echo-base-xiaoling-02.jpg" width="80%" />
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/903/atomic-echo-base-xiaoling-03.jpg" width="80%" />

## 3.Wi-Fi 配置

1. 设备启动后，将提示连接 AP 热点，可在手机连接热点**Xiaozhi-xxx**，或者访问`192.168.4.1`进入网络配置页面。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/903/atomic-echo-base-xiaoling-04.jpg" width="60%" />

2. 根据页面提示完成 Wi-Fi 配置。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/903/atomic-echo-base-xiaoling-05.jpg" width="60%" />

Wi-Fi 配置成功后，小聆语音助手即进入聆听状态，此时可进行对话。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/903/atomic-echo-base-xiaoling-02.gif" width="60%" />

## 4. 绑定微信小程序

1. 获取设备验证码。Wi-Fi 配置成功后，设备会自动播报`请登录到控制面板添加设备，输入验证码xxx`。

2. 在微信搜索小程序`小聆语音助手`，选中`开源套件`，输入设备播报的验证码，并根据界面提示登录后，即可绑定设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/903/atomic-echo-base-xiaoling-06.jpg" width="60%" />

绑定小程序后，可以查看历史对话信息。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/903/atomic-echo-base-xiaoling-09.jpg" width="60%" />

## 5. 设备解绑

在`小聆语音助手`小程序界面点击`设置` → `解除绑定` → `确认`后，即可解绑设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/903/atomic-echo-base-xiaoling-08.jpg" width="60%" />
