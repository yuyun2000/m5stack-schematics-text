# Camera-Tool上手指南

## 注意事项

#>固件兼容|Camera-Tool适用于TimerCAM及UnitCAM系列产品，UnitCAM使用前需要将GROVE接口通过TTL-TO-USB转接板连接至PC。

## 驱动安装

#>驱动安装|将设备连接至PC，打开设备管理器为设备安装[FTDI驱动](https://ftdichip.com/drivers/vcp-drivers/)。以win10环境为例,下载匹配操作系统的驱动文件, 并解压,通过设备管理器进行安装。(注:某些系统环境下,需要安装两次,驱动才会生效,未识别的设备名通常为`M5Stack`或`USB Serial`, Windows推荐使用驱动文件在设备管理器直接进行安装(自定义更新), 可执行文件安装方式可能无法正常工作)。[点击此处，前往下载FTDI驱动](https://ftdichip.com/drivers/vcp-drivers/)

<div class="product_pic"><img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/ftdi_01.webp"><img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/ftdi_02.webp"><img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/ftdi_03.webp"></div>

#>MacOS用户注意事项 | 对于MacOS用户安装前请勾选 `系统偏好设置` - >`安全性与隐私` - >`通用` - >`允许以下位置下载的App` - > `App Store和认可的开发者选项`。

## 软件介绍

Camera-Tool用于控制Timer-CAM摄像头进行图片拍摄,目前支持串口与WiFi两种设备连接模式。

## 软件下载 

目前仅提供windows版本

| 工具版本        | 下载链接                                                                                       |
| --------------- | ---------------------------------------------------------------------------------------------- |
| cameraToolsV1.5 | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/software/cameraToolsV1.5.rar) |


## 烧录固件

1.打开上位机软件, 将设备连接至电脑, 选择对应的端口, 点击Burner进行烧录, 等待弹窗successful则表示烧录完成。

?> 注意| 烧录固件之前不能点击Connect，不然会占用端口导致烧录固件失败

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/wifi_camera/timer_cam/cameratool/cameratool_01.jpg" width="70%">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/wifi_camera/timer_cam/cameratool/cameratool_02.png" width="70%">

## 串口模式

串口模式下,设备通过USB连接至电脑,并通过Camera-Tool访问设备串口/获取图像。 

#>**注意:** `Unit-CAM`系列在使用CameraTools时, 图像传输接口为Grove接口。请将Grove接口的TX,RX通过USB-TTL转接板连接至电脑, 然后选择对应端口进行连接。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/wifi_camera/timer_cam/cameratool/cameratool_03.jpg" width="70%">


## Wi-Fi模式

连接设备到端口, 点击配置按钮, 输入Wi-Fi名称和密码, 点击连接, 面会自动切换至`HTTP`页签 将模式切换为`Wi-Fi-HTTP`,并显示图像.

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/wifi_camera/timer_cam/cameratool/cameratool_04.jpg" width="70%">


## 拍摄图片

点击折叠开关,能够展开拍摄操作菜单。操作栏中提供`拍摄`、`延时拍摄`、`设置图片保存路径`功能

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/wifi_camera/timer_cam/cameratool/cameratool_05.jpg" width="40%">

## 参数调整

左侧的配置菜单中提供了一系列的图像参数设置,用于调整图片的成像效果。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/wifi_camera/timer_cam/cameratool/cameratool_06.jpg" width="70%">

## 手机版APP

网络模式下,还可以使用手机版APP进行图片拍摄与查看监控

| 工具版本                  | 下载链接                                                                                            |
| ------------------------- | --------------------------------------------------------------------------------------------------- |
| TimerCAM-App-Android v1.0 | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/software/TimerCAM-App-Android.apk) |


