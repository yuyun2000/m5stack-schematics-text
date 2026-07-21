# [Module Servo](/zh_CN/module/servo)

## 案例程序

设置舵机按任意 0~180 角度旋转

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/servo/uiflow_block_servo_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import module

import time

setScreenColor(0x222222)
i = None

servo = module.get(module.SERVO)

import random

while True:
  i = random.randint(0, 180)
  servo.write_angle(0, i)
  servo.write_angle(1, i)
  servo.write_angle(2, i)
  servo.write_angle(3, i)
  servo.write_angle(4, i)
  servo.write_us(0, 600)
  print((str("Servo's Status") + str(i)))
  wait(0.5)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/servo/uiflow_block_servo_angle.svg">

```python
servo.write_angle(0, 180)
```

- 驱动舵机旋转角度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/servo/uiflow_block_servo_write.svg">

```python
servo.write_us(0, 600)
```

- 驱动舵机脉冲时长

