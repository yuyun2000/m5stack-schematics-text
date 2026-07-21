# AtomS3/AtomS3-Lite Arduino 示例程序编译与烧录 

## 1.准备工作

- 1.Arduino IDE安装： 参考[Arduino IDE安装教程](/zh_CN/arduino/arduino_ide)，完成IDE安装。
- 2.板管理安装: 参考[基本环境搭建教程](/zh_CN/arduino/arduino_board)，完成M5Stack板管理安装并选择开发板`M5AtomS3`。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/atoms3/quickstart_arduino_atoms3_select_board.png" width="70%" />

- 3.依赖库安装： 参考[库管理安装教程](/zh_CN/arduino/arduino_library)，完成`M5AtomS3`驱动库安装，并根据提示下载全部依赖库。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/atoms3/quickstart_arduino_atoms3_download_library.png" width="70%" />


## 2.下载模式

- 长按复位按键(大约2秒)直到内部绿色LED灯亮起，便可松开，此时设备已进入下载模式，等待烧录。

### M5AtomS3 / M5AtomS3 Lite

- M5AtomS3

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3/download%20mode1.gif" width="50%">

- M5AtomS3 Lite

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3%20Lite/download%20mode.gif" width="50%">


## 3.端口选择

将设备通过USB线连接至电脑，在设备进入下载模式后， Arduino IDE中可选中对应设备的端口。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/atoms3/quickstart_arduino_atoms3_select_port.png" width="70%" />


## 4.程序编译&烧录

打开驱动库中的案例程序“display”, 点击上传按钮，将自动进行程序编译，与程序烧录。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/atoms3/quickstart_arduino_atoms3_select_demo.png" width="70%" />

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/atoms3/quickstart_arduino_atoms3_select_demoupload.png" width="70%">

效果如下图：

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3/download%20demo.gif" width="30%" />

## 5.相关资源

-  **Github**
   - [M5AtomS3 Library](https://github.com/m5stack/M5AtomS3)

-  **Arduino API & Examples**
    - [Button](/zh_CN/arduino/m5atoms3/button)
    - [Display](/zh_CN/arduino/m5atoms3/display)
    - [IMU](/zh_CN/arduino/m5atoms3/imu)
    - [IR NEC](/zh_CN/arduino/m5atoms3/ir_nec)
    - [LED](/zh_CN/arduino/m5atoms3/lite_led)