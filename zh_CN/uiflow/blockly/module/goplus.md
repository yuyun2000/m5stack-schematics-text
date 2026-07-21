# Module13.2 GoPlus

## 案例程序

打印引脚的模拟值和电压值，然后设置直流电机每间隔一秒一最大速度转动一次，舵机由0°和180°之前来回切换

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/goplus/uiflow_block_go_plus_demo.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import module

import time

setScreenColor(0x222222)

go_plus = module.get(module.GOPLUS)

go_plus.set_motor_speed(1, 0)
while True:
  print(go_plus.digital_read(go_plus.PB1, 0))
  print(go_plus.analog_read(go_plus.PB1))
  go_plus.set_motor_speed(1, 0)
  go_plus.set_servo(0, 0)
  wait(1)
  go_plus.set_motor_speed(1, 127)
  go_plus.set_servo(0, 180)
  wait(1)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/goplus/uiflow_block_go_plus_analog_read.svg">

```python
go_plus.analog_read(go_plus.PB1)
```

- 读取引脚的模拟值。返回一个表示电压的模拟值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/goplus/uiflow_block_go_plus_digital_read.svg">

```python
go_plus.digital_read(go_plus.PB1, 0)
```

- 读取引脚的数字值。返回一个表示高或低状态的数字值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/goplus/uiflow_block_go_plus_set_motor_speed.svg">

```python
 go_plus.set_motor_speed(1, 0)
```

- 设置电机的速度。速度值可以是正或负，用于控制电机的转速和方向

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/goplus/uiflow_block_go_plus_set_servo.svg">

```python
go_plus.set_servo(0, 0)
```

- 设置舵机的角度。角度值可以在舵机的范围内，用于控制舵机的位置

