# StickC-Plus Arduino 示例程序编译与烧录

## 1.准备工作

- 1.Arduino IDE安装： 参考[Arduino IDE安装教程](/zh_CN/arduino/arduino_ide)，完成IDE安装。
- 2.板管理安装: 参考[基本环境搭建教程](/zh_CN/arduino/arduino_board)，完成M5Stack板管理安装并选择开发板`M5StickC Plus`。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/m5stickc_plus/quickstart_arduino_stickcplus_select_board.png" width="70%" />

- 3.依赖库安装： 参考[库管理安装教程](/zh_CN/arduino/arduino_library)，完成`M5StickC Plus`驱动库安装，并根据提示下载全部依赖库。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/m5stickc_plus/quickstart_arduino_stickcplus_download_library.png" width="70%" />


## 2.USB驱动安装

#>驱动程序安装提示|将设备连接至PC，打开设备管理器为设备安装[FTDI驱动](https://ftdichip.com/drivers/vcp-drivers/)。以win10环境为例,下载匹配操作系统的驱动文件, 并解压,通过设备管理器进行安装。(注:某些系统环境下,需要安装两次,驱动才会生效,未识别的设备名通常为`M5Stack`或`USB Serial`, Windows推荐使用驱动文件在设备管理器直接进行安装(自定义更新), 可执行文件安装方式可能无法正常工作)。[点击此处，前往下载FTDI驱动](https://ftdichip.com/drivers/vcp-drivers/)

<div class="product_pic"><img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/ftdi_01.webp"><img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/ftdi_02.webp"><img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/ftdi_03.webp"></div>

#>对于MacOS用户安装前请勾选 `系统偏好设置` - >`安全性与隐私` - >`通用` - >`允许以下位置下载的App` - > `App Store和认可的开发者选项`。

## 3.端口选择

将设备通过USB线连接至电脑，在完成驱动安装后， Arduino IDE中可选中对应设备的端口。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/m5stickc_plus/quickstart_arduino_stickcplus_select_port.png" width="70%" />


## 4.程序编译&烧录

打开驱动库中的案例程序“Display”, 点击上传按钮，将自动进行程序编译，与程序烧录。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/m5stickc_plus/quickstart_arduino_stickcplus_select_demo.png" width="70%" />

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/m5stickc_plus/quickstart_arduino_stickcplus_select_demoupload.png" width="70%">

效果如下图：

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5StickC%20PLUS2/M5PPT%20(810%20x%201080%20%E5%83%8F%E7%B4%A0).gif" width="30%" />

## 5.相关资源

-  **Github**
   - [M5StickC-Plus Library](https://github.com/m5stack/M5StickC-Plus)

-  **Arduino API & Examples**
    - [Button](/zh_CN/arduino/m5stickc_plus/button)
    - [Buzzer](/zh_CN/arduino/m5stickc_plus/buzzer)
    - [Display](/zh_CN/arduino/m5stickc_plus/display)
    - [Power](/zh_CN/arduino/m5stickc_plus/power)
    - [IMU](/zh_CN/arduino/m5stickc_plus/imu)
    - [Mic](/zh_CN/arduino/m5stickc_plus/mic)