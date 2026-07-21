# Tab5 Keyboard 用户案例介绍

本教程介绍 Tab5 Keyboard 搭配 Tab5 使用的用户案例，包括固件烧录的方法，以及 USB HID 输出，寄存器显示等功能。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1241/A164_user_demo_doc_01.jpg" width="50%" />

## 固件烧录

1. 请根据您所使用的操作系统，点击下方按钮下载相应的 M5Burner 固件烧录工具，解压打开应用程序。

| 软件版本         | 下载链接                                                                        |
| ---------------- | ------------------------------------------------------------------------------- |
| M5Burner_Windows | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-beta-win-x64.zip)   |
| M5Burner_MacOS   | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-mac-x64.dmg)        |
| M5Burner_Linux   | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-beta-linux-x64.zip) |

2. 双击打开 Burner 烧录工具，在左侧菜单中选择设备类型 `TAB5`, 点击 `Download` 下载`Tab5 Keyboard`出厂程序固件。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/A164_user_demo_doc_02.jpg" width="70%" />

3. 将 Tab5 Keyboard 与 Tab5 正确连接。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1241/A164_operate_01.jpg" width="70%" />

4. 进入 Tab5 下载模式：在已接入 USB Type-C 数据线或电池供电的情况下，长按复位按键（约 2 秒），直至内部绿色 LED 指示灯开始快速闪烁，松开按键后，设备即进入下载模式，等待固件烧录。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1241/tab5-keyboard-download-mode.gif" width="40%">

5. 将 Tab5 通过 USB 线连接至电脑，在 M5Burner 中点击对应固件的`Burn` 按钮，选择对应设备端口后，单击`Start`，开始烧录。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/A164_user_demo_doc_03.jpg" width="70%" />

6. 当提示 `Burn successfully, click here to return` 时，表示烧录成功。此时需重启设备，使烧录信息生效。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/A164_user_demo_doc_04.jpg" width="70%" />

出厂程序界面：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1241/tab5-keyboard-menu.jpg" width="70%" />

## Demo 介绍

在 Demo 的初始界面共包含五个功能菜单，分别为：

- Normal：普通模式，该模式下按下按键会显示按键所在的行列坐标
- String：字符模式，返回按下的一般按键的名称字符串、Ctrl/Alt 修饰符状态，Sym/Aa 直接实现相应功能。
- HID：HID 模式下，Tab5 Keyboard 可作为 USB 键盘输出按键信号，和手机、电脑等设备通信。
- REGISTRY：寄存器显示界面
- FACTORY：键盘功能测试界面

### HID 模式

在 HID 功能页面，可以把 Tab5 Keyboard 作为 USB HID 设备，给手机、电脑、平板等设备输入信号。包含以下两种模式：
- USBC OTG (FS)：可将 Tab5 通过 USB-C 接口直连电脑、手机等移动设备，作为 USB 键盘使用。
- USB2.0 PHY (HS)：可将 Tab5 通过 USB-A 接口直连电脑，作为电脑键盘使用。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1241/tab5-keyboard-HID.jpg" width="70%" />

### HID 模式使用方法

- USBC OTG (FS)模式：在 HID 界面将键盘模式设置为`USBC OTG (FS)`后， 用 USB Type-C 线，把 Tab5（带键盘）连接到电脑、手机平板等设备上，点击屏幕上的`Start HID`后，按下键盘按键，即可直接输入文字。
- USB2.0 PHY (HS)模式：在 HID 界面将键盘模式设置为`USB2.0 PHY (HS)`后，用 USB Type-A 公对公数据线将 Tab5（带键盘）连接到电脑，点击屏幕上的`Start HID`，此时按下键盘上的按键，就会像普通键盘一样输入字符。