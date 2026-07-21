# Module13.2 PPS

## 关于本章

Module13.2 PPS 是一款可编程电源模块。该模块采用 STEP-DOWN 降压技术，支持 DC 9 ~ 36V 宽电压输入。内置 STM32 控制处理器及 AD8418 高分辨率电流放大器，通过高精度闭环控制，实现额定输出功率 100W（峰值 150W）的电流和电压输出，能输出 0.5 ~ 30V/0 ~ 5A，回读精度为正负 30mV/5mA。

本章节介绍使用 Core/Core2/Core3 系列主机，堆叠 Module13.2 PPS 进行额定电流和电压输出的操作方法。

<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Module13.2-PPS/img-654af383-0355-4cf9-a744-2990a360b274.webp" width="30%"><img src="https://static-cdn.m5stack.com/resource/docs/products/module/Module13.2-PPS/img-3ce0f002-8d9b-4e9f-8717-28e7916cc2f1.webp" width="30%">

## 烧录固件

1. 请根据您所使用的操作系统，点击下方按钮下载相应的 M5Burner 固件烧录工具。解压打开应用程序。

| 软件版本         | 下载链接                                                                        |
| ---------------- | ------------------------------------------------------------------------------- |
| M5Burner_Windows | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-beta-win-x64.zip)   |
| M5Burner_MacOS   | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-mac-x64.dmg)        |
| M5Burner_Linux   | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-beta-linux-x64.zip) |

2. 双击打开 Burner 烧录工具，找到对应主机适配的 Module13.2 PPS 的 Demo，Core/Core2/CoreS3 适配的 Demo 分别如下：

- 适配 Core 的 Demo：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/991/PPS_01.jpg" width="70%">

- 适配 Core2 的 Demo：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/991/PPS_02.jpg" width="70%">

- 适配 CoreS3 的 Demo：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/991/PPS_03.jpg" width="70%">

3. 单击`Download`下载主机适配的 Demo。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/991/PPS_04.jpg" width="70%">

4. 将设备通过 USB 线连接至电脑，单击对应 Demo 的`Burn`按钮。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/991/PPS_05.jpg" width="70%">

5. 在弹窗中选择设备对应的端口号后，单击`Start`开始进行烧录。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/991/PPS_06.jpg" width="70%">

完成固件烧录后，设备自动进入电流和电压的设置页面，如下图所示。按任意键即可进入设置模式。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/991/PPS_07.jpg" width="70%">

## 操作说明

电流 / 电压设置界面介绍如下所示。Core 通过设备上的按键进行操作，Core2/CoreS3 通过触摸屏上的按钮进行操作。操作效果都是一致的。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/991/PPS_09.jpg" width="70%">

- 1：设置电压
- 2：设置电流
- 3：切换选项 / 长按表示确定
- 4：数值增加
- 5：数值减少

例如，下图演示的是设置额定的输出电压为 5V，输出电流为 5A，界面上左侧显示设置的额定数值，通过数值增加 / 数值减少的按键设置完成后，长按`ON`确认即可开始输出。右侧`OUTPUT`对应的数值表示设备当前的实际输出电压 / 电流。

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/991/PP2.mp4" type="video/mp4"></video>

?> 注意事项 | 使用 Module13.2 PPS 需要外接 DC 9 ~ 36V 电源，否则会提示无 I2C 设备，设备不工作。输出的最大值取决于输入 DC 电源的输出能力。
