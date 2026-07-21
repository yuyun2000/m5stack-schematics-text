# Network

## 案例程序

### 案例一 

设置 WiFi 名称密码，连接 WiFi，连接结果打印在串口上

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/network/uiflow_block_network_demo1.svg"> 


```python
from m5stack import *
from m5stack_ui import *
from uiflow import *
import wifiCfg

wifiCfg.doConnect('M5-R&D', '**********')
print(wifiCfg.wlan_sta.isconnected())
```

### 案例二

手机下载 Esptouch 这个软件，上传程序至 M5设备，在 Esptouch 软件输入手机连接的 WiFi 密码，串口显示连接成功，输出 IP 地址，则设备配置 WiFi 连接成功，会自动连接这个 WiFi 了。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/network/uiflow_block_network_demo_smartconfig.svg"> 

1.上传完成上面的程序至 m5设备之后，在 Esptouch 软件输入 WiFi 密码，点击确认即可

<img alt="schematics" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/network/uiflow_block_network_smartconfig_connect_wifi.png" width="20%" />

2.完成之后，设备自动连接 WiFi，输出 ip 地址

<img alt="schematics" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/network/uiflow_block_network_smartconfig_get_ip_address.png" width="50%" />


## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/network/uiflow_block_wifi_connect.svg"> 

```python
wifiCfg.autoConnect(lcdShow=False)
```

- 尝试自动连接到先前配置过的 Wi-Fi 网络。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/network/uiflow_block_wifi_connect.svg"> 

```python
wifiCfg.autoConnect(lcdShow=True)
```

- 尝试自动连接到先前配置过的 Wi-Fi 网络，并在 LCD 上显示连接过程的状态信息。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/network/uiflow_block_network_reconnect.svg"> 

```python
wifiCfg.reconnect()
```

- 尝试重新连接到之前配置并保存的 Wi-Fi 网络。这个方法通常用于设备失去连接后重新尝试连接。


<img class="blockly_svg" src="
https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/network/uiflow_block_network_doConnect.svg"> 

```python
wifiCfg.doConnect('', '')

```

- 设置 WiFi 名称和密码

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/network/uiflow_block_network_p2p.svg"> 

```python
M5Label('label0', x=193, y=67, color=0x000, font=FONT_MONT_14, parent=None)

```

- 表示发送点对点消息到指定的 API Key。


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/network/uiflow_block_network_getp2p.svg"> 

```python
str(getP2PData())
```

- 获取接收到的 P2P(点对点)消息数据。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/network/uiflow_block_network_wlan_create_station.svg"> 

```python
network.WLAN(network.STA_IF)
```

- 创建一个 WLAN(无线局域网)接口对象。选择 Wi-Fi 模式
  - station 模式：连接局域网 Wi-Fi
  - access point 模式：自开启热点

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/network/uiflow_block_network_wlan_config_ap.svg"> 

```python
wlan.config(essid='', password='', authmode=network.AUTH_OPEN)
```

- wlan.config(): 配置 WLAN 接口的参数。
    - essid: 设置接入点的 SSID(网络名称)。
    - password: 设置接入点的密码。
    - authmode: 设置接入点的认证模式。


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/network/uiflow_block_network_wlan_active.svg"> 

```python
wlan.active(True)
```

- 激活接口：用来激活无线网络接口的。这个命令用于启用设备的 Wi-Fi 功能，使其可以开始进行无线通信


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/network/uiflow_block_network_wlan_scan.svg"> 

```python
str(wlan.scan())
```

- 扫描周围的 Wi-Fi 网络，并返回一个包含可用网络信息的列表

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/network/uiflow_block_network_wlan_isconnected.svg"> 

```python
str(wlan.scan())
```

- 检查 ESP32是否已连接到 Wi-Fi 网络


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/network/uiflow_block_network_wlan_connect.svg"> 

```python
wlan.connect('your_SSID', 'your_PASSWORD')

```

- ssid: 要连接的 Wi-Fi 网络的名称。
- password: Wi-Fi 网络的密码。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/network/uiflow_block_network_wlan_config.svg"> 

```python
str(wlan.config('mac'))
```

- str(wlan.config('mac')): 获取设备的 MAC 地址，并将其转换为字符串格式。
- str(wlan.config('essid')): 获取当前配置的 SSID(网络名称)，并将其转换为字符串格式。


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/network/uiflow_block_network_wlan_ifconfig.svg"> 

```python
str(wlan.ifconfig())
```

- 获取设备的网络配置


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/network/uiflow_block_network_wlan_status.svg"> 

```python
str(wlan.status())
```

- 获取当前 Wi-Fi 连接的状态。


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/network/uiflow_block_network_wlan_disconnect.svg"> 

```python
wlan.disconnect()
```

- 断开 Wi-Fi 连接

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/network/uiflow_block_network_wlan_state_define.svg"> 

```python
str(1001)
```

- STAT_IDLE: Wi-Fi 空闲状态。设备当前未尝试连接到任何 Wi-Fi 网络。
- STAT_CONNECTING: Wi-Fi 连接中。设备正在尝试连接到指定的 Wi-Fi 网络。
- STAT_GOT_IP: Wi-Fi 已连接并获得 IP 地址。设备已成功连接到 Wi-Fi 网络，并从 DHCP 服务器获得了 IP 地址。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/network/uiflow_block_network_smartconfig_set_type.svg"> 

```python
smartconfig.set_type(smartconfig.ESPTOUCH)
```

- ESPTOUCH: 使用 ESPTOUCH 协议进行配置。通过手机 App 将 Wi-Fi 配置信息(SSID 和密码)发送给设备，使其连接到指定的 Wi-Fi 网络。
- AIRKISS: 使用 AIRKISS 协议进行配置。AIRKISS 是腾讯开发的一种无线配置协议，用于将 Wi-Fi 配置信息发送到设备。
- ESPTOUCH_AIRKISS: 同时使用 ESPTOUCH 和 AIRKISS 协议进行配置。设备将同时监听两种协议，手机可以使用任意一种协议发送 Wi-Fi 配置信息，设备接收到后进行配置。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/network/uiflow_block_network_smartconfig_start.svg"> 

```python
smartconfig.start()
```

- 启动 SmartConfig 功能，使设备进入 SmartConfig 配置模式，等待接收来自手机 App 的 Wi-Fi 配置信息(SSID 和密码)。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/network/uiflow_block_network_smartconfig_stop.svg"> 

```python
smartconfig.stop()
```

- 停止 SmartConfig 功能，退出 SmartConfig 配置模式。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/network/uiflow_block_network_smartconfig_get_status.svg"> 

```python
str(smartconfig.status())
```

- 获取 SmartConfig 当前的状态。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/network/uiflow_block_network_smartconfig_get_ssid.svg"> 

```python
str(smartconfig.get_ssid())
```

- 获取 SmartConfig 过程中接收到的 Wi-Fi 网络的 SSID(网络名称)。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/network/uiflow_block_network_smartconfig_get_password.svg"> 

```python
str(smartconfig.get_password())
```

- 获取 SmartConfig 过程中接收到的 Wi-Fi 网络的 password(网络密码)。


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/network/uiflow_block_network_smartconfig_get_phoneip.svg"> 

```python
str(smartconfig.get_phoneip())
```

- 获取在 SmartConfig 过程中，手机的 IP 地址。


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hardwares/network/uiflow_block_network_smartconfig_state_define.svg"> 

```python
str(smartconfig.get_phoneip())
```

- 表示 SmartConfig 扫描 Wi-Fi 网络完成的事件。


