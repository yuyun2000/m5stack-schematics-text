# [Atomic PoE Base](/zh_CN/atom/Atomic%20PoE%20Base)

## 案例程序

连接 MQTT 服务，接收订阅消息

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/poe/uiflow_poebase_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
from base.PoE import PoE

setResolution(1280, 720)
setScreenColor(0x000000)

lan_topic = None
lan_msg = None

poe = PoE()

def atom_poe_mqtt_cb(poe_mq_topic, poe_mq_payload):
  global lan_topic, lan_msg
  lan_topic = poe_mq_topic
  lan_msg = poe_mq_payload
  print((str('mag:') + str(lan_msg)))
  print((str('topic:') + str(lan_topic)))
  pass


poe.mqtt_config('mqtt.m5stack.com', 1883, '', '', '', 120)
poe.mqtt_connect()
poe.mqtt_subscribe('M5Sack', atom_poe_mqtt_cb, 0)

``` 

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/poe/uiflow_block_atom_poe_init.svg">

```python
poe.tcp_udp_config('', 0, 1, 1)
```

- 初始化局域网连接。配置远程 IP 地址、端口号和选择使用的通信协议类型(TCP/UDP)，以及指定设备作为服务器或客户端。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/poe/uiflow_block_atom_poe_mqtt_init.svg">

```python
poe.mqtt_config('mqtt.m5stack.com', 1883, '', '', '', 120)
```

- 初始化 MQTT 服务器连接，包含服务器地址、端口号、客户端 ID、用户名、密码及心跳间隔(keepalive)。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/poe/uiflow_block_atom_poe_available_packet.svg">

```python
poe.is_available_packet(1)
```

- 检查当前是否有可用的 TCP 数据包，并返回数据包的数量。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/poe/uiflow_block_atom_poe_ezdata_async_get_value.svg">

```python
poe.get_ezdata(ezdata_get_KzSyFcb, 'GCJ3Ic5h2eXnzV3rT3bBXvrncCaJnART', '')
```

- 从指定的 MQTT 话题中获取数据，基于话题名和 token 进行操作。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/poe/uiflow_block_atom_poe_ezdata_remove.svg">

```python
poe.remove_ezdata('GCJ3Ic5h2eXnzV3rT3bBXvrncCaJnART', '')
```

- 从 MQTT 服务器中删除指定的话题，使用话题名和 token 进行删除操作。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/poe/uiflow_block_atom_poe_ezdata_save.svg">

```python
poe.set_ezdata('GCJ3Ic5h2eXnzV3rT3bBXvrncCaJnART', '', '', 0)
```

- 将指定的数据保存到某个话题中，并使用 token 进行身份验证。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/poe/uiflow_block_atom_poe_get_if_config.svg">

```python
poe.get_if_config()
```

- 获取当前网络或设备的配置信息。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/poe/uiflow_block_atom_poe_http_get.svg">

```python
poe.http_get('', True)
```

- 通过 HTTP 或 HTTPS 协议从指定的 URL 获取数据，可以选择获取完整内容或其他方式。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/poe/uiflow_block_atom_poe_http_post.svg">

```python
poe.http_post('', 'application/json', '')
```

- 通过 HTTP 或 HTTPS 协议向指定的 URL 发送数据，数据可以是 JSON、表单等多种格式。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/poe/uiflow_block_atom_poe_local_ip.svg">

```python
poe.local_ip()
```

- 获取设备在局域网中的本地 IP 地址。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/poe/uiflow_block_atom_poe_mqtt_check_connection.svg">

```python
poe.mqtt_is_connect()
```

- 检查当前设备是否已成功连接到 MQTT 服务器。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/poe/uiflow_block_atom_poe_mqtt_connect.svg">

```python
poe.mqtt_connect()
```

- 连接到指定的 MQTT 服务器。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/poe/uiflow_block_atom_poe_mqtt_disconnect.svg">

```python
poe.mqtt_disconnect()

```

- 断开当前与 MQTT 服务器的连接。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/poe/uiflow_block_atom_poe_mqtt_poll.svg">

```python
poe.mqtt_poll_loop()
```

- u 轮询从 MQTT 服务器接收到的下行消息。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/poe/uiflow_block_atom_poe_mqtt_publish.svg">

```python
poe.mqtt_publish('', '', 0)
```

- 发布一条消息到指定的 MQTT 主题(topic)。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/poe/uiflow_block_atom_poe_mqtt_sub.svg">

```python
poe.mqtt_subscribe('', atom_poe_mqtt_cb, 0)
```

- 订阅指定的 MQTT 主题(topic)，可以指定消息传递的服务质量(QoS)。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/poe/uiflow_block_atom_poe_mqtt_sub_cb.svg">

```python
def atom_poe_mqtt_cb(poe_mq_topic, poe_mq_payload):
  global ezdata_value1, lan_topic, lan_msg
  lan_topic = poe_mq_topic
  lan_msg = poe_mq_payload
  pass
```

- 设置一个回调函数，当指定的 MQTT 主题接收到消息时，调用该回调处理消息。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/poe/uiflow_block_atom_poe_remote_ip.svg">

```python
poe.remote_ip()
```

- 获取远程设备的 IP 地址。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/poe/uiflow_block_atom_poe_socket_close.svg">

```python
poe.socket_close()
```

- 关闭当前的网络套接字连接。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/poe/uiflow_block_atom_poe_tcp_receive_packet.svg">

```python
poe.tcp_receive_packet(0)
```

- 接收通过 TCP 协议传输的数据包，并根据指定的字节大小读取数据。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/poe/uiflow_block_atom_poe_tcp_send_packet.svg">

```python
poe.tcp_send_packet('1234')
```

- 通过 TCP 协议发送数据包，数据内容为指定的字符串或数字。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/poe/uiflow_block_atom_poe_udp_receive_packet.svg">

```python
poe.udp_receive_packet(0)
```

- 接收通过 UDP 协议传输的数据包，并根据指定的字节大小读取数据。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/poe/uiflow_block_atom_poe_udp_send_packet.svg">

```python
poe.udp_send_packet('', 0, '')
```

- 通过 UDP 协议发送数据包，指定目标 IP 地址、端口号和发送的数据内容。

