# [Unit NbIoT](/zh_CN/unit/nbiot_global)

## 案例程序

CoAP 测试

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/nb_iot/uiflow_nbiot_example01.svg">

```python
from m5stack import *
from m5stack_ui import *
from uiflow import *
import unit

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
NBIoT_0 = unit.get(unit.NBIOT, unit.PORTA)

if NBIoT_0.coap_connect('120.77.157.90', 5683):
  print(NBIoT_0.coap_get('/m5stack-get'))
  print(NBIoT_0.coap_post('/m5stack-post', 'post-test', content_format=0))
  print(NBIoT_0.coap_put('/m5stack-put', 'put-test', content_format=0))
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/nb_iot/uiflow_block_unit_nbiot_uart_init.svg">

```python
NBIoT_0.uart_port_id(1)
```

- 配置核心UART接口ID编号

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/nb_iot/uiflow_block_unit_nbiot_check_gprs_network_registration.svg">

```python
print((str('GPRS:') + str((NBIoT_0.get_gprs_network_registration()))))
```

- 查询GPRS网络注册状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/nb_iot/uiflow_block_unit_nbiot_check_network_registration.svg">

```python
print((str('network registration:') + str((NBIoT_0.get_network_registration()))))
```

- 查询网络注册状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/nb_iot/uiflow_block_unit_nbiot_check_single_quality.svg">

```python
print((str('single quality:') + str((NBIoT_0.get_single_quality()))))
```

- 检测信号质量

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/nb_iot/uiflow_block_unit_nbiot_check_status.svg">

```python
print((str('status:') + str((NBIoT_0.check_status()))))
```

- 查询模块运行状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/nb_iot/uiflow_block_unit_nbiot_coap_connect_ip.svg">

```python
print((str('connect status:') + str((NBIoT_0.coap_connect('', 5683)))))
```

- CoAP协议连接指定IP及端口

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/nb_iot/uiflow_block_unit_nbiot_coap_destroy.svg">

```python
print((str('destroy status:') + str((NBIoT_0.coap_destroy()))))
```

- 终止CoAP连接

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/nb_iot/uiflow_block_unit_nbiot_coap_get.svg">

```python
print((str('get status:') + str((NBIoT_0.coap_get('')))))
```

- 发起无加密的CoAP GET请求到指定URL

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/nb_iot/uiflow_block_unit_nbiot_coap_post.svg">

```python
print((str('post status:') + str((NBIoT_0.coap_post('', '', content_format=0)))))
```

- 向指定URL发送纯文本格式的POST请求

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/nb_iot/uiflow_block_unit_nbiot_coap_put.svg">

```python
print((str('put status:') + str((NBIoT_0.coap_put('', '', content_format=0)))))
```

- 向指定URL发送纯文本格式的PUT请求

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/nb_iot/uiflow_block_unit_nbiot_mqtt_check_connection.svg">

```python
print((str('is connection:') + str((NBIoT_0.mqtt_check_connection()))))
```

- 查询MQTT连接状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/nb_iot/uiflow_block_unit_nbiot_mqtt_connect.svg">

```python
NBIoT_0.mqtt_connect('', 1883, '', '', '', 0)
```

- 设置 MQTT 服务器的 MQTT 服务器地址、端口号、客户端 ID、用户名、密码和保活时间
 - server：服务器地址为字符串格式
 - port：端口号为 int 格式
 - client_id：客户端 ID 为字符串格式
 - username：username 为字符串格式
 - passwd：密码为字符串格式
 - keepalive：seconds 为 int 格式

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/nb_iot/uiflow_block_unit_nbiot_mqtt_disconnect.svg">

```python
NBIoT_0.mqtt_disconnect()
```

- 取消MQTT连接

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/nb_iot/uiflow_block_unit_nbiot_mqtt_poll.svg">

```python
NBIoT_0.mqtt_poll()
```

- 轮询获取下行MQTT消息

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/nb_iot/uiflow_block_unit_nbiot_mqtt_publish.svg">

```python
NBIoT_0.mqtt_publish('', '', 0)
```

- 发布MQTT订阅消息
 - topic：MQTT 主题
 - payload：消息内容
 - QoS：服务质量等级

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/nb_iot/uiflow_block_unit_nbiot_mqtt_sub.svg">

```python
print((str('MQTT subscribe:') + str((NBIoT_0.mqtt_subscribe('', unit_nbiot_mqtt_cb, 0)))))
```

- 订阅指定主题并设置QoS等级

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/nb_iot/uiflow_block_unit_nbiot_mqtt_sub_cb.svg">

```python
def unit_nbiot_mqtt_cb(nb_mq_topic, nb_mq_payload):
  global nb_topic, nb_msg
  nb_topic = nb_mq_topic
  nb_msg = nb_mq_payload
  pass
```

- 订阅主题设置回调函数

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/nb_iot/uiflow_block_unit_nbiot_mqtt_unsubscribe.svg">

```python
NBIoT_0.mqtt_unsubscribe('')
```

- 取消订阅指定主题

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/nb_iot/uiflow_block_unit_nbiot_power_down_module.svg">

```python
NBIoT_0.poweroff()
```

- 关闭模块电源

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/nb_iot/uiflow_block_unit_nbiot_reset_module.svg">

```python
NBIoT_0.reset()
```

- 复位模块

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/nb_iot/uiflow_block_unit_nbiot_set_echo_mode.svg">

```python
print((str('echo module:') + str((NBIoT_0.set_command_echo_mode(0)))))
```

- 开启/关闭AT命令回显功能

