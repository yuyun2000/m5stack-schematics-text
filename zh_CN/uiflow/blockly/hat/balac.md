
# [Hat Balac](/zh_CN/app/balac)

## 案例程序

控制 balac 前进，左右转弯以及后退

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/balac/uiflow_block_balac_demo.svg">

```python
from m5stack import *
from m5ui import *
from uiflow import *
import time
import hat

setScreenColor(0x111111)

balac = hat.get(hat.BALAC)

balac.set_motor_speed(1, 50)
balac.set_motor_speed(2, 50)
wait(1)
balac.set_motor_speed(1, 50)
balac.set_motor_speed(2, 0)
wait(1)
balac.set_motor_speed(1, 0)
balac.set_motor_speed(2, 50)
wait(1)
balac.set_motor_speed(1, -50)
balac.set_motor_speed(2, -50)
wait(1)
balac.stop_motor(1)
wait(1)
```

## 功能说明

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/balac/uiflow_block_hat_balac_set_motor_speed.svg">

```python
balac.set_motor_speed(1, 50)
```

- 设置直流电机 A 的速度，当前速度为50,最大255

<img class="blockly_svg" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/blockly/hat/balac/uiflow_block_hat_balac_stop_motor.svg">

```python
balac.stop_motor(1)
```

- 停止直流电机 A 的运行

