# [Unit Button](/zh_CN/unit/button)

## 案例程序

> 输出按钮状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/button/uiflow_block_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import unit

setScreenColor(0x222222)
button_0 = unit.get(unit.BUTTON, unit.PORTB)

while True:
  if button_0.wasPressed():
    print('Pressed')
  else:
    print('Released')
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/button/uiflow_block_unit_button_callback.svg">

```python
def button_0_wasPressed_cb():
  # global params
  pass
button_0.wasPressed(button_0_wasPressed_cb)

```

- 回调函数(触发按钮)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/button/uiflow_block_unit_button_state.svg">

```python
print((str('status:') + str((button_0.wasPressed()))))
```

- 获取按钮触发后的状态
