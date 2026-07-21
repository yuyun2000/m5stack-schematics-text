# [Module COMX NB IoT](/zh_CN/module/comx_nb-iot)

## 案例程序

通过 NB-IoT 模块连接到指定的 CoAP 服务器 IP 地址 120.77.157.90，端口 5683，并依次发送 GET 请求、带有 post-test 数据的 POST 请求，以及带有 put-test 数据的 PUT 请求，均采用纯文本格式传输数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_nb_iot/uiflow_block_comx_nbiot_demo.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
from comx.nbiot import NBIoT

setScreenColor(0x222222)

nb = NBIoT(tx=13, rx=5)
if nb.coap_connect('120.77.157.90', 5683):
  print(nb.coap_get('/m5stack-get'))
  print(nb.coap_post('/m5stack-post', 'post-test', content_format=0))
  print(nb.coap_put('/m5stack-put', 'put-test', content_format=0))
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_nb_iot/uiflow_block_nbiot_check_gprs_network_registration.svg">

```python
nb.get_gprs_network_registration()
```

- 检查 GPRS 网络注册状态，返回设备是否已经成功注册到 GPRS 网络

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_nb_iot/uiflow_block_nbiot_check_network_registration.svg">

```python
nb.get_network_registration()
```

- 检查网络注册状态，返回设备是否已经成功注册到任何网络

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_nb_iot/uiflow_block_nbiot_check_single_quality.svg">

```python
nb.get_single_quality()
```

- 检查信号质量，返回当前网络信号的强度，以评估连接的可靠性

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_nb_iot/uiflow_block_nbiot_check_status.svg">

```python
nb.check_status()
```

- 检查模块状态，返回设备当前的运行状态，以判断设备是否正常工作

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_nb_iot/uiflow_block_nbiot_coap_connect_ip.svg">

```python
nb.coap_connect('', 5683)
```

- 使用 CoAP 协议连接到指定的 IP 地址和端口。CoAP(Constrained Application Protocol)是一种轻量级协议，常用于物联网设备之间的数据传输

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_nb_iot/uiflow_block_nbiot_coap_destroy.svg">

```python
nb.coap_destroy()
```

- 断开与 CoAP 服务器的连接并销毁 CoAP 会话

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_nb_iot/uiflow_block_nbiot_coap_get.svg">

```python
nb.coap_get('')
```

- 使用 GET 请求从指定的 URL 获取数据，可以选择是否使用安全连接

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_nb_iot/uiflow_block_nbiot_coap_post.svg">

```python
nb.coap_post('', '', content_format=0)
```

- 使用 POST 请求向指定的 URL 发送数据，指定数据的内容格式(例如，纯文本)，并可以选择是否使用安全连接

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_nb_iot/uiflow_block_nbiot_coap_put.svg">

```python
nb.coap_put('', '', content_format=0)
```

- 使用 PUT 请求向指定的 URL 上传数据，指定数据的内容格式，并可以选择是否使用安全连接

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_nb_iot/uiflow_block_nbiot_init.svg">

```python
NBIoT(tx=13, rx=5)
```

- 初始化 NB-IoT 模块，设置传输(TX)和接收(RX)的引脚编号，用于串行通信

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_nb_iot/uiflow_block_nbiot_mqtt_check_connection.svg">

```python
nb.mqtt_check_connection()
```

- 检查当前的 MQTT 连接状态，确认设备是否已成功连接到 MQTT 服务器

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_nb_iot/uiflow_block_nbiot_mqtt_connect.svg">

```python
nb.mqtt_connect('', 1883, '', '', '', 0)
```

- 连接到指定的 MQTT 服务器，使用提供的端口、客户端 ID、用户名、密码以及保活间隔(keepalive)。常见的 MQTT 端口为1883

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_nb_iot/uiflow_block_nbiot_mqtt_disconnect.svg">

```python
nb.mqtt_disconnect()
```

- 断开与当前 MQTT 服务器的连接

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_nb_iot/uiflow_block_nbiot_mqtt_poll.svg">

```python
nb.mqtt_poll()
```

- 轮询从服务器下发的消息，即检查服务器是否有新的消息发送给设备

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_nb_iot/uiflow_block_nbiot_mqtt_publish.svg">

```python
nb.mqtt_publish('', '', 0)
```

- 发布消息到指定的 MQTT 主题(topic)。消息的内容由 payload 指定，QoS(服务质量)定义了消息传输的可靠性等级

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_nb_iot/uiflow_block_nbiot_mqtt_sub.svg">

```python
nb.mqtt_subscribe('', nbiot_mqtt_cb, 0)
```

- 订阅指定的 MQTT 主题，并设置消息传输的服务质量等级(QoS)。设备将接收到这个主题的所有消息

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_nb_iot/uiflow_block_nbiot_mqtt_sub_cb.svg">

```python
def nbiot_mqtt_cb(nb_mq_topic, nb_mq_payload):
  global nb_topic, nb_msg, nb
  nb_topic = nb_mq_topic
  nb_msg = nb_mq_payload
  pass
```

- 在订阅特定主题时设置回调函数，nb_topic 是主题变量，nb_msg 是消息变量。当订阅的主题接收到消息时，执行相应的操作

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_nb_iot/uiflow_block_nbiot_mqtt_unsubscribe.svg">

```python
nb.mqtt_unsubscribe('')
```

- 取消订阅指定的 MQTT 主题，不再接收这个主题的消息

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_nb_iot/uiflow_block_nbiot_power_down_module.svg">

```python
nb.poweroff()
```

- 关闭 NB-IoT 模块，进入低功耗状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_nb_iot/uiflow_block_nbiot_reset_module.svg">

```python
nb.reset()
```

- 重置 NB-IoT 模块，使其重新启动并恢复到初始状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_nb_iot/uiflow_block_nbiot_set_echo_mode.svg">

```python
nb.set_command_echo_mode(0)
```

- 设置命令回显模式，可以选择开启或关闭。回显模式决定模块是否在接收命令后返回原始命令字符串

