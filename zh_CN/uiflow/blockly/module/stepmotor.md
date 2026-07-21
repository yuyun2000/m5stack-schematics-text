# [Module Stepmotor](/zh_CN/module/stepmotor)

## 案例程序

通过步进电机以设定的速度在 X、Y、Z 三个方向上进行往复移动，每次移动后等待2秒钟

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/stepmotor/uiflow_block_stepmotor_demo.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import module

import time

setScreenColor(0x111111)

label0 = M5TextBox(-7, -11, "STEPMOTOR Example", lcd.FONT_DejaVu24, 0xFFFFFF, rotate=0)

stepmotor1 = module.get(module.STEP_MOTOR, 0x70)
stepmotor1.set_mode("distance")
while True:
  stepmotor1.turn(x=(-10),  y=(-10), z=(-10), speed=300)
  wait(2)
  stepmotor1.turn(x=10,  y=10, z=10, speed=300)
  wait(2)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/stepmotor/uiflow_block_motor_g_code.svg">

```python
stepmotor1.g_code('')
```

- 发送 G 代码指令到步进电机控制器。这通常用于控制步进电机执行复杂的路径或操作

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/stepmotor/uiflow_block_motor_instance.svg">

```python
module.get(module.STEP_MOTOR, 0x70)
```

- 初始化步进电机，设置其 I2C 地址为0x70。这是步进电机与控制器通信的地址

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/stepmotor/uiflow_block_motor_lock.svg">

```python
stepmotor1.lock_motor()
```

- 锁定步进电机，防止电机在未解锁的情况下移动。这通常用于确保电机在执行操作之前处于稳定状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/stepmotor/uiflow_block_motor_move_xyz.svg">

```python
stepmotor1.turn(x=0,  y=0, z=0, speed=0)
```

- 控制步进电机沿 X、Y、Z 三个方向移动，速度由 Speed 参数决定。这个块允许精确控制步进电机的移动

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/stepmotor/uiflow_block_motor_set_mode.svg">

```python
stepmotor1.set_mode("distance")
```

- 设置步进电机的模式为“距离”模式。这意味着电机的移动将基于指定的距离，而非其他模式(如速度模式)。

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/stepmotor/uiflow_block_motor_unlock.svg">

```python
stepmotor1.unlock_motor()
```

- 解锁步进电机，允许电机自由移动。通常在操作完成后使用此块来解锁电机

