# PaperColor 出厂固件使用教程

## 1. 简介

PaperColor 出厂固件提供便捷的图片管理与显示功能，支持通过 AP Web 页面或 Ezdata 云平台将自定义图片推送到设备。
固件支持图片循环轮播和低功耗模式，在电池供电场景下也可长时间稳定运行。

## 2. 配置页面

单击设备左侧电源键开机。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1239/guide_papercolor_start_01.jpg" width="70%">

开机后，设备会自动开启 AP 热点 `PaperColor-XXXXXX`。使用手机连接热点后，在浏览器中访问 `192.168.4.1` 即可打开 Web 配置页面。

注意事项：Android 手机自动弹窗跳转的页面可能无法正常上传图片，建议通过浏览器访问 `192.168.4.1` 打开配置页面。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1239/guide_papercolor_start_02.jpg" width="70%">

点击页面下方的 `Mode` 按钮可用于切换模式，不同模式说明见下文。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1239/guide_papercolor_start_03.jpg" width="70%">

## 3. 本地模式 (AP)

### 基础使用

连接设备 AP 并进入本地模式 (AP) 页面， 点击页面的图片上传框，根据图片内容选择合适的刷新模式，点击 `Upload & Display` 上传并显示。

- Upload & Display: 上传并显示
- Upload Only: 仅上传至设备

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1239/guide_papercolor_ap_demo_01.jpg" width="70%">

### 刷新模式

提供两种刷新模式:

- Nearest: 图像会经过色彩缩减处理，将其转换为设备屏幕的标准颜色，显示更加清晰，但丢失细节。
- Dither: 使用抖动刷新方式，细节还原更多，但会有一些噪点。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1239/guide_papercolor_display_mode_compare_01.jpg" width="70%">

支持同时加载多张图片，并可自由缩放和摆放。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1239/guide_papercolor_display_multi_pic_01.jpg" width="70%">

### 本地存储说明

- 上传图片至设备时，将自动存储图片至本地。
- 若设备已插入 microSD 卡，将优先使用 microSD 卡进行图片存储。
- 未插入 microSD 卡时，将使用内置文件系统（存储空间约 6 MB）进行图片存储。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1239/guide_papercolor_storage_01.jpg" width="70%">

### 更多配置

- Auto Slideshow: 循环轮播模式 启用后设备将按设定间隔自动切换并刷新图片。
- Low Power Mode: 低功耗模式 启用后设备在图片刷新完成后进入深度睡眠，可延长电池续航。
- Interval: 设备循环轮播刷新图片的间隔。
- Boot sound: 开机提示音 控制设备开机时是否播放提示音。
- Reset machine: 恢复出厂设置 清除所有用户配置并恢复出厂默认状态。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1239/guide_papercolor_ap_mode_config_01.jpg" width="70%">

### 按键操作

支持通过按键 A, B 手动切换图片，单击顶部按键 C 将旋转图片显示。长按顶部按键 C 将再次打开 AP 配置引导页面。

## 4. Ezdata 模式 (INTERNET)

连接设备 AP 并进入 Ezdata 模式 (INTERNET) 页面，为设备配置 Wi-Fi 网络，等待生成设备 Token 与远程页面二维码。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1239/guide_papercolor_ezdata_mode_01.jpg" width="70%">

扫描屏幕二维码访问远程页面，使用 M5Stack 账户登录。 访问远程图片上传页面前，请先断开 PaperColor-XXXX AP 连接。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1239/guide_papercolor_ezdata_mode_02.jpg" width="70%">

远程页面将显示设备内置 SHT40 温湿度传感器数据，同时提供与 AP 模式相同的图片上传框。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1239/guide_papercolor_ezdata_mode_03.jpg" width="70%">

Ezdata 模式支持通过 M5Stack Ezdata 云平台远程推图。用户无需与设备处于同一局域网，也可将图片推送到设备显示，适用于远程更新场景。
注意：通过 Ezdata 上传的图像不会存储到本地。

### 更多配置

- Low Power Mode: 低功耗模式 启用后设备在图片刷新完成后进入深度睡眠，可延长电池续航。
- Interval: 配置设备通过 Ezdata 拉取新图片的周期，每次拉取将检查图片更新日期，存在新图片时将自动拉取和显示。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1239/guide_papercolor_ezdata_mode_config_01.jpg" width="70%">

### 按键操作

长按顶部按键 C ，设备将再次显示远程二维码界面。
