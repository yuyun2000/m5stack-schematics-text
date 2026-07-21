# [Base X](/zh_CN/base/basex)

#> 在正常模式下设置电机 M1 的速度，在位置模式下设置目标位置，在速度模式下设置目标速度，并在每个模式下实时打印电机的编码器值

## 案例程序

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/basex/uiflow_block_basex_demo.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import module

import time

setScreenColor(0x222222)

mode = None

base_x = module.get(module.BASE_X)

while True:
  print((str('') + str((base_x.get_encoder(1)))))
  base_x.set_mode(1, base_x.NORMAL_MODE)
  base_x.set_motor_speed(1, 100)
  wait(1)
  print((str('') + str((base_x.get_encoder(1)))))
  base_x.set_mode(1, base_x.POSITION_MODE)
  base_x.set_position_pid_max_speed(1, 50)
  base_x.set_position_point(1, 1000)
  wait(1)
  print((str('') + str((base_x.get_encoder(1)))))
  base_x.set_mode(1, base_x.SPEED_MODE)
  base_x.set_speed_point(1, 100)
  wait(1)
  wait_ms(2)

```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/basex/uiflow_block_basex_get_encoder.svg">

```python
base_x.get_encoder(1)
```

- 获取电机的编码器值，返回的是编码器的当前读数

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/basex/uiflow_block_basex_get_speed_20ms.svg">

```python
base_x.get_speed_20ms(1)
```

- 在20毫秒的时间间隔内获取电机的速度，返回的是电机在此时间段内的速度值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/basex/uiflow_block_basex_run_ahead.svg">

```python
base_x.run_ahead(1, 0)
```

- 设置电机提前运行的距离或角度，参数为整数值0，指定电机提前运行的步数或距离

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/basex/uiflow_block_basex_set_encoder.svg">

```python
base_x.set_encoder(1, 0)
```

- 将电机的编码器值设置为指定的整数值0，通常用于重置编码器的当前值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/basex/uiflow_block_basex_set_mode.svg">

```python
base_x.set_mode(1, base_x.NORMAL_MODE)
```

- 将电机设置为正常模式，以正常运行模式操作电机

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/basex/uiflow_block_basex_set_motor_speed.svg">

```python
base_x.set_motor_speed(1, 0)
```

- 设置电机的速度。输入的值0表示将电机速度设置为0，即停止电机的运行

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/basex/uiflow_block_basex_set_position_pid_max_speed.svg">

```python
base_x.set_position_pid_max_speed(1, 0)
```

- 设置电机的位置 PID 控制的最大速度。输入的值0表示在位置控制时，电机的最大速度被限制为0

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/basex/uiflow_block_basex_set_position_point.svg">

```python
base_x.set_position_point(1, 0)
```

- 设置电机的位置点。输入的值0表示将电机的目标位置设置为0点

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/basex/uiflow_block_basex_set_servo_angle.svg">

```python
base_x.set_servo_angle(1, 0)
```

- 设置舵机的角度。输入的值0表示将舵机角度设置为0度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/basex/uiflow_block_basex_set_servo_pulse.svg">

```python
base_x.set_servo_pulse(1, 0)
```

- 设置舵机的脉冲宽度。输入的值0表示将舵机的脉冲宽度设置为0

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/basex/uiflow_block_basex_set_speed_point.svg">

```python
base_x.set_speed_point(1, 0)
```

- 设置电机的目标速度点。输入的值0表示将电机的目标速度设置为0，即电机将不运行或停止运行

