# [Unit Angle](/zh_CN/unit/angle)

## 案例程序

获取旋钮值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/angle/uiflow_angle_example.svg">

```python
from m5stack import *
from m5stack_ui import *
from uiflow import *
import time
import unit

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
angle_0 = unit.get(unit.ANGLE, unit.PORTB)

while True:
  print(angle_0.read())
  wait_ms(10)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/angle/uiflow_block_angle_read.svg">

```python
print((str('value:') + str((angle_0.read()))))
```

- 获取旋钮值

