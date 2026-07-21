# 小智墨伴语音助手

本教程将介绍如何上手配置和使用小智墨伴语音助手。

## 1. 基础操作

1. 设备背部的圆形按键为电源键，单击进行开机，双击关机。设备出厂时默认插入了配套的物联网卡（nano SIM），若需要更换别的流量卡，安装方向请参考下图。产品配套的物联网卡请勿用于其他设备、其他用途，否则会被锁卡。关于 SIM 卡 运营商，以及到期充值相关说明，可参见 [Xiaozhi Card Kit文档](/zh_CN/core/Xiaozhi_Card_Kit)。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1157/xiaozhi_card_sim_card_01.jpg" width="40%" /><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1157/xiaozhi_card_pwr_btn_01.jpg" width="40%" />

2. 设备首次开机后，将进入基础引导页面，根据提示，依次进入下一页。并在进入主页面后，获取设备绑定的验证码。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1157/xiaozhi_card_guide_01.jpg" width="80%" />

## 2. 注册小智 AI

1. 首次使用，需要访问[小智 AI 控制面板](https://xiaozhi.me/)，注册并登录账号。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1157/xiaozhi_card_register_01.jpg" width="80%" />

2. 进入小智 AI 控制台，创建新的智能体。点击添加设备，并填入设备显示的验证码信息，实现设备绑定。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1157/xiaozhi_card_register_02.jpg" width="80%" />
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1157/xiaozhi_card_register_03.jpg" width="80%" />
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1157/xiaozhi_card_register_04.jpg" width="80%" />
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1157/xiaozhi_card_register_05.jpg" width="80%" />
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1157/xiaozhi_card_register_06.jpg" width="80%" />

## 3. 开始使用

1. 完成绑定后， 设备即可正常使用，可通过以下三种方式唤醒设备进行对话。

- 语音唤醒：使用唤醒词 "你好小智" 唤醒设备。
- 电源按键：单击背部圆形按键切换待机（待命）与唤醒（聆听）状态。
- 触摸屏幕：触摸屏幕即可唤醒

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1157/xiaozhi_card_listen_01.jpg" width="50%" />

2. 超过 3 分钟没有交互，将进入休眠状态。进入休眠模式后，无法直接通过唤醒词进行唤醒，需触摸屏幕重新进入主页面。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1157/xiaozhi_card_sleep_01.jpg" width="50%" />

## 4. 充电底座

1. 设备需通过配套的磁吸充电底座进行充电， 请参考以下操作，安装充电底座。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1157/xiaozhi_card_base_fixed_01.jpg" width="80%" />

2. 充电底座接口如下图所示，其中红色的 PORT.A 接口可用于二次开发和拓展。复位按键单击进行复位，长按可使设备进入程序下载模式。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1157/xiaozhi_card_base_interface_01.jpg" width="50%" />

3. 充电底座底部提供状态指示灯。<span style="color:green">**绿色**</span>：聆听中。 <span style="color:blue">**蓝色**</span>：充电中。

\#> 充电说明 | 设备充电时，设备将保持开启，无法进行关机。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1157/xiaozhi_card_base_light_01.jpg" width="80%" />

## 5. 配置模式

1. 主页面中，触摸下滑屏幕可切换至配置页面。该页面中提供音量调节，网络模式配置，关机与休眠等操作。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1157/xiaozhi_card_setting_page_01.jpg" width="50%" />

## 6. 使用 Wi-Fi 网络

设备支持切换使用 Wi-Fi 网络，具体可参考下方步骤进行配置.

1. 开机后，在主页面下滑屏幕。点击 切换网络为 Wi-Fi 选项。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1157/xiaozhi_card_wifi_config_01.jpg" width="80%" />

2. 根据提示连接 AP 热点 (Xiaozhi-XXXX)，连接成功后将自动跳转网络配置页面，若出现没有自动跳转的情况，可尝试手动使用浏览器访问`192.168.4.1`进入网络配置页面。

?> 注意事项 | 仅支持连接 2.4GHz Wi-Fi 网络，若使用手机热点的无法正常连接情况，请尝试打开手机 AP 的兼容性配置选项。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1157/xiaozhi_card_wifi_config_02.jpg" width="80%" />

3. 完成配置 Wi-Fi 配置连接后，设备将自动重启复位，切换使用 Wi-Fi 网络。
