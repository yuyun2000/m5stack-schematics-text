# [Unit MQTT](/zh_CN/unit/mqtt)

## 案例程序

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/mqtt/uiflow_mqtt_example.svg">

```python
from m5stack import *
from m5stack_ui import *
from uiflow import *
import unit

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
mqtt_0 = unit.get(unit.MQTT_ETH, 1, unit.PORTC)

mqtt_0.MqttStop()
while not (mqtt_0.isConnectLAN()):
  print('waiting LAN connection')
mqtt_0.configMQTT('mqtt.m5stack.com', 1883, 'unit_mqtt_id', '', '', 30,)
while not (mqtt_0.subscribe(1, 'mqtt_unit_down', unit_mqtt_cb, 0)):
  print('waiting subcribe topic')
while not (mqtt_0.saveParam()):
  print('waiting save configure')
mqtt_0.MqttStart()
while not (mqtt_0.isConnectMQTT()):
  print('waiting MQTT connection')
print('MQTT connected!')
while True:
  mqtt_0.publish('mqtt_unit_up', 'hello', 0)
  print(mqtt_0.receive_mqtt_message(5))
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/mqtt/uiflow_block_unit_mqtt_uart_init.svg">

```python
mqtt_0.uart_port_id(1)
```

- 设置主机传感器ID

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/mqtt/uiflow_block_unit_mqtt_cb_loop.svg">

```python
mqtt_0.Mqtt_cb_Loop()
```

- 回调轮询

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/mqtt/uiflow_block_unit_mqtt_config.svg">

```python
mqtt_0.configMQTT('', 0, '', '', '', 0,)
```

- 创建 MQTTUnit 对象
  - client_id （str） – 连接到 时使用的唯一客户端 ID 字符串 经纪人。
  - Server （STR） （服务器 （STR） – 远程代理的主机名或 IP 地址。
  - port （int） – 要连接的服务器主机的网络端口。
  - username （str 或 None） – 用于代理身份验证的用户名。
  - password （str 或 None） – 用于代理身份验证的密码。
  - keepalive （int） – 允许的最大时间段（以秒为单位） 与经纪人的通信。如果没有其他消息 正在交换，这控制了 客户端将向 Broker 发送 ping 消息。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/mqtt/uiflow_block_unit_mqtt_is_lan_connect.svg">

```python
print((str('LAN:') + str((mqtt_0.isConnectLAN()))))
```

- 获取检查LAN连接状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/mqtt/uiflow_block_unit_mqtt_is_mqtt_connect.svg">

```python
print((str('MQTT:') + str((mqtt_0.isConnectMQTT()))))
```

- 获取MQTT连接状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/mqtt/uiflow_block_unit_mqtt_publish.svg">

```python
mqtt_0.publish('', '', 0)
```

- 发布消息

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/mqtt/uiflow_block_unit_mqtt_save_param.svg">

```python
print((str('parameter:') + str((mqtt_0.saveParam()))))
```

- 保存配置参数

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/mqtt/uiflow_block_unit_mqtt_start.svg">

```python
mqtt_0.MqttStart()
```

- 启动MQTT

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/mqtt/uiflow_block_unit_mqtt_stop.svg">

```python
mqtt_0.MqttStop()
```

- 关闭MQTT

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/mqtt/uiflow_block_unit_mqtt_subscribe.svg">

```python
print((str('msg:') + str((mqtt_0.subscribe(1, '', unit_mqtt_cb, 0)))))
```

- 获取订阅消息

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/mqtt/uiflow_block_unit_mqtt_sub_cb.svg">

```python
def unit_mqtt_cb(mq_topic, mq_payload):
  global mqtt_topic, mqtt_msg
  mqtt_topic = mq_topic
  mqtt_msg = mq_payload
  pass
```

- 发布订阅消息

