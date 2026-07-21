# [Hat CBack Nbiot](/zh_CN/hat/C-BACK%20NB-IoT(SIM7020G))

## 案例程序

该程序通过 MQTT 连接服务器，订阅特定主题，在按钮 A 被按下时生成一个随机数并发布到主题中，同时显示在串口上。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/cback_nbiot/uiflow_block_hat_cback_nbiot_demo.png">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import hat

setScreenColor(0xffffff)

nb = hat.get(hat.CBACK_NBIOT)

nb_topic = None
nb_msg = None
counter = None
previous = None

import random


def hat_cbacknbiot_mqtt_cb(nb_mq_topic, nb_mq_payload):
  global nb_topic, nb_msg, counter, previous
  nb_topic = nb_mq_topic
  nb_msg = nb_mq_payload
  print(nb_topic)
  print(nb_msg)
  pass

def buttonA_wasPressed():
  global nb_topic, nb_msg, counter, previous
  counter = random.randint(100000, 999999)
  print(counter)
  label2.setText(str(counter))
  pass
btnA.wasPressed(buttonA_wasPressed)

counter = 0
previous = 0
nb.mqtt_to_connect('mqtt.m5stack.com', 1883, 'm5_mqtt999', '', '', 120)
if nb.mqtt_check_connection():
  print('Connected')
while not (nb.mqtt_subscribe('SubTopic', hat_cbacknbiot_mqtt_cb, 0)):
  nb.mqtt_unsubscribe('SubTopic')
print('Subscribed')
while True:
  nb.mqtt_poll()
  if counter != previous:
    nb.mqtt_publish('PubTopic', str(counter), 0)
    previous = counter
  wait_ms(2)

```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/cback_nbiot/uiflow_block_hat_cbacknbiot_coap_init_ip.svg">

```python
print((str('ip:') + str((nb.coap_to_connect('120.77.157.90', 5683)))))
```

- 使用 IP 设置初始化 CoAP

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/cback_nbiot/uiflow_block_cbacknbiot_ezdata_async_get_value.svg">

```python
def ezdata_get_jsdbZcb(value):
  global ezdata_value1
  ezdata_value1 = value
  pass

