# Unit Servo

## 案例程序

启动电机

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/servo/uiflow_servo_example.svg">

```python
from m5stack import *
from m5stack_ui import *
from uiflow import *
import unit

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)
servo_0 = unit.get(unit.SERVO, unit.PORTC)

servo_0.write_angle(0)
servo_0.write_us(600)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/servo/uiflow_block_servo_unit_write_angle.svg">

```python
servo_0.write_angle(0)
```

- 设置零度转角

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/unit/servo/uiflow_block_servo_unit_write_us.svg">

```python
servo_0.write_us(600)
```

- 设置脉冲

