# [Unit 4Relay](/zh_CN/unit/4relay)

## 案例程序

> 设置指定通道继电器状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/4relay/uiflow_block_relay4_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import time
import unit

setScreenColor(0x222222)
relay4_0 = unit.get(unit.RELAY4, unit.PORTA)

relay4_0.set_mode(1)
while True:
  relay4_0.set_relay_status(1, 1)
  relay4_0.set_relay_status(2, 1)
  relay4_0.set_relay_status(3, 1)
  relay4_0.set_relay_status(4, 1)
  wait(1)
  relay4_0.set_relay_status(1, 0)
  relay4_0.set_relay_status(2, 0)
  relay4_0.set_relay_status(3, 0)
  relay4_0.set_relay_status(4, 0)
  wait(1)
  wait_ms(2)
```

## 功能说明


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/4relay/uiflow_block_relay4_set_mode.svg">

```python
relay4_0.set_mode(1)
```

- 设置 Relay LED 跟随模式：
  - 1:LED 跟随 Relay 状态变化
  - 0:LED 不跟随 Relay 状态变化


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/4relay/uiflow_block_relay4_set_status.svg">

```python
relay4_0.set_relay_status(ch, status)
```

- 设置 Relay 状态：
  - ch:
    - 1-4
  - status:
    - 1:on
    - 0:off


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/4relay/uiflow_block_relay4_set_led_status.svg">

```python
relay4_0.set_led_status(ch, status)
```

- 设置 LED 状态：
  - ch:
    - 1-4
  - status:
    - 1:on
    - 0:off


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/4relay/uiflow_block_relay4_get_mode.svg">

```python
relay4_0.get_mode()
```

- 读取 Relay LED 跟随模式状态：
  - 1:LED 跟随 Relay 状态变化
  - 0:LED 不跟随 Relay 状态变化


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/4relay/uiflow_block_relay4_get_status.svg">

```python
relay4_0.get_relay_status(ch)
```

- 读取继电器状态：
  - ch:
    - 1-4
- 返回值 status:
  - 1:on
  - 0:off


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/4relay/uiflow_block_relay4_get_led_status.svg">

```python
relay4_0.get_led_status(ch)
```

- 读取 LED 状态：
  - ch:
    - 1-4
- 返回值 status:
  - 1:on
  - 0:off

