# [Unit Dual Button](/zh_CN/unit/dual_button)

## 案例程序

> 输出按钮状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/dual_button/uiflow_block_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import unit

setScreenColor(0x222222)
dual_button_0 = unit.get(unit.DUAL_BUTTON, unit.PORTB)

while True:
  if dual_button_0.btnBlue.wasPressed():
    rgb.setColorAll(0x000099)
    print('Blue button pressed')
  elif dual_button_0.btnRed.wasPressed():
    rgb.setColorAll(0xcc0000)
    print('Red button pressed')
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/dual_button/uiflow_block_unit_dual_button_callback.svg">

```python
def btnRed0_wasPressed():
  # global params
  pass
dual_button_0.btnRed.wasPressed(btnRed0_wasPressed)
```

- 回调函数(触发按钮)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/dual_button/uiflow_block_unit_dual_button_state.svg">

```python
print((str('status:') + str((dual_button_0.btnRed.wasPressed()))))
```

- 获取按钮触发后的状态

