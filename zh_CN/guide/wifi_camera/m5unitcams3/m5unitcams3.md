# Unit CamS3/Unit CamS3-5MP 上手教程

#> 开箱即用的网络摄像头，支持实时预览，定时云端上传，microSD 卡延时拍摄

## 准备

<div class="product_pic"><img class="pic" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-CAMS3%205MP/99f0c53f2ce63b959c4a9218c947901.png"><img class="pic" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-CAMS3%205MP/70fac327c0d9dc806d81c73bdae080a.png"></div>

- 为设备供电

- 搭配[Grove2USB-C](/zh_CN/accessory/Grove2USB-C)转接板为设备供电或是二次开发烧录程序，按照如下图片的顺序接好线

<img alt="schematics" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-CAMS3%205MP/d361e7c8cd2fdbd0aecd8cbe4d959ae.png" width="80%" />

## 上传程序

#> 注意|此步骤在出厂的时候已经烧录了固件，如果你不需要可以跳过进行下一步查看该设备的功能

- 1.安装 M5Burner 固件烧录工具。

请根据您所使用的操作系统,点击下方按钮下载相应的 M5Burner 固件烧录工具.解压打开应用程序。

| 软件版本         | 下载链接                                                                    |
| ---------------- | --------------------------------------------------------------------------- |
| M5Burner_Windows | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-beta-win-x64.zip)   |
| M5Burner_MacOS   | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-mac-x64.dmg)        |
| M5Burner_Linux   | [Download](https://m5burner-cdn.m5stack.com/app/M5Burner-v3-beta-linux-x64.zip) |


- 2.根据需要选择对应的固件进行下载,有UnitCamS3和UnitCamS3 5MP的固件

<img alt="schematics" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-CAMS3%205MP/7792fb38eafb3929ed6af36be6b3f42.png" width="80%" />

- 3.点击“download”下载固件

<img alt="schematics" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-CAMS3%205MP/fc8a49884189de96a71fe8fd2abd534.png" width="80%" />

-  4.点击“Burn”

<img alt="schematics" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-CAMS3%205MP/ea817719aa25a5753907a09d842cdbf.png" width="80%" />

- 5.选择对应设备端口，点击“Start”开始烧录固件

<img alt="schematics" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-CAMS3%205MP/f685de1f1a7b4067d790e3a922babbf.png" width="80%" />

- 6.等待烧录完成，点击“Burn successful，click here to return”完成烧录

<img alt="schematics" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-CAMS3%205MP/528110fa65307e296a0d1f8f1f09945.png" width="80%" />

## 配置Wi-Fi

- 设备每次启动都会打开AP：UnitCamS3-WiFi，若10s内无用户连接则关闭

<img alt="schematics" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-CAMS3%205MP/2ab2a25f33a36835b3dfc40f0316767.png" width="30%" />


- 连接AP，浏览器访问“192.168.4.1”，进入配置页面

<img alt="schematics" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-CAMS3%205MP/d1c7f86614a60eec622aab6efe3e1c9.png" width="30%" />


- 如下图看到有 microSD，Microphone Applications，LED control等应用功能

<img alt="schematics" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-CAMS3%205MP/39a70086d3289306e7a48596929ddcc.png" width="30%" />

## 工作模式介绍

### 1.单张拍摄

<img alt="schematics" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-CAMS3%205MP/6128a94c8149293bb4b8e35ee7276f5.png" width="30%" />

### 2.实时预览图像

<img alt="schematics" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-CAMS3%205MP/fbace5452bd28cd2be5e3a95a824e5f.png" width="30%" />


### 3.云端定时上传图片

- 配置Wi-Fi，唤醒间隔设置，实现低功耗远程拍摄，通过二维码或者链接即可获取最新图片

<div class="product_pic"><img class="pic" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-CAMS3%205MP/bd65062c96f3af2935c337bdc4e4dd6.png"><img class="pic" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-CAMS3%205MP/c28c266b0e13c431b5f8c0b54cb609e.png"><img class="pic" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-CAMS3%205MP/793f3f2b73cff6ebe8c0cb711e51e0d.png"><img class="pic" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-CAMS3%205MP/56b4bee2edb1d4fcf1d9afcd3a502a2.png"><img class="pic" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-CAMS3%205MP/16b7359ea13b0fc077bd3b83d45f647.png"></div>

## 视频

- Unit CamS3-5MP 基本功能介绍以及配置教程

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-CAMS3%205MP/9b258811e7e5a229195bc3b521f3f1c2.mp4" type="video/mp4"></video>
