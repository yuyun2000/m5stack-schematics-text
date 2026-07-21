# [Unit Fan](/zh_CN/unit/unit_fan)

## 案例程序

启动电机

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/fan/uiflow_fan_example.svg">

```python
from m5stack import *
from m5stack_ui import *
from uiflow import *
import unit

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
fan_0 = unit.get(unit.FAN, unit.PORTB)

while True:
  fan_0.on(10)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/fan/uiflow_block_fan_off.svg">

```python
fan_0.off()
```

- 关闭电机

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/fan/uiflow_block_fan_on.svg">

```python
fan_0.on(10)
```

- 设置电机的占空比

