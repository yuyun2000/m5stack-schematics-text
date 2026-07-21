# [Module COMX Cat1](/zh_CN/module/comx_cat1)

## 案例程序

初始化 MQTT 连接。<br/>订阅指定主题，并通过 MQTT 发布消息。<br/>在循环中，生成一个随机数作为计数器值，如果计数器值不同于之前的值，则将其发布到指定的主题。<br/>程序会显示当前计数器值、订阅主题的消息以及 MQTT 连接状态。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_cat1/uiflow_block_comx_cat1_demo.svg">

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_cat1/uiflow_block_comx_cat1_demo1.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
from comx.cat1 import CAT1

setScreenColor(0x222222)

cat_topic = None
cat_msg = None
counter = None
previous = None

import random

def cat_mqtt_cb(cat_mq_topic, cat_mq_payload):
  global cat_topic, cat_msg, counter, previous, cat
  cat_topic = cat_mq_topic
  cat_msg = cat_mq_payload
  label5.setText(str(cat_topic))
  label7.setText(str(cat_msg))
  pass

print('Start Mqtt')
counter = 0
previous = 0
cat = CAT1(tx=17, rx=16)
cat.mqtt_to_connect('mqtt.m5stack.com', 1883, 'mqtt_m9', '', '', 120)
if cat.is_connect_mqtt():
  print('Connected Mqtt')
while not (cat.mqtt_subscribe('SubTopic', cat_mqtt_cb, 0)):
  cat.mqtt_unsubscribe('SubTopic')
print('Success Subscribe')
while True:
  cat.mqtt_poll()
  if counter != previous:
    cat.mqtt_publish('PubTopic', str(counter), 0)
    previous = counter
  if cat.is_connect_mqtt():
    print('Connected Mqtt')
  counter = random.randint(100000, 999999)
  print((str('counter：') + str(counter)))
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_cat1/uiflow_block_com_cat1_check_gprs_network_registration.svg">

```python
cat.get_gprs_network_registration()
```

- 检查 GPRS 网络注册状态。用于确认设备是否已经成功注册到 GPRS 网络中

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_cat1/uiflow_block_com_cat1_check_network_registration.svg">

```python
cat.get_network_registration()
```

- 检查网络注册状态。用于确认设备是否已经成功注册到网络中，这可能包括 GPRS、LTE 等不同网络类型

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_cat1/uiflow_block_com_cat1_check_single_quality.svg">

```python
cat.get_single_quality()
```

- 检查信号质量。返回当前网络信号的强度，以评估设备与网络的连接质量

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_cat1/uiflow_block_com_cat1_check_status.svg">

```python
cat.check_status()
```

- 检查模块状态。用于获取模块的当前工作状态，确认是否正常运行

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_cat1/uiflow_block_com_cat1_enable_pdp_context.svg">

```python
cat.enable_PDP_context()
```

- 启用 PDP 上下文。PDP 上下文通常用于数据传输，启用后，设备可以通过网络进行数据通信

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_cat1/uiflow_block_com_cat1_ezdata_async_get_value.svg">

```python
cat.get_ezdata(ezdata_get_IklJVcb, 'GCJ3Ic5h2eXnzV3rT3bBXvrncCaJnART', '')
```

- 通过提供的主题名称和令牌，异步获取与该主题相关的值。此操作通常用于从云端或远程服务器获取特定数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_cat1/uiflow_block_com_cat1_ezdata_remove.svg">

```python
cat.remove_ezdata('GCJ3Ic5h2eXnzV3rT3bBXvrncCaJnART', '')
```

- 使用提供的令牌，从指定的主题中移除数据或取消订阅。此操作用于管理数据存储或流量，确保不再需要的主题不会继续占用资源

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_cat1/uiflow_block_com_cat1_ezdata_save.svg">

```python
at.set_ezdata('GCJ3Ic5h2eXnzV3rT3bBXvrncCaJnART', '', '', 0)
```

- 将指定的值保存到主题中，并通过令牌进行认证。可以选择保存数据的模式，例如单次保存或连续保存。此功能通常用于将数据上传到云端或远程服务器

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_cat1/uiflow_block_com_cat1_get_ccid.svg">

```python
cat.get_CCID()
```

- 获取设备的 CCID(集成电路卡标识)，这是一个唯一的 SIM 卡标识符，用于识别移动网络中的 SIM 卡

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_cat1/uiflow_block_com_cat1_get_imei.svg">

