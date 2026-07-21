## Socket

>使用Socket实现UDP通信

### 获取本机IP

```python

#获取本机IP
from wifiCfg import wlan_sta

print(wlan_sta.ifconfig())

```

### UDP Server

```python 

import socket

#创建Socket实例
udpsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print(socket.AF_INET)

#监听Host和端口
udpsocket.bind(('0.0.0.0', 5000))

#发送数据到指定IP与端口
udpsocket.sendto(data, (IP, 5000))

while True:
  #接收1024个bytes数据
  print(udpsocket.recv(1024))
  wait_ms(2)

```

### UDP Client

```python 

import socket

#创建Socket实例
udpsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#配置连接指定UDP服务器IP与端口
udpsocket.connect((IP, 5000))

#发送数据
udpsocket.send(DATA)

#发送数据到指定UDP服务器
udpsocket.sendto(DATA, (IP, 5000))

while True:
  #接收1024个bytes数据
  print(udpsocket.recv(1024))
  wait_ms(2)

```


