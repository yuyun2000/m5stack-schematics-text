# Atom Printer 使用教程

>本教程将演示如何为Atom Printer烧录固件, 并实现web打印和MQTT远程打印操作。

## 1.准备工作

- [参考M5Burner教程](/zh_CN/uiflow/m5burner/intro)完成烧录工具下载, 并参考下图, 下载对应的固件。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/917/atom_printer_firmware_01.jpg" width="80%" />

## 2.USB驱动安装

#>驱动程序安装提示|将设备连接至PC，打开设备管理器为设备安装[FTDI驱动](https://ftdichip.com/drivers/vcp-drivers/)。以win10环境为例,下载匹配操作系统的驱动文件, 并解压,通过设备管理器进行安装。(注:某些系统环境下,需要安装两次,驱动才会生效,未识别的设备名通常为`M5Stack`或`USB Serial`, Windows推荐使用驱动文件在设备管理器直接进行安装(自定义更新), 可执行文件安装方式可能无法正常工作)。[点击此处，前往下载FTDI驱动](https://ftdichip.com/drivers/vcp-drivers/)

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/ftdi_01.webp" width="30%"><img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/ftdi_02.webp" width="30%"><img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/ftdi_03.webp" width="30%">

#>对于MacOS用户安装前请勾选 `系统偏好设置` - >`安全性与隐私` - >`通用` - >`允许以下位置下载的App` - > `App Store和认可的开发者选项`。


## 3.固件烧录

将设备通过USB线连接至电脑，点击Burn按钮， 并选中设备对应的端口进行烧录。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/917/atom_printer_firmware_02.jpg" width="80%" />
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/917/atom_printer_firmware_03.jpg" width="80%" />

## 4.开始使用

### AP打印

设备启动后将默认可开启AP热点（`ATOM_PRINTER-xxxx`），使用手机连接AP热点并使用浏览器(推荐使用chrome浏览器)访问`192.168.4.1`跳转至打印页面（连接AP后一般会默认跳转至该页面）。页面提供多种打印选项，字符，QRCode, BarCode。选中对应的输入框并输入字符，然后点击`Print`按钮即可打印。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/917/atom_printer_config_01.png" width="60%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/917/atom_printer_firmware_test_01.jpg" width="60%">

### MQTT远程打印

AP打印页面的底部是Wi-Fi配置选项。通过配置Wi-Fi连接，设备将自动连接至M5Stack MQTT服务器(Server: mqtt.m5stack.com, Port: 1883)。同时在成功连接服务器后使用本机的mac地址作为订阅topic，方便通过别的MQTT Client进行打印控制。

- eg: 通过[MQTT调试工具](https://mqttx.app/)，远程控制打印。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/917/atom_printer_config_02.jpg" width="60%">


- 打印文本指令

```
TEXT,10,0:Hai
```

- 打印QRCode指令

```
QR:1234
```

- 打印BarCode指令

```
BAR:1234
```


## 5.补充说明

### 状态指示灯

- 绿灯闪烁：初始化完成
- 绿灯常亮：Wi-Fi已连接
- 蓝灯常亮：MQTT已连接
- 蓝灯闪烁：MQTT断开连接


### 按键操作

- 长按Atom中间按键，将重启，并清除Wi-Fi信息。