```python
cat.get_IMEI()
```

- 获取设备的 IMEI(国际移动设备识别码)，这是一个唯一的设备标识符，用于识别设备在移动网络中的身份

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_cat1/uiflow_block_com_cat1_http_get.svg">

```python
cat.http_get('')
```

- 发送一个 HTTP 或 HTTPS GET 请求到指定的 URL，用于从服务器获取数据。可以通过 URL 参数来指定要请求的资源

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_cat1/uiflow_block_com_cat1_http_post.svg">

```python
cat.http_post('', 'application/json', '')
```

- 发送一个 HTTP 或 HTTPS POST 请求到指定的 URL，带有 JSON 格式的数据，用于将数据上传到服务器。POST 请求通常用于提交表单数据或上传数据到服务器

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_cat1/uiflow_block_com_cat1_http_terminate.svg">

```python
cat.http_terminate()
```

- 终止当前的 HTTP 或 HTTPS 会话，释放资源。这在完成数据传输后，用于确保会话被正确关闭

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_cat1/uiflow_block_com_cat1_init.svg">

```python
CAT1(tx=17, rx=16)
```

- 初始化 Cat1模块的 TX 和 RX 引脚，用于设定串口通信的引脚编号。此模块通常用于与 Cat1模块进行串口通信

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_cat1/uiflow_block_com_cat1_mqtt_check_connect.svg">

```python
cat.is_connect_mqtt()
```

- 检查当前的 MQTT 连接状态，确保设备是否已经成功连接到 MQTT 服务器

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_cat1/uiflow_block_com_cat1_mqtt_connect.svg">

```python
cat.mqtt_to_connect('mqtt.m5stack.com', 1883, '', '', '', 120)
```

- 初始化 MQTT 服务器的连接设置，包括服务器地址(mqtt.m5stack.com)、端口号(1883)、客户端 ID、用户名、密码，以及保持连接的时间(keepalive)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_cat1/uiflow_block_com_cat1_mqtt_disconnect.svg">

```python
cat.mqtt_disconnect()
```

- 断开与 MQTT 服务器的连接，用于结束 MQTT 会话

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_cat1/uiflow_block_com_cat1_mqtt_poll.svg">

```python
cat.mqtt_poll()
```

- 检查并获取下行消息，即从 MQTT 服务器发送到设备的消息。用于接收消息

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_cat1/uiflow_block_com_cat1_mqtt_publish.svg">

```python
cat.mqtt_publish('', '', 0)
```

- 将消息发布到指定的 MQTT 主题(topic)上。可以设定主题名称和发送的消息内容(payload)，并可选择消息的 QoS(服务质量)等级

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_cat1/uiflow_block_com_cat1_mqtt_sub.svg">

```python
cat.mqtt_subscribe('', cat_mqtt_cb, 0)
```

- 订阅指定的 MQTT 主题。设备将接收发布在这个主题上的所有消息。可以设定主题名称，并选择 QoS 等级

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_cat1/uiflow_block_com_cat1_mqtt_sub_cb.svg">

```python
def cat_mqtt_cb(cat_mq_topic, cat_mq_payload):
  global ezdata_value1, cat_topic, cat_msg, cat
  cat_topic = cat_mq_topic
  cat_msg = cat_mq_payload
  pass
```

- 设置订阅主题的回调函数。当设备接收到指定主题的消息时，会调用此回调函数处理消息。在此块中，cat_topic 表示主题，cat_msg 表示接收到的消息

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_cat1/uiflow_block_com_cat1_mqtt_unsubscribe.svg">

```python
cat.mqtt_unsubscribe('')
```

- 取消订阅指定的 MQTT 主题。设备将不再接收这个主题上的消息

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_cat1/uiflow_block_com_cat1_power_down_module.svg">

```python
cat.poweroff()
```

- 关闭模块电源，使模块进入低功耗模式。这可以节省能源，但模块将无法执行任务

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_cat1/uiflow_block_com_cat1_reset_module.svg">

```python
cat.reset()
```

- 重置模块，类似于重新启动设备。通常用于恢复模块的初始状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/comx_cat1/uiflow_block_com_cat1_set_echo_mode.svg">

```python
cat.set_command_echo_mode(0)
```

- 设置命令回显模式。当开启时，模块会在执行每个命令后回显命令输入。关闭时，模块不再回显命令输入

