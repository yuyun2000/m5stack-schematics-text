# [Module DC Motor](/zh_CN/module/lego_plus)

## 案例程序

控制四个直流电机顺时针旋转一段时间，然后逆时针旋转，最后停止所有电机

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/dc_motor/uiflow_block_dc_motor_demo.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import module

import time

setScreenColor(0x111111)

lego_motor = module.get(module.LEGO)
LegoM1 = NXT_Motor(1)
LegoM2 = NXT_Motor(2)
LegoM3 = NXT_Motor(3)
LegoM4 = NXT_Motor(4)
while True:
  lego_motor.M1.set_pwm(180)
  lego_motor.M2.set_pwm(180)
  lego_motor.M3.set_pwm(180)
  lego_motor.M4.set_pwm(180)
  wait(1)
  lego_motor.M1.set_pwm(-180)
  lego_motor.M2.set_pwm(-180)
  lego_motor.M3.set_pwm(-180)
  lego_motor.M4.set_pwm(-180)
  wait(1)
  lego_motor.M1.stop()
  lego_motor.M2.stop()
  lego_motor.M3.stop()
  lego_motor.M4.stop()
  wait(1)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/dc_motor/uiflow_block_lego_clear.svg">

```python
lego_motor.M1.encode_clear()
```

- 清除或重置与直流电机关联的编码器值。编码器值通常用于跟踪电机的转动位置

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/dc_motor/uiflow_block_lego_read_encoder.svg">

```python
lego_motor.M1.encoder_read()
```

- 读取直流电机的编码器值。编码器值通常以一个整数形式返回，表示电机已经转动的角度或步数

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/dc_motor/uiflow_block_lego_set_pwm.svg">

```python
lego_motor.M1.set_pwm(0)
```

- 设置直流电机的转动方向和 PWM(脉宽调制)值。方向可以设置为顺时针(clockwise)或逆时针(counterclockwise)，PWM 值控制电机的转速，范围通常为 0 到 255

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/modules/dc_motor/uiflow_block_lego_stop.svg">

```python
lego_motor.M1.stop()
```

- 停止直流电机的转动
