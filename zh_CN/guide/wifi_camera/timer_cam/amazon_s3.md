# Timer Amazon S3 Folder Pusher

>本教程将向你介绍, 如何通过TimerCAM定时传输图像至Amazon S3文件存储服务

## 驱动安装

#>将设备连接至PC，打开设备管理器为设备安装[FTDI驱动](https://ftdichip.com/drivers/vcp-drivers/)。以win10环境为例,下载匹配操作系统的驱动文件, 并解压,通过设备管理器进行安装。(注:某些系统环境下,需要安装两次,驱动才会生效,未识别的设备名通常为`M5Stack`或`USB Serial`, Windows推荐使用驱动文件在设备管理器直接进行安装(自定义更新), 可执行文件安装方式可能无法正常工作)。[点击此处，前往下载FTDI驱动](https://ftdichip.com/drivers/vcp-drivers/)

<div class="product_pic"><img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/ftdi_01.webp"><img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/ftdi_02.webp"><img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/ftdi_03.webp"></div>

#>MacOS用户注意事项 | 对于MacOS用户安装前请勾选 `系统偏好设置` - >`安全性与隐私` - >`通用` - >`允许以下位置下载的App` - > `App Store和认可的开发者选项`。


## 下载烧录工具

>请根据您所使用的操作系统,点击下方按钮下载相应的M5Burner固件烧录工具.解压打开应用程序。

| Software version | Download link                                                               |
| ---------------- | --------------------------------------------------------------------------- |
| M5Burner_Windows | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-beta-win-x64.zip)   |
| M5Burner_MacOS   | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-mac-x64.dmg)        |
| M5Burner_Linux   | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-beta-linux-x64.zip) |


## 烧录固件

>`打开M5Burner`-->`将设备连接至电脑`-->`选择对应的端口`-->`切换至TimerCam选项`-->`选择TimerS3FolderPusher固件点击download`-->点击`Burn`进行烧录-->等待弹窗`successful`则表示烧录完成

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/wifi_camera/timer_cam/amazon_s3/amazon_s3_01.jpg" width="70%">

>点击`Burn`， 在进行烧录前，需要为设备配置一些相关的连接参数。


<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/wifi_camera/timer_cam/amazon_s3/amazon_s3_02.jpg" width="70%">

#>`WIFI SSID`: WIFI名称， 注意不要出现特殊字符，建立共享文件夹的计算机与TimerCAM需处于同一网络下<br/>`WIFI PASSWORD`: WIFI密码<br/>`Access Key`: AWS Access Key<br/>`Secret Key`: AWS Secret Key<br/>`URL`: AWS S3 URL (文件夹所在路径)<br/>`File Prefix`: 图片的默认前缀名称<br/>`Image Size`: 图片尺寸<br/>`Interval`:图像发送间隔， 建议间隔大于20s.
