# [Hat Roverc](/zh_CN/hat/hat-powerc)

## 案例程序

循环控制 RoverC 的车轮速度和方向，使其在不同方向上移动并等待1秒

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/roverc/uiflow_block_hat_roverc_demo.png">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import time
import hat

setScreenColor(0x111111)

hat_roverc_0 = hat.get(hat.ROVERC)

while True:
  hat_roverc_0.SetAllPulse(20, 20, 20, 20)
  wait(1)
  hat_roverc_0.SetSpeed(0, (-20), 0)
  wait(1)
  hat_roverc_0.SetAllPulse(20, (-20), (-20), 20)
  wait(1)
  hat_roverc_0.SetSpeed((-20), 0, 0)
  wait(1)
  wait_ms(2)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/roverc/uiflow_block_hat_roverc_set_all_pulse.svg">

```python
hat_roverc_0.SetAllPulse(0, 0, 0, 0)
```

- 设置 RoverC 的前左、前右、后左、后右四个轮子的脉冲宽度，控制每个轮子的动作

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/roverc/uiflow_block_hat_roverc_set_pulse.svg">

```python
hat_roverc_0.SetPulse(0, 0)
```

- 设置单个指定轮子的脉冲宽度，这里指定了前左轮

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/roverc/uiflow_block_hat_roverc_set_servo_angle.svg">

```python
hat_roverc_0.SetServoAngle(0, 0)
```

- 设置指定舵机的位置角度，数值代表舵机的旋转角度

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/roverc/uiflow_block_hat_roverc_set_servo_pulse.svg">

```python
hat_roverc_0.SetServoPulse(0, 500)
```

- 设置指定舵机的脉冲宽度，控制舵机的动作

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/roverc/uiflow_block_hat_roverc_set_speed.svg">

```python
hat_roverc_0.SetSpeed(0, 0, 0)
```

- 设置 RoverC 的移动速度，分别控制 X、Y、Z 轴上的移动速度

