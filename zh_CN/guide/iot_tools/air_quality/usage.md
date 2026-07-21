# Air Quality / Air Quality v1.1 使用教程

## 产品介绍

**Air Quality / Air Quality v1.1**是一款一体化低功耗空气质量监测装置，内置多功能空气质量传感器 **SEN55** 和 CO2 传感器 **SCD40**，能监测空气中的 PM1.0、PM2.5、PM4、PM10 颗粒物、温度、湿度、VOC 和 CO2 浓度，适用于家庭、学校、工业、医院空气环境的长时间在线监测。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1180/K131-V11_Air_Quality_note_ZH.png" width="70%">

### 关于设备供电

本产品内置电池供电，支持低功耗定时唤醒。同时支持外接 USB 供电，可以保持工作，不休眠，使传感器连续工作，以确保采集数据的准确性。

## 操作说明

### 开关机与复位

- 开机：长按`开机按键`
- 复位与关机：
  - 当 USB 供电的时候，按下`复位与关机`， 设备复位。
  - 当用电池供电时，按下`复位与关机`， 设备关机。
  - 当 USB 供电时，将无法关闭本装置。

### 按键操作

- 单击 `按键A`进入远程二维码页面：

  - 按键 A 单击返回上一层

- 单击 `按键B`进入配署页面：
  - `按键A` 单击返回上一级菜单
  - `按键A` 长按 5s 开关峰鸣器
  - `按键B` 单击启用 AP 配置
  - `按键B` 长按 5s 恢复出厂设置

## 设置远程访问

1. 单击电源按钮开机，或者使用 USB 供电。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1180/Air-quality_learn_03.jpg" width="40%">

2. 按下 `按键B`，进入 AP 配置模式，此时屏幕显示链接 AP 热点名称和二维码。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1180/Air-quality_learn_04.jpg" width="40%">

3. 通过手机连接 AP 热点 `AirQ-xxxxxx`。连接 AP 后，屏幕显示配置的二维码以及 IP 地址。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1180/Air-quality_learn_06.jpg" width="40%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1180/Air-quality_learn_07.jpg" width="40%">

4. 扫描设备屏幕上的配置二维码，或手动访问 **192.168.4.1**，进入 Wi-Fi 配置页面。 配置设备上网用的 Wi-Fi、时区、唤醒间隔等信息，点击`CONNECT`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1180/Air-quality_learn_02.jpg" width="70%">

此时屏幕显示获取设备数据的公网访问地址。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1180/Air-quality_learn_05.jpg" width="40%">

5. 将地址拷贝到电脑端 / 手机端的浏览器，即可远程进入设备的数据读取页面，实时获取数据采集信息。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1180/Air-quality_learn_01.jpg" width="70%">

（注意：上图的`Data Share Link` 为原始数据接口， 详细数据格式可以参见[Raw Data Format](https://github.com/m5stack/AirQUserDemo/blob/main/AboutEzdataRawData.md)）

如果重启了设备，可以按下`按键B`进入配置选项，然后再次按下`按键B`，即可重新进入 AP 配置模式。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1180/Air-quality_learn_08.jpg" width="40%">

## 恢复出厂设置

\#> 说明 | 恢复出厂设置会清除所有自定义配置。

1. 在设备开机状态下，按下 `按键B` 进入设置界面。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1180/Air-quality_learn_09.jpg" width="40%">

2. 长按 5s `按键B`，设备恢复出厂设置，并重新启动。

## 视频介绍

<video class="video-container" controls><source src="https://static-cdn.m5stack.com/resource/docs/products/core/AirQ/K131%20AirQ%20%E8%A7%86%E9%A2%91.mp4" type="video/mp4"></video>
