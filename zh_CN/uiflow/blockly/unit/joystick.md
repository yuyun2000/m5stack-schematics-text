# [Unit Joystick](/zh_CN/unit/joystick)

## 案例程序

> 获取操纵杆的当前状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/joystick/uiflow_block_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import time
import unit

setScreenColor(0x222222)
joystick_0 = unit.get(unit.JOYSTICK, unit.PORTA)

while True:
  print(joystick_0.X)
  print(joystick_0.Y)
  print(joystick_0.Press)
  wait(0.2)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/joystick/uiflow_block_joystick_press.svg">

```python
print(joystick_0.Press)
```

- Get is pressed 返回按键的值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/joystick/uiflow_block_joystick_reversal_x.svg">

```python
print(joystick_0.InvertX)
```

- Get Reverse X 返回 X 轴反向数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/joystick/uiflow_block_joystick_reversal_y.svg">

```python
print(joystick_0.InvertY)
```

- Get Reverse Y 返回 Y 轴反向数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/joystick/uiflow_block_joystick_x.svg">

```python
print(joystick_0.X)
```

- Get X 返回 X 轴的数据

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/joystick/uiflow_block_joystick_y.svg">

```python
print(joystick_0.Y)
```

- Get Y 返回 Y 轴的数据

