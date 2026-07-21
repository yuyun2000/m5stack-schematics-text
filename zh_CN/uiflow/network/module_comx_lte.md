# Network Over COM.LTE 使用教程

Network Over COM.LTE 模式，可以使得设备在使用 UiFlow 时，所有网络数据经过 LTE 发送。本教程主要介绍设置Network Over COM.LTE 模式的操作方法。

## 1. 准备工作

- 参考[UiFlow Web IDE教程](/zh_CN/uiflow/uiflow_web)，了解使用 UiFlow 的基本流程，并完成 M5Burner 固件烧录工具的安装。
- 通过 M5Burner 烧录使用主控所对应的UiFlow 固件。
- 将 NanoSIM 卡插入模块卡槽。
- 调整拨码开关，并连接好外部天线。当使用 Core1 设备时，请将`引脚13`和`引脚5`的拨码开关调整至`ON`，Core2 则将`引脚16`和`引脚17`的拨码开关调整至`ON`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/942/COMX_01.jpg" width="70%">


## 2. 设置 APN以及切换模式

使用USB线将主控连接至电脑，在 M5Burner 中点击`Configure`选项，在弹出的配置框中，将`COM.X`选项设置为`True`，配置 NanoSIM 卡对应的运营商以及 APN，然后单击`Save`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/942/COMX_02.jpg" width="70%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/942/COMX_04.jpg" width="70%">



## 3. 开始使用

配置完成后，设备开机将会自动启用，并开始检查。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/942/COMX_05.jpg" width="70%">


当设备界面显示`LTE`标识，且云朵图标变成绿色时，表示LTE模式配置成功，设备已连接UiFlow服务器。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/942/COMX_06.jpg" width="70%">
