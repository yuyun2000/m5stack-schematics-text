## wifiCfg

#>使用wifiCfg模块中的API, 配置设备WiFi连接。

`wifiCfg.autoConnect(lcdShow=True)`
- 自动连接已经保存的WiFi,屏幕显示连接UI

`wifiCfg.doConnect(ssid, pwd)`
- 连接指定的WiFi

`wifiCfg.connect(ssid, pwd, timeout, block=False)`
- 连接指定的WiFi,并指定连接超时时间

`wifiCfg.reconnect()`
- WiFi重连

`wifiCfg.wlan_sta.isconnected()`
- 是否已经连接

`wifiCfg.wlan_sta.ifconfig()`
- 查看连接信息

## 案例程序

```python

import wifiCfg
import time

print("start connect")
wifiCfg.doConnect('ssid', 'password')

while True:
    if not (wifiCfg.wlan_sta.isconnected()):
        print("try reconnect")
        wifiCfg.reconnect()
    print("get ifconfig")
    print(wifiCfg.wlan_sta.ifconfig())
    #('192.168.1.xx', '255.255.255.0', '192.168.1.1', '192.168.1.1')
    wait(5)

```