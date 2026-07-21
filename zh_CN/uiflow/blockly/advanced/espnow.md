# ESP-NOW

#>什么是 ESP-NOW?|ESP-NOW 是一种短程低功耗通信协议，可以使多个设备在没有或不使用 Wi-Fi 的情况下进行通信。这种协议类似常见于无线鼠标中的低功耗 2.4GHz 无线连接——设备在进行通信之前要进行配对。配对之后，设备之间的连接是持续的、点对点的，并且不需要握手协议。

## 案例程序

### ESP-NOW Master

主机通过扫描指定 SSID 的 AP 获取从机的 mac 地址， 然后添加到配对列表中。在主循环中执行数据发送。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/espnow/uiflow_block_m5_espnow_master_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
from libs.m5_espnow import M5ESPNOW
import time

setScreenColor(0x222222)

flag_cb = None
slave_mac = None
slave_data = None
run = None
cnt_succes = None
count_send = None
peer_mac = None
slave_ssid = None

now = M5ESPNOW()

title0 = M5Title(title="ESPNOW-MASTER", x=100, fgcolor=0xFFFFFF, bgcolor=0xff0000)
label0 = M5TextBox(24, 75, "SLAVE MAC:", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
label1 = M5TextBox(125, 38, "label1", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
label2 = M5TextBox(24, 109, "SEND COUNT:", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
label9 = M5TextBox(230, 219, "STOP", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
label3 = M5TextBox(126, 75, "label3", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
label10 = M5TextBox(24, 175, "REVC COUNT:", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
label4 = M5TextBox(25, 38, "SLAVE SSID:", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
label11 = M5TextBox(145, 175, "label11", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
label5 = M5TextBox(146, 109, "label5", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
label6 = M5TextBox(48, 219, "SEND", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
label7 = M5TextBox(24, 144, "SUCCESS COUNT:", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
label8 = M5TextBox(174, 144, "label8", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)

peer_mac = None

def send_cb(flag):
  global flag_cb,slave_mac,slave_data,run,cnt_succes,count_send,peer_mac,slave_ssid
  flag_cb = flag
  if flag_cb:
    cnt_succes = cnt_succes + 1
    label8.setText(str(cnt_succes))

  pass


def recv_cb(dummy):
  global flag_cb,slave_mac,slave_data,run,cnt_succes,count_send,peer_mac,slave_ssid
  slave_mac, slave_data = now.espnow_recv_str()
  label11.setText(str(slave_data))

  pass

def buttonA_wasPressed():
  global flag_cb, slave_mac, slave_data, run, cnt_succes, count_send, peer_mac, slave_ssid
  run = 1
  pass
btnA.wasPressed(buttonA_wasPressed)

def buttonC_wasPressed():
  global flag_cb, slave_mac, slave_data, run, cnt_succes, count_send, peer_mac, slave_ssid
  run = 0
  pass
btnC.wasPressed(buttonC_wasPressed)

now.espnow_init(1, 1)
count_send = 0
cnt_succes = 0
flag_cb = 0
run = 0
slave_ssid = 'M5_Slave'
while peer_mac == None:
  peer_mac = now.espnow_scan(1, slave_ssid)
label1.setText(str(slave_ssid))
label3.setText(str(peer_mac))
now.espnow_add_peer(peer_mac, 1, 0, False)
now.espnow_send_cb(send_cb)
now.espnow_recv_cb(recv_cb)
while True:
  if run:
    count_send = count_send + 1
    now.espnow_send_data(1, str(count_send))
    label5.setText(str(count_send))
    wait_ms(1)
  wait_ms(2)

```

### ESP-NOW Slave


从机开启指定名称的 AP 热点(提供主机发现并获取 mac 地址使用), 在接收回调中获取发送者的 mac 地址和数据， 发送返回相同数据。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/espnow/uiflow_block_m5_espnow_slave_example.svg">


```python
from m5stack import *
from m5ui import *
from uiflow import *
from libs.m5_espnow import M5ESPNOW


setScreenColor(0x222222)
mac_addr = None
data = None
onetime = None
ssid = None

now = M5ESPNOW()

title0 = M5Title(title="ESPNOW-SLAVE", x=105, fgcolor=0xFFFFFF, bgcolor=0xff7c00)
label0 = M5TextBox(26, 82, "MAC ADDR:", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
label1 = M5TextBox(76, 47, "label1", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
label2 = M5TextBox(26, 119, "REMOTE MAC:", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
label3 = M5TextBox(126, 82, "label3", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
label4 = M5TextBox(26, 47, "SSID:", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
label5 = M5TextBox(150, 119, "label5", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
label7 = M5TextBox(26, 159, "REMOTE DATA:", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
label8 = M5TextBox(157, 159, "label8", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
label6 = M5TextBox(26, 195, "SEND DATA:", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
label9 = M5TextBox(133, 195, "label9", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)

def recv_cb(dummy):
  global mac_addr,data,onetime,ssid
  mac_addr, data = now.espnow_recv_str()
  label5.setText(str(mac_addr))
  label8.setText(str(data))
  label9.setText(str(data))
  if onetime:
    now.espnow_add_peer(mac_addr, 1, 1, False)
    now.espnow_recv_cb(recv_cb)
    onetime = 0
  now.espnow_send_data(1, data)

  pass

now.espnow_init(1, 1)
onetime = 1
ssid = 'M5_Slave'
now.espnow_set_ap(ssid, '')
label1.setText(str(ssid))
label3.setText(str(now.espnow_get_mac(0)))
now.espnow_recv_cb(recv_cb)

```


## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/espnow/uiflow_block_m5_espnow_init_channel.svg">

```python
from libs.m5_espnow import M5ESPNOW
now = M5ESPNOW()
now.espnow_init(ch, type)
```

- 初始化 ESP-NOW 到某一信道， 同时配置数据类型：
  - ch:0-13
  - type:
    - list: 0
    - string: 1


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/espnow/uiflow_block_m5_espnow_add_peer.svg">

```python
now.espnow_add_peer('', 1, 0, False)
```

- 添加配对设备， 并映射指定 id:
  - peer: 设备 mac 地址
  - id：0-10
  - ifidx:s
    - ESP_IF_WIFI_STA:0
    - ESP_IF_WIFI_AP:1
  - encrypt:启用加密则需填入 LMK


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/espnow/uiflow_block_m5_espnow_send_data.svg">

```python
now.espnow_send_data(1, "Hello")
```

- 发送数据给已添加到配对列表中的 id 设备

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/espnow/uiflow_block_m5_espnow_enable_send_cb.svg">

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/espnow/uiflow_block_m5_espnow_send_cb.svg">

```python
def send_cb(flag):
  global flag_cb
  flag_cb = flag
  pass

now.espnow_send_cb(send_cb)
```

- 数据发送 callback:
  - flag: 发送状态标志位
    - 发送成功：1
    - 发送失败：0


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/espnow/uiflow_block_m5_espnow_broadcast_data.svg">

```python
now.espnow_broadcast_data('1234')
```

- 广播发送数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/espnow/uiflow_block_m5_espnow_enable_recv_cb.svg">

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/espnow/uiflow_block_m5_espnow_recv_cb.svg">

```python
def recv_cb(dummy):
  slave_mac, slave_data = now.espnow_recv_str()
  print(str(slave_data))
  pass

now.espnow_recv_cb(recv_cb)
```

- 数据接收 callback

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/espnow/uiflow_block_m5_espnow_get_mac_address.svg">

```python
now.espnow_get_mac(0)
```

- 获取本机 mac 地址

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/espnow/uiflow_block_m5_espnow_get_remote_mac1.svg">

```python
peer_mac = now.espnow_scan(1, slave_ssid)
```

- 扫描指定 AP SSID, 并获得其 mac 地址。该功能常用于发现和添加新的设备。


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/espnow/uiflow_block_m5_espnow_set_ap_mode1.svg">

```python
now.espnow_set_ap(ssid, '')
```

- 启用 AP 热点， 并指定 SSID 和 PASSWORD

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/espnow/uiflow_block_m5_espnow_set_pmk.svg">

```python
now.espnow_set_pmk('')
```

- 若在添加配对设备时候启用了 encrypt, 双方设备再可通过设置一致的 PMK(Primary Master Key), 对 LMK 进行 AES-128加密， 来实现加密通信， 未设置则使用默认值。


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/espnow/uiflow_block_m5_espnow_deinit.svg">

```python
now.espnow_deinit()
```

- 逆初始化， 释放 ESP-NOW。


