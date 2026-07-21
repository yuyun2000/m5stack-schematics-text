# [Unit Limit](/zh_CN/unit/Unit%20Limit)

## 案例程序

> 输出按钮状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/limit/uiflow_block_examle.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import unit

setScreenColor(0x222222)
limit_0 = unit.get(unit.LIMIT, unit.PORTB)

while True:
  if limit_0.get_switch_status():
    print((str('Button:') + str((limit_0.get_switch_status()))))
  else:
    print((str('Button:') + str((limit_0.get_switch_status()))))
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/limit/uiflow_block_unit_limit_get_switch_status.svg">

```python
print((str('status:') + str((limit_0.get_switch_status()))))
```

- 获取当前按钮状态

