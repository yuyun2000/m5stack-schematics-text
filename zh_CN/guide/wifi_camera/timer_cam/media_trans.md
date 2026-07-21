# Timer Camera - UiFlow MediaTrans

## 功能介绍

使用 TimerCAM 实现低功耗定时唤醒拍摄功能，该功能需依赖 Wi-Fi 连接。拍摄的图片将自动上传至 M5 云端，并通过唯一 token 生成固定一个 HTTP 接口，其他的设备可以通过该接口访问获取最新一帧图片以及设备当前电池电压状态。

## 驱动安装

\#> 将设备连接至 PC，打开设备管理器为设备安装[FTDI驱动](https://ftdichip.com/drivers/vcp-drivers/)。以 win10 环境为例，下载匹配操作系统的驱动文件，并解压，通过设备管理器进行安装。(注：某些系统环境下，需要安装两次，驱动才会生效，未识别的设备名通常为`M5Stack`或`USB Serial`, Windows 推荐使用驱动文件在设备管理器直接进行安装 (自定义更新), 可执行文件安装方式可能无法正常工作)。[点击此处，前往下载FTDI驱动](https://ftdichip.com/drivers/vcp-drivers/)

<div class="product_pic"><img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/ftdi_01.webp"><img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/ftdi_02.webp"><img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickc/ftdi_03.webp"></div>

\#>MacOS 用户注意事项 | 对于 MacOS 用户安装前请勾选 `系统偏好设置` - >`安全性与隐私` - >`通用` - >`允许以下位置下载的App` - > `App Store和认可的开发者选项`。

## 下载烧录工具

> 请根据您所使用的操作系统，点击下方按钮下载相应的 M5Burner 固件烧录工具。解压打开应用程序。

| 软件版本         | 下载链接                                                                        |
| ---------------- | ------------------------------------------------------------------------------- |
| M5Burner_Windows | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-beta-win-x64.zip)   |
| M5Burner_MacOS   | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-mac-x64.dmg)        |
| M5Burner_Linux   | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-beta-linux-x64.zip) |

## 烧录固件

`打开M5Burner`-->`将设备连接至电脑`-->`选择对应的端口`-->`切换至TimerCam选项`-->`选择合适版本点击download`-->`配置合适的参数`--> 点击`Burn`进行烧录 --> 等待弹窗`successful`则表示烧录完成

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/wifi_camera/timer_cam/media_trans/media_trans_01.png" width="70%">

\#>`WIFI SSID`: WIFI 名称， 注意不要出现特殊字符<br/>`WIFI PASSWORD`: WIFI 密码 (注: WIFI 密码为必填项，不可为空，建议使用带有密码的 WIFI 热点)<br/>`Image Size`: 图片尺寸<br/>`Wake Time`: 图像发送间隔， 建议间隔大于 30s.

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/wifi_camera/timer_cam/media_trans/media_trans_02.jpg" width="70%">

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/wifi_camera/timer_cam/media_trans/media_trans_03.jpg" width="70%">

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/wifi_camera/timer_cam/media_trans/media_trans_04.jpg" width="70%">

## TOKEN 获取

点击`Get Token`即可获取 --> 等待弹窗`Token`, 显示的字符串即为 Token, 也可通过扫描二维码获取，或直接在浏览器中打开。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/wifi_camera/timer_cam/media_trans/media_trans_05.jpg" width="70%">

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/wifi_camera/timer_cam/media_trans/media_trans_06.jpg" width="70%">

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/wifi_camera/timer_cam/media_trans/media_trans_07.jpg" width="70%">

## HTTP 接口

请求方式为`GET`, 返回数据为 JPG 图像数据，设备电压值将包含在 HTTP Response Headers 中的`Voltage`字段。

```bash
#GET
#http://api.m5stack.com:5003/timer-cam/image?tok=token

http://api.m5stack.com:5003/timer-cam/image?tok=8caab58179bc02d5435c653acbe03966
```

## UiFlow 编程

- [在UiFlow中使用MediaTrans功能获取TimerCAM图片, 并进行显示](/zh_CN/uiflow/blockly/media_trans/timer_camera)
