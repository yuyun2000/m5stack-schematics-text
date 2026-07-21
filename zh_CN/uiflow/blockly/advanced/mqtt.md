# MQTT

#>什么是 MQTT? |(Message Queuing Telemetry Transport,消息队列遥测传输协议),是一种基于发布/订阅(publish/subscribe)模式的"轻量级"通讯协议。 该协议构建于 TCP/IP 协议上， 作为一种低开销、低带宽占用的即时通讯协议，使其在物联网、小型设备、移动应用等方面有较广泛的应用。

## 案例程序

连接 MQTT 服务器， 实现订阅和主题消息发布。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/mqtt/uiflow_block_mqtt_example.svg"> 


```python
from m5stack import *
from m5ui import *
from uiflow import *
from m5mqtt import M5mqtt
import time

setScreenColor(0x222222)

def fun__dev_sub_(topic_data):
  # global params
  print('topic: /dev/sub received:')
  print(topic_data)
  pass

m5mqtt = M5mqtt('id_123456', 'broker.emqx.io', 1883, 'user_123456', 'pwd_123456', 20)
m5mqtt.subscribe(str('/dev/sub'), fun__dev_sub_)
print('mqtt connecting....')
m5mqtt.set_last_will(str('/dev/last_will'),str('device disconnect'))
m5mqtt.start()
print('mqtt connected')
while True:
  m5mqtt.publish(str('/dev/pub'), str('Hello'), 0)
  wait(10)
  wait_ms(2)

```


## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/mqtt/uiflow_block_mqtt_set_client.svg"> 

```python
m5mqtt = M5mqtt('id_123456', 'broker.emqx.io', 1883, 'user_123456', 'pwd_123456', 20)

```

- 初始化 MQTT 客户端信息


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/mqtt/uiflow_block_mqtt_set_client_ssl.svg"> 

```python
m5mqtt = M5mqtt('id_123456', 'broker.emqx.io', 1883, 'user_123456', 'pwd_123456', 20, ssl = True, ssl_params = {'key': "/flash/res/certificate.pem.crt", 'cert': "/flash/res/private.pem.key"})
```

- 若希望初始化 MQTTS 连接，可启用 SSL 选项，并通过`+`号导入客户端证书到设备。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/mqtt/uiflow_block_mqtt_set_last_will.svg"> 

```python
m5mqtt.set_last_will(str('/dev/last_will'),str('device disconnect'))
```

- 设置 MQTT 客户端遗嘱(last will)信息，当客户端异常断开时，服务器将会发布该信息。注： last will 信息需要在 mqtt start 连接前进行配置。


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/mqtt/uiflow_block_mqtt_start.svg"> 

```python
m5mqtt.start()
```

- 开始连接 MQTT 服务器

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/mqtt/uiflow_block_mqtt_publish.svg"> 

```python
m5mqtt.publish(str('/dev/pub'), str('Hello'), 0)
```

- 发布指定 topic 信息，以及配置信息 QoS 级别


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/mqtt/uiflow_block_mqtt_sub.svg"> 

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/advanced/mqtt/uiflow_block_mqtt_get_topic_data.svg"> 

```python
def fun__dev_sub_(topic_data):
  print(topic_data)
  pass

m5mqtt.subscribe(str('/dev/sub'), fun__dev_sub_)
```

- 订阅主题信息，并配置对应的回调函数，当接收到该主题消息将自动执行。

