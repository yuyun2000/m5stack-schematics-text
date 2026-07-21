# [Unit PoESP32](/zh_CN/unit/poesp32)

## 案例程序

<img class="blockly_svg" src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/832/uiflow_block_poesp32.png">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import unit

setScreenColor(0x222222)
poesp32_1 = unit.get(unit.TCP_ETH, 1, unit.PORTA)

poesp32_mqtt_value1 = None
timer_100ms_counter = None

title0 = M5Title(title="Unit POESP32", x=100, fgcolor=0xFFFFFF, bgcolor=0x0000FF)
label0 = M5TextBox(11, 58, "MQTT subscribe topic:", lcd.FONT_Default, 0xFFFFFF, rotate=0)
label1 = M5TextBox(187, 58, "PoESP32_MQTT_D", lcd.FONT_Default, 0x0af60b, rotate=0)
label2 = M5TextBox(11, 87, "publish message:", lcd.FONT_Default, 0xFFFFFF, rotate=0)
label3 = M5TextBox(157, 87, "hello", lcd.FONT_Default, 0x0af60b, rotate=0)
label4 = M5TextBox(11, 119, "recevied message:", lcd.FONT_Default, 0xFFFFFF, rotate=0)
label5 = M5TextBox(157, 119, "message", lcd.FONT_Default, 0x0af60b, rotate=0)

from numbers import Number
import random

def poesp32_blKNXcb(value):
  global poesp32_mqtt_value1, timer_100ms_counter
  poesp32_mqtt_value1 = value
  print((str('mqtt recevied message: ') + str(poesp32_mqtt_value1)))
  label5.setText(str(poesp32_mqtt_value1))
  pass

@timerSch.event('timer1')
def ttimer1():
  global poesp32_mqtt_value1, timer_100ms_counter
  timer_100ms_counter = (timer_100ms_counter if isinstance(timer_100ms_counter, Number) else 0) + 1
  pass

timer_100ms_counter = 0
timerSch.run('timer1', 100, 0x00)
poesp32_1.create_mqtt_client('120.77.157.90', 1883, ((str('client') + str(random.randint(1000, 9999)))), 'user_name', 'password')
while not (poesp32_1.subscribe_mqtt('PoESP32_MQTT_D', 0)):
  print('...')
print('MQTT Subscribed')
while True:
  if poesp32_1.publish_mqtt_msg('PoESP32_MQTT_D', 'hello', 0):
    print('mqtt message published')
  poesp32_1.receive_mqtt_msg(poesp32_blKNXcb)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/poesp32/uiflow_block_unit_poesp32_mqtt_init.svg">

```python
poesp32_0.create_mqtt_client('', 1883, '', '', '')
```

- mqtt 初始化

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/poesp32/uiflow_block_unit_poesp32_uart_init.svg">

```python
poesp32_0.uart_port_id(1)
```

- 设置核心串口编号

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/poesp32/uiflow_block_unit_poesp32_check_eth.svg">

```python
print(poesp32_0.isConnect_ETH())
```

- 检查以太网连接状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/poesp32/uiflow_block_unit_poesp32_check_uart.svg">

```python
print(poesp32_0.check_uart())
```

- 获取设备状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/poesp32/uiflow_block_unit_poesp32_create_tcp.svg">

```python
print((str('status:') + str((poesp32_0.create_tcp_client('', 0)))))
```

- 获取创建的 TCP 连接状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/poesp32/uiflow_block_unit_poesp32_mqtt_publish.svg">

```python
print((str('mqtt:') + str((poesp32_0.publish_mqtt_msg('', '', 0)))))
```

- 获取 MQTT 发布消息状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/poesp32/uiflow_block_unit_poesp32_mqtt_receive.svg">

```python
def poesp32_WrCiScb(value):
  global poesp32_mqtt_value1
  poesp32_mqtt_value1 = value
  pass

poesp32_0.receive_mqtt_msg(poesp32_WrCiScb)
```

- 接收消息

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/poesp32/uiflow_block_unit_poesp32_mqtt_subscribe.svg">

```python
print((str('mqtt:') + str((poesp32_0.subscribe_mqtt('', 0)))))
```

- 订阅主题

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/poesp32/uiflow_block_unit_poesp32_mqtt_unsubscribe.svg">

```python
print((str('mqtt:') + str((poesp32_0.unsubscribe_mqtt('')))))
```

- 获取取消订阅状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/poesp32/uiflow_block_unit_poesp32_receive_tcp_packet.svg">

```python
def poesp32_dFAnAcb(value):
  global poesp32_tcp_value1
  poesp32_tcp_value1 = value
  pass

poesp32_0.receive_tcp_packet(poesp32_dFAnAcb)
```

- 接收 TCP 数据包

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/poesp32/uiflow_block_unit_poesp32_send_tcp_packet.svg">

```python
print(poesp32_0.send_tcp_packet('12345'))
```

- 发送 TCP 数据包
