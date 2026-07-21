# TimerCAM Arduino 示例程序编译与烧录

## 1. 准备工作

- 1.Arduino IDE 安装： 参考[Arduino IDE安装教程](/zh_CN/arduino/arduino_ide)，完成 IDE 安装。
- 2\. 板管理安装：参考[基本环境搭建教程](/zh_CN/arduino/arduino_board)，完成 M5Stack 板管理安装并选择开发板`M5TimerCAM`。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/timercam/quickstart_arduino_timercam_select_board.png" width="70%" />

- 3\. 依赖库安装： 参考[库管理安装教程](/zh_CN/arduino/arduino_library)，完成`Timer-CAM`驱动库安装，并根据提示下载全部依赖库。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/timercam/quickstart_arduino_timercam_download_library.png" width="70%" />

## 2.USB 驱动安装

\#> 驱动程序安装提示 | 将设备连接至 PC，打开设备管理器为设备安装[FTDI驱动](https://ftdichip.com/drivers/vcp-drivers/)。以 win10 环境为例，下载匹配操作系统的驱动文件，并解压，通过设备管理器进行安装。(注：某些系统环境下，需要安装两次，驱动才会生效，未识别的设备名通常为`M5Stack`或`USB Serial`, Windows 推荐使用驱动文件在设备管理器直接进行安装 (自定义更新), 可执行文件安装方式可能无法正常工作)。[点击此处，前往下载FTDI驱动](https://ftdichip.com/drivers/vcp-drivers/)

<div class="product_pic"><img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/ftdi_01.webp"><img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/ftdi_02.webp"><img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/ftdi_03.webp"></div>

\#>MacOS 注意事项 | 对于 MacOS 用户安装前请勾选 `系统偏好设置` - >`安全性与隐私` - >`通用` - >`允许以下位置下载的App` - > `App Store和认可的开发者选项`。

## 3. 端口选择

将设备通过 USB 线连接至电脑，在完成驱动安装后， Arduino IDE 中可选中对应设备的端口。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/timercam/quickstart_arduino_timercam_select_port.png" width="70%" />

## 4. 程序编译 & 烧录

1\. 打开驱动库中的案例程序 “web_cam”

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/timercam/quickstart_arduino_timercam_select_demo.png" width="70%" />

2\. 在代码中填入 WiFi 名称和密码

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/timercam/quickstart_arduino_timercam_select_wifi.png" width="70%" />

3\. 点击上传按钮，将自动进行程序编译，与程序烧录。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/timercam/quickstart_arduino_timercam_select_demoupload.png" width="70%" />

## 5. 程序效果如下

1. 打开串口，按下复位按键，显示 WiFi 已连接，并将 IP 地址复制至浏览器，点击 `Start Stream`。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/timercam/quickstart_arduino_timercam_connect_wifi.png" width="70%" />

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/timercam/quickstart_arduino_timercam_web_select.png" width="70%" />

2. 效果如下：

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/timercam/effect.png" width="70%" />

## 6. 相关资源

- **Github**

  - [TimerCam-Arduino 驱动库](https://github.com/m5stack/TimerCam-arduino)

- **Arduino API & Examples**
  - [Camera](/zh_CN/arduino/m5timer_cam/camera)
  - [Power](/zh_CN/arduino/m5timer_cam/power)
  - [LED](/zh_CN/arduino/m5timer_cam/led)
  - [Wakeup](/zh_CN/arduino/m5timer_cam/wakeup)
