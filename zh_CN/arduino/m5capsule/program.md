# Capsule Arduino示例程序编译与烧录 

## 1.准备工作

- 1.Arduino IDE安装： 参考[Arduino IDE安装教程](/zh_CN/arduino/arduino_ide)，完成IDE安装。
- 2.板管理安装: 参考[基本环境搭建教程](/zh_CN/arduino/arduino_board)，完成M5Stack板管理安装并选择开发板`M5Capsule`。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/m5capsule/quickstart_arduino_capsule_select_board.png" width="70%" />

- 3.依赖库安装： 参考[库管理安装教程](/zh_CN/arduino/arduino_library)，完成`M5Capsule`驱动库安装，并根据提示下载全部依赖库。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/m5capsule/quickstart_arduino_capsule_download_library.png" width="70%" />


## 2.下载模式

- 上电前按住M5Capsule上的G0按键, 然后连接USB线供电将进入下载模式。

<br/><img alt="schematics" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5Capsule/capsule%20(2).gif" width="70%" />


## 3.端口选择

将设备通过USB线连接至电脑，在设备进入下载模式后， Arduino IDE中可选中对应设备的端口。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/m5capsule/quickstart_arduino_capsule_select_port.png" width="70%" />


## 4.程序编译&烧录

打开驱动库中的案例程序“button”, 点击上传按钮，将自动进行程序编译，与程序烧录。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/m5capsule/quickstart_arduino_capsule_select_demo.png" width="70%" />

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/m5capsule/quickstart_arduino_capsule_select_demoupload.png" width="70%">

上传完成程序，按下按钮，蜂鸣器就会响。

## 5.相关资源

-  **Github**
   - [M5Capsule Library](https://github.com/m5stack/M5Capsule)

-  **Arduino API & Examples**
    - [Buzzer](/zh_CN/arduino/m5capsule/buzzer)
    - [Button](/zh_CN/arduino/m5capsule/button)
    - [RTC](/zh_CN/arduino/m5capsule/rtc)
    - [Wakeup](/zh_CN/arduino/m5capsule/wakeup)

