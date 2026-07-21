# Timer Folder Pusher

本教程将向你介绍, 如何通过TimerCAM定时传输图像至电脑共享文件夹(基于SMB文件共享传输协议)

## 创建共享文件夹

以`Windows 10`系统为例， `创建文件夹` -> 文件夹内右键打开`属性` -> `分享设置` -> 添加访问权限->点击输入框的下拉菜单，并选择`Everyone`点击添加->点击权限级别下拉选项，启用`读取/写入`权限 -> 确认共享。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/wifi_camera/timer_cam/smb/smb_01.jpg" width="70%">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/wifi_camera/timer_cam/smb/smb_02.jpg" width="70%">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/wifi_camera/timer_cam/smb/smb_03.jpg" width="70%">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/wifi_camera/timer_cam/smb/smb_04.jpg" width="70%">

## 修改共享设置

文件夹内右键打开`属性`->`网络共享中心`

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/wifi_camera/timer_cam/smb/smb_05.jpg" width="70%">

将网络发现更改为`启用网络发现`。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/wifi_camera/timer_cam/smb/smb_06.jpg" width="70%">

点击所有网络的下拉图标，在密码保护的共享中选择`无密码保护的共享`，最后点击`保存修改`。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/wifi_camera/timer_cam/smb/smb_07.jpg" width="70%">

## 驱动安装

#>将设备连接至PC，打开设备管理器为设备安装[FTDI驱动](https://ftdichip.com/drivers/vcp-drivers/)。以win10环境为例,下载匹配操作系统的驱动文件, 并解压,通过设备管理器进行安装。(注:某些系统环境下,需要安装两次,驱动才会生效,未识别的设备名通常为`M5Stack`或`USB Serial`, Windows推荐使用驱动文件在设备管理器直接进行安装(自定义更新), 可执行文件安装方式可能无法正常工作)。[点击此处，前往下载FTDI驱动](https://ftdichip.com/drivers/vcp-drivers/)

<div class="product_pic"><img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/ftdi_01.webp"><img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/ftdi_02.webp"><img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/ftdi_03.webp"></div>

#>MacOS用户注意事项 | 对于MacOS用户安装前请勾选 `系统偏好设置` - >`安全性与隐私` - >`通用` - >`允许以下位置下载的App` - > `App Store和认可的开发者选项`。


### 下载烧录工具

>请根据您所使用的操作系统,点击下方按钮下载相应的M5Burner固件烧录工具.解压打开应用程序。

| Software version | Download link                                                               |
| ---------------- | --------------------------------------------------------------------------- |
| M5Burner_Windows | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-beta-win-x64.zip)   |
| M5Burner_MacOS   | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-mac-x64.dmg)        |
| M5Burner_Linux   | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-beta-linux-x64.zip) |


## 获取本机IP

>同时按下`Win + R`键打开运行窗口，输入`cmd`回车打开命令行, 输入`ipconfig`回车确认，查看当前电脑的IP地址。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/wifi_camera/timer_cam/smb/ip_01.jpg" width="70%">


### 烧录固件

>`打开M5Burner`-->`将设备连接至电脑`-->`选择对应的端口`-->`切换至TimerCam选项`-->`选择TimerFolderPusher固件点击download`-->点击`Burn`进行烧录-->等待弹窗`successful`则表示烧录完成

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/wifi_camera/timer_cam/smb/burner_01.jpg" width="70%">

>点击`Burn`， 在进行烧录前，需要为设备配置一些相关的连接参数。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/wifi_camera/timer_cam/smb/burner_02.jpg" width="70%">


#>`WIFI SSID`: WIFI名称， 注意不要出现特殊字符，建立共享文件夹的计算机与TimerCAM需处于同一网络下<br/>`WIFI PASSWORD`: WIFI密码<br/>`Host/IP`: 文件分享服务所在的IP地址<br/>`Username`: 登录文件分享服务的用户名(若服务访问权限为所有人, 可省略)<br/>`Password`: 登录文件分享服务的用户密码(若服务访问权限为所有人, 可省略)<br/>`Folder Path`: 共享文件夹所在路径<br/>`File Prefix`: 图片的默认前缀名称<br/>`Image Size`: 图片尺寸<br/>`Interval`:图像发送间隔

#>注意事项:|不推荐在系统盘下创建共享文件夹, 当出现摄像头无法正常连接共享文件夹服务时可尝试更换一个简短的路径进行重试。

## 开始定时传输

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/wifi_camera/timer_cam/smb/smb_08.png" width="70%">

