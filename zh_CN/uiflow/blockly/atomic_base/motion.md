# [Atomic Motion Base](/zh_CN/atom/Atomic%20Motion%20Base)

## 案例程序

实现电机持续旋转与舵机的周期性摆动

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/motion/uiflow_block_motion_example.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
from base.Motion import Motion
import time

motion = Motion()
motion.set_motor_speed(1, 127)
motion.set_motor_speed(2, -127)
while True:
  motion.set_servo_angle(1, 90)
  motion.set_servo_angle(2, 90)
  motion.set_servo_angle(3, 90)
  motion.set_servo_angle(4, 90)
  wait(1)
  motion.set_servo_angle(1, 180)
  motion.set_servo_angle(2, 180)
  motion.set_servo_angle(3, 180)
  motion.set_servo_angle(4, 180)
  wait(1)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/motion/uiflow_block_motion_init.svg">

```python
from base.Motion import Motion
motion = Motion()
```

- 初始化 Atomic Motion

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/motion/uiflow_block_motion_set_motor_speed.svg">

```python
motion.set_motor_speed(ch, speed)
```

- 控制直流电机转速：
  - ch: 1-2
  - speed: -127 ~ +127, 0为停止

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/motion/uiflow_block_motion_get_motor_speed.svg">

```python
motion.get_motor_speed(ch)
```

- 获取直流电机转速配置：
  - ch: 1-2


<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/motion/uiflow_block_motion_set_servo_angle.svg">

```python
motion.set_servo_angle(ch, angle)
```

- 控制舵机旋转角度
  - ch: 1-4
  - angle: 0-180

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/motion/uiflow_block_motion_get_servo_angle.svg">

```python
motion.get_servo_angle(ch)
```

- 获取舵机旋转角度：
  - ch: 1-4

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/motion/uiflow_block_motion_set_servo_pulse.svg">

```python
motion.set_servo_pulse(ch, pulse)
```

- 控制舵机脉冲时间(us)
  - ch: 1-4
  - pulse: 500-2500

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/atomic_base/motion/uiflow_block_motion_get_servo_pulse.svg">

```python
motion.get_servo_pulse(ch)
```

- 获取舵机脉冲时间(us):
  - ch: 1-4

