# Tab5 Arduino 示例程序编译与烧录

## 1.准备工作

- 1.Arduino IDE安装： 参考[Arduino IDE安装教程](/zh_CN/arduino/arduino_ide)，完成IDE安装。
- 2.板管理安装: 参考[基本环境搭建教程](/zh_CN/arduino/arduino_board)，完成M5Stack板管理安装并选择开发板`M5Tab5`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/quickstart_arduino_tab5_select_board.png" width="70%" />

- 3.依赖库安装： 参考[库管理安装教程](/zh_CN/arduino/arduino_library)，完成`M5Unified`，`M5GFX`驱动库安装，并根据提示安装全部依赖库。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/tab5_arduino_lib_01.png" width="70%" />
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/tab5_arduino_lib_02.png" width="70%" />

?> 依赖库版本 | 由于 Tab5 设备存在多种屏幕驱动芯片型号，为确保设备正常适配，建议更新驱动版本至最新版版本 (M5Unified >= 0.2.17, M5GFX >= 0.2.22)

## 2.下载模式

在已接入 USB 数据线或电池供电的情况下，长按复位按键（约 2 秒），直至内部绿色 LED 指示灯开始快速闪烁，松开按键后，设备即进入下载模式，等待固件烧录。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/download_mode2.gif" width="50%" />

## 3.端口选择

将设备通过USB线连接至电脑，在完成驱动安装后， Arduino IDE中可选中对应设备的端口。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/quickstart_arduino_tab5_selectport.png" width="70%" />


## 4.程序编译&烧录

打开M5GFX驱动库中的案例程序"BarGraph",  点击上传按钮，将自动进行程序编译与烧录。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/quickstart_arduino_tab5_select_demo.png" width="70%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/quickstart_arduino_tab5_select_demoupload.png" width="70%">

效果如下图：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/tab5_arduino_example.jpg" width="50%" />

## 5.相关资源

- Arduino Library
   - [M5Unified](https://github.com/m5stack/M5Unified)
   - [M5GFX](https://github.com/m5stack/M5GFX)
- Arduino API & Examples
   - [IMU](/zh_CN/arduino/m5tab5/imu)
   - [Mic](/zh_CN/arduino/m5tab5/mic)
   - [microSD](/zh_CN/arduino/m5tab5/microsd)
   - [RTC](/zh_CN/arduino/m5tab5/rtc)
   - [Speaker](/zh_CN/arduino/m5tab5/speaker)
   - [Touch](/zh_CN/arduino/m5tab5/touch)
   <!-- - [Wakeup](/zh_CN/arduino/m5tab5/wakeup)  -->
