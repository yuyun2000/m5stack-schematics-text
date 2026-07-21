# PaperS3 Arduino 示例程序编译与烧录

## 1.准备工作

- 1.Arduino IDE安装：参考[Arduino IDE安装教程](/zh_CN/arduino/arduino_ide)，完成IDE安装。

- 2.板管理安装：参考[基本环境搭建教程](/zh_CN/arduino/arduino_board)，完成M5Stack板管理安装并选择开发板 `M5PaperS3`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/517/PaperS3_Arduino_board.png" width="70%"/>

- 3.依赖库安装：参考[库管理安装教程](/zh_CN/arduino/arduino_library)，完成最新版 `M5Unified`、`M5GFX` 驱动库安装，并根据提示安装全部依赖库。

#> M5Unified 版本 >= `0.2.5`，M5GFX 版本 >= `0.2.7`。在旧版 M5Unified、M5GFX 时需要手动额外安装的 `epdiy` 库现已不再需要。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/m5papers3/lib_01.jpg" width="70%"/>
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/m5papers3/lib_02.jpg" width="70%"/>

## 2.下载模式

将设备通过USB线连接至电脑, 长按M5PaperS3上的电源按键, 当背部状态灯红色闪烁时表示设备已进入下载模式。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/PaperS3/download.gif" width="30%"/>

## 3.端口选择

等待设备识别端口成功，在Arduino IDE中选中对应设备的端口。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/517/PaperS3_Arduino_port.png" width="70%"/>

## 4.程序编译&烧录

打开 `M5GFX` 驱动库中的案例程序 `BarGraph`，点击上传按钮，程序将开始编译与烧录。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/m5papers3/bar_example_01.jpg" width="70%"/>
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/m5papers3/bar_example_03.jpg" width="70%"/>

## 5.相关资源

- **GitHub**
  - [M5Unified Library](https://github.com/m5stack/M5Unified)
  - [M5GFX Library](https://github.com/m5stack/M5GFX)

- **Arduino API & Examples**
  - [Battery](/zh_CN/arduino/m5papers3/battery)
  - [Buzzer](/zh_CN/arduino/m5papers3/buzzer)
  - [IMU](/zh_CN/arduino/m5papers3/imu)
  - [RTC](/zh_CN/arduino/m5papers3/rtc)
  - [SD Card](/zh_CN/arduino/m5papers3/sdcard)
  - [Touch](/zh_CN/arduino/m5papers3/touch)
  - [Wakeup](/zh_CN/arduino/m5papers3/wakeup)