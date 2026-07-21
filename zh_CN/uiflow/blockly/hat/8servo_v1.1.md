# [Hat 8Servo V1.1](/zh_CN/hat/hat_8servos_1.1)

## 案例程序

控制多个舵机循环每隔一秒转动一个角度，你可以继续添加舵机数量

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/8servo_v1.1/uiflow_block_8servov1.1_demo.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import time
import hat

setScreenColor(0x111111)

hat_servos_1 = hat.get(hat.SERVOS)

hat_8servos_2.set_pwr_ctrl(1)
while True:
  .write_servo_angle(1,0)
  hat_8servos_2.write_servo_angle(2,0)
  hat_8servos_2.write_servo_angle(3,0)
  hat_8servos_2.write_servo_angle(4,0)
  wait(1)
  hat_8servos_2.write_servo_angle(1,90)
  hat_8servos_2.write_servo_angle(2,90)
  hat_8servos_2.write_servo_angle(3,90)
  hat_8servos_2.write_servo_angle(4,90)
  wait(1)
  hat_8servos_2.write_servo_angle(1,180)
  hat_8servos_2.write_servo_angle(2,180)
  hat_8servos_2.write_servo_angle(3,180)
  hat_8servos_2.write_servo_angle(4,180)
  wait(1)
  hat_8servos_2.write_servo_angle(1,90)
  hat_8servos_2.write_servo_angle(2,90)
  hat_8servos_2.write_servo_angle(3,90)
  hat_8servos_2.write_servo_angle(4,90)
  wait(1)
  hat_8servos_2.write_servo_angle(1,0)
  hat_8servos_2.write_servo_angle(2,0)
  hat_8servos_2.write_servo_angle(3,0)
  hat_8servos_2.write_servo_angle(4,0)
  wait(1)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/8servo_v1.1/uiflow_block_hat_8servo_get_power_control.svg">

```python
hat_8servos_1.get_pwr_ctrl()
```

- 获取舵机电源控制状态

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/8servo_v1.1/uiflow_block_hat_8servo_read_servo_angle.svg">

```python
hat_8servos_1.read_servo_angle(1)
```

- 读取指定通道的舵机角度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/8servo_v1.1/uiflow_block_hat_8servo_read_servo_pulse.svg">

```python
hat_8servos_1.read_servo_pulse(1)
```

- 读取指定通道的舵机脉冲

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/8servo_v1.1/uiflow_block_hat_8servo_set_power_control.svg">

```python
hat_8servos_1.set_pwr_ctrl(1)
```

- 设置舵机的电源控制

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/8servo_v1.1/uiflow_block_hat_8servo_write_servo_angle.svg">

```python
hat_8servos_1.write_servo_angle(1,0)
```

- 设置指定通道的舵机角度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/8servo_v1.1/uiflow_block_hat_8servo_write_servo_pulse.svg">

```python
hat_8servos_1.write_servo_pulse(1,500)
```

- 设置指定通道的舵机脉冲

