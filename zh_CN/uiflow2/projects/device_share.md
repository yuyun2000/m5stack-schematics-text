# UiFlow2 设备分享

> UiFlow2 进一步引入了设备分享机制。这一功能不仅使得设备间的数据交换和协作变得更为高效，还极大地提升了开发流程的快捷性。

## 1. 准备

使用 UiFlow2 进行设备分享的几个准备步骤：

- 1\. 设备须提前下载好 UiFlow2 固件。如果没有下载固件，可以访问 [UiFlow2 Quick Start](/zh_CN/uiflow2/uiflow_web) 按照文档或视频步骤下载相应的固件
- 2\. 访问 UiFlow2 官方应用或者 UIFlow Web IDE 2.0 。
- 3\. 点击下方设备管理按钮，点击设备编辑按钮，进入设备信息界面。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/projects/deviceshare/share_01.png" width="70%">

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/projects/deviceshare/share_02.png" width="70%">

## 2.Mac 分享

把 Mac 地址通过常用通讯方式发送给另一个用户，该用户点击设备添加按钮，填入分享的 MAC 地址即可在线使用该设备。

> 注意：若设备配置 Permissions 需设置为 Public，分享的 MAC 地址才会生效。

设备主分享界面

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/projects/deviceshare/share_03.png" width="70%">

使用者分享`成功`界面

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/projects/deviceshare/share_04.png" width="70%">

> 注意：若设备被分享后，原设备主设备设置为私有，分享将会被禁用。

设备主分享界面

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/projects/deviceshare/share_05.png" width="70%">

使用者分享`禁止`界面

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/projects/deviceshare/share_06.png" width="70%">

## 3.Token 分享

> 注意：Token 分享设备需要用户主在设备信息中配置 Token Required，发送给其他用户的 Token 才能生效。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/projects/deviceshare/share_07.png" width="70%">