nb.get_ezdata(ezdata_get_jsdbZcb, 'wCGubMfa3ExoVXuEzuYQy4zm7cumT5FI', '')
```

- 从 ezdata 异步获取值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/cback_nbiot/uiflow_block_hat_cbacknbiot_check_gprs_network_registration.svg">

```python
print((str('registration:') + str((nb.get_gprs_network_registration()))))
```

- 检查 GPRS 网络注册状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/cback_nbiot/uiflow_block_hat_cbacknbiot_check_network_registration.svg">

```python
print((str('registration:') + str((nb.get_network_registration()))))
```

- 检查网络注册状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/cback_nbiot/uiflow_block_hat_cbacknbiot_check_single_quality.svg">

```python
print((str('quality:') + str((nb.get_single_quality()))))
```

- 评估信号质量

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/cback_nbiot/uiflow_block_hat_cbacknbiot_check_status.svg">

```python
print((str('status:') + str((nb.check_status()))))
```

- 检查设备状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/cback_nbiot/uiflow_block_hat_cbacknbiot_coap_destroy.svg">

```python
print(nb.coap_destroy())
```

- 销毁 CoAP 资源

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/cback_nbiot/uiflow_block_hat_cbacknbiot_coap_get.svg">

```python
print((str('get:') + str((nb.coap_get('/m5stack-get')))))
```

- 检索 CoAP 数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/cback_nbiot/uiflow_block_hat_cbacknbiot_coap_post.svg">

```python
print((str('post:') + str((nb.coap_post('/m5stack-post', '', content_format=0)))))
```

- 提交 CoAP 数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/cback_nbiot/uiflow_block_hat_cbacknbiot_coap_put.svg">

```python
print((str('put:') + str((nb.coap_put('/m5stack-put', '', content_format=0)))))
```

- 更新 CoAP 数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/cback_nbiot/uiflow_block_hat_cbacknbiot_destroy_https.svg">

```python
nb.destroy_https()
```

- 销毁 HTTPS 连接

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/cback_nbiot/uiflow_block_hat_cbacknbiot_disconnect_server.svg">

```python
print((str('connect:') + str((nb.disconnect_server()))))
```

- 断开服务器连接

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/cback_nbiot/uiflow_block_hat_cbacknbiot_ezdata_remove.svg">

```python
nb.remove_ezdata('wCGubMfa3ExoVXuEzuYQy4zm7cumT5FI', '')
```

- 从 ezdata 中移除数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/cback_nbiot/uiflow_block_hat_cbacknbiot_ezdata_save.svg">

```python
nb.set_ezdata('wCGubMfa3ExoVXuEzuYQy4zm7cumT5FI', '', '', 0)
```

- 将数据保存到 ezdata

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/cback_nbiot/uiflow_block_hat_cbacknbiot_get_ccid.svg">

```python
print(nb.get_CCID())
```

- 检索 CCID

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/cback_nbiot/uiflow_block_hat_cbacknbiot_get_imei.svg">

```python
print(nb.get_IMEI())
```

- 检索 IMEI

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/cback_nbiot/uiflow_block_hat_cbacknbiot_http_services.svg">

```python
print((str('http:') + str((nb.http_service(0, '', '', 'application/json', '')))))
```

- HTTP 服务

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/cback_nbiot/uiflow_block_hat_cbacknbiot_modem_power.svg">

```python
nb.modem_power(True)
```

- 调制解调器电源控制

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/cback_nbiot/uiflow_block_hat_cbacknbiot_mqtt_check_connection.svg">

```python
print(nb.mqtt_check_connection())
```

- 检查 MQTT 连接状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/cback_nbiot/uiflow_block_hat_cbacknbiot_mqtt_connect.svg">

```python
nb.mqtt_to_connect('mqtt.m5stack.com', 1883, '', '', '', 120)
```

- 建立 MQTT 连接

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/cback_nbiot/uiflow_block_hat_cbacknbiot_mqtt_disconnect.svg">

```python
nb.mqtt_disconnect()
```

- 断开 MQTT 连接

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/cback_nbiot/uiflow_block_hat_cbacknbiot_mqtt_poll.svg">

```python
nb.mqtt_poll()
```

- 轮询 MQTT 消息

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/cback_nbiot/uiflow_block_hat_cbacknbiot_mqtt_publish.svg">

```python
nb.mqtt_publish('', '', 0)
```

- 发布 MQTT 消息

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/cback_nbiot/uiflow_block_hat_cbacknbiot_mqtt_sub.svg">

```python
print((str('mqtt:') + str((nb.mqtt_subscribe('', hat_cbacknbiot_mqtt_cb, 0)))))
```

- 订阅 MQTT 主题

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/cback_nbiot/uiflow_block_hat_cbacknbiot_mqtt_sub_cb.svg">

```python
def hat_cbacknbiot_mqtt_cb(nb_mq_topic, nb_mq_payload):
  global nb_topic, nb_msg
  nb_topic = nb_mq_topic
  nb_msg = nb_mq_payload
  pass
```

- 设置 MQTT 订阅回调

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/cback_nbiot/uiflow_block_hat_cbacknbiot_mqtt_unsubscribe.svg">

```python
nb.mqtt_unsubscribe('')
```

- 取消订阅 MQTT 主题

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/cback_nbiot/uiflow_block_hat_cbacknbiot_power_down_module.svg">

```python
nb.poweroff()
```

- 关闭模块电源

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/cback_nbiot/uiflow_block_hat_cbacknbiot_reset_module.svg">

```python
nb.reset()
```

- 重置模块

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/cback_nbiot/uiflow_block_hat_cbacknbiot_set_echo_mode.svg">

```python
print((str('status:') + str((nb.set_command_echo_mode(0)))))
```

- 设置回显模式

