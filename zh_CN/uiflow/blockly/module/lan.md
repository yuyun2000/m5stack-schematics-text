# [Module13.2 LAN](/zh_CN/module/LAN%20Module%2013.2)

## 案例程序

通过 LAN 模块连接到 MQTT 服务器，订阅和发布消息，并轮询下行消息来控制设备的状态(例如控制继电器的开关)


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan/uiflow_block_lan_demo.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import module
import time

setScreenColor(0x810000)

lan_topic = None
lan_msg = None

lan = module.get(module.LAN_MODULE)

label2 = M5TextBox(53, 219, "ON", lcd.FONT_DejaVu18, 0x810000, rotate=0)
label3 = M5TextBox(230, 219, "OFF", lcd.FONT_DejaVu18, 0x810000, rotate=0)

def module_lan_mqtt_cb(lan_mq_topic, lan_mq_payload):
  global lan_topic, lan_msg
  lan_topic = lan_mq_topic
  lan_msg = lan_mq_payload
  print(lan_msg)
  pass

lan.lan_init(18, 23, 19, 5, 0, 35)
print('Lan Init')
wait(1.5)
lan.mqtt_config('mqtt.m5stack.com', 1883, 'm5mqttid', '', '', 120)
print('Mqtt Configured')
wait(1.5)
lan.mqtt_connect()
print('Connect Server')
wait(1.5)
lan.mqtt_subscribe('m5stack/relay', module_lan_mqtt_cb, 0)
while True:
  lan.mqtt_publish('m5stack/relay', 'ON', 0)
  wait(1.5)
  lan.mqtt_poll_loop()
  if False:
    print('ON')
  else:
    print('OFF')
  wait_ms(2)

```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan/uiflow_block_module_lan_available_packet.svg">

```python
lan.is_available_packet(1)
```

- 配置局域网 TCP 或 UDP 连接，指定套接字类型(如 TCP 或 UDP)、端口号和设备类型(如服务器或客户端)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan/uiflow_block_module_lan_config.svg">

```python
lan.tcp_udp_config('', 0, 1, 1)
```

- 通过指定的主题和 token 从服务器获取数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan/uiflow_block_module_lan_ezdata_async_get_value.svg">

```python
lan.get_ezdata(ezdata_get_AlUvNcb, 'GCJ3Ic5h2eXnzV3rT3bBXvrncCaJnART', '')
```

- 异步获取EZData数据（需提供token和主题）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan/uiflow_block_module_lan_ezdata_remove.svg">

```python
lan.remove_ezdata('GCJ3Ic5h2eXnzV3rT3bBXvrncCaJnART', '')
```

- 删除EZData云端数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan/uiflow_block_module_lan_ezdata_save.svg">

```python
lan.set_ezdata('GCJ3Ic5h2eXnzV3rT3bBXvrncCaJnART', '', '', 0)
```

- 保存数据到EZData云端（参数：token、主题、数据、超时时间）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan/uiflow_block_module_lan_get_data.svg">

```python
req.text
```

- 获取HTTP请求返回的文本内容

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan/uiflow_block_module_lan_get_if_config.svg">

```python
lan.get_if_config()
```

- 获取当前网络接口配置（IP/掩码/网关/DNS）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan/uiflow_block_module_lan_get_status_code.svg">

```python
req.status_code
```

- 获取HTTP请求状态码

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan/uiflow_block_module_lan_http_request.svg">

```python
try:
  req = lan.http_request(method='GET', url='', headers={})
  gc.collect()
  req.close()
except:
  pass
```

- 发送HTTP请求（自动内存回收）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan/uiflow_block_module_lan_init.svg">

```python
lan.lan_init(18, 23, 19, 5, 0, 35)
```

- 初始化LAN模块（参数：RST/CS/INT/MOSI/MISO/SCLK引脚号）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan/uiflow_block_module_lan_local_ip.svg">

```python
lan.local_ip()
```

- 获取本地IP地址

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan/uiflow_block_module_lan_mqtt_check_connection.svg">

```python
lan.mqtt_is_connect()
```

- 检查MQTT连接状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan/uiflow_block_module_lan_mqtt_connect.svg">

```python
lan.mqtt_connect()
```

- 建立MQTT连接

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan/uiflow_block_module_lan_mqtt_disconnect.svg">

```python
lan.mqtt_disconnect()
```

- 断开MQTT连接

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan/uiflow_block_module_lan_mqtt_init.svg">

```python
lan.mqtt_config('mqtt.m5stack.com', 1883, '', '', '', 120)
```

- 配置MQTT参数（服务器/端口/用户名/密码/客户端ID/保活时间）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan/uiflow_block_module_lan_mqtt_poll.svg">

```python
lan.mqtt_poll_loop()
```

- MQTT消息轮询处理（需在循环中调用）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan/uiflow_block_module_lan_mqtt_publish.svg">

```python
lan.mqtt_publish('', '', 0)
```

- MQTT消息发布（参数：主题/消息/QoS等级）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan/uiflow_block_module_lan_mqtt_sub.svg">

```python
lan.mqtt_subscribe('', module_lan_mqtt_cb, 0)
```

- 订阅MQTT主题（带回调函数）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan/uiflow_block_module_lan_mqtt_sub_cb.svg">

```python
def module_lan_mqtt_cb(lan_mq_topic, lan_mq_payload):
  global ezdata_value1, lan_topic, lan_msg
  lan_topic = lan_mq_topic
  lan_msg = lan_mq_payload
  pass
```

- MQTT订阅回调函数模板

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan/uiflow_block_module_lan_remote_ip.svg">

```python
lan.remote_ip()
```

- 获取远程主机IP地址

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan/uiflow_block_module_lan_set_ifconfig.svg">

```python
lan.set_if_config('192.168.1.100', '255.255.255.0', '192.168.1.1', '8.8.8.8')
```

- 手动设置网络接口（IP/掩码/网关/DNS）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan/uiflow_block_module_lan_socket_close.svg">

```python
lan.socket_close()
```

- 关闭当前socket连接

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan/uiflow_block_module_lan_tcp_receive_packet.svg">

```python
lan.tcp_receive_packet(0)
```

- TCP接收数据包（参数：socket句柄）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan/uiflow_block_module_lan_tcp_send_packet.svg">

```python
lan.tcp_send_packet('1234')
```

- TCP发送数据包

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan/uiflow_block_module_lan_udp_receive_packet.svg">

```python
lan.udp_receive_packet(0)
```

- UDP接收数据包（参数：socket句柄）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/lan/uiflow_block_module_lan_udp_send_packet.svg">

```python
lan.udp_send_packet('', 0, '')
```

- UDP发送数据包（参数：目标IP/端口/数据）