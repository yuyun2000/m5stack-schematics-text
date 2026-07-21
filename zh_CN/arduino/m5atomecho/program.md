# Atom Voice Arduino 示例程序编译与烧录

## 1. 准备工作

- 1.Arduino IDE 安装： 参考[Arduino IDE安装教程](/zh_CN/arduino/arduino_ide)，完成 IDE 安装。
- 2\. 板管理安装：参考[基本环境搭建教程](/zh_CN/arduino/arduino_board)，完成 M5Stack 板管理安装并选择开发板`M5Atom`(与 M5AtomEcho 使用相同主控)。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/m5echo/quickstart_arduino_echo_select_board.png" width="70%" />

- 3\. 依赖库安装： 参考[库管理安装教程](/zh_CN/arduino/arduino_library)，完成`M5Atom`驱动库安装，并根据提示下载全部依赖库。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/m5echo/quickstart_arduino_echo_download_library.png" width="70%" />

## 2.USB 驱动安装

\#> 驱动程序安装提示 | 将设备连接至 PC，打开设备管理器为设备安装[FTDI驱动](https://ftdichip.com/drivers/vcp-drivers/)。以 win10 环境为例，下载匹配操作系统的驱动文件，并解压，通过设备管理器进行安装。(注：某些系统环境下，需要安装两次，驱动才会生效，未识别的设备名通常为`M5Stack`或`USB Serial`, Windows 推荐使用驱动文件在设备管理器直接进行安装 (自定义更新), 可执行文件安装方式可能无法正常工作)。[点击此处，前往下载FTDI驱动](https://ftdichip.com/drivers/vcp-drivers/)

<div class="product_pic"><img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/ftdi_01.webp"><img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/ftdi_02.webp"><img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/ftdi_03.webp"></div>

\#>MacOS 注意事项 | 对于 MacOS 用户安装前请勾选 `系统偏好设置` - >`安全性与隐私` - >`通用` - >`允许以下位置下载的App` - > `App Store和认可的开发者选项`。

## 3. 端口选择

将设备通过 USB 线连接至电脑，在完成驱动安装后， Arduino IDE 中可选中对应设备的端口。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/m5echo/quickstart_arduino_echo_select_port.png" width="70%" />

## 4. 程序编译 & 烧录

1. 打开驱动库中的案例程序 “EchoRest”

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/m5echo/quickstart_arduino_echo_select_demo.png" width="70%" />

1. 在代码中填入 WiFi 名称和密码

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/m5echo/ADD_WIFI.png" width="70%" />

1. 点击上传按钮，将自动进行程序编译，与程序烧录。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/m5echo/quickstart_arduino_echo_select_demoupload.png" width="70%" />

## 5. 程序效果如下

指示灯说明

- 开机后红色状态灯表示网络未连接

- 开机后绿色状态灯表示已连接网络

- 按下按键状态灯变为黄色

- 识别结果识别状态灯为红色

- 识别结果成功状态灯为绿色

1\. 打开串口，按下复位按键，显示 WiFi 已连接

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/m5echo/reset%20button.png" width="30%" />

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/m5echo/wifi%20connected.png" width="70%" />

2\. 按住按键不放，开始说话进行语音识别，说话完成，会打印 “end”，放开按键，等待返回识别结果。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/m5echo/buttonA.png" width="30%" />

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/m5echo/recognize.png" width="70%" />

## 6. 相关资源

- **Github**

  - [M5Atom Library](https://github.com/m5stack/M5Atom/tree/master)

- **Arduino API & Examples**
  - [EchoRest](https://github.com/m5stack/M5Atom/tree/master/examples/Echo/EchoRest)
  - [PlayMusic](https://github.com/m5stack/M5Atom/tree/master/examples/Echo/PlayMusic)
  - [RecordPlay](https://github.com/m5stack/M5Atom/tree/master/examples/Echo/RecordPlay)
