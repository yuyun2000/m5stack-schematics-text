# M5StickC 恢复出厂固件

#>出厂固件|当设备出现工作异常时, 可尝试重新烧录出厂固件来检验设备硬件是否存在故障。参考以下教程。使用M5Burner固件烧录工具, 为设备烧录出厂固件。

## 1.准备工作

- [参考M5Burner教程](/zh_CN/uiflow/m5burner/intro)完成烧录工具下载, 并参考下图, 下载对应的固件。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/restore_factory/m5stickc/m5stickc_burner_factory_01.png" width="80%" />

## 2.USB驱动安装

#>驱动程序安装提示|将设备连接至PC，打开设备管理器为设备安装[FTDI驱动](https://ftdichip.com/drivers/vcp-drivers/)。以win10环境为例,下载匹配操作系统的驱动文件, 并解压,通过设备管理器进行安装。(注:某些系统环境下,需要安装两次,驱动才会生效,未识别的设备名通常为`M5Stack`或`USB Serial`, Windows推荐使用驱动文件在设备管理器直接进行安装(自定义更新), 可执行文件安装方式可能无法正常工作)。[点击此处，前往下载FTDI驱动](https://ftdichip.com/drivers/vcp-drivers/)

<div class="product_pic"><img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/ftdi_01.webp"><img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/ftdi_02.webp"><img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/ftdi_03.webp"></div>

#>对于MacOS用户安装前请勾选 `系统偏好设置` - >`安全性与隐私` - >`通用` - >`允许以下位置下载的App` - > `App Store和认可的开发者选项`。

## 3.端口选择

将设备通过USB线连接至电脑，在完成驱动安装后， M5Burner中可选中对应设备的端口。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/restore_factory/m5stickc/m5stickc_burner_factory_02.png" width="80%" />

## 4.固件烧录

点击Burn开始烧录。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/restore_factory/m5stickc/m5stickc_burner_factory_03.png" width="80%" />

效果如下图：

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/restore_factory/m5stickc/m5stickc_burner_factory_04.gif" width="30%" />

