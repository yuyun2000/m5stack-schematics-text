# [Unit NbIoT2](/zh_CN/unit/Unit%20NB-IoT2(SIM7028))

## 案例程序

连接MQTT发送订阅消息

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/nb_iot2/uiflow_nbiot2_example.svg">

```python
from m5stack import *
from m5stack_ui import *
from uiflow import *
import unit

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
nbiot2_0 = unit.get(unit.NBIOT2, unit.PORTC)

nbiot2_0.mqtt_service_config('mqtt.m5stack.com', 1883, '', '', '', 120)
while True:
  if True & (nbiot2_0.mqtt_server_is_connect()):
    nbiot2_0.mqtt_publish_topic('nbiot001', 'test', 0)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/nb_iot2/uiflow_block_unit_nbiot2_check_SIM_card.svg">

```python
print((str('card status:') + str((nbiot2_0.check_SIM_card()))))
```

- 检查调制解调器 SIM 卡状态（返回 true 或 false）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/nb_iot2/uiflow_block_unit_nbiot2_debug.svg">

```python
nbiot2_0.debug = True
```

- 启用 AT 命令调试打印功能

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/nb_iot2/uiflow_block_unit_nbiot2_get_gprs_status.svg">

```python
print((str('network status:') + str((nbiot2_0.get_gprs_status()))))
```

- 获取 GPRS 网络状态（返回整型值）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/nb_iot2/uiflow_block_unit_nbiot2_get_identification.svg">

```python
print((str('model identification:') + str((nbiot2_0.get_identification()))))
```

- 获取型号标识（返回字符串）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/nb_iot2/uiflow_block_unit_nbiot2_get_IMEI.svg">

```python
print((str('identification number:') + str((nbiot2_0.get_IMEI()))))
```

- 获取识别号（返回字符串）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/nb_iot2/uiflow_block_unit_nbiot2_get_PDP_context_ip.svg">

```python
print((str('cid:') + str((nbiot2_0.get_PDP_context_ip(0)))))
```

- 获取 PDP 上下文 ID 为 0 的 IP 地址（返回字符串）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/nb_iot2/uiflow_block_unit_nbiot2_get_single_quality.svg">

```python
print((str('signal strength:') + str((nbiot2_0.get_single_quality()))))
```

- 获取信号强度（返回整型值）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/nb_iot2/uiflow_block_unit_nbiot2_http_data.svg">

```python
print((str('data content:') + str((nbiot2_0.http_data))))
```

- 获取 HTTP 数据内容（返回字符串）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/nb_iot2/uiflow_block_unit_nbiot2_http_request.svg">

```python
nbiot2_0.http_request(0, '', {}, {})
```

- 发送HTTP网络请求

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/nb_iot2/uiflow_block_unit_nbiot2_http_status_code.svg">

```python
print((str('response status:') + str((nbiot2_0.http_status_code))))
```

- 使用 GET 方法发起 HTTP 请求并获取 URL 头部数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/nb_iot2/uiflow_block_unit_nbiot2_http_terminate.svg">

```python
nbiot2_0.http_terminate()
```

- 检查 HTTP 服务器是否已终止

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/nb_iot2/uiflow_block_unit_nbiot2_mqtt_poll.svg">

```python
nbiot2_0.mqtt_poll()
```

- MQTT 轮询循环

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/nb_iot2/uiflow_block_unit_nbiot2_mqtt_publish_topic.svg">

```python
nbiot2_0.mqtt_publish_topic('', '', 0)
```

- MQTT 发布主题、负载和 QoS 等级

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/nb_iot2/uiflow_block_unit_nbiot2_mqtt_server_disconnect.svg">

```python
nbiot2_0.mqtt_server_disconnect()
```

- 断开与 MQTT 服务器的连接

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/nb_iot2/uiflow_block_unit_nbiot2_mqtt_server_is_connect.svg">

```python
print((str('server status:') + str((nbiot2_0.mqtt_server_is_connect()))))
```

- 检查 MQTT 服务器是否已连接（返回 true 或 false）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/nb_iot2/uiflow_block_unit_nbiot2_mqtt_service_config.svg">

```python
nbiot2_0.mqtt_service_config('mqtt.m5stack.com', 1883, '', '', '', 120)
```

- 配置MQTT

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/nb_iot2/uiflow_block_unit_nbiot2_mqtt_service_connect.svg">

```python
nbiot2_0.mqtt_server_connect(0)
```

- 连接到 MQTT 服务器并禁用清理会话

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/nb_iot2/uiflow_block_unit_nbiot2_mqtt_subscribe_topic.svg">

```python
nbiot2_0.mqtt_subscribe_topic('', nbiot2_0_mqtt_cb_func, 0)
```

- 订阅 MQTT 主题并指定 QoS 等级

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/nb_iot2/uiflow_block_unit_nbiot2_mqtt_subscribe_topic_cb.svg">

```python
def nbiot2_0_mqtt_cb_func(mq_topic, mq_payload):
  global nbiot_topic, nbiot_msg
  nbiot_topic = mq_topic
  nbiot_msg =  mq_payload
  pass
```

- 接收订阅消息

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/nb_iot2/uiflow_block_unit_nbiot2_mqtt_unsubscribe_topic.svg">

```python
nbiot2_0.mqtt_unsubscribe_topic('')
```

-  取消订阅 MQTT 主题

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/nb_iot2/uiflow_block_unit_nbiot2_set_enable_PDP_context.svg">

```python
nbiot2_0.set_enable_PDP_context('cmnbiot')
```

- 设置 PDP 上下文 APN 

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/nb_iot2/uiflow_block_unit_nbiot2_uart_port_id.svg">

```python
nbiot2_0.uart_port_id(1)
```

- 设置核心 UART ID 号为

