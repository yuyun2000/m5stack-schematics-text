
# Socket

## UDP Server

### 案例程序

创建 UDP Server 监听数据接收， 并发送返回相同的数据内容。通过网络相关的 API 可获取当前本机的 IP 地址， 用于提供其他 Client 数据发送。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/socket/uiflow_block_socket_udp_server_example.svg"> 


```python
from m5stack import *
from m5ui import *
from uiflow import *
import network
import socket

setScreenColor(0x222222)
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('SSID', 'PASSWORD')
print(wlan.ifconfig())

udpsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpsocket.bind(('0.0.0.0', 5000))
while True:
  print(udpsocket.recv(1024))
  wait_ms(2)
```


### 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/socket/uiflow_block_socket_udp_server_start.svg"> 

```python
udpsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpsocket.bind(('0.0.0.0', 5000))
```

- 创建 socket server 并指定监听的 IP(通常使用0.0.0.0监听本机)和端口

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/socket/uiflow_block_socket_udp_server_sendto.svg"> 

```python
udpsocket.sendto('Hello', ('192.168.31.11', 5000))
```

- 发送数据到指定 IP 和端口

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/socket/uiflow_block_socket_udp_server_close.svg"> 

```python
udpsocket.close()
```

- 关闭 socket

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/socket/uiflow_block_socket_udp_server_recv.svg"> 

```python
data = udpsocket.recv(1024)
```

- 阻塞接收监听数据， 并设置最大 buffer 长度， 接收到数据时返回。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/socket/uiflow_block_socket_udp_server_read.svg"> 

```python
data = udpsocket.read(10)
```

- 阻塞接收监听数据， 并设置接收 buffer 长度，当接收 buffer 填满时返回。

## UDP Client

### 案例程序

创建 UDP Client 发送数据到指定服务器。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/socket/uiflow_block_socket_udp_client_example.svg"> 

```python
from m5stack import *
from m5ui import *
from uiflow import *
import socket
import time
setScreenColor(0x222222)

udpsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpsocket.connect(('192.168.31.10', 5000))
while True:
  udpsocket.send('Hello World')
  wait(1)
  wait_ms(2)
```


### 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/socket/uiflow_block_socket_udp_client_start.svg"> 

```python
udpsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpsocket.connect(('192.168.31.10', 5000))
```

- 创建 socket server 并指定发送数据目标 IP 和端口


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/socket/uiflow_block_socket_udp_client_sendmsg.svg"> 

```python
udpsocket.send('Hello World')
```

- 发送字符数据


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/socket/uiflow_block_socket_udp_client_sendto.svg"> 

```python
udpsocket.write('')
```

- 写入原始数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/socket/uiflow_block_socket_udp_client_sendto.svg"> 

```python
udpsocket.sendto('Hello World', ('192.168.31.10', 5000))
```

- 发送数据至指定 IP 和端口

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/socket/uiflow_block_socket_udp_client_close.svg"> 

```python
udpsocket.close()
```

- 关闭 socket

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/socket/uiflow_block_socket_udp_client_recv.svg"> 

```python
data = udpsocket.recv(1024)
```

- 阻塞接收监听数据， 并设置最大 buffer 长度， 接收到数据时返回。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/socket/uiflow_block_socket_udp_client_read.svg"> 

```python
data = udpsocket.read(10)
```

- 阻塞接收监听数据， 并设置接收 buffer 长度，当接收 buffer 填满时返回。

