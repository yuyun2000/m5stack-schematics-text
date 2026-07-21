# CoreS3 小聆语音助手

本教程将使用 CoreS3 主控，通过 M5Burner 烧录小聆语音助手固件，构建个人语音助手应用。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/903/coreS3-xiaoling-06.jpg" width="50%" />

## 1. 准备工作

请根据您所使用的操作系统，点击下方按钮下载相应的 M5Burner 固件烧录工具，并解压打开应用程序。

| 软件版本         | 下载链接                                                                        |
| ---------------- | ------------------------------------------------------------------------------- |
| M5Burner_Windows | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-beta-win-x64.zip)   |
| M5Burner_MacOS   | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-mac-x64.dmg)        |
| M5Burner_Linux   | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-beta-linux-x64.zip) |

## 2. 固件烧录

1. 双击打开 Burner 烧录工具，在左侧菜单中选择对应的设备类型`CORES3`，单击`Download`下载`CoreS3小聆语音助手`固件。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/coreS3-xiaoling-01.jpg" width="80%" />

2. 设备连接 USB 后，长按复位按键（大约 2 秒）到内部绿色 LED 灯亮起，便可松开，此时设备已进入下载模式，等待烧录。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5CORES3%20SE/cores3%20(2).gif" width="40%">

3. 单击`Burn`，选择设备对应的端口后，单击`Start`，等待烧录完成。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/coreS3-xiaoling-02.jpg" width="80%" />
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/coreS3-xiaoling-03.jpg" width="80%" />

## 3. 通过蓝牙配网

1. 设备固件烧录完成后，进入蓝牙配网模式。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_01.png" width="60%" />

2. 使用微信扫描屏幕的二维码，输入 Wi-Fi 名称和密码后，设备开始自动进行配网和绑定。配网成功后，小聆语音助手即进入聆听状态，此时可进行对话。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_03.png" width="60%" />

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_02.png" width="40%" />

## 4. 绑定微信小程序

Wi-Fi 配置成功后，设备会自动绑定到微信小程序`小聆语音助手`，可以在小程序对设备进行配置，以及查看历史对话信息。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/atomic-echo-base-xiaoling-09-20251231.jpg" width="40%" />

## 5. 设备解绑

在`小聆语音助手`小程序界面点击`设置` → `解除绑定` → `确认`后，即可解绑设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/atomic-echo-base-xiaoling-08-20251231.jpg" width="60%" />

设备解绑后，如果需要重新绑定设备，可以重启设备，重启过程中按一下设备屏幕，会重新显示蓝牙配网的界面。
