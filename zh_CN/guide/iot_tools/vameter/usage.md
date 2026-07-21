# VAMeter使用教程

## 1.功能布局

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/iot_tools/vameter/vameter_interface_01.png" width="70%">

- 1.顶部USB接口: VAMeter设备供电,MSC模式导出数据,固件烧录更新
- 2.右侧USB接口：测量电源输出接口
- 3.左侧USB接口：测量电源输入接口
- 4.右侧按键: 顺序切换菜单选项, 长按返回上一级。
- 5.左侧复位开关：整机复位
- 6.旋转编码器开关(左, 右, 中间按键): 左右切换菜单选项, 中间按键确认。
- 7.隔离电源切换开关

#>隔离电源切换开关使用说明: | VAMeter的旋转编码器开关下方提供了一个隔离电源切换开关。当开关切至(5V MIX)则左侧的输入电源将同时用于整机设备供电,当开关切至(5V ISO)则左侧的输入电源仅用于待测负载供电,此状态下整机需要额外供电才能启动。

?>PD供电注意事项: | VAMeter测量电源输入端的CC1,CC2引脚直连至电源输出端,在对PD供电设备进行供电测量时,若出现无法正常供电的情况,请尝试翻转USB接口重试。请确保两侧使用的数据线均为支持PD快充,确保CC1,CC2能正确握手。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/iot_tools/vameter/vameter_usb_flipping_01.png" width="50%">

## 2.功耗测量

1.VAMeter开机默认进入`Power Monitor`功耗监测APP页面, 左侧接口连接输入电源。右侧接口连接测量负载即可实时监测功耗状态。使用下方旋转编码器开关可切换数据页面。`长按右侧按键可返回主菜单`。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/iot_tools/vameter/power_monitor_01.png" width="70%">


## 3.WiFi配置

1.设备启动后主菜单切换进入设置页面, 打开`Network`选项, 根据提示使用手机连接AP热点`M5-VAMeter-WiFi`,然后通过扫描设备屏幕二维码或浏览器直接访问`192.168.4.1/syscfg`跳转至WiFi配置页面。点击下拉菜单扫描,填入WiFi信息进行配置。

#>WiFi配置补充说明 | 1.仅支持配置连接2.4G WiFi<br/>2.WiFi配置后并不会马上进行连接, 仅进行本地保存, 在需要进行网络连接的场景如:功耗曲线数据上传Ezdata, 设备固件OTA情况才会进行连接。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/iot_tools/vameter/wifi_01.jpg" width="70%">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/iot_tools/vameter/wifi_02.png" width="70%">


## 4.功耗曲线

1.VAMeter支持以曲线的方式直观的显示当前功耗状态,同时支持录制一段时间内的功耗变化数据,方便用于设备功耗分析。

2.使用方式：设备启动后,在主菜单通过按键切换进入`Waveform`页面,此时能够看到实时的功耗曲线监控, 此时`单击旋转编码器开关中间按键`即可进行录制, 完成录制后将自动保存数据，可用于本地预览分析。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/iot_tools/vameter/waveform_01.png" width="70%">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/iot_tools/vameter/waveform_02.png" width="70%">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/iot_tools/vameter/waveform_03.jpg" width="70%">

#>录制模式配置：| 目前支持以下几种数据录制触发模式, 单击右侧按键可进入配置页面。<br/>配置及录制流程为：单击右侧按键进入配置页面->旋转编码器开关左右切换配置选项,再次单击中键选中/确认配置(支持选择`手动按键触发`,`电流触发`,`电压触发`三种触发模式, 后两种需要配置一个触发阈值, 当前版本支持配置最大录制时间为10min)->单击右侧按键完成配置->单击旋转编码器开关中间按键开始录制。

- 手动按键触发: `按下旋转编码器开关中间按键`, `直接`开始数据`录制`
- 电流触发: 配置电流触发模式和对应阈值后, `按下旋转编码器开关中间按键`,设备将进入`等待状态`, 当`大于/小于电流触发阈值`时将触发数据`录制`。
- 电压触发：配置电压触发模式和对应阈值后,`按下旋转编码器开关中间按键`,设备将进入`等待状态`, 当`大于/小于电压触发阈值`时值触发数据`录制`。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/iot_tools/vameter/waveform_04.png" width="70%">

#>Ezdata云端数据共享：| 选中`Upload Ezdata`,设备将使用配置的WiFi信息进行联网,同时将数据发送至Ezdata服务器,屏幕上将显示远程界面二维码。注：使用该功能前需完成WiFi配置。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/iot_tools/vameter/vameter_ezdata_web_01.png" width="60%">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/iot_tools/vameter/vameter_ezdata_web_02.png" width="60%">

## 5.导出CSV与修改启动logo

1.VAMeter顶部USB接口连接至电脑,设备启动后主菜单切换进入设置页面, 打开`Files`选项, 进入MSC模式。此时电脑将识别到存储设备。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/iot_tools/vameter/msc_01.png" width="70%">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/iot_tools/vameter/msc_02.png" width="70%">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/iot_tools/vameter/msc_03.png" width="70%">

#>导出csv数据：| 打开存储设备下的目录`rec`即可获取所有保存的测量数据集。

#>修改启动Logo:| 打开存储设备下的目录`startup_logo`, 添加新的启动图。当前仅支持jpg格式文件，推荐分辨率为240x240。完成保存后，VAMeter返回主菜单, 进入`Settings`->`Startup Image`选项配置新的启动图像。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/iot_tools/vameter/msc_04.jpg" width="70%">

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/iot_tools/vameter/msc_05.png" width="70%">

## 6.固件OTA

1.设备启动后主菜单切换进入设置页面, 打开`OTA Upgrade`选项, 根据提示依次按下旋转编码器开关中间按键进行固件升级。注：使用该功能前需完成WiFi配置。

## 7.VAMeter Base

1.VAMeter套装中标配的VAMeter Base内嵌了一个机械式继电器。底座接口支持输入DC 5-24V电源, 可用于负载供电与整机供电, 基于这一外设用户可以将其应用于一些自动化测试场景, 同时能够实时监测输入电源情况。同时提供了一组HY2.0-4P拓展接口, 通过二次开发可以有更多的应用可能。打开`Settings`->`Base Test`选项可用于继电器通断测试.

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/iot_tools/vameter/vameter_base_relay_01.jpg" width="70%">

## 8.操作视频

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/VA%20Meter/K136%20VA%20Meter%20%E8%A7%86%E9%A2%91.mp4" type="video/mp4">
</video>
