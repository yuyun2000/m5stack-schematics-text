# AtomS3R Arduino示例程序编译与烧录

## 1.准备工作

- 1.**Arduino IDE安装**：参考[Arduino IDE安装教程](/zh_CN/arduino/arduino_ide)，完成 IDE 安装。
- 2.**板管理安装**：参考[基本环境搭建教程](/zh_CN/arduino/arduino_board)，完成 M5Stack 板管理安装并选择开发板`M5AtomS3R`。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/atoms3r/quickstart_arduino_atoms3r_select_board.png" width="70%" />

- 3.驱动库安装：参考[库管理安装教程](/zh_CN/arduino/arduino_library)，完成`M5Unified`、`M5GFX`驱动库安装，并根据提示安装全部依赖库。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/680/atoms3r_arduino_lib_01.png" width="70%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/680/atoms3r_arduino_lib_02.png" width="70%">

?>依赖库版本 | 为确保设备正常适配，建议更新驱动版本至最新版版本（M5unified >= 0.2.17，M5GFX >= 0.2.22）

## 2.下载模式

长按复位按键（大约2秒）直到内部绿色 LED 灯亮起，便可松开，此时设备已进入下载模式，等待烧录。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3R/download%20mode.gif" width="30%">

## 3.端口选择

将设备通过 USB 线连接至电脑，在设备进入下载模式后，Arduino IDE中可选中对应设备的端口。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/680/quickstart_arduino_atoms3r_select_port.png" width="70%" />

## 4.程序编译&烧录

打开驱动库中的案例程序 `BarGraph`, 点击上传按钮，程序将开始编译与烧录。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/680/quickstart_arduino_atoms3r_select_demo.png" width="70%" />
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/680/quickstart_arduino_atoms3r_select_demoupload.png" width="70%" />

效果如下图：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/680/quickstart_arduino_atoms3r_example.jpg" width="30%" />

## 5.相关资源

- **Github**
   - [M5Unified Library](https://github.com/m5stack/M5Unified)
   - [M5GFX Library](https://github.com/m5stack/M5GFX)

- **Arduino API & Examples**
    - [Button](/zh_CN/arduino/m5atoms3r/button)
    - [Display](/zh_CN/arduino/m5atoms3r/display)
    - [IMU](/zh_CN/arduino/m5atoms3r/imu)
    - [IR NEC](/zh_CN/arduino/m5atoms3r/ir_nec)