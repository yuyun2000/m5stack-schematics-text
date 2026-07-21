# StamPLC 使用教程

## 1.功能布局

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/stamplc_guide_interface_01.png"> 
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/stamplc_guide_interface_02.png"> 
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/stamplc_guide_interface_03.png"> 
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/stamplc_guide_interface_04.png"> 
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/stamplc_guide_interface_05.png"> 
</PictureViewer>


- 电源供电：DC 6 ~ 36V@1A
- 按键RST: 单击复位，保持长按(红灯亮起)进入下载模式
- 按键A: BACK，返回上一级
- 按键B: NEXT, 切换下一项
- 按键C: OK, 确认选项
- INPUT: 8x 隔离输入
- RELAY: 4x 继电器控制
- PORT.A/PORT.B Grove拓展接口
- GPIO.EXT 2x8P 总线拓展
- microSD 卡槽
- PWR-CAN，PWR-CAN 120Ω终端电阻接入开关
- PWR-485，PWR-485，120Ω终端电阻接入开关

## 2.Dashboard

Dashboard中将实时显示当前继电器与输入通道的状态，左侧日志监视器显示操作记录，导航栏显示当前网络与Ezdata服务的连接状态。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/stamplc_guide_dashboard_01.jpg" width="40%"><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/stamplc_guide_dashboard_02.jpg" width="40%"> 


## 3.Ezdata

StamPLC 默认固件支持Ezdata连接，可实现远程继电器控制与输入状态监控。使用按键A返回至主菜单中，依次按下按键B切换至`Ezdata`选项，按下按键C确认并进入Ezdata配置页面。再次使用按键B切换至WIFI配置选项并确认。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/stamplc_guide_ezdata_01.jpg" width="40%"><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/stamplc_guide_ezdata_02.jpg" width="40%"> <img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/stamplc_guide_ezdata_03.jpg" width="40%"> 

此时设备将处于配网状态，使用手机扫描屏幕二维码，或手动连接AP热点`M5StamPLC-WiFi-Config`, 然后使用浏览器(推荐使用chrome浏览器)直接访问`192.168.4.1`跳转至WiFi配置页面。点击下拉菜单扫描,填入WiFi信息进行配置。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/stamplc_guide_wifi_config_01.png" width="40%"> 

#>WiFi配置补充说明 | 1.仅支持配置连接2.4G WiFi<br/>2.WiFi配置后将在后台自动尝试连接，并在成功连接网络后自动启用Ezdata服务连接。连接状态可在Dashboard页面中导航栏通过图标进行查看。

选中`Monitor Link`选项，查看远程访问页面二维码。使用手机扫描并访问远程页面，并使用M5Stack账户进行登录，即可进入控制操作面板。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/stamplc_guide_ezdata_04.jpg" width="40%"><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/stamplc_guide_ezdata_05.jpg" width="40%">

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/stamplc_guide_web_page_01.png" width="80%"> 

为了方便通过其他设备远程交互控制StamPLC, 基于Ezdata服务还提供了对StamPLC远程控制的HTTP API，可点击页面底部`ADVANCED`选项，查看并复制对应的URL。并使用指定的请求method进行控制。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/stamplc_guide_web_page_02.png" width="80%"> 

同一个StamPLC允许多个用户共同使用，通过设备`Monitor Link`页面二维码访问控制面板页面并登录时，将会登录用户添加到当前StamPLC的授权用户列表中。已经登录添加过的用户，可以通过设备的device_id URL 登录并直接使用。

- device_id URL

```bash
https://ezdata-stamplc.m5stack.com/${device_id}
```

`Ezdata`功能菜单中提供了`Clear Monitoring`选项，用于清除所有已授权的用户，来限制其他用户的访问。(该步骤将刷新所有HTTP API的token，基于旧token的URL将失效)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/stamplc_guide_ezdata_06.jpg" width="40%"><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/stamplc_guide_ezdata_07.jpg" width="40%"> 

## 4.LogMonitor

StamPLC LogMonitor功能用于监控几个通信接口状态与内部传感器状态。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/stamplc_guide_log_monitor_01.jpg" width="40%"> <img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/stamplc_guide_log_monitor_02.jpg" width="40%"><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/stamplc_guide_log_monitor_03.jpg" width="40%"> 


## 5.TimerRelay

StamPLC TimerRelay 能够设置继电器按照一定的通断周期进行工作。该功能仅用于测试，设备复位后或退出页面后将自动暂停。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/stamplc_guide_timer_relay_01.jpg" width="40%"><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/stamplc_guide_timer_relay_02.jpg" width="40%"> 

## 6.TriggerRelay

StamPLC TriggerRelay 用于设置监听 8 通道的输入信号状态，当信号状态满足设置的触发条件时，可配置执行对应的动作。如输入信号高电平时触发某个继电器闭合，并且支持保存触发预设至SD卡中。该功能仅用于测试，设备复位后或退出页面后将自动暂停。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/stamplc_guide_trigger_relay_01.jpg" width="40%"><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/stamplc_guide_trigger_relay_02.jpg" width="40%"><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/stamplc_guide_trigger_relay_03.jpg" width="40%"> 

## 7.Setting

查看设备固件版本，对Modbus从机地址，蜂鸣器以及RTC时钟显示的时区(UTC)进行配置。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/stamplc_guide_setting_01.jpg" width="40%"><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/stamplc_guide_setting_02.jpg" width="40%"> 

## 8.Modbus Slave

StamPLC固件默认启动后将自动初始化Modbus从机，外部设备可通过PWR-485接口，使用Modbus RTU协议对设备进行控制，具体寄存器协议如下。

Register Map:

1. Coils (Read/Write)
- Address 0: Relay 1 output (true/false)
- Address 1: Relay 2 output (true/false)
 - Address 2: Relay 3 output (true/false)
- Address 3: Relay 4 output (true/false)

2. Input Registers (Read-only)
- Address 0-7:   Inputs (true/false) - 8 registers
- Address 8-9:   Temperature (FLOAT32) - 2 registers
- Address 10-11: Bus Voltage (FLOAT32) - 2 registers
- Address 12-13: Shunt Current (FLOAT32) - 2 registers

