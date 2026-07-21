# [Atom Socket](/zh_CN/atom/atom_socket)

## 案例程序

这个程序通过 MQTT 协议进行远程控制，监测负载的电压、电流和功率，并在 AP 模式下启动 Web 服务器以轮询数据。按下按钮 A 时，切换继电器状态(开/关)，并更新 RGB 灯的颜色指示状态。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/socket/uiflow_block_atomic_base_socket_demo.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
from base.Socket_Kit import Socket
import time

button_next = None

sock = Socket()

from numbers import Number

def buttonA_wasPressed():
  global button_next
  button_next = (button_next if isinstance(button_next, Number) else 0) + 1
  if button_next == 1:
    sock.set_relay_state(1)
  elif button_next == 2:
    sock.set_relay_state(0)
    button_next = 0
  pass
btnA.wasPressed(buttonA_wasPressed)

button_next = 0
sock.remote_control(1)
print(sock.pub_topic)
print((str('This is Subscribe Topic(Relay State), Use Remote User: ') + str((sock.sub_topic_relay))))
print((str('This is Subscribe Topic(Parameter Status), Use Remote User: ') + str((sock.sub_topic_data))))
while True:
  if sock.wait_update_data():
    print((str('Voltage(V): ') + str((sock.get_voltage()))))
    print((str('Current(mA): ') + str((sock.get_current()))))
    print((str('Power(W): ') + str((sock.get_active_power()))))
    sock.server_loop()
    wait(1)
  button_next = int((sock.get_relay_status()))
  if button_next:
    rgb.setColorAll(0x009900)
  else:
    rgb.setColorAll(0xff0000)
  wait_ms(2)

```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/socket/uiflow_block_atom_socket_kit_get_publish_topic.svg">

```python
sock.pub_topic
```

- 获取设备发送数据的主题(Topic)。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/socket/uiflow_block_atom_socket_kit_get_subscribe_topic.svg">

```python
sock.sub_topic_relay
```

- 获取设备的订阅主题，设备会接收该主题下发布的消息。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/socket/uiflow_block_atom_socket_kit_load_active_power.svg">

```python
sock.get_active_power()
```

- 获取设备当前的负载有功功率。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/socket/uiflow_block_atom_socket_kit_load_current.svg">

```python
sock.get_current()
```

- 获取设备当前负载的电流。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/socket/uiflow_block_atom_socket_kit_load_voltage.svg">

```python
sock.get_voltage()
```

- 获取设备当前负载的电压。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/socket/uiflow_block_atom_socket_kit_relay_status.svg">

```python
sock.get_relay_status()
```

- 获取设备继电器的当前状态(开/关)。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/socket/uiflow_block_atom_socket_kit_remote_control.svg">

```python
sock.remote_control(1)
```

- 设置设备的远程控制模式，这里设定为 MQTT。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/socket/uiflow_block_atom_socket_kit_server_loop.svg">

```python
sock.server_loop()
```

- 在设备工作在 AP 模式下时，启用一个 Web 服务器轮询循环。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/socket/uiflow_block_atom_socket_kit_set_relay_state.svg">

```python
sock.set_relay_state(1)
```

- 设置继电器的状态为"开"(ON)。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/socket/uiflow_block_atom_socket_kit_wait_update_data.svg">

```python
sock.wait_update_data()
```

- 等待设备接收并处理更新的数据。

