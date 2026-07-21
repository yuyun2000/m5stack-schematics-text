# [Unit Relay](/zh_CN/unit/relay)

## 案例教程

每隔一秒改变继电器状态（ON/OF）

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/relay/uiflow_relay_example.svg">

```python
from m5stack import *
from m5stack_ui import *
from uiflow import *
import time
import unit

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
relay_0 = unit.get(unit.RELAY, unit.PORTB)

while True:
  relay_0.on()
  print('Relay ON')
  wait(1)
  relay_0.off()
  print('Relay OFF')
  wait(1)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/relay/uiflow_block_set_relay_off.svg">

```python
relay_0.off()
```

- 设置公共端连接为断开状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/relay/uiflow_block_set_relay_on.svg">

```python
relay_0.on()
```

- 设置公共端连接为接通状态

