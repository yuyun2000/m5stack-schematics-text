# 一键烧录 ESPHome 出厂固件

自 ESPHome 2026.3.0 版本起，我们已陆续上线多款设备的 ESPHome 预编译固件，可通过 ESPHome 网页工具完成一键烧录。本文以 Atom EchoS3R 语音助手固件为例进行演示。不同设备的固件名称、选型界面会略有差异，但网络配置与设备添加的操作流程基本一致。

## 准备工作

为确保固件烧录流程正常进行，请提前准备以下物品与环境：

- 对应型号的 M5Stack 设备
- 一根 USB Type-C 数据线 （**非供电线**）
- 支持 `WebSerial` API 的浏览器：推荐 [`Google Chrome`](https://www.google.com/intl/zh-CN/chrome/) 和 [`Microsoft Edge`](https://www.microsoft.com/zh-cn/edge/download)
- 电脑安装对应 USB 串口驱动（例如 CH9102 等，根据设备搭载的串口芯片按需安装）

## 烧录固件

1. 使用 USB Type‑C 数据线将设备连接至电脑，并将设备进入下载模式。
2. 点击**固件一键烧录**按钮，选择对应串口设备完成连接；如果有多个设备，请务必选中目标设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1230/ha_select_firmware_button.webp" width="60%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1230/ha_select_serial_device.webp" width="80%">

3. 设备连接成功后，点击安装选项。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1230/ha_improv_serial_install_firmware_1.webp" width="80%">

4. 确认固件和设备信息，确认无误后点击 `Install` 开始烧录。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1230/ha_improv_serial_install_firmware_2.webp" width="80%">

等待固件自动下载并完成烧录。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1230/ha_improv_serial_install_firmware_3.webp" width="80%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1230/ha_improv_serial_install_firmware_4.webp" width="80%">

5. 烧录完成后，部分设备会自动复位，可直接进入串口配网流程；若设备未自动重启，请根据实际情况手动执行复位操作。

## 网络配置

本步骤用于为设备配置 Wi‑Fi 信息，使设备正常接入无线网络。

\#> 提示 | 该操作不适用于默认采用网口联网的设备（如 PoE 摄像头）。此类设备接通网线后，将通过 DHCP 自动获取 IP 地址，可直接跳转至 “配置设备” 章节，继续完成设备添加。

### 通过串口配置网络

1. 完成固件烧录并对设备执行复位操作后，设备将**默认开启串口配网功能**。请再次点击**固件一键烧录**按钮，重新连接设备。

2. 在配网选项中，选择 **Connect to Wi-Fi** 进入网络配置界面。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1230/ha_improv_serial_wifi_config_1.webp" width="80%" />

3. 选择需要连接的**网络名称（SSID）**，输入对应 Wi‑Fi 密码，点击 **Connect** 开始连接。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1230/ha_improv_serial_wifi_config_2.webp" width="80%" />

4. 等待设备完成网络连接，界面显示连接成功即可。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1230/ha_improv_serial_wifi_config_3.webp" width="80%" />

### 通过 BLE 配置网络

若您未使用本站的 WebSerial 工具进行固件烧录（例如通过 [Web ESPHome](https://web.esphome.io/) 烧录），设备将不会自动弹出网络配置界面。此时可通过手机蓝牙为设备发送配网信息，完成网络配置。

\#> 注意 | 请提前在手机上安装 **Home Assistant 配套应用（Home Assistant Companion APP）**：<br>- 安卓（Android）：[点击下载](https://play.google.com/store/apps/details?id=io.homeassistant.companion.android)<br>- iOS：[点击下载](https://apps.apple.com/us/app/home-assistant/id1099568401)

1. 固件烧录完成后，**开启手机蓝牙**，并打开 Home Assistant 配套应用。

2. 在应用内依次进入：`Settings（设置） -> Devices & services（设备与服务）`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1230/ha_companion_app_dashboard.webp" width="30%" /><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1230/ha_companion_app_sidebar.webp" width="30%" /><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1230/ha_companion_app_settings.webp" width="30%" />

3. 在 `Discovery（发现）` 页面中找到待配置的设备，点击 `Add（添加）`，并按照提示输入 Wi‑Fi 网络信息。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1230/ha_companion_app_discover.webp" width="30%" /><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1230/ha_companion_app_configure_wifi.webp" width="30%" /><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1230/ha_companion_app_connecting.webp" width="30%" />

4. 等待设备完成网络连接，配置即生效。

### 通过 AP 配置网络

1. 固件烧录完成后，设备将自动创建一个开放热点，名称格式为：`<设备名称>_<MAC地址前六位>`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1230/ha_device_ap_connect_1.webp" width="60%" />

2. 使用手机或电脑连接该设备热点，系统将自动跳转至配置页面；若未自动跳转，请手动在浏览器中访问地址：`http://192.168.4.1`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1230/ha_device_ap_connect_2.webp" width="80%" />

3. 在配置页面中，选择目标 Wi‑Fi 网络名称（SSID）并输入对应密码，点击 **Save** 保存配置。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1230/ha_device_ap_connect_3.webp" width="80%" />

4. 等待设备完成网络连接，配置弹窗自动关闭即可。

## 配置设备

完成任意一种配网方式后，设备将自动接入指定网络。

1. 打开 Home Assistant，依次进入 `Settings -> Devices & services`，在 `Discovered` 页面查找对应设备（支持浏览器端与手机 App 操作），选中设备即可完成添加。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1230/ha_add_discovered_device.png" width="80%" />

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1230/ha_add_discovered_device_2.png" width="80%" />

\#> 提示 | 针对设备类型不同，部分设备可能会有相应的初始化流程（比如语音助手），请根据设备实际指引操作，或者访问具体产品适配页面教程进行初始化配置。

2. 设备添加成功后，可在 ESPHome 集成页面中查看该设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1230/ha_esphome_integration_card.webp" width="80%" />

3. 点击可以查看设备实体和相关属性：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1230/ha_esphome_locate_device.webp" width="80%">

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1230/ha_device_detail.webp" width="80%">

## 后续操作

出厂默认固件未集成 API 加密相关配置。若您需要对设备身份验证进行加密处理，可参考官方设备适配教程，手动添加加密配置信息，自行编译固件后重新上传至设备。
