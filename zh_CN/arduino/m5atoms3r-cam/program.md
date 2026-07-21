# AtomS3R-CAM Arduino示例程序编译与烧录

## 1.准备工作

- 1.**Arduino IDE安装**：参考[Arduino IDE安装教程](/zh_CN/arduino/arduino_ide)，完成IDE安装。
- 2.**板管理安装**：参考[基本环境搭建教程](/zh_CN/arduino/arduino_board)，完成M5Stack板管理安装并选择开发板`M5AtomS3R`。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/atoms3r/quickstart_arduino_atoms3r_select_board.png" width="70%" />

- 3.**依赖库安装**：参考[库管理安装教程](/zh_CN/arduino/arduino_library)，完成`M5AtomS3`驱动库安装，并根据提示下载全部依赖库。(AtomS3R-CAM可直接使用`M5AtomS3`驱动库)

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/atoms3r/quickstart_arduino_atoms3r_download_library.png" width="70%" />

## 2.下载模式

长按复位按键(大约2秒)直到内部绿色LED灯亮起，便可松开，此时设备已进入下载模式，等待烧录。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/681/AtomS3R-CAM_download_mode.gif" width="30%">

## 3.端口选择

将设备通过USB线连接至电脑，在设备进入下载模式后，Arduino IDE中可选中对应设备的端口。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/atoms3r/quickstart_arduino_atoms3r_select_port.png" width="70%" />

## 4.程序编译&烧录

打开驱动库中的案例程序`camera`，确认宏定义为`USE_ATOMS3R_CAM`，修改你想要连接的无线网络名称及密码。点击上传按钮，程序将开始编译与烧录。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/681/M5AtomS3R-CAM_Arduino_example_zh_1.png" width="50%" />

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/681/M5AtomS3R-CAM_Arduino_example_zh_2.png" width="50%" />

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/681/M5AtomS3R-CAM_Arduino_example_zh_3.png" width="50%" />

烧录完成后打开右上角的串口监视器，等待设备连接网络。如果没有出现 IP 地址，可以短按一次设备侧边的按钮，让程序重新运行。出现 IP 地址后，在同一网络下的计算机的浏览器中输入这个 IP 地址，即可看到实时传输的画面流。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/681/M5AtomS3R-CAM_Arduino_example_zh_4.png" width="70%" />

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/681/M5AtomS3R-CAM_Arduino_example_zh_5.png" width="70%" />

效果如下图：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/681/M5AtomS3R-CAM_Arduino_example_zh_6.png" width="50%" />

## 5.相关资源

- **Github**
    - [M5AtomS3 Library](https://github.com/m5stack/M5AtomS3)

- **Arduino API & Examples**
    - [IMU](/zh_CN/arduino/m5atoms3/imu)
    - [IR NEC](/zh_CN/arduino/m5atoms3/ir_nec)