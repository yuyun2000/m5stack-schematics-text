# AtomS3R-M12 火山引擎语音助手

\#> 案例说明 | 本教程将使用[AtomS3R-M12 火山引擎语音视觉套件](/zh_CN/core/AtomS3R-M12%20Volcengine%20Kit), 通过 M5Burner 烧录火山引擎语音助手测试固件，构建个人语音助手应用。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1146/D062-M12_01.jpg" width="40%" />

## 1. 准备工作

请根据您所使用的操作系统，点击下方按钮下载相应的 M5Burner 固件烧录工具，解压打开应用程序。

| 软件版本         | 下载链接                                                                        |
| ---------------- | ------------------------------------------------------------------------------- |
| M5Burner_Windows | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-beta-win-x64.zip)   |
| M5Burner_MacOS   | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-mac-x64.dmg)        |
| M5Burner_Linux   | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-beta-linux-x64.zip) |

## 2. 固件烧录

1. 双击打开 Burner 烧录工具，在左侧菜单中选择对应的设备类型`AtomS3`后，再勾选界面上方的`Only Official`选项，找到`AtomS3R-M12火山引擎语音助手`固件进行下载。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/683/M12_04.jpg" width="100%" />

2. 设备连接 USB 后，长按复位按键（大约 2 秒）直到内部绿色 LED 灯亮起，便可松开，此时设备已进入下载模式，等待烧录。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3R-M12/download%20mode.gif" width="30%" />

3. 在 Burner 工具界面单击`Burn`，在弹出的窗口中选择设备对应的端口。点击`Start`, 等待烧录完成。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1146/M12_02.jpg" width="80%" />

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1146/M12_06.jpg" width="80%" />

## 3. 热点配置

使用手机开启 2.4GHz 热点，设置热点的名称为`M5VolcRTC`，密码为`m5volcrtc`。设备成功联网后，即可进行语音交互。

## 4. 开始使用

完成上述配置后，即可开始对话。可通过串口（115200bps）查看实时状态与日志。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1146/M12_07.jpg" width="80%" />

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1146/M12_08.jpg" width="80%" />
