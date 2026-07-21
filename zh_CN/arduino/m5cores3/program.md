# CoreS3 Arduino 示例程序编译与烧录

## 1.准备工作

- 1.Arduino IDE安装： 参考[Arduino IDE安装教程](/zh_CN/arduino/arduino_ide)，完成IDE安装。
- 2.板管理安装: 参考[基本环境搭建教程](/zh_CN/arduino/arduino_board)，完成M5Stack板管理安装并选择开发板`M5CoreS3`。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/m5cores3/quickstart_arduino_cores3_select_board.png" width="70%" />

- 3.驱动库安装：参考[库管理安装教程](/zh_CN/arduino/arduino_library)，完成`M5Unified`、`M5GFX`驱动库安装，并根据提示安装全部依赖库。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_arduino_lib_01.png" width="70%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/cores3_arduino_lib_02.png" width="70%">

## 2.下载模式

- 长按复位按键（大约2秒）直到内部绿色 LED 灯亮起，便可松开，此时设备已进入下载模式，等待烧录。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5CORES3%20SE/cores3%20(2).gif" width="40%">

## 3.端口选择

将设备通过 USB 线连接至电脑，在设备进入下载模式后， Arduino IDE 中可选中对应设备的端口。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/m5cores3/quickstart_arduino_cores3_select_port.png" width="70%" />

## 4.程序编译&烧录

打开驱动库中的案例程序“BarGraph”, 点击上传按钮，将自动进行程序编译，与程序烧录。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/quickstart_arduino_cores3_select_demo.png" width="70%" />

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/quickstart_arduino_cores3_select_demoupload.png" width="70%">

效果如下图：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/quickstart_arduino_cores3_example.jpg" width="40%" />

## 5.相关资源

-  **Github**
   - [M5Unified Library](https://github.com/m5stack/M5Unified)
   - [M5GFX Library](https://github.com/m5stack/M5GFX)

-  **Arduino API & Examples**
   - [Button](/zh_CN/arduino/m5cores3/button)
   - [Camera](/zh_CN/arduino/m5cores3/camera)
   - [Display](/zh_CN/arduino/m5cores3/display)
   - [LTR553](/zh_CN/arduino/m5cores3/ltr553)
   - [Mic](/zh_CN/arduino/m5cores3/mic)
   - [RTC](/zh_CN/arduino/m5cores3/rtc)
   - [SDcard](/zh_CN/arduino/m5cores3/sdcard)
   - [Speaker](/zh_CN/arduino/m5cores3/speaker)
   - [Touch](/zh_CN/arduino/m5cores3/touch)
   - [IMU](/zh_CN/arduino/m5cores3/imu)
   - [Wakeup](/zh_CN/arduino/m5cores3/wakeup)
   - [Power](/zh_CN/arduino/m5cores3/power)