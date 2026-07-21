# [Unit Finger](/zh_CN/unit/finger)

## 案例程序

> 录入并识别指纹

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/finger/uiflow_block_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import time
import unit

setScreenColor(0x222222)
finger_0 = unit.get(unit.FINGER, unit.PORTE)

label1 = M5TextBox(23, 69, "Text", lcd.FONT_Default, 0xFFFFFF, rotate=0)
title0 = M5Title(title="FINGERPRINT", x=3, fgcolor=0xFFFFFF, bgcolor=0x0000FF)

def finger_0_cb(user_id, access):
  # global params
  if (access) == 1 and (user_id) == 1:
    rgb.setColorAll(0x33ff33)
    wait(1)
    rgb.setColorAll(0x000000)
  pass
finger_0.readFingerCb(callback=finger_0_cb)

def buttonA_wasPressed():
  # global params
  finger_0.removeAllUser()
  pass
btnA.wasPressed(buttonA_wasPressed)

def buttonB_wasPressed():
  # global params
  finger_0.addUser(1, 1)
  pass
btnB.wasPressed(buttonB_wasPressed)

while True:
  label1.setText(str(finger_0.state))
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/finger/uiflow_block_finger_uart_init.svg">

```python
finger_0.uart_port_id(1)
```

- 设置核心部件 ID

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/finger/uiflow_block_finger_add_user.svg">

```python
finger_0.addUser(1, 1)
```

- 添加 ID 和访问权限

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/finger/uiflow_block_finger_getUnknown.svg">

```python
def finger_0_unknownCb():
  # global params
  pass
finger_0.getUnknownCb(finger_0_unknownCb)
```

- 未知的 id 及权限执行以下操作(回调函数)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/finger/uiflow_block_finger_get_access.svg">

```python
print(access)
```

- 返回访问权限

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/finger/uiflow_block_finger_get_id.svg">

```python
print(user_id)
```

- 返回 ID

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/finger/uiflow_block_finger_get_state.svg">

```python
print(finger_0.state)
```

- 读取传感器状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/finger/uiflow_block_finger_read.svg">

```python
def finger_0_cb(user_id, access):
  # global params
  pass
finger_0.readFingerCb(callback=finger_0_cb)
```

- 添加 ID 和访问权限(回调函数)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/finger/uiflow_block_finger_removeAll.svg">

```python
finger_0.removeAllUser()
```

- 移除所有指纹信息

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/finger/uiflow_block_finger_remove_user.svg">

```python
移出指纹 ID
```

- 移出指纹 ID

