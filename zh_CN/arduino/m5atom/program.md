# Atom-Lite/Matrix Arduino 示例程序编译与烧录

## 1. 准备工作

- 1\.Arduino IDE安装： 参考[Arduino IDE安装教程](/zh_CN/arduino/arduino_ide)，完成IDE安装。
- 2\.板管理安装: 参考[基本环境搭建教程](/zh_CN/arduino/arduino_board)，完成M5Stack板管理安装并选择开发板`M5Atom`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1228/quickstart_arduino_atom_select_board.png" width="70%" />

- 3\.依赖库安装： 参考[库管理安装教程](/zh_CN/arduino/arduino_library)，完成`M5Unified`，`M5GFX`驱动库安装，并根据提示安装全部依赖库。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1228/Atom_arduino_lib_01.png" width="70%" />
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1228/Atom_arduino_lib_02.png" width="70%" />

## 2. USB 驱动安装

#>驱动程序安装提示 | 将设备连接至PC，打开设备管理器为设备安装 [FTDI驱动](https://ftdichip.com/drivers/vcp-drivers/)。请下载匹配操作系统的驱动文件并解压，通过设备管理器进行安装。(注:某些系统环境下,需要安装两次，驱动才会生效，未识别的设备名通常为 `M5Stack` 或 `USB Serial`，Windows 推荐使用驱动文件在设备管理器直接进行安装（自定义更新），可执行文件安装方式可能无法正常工作)。

[FTDI VCP 驱动下载页面：](https://ftdichip.com/drivers/vcp-drivers/)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1228/VCP_Drivers.png" width="80%">

**安装方法：**

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1040/U082-X-USB-note-01.png" width="100%">

#>MacOS注意事项|对于MacOS用户安装前请勾选 `系统偏好设置` - >`安全性与隐私` - >`通用` - >`允许以下位置下载的App` - > `App Store和认可的开发者选项`。

## 3. 端口选择

将设备通过 USB 线连接至电脑，在完成驱动安装后， Arduino IDE 中可选中对应设备的端口。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1228/quickstart_arduino_atom_select_port.png" width="70%" />

## 4. 程序编译 & 烧录

打开驱动库中的案例程序“LogOutput”, 将 `Tools -> Core Debug Level` 设置为 `Info`，点击上传按钮，将自动进行程序编译与程序烧录。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1228/quickstart_arduino_atom_select_demo.png" width="70%" />
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1228/quickstart_arduino_atom_select_info.png" width="70%" />
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1228/quickstart_arduino_atom_select_demoupload.png" width="70%">

串口输出示例如下：

```
 [0;31mM5.Log error log [0m
 [0;33mM5.Log warn log [0m
 [0;32mM5.Log info log [0m
 [0;36mM5.Log debug log [0m
 [0;37mM5.Log verbose log [0m
 [0;31m[   386][E][LogOutput.ino:63] setup(): M5_LOGE error log [0m
 [0;33m[   393][W][LogOutput.ino:64] setup(): M5_LOGW warn log [0m
 [0;32m[   399][I][LogOutput.ino:65] setup(): M5_LOGI info log [0m
 [0;36m[   404][D][LogOutput.ino:66] setup(): M5_LOGD debug log [0m
 [0;37m[   411][V][LogOutput.ino:67] setup(): M5_LOGV verbose log [0m
M5.Log.printf non level output
 [0;33m[  1407][W][LogOutput.ino:79] loop(): BtnA 1 click [0m
 [0;37m[  1443][V][LogOutput.ino:93] loop(): count:1 [0m
 [0;37m[  2467][V][LogOutput.ino:93] loop(): count:2 [0m
 [0;37m[  3491][V][LogOutput.ino:93] loop(): count:3 [0m
 [0;37m[  4515][V][LogOutput.ino:93] loop(): count:4 [0m
 [0;37m[  5539][V][LogOutput.ino:93] loop(): count:5 [0m
 [0;37m[  6563][V][LogOutput.ino:93] loop(): count:6 [0m
......
```

## 5. 相关资源

- **Github**
  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5GFX](https://github.com/m5stack/M5GFX)

- **Arduino API & Examples**
   - [Button](/zh_CN/arduino/m5atom/button)
   - [RGB LED](/zh_CN/arduino/m5atom/rgb)
   - [IMU](/zh_CN/arduino/m5atom/imu)
   - [IR NEC](/zh_CN/arduino/m5atom/ir_nec)
