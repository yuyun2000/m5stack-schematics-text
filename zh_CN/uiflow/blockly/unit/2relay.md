
# [Unit 2Relay](/zh_CN/unit/2relay)

## 案例程序

> 控制继电器输出状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/2relay/uiflow_block_unit_relay2_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import time
import unit

setScreenColor(0x222222)
relay2_0 = unit.get(unit.RELAY2, unit.PORTA)

while True:
  relay2_0.set_value(3, 1)
  wait(1)
  relay2_0.set_value(3, 0)
  wait(1)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/2relay/uiflow_block_unit_relay2_control.svg">

```python
relay2_0.set_value(ch, status)
```

- 继电器控制：
  - ch:
    - 1:控制继电器1
    - 2:控制继电器2
    - 3:控制所有继电
  - status:
    - 1:on
    - 0:off


