# [Unit Key](/zh_CN/unit/key)

## 案例程序

按下按钮，测试按键

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/key/uiflow_key_example.svg">

```python
from m5stack import *
from m5stack_ui import *
from uiflow import *
import unit

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
key_0 = unit.get(unit.KEY, unit.PORTB)

key_0.set_color(0xff0000, 50)
while True:
  if key_0.get_switch_status():
    print((str('status:') + str((key_0.get_switch_status()))))
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/key/uiflow_block_unit_key_get_switch_status.svg">

```python
print((str('status:') + str((key_0.get_switch_status()))))
```

- 获取按键开关状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/key/uiflow_block_unit_key_set_color.svg">

```python
key_0.set_color(0xff0000, 50)
```

- 设置按键颜色

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/key/uiflow_block_unit_key_set_color_input.svg">

```python
key_0.set_color(0xff0000, 50)
```

- 设置按键颜色
 - Palette
 - RGB
 - HEX

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/key/uiflow_block_unit_key_set_rgb_color.svg">

```python
key_0.set_color(0x000000, 50)
```

- 设置按键RGB颜色

