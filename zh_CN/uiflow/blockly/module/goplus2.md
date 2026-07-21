# [Module13.2 GoPlus2](/zh_CN/module/goplus2)

## 案例程序

每秒切换4个舵机的角度值，和变化电机的速度和转动方向

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/goplus2/uiflow_block_go_plus2_demo.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import module

import time

setScreenColor(0x222222)

go_plus_2 = module.get(module.GOPLUS2)

label1 = M5TextBox(0, 81, "btnA: Set up Servo and MA", lcd.FONT_UNICODE, 0x19fe46, rotate=0)
label2 = M5TextBox(0, 123, "btnB: Set up Servo and MB", lcd.FONT_UNICODE, 0xfe6019, rotate=0)
title0 = M5Title(title="GoPlus 2", x=125, fgcolor=0xFFFFFF, bgcolor=0x0000FF)

def buttonA_wasPressed():
  # global params
  pass
btnA.wasPressed(buttonA_wasPressed)

def buttonB_wasPressed():
  # global params
  pass
btnB.wasPressed(buttonB_wasPressed)

while True:
  go_plus_2.set_servo_angle(go_plus_2.S1, 180)
  go_plus_2.set_servo_angle(go_plus_2.S2, 0)
  go_plus_2.set_servo_angle(go_plus_2.S3, 90)
  go_plus_2.set_servo_angle(go_plus_2.S4, 45)
  go_plus_2.set_motor_speed(go_plus_2.MB, 0)
  go_plus_2.set_motor_speed(go_plus_2.MA, 127)
  wait(1)
  go_plus_2.set_servo_plus(go_plus_2.S1, 800)
  go_plus_2.set_servo_plus(go_plus_2.S2, 1500)
  go_plus_2.set_servo_plus(go_plus_2.S3, 500)
  go_plus_2.set_servo_plus(go_plus_2.S4, 2500)
  go_plus_2.set_motor_speed(go_plus_2.MA, 0)
  go_plus_2.set_motor_speed(go_plus_2.MB, (-127))
  wait(1)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/goplus2/uiflow_block_go_plus2_analog_read.svg">

```python
go_plus_2.analog_read(go_plus_2.PB1)
```

- 读取引脚的模拟值。返回一个表示电压的模拟值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/goplus2/uiflow_block_go_plus2_digital_read.svg">

```python
go_plus_2.digital_read(go_plus_2.PB1)
```

- 读取引脚的数字值。返回一个表示高或低状态的数字值

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/goplus2/uiflow_block_go_plus2_digital_write.svg">

```python
go_plus_2.digital_write(go_plus_2.PB1, 0)
```

- 将引脚设置为数字输出0(低电平)

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/goplus2/uiflow_block_go_plus2_set_motor_speed.svg">

```python
 go_plus_2.set_motor_speed(go_plus_2.MA, 0)
```

- 设置电机的速度。速度值可以是正或负，用于控制电机的转速和方向

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/goplus2/uiflow_block_go_plus2_set_servo_angle.svg">

```python
go_plus_2.set_servo_angle(go_plus_2.S1, 0)
```

- 设置舵机 S1的角度为0。角度值可以在舵机的范围内，用于控制舵机的位置

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/goplus2/uiflow_block_go_plus2_set_servo_plus.svg">

```python
 go_plus_2.set_servo_plus(go_plus_2.S1, 500)
```

- 通过增加指定的增量值来调整舵机的位置(PWM)

