## ESP-NOW

>使用ESP-NOW技术,无线传输数据到其他ESP32主控设备

```python
import espnow

# 初始化
espnow.init()

# 设置信道

# 获取本机mac_addr
espnow.get_mac_addr()

# 广播
espnow.broadcast(data='Hello')

# 设置peer列表
espnow.add_peer(slave_mac_addr, id)

# 发送消息
espnow.send(id, data='World')

# 发送消息回调
def send_cb(flag):
  if flag:
    print('succeed')
  else:
    print('Failed')

espnow.send_cb(send_cb)

# 接收消息回调
def recv_cb():
    # 获取数据
    sender_address, _, receive_data = espnow.recv_data(encoder='str')

espnow.recv_cb(recv_cb)

```