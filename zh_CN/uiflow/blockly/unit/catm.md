# [Unit CatM](/zh_CN/unit/cat_m)

## 案例程序

测试 EZData 

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/catm/uiflow_catm_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import time
import unit

setScreenColor(0x222222)
catm_0 = unit.get(unit.CATM, unit.PORTC)

ezdata_value1 = None
ezdata_value2 = None
loop = None
random2 = None

title0 = M5Title(title="CAT-M EZDATA", x=115, fgcolor=0xFFFFFF, bgcolor=0xcf0000)
label3 = M5TextBox(46, 219, "Single", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
label8 = M5TextBox(235, 219, "List", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
label11 = M5TextBox(8, 47, "Random Value:", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
label12 = M5TextBox(130, 47, "Text", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
label0 = M5TextBox(8, 88, "Single Data:", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
label1 = M5TextBox(8, 130, "List Data:", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
label2 = M5TextBox(105, 88, "Text", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)
label4 = M5TextBox(89, 130, "Text", lcd.FONT_Ubuntu, 0xFFFFFF, rotate=0)

import random

def ezdata_get_bvKoUcb(value):
  global ezdata_value1, ezdata_value2, loop, random2
  ezdata_value1 = value
  label2.setText(str(ezdata_value1))
  pass

def ezdata_get_BZTZbcb(value):
  global ezdata_value1, ezdata_value2, loop, random2
  ezdata_value2 = value
  label4.setText(str(ezdata_value2))
  pass

def buttonA_wasPressed():
  global ezdata_value1, ezdata_value2, loop, random2
  catm_0.set_ezdata('orsNTFbxLj1uWSMMGqXFPKEJKzQKSlVl', 'm5_topic_single', str(random2), 0)
  loop = 1
  pass
btnA.wasPressed(buttonA_wasPressed)

def buttonC_wasPressed():
  global ezdata_value1, ezdata_value2, loop, random2
  catm_0.set_ezdata('orsNTFbxLj1uWSMMGqXFPKEJKzQKSlVl', 'm5_topic_list', str(random2), 1)
  loop = 2
  pass
btnC.wasPressed(buttonC_wasPressed)


catm_0.init_modem()
label12.setText(str(catm_0.network_active(0, 0)))
while True:
  if loop == 1:
    catm_0.get_ezdata(ezdata_get_bvKoUcb, 'orsNTFbxLj1uWSMMGqXFPKEJKzQKSlVl', 'm5_topic_single')
    loop = 0
  elif loop == 2:
    catm_0.get_ezdata(ezdata_get_BZTZbcb, 'orsNTFbxLj1uWSMMGqXFPKEJKzQKSlVl', 'm5_topic_list')
    loop = 0
  else:
    random2 = random.randint(10000, 99999)
  label12.setText(str(random2))
  wait_ms(100)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/catm/uiflow_block_unit_catm_coap_init.svg">

```python
catm_0.coap_to_connect('120.77.157.90', 5683)
```

- 初始化CoAP协议

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/catm/uiflow_block_unit_catm_init_module.svg">

```python
catm_0.init_modem()
```

- 初始化模块

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/catm/uiflow_block_unit_catm_uart_init.svg">

```python
catm_0.uart_port_id(1)
```

- 初始化UART串口

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/catm/uiflow_block_unit_catm_check_gprs_network_registration.svg">

```python
print((str('network registration:') + str((catm_0.get_gprs_network_registration()))))
```

- 获取检查GPRS网络注册的状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/catm/uiflow_block_unit_catm_check_network_registration.svg">

```python
print((str('network registration:') + str((catm_0.get_network_registration()))))
```

- 获取检查网络注册的状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/catm/uiflow_block_unit_catm_check_single_quality.svg">

```python
print((str('signal quality:') + str((catm_0.get_single_quality()))))
```

- 获取检查单件的质量

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/catm/uiflow_block_unit_catm_check_status.svg">

```python
print((str('status:') + str((catm_0.check_status()))))
```

- 获取检查模块的状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/catm/uiflow_block_unit_catm_coap_delete.svg">

```python
print(catm_0.delete_coap())
```

- 获取CoAP请求删除状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/catm/uiflow_block_unit_catm_coap_get.svg">

```python
print((str('data:') + str((catm_0.coap_request('/m5stack-get')))))
```

- 获取CoAP GET 请求返回数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/catm/uiflow_block_unit_catm_coap_post.svg">

```python
print((str('data:') + str((catm_0.coap_request('/m5stack-post', 2, '')))))
```

- 获取CoAP POST 请求返回数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/catm/uiflow_block_unit_catm_disconnect_server.svg">

```python
catm_0.disconnect_server()
```

- 断开服务器连接

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/catm/uiflow_block_unit_catm_enable_pdp_context.svg">

```python
catm_0.enable_PDP_context()
```

- 激活PDP上下文

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/catm/uiflow_block_unit_catm_ezdata_async_get_value.svg">

```python
catm_0.get_ezdata(ezdata_get_oghkvcb, 'nfpmn7gVNHlhC5LG9hF7Qax1L6zKInc6', '')
```

- 异步获取EZData值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/catm/uiflow_block_unit_catm_ezdata_remove.svg">

```python
catm_0.remove_ezdata('nfpmn7gVNHlhC5LG9hF7Qax1L6zKInc6', '')
```

- 删除EZData数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/catm/uiflow_block_unit_catm_ezdata_save.svg">

```python
catm_0.set_ezdata('nfpmn7gVNHlhC5LG9hF7Qax1L6zKInc6', '', '', 0)
```

- 保存EZData数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/catm/uiflow_block_unit_catm_get_ccid.svg">

```python
print(catm_0.get_CCID())
```

- 获取SIM卡CCID号码

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/catm/uiflow_block_unit_catm_get_imei.svg">

```python
print(catm_0.get_IMEI())
```

- 获取设备IMEI号

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/catm/uiflow_block_unit_catm_gprs_service.svg">

```python
catm_0.gprs_service(1)
```

- GPRS服务控制

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/catm/uiflow_block_unit_catm_http_services.svg">

```python
print((str('http data:') + str((catm_0.http_service(1, '', '', {}, '')))))
```

- 获取 HTTP 返回数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/catm/uiflow_block_unit_catm_mqtt_check_connection.svg">

```python
print((str('connection status:') + str((catm_0.mqtt_ischeck_connect()))))
```

- 获取MQTT连接状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/catm/uiflow_block_unit_catm_mqtt_connect.svg">

```python
catm_0.mqtt_to_connect('mqtt.m5stack.com', 1883, '', '', '', 120)
```

- 建立MQTT连接

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/catm/uiflow_block_unit_catm_mqtt_disconnect.svg">

```python
catm_0.mqtt_disconnect()
```

- 断开MQTT连接

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/catm/uiflow_block_unit_catm_mqtt_poll.svg">

```python
catm_0.mqtt_poll()
```

- MQTT轮询操作

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/catm/uiflow_block_unit_catm_mqtt_publish.svg">

```python
catm_0.mqtt_publish('', '', 0)
```

- MQTT消息发布

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/catm/uiflow_block_unit_catm_mqtt_sub.svg">

```python
print((str('status:') + str((catm_0.mqtt_subscribe('', catm_0_mqtt_cb, 0)))))
```

- MQTT订阅主题

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/catm/uiflow_block_unit_catm_mqtt_sub_cb.svg">

```python
def catm_0_mqtt_cb(catm_mq_topic, catm_mq_payload):
  global catm_topic, catm_msg
  catm_topic = catm_mq_topic
  catm_msg = catm_mq_payload
  pass
```

- MQTT订阅回调设置

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/catm/uiflow_block_unit_catm_mqtt_unsubscribe.svg">

```python
catm_0.mqtt_unsubscribe('')
```

- MQTT取消订阅

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/catm/uiflow_block_unit_catm_network_active.svg">

```python
print((str('status:') + str((catm_0.network_active(0, 1)))))
```

- 获取网络激活状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/catm/uiflow_block_unit_catm_network_ip_id.svg">

```python
print((str('id:') + str((catm_0.get_network_ip(0)))))
```

- 获取网络IP标识

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/catm/uiflow_block_unit_catm_power_down_module.svg">

```python
catm_0.poweroff()
```

- 模块关机

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/catm/uiflow_block_unit_catm_set_echo_mode.svg">

```python
print((str('status:') + str((catm_0.set_command_echo_mode(0)))))
```

- 获取关闭命令回显模式状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/catm/uiflow_block_unit_catm_show_pdp_address.svg">

```python
catm_0.enable_PDP_context()
```

- 获取显示的PDP地址

