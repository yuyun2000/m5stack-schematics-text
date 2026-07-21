# [Unit Grove to Grove](/zh_CN/unit/unit_grove2grove)

## 案例程序

> 点击按钮，控制 GROVE 的连接与阻断

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/grove2grove/uiflow_block_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import time
import unit

setScreenColor(0x252525)
grove_0 = unit.get(unit.GROVE2GROVE, unit.PORTB)

title0 = M5Title(title="UNIT GROVE2GROVE", x=84, fgcolor=0xFFFFFF, bgcolor=0x000000)

def buttonA_wasPressed():
  # global params
  grove_0.grove_Ctrl_Status(1)
  pass
btnA.wasPressed(buttonA_wasPressed)

def buttonB_wasPressed():
  # global params
  grove_0.grove_Ctrl_Status(0)
  pass
btnB.wasPressed(buttonB_wasPressed)

while True:
  if grove_0.grove_Ctrl_Status():
    print('is turn on')
  else:
    print('is turn off')
  print((str('Ameter') + str(((str((grove_0.grove_Ameter())) + str('mA'))))))
  wait_ms(1)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/grove2grove/uiflow_block_unit_grove_get_ameter.svg">

```python
print(grove_0.grove_Ameter())
```

- 获取当前 Unit 检测的电流(mA)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/grove2grove/uiflow_block_unit_grove_get_status.svg">

```python
print(grove_0.grove_Ctrl_Status())
```

- 获取当前 Unit 状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/grove2grove/uiflow_block_unit_grove_set_pin.svg">

```python
grove_0.grove_Ctrl_Status(1)
```

- 设置 Unit 状态
  - ON
  - OFF

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/grove2grove/uiflow_block_unit_grove_set_vref.svg">

```python
grove_0.grove_Set_Vref()
```

- 设置 0 mA 参考电流

