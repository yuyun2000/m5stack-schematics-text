# StopWatch 恢复出厂固件

\#> 出厂固件 | 当设备出现工作异常时，可尝试重新烧录出厂固件来检验设备硬件是否存在故障。参考以下教程。使用 M5Burner 固件烧录工具，为设备烧录出厂固件。

## 1. 准备工作

- 参考[M5Burner教程](/zh_CN/uiflow/m5burner/intro)完成烧录工具下载，并参考下图，下载对应的固件。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1242/stopwatch_burner_factory_01.jpg" width="80%" />

## 2. 下载模式

将设备通过 USB Type-C 数据线连接至电脑，长按复位按键（大约 2 秒）直到绿色 LED 灯亮起，便可松开，此时设备已进入下载模式，等待烧录。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1242/C132-download-mode.gif" width="35%">

## 3. 固件烧录

1. 在 M5Burner 中点击对应固件的 Burn 按钮。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1242/stopwatch_burner_factory_02.jpg" width="80%" />

2. 选择对应设备端口后，单击`Start`开始烧录。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1242/stopwatch_burner_factory_03.jpg" width="80%" />

烧录完成后界面将显示`Burn successfully, click here to return`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1242/stopwatch_burner_factory_04.jpg" width="80%" />

3. 单击设备的复位按键，设备重启后，效果如下图：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1242/stopwatch_burner_factory_05.jpg" width="40%" />

## 相关参考

StopWatch 出厂固件的具体使用方法，可参见[教程](/zh_CN/guide/display_device/stopwatch/usage)。